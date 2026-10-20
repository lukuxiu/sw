import os, fitz, re, json, sys

sys.stdout.reconfigure(encoding='utf-8')
pdfs = sorted([f for f in os.listdir('.') if f.endswith('.pdf')])
doc0 = fitz.open(pdfs[0]) # 大串讲
doc1 = fitz.open(pdfs[1]) # 分类精解

print(f"Doc0: {pdfs[0]} ({len(doc0)} pages)")
print(f"Doc1: {pdfs[1]} ({len(doc1)} pages)")

# Test extracting a question from Doc 0 (大串讲)
pno = 49 # page 50
txt = doc0[pno].get_text()
print("Sample text from Doc 0 p.50:")
print(txt[:1000])
