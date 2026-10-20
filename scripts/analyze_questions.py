import os, fitz, re, sys
from collections import Counter

sys.stdout.reconfigure(encoding='utf-8')
pdfs = sorted([f for f in os.listdir('.') if f.endswith('.pdf')])
doc0 = fitz.open(pdfs[0])
doc1 = fitz.open(pdfs[1])

c0 = Counter()
for pno in range(len(doc0)):
    txt = doc0[pno].get_text()
    for m in re.finditer(r'真题\s*(\d+\.\d+)\s*\n\s*(20\d\d)\s*[・·]\s*(数[一二三])\s*[・·]\s*(\([^\)]+\)|\d+)', txt):
        c0[(m.group(2), m.group(3))] += 1

print('Doc 0 (大串讲) counts by year & subject:')
for yr in sorted(set(k[0] for k in c0.keys())):
    sub_str = ', '.join([f'{sub}: {c0[(yr, sub)]}' for sub in ['数一', '数二', '数三'] if (yr, sub) in c0])
    total_yr = sum(c0[(yr, s)] for s in ['数一', '数二', '数三'] if (yr, s) in c0)
    print(f'{yr}: total={total_yr} ({sub_str})')

c1 = Counter()
for pno in range(len(doc1)):
    txt = doc1[pno].get_text()
    for m in re.finditer(r'(?:题|真题)\s*(\d+\.\d+)\s*\n\s*(20\d\d)\s*[・·]\s*(数[一二三])\s*[・·]\s*(\([^\)]+\)|\d+)', txt):
        c1[(m.group(2), m.group(3))] += 1

print('\nDoc 1 (分类精解) counts by year (>=2020):')
for yr in sorted(set(k[0] for k in c1.keys() if int(k[0]) >= 2020)):
    sub_str = ', '.join([f'{sub}: {c1[(yr, sub)]}' for sub in ['数一', '数二', '数三'] if (yr, sub) in c1])
    total_yr = sum(c1[(yr, s)] for s in ['数一', '数二', '数三'] if (yr, s) in c1)
    print(f'{yr}: total={total_yr} ({sub_str})')
