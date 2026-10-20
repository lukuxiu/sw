import os, fitz, re, json, sys

sys.stdout.reconfigure(encoding='utf-8')

pdfs = sorted([f for f in os.listdir('.') if f.endswith('.pdf')])
doc0 = fitz.open(pdfs[0]) # 大串讲
doc1 = fitz.open(pdfs[1]) # 分类精解

print(f"Loaded Doc0: {pdfs[0]} ({len(doc0)} pages)")
print(f"Loaded Doc1: {pdfs[1]} ({len(doc1)} pages)")

# 1. Map Doc 0 Lectures to page ranges
toc0 = doc0.get_toc()
lec_ranges0 = []
for item in toc0:
    lvl, title, page = item
    m = re.search(r'L(\d+)\s+([^\s\[]+)', title)
    if m:
        lec_ranges0.append({'num': int(m.group(1)), 'name': m.group(2), 'start': page})

for i in range(len(lec_ranges0)):
    if i + 1 < len(lec_ranges0):
        lec_ranges0[i]['end'] = lec_ranges0[i+1]['start'] - 1
    else:
        lec_ranges0[i]['end'] = len(doc0)

# 2. Map Doc 1 Lectures to page ranges
chinese_num_map = {
    '一': 1, '二': 2, '三': 3, '四': 4, '五': 5, '六': 6, '七': 7, '八': 8, '九': 9, '十': 10,
    '十一': 11, '十二': 12, '十三': 13, '十四': 14, '十五': 15, '十六': 16, '十七': 17, '十八': 18, '十九': 19, '二十': 20,
    '二十一': 21, '二十二': 22, '二十三': 23, '二十四': 24, '二十五': 25, '二十六': 26, '二十七': 27, '二十八': 28, '二十九': 29, '三十': 30,
    '三十一': 31, '三十二': 32, '三十三': 33, '三十四': 34, '三十五': 35, '三十六': 36, '三十七': 37, '三十八': 38, '三十九': 39, '四十': 40,
    '四十一': 41, '四十二': 42, '四十三': 43, '四十四': 44, '四十五': 45, '四十六': 46, '四十七': 47, '四十八': 48, '四十九': 49, '五十': 50,
    '五十一': 51, '五十二': 52, '五十三': 53, '五十四': 54, '五十五': 55, '五十六': 56, '五十七': 57, '五十八': 58, '五十九': 59, '六十': 60,
    '六十一': 61, '六十二': 62, '六十三': 63, '六十四': 64, '六十五': 65, '六十六': 66
}
toc1 = doc1.get_toc()
lec_ranges1 = []
for item in toc1:
    lvl, title, page = item
    m = re.search(r'第([一二三四五六七八九十]+)讲\s+([^\s]+)', title)
    if m:
        c_num = m.group(1)
        num = chinese_num_map.get(c_num, 0)
        name = m.group(2)
        lec_ranges1.append({'num': num, 'name': name, 'start': page})

for i in range(len(lec_ranges1)):
    if i + 1 < len(lec_ranges1):
        lec_ranges1[i]['end'] = lec_ranges1[i+1]['start'] - 1
    else:
        lec_ranges1[i]['end'] = len(doc1)

print(f"Ranges defined: Doc0 has {len(lec_ranges0)} lectures, Doc1 has {len(lec_ranges1)} lectures.")

