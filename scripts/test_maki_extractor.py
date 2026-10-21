import os, fitz, re, json, sys

sys.stdout.reconfigure(encoding='utf-8')

pdf_path = 'Maki考研数学一站式大串讲 -2026-version 1.0(1).pdf'
doc = fitz.open(pdf_path)

toc = doc.get_toc()

# 1. Map all lectures from TOC
lectures = []
curr_lec = None

part_names = {
    0: "第 0 编 预备",
    1: "第 1 编 一元函数微积分",
    2: "第 2 编 常微分方程与差分方程",
    3: "第 3 编 多元函数微积分",
    4: "第 4 编 无穷级数",
    5: "第 5 编 线性代数",
    6: "第 6 编 概率论与数理统计",
    7: "第 7 编 应试工程"
}

curr_part = 0
for lvl, title, page in toc:
    m_part = re.search(r'第\s*(\d+)\s*编', title)
    if m_part:
        curr_part = int(m_part.group(1))

    m_lec = re.search(r'L(\d+)\s+([^\s\[]+)', title)
    if m_lec:
        lec_num = int(m_lec.group(1))
        # Determine tags from title
        is_key = '重点讲' in title or 'MakiRed重点讲' in title
        is_compressed = '压缩讲' in title or 'MakiGray压缩讲' in title
        is_math1_only = '仅一' in title or 'MakiRed仅一' in title
        is_math2_heavy = '二重' in title or 'MakiOrange二重' in title
        is_math3_only = '仅三' in title or 'MakiGreen仅三' in title
        is_method = lec_num in [1, 2, 28, 53, 64, 65, 66]

        # Clean title
        clean_title = re.sub(r'\[.*?\]', '', title)
        clean_title = re.sub(r'Maki[A-Za-z]+[^\s]*', '', clean_title).strip()
        clean_title = re.sub(r'^L\d+\s*', '', clean_title).strip()

        curr_lec = {
            'num': lec_num,
            'id': f'L{lec_num:02d}',
            'partNum': curr_part,
            'partTitle': part_names.get(curr_part, f"第 {curr_part} 编"),
            'title': clean_title,
            'page': page,
            'isKey': is_key,
            'isCompressed': is_compressed,
            'isMath1Only': is_math1_only,
            'isMath2Heavy': is_math2_heavy,
            'isMath3Only': is_math3_only,
            'isMethod': is_method,
            'subsections': [],
        }
        lectures.append(curr_lec)
    elif lvl >= 3 and curr_lec:
        clean_sub = re.sub(r'\[.*?\]', '', title)
        clean_sub = re.sub(r'Maki[A-Za-z]+[^\s]*', '', clean_sub).strip()
        if clean_sub not in curr_lec['subsections']:
            curr_lec['subsections'].append(clean_sub)

# Deduplicate lectures by num
dedup_lecs = []
seen = set()
for l in lectures:
    if l['num'] not in seen:
        seen.add(l['num'])
        dedup_lecs.append(l)

dedup_lecs.sort(key=lambda x: x['num'])
print(f"Total parsed lectures: {len(dedup_lecs)}")

# Map each lecture's page end
for i in range(len(dedup_lecs)):
    next_page = dedup_lecs[i+1]['page'] if i + 1 < len(dedup_lecs) else len(doc)
    dedup_lecs[i]['pageEnd'] = next_page

# Extract orientation, frequency table, and key methods for each lecture
print("Extracting detailed text, orientation, and tables for all 66 lectures...")

for l in dedup_lecs:
    p_start = l['page'] - 1
    p_end = min(l['pageEnd'], len(doc))
    
    # Read first 3 pages of lecture
    text_sample = ""
    for p in range(p_start, min(p_start + 3, p_end)):
        text_sample += doc[p].get_text() + "\n"

    # Extract orientation
    m_orient = re.search(r'本讲定位[：:](.*?)(?:定理/公式|三卷的基本盘|本讲真题考频|三条局部性质|定义|一、|1\.|\n\n[^\n]{1,10}\n)', text_sample, re.DOTALL)
    if m_orient:
        orient = m_orient.group(1).strip()
        orient = re.sub(r'\s+', ' ', orient)
    else:
        # Fallback orientation
        orient = f"本讲为《Maki考研数学一站式大串讲》第 {l['num']} 讲，系统覆盖 {l['title']} 核心考查点与真题方法。"
    l['orientation'] = orient

    # Extract frequency table if available
    # Search for 本讲真题考频 or similar
    m_freq = re.search(r'本讲真题考频.*?合计\s*(\d+)\s*(\d+)\s*(\d+)\s*(\d+)\s*(\d+)\s*(\d+)\s*(\d+)\s*(\d+)', text_sample)
    if m_freq:
        l['stats'] = {
            'independentQuestions': int(m_freq.group(1)),
            'positions': int(m_freq.group(2)),
            'choiceCount': int(m_freq.group(3)),
            'blankCount': int(m_freq.group(4)),
            'solutionCount': int(m_freq.group(5)),
            'math1Score': int(m_freq.group(6)),
            'math2Score': int(m_freq.group(7)),
            'math3Score': int(m_freq.group(8)),
        }
    else:
        # Search anywhere in the lecture pages for 合计
        # Or estimate from subsections
        l['stats'] = {
            'independentQuestions': 0,
            'positions': 0,
            'choiceCount': 0,
            'blankCount': 0,
            'solutionCount': 0,
            'math1Score': 0,
            'math2Score': 0,
            'math3Score': 0,
        }

    # Extract tags list
    tags = []
    if l['isKey']: tags.append('重点讲')
    if l['isCompressed']: tags.append('压缩讲')
    if l['isMethod']: tags.append('方法课')
    if l['isMath1Only']: tags.append('数一专属')
    if l['isMath2Heavy']: tags.append('数二重点')
    if l['isMath3Only']: tags.append('数三专属')
    if not (l['isMath1Only'] or l['isMath3Only']): tags.append('三卷必考')
    l['tags'] = tags

print("Done extracting basics. Sample lecture L09:")
print(json.dumps(dedup_lecs[8], ensure_ascii=False, indent=2))
