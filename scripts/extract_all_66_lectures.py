import os, fitz, re, json, sys

sys.stdout.reconfigure(encoding='utf-8')

doc = fitz.open('Maki考研数学一站式大串讲 -2026-version 1.0(1).pdf')
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
        curr_lec['subsections'].append(clean_sub)

# Deduplicate lectures by num
dedup_lecs = []
seen = set()
for l in lectures:
    if l['num'] not in seen:
        seen.add(l['num'])
        dedup_lecs.append(l)

dedup_lecs.sort(key=lambda x: x['num'])
print(f"Extracted {len(dedup_lecs)} unique lectures.")

# Let's inspect the first 10
for l in dedup_lecs[:8]:
    print(f"{l['id']}: {l['title']} (Part: {l['partTitle']}, p.{l['page']}, subs: {len(l['subsections'])}, key: {l['isKey']}, comp: {l['isCompressed']})")
