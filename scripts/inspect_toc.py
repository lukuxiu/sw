import fitz
import sys

sys.stdout.reconfigure(encoding='utf-8')

doc_chuanjiang = fitz.open('Maki考研数学一站式大串讲 -2026-version 1.0(1).pdf')
toc = doc_chuanjiang.get_toc()
print(f"Total TOC entries in 大串讲: {len(toc)}")
for item in toc[:40]:
    lvl, title, page = item
    print(f"{'  '*(lvl-1)}{title} (p.{page})")
