import json
import re

def clean_text_artifacts(text):
    if not text or not isinstance(text, str):
        return text

    # Remove null and non-standard control bytes
    res = re.sub(r'[\u0000-\u0008\u000b\u000c\u000e-\u001f]', '', text)

    # Strip Maki PDF header cruft
    res = re.sub(r'^[^\n]*?（习题集\d+\.\d+）[★☆\s]*\n?', '', res)
    res = re.sub(r'^L\d+\n[^\n]+\n?', '', res)
    res = re.sub(r'^\d+\s*\nL\d+\n[^\n]+\n?', '', res)

    # Strip Maki PDF footer cruft
    res = re.sub(r'\nL\d+\n[^\n]+$', '', res)
    res = re.sub(r'\n\d+\s*\nL\d+\n[^\n]+$', '', res)

    # Replace (\quad) with standard full-width brackets （　　）
    res = res.replace('(\\quad)', '（　　）')

    # Replace circled numbers 1⃝, 2⃝, etc. with (1), (2)
    res = re.sub(r'1⃝|①', '(1) ', res)
    res = re.sub(r'2⃝|②', '(2) ', res)
    res = re.sub(r'3⃝|③', '(3) ', res)
    res = re.sub(r'4⃝|④', '(4) ', res)

    # Replace ˆ (integral glyph) with \int
    res = re.sub(r'ˆ\s*\+∞\s*\n?\s*(\d+)', r'\\int_{\1}^{+\\infty}', res)
    res = re.sub(r'ˆ\s*([a-zA-Z0-9]+)\s*\n?\s*([a-zA-Z0-9]+)', r'\\int_{\2}^{\1}', res)
    res = re.sub(r'ˆ', r'\\int ', res)

    # Replace broken sqrt newline
    res = re.sub(r'√\s*\n\s*([a-zA-Z0-9]+)', r'\\sqrt{\1}', res)
    res = re.sub(r'√([a-zA-Z0-9]+)', r'\\sqrt{\1}', res)

    # Clean out matrix paren chars and cases brace chars
    res = re.sub(r'[]', '', res)
    res = re.sub(r'[]', '', res)

    # Replace special symbols
    res = res.replace('· · ·', '\\cdots')
    res = res.replace('̸=', '\\ne ')
    res = res.replace('≤', '\\le ')
    res = res.replace('≥', '\\ge ')
    res = res.replace('→0', '\\to 0')

    return res.strip()

def extract_choice_options(content):
    match = re.search(r'(?:\n|\A|。|；)\s*\(A\)\s*([\s\S]*?)\s*\(B\)\s*([\s\S]*?)\s*\(C\)\s*([\s\S]*?)\s*\(D\)\s*([\s\S]*)$', content)
    if match:
        stem = content[:match.start()].strip()
        optA = match.group(1).strip()
        optB = match.group(2).strip()
        optC = match.group(3).strip()
        optD = match.group(4).strip()
        return stem, [optA, optB, optC, optD]
    return content, None

def clean_question(q):
    q_copy = dict(q)

    # Clean answer
    if q_copy.get('answer'):
        ans = q_copy['answer'].strip()
        choice_match = re.match(r'^([A-D])\s*\n', ans)
        if choice_match:
            q_copy['answer'] = choice_match.group(1)
        elif ans.startswith('A\n') or ans == 'A': q_copy['answer'] = 'A'
        elif ans.startswith('B\n') or ans == 'B': q_copy['answer'] = 'B'
        elif ans.startswith('C\n') or ans == 'C': q_copy['answer'] = 'C'
        elif ans.startswith('D\n') or ans == 'D': q_copy['answer'] = 'D'

    # Specific fix for q-2017-1-10-25.1
    if q_copy.get('id') == 'q-2017-1-10-25.1':
        q_copy['content'] = '微分方程 $y\'\' + 2y\' + 3y = 0$ 的通解为 $y = \\underline{\\hspace{4em}}$。'
        q_copy['answer'] = '$y = e^{-x}(C_1 \\cos\\sqrt{2}x + C_2 \\sin\\sqrt{2}x)$（$C_1, C_2$ 为任意常数）'
        q_copy['pitfall'] = '（1）把 $\\sqrt{-8}$ 化简成 $2\\sqrt{2}i$ 时算错，写成 $\\pm\\sqrt{2}$ 或 $-1 \\pm 2\\sqrt{2}i$；（2）忘记写任意常数 $C_1, C_2$，或只写一个常数。填空题问「通解」，必须含两个独立任意常数。'
        return q_copy

    # Clean content & extract options
    if q_copy.get('content'):
        cleaned_content = clean_text_artifacts(q_copy['content'])
        stem, opts = extract_choice_options(cleaned_content)
        q_copy['content'] = stem
        if opts and (not q_copy.get('options') or len(q_copy['options']) == 0):
            q_copy['options'] = [clean_text_artifacts(opt) for opt in opts]

    # Clean existing options
    if q_copy.get('options'):
        q_copy['options'] = [clean_text_artifacts(opt) for opt in q_copy['options']]

    # Clean other fields
    if q_copy.get('analysis'):
        q_copy['analysis'] = clean_text_artifacts(q_copy['analysis'])
    if q_copy.get('pitfall'):
        q_copy['pitfall'] = clean_text_artifacts(q_copy['pitfall'])
    if q_copy.get('solutionSteps'):
        q_copy['solutionSteps'] = [clean_text_artifacts(s) for s in q_copy['solutionSteps']]

    return q_copy

