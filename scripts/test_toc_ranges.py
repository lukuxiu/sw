import os, fitz, re, sys

sys.stdout.reconfigure(encoding='utf-8')
doc0 = fitz.open(sorted([f for f in os.listdir('.') if f.endswith('.pdf')])[0])

toc = doc0.get_toc()
lectures = []
for i, item in enumerate(toc):
    lvl, title, page = item
    m = re.search(r'L(\d+)\s+([^\s\[]+)', title)
    if m:
        l_num = int(m.group(1))
        l_name = m.group(2)
        lectures.append({'num': l_num, 'name': l_name, 'start_page': page})

for i in range(len(lectures)):
    if i + 1 < len(lectures):
        lectures[i]['end_page'] = lectures[i+1]['start_page'] - 1
    else:
        lectures[i]['end_page'] = len(doc0)

print(f"Total lectures detected in Doc 0: {len(lectures)}")
print("Sample lectures with page ranges:")
for l in lectures[:10]:
    print(f"L{l['num']:02d}: {l['name']} (p.{l['start_page']} ~ p.{l['end_page']})")
