import os, fitz, re, json, sys

sys.stdout.reconfigure(encoding='utf-8')

pdfs = sorted([f for f in os.listdir('.') if f.endswith('.pdf')])
doc0 = fitz.open(pdfs[0]) # 大串讲
doc1 = fitz.open(pdfs[1]) # 分类精解

print("Testing parser on Doc 0 L03...")

# Let's inspect pages 49 to 56 for L03 questions in Doc 0
l03_text = ""
for pno in range(48, 56):
    l03_text += f"\n--- PAGE {pno+1} ---\n" + doc0[pno].get_text()

# Find question boundaries
blocks = re.split(r'\n(?=真题\s*\d+\.\d+)', l03_text)
print(f"L03 split into {len(blocks)} blocks:")
for i, b in enumerate(blocks):
    if b.strip().startswith('真题'):
        lines = [l.strip() for l in b.strip().split('\n') if l.strip()]
        header = lines[0] if len(lines) > 0 else ''
        meta = lines[1] if len(lines) > 1 else ''
        title = lines[2] if len(lines) > 2 else ''
        print(f"Block {i}: Header='{header}', Meta='{meta}', Title='{title}'")
