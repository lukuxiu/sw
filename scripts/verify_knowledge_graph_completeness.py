import os, fitz, re, json, sys

sys.stdout.reconfigure(encoding='utf-8')
doc0 = fitz.open(sorted([f for f in os.listdir('.') if f.endswith('.pdf')])[0])
toc0 = doc0.get_toc()

print(f"Total TOC entries in Doc 0: {len(toc0)}")

# Extract all L01 to L66 lectures and their sub-sections
lectures = []
curr_lec = None

for lvl, title, page in toc0:
    m_lec = re.search(r'L(\d+)\s+([^\s\[]+)', title)
    if m_lec:
        curr_lec = {
            'num': int(m_lec.group(1)),
            'title': m_lec.group(2).strip(),
            'page': page,
            'sections': []
        }
        lectures.append(curr_lec)
    elif lvl >= 3 and curr_lec:
        clean_title = re.sub(r'\[on line.*?\]', '', title).strip()
        curr_lec['sections'].append({
            'lvl': lvl,
            'title': clean_title,
            'page': page
        })

print(f"Extracted {len(lectures)} lectures from 大串讲:")
for l in lectures:
    sec_names = [s['title'] for s in l['sections']]
    print(f"L{l['num']:02d}: {l['title']} -> {len(sec_names)} sections: {', '.join(sec_names[:4])}")
