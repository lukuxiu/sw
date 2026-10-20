import json, re, sys

sys.stdout.reconfigure(encoding='utf-8')

# 1. Load existing extracted_questions.json
with open('scripts/extracted_questions.json', 'r', encoding='utf-8') as f:
    existing_all = json.load(f)

# Keep only non-recent questions (Maki lecture questions, years < 2021)
maki_questions = []
for entry in existing_all:
    qid = entry['item'].get('id', '')
    # Check if it's a recent exam question q-202[1-6]
    if re.match(r'q-(202[1-6])-(\d+)-(\d+)', qid):
        continue
    # Also check source year
    yr = entry['item'].get('year', '')
    if yr in ['2021', '2022', '2023', '2024', '2025', '2026']:
        continue
    maki_questions.append(entry)

print(f"Kept {len(maki_questions)} Maki lecture questions (< 2021).")

# 2. Load cxy questions and deduplicate
with open('scripts/cxy_2021_2026_raw.json', 'r', encoding='utf-8') as f:
    cxy_raw = json.load(f)

# Load existing mapping: (year, sub, qnum) -> topicId
existing_mapping = {}
for entry in existing_all:
    qid = entry['item'].get('id', '')
    tid = entry['topicId']
    m = re.match(r'q-(202[1-6])-(\d+)-(\d+)', qid)
    if m:
        yr = m.group(1)
        sub = '数一' if m.group(2) == '1' else ('数二' if m.group(2) == '2' else '数三')
        qnum = int(m.group(3))
        existing_mapping[(yr, sub, qnum)] = tid

unique_cxy = {}
for q in cxy_raw:
    cid = q.get('id')
    if cid not in unique_cxy:
        unique_cxy[cid] = {
            'cxy_id': cid,
            'stem': q.get('stem', '').strip(),
            'option_a': q.get('option_a', ''),
            'option_b': q.get('option_b', ''),
            'option_c': q.get('option_c', ''),
            'option_d': q.get('option_d', ''),
            'correct_answer': q.get('correct_answer', '').strip(),
            'answer_explanation': q.get('answer_explanation', '').strip(),
            'source': q.get('source', '').strip(),
            'original_source': q.get('original_source', '').strip(),
            'category_full_path': q.get('category_full_path', '').strip(),
            'papers': []
        }
    unique_cxy[cid]['papers'].append((q.get('paper_year'), q.get('paper_subject'), q.get('serial_number')))

print(f"Processed {len(unique_cxy)} unique cxy questions.")

# 3. Format into PastQuestionItem
def format_cxy_item(q):
    papers = q['papers']
    year = papers[0][0]
    
    # Sort papers: 数一, 数二, 数三
    sub_order = {'数一': 1, '数二': 2, '数三': 3}
    papers_sorted = sorted(papers, key=lambda p: (sub_order.get(p[1], 9), p[2]))
    
    # Combined category string
    subs = [p[1] for p in papers_sorted]
    category_str = " / ".join(["数学" + s[1] for s in subs])
    
    # Combined question number
    if len(papers_sorted) == 1:
        qnum_str = f"题{papers_sorted[0][2]}"
    else:
        qnum_str = " · ".join([f"题{p[2]} ({p[1]})" for p in papers_sorted])
        
    # Topic ID
    tid = None
    for p in papers_sorted:
        if p in existing_mapping:
            tid = existing_mapping[p]
            break
    if not tid:
        tid = 'gaoshu-01-indeterminate-0-0' # fallback if any
        
    # Options
    options = None
    if q['option_a']:
        raw_opts = [q['option_a'], q['option_b'], q['option_c'], q['option_d']]
        opts = []
        for opt in raw_opts:
            opt = opt.strip()
            # If math expression not wrapped in $, wrap it
            if not opt.startswith('$') and not re.search(r'[\u4e00-\u9fa5]', opt) and len(opt) > 0:
                opt = f"${opt}$"
            opts.append(opt)
        options = opts
        
    # Solution steps from answer_explanation
    # Split by double newline or numbered paragraphs
    raw_exp = q['answer_explanation']
    paragraphs = [p.strip() for p in re.split(r'\n{2,}', raw_exp) if p.strip()]
    if not paragraphs:
        paragraphs = [raw_exp] if raw_exp else ["详见参考答案与解析。"]
        
    # Analysis
    analysis = f"考查知识点：{q['category_full_path'].replace('历年真题 / ', '')}。"
    if len(paragraphs) > 1 and len(paragraphs[0]) < 120 and not paragraphs[0].startswith('$$'):
        analysis += " " + paragraphs[0]
        solution_steps = paragraphs[1:]
    else:
        solution_steps = paragraphs
        
    if not solution_steps:
        solution_steps = [paragraphs[0]]
        
    # Difficulty
    primary_qnum = papers_sorted[0][2]
    if primary_qnum <= 10:
        difficulty = "★★★☆☆"
    elif primary_qnum <= 16:
        difficulty = "★★★☆☆"
    else:
        difficulty = "★★★★☆"
        
    primary_sub = '1' if '一' in papers_sorted[0][1] else ('2' if '二' in papers_sorted[0][1] else '3')
    item_id = f"q-{year}-{primary_sub}-{primary_qnum}"
    
    item = {
        'id': item_id,
        'year': year,
        'category': category_str,
        'questionNumber': qnum_str,
        'difficulty': difficulty,
        'source': q['source'] or f"{year}年·{category_str}",
        'content': q['stem'],
        'answer': q['correct_answer'],
        'analysis': analysis,
        'solutionSteps': solution_steps,
        'pitfall': "注意审题条件与运算符号，规避常见计算失误。"
    }
    if options:
        item['options'] = options
        
    return tid, item

new_cxy_entries = []
for qid, q in unique_cxy.items():
    tid, item = format_cxy_item(q)
    new_cxy_entries.append({
        'topicId': tid,
        'item': item
    })

print(f"Generated {len(new_cxy_entries)} deduplicated cxy entries.")
total_all = len(maki_questions) + len(new_cxy_entries)
print(f"Total merged questions in database: {total_all} (309 Maki + 306 cxy 2021-2026).")

# Save to test JSON
with open('scripts/merged_questions_test.json', 'w', encoding='utf-8') as f:
    json.dump(maki_questions + new_cxy_entries, f, ensure_ascii=False, indent=2)

print("Saved scripts/merged_questions_test.json successfully!")
