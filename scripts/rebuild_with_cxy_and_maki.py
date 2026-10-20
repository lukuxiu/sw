import json, re, sys, unicodedata

sys.stdout.reconfigure(encoding='utf-8')

# 1. Load existing extracted_questions.json
with open('scripts/extracted_questions.json', 'r', encoding='utf-8') as f:
    existing_all = json.load(f)

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

# Keep only Maki lecture questions (< 2021)
maki_questions = []
for entry in existing_all:
    qid = entry['item'].get('id', '')
    if re.match(r'q-(202[1-6])-(\d+)-(\d+)', qid):
        continue
    yr = entry['item'].get('year', '')
    if yr in ['2021', '2022', '2023', '2024', '2025', '2026']:
        continue
    maki_questions.append(entry)

print(f"Loaded {len(maki_questions)} Maki lecture questions (< 2021).")

# 2. Load cxy 2021~2026 raw questions
with open('scripts/cxy_2021_2026_raw.json', 'r', encoding='utf-8') as f:
    cxy_raw = json.load(f)

print(f"Loaded {len(cxy_raw)} raw cxy question entries.")

# Deduplicate by cxy id
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

print(f"Deduplicated to {len(unique_cxy)} unique cxy questions.")

def clean_latex(s):
    if not s or not isinstance(s, str):
        return ""
    # Strip asset attachments and raw answer scans
    s = re.sub(r'###\s*原始参考答案[\s\S]*$', '', s).strip()
    s = re.sub(r'!\[[^\]]*\]\(asset://[^\)]+\)', '', s).strip()
    
    # Replace xlongequal with stackrel
    def replace_xlongequal(m):
        inner = m.group(1).replace(r'\gt', '>').replace(r'\lt', '<').replace('{}', '').strip()
        if re.search(r'[\u4e00-\u9fa5]', inner):
            return f'\\stackrel{{\\text{{{inner}}}}}{{=}}'
        return f'\\stackrel{{{inner}}}{{=}}'

    s = re.sub(r'\\xlongequal\{\s*([^\}]+?)\s*\}', replace_xlongequal, s)
    
    # Clean redundant newlines
    s = re.sub(r'\n{3,}', '\n\n', s)
    return s.strip()

# Format cxy questions into PastQuestionItem
by_topic = {}

# First, populate Maki questions
for entry in maki_questions:
    tid = entry['topicId']
    if tid not in by_topic:
        by_topic[tid] = []
    by_topic[tid].append(entry['item'])

# Next, format and populate CXY questions
for cid, q in unique_cxy.items():
    papers = q['papers']
    year = papers[0][0]
    
    # Sort papers: 数一, 数二, 数三
    sub_order = {'数一': 1, '数二': 2, '数三': 3}
    papers_sorted = sorted(papers, key=lambda p: (sub_order.get(p[1], 9), p[2]))
    
    # Combined category string (e.g. '数一 / 数二 / 数三')
    subs = [p[1] for p in papers_sorted]
    category_str = " / ".join(subs)
    
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
        tid = 'gaoshu-01-indeterminate-0-0'
        
    # Options
    options = None
    if q['option_a']:
        raw_opts = [q['option_a'], q['option_b'], q['option_c'], q['option_d']]
        opts = []
        for opt in raw_opts:
            opt = clean_latex(opt.strip())
            # If math expression not wrapped in $, wrap it
            if not opt.startswith('$') and not re.search(r'[\u4e00-\u9fa5①②③④⑤⑥⑦⑧⑨⑩]', opt) and len(opt) > 0:
                opt = f"${opt}$"
            opts.append(opt)
        options = opts
        
    # Solution steps from answer_explanation
    raw_exp = clean_latex(q['answer_explanation'])
    paragraphs = [p.strip() for p in re.split(r'\n{2,}', raw_exp) if p.strip()]
    if not paragraphs:
        paragraphs = [raw_exp] if raw_exp else ["详见参考答案与解析。"]
        
    # Analysis
    cat_tag = q['category_full_path'].replace('历年真题 / ', '')
    analysis = f"考查知识点：{cat_tag}。"
    if len(paragraphs) > 1 and len(paragraphs[0]) < 120 and not paragraphs[0].startswith('$$') and not paragraphs[0].startswith('\\['):
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
        'content': clean_latex(q['stem']),
        'answer': clean_latex(q['correct_answer']),
        'analysis': analysis,
        'solutionSteps': [clean_latex(s) for s in solution_steps],
        'pitfall': "注意审题条件与运算符号，规避常见计算失误。",
        'verified': True
    }
    if options:
        item['options'] = options
        
    if tid not in by_topic:
        by_topic[tid] = []
    by_topic[tid].append(item)

total_items = sum(len(v) for v in by_topic.values())
print(f"Total topics: {len(by_topic)}, Total questions in DB: {total_items}")

# Write to pastQuestionsData.ts
ts_code = """import { PastQuestionItem } from './types';

/**
 * 考研数学真题全集索引 (包括大串讲经典精解例题 + 2021~2026 年数一/数二/数三全量真题)
 * 直接对标并同步大观园 (cxyonly.fans) 高精度 LaTeX 公式排版，去重数一数二数三共用题，选项徽标网格化呈现。
 */
export const EXTRACTED_PAST_QUESTIONS: Record<string, PastQuestionItem[]> = """

ts_code += json.dumps(by_topic, ensure_ascii=False, indent=2) + ";\n"

with open('src/data/pastQuestionsData.ts', 'w', encoding='utf-8') as f:
    f.write(ts_code)

print("Saved clean src/data/pastQuestionsData.ts successfully!")