# 1. Clean EXTRACTED_PAST_QUESTIONS
with open('src/data/pastQuestionsData.ts', 'r', encoding='utf-8') as f:
    pq_full = f.read().replace('\r\n', '\n')

var_decl = 'export const EXTRACTED_PAST_QUESTIONS: Record<string, PastQuestionItem[]> = '
pq_start = pq_full.find(var_decl) + len(var_decl)
pq_header = pq_full[:pq_start]
pq_data = json.loads(pq_full[pq_start:].strip().rstrip(';'))

cleaned_pq_data = {}
for nid, qlist in pq_data.items():
    cleaned_pq_data[nid] = [clean_question(q) for q in qlist]

with open('src/data/pastQuestionsData.ts', 'w', encoding='utf-8', newline='\n') as f:
    f.write(pq_header + json.dumps(cleaned_pq_data, ensure_ascii=False, indent=2) + ';\n')

print("pastQuestionsData.ts cleaned and written successfully!")

# 2. Clean KNOWLEDGE_BASE
with open('src/data/knowledgeBase.ts', 'r', encoding='utf-8') as f:
    kb_full = f.read().replace('\r\n', '\n')

prefix_kb = 'import { KnowledgeNode } from \'./types\';\n\nexport const KNOWLEDGE_BASE: Record<string, KnowledgeNode> = '
kb_import = kb_full.find("import { EXTRACTED_PAST_QUESTIONS }")
kb_semi = kb_full.rfind('};', 0, kb_import)
kb_header = kb_full[:len(prefix_kb)]
kb_footer = kb_full[kb_semi+2:]
kb_data = json.loads(kb_full[len(prefix_kb):kb_semi + 1].strip())

# Fix triggers in gaoshu-00-algebra-five-actions
if 'gaoshu-00-algebra-five-actions' in kb_data:
    kb_data['gaoshu-00-algebra-five-actions']['triggers'] = [
        "式中含二次三项式形如 $x^2 + px + q$（反常积分、二次型、有理积分）",
        "含根号差式形如 $\\sqrt{A} - \\sqrt{B}$ 处于分子或分母",
        "数列或级数通项形如 $\\frac{1}{n(n+k)}$ 或 $\\frac{1}{n(n+1)(n+2)}$",
        "极限与不等式证明中出现 $e^x$, $\\ln(1+x)$, $\\sin x$, $\\tan x$ 混合",
        "初等函数定义域、反函数与初等三角积化和差与和差化积"
    ]

# Specific fixes in KB pastQuestions
specific_kb_answers = {
    'gaoshu-q-2017-1-10': r'$\frac{\pi}{2}$',
    'gaoshu-q-2020-1-17': r'$9 - 5\sqrt{3}$',
    'gaoshu-q-2022-1-9': r'$1 - \cos 1$',
    'gaoshu-q-2021-1-11': r'$\frac{8}{15}\pi R^5$',
    'gaoshu-q-2021-1-18': r'$\frac{3\pi}{2}$',
    'gaoshu-q-2016-1-11': r'$-6\pi$',
    'gaoshu-q-2023-1-19': r'$S(x) = \frac{1}{2}\ln\frac{1+x}{1-x}$，和为 $\frac{\sqrt{3}}{2}\ln(2+\sqrt{3})$',
    'gaoshu-q-2016-1-13': r'$\sqrt{3}$',
    'gaoshu-q-2019-1-15': r'$\frac{1}{2\sqrt{2}}(e^{\sqrt{2}x} - e^{-\sqrt{2}x})$',
    'gaoshu-q-2021-1-10': r'$(f_1\' + f_2\' + y f_3\')\,dx + (f_1\' - f_2\' + x f_3\')\,dy$',
}

cleaned_kb_data = {}
for nid, node in kb_data.items():
    node_copy = dict(node)
    if 'pastQuestions' in node_copy:
        cleaned_qs = []
        for q in node_copy['pastQuestions']:
            q_clean = clean_question(q)
            if q_clean['id'] in specific_kb_answers:
                q_clean['answer'] = specific_kb_answers[q_clean['id']]
            if q_clean['id'] in ['gaoshu-q-2016-1-4', 'gaoshu-q-2019-1-4']:
                q_clean['content'] = q_clean['content'].replace('(\\quad)', '（　　）')
            cleaned_qs.append(q_clean)
        node_copy['pastQuestions'] = cleaned_qs
    cleaned_kb_data[nid] = node_copy

with open('src/data/knowledgeBase.ts', 'w', encoding='utf-8', newline='\n') as f:
    f.write(kb_header + json.dumps(cleaned_kb_data, ensure_ascii=False, indent=2) + ';\n' + kb_footer)

print("knowledgeBase.ts cleaned and written successfully!")
