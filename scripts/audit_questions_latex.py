import json
import re
import os

LATEX_COMMAND_PATTERN = re.compile(r'\\[a-zA-Z]+')

COMMON_COMMANDS = {
    'frac', 'lim', 'int', 'iint', 'iiint', 'oint', 'sum', 'prod',
    'alpha', 'beta', 'gamma', 'delta', 'epsilon', 'zeta', 'eta', 'theta',
    'iota', 'kappa', 'lambda', 'mu', 'nu', 'xi', 'pi', 'rho', 'sigma',
    'tau', 'upsilon', 'phi', 'chi', 'psi', 'omega',
    'Gamma', 'Delta', 'Theta', 'Lambda', 'Xi', 'Pi', 'Sigma', 'Phi', 'Psi', 'Omega',
    'partial', 'infty', 'nabla', 'sqrt', 'cdot', 'times', 'div', 'pm', 'mp',
    'le', 'ge', 'leq', 'geq', 'neq', 'approx', 'equiv', 'sim',
    'in', 'notin', 'subset', 'subseteq', 'cup', 'cap',
    'to', 'rightarrow', 'leftarrow', 'Rightarrow', 'Leftarrow', 'iff',
    'quad', 'qquad', 'text', 'mathrm', 'mathbf', 'mathit', 'bm',
    'sin', 'cos', 'tan', 'cot', 'sec', 'csc', 'arcsin', 'arccos', 'arctan',
    'ln', 'log', 'exp', 'det', 'tr', 'rank', 'dim', 'ker',
    'begin', 'end', 'pmatrix', 'bmatrix', 'vmatrix', 'matrix', 'cases', 'aligned'
}

def remove_dollar_math(text):
    no_display = re.sub(r'\$\$[\s\S]*?\$\$', ' ', text)
    no_inline = re.sub(r'\$[^\$\n]+?\$', ' ', no_display)
    return no_inline

def audit_text(text, location):
    if not text or not isinstance(text, str):
        return []

    issues = []

    # 1. Check unmatched $
    dollars = re.findall(r'(?<!\\)\$', text)
    if len(dollars) % 2 != 0:
        issues.append({
            'type': 'UNMATCHED_DOLLAR',
            'location': location,
            'details': f'Odd number of $ ({len(dollars)}): "{text[:120]}..."',
            'text': text
        })

    # 2. Check for \( or \) or \[ or \] outside $
    outside = remove_dollar_math(text)
    if r'\(' in outside or r'\)' in outside or r'\[' in outside or r'\]' in outside:
        issues.append({
            'type': 'PAREN_BRACKET_LATEX_DELIMITER',
            'location': location,
            'details': f'Found \\( / \\) / \\[ / \\] outside $: "{text[:120]}..."',
            'text': text
        })

    # 3. Check for raw LaTeX commands outside of $...$
    found_cmds = LATEX_COMMAND_PATTERN.findall(outside)
    leaked = [cmd[1:] for cmd in found_cmds if cmd[1:] in COMMON_COMMANDS]
    if leaked:
        issues.append({
            'type': 'RAW_LATEX_OUTSIDE_DOLLARS',
            'location': location,
            'commands': list(set(leaked)),
            'details': f'Raw LaTeX commands {list(set(leaked))} without $: "{text[:120]}..."',
            'text': text
        })

    # 4. Check HTML entities in formulas
    formulas = re.findall(r'(\$\$[\s\S]*?\$\$|\$[^\$]+?\$)', text)
    for f in formulas:
        inner = f[2:-2] if f.startswith('$$') else f[1:-1]
        if '&lt;' in inner or '&gt;' in inner or '&amp;' in inner or '&nbsp;' in inner:
            issues.append({
                'type': 'HTML_ENTITY_IN_FORMULA',
                'location': location,
                'details': f'HTML entity in formula: "{f}"',
                'text': text
            })

    # 5. Check empty formula $ $
    for f in re.findall(r'\$\s*\$', text):
        issues.append({
            'type': 'EMPTY_FORMULA',
            'location': location,
            'details': 'Found empty formula $$',
            'text': text
        })

    return issues

all_issues = []

# Audit knowledgeBase.ts
print("Auditing knowledgeBase.ts...")
with open('src/data/knowledgeBase.ts', 'r', encoding='utf-8') as f:
    kb_text = f.read()
kb_start = kb_text.find('export const KNOWLEDGE_BASE: Record<string, KnowledgeNode> = {') + len('export const KNOWLEDGE_BASE: Record<string, KnowledgeNode> = ')
kb_import = kb_text.find('import { EXTRACTED_PAST_QUESTIONS }')
kb_semi = kb_text.rfind('};', 0, kb_import)
kb_data = json.loads(kb_text[kb_start:kb_semi+1])

