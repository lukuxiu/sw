import json, re, sys

sys.stdout.reconfigure(encoding='utf-8')

with open('scripts/extracted_questions.json', 'r', encoding='utf-8') as f:
    raw_questions = json.load(f)

print(f"Reprocessing {len(raw_questions)} questions for optimal readability and formula completeness...")

def normalize_math(text):
    if not text:
        return ""
    
    # 1. Unicode mathematical symbols
    text = text.replace('≤', r' \le ').replace('≥', r' \ge ').replace('≠', r' \ne ').replace('̸=', r' \ne ')
    text = text.replace('→', r' \to ').replace('∞', r' \infty ').replace('π', r' \pi ')
    text = text.replace('α', r' \alpha ').replace('β', r' \beta ').replace('λ', r' \lambda ')
    text = text.replace('ε', r' \varepsilon ').replace('σ', r' \sigma ').replace('μ', r' \mu ')
    text = text.replace('θ', r' \theta ').replace('γ', r' \gamma ').replace('η', r' \eta ')
    text = text.replace('−', '-')
    
    # 2. Fix broken lim
    text = re.sub(r'lim\s*\n\s*([a-zA-Z]\s*\\to\s*[\w\\\^\+\-]+)', r'\\lim_{\1}', text)
    text = re.sub(r'lim\s+([a-zA-Z]\s*\\to\s*[\w\\\^\+\-]+)', r'\\lim_{\1}', text)
    
    # 3. Fix broken fractions like - \pi \n 2 or 1 \n 2
    text = re.sub(r'-\s*\\pi\s*\n\s*2', r'-\\frac{\\pi}{2}', text)
    text = re.sub(r'\\pi\s*\n\s*2', r'\\frac{\\pi}{2}', text)
    text = re.sub(r'1\s*\n\s*2', r'\\frac{1}{2}', text)
    text = re.sub(r'1\s*\n\s*x', r'\\frac{1}{x}', text)
    text = re.sub(r'1\s*\n\s*n', r'\\frac{1}{n}', text)

    # 4. Remove book headers
    text = re.sub(r'Maki\s*的完美算术教室', '', text)
    text = re.sub(r'L\d+\n[^\n]+\n(?:压缩讲|重点讲)', '', text)
    text = re.sub(r'★★[★☆]{2,3}', '', text)
    text = re.sub(r'\n\s*\d+\s*\n', '\n', text)
    
    # 5. Fix common sub/superscripts
    text = re.sub(r'\bxn\b', r'x_n', text)
    text = re.sub(r'\bx2n\b', r'x_{2n}', text)
    text = re.sub(r'\bx2n\+1\b', r'x_{2n+1}', text)
    text = re.sub(r'\bx3n\b', r'x_{3n}', text)
    text = re.sub(r'\bx3n\+1\b', r'x_{3n+1}', text)
    text = re.sub(r'\bx3n\+2\b', r'x_{3n+2}', text)
    text = re.sub(r'\ban\b', r'a_n', text)
    text = re.sub(r'\bλ(\d+)\b', r'\\lambda_{\1}', text)

    # 6. Wrap math formula fragments properly
    # If a line contains math commands but has no $, let's split on Chinese punctuation & conjunctions
    lines = text.split('\n')
    cleaned_lines = []
    for line in lines:
        l = line.strip()
        if not l:
            continue
        if any(k in l for k in ['\\lim', '\\to', '\\frac', '\\le', '\\ge', '\\pi', '\\alpha', '\\beta', '\\lambda', '\\int', '=']) and '$' not in l:
            parts = re.split(r'([，,、。；;\s]*[若则当且仅当由于故因此由但可得可知设若使][，,、\s]*)', l)
            res_parts = []
            for p in parts:
                if not p.strip():
                    res_parts.append(p)
                elif re.match(r'^[，,、。；;\s]*[若则当且仅当由于故因此由但可得可知设若使][，,、\s]*$', p):
                    res_parts.append(p)
                elif any(k in p for k in ['\\lim', '\\to', '\\frac', '\\le', '\\ge', '\\pi', '\\alpha', '\\beta', '\\lambda', '\\int', '=']):
                    res_parts.append(f"${p.strip()}$")
                else:
                    res_parts.append(p)
            cleaned_lines.append(''.join(res_parts))
        else:
            cleaned_lines.append(l)

    return '\n'.join(cleaned_lines)

def extract_options(content):
    m = re.search(r'\(A\)([\s\S]*?)\(B\)([\s\S]*?)\(C\)([\s\S]*?)\(D\)([\s\S]*)', content, re.IGNORECASE)
    if m:
        stem = normalize_math(content[:m.start()].strip())
        opts = [
            normalize_math(m.group(1).strip()),
            normalize_math(m.group(2).strip()),
            normalize_math(m.group(3).strip()),
            normalize_math(m.group(4).strip())
        ]
        return stem, opts
    return normalize_math(content), None

by_topic = {}
mc_count = 0

for entry in raw_questions:
    original_tid = entry['topicId']
    item = entry['item']
    
    # Beautify content and extract options
    stem, options = extract_options(item['content'])
    item['content'] = stem
    if options:
        item['options'] = options
        mc_count += 1
        
    item['analysis'] = normalize_math(item.get('analysis', ''))
    item['pitfall'] = normalize_math(item.get('pitfall', ''))
    item['solutionSteps'] = [normalize_math(s) for s in item.get('solutionSteps', [])]
    
    tid = entry['topicId']
    if tid not in by_topic:
        by_topic[tid] = []
    by_topic[tid].append(item)

print(f"Extracted options for {mc_count} multiple-choice questions.")
print(f"Grouped into {len(by_topic)} topics.")

# Write to src/data/pastQuestionsData.ts
ts_code = """import { PastQuestionItem } from './types';

/**
 * 考研数学真题全集索引 (包括大串讲全部 309 道精解例题 + 2021~2026 年数一/数二/数三全部真题分类)
 * 依据真实考研数学考题规范渲染：选项拆分网格卡片、公式 KaTeX 规范化、解题步骤结构化。
 */
export const EXTRACTED_PAST_QUESTIONS: Record<string, PastQuestionItem[]> = """

ts_code += json.dumps(by_topic, ensure_ascii=False, indent=2) + ";\n"

with open('src/data/pastQuestionsData.ts', 'w', encoding='utf-8') as f:
    f.write(ts_code)

print("Saved updated src/data/pastQuestionsData.ts.")
