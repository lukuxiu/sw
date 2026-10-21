import os, fitz, re, json, sys

sys.stdout.reconfigure(encoding='utf-8')

doc = fitz.open('Maki考研数学一站式大串讲 -2026-version 1.0(1).pdf')

def inspect_lecture(num, page):
    print(f"\n=================== L{num:02d} (p.{page}) ===================")
    text = ""
    for p in range(page - 1, min(page + 2, len(doc))):
        text += doc[p].get_text()
    print(text[:1500])

inspect_lecture(1, 35)
inspect_lecture(9, 133)
inspect_lecture(10, 155)
inspect_lecture(16, 269)
inspect_lecture(53, 923)
inspect_lecture(65, 1089)
