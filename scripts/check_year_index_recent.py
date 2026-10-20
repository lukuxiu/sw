import os, fitz, sys

sys.stdout.reconfigure(encoding='utf-8')
pdfs = sorted([f for f in os.listdir('.') if f.endswith('.pdf')])
doc1 = fitz.open(pdfs[1])

print('=== DOC 1 YEAR INDEX 2021~2026 ===')
for p in range(1516, 1523):
    txt = doc1[p].get_text()
    if any(yr in txt for yr in ['2021', '2022', '2023', '2024', '2025', '2026']):
        print(f'--- PAGE {p+1} ---')
        print(txt)
