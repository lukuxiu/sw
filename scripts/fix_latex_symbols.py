import json, re, sys

sys.stdout.reconfigure(encoding='utf-8')

with open('src/data/pastQuestionsData.ts', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Unicode prime to standard prime '
text = text.replace('′', "'")

# 2. Fix unicode piecewise cases
def fix_cases(m):
    block = m.group(0)
    lines = [l.strip() for l in block.split('\n') if l.strip() and l.strip() not in ['', '', '']]
    return '\\begin{cases} ' + ' \\\\ '.join(lines) + ' \\end{cases}'

text = re.sub(r'[\s\S]*?[\s\S]*?(?=(?:\n\s*\(?[A-D]\)?|\n\s*[考解答]|\$|\Z))', fix_cases, text)

# 3. Fix unicode matrices    ...   
def fix_matrices(m):
    inner = m.group(0)
    lines = [l.strip() for l in inner.split('\n') if l.strip() and not re.match(r'^[\(\)]+$', l.strip())]
    if lines:
        return '\\begin{pmatrix} ' + ' \\\\ '.join(lines) + ' \\end{pmatrix}'
    return '\\begin{pmatrix} 0 \\end{pmatrix}'

text = re.sub(r'[\s\S]*?', fix_matrices, text)

# 4. Fix \sqrt
text = re.sub(r'\\sqrt\{\}\s*(\d+)', r'\\sqrt{\1}', text)
text = text.replace(r'\sqrt{}', r'\sqrt{x}')

# 5. Fix spaces right after $ or before $: $ \frac -> $\frac
text = re.sub(r'\$\s+', '$', text)
text = re.sub(r'\s+\$', '$', text)

# 6. KaTeX parse errors where $ was wrapped around invalid tokens:
# Remove $ if option has broken newline or parenthesis
def clean_invalid_dollars(m):
    content = m.group(1)
    if '\n' in content and any(c in content for c in ['o \n', 'P\n', 'ln\n']):
        return content.replace('\n', ' ')
    if any(c in content for c in ['', '', '', '', '', '', '', '', '']):
        return content.replace('$', '')
    return '$' + content.strip() + '$'

text = re.sub(r'\$([^\$]+?)\$', clean_invalid_dollars, text)

with open('src/data/pastQuestionsData.ts', 'w', encoding='utf-8') as f:
    f.write(text)

print("Applied symbol cleanup to pastQuestionsData.ts successfully.")
