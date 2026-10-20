import fitz
import sys

sys.stdout.reconfigure(encoding='utf-8')

doc_zhenti = fitz.open('Maki考研数学真题分类精解-2026-version 1.0.pdf')
toc = doc_zhenti.get_toc()
for item in toc[40:]:
    lvl, title, page = item
    if lvl <= 2:
        print(f"{'  '*(lvl-1)}{title} (p.{page})")
