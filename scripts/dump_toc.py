import os, fitz, sys

sys.stdout.reconfigure(encoding='utf-8')
pdfs = sorted([f for f in os.listdir('.') if f.endswith('.pdf')])
doc0 = fitz.open(pdfs[0])
doc1 = fitz.open(pdfs[1])

print('=== DOC 0 TOC (Lecture list) ===')
for lvl, title, page in doc0.get_toc():
    if lvl <= 2:
        print(f'L{lvl}: {title} (p.{page})')

print('\n=== DOC 1 TOC (Lecture list) ===')
for lvl, title, page in doc1.get_toc():
    if lvl <= 2:
        print(f'L{lvl}: {title} (p.{page})')