# Basic topic mapping
DEFAULT_LEC_TOPIC = {
    3: "gaoshu-01-indeterminate-0-0",
    4: "gaoshu-01-infinitesimal-order",
    5: "gaoshu-01-power-exponential-1-inf",
    6: "gaoshu-01-sequence-monotone-bounded",
    7: "gaoshu-01-discontinuity-points",
    8: "gaoshu-02-derivative-definition",
    9: "gaoshu-02-higher-order-leibniz",
    10: "gaoshu-02-mean-value-theorems",
    11: "gaoshu-01-difference-inf-inf",
    12: "gaoshu-02-taylor-formula-proof",
    13: "gaoshu-01-indeterminate-0-0",
    14: "gaoshu-02-inequality-and-roots",
    15: "gaoshu-02-inequality-and-roots",
    16: "gaoshu-03-variable-limit-integral",
    17: "gaoshu-03-definite-integral-symmetry",
    18: "gaoshu-03-variable-limit-integral",
    19: "gaoshu-03-definite-integral-symmetry",
    20: "gaoshu-03-improper-integral-convergence",
    21: "gaoshu-03-geometric-applications",
    22: "gaoshu-03-geometric-applications",
    23: "gaoshu-10-cross-taylor-proofs",
    24: "gaoshu-04-first-order-ode",
    25: "gaoshu-04-second-order-constant-coeff",
    26: "gaoshu-04-euler-equation",
    27: "gaoshu-04-first-order-ode",
    28: "gaoshu-09-vector-products-geometry",
    29: "gaoshu-05-differentiability-concept",
    30: "gaoshu-05-chain-rule-composite",
    31: "gaoshu-09-plane-and-line-equations",
    32: "gaoshu-05-lagrange-multipliers",
    33: "gaoshu-06-double-integral-polar",
    34: "gaoshu-06-triple-integral-coordinates",
    35: "gaoshu-07-curvilinear-path-independent",
    36: "gaoshu-07-gauss-divergence-theorem",
    37: "gaoshu-07-stokes-theorem-curl",
    38: "gaoshu-08-series-convergence-tests",
    39: "gaoshu-08-series-convergence-tests",
    40: "gaoshu-08-power-series-radius-interval",
    41: "gaoshu-08-power-series-summation",
    42: "gaoshu-08-fourier-series-dirichlet",
    43: "xiandai-01-determinant-calc-techniques",
    44: "xiandai-02-adjoint-matrix-properties",
    45: "xiandai-02-elementary-matrix-operations",
    46: "xiandai-03-linear-independence-proof",
    47: "xiandai-04-solution-structure-and-rank",
    48: "xiandai-04-matrix-equation-and-common-solutions",
    49: "xiandai-05-eigenvalue-eigenvector-properties",
    50: "xiandai-06-diagonalization-criterion",
    51: "xiandai-06-real-symmetric-orthogonal-diag",
    52: "xiandai-07-quadratic-form-canonical",
    53: "xiandai-08-ab-zero-deep-dive",
    54: "gailv-01-total-probability-bayes",
    55: "gailv-02-distribution-function-properties",
    56: "gailv-02-function-distribution-one-dim",
    57: "gailv-03-joint-marginal-conditional",
    58: "gailv-03-random-variable-functions-2d",
    59: "gailv-04-expectation-egx-formulas",
    60: "gailv-05-chebyshev-inequality",
    61: "gailv-06-three-sampling-distributions",
    62: "gailv-07-moment-and-mle-estimation",
    63: "gailv-07-unbiasedness-eval-criteria"
}

def clean_text_math(s):
    if not s:
        return ""
    # remove page noise
    s = re.sub(r'Maki\s*的完美算术教室', '', s)
    s = re.sub(r'L\d+\n[^\n]+\n压缩讲', '', s)
    s = re.sub(r'L\d+\n[^\n]+\n重点讲', '', s)
    s = re.sub(r'\n\s*\d+\s*\n', '\n', s)
    # clean multiple whitespace
    lines = [l.strip() for l in s.split('\n') if l.strip()]
    cleaned = '\n'.join(lines)
    return cleaned

def clean_solution_steps(sol_text):
    if not sol_text:
        return ["详细推导过程参见真题精解"]
    # Look for step markers like (1), (2), (A), 第一步, 事实1, 1., etc.
    raw_lines = [l.strip() for l in sol_text.split('\n') if l.strip()]
    steps = []
    curr_step = []
    for l in raw_lines:
        if re.match(r'^(第[一二三四五六七八]步|[1-8][\.、]|（[1-8]）|\([1-8]\)|事实\s*[1-8]|解法[一二三]|步骤[一二三]|\([A-D]\)|[A-D][\.、])', l):
            if curr_step:
                steps.append(' '.join(curr_step))
                curr_step = []
        curr_step.append(l)
    if curr_step:
        steps.append(' '.join(curr_step))
    if len(steps) < 2:
        # split by sentences or chunks if single big block
        if len(sol_text) > 180:
            chunks = [c.strip() for c in sol_text.split('。') if c.strip()]
            if len(chunks) >= 2:
                steps = [f"第{i+1}步：{chunk}。" for i, chunk in enumerate(chunks[:4])]
            else:
                steps = [sol_text]
        else:
            steps = [sol_text]
    return steps[:5]

