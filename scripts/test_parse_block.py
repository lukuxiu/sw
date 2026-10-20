import os, fitz, re, sys

sys.stdout.reconfigure(encoding='utf-8')
doc0 = fitz.open(sorted([f for f in os.listdir('.') if f.endswith('.pdf')])[0])

l03_text = ""
for pno in range(48, 56):
    l03_text += f"\n" + doc0[pno].get_text()

blocks = re.split(r'\n(?=真题\s*\d+\.\d+)', l03_text)

def parse_question_block(text, source_prefix="Maki 大串讲"):
    lines = [l.strip() for l in text.strip().split('\n') if l.strip()]
    if not lines:
        return None
    qid_m = re.match(r'(?:真题|题)\s*(\d+\.\d+)', lines[0])
    if not qid_m:
        return None
    qid = qid_m.group(0)
    
    # Extract metadata lines (years, categories, question numbers)
    idx = 1
    meta_list = []
    while idx < len(lines):
        m = re.search(r'(20\d\d)\s*[・·]\s*(数[一二三])\s*[・·]\s*(\([^\)]+\)|\d+)', lines[idx])
        if m:
            meta_list.append({
                'year': m.group(1),
                'category': m.group(2),
                'num': m.group(3)
            })
            idx += 1
        elif '跨卷重复' in lines[idx]:
            idx += 1
        else:
            break
            
    # Title & Difficulty
    title = ""
    difficulty = "★★★☆☆"
    if idx < len(lines):
        t_line = lines[idx]
        diff_m = re.search(r'[★☆]{5}', t_line)
        if diff_m:
            difficulty = diff_m.group(0)
            t_line = t_line.replace(difficulty, '').strip()
        t_line = re.sub(r'（习题集[^）]+）', '', t_line).strip()
        title = t_line
        idx += 1
        
    remaining = '\n'.join(lines[idx:])
    
    # Split by section markers
    # Markers: 考点, 解, 答案：, 结论, 易错/ 提醒
    sec_markers = ['考点', '解', '答案[：:]', '结论', '易错[/\s]*提醒']
    pattern = r'\n(?=(?:' + '|'.join(sec_markers) + r'))'
    parts = re.split(pattern, remaining)
    
    content = ""
    analysis = ""
    solution = ""
    answer = ""
    pitfall = ""
    
    if len(parts) > 0:
        content = parts[0].strip()
        
    for p in parts[1:]:
        p_strip = p.strip()
        if p_strip.startswith('考点'):
            analysis = re.sub(r'^考点\s*', '', p_strip).strip()
        elif p_strip.startswith('解'):
            solution = re.sub(r'^解\s*', '', p_strip).strip()
        elif re.match(r'^答案[：:]', p_strip):
            answer = re.sub(r'^答案[：:]\s*', '', p_strip).strip()
        elif p_strip.startswith('结论'):
            pitfall = re.sub(r'^结论\s*', '', p_strip).strip()
        elif re.match(r'^易错[/\s]*提醒', p_strip):
            pitfall = re.sub(r'^易错[/\s]*提醒\s*', '', p_strip).strip()
            
    return {
        'qid': qid,
        'meta_list': meta_list,
        'title': title,
        'difficulty': difficulty,
        'content': content,
        'analysis': analysis,
        'solution': solution,
        'answer': answer,
        'pitfall': pitfall
    }

for b in blocks[1:]:
    res = parse_question_block(b)
    if res:
        print(f"=== {res['qid']} ({res['title']}) ===")
        print(f"Meta: {res['meta_list']}")
        print(f"Difficulty: {res['difficulty']}")
        print(f"Content: {res['content'][:80]}...")
        print(f"Analysis: {res['analysis'][:80]}...")
        print(f"Answer: {res['answer']}")
        print(f"Pitfall: {res['pitfall'][:80]}...")
