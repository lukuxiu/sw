import json, re, sys

sys.stdout.reconfigure(encoding='utf-8')

with open('scripts/extracted_questions.json', 'r', encoding='utf-8') as f:
    questions = json.load(f)

print(f"Loaded {len(questions)} questions.")

def clean_math_string(s):
    if not s:
        return ""
    
    # 1. Normalize unicode characters to LaTeX
    s = s.replace('≤', r' \le ').replace('≥', r' \ge ').replace('≠', r' \ne ').replace('̸=', r' \ne ')
    s = s.replace('→', r' \to ').replace('∞', r' \infty ').replace('π', r' \pi ')
    s = s.replace('α', r' \alpha ').replace('β', r' \beta ').replace('λ', r' \lambda ')
    s = s.replace('ε', r' \varepsilon ').replace('σ', r' \sigma ').replace('μ', r' \mu ')
    s = s.replace('θ', r' \theta ').replace('γ', r' \gamma ').replace('η', r' \eta ')
    s = s.replace('−', '-')
    
    # 2. Fix broken lim
    # lim\s*\n\s*x \to ...
    s = re.sub(r'lim\s*\n\s*([a-zA-Z]\s*\\to\s*[\w\\\^\+\-]+)', r'\\lim_{\1}', s)
    s = re.sub(r'lim\s+([a-zA-Z]\s*\\to\s*[\w\\\^\+\-]+)', r'\\lim_{\1}', s)
    
    # 3. Fix broken fractions like − \pi \n 2 or \pi \n 2
    s = re.sub(r'-\s*\\pi\s*\n\s*2', r'-\\frac{\\pi}{2}', s)
    s = re.sub(r'\\pi\s*\n\s*2', r'\\frac{\\pi}{2}', s)
    s = re.sub(r'1\s*\n\s*2', r'\\frac{1}{2}', s)
    s = re.sub(r'1\s*\n\s*x', r'\\frac{1}{x}', s)
    s = re.sub(r'1\s*\n\s*n', r'\\frac{1}{n}', s)

    # 4. Remove dangling header noises
    s = re.sub(r'Maki\s*的完美算术教室', '', s)
    s = re.sub(r'L\d+\n[^\n]+\n(?:压缩讲|重点讲)', '', s)
    s = re.sub(r'★★[★☆]{2,3}', '', s)
    s = re.sub(r'\n\s*\d+\s*\n', '\n', s)
    
    # 5. Fix common sub/superscripts: xn -> x_n, x2n -> x_{2n}, an -> a_n
    s = re.sub(r'\bxn\b', r'x_n', s)
    s = re.sub(r'\bx2n\b', r'x_{2n}', s)
    s = re.sub(r'\bx2n\+1\b', r'x_{2n+1}', s)
    s = re.sub(r'\bx3n\b', r'x_{3n}', s)
    s = re.sub(r'\bx3n\+1\b', r'x_{3n+1}', s)
    s = re.sub(r'\bx3n\+2\b', r'x_{3n+2}', s)
    s = re.sub(r'\ban\b', r'a_n', s)
    s = re.sub(r'\bλ(\d+)\b', r'\\lambda_{\1}', s)

    # Ensure formulas with \lim or \to or \frac or \le or \ge or \pi are properly wrapped in $ if not already
    lines = s.split('\n')
    cleaned_lines = []
    for line in lines:
        l = line.strip()
        if not l:
            continue
        # if line contains math commands but no $, wrap math segments
        cleaned_lines.append(l)

    res = '\n'.join(cleaned_lines)
    return res

def extract_mc_options(content):
    # Check if (A), (B), (C), (D) or (a), (b), (c), (d) are present
    m = re.search(r'\(A\)([\s\S]*?)\(B\)([\s\S]*?)\(C\)([\s\S]*?)\(D\)([\s\S]*)', content, re.IGNORECASE)
    if m:
        stem = content[:m.start()].strip()
        optA = m.group(1).strip()
        optB = m.group(2).strip()
        optC = m.group(3).strip()
        optD = m.group(4).strip()
        
        # Helper to wrap option content in $ if it's math
        def wrap_opt(opt_text):
            opt_text = clean_math_string(opt_text)
            if any(k in opt_text for k in ['\\lim', '\\to', '\\frac', '\\le', '\\ge', '\\pi', '=', '+', '-']) and '$' not in opt_text:
                return f"${opt_text}$"
            return opt_text

        return stem, [
            wrap_opt(optA),
            wrap_opt(optB),
            wrap_opt(optC),
            wrap_opt(optD)
        ]
    return content, None

sample_count = 0
for q in questions:
    item = q['item']
    old_content = item['content']
    stem, options = extract_mc_options(old_content)
    stem_clean = clean_math_string(stem)
    item['content'] = stem_clean
    if options:
        item['options'] = options
        if sample_count < 3:
            print(f"=== Sample Beautified Question: {item['id']} ===")
            print("Stem:", stem_clean)
            print("Options:")
            for idx, opt in enumerate(options):
                print(f"  ({chr(65+idx)}) {opt}")
            sample_count += 1

print(f"\nCompleted beautification pass on {len(questions)} questions.")
