import os, fitz, re, json, sys

sys.stdout.reconfigure(encoding='utf-8')

doc = fitz.open('Maki考研数学一站式大串讲 -2026-version 1.0(1).pdf')

text_p20_35 = ""
for p in range(19, 35):
    text_p20_35 += f"\n--- Page {p+1} ---\n" + doc[p].get_text()

with open('scripts/preface_dump.txt', 'w', encoding='utf-8') as f:
    f.write(text_p20_35)

print("Dumped pages 20-35. Size:", len(text_p20_35))
print(text_p20_35[:2000])
