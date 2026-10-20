import fitz
import re

doc = fitz.open('Maki考研数学真题分类精解-2026-version 1.0.pdf')

def scan_questions():
    q_map = {}
    for pno in range(len(doc)):
        text = doc[pno].get_text()
        # Find pattern like '题 6.1\n2016 · 数一 · (4)' or '题47.2\n2015 数一 (5)'
        matches = re.finditer(r'(题\s*\d+\.\d+)[\s\n]+((?:19\d\d|20\d\d)\s*[·・\s]\s*数[一二三]\s*[·・\s]?\s*(?:\(\d+\)|\d+))', text)
        for m in matches:
            qid = m.group(1).replace(' ', '')
            meta = m.group(2).replace('\n', ' ')
            q_map[qid] = {'page': pno + 1, 'meta': meta}
    return q_map

q_dict = scan_questions()
print(f'Total questions found: {len(q_dict)}')
for k in list(q_dict.keys())[:30]:
    print(f'  {k}: {q_dict[k]["meta"]} (p.{q_dict[k]["page"]})')
