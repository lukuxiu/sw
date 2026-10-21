import os, fitz, re, json, sys

sys.stdout.reconfigure(encoding='utf-8')

doc = fitz.open('Maki考研数学一站式大串讲 -2026-version 1.0(1).pdf')
toc = doc.get_toc()

# Let's map every lecture to its page range
lecture_pages = []
for i, item in enumerate(toc):
    lvl, title, page = item
    m = re.search(r'L(\d+)\s+([^\s\[]+)', title)
    if m:
        lec_num = int(m.group(1))
        clean_title = re.sub(r'\[.*?\]', '', title).strip()
        lecture_pages.append((lec_num, clean_title, page))

# Dedup by lecture num
seen = set()
unique_lecs = []
for num, title, page in lecture_pages:
    if num not in seen:
        seen.add(num)
        unique_lecs.append((num, title, page))

unique_lecs.sort(key=lambda x: x[2])

print(f"Total unique lectures: {len(unique_lecs)}")
for i, (num, title, page) in enumerate(unique_lecs):
    next_page = unique_lecs[i+1][2] if i + 1 < len(unique_lecs) else len(doc)
    page_count = next_page - page
    print(f"L{num:02d} | p.{page:04d}-p.{next_page:04d} ({page_count:2d} pages) | {title}")
