import json, re, sys, unicodedata

sys.stdout.reconfigure(encoding='utf-8')

with open('scripts/extracted_questions.json', 'r', encoding='utf-8') as f:
    raw_questions = json.load(f)

print(f"Reprocessing {len(raw_questions)} questions with strict NFKC and KaTeX compatibility...")

def clean_text_with_math(text):
    if not text:
        return ""
    
    # 1. Unicode NFKC normalization (fixes italic unicode math chars like 𝑥, 𝑎, 𝑏)
    text = unicodedata.normalize('NFKC', text)
    
    # 2. Fix bullet points and strange unicode symbols
    text = text.replace('•', '·').replace('√', r'\sqrt{}').replace('̸=', r'\ne ').replace('≠', r'\ne ')
    text = text.replace('≤', r'\le ').replace('≥', r'\ge ').replace('→', r'\to ').replace('∞', r'\infty ').replace('π', r'\pi ')
    text = text.replace('α', r'\alpha ').replace('β', r'\beta ').replace('λ', r'\lambda ').replace('σ', r'\sigma ').replace('μ', r'\mu ')
    text = text.replace('ε', r'\varepsilon ').replace('θ', r'\theta ')
    text = text.replace('−', '-')
    
    # 3. Remove book headers
    text = re.sub(r'Maki\s*的完美算术教室', '', text)
    text = re.sub(r'L\d+\n[^\n]+\n(?:压缩讲|重点讲)', '', text)
    text = re.sub(r'★★[★☆]{2,3}', '', text)
    text = re.sub(r'\n\s*\d+\s*\n', '\n', text)
    
    # 4. Fix lim
    text = re.sub(r'lim\s*\n\s*([a-zA-Z]\s*\\to\s*[\w\\\^\+\-]+)', r'\\lim_{\1}', text)
    text = re.sub(r'lim\s+([a-zA-Z]\s*\\to\s*[\w\\\^\+\-]+)', r'\\lim_{\1}', text)

    # 5. Fix common fractions broken across lines
    text = re.sub(r'-\s*\\pi\s*\n\s*2', r'-\\frac{\\pi}{2}', text)
    text = re.sub(r'\\pi\s*\n\s*2', r'\\frac{\\pi}{2}', text)
    text = re.sub(r'1\s*\n\s*2', r'\\frac{1}{2}', text)
    text = re.sub(r'1\s*\n\s*x', r'\\frac{1}{x}', text)
    text = re.sub(r'1\s*\n\s*n', r'\\frac{1}{n}', text)

    # 6. Fix sub/superscripts
    text = re.sub(r'\bxn\b', r'x_n', text)
    text = re.sub(r'\bx2n\b', r'x_{2n}', text)
    text = re.sub(r'\bx2n\+1\b', r'x_{2n+1}', text)
    text = re.sub(r'\bx3n\b', r'x_{3n}', text)
    text = re.sub(r'\bx3n\+1\b', r'x_{3n+1}', text)
    text = re.sub(r'\bx3n\+2\b', r'x_{3n+2}', text)
    text = re.sub(r'\ban\b', r'a_n', text)
    
    # 7. NEVER wrap Chinese characters in $!
    # If text has $, make sure no Chinese character is inside $...$
    parts = text.split('$')
    new_parts = []
    for i, p in enumerate(parts):
        if i % 2 == 1:
            # Inside math mode
            # If this math part contains Chinese characters, pull Chinese out!
            if re.search(r'[\u4e00-\u9fa5]', p):
                sub_tokens = re.split(r'([\u4e00-\u9fa5，。；、（）]+)', p)
                reconstructed = []
                for st in sub_tokens:
                    if re.search(r'[\u4e00-\u9fa5，。；、（）]', st):
                        reconstructed.append(st) # Chinese OUTSIDE $
                    elif st.strip():
                        reconstructed.append(f"${st.strip()}$") # Math INSIDE $
                new_parts.append(''.join(reconstructed))
            else:
                new_parts.append(f"${p}$")
        else:
            new_parts.append(p)
            
    res = ''.join(new_parts)
    # clean up empty $$
    res = re.sub(r'\${2,}', '', res)
    return res.strip()

def extract_options(content):
    # Match (A), (B), (C), (D)
    m = re.search(r'\(A\)([\s\S]*?)\(B\)([\s\S]*?)\(C\)([\s\S]*?)\(D\)([\s\S]*)', content, re.IGNORECASE)
    if m:
        stem = clean_text_with_math(content[:m.start()].strip())
        raw_opts = [
            m.group(1).strip(),
            m.group(2).strip(),
            m.group(3).strip(),
            m.group(4).strip()
        ]
        opts = []
        for opt in raw_opts:
            cleaned_opt = clean_text_with_math(opt)
            # If option is a pure formula (no Chinese) and not wrapped in $, wrap it in $
            if not re.search(r'[\u4e00-\u9fa5]', cleaned_opt) and '$' not in cleaned_opt:
                cleaned_opt = f"${cleaned_opt}$"
            opts.append(cleaned_opt)
        return stem, opts
    return clean_text_with_math(content), None

by_topic = {}
mc_count = 0

for entry in raw_questions:
    original_tid = entry['topicId']
    item = entry['item']
    
    stem, options = extract_options(item['content'])
    item['content'] = stem
    if options:
        item['options'] = options
        mc_count += 1
        
    item['analysis'] = clean_text_with_math(item.get('analysis', ''))
    item['pitfall'] = clean_text_with_math(item.get('pitfall', ''))
    item['solutionSteps'] = [clean_text_with_math(s) for s in item.get('solutionSteps', [])]
    
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

print("Saved clean src/data/pastQuestionsData.ts.")