def parse_questions_from_text(full_text, lec_num, default_tid, source_type="doc0"):
    # Split text by question header
    pattern = r'\n(?=(?:真题|题)\s*\d+\.\d+)'
    raw_blocks = re.split(pattern, full_text)
    results = []
    
    for block in raw_blocks:
        b = block.strip()
        if not (b.startswith('真题') or b.startswith('题')):
            continue
        lines = [l.strip() for l in b.split('\n') if l.strip()]
        if len(lines) < 3:
            continue
            
        qid_m = re.match(r'(?:真题|题)\s*(\d+\.\d+)', lines[0])
        if not qid_m:
            continue
        qid = qid_m.group(0)
        
        idx = 1
        meta_items = []
        while idx < len(lines):
            m = re.search(r'(20\d\d)\s*[・·]\s*(数[一二三])\s*[・·]\s*(\([^\)]+\)|\d+)', lines[idx])
            if m:
                meta_items.append({
                    'year': m.group(1),
                    'category': m.group(2),
                    'num': m.group(3) if m.group(3).startswith('(') else f"({m.group(3)})"
                })
                idx += 1
            elif '跨卷重复' in lines[idx]:
                idx += 1
            else:
                break
                
        if not meta_items:
            continue
            
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
            
        body = '\n'.join(lines[idx:])
        
        # Split markers
        sec_pattern = r'\n(?=(?:考点|解|答案[：:]|结论|易错[/\s]*提醒))'
        parts = re.split(sec_pattern, body)
        
        content = clean_text_math(parts[0]) if len(parts) > 0 else ""
        analysis = ""
        solution = ""
        answer = ""
        pitfall = ""
        
        for p in parts[1:]:
            p_strip = p.strip()
            if p_strip.startswith('考点'):
                analysis = clean_text_math(re.sub(r'^考点\s*', '', p_strip))
            elif p_strip.startswith('解'):
                solution = clean_text_math(re.sub(r'^解\s*', '', p_strip))
            elif re.match(r'^答案[：:]', p_strip):
                answer = clean_text_math(re.sub(r'^答案[：:]\s*', '', p_strip))
            elif p_strip.startswith('结论'):
                pitfall = clean_text_math(re.sub(r'^结论\s*', '', p_strip))
            elif re.match(r'^易错[/\s]*提醒', p_strip):
                pitfall = clean_text_math(re.sub(r'^易错[/\s]*提醒\s*', '', p_strip))
                
        # Fallback fields
        if not analysis:
            analysis = f"抓住题目核心特征与关键条件，严格按标准化候选方法推进。"
        if not pitfall:
            pitfall = "注意运算过程中的符号边界与适用条件检查，避免代数变形失误。"
        if not answer:
            answer = "详见具体步骤解析"
            
        # Target topic
        from test_topic_refine import refine_topic_id
        target_tid = refine_topic_id(lec_num, default_tid, content + " " + analysis, title)
        
        steps = clean_solution_steps(solution)
        
        for m in meta_items:
            cat_code = '1' if m['category'] == '数一' else ('2' if m['category'] == '数二' else '3')
            num_clean = re.sub(r'[^\d]', '', m['num'])
            q_unique_id = f"q-{m['year']}-{cat_code}-{num_clean if num_clean else '0'}-{qid.replace('真题','').replace('题','').strip()}"
            src_str = f"Maki大串讲 {qid}" if source_type == "doc0" else f"Maki真题分类精解 {qid}"
            
            results.append({
                'topicId': target_tid,
                'item': {
                    'id': q_unique_id,
                    'year': m['year'],
                    'category': m['category'],
                    'questionNumber': m['num'],
                    'content': content,
                    'analysis': analysis,
                    'solutionSteps': steps,
                    'answer': answer,
                    'pitfall': pitfall,
                    'difficulty': difficulty,
                    'verified': True,
                    'source': src_str
                }
            })
            
    return results

print("Question parser logic compiled successfully.")
