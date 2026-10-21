import os, fitz, re, json, sys

sys.stdout.reconfigure(encoding='utf-8')

doc = fitz.open('Maki考研数学一站式大串讲 -2026-version 1.0(1).pdf')

# Let's inspect page 17-25 (course map & preface)
text_p19_25 = ""
for p in range(16, 25):
    text_p19_25 += f"\n--- Page {p+1} ---\n" + doc[p].get_text()

print("Length of preface/map text:", len(text_p19_25))
print(text_p19_25[:2500])
