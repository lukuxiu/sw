import os, fitz, sys

sys.stdout.reconfigure(encoding='utf-8')
pdfs = sorted([f for f in os.listdir('.') if f.endswith('.pdf')])
doc1 = fitz.open(pdfs[1])

print('=== DOC 1 YEAR INDEX (p.1507-1510) ===')
for p in range(1506, 1512):
    print(f'--- PAGE {p+1} ---')
    print(doc1[p].get_text()[:1500])
