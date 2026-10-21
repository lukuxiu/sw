import os, fitz, re, json, sys

sys.stdout.reconfigure(encoding='utf-8')

doc = fitz.open('Maki考研数学一站式大串讲 -2026-version 1.0(1).pdf')
toc = doc.get_toc()

lectures = []
curr_lec = None

for lvl, title, page in toc:
    m_lec = re.search(r'L(\d+)\s+([^\s\[]+)', title)
    if m_lec:
        lec_num = int(m_lec.group(1))
        curr_lec = {
            'num': lec_num,
            'title': title.strip(),
            'page': page,
            'subsections': []
        }
        lectures.append(curr_lec)
    elif lvl >= 3 and curr_lec:
        curr_lec['subsections'].append({
            'title': title.strip(),
            'page': page
        })

for l in lectures[15:]:
    sub_titles = [s['title'] for s in l['subsections']]
    print(f"L{l['num']:02d} (p.{l['page']:04d}): {l['title']}")
    for st in sub_titles:
        print(f"    - {st}")