for nid, node in kb_data.items():
    for i, q in enumerate(node.get('pastQuestions', [])):
        loc_prefix = f"knowledgeBase[{nid}].pastQuestions[{i}]({q.get('id', '')})"
        all_issues.extend(audit_text(q.get('content', ''), f"{loc_prefix}.content"))
        for oi, opt in enumerate(q.get('options', [])):
            all_issues.extend(audit_text(opt, f"{loc_prefix}.options[{oi}]"))
        all_issues.extend(audit_text(q.get('analysis', ''), f"{loc_prefix}.analysis"))
        all_issues.extend(audit_text(q.get('answer', ''), f"{loc_prefix}.answer"))
        all_issues.extend(audit_text(q.get('pitfall', ''), f"{loc_prefix}.pitfall"))
        for si, st in enumerate(q.get('solutionSteps', [])):
            all_issues.extend(audit_text(st, f"{loc_prefix}.solutionSteps[{si}]"))

# Audit pastQuestionsData.ts
print("Auditing pastQuestionsData.ts...")
with open('src/data/pastQuestionsData.ts', 'r', encoding='utf-8') as f:
    pq_text = f.read()
pq_start = pq_text.find('export const EXTRACTED_PAST_QUESTIONS: Record<string, PastQuestionItem[]> = ') + len('export const EXTRACTED_PAST_QUESTIONS: Record<string, PastQuestionItem[]> = ')
pq_json_str = pq_text[pq_start:].strip().rstrip(';')
pq_data = json.loads(pq_json_str)

for nid, qlist in pq_data.items():
    for i, q in enumerate(qlist):
        loc_prefix = f"pastQuestionsData[{nid}][{i}]({q.get('id', '')})"
        all_issues.extend(audit_text(q.get('content', ''), f"{loc_prefix}.content"))
        for oi, opt in enumerate(q.get('options', [])):
            all_issues.extend(audit_text(opt, f"{loc_prefix}.options[{oi}]"))
        all_issues.extend(audit_text(q.get('analysis', ''), f"{loc_prefix}.analysis"))
        all_issues.extend(audit_text(q.get('answer', ''), f"{loc_prefix}.answer"))
        all_issues.extend(audit_text(q.get('pitfall', ''), f"{loc_prefix}.pitfall"))
        for si, st in enumerate(q.get('solutionSteps', [])):
            all_issues.extend(audit_text(st, f"{loc_prefix}.solutionSteps[{si}]"))

# Audit makiLectures.ts
print("Auditing makiLectures.ts...")
with open('src/data/makiLectures.ts', 'r', encoding='utf-8') as f:
    maki_text = f.read()

maki_start = maki_text.find('export const MAKI_LECTURES: MakiLecture[] = ') + len('export const MAKI_LECTURES: MakiLecture[] = ')
maki_json = maki_text[maki_start:].strip().rstrip(';')
maki_lectures = json.loads(maki_json)

for lec in maki_lectures:
    loc_prefix = f"makiLectures[{lec.get('id')}]"
    all_issues.extend(audit_text(lec.get('orientation', ''), f"{loc_prefix}.orientation"))
    for s_idx, sub in enumerate(lec.get('subsections', [])):
        all_issues.extend(audit_text(sub, f"{loc_prefix}.subsections[{s_idx}]"))
    for c_idx, card in enumerate(lec.get('methodCards', [])):
        all_issues.extend(audit_text(card.get('title', ''), f"{loc_prefix}.methodCards[{c_idx}].title"))
        all_issues.extend(audit_text(card.get('content', ''), f"{loc_prefix}.methodCards[{c_idx}].content"))

# Audit metaMethods.ts
print("Auditing metaMethods.ts...")
with open('src/data/metaMethods.ts', 'r', encoding='utf-8') as f:
    meta_text = f.read()

meta_start = meta_text.find('export const UNIVERSAL_META_METHODS: UniversalMetaMethod[] = ') + len('export const UNIVERSAL_META_METHODS: UniversalMetaMethod[] = ')
meta_json_str = meta_text[meta_start:].strip().rstrip(';')
meta_methods = json.loads(meta_json_str)

for method in meta_methods:
    loc_prefix = f"metaMethods[{method.get('id')}]"
    for q_idx, q in enumerate(method.get('pastQuestions', [])):
        all_issues.extend(audit_text(q.get('stem', ''), f"{loc_prefix}.pastQuestions[{q_idx}].stem"))
        all_issues.extend(audit_text(q.get('methodUsage', ''), f"{loc_prefix}.pastQuestions[{q_idx}].methodUsage"))
        all_issues.extend(audit_text(q.get('solutionKey', ''), f"{loc_prefix}.pastQuestions[{q_idx}].solutionKey"))

print(f"\n================ AUDIT SUMMARY ================")
print(f"Total issues found: {len(all_issues)}")

issue_types = {}
for iss in all_issues:
    t = iss['type']
    issue_types[t] = issue_types.get(t, 0) + 1

for t, count in issue_types.items():
    print(f"  {t}: {count}")

print(f"\nListing first 40 issues:")
for i, iss in enumerate(all_issues[:40]):
    print(f"\n[{i+1}] {iss['type']} at {iss['location']}:")
    print(f"    {iss['details']}")
