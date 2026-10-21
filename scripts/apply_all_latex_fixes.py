import json
import re

# ==========================================
# 1. FIX KNOWLEDGE_BASE.TS
# ==========================================
print("Updating src/data/knowledgeBase.ts...")
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

# Specific answer fixes in KB
kb_answer_fixes = {
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

for nid, node in kb_data.items():
    for q in node.get('pastQuestions', []):
        qid = q.get('id', '')
        if qid in kb_answer_fixes:
            q['answer'] = kb_answer_fixes[qid]
        if qid in ['gaoshu-q-2016-1-4', 'gaoshu-q-2019-1-4']:
            q['content'] = q['content'].replace('(\\quad)', '（　　）')
        # General clean for any (\quad) in content
        if '(\\quad)' in q.get('content', ''):
            q['content'] = q['content'].replace('(\\quad)', '（　　）')

with open('src/data/knowledgeBase.ts', 'w', encoding='utf-8', newline='\n') as f:
    f.write(kb_header + json.dumps(kb_data, ensure_ascii=False, indent=2) + ';\n' + kb_footer)

print("knowledgeBase.ts updated successfully!")

# ==========================================
# 2. FIX PASTQUESTIONSDATA.TS
# ==========================================
print("Updating src/data/pastQuestionsData.ts...")
with open('src/data/pastQuestionsData.ts', 'r', encoding='utf-8') as f:
    pq_full = f.read().replace('\r\n', '\n')

var_decl = 'export const EXTRACTED_PAST_QUESTIONS: Record<string, PastQuestionItem[]> = '
pq_start = pq_full.find(var_decl) + len(var_decl)
pq_header = pq_full[:pq_start]
pq_data = json.loads(pq_full[pq_start:].strip().rstrip(';'))

def clean_text(text):
    if not text or not isinstance(text, str):
        return text
    # Remove null / control chars
    res = re.sub(r'[\u0000-\u0008\u000b\u000c\u000e-\u001f]', '', text)
    # Strip Maki PDF header cruft
    res = re.sub(r'^[^\n]*?（习题集\d+\.\d+）[★☆\s]*\n?', '', res)
    res = re.sub(r'^L\d+\n[^\n]+\n?', '', res)
    res = re.sub(r'^\d+\s*\nL\d+\n[^\n]+\n?', '', res)
    # Strip Maki PDF footer cruft
    res = re.sub(r'\nL\d+\n[^\n]+$', '', res)
    res = re.sub(r'\n\d+\s*\nL\d+\n[^\n]+$', '', res)
    # Replace (\quad)
    res = res.replace('(\\quad)', '（　　）')
    # Replace circled numbers
    res = re.sub(r'1⃝|①', '(1) ', res)
    res = re.sub(r'2⃝|②', '(2) ', res)
    res = re.sub(r'3⃝|③', '(3) ', res)
    res = re.sub(r'4⃝|④', '(4) ', res)
    return res.strip()

for nid, qlist in pq_data.items():
    for q in qlist:
        qid = q.get('id', '')

        # Clean answer trailing headers
        if q.get('answer'):
            ans = q['answer'].strip()
            choice_match = re.match(r'^([A-D])\s*\n', ans)
            if choice_match:
                q['answer'] = choice_match.group(1)
            elif ans.startswith('A\n') or ans == 'A': q['answer'] = 'A'
            elif ans.startswith('B\n') or ans == 'B': q['answer'] = 'B'
            elif ans.startswith('C\n') or ans == 'C': q['answer'] = 'C'
            elif ans.startswith('D\n') or ans == 'D': q['answer'] = 'D'

        # Special fix for q-2017-1-10-25.1
        if qid == 'q-2017-1-10-25.1':
            q['content'] = '微分方程 $y\'\' + 2y\' + 3y = 0$ 的通解为 $y = \\underline{\\hspace{4em}}$。'
            q['answer'] = '$y = e^{-x}(C_1 \\cos\\sqrt{2}x + C_2 \\sin\\sqrt{2}x)$（$C_1, C_2$ 为任意常数）'
            q['pitfall'] = '（1）把 $\\sqrt{-8}$ 化简成 $2\\sqrt{2}i$ 时算错，写成 $\\pm\\sqrt{2}$ 或 $-1 \\pm 2\\sqrt{2}i$；（2）忘记写任意常数 $C_1, C_2$，或只写一个常数。填空题问「通解」，必须含两个独立任意常数。'
            continue

        # Clean content & fields
        if q.get('content'):
            q['content'] = clean_text(q['content'])
        if q.get('options'):
            q['options'] = [clean_text(opt) for opt in q['options']]
        if q.get('analysis'):
            q['analysis'] = clean_text(q['analysis'])
        if q.get('pitfall'):
            q['pitfall'] = clean_text(q['pitfall'])
        if q.get('solutionSteps'):
            q['solutionSteps'] = [clean_text(s) for s in q['solutionSteps']]

with open('src/data/pastQuestionsData.ts', 'w', encoding='utf-8', newline='\n') as f:
    f.write(pq_header + json.dumps(pq_data, ensure_ascii=False, indent=2) + ';\n')

print("pastQuestionsData.ts updated successfully!")
