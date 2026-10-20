import os, fitz, re, sys

sys.stdout.reconfigure(encoding='utf-8')
pdfs = sorted([f for f in os.listdir('.') if f.endswith('.pdf')])
doc1 = fitz.open(pdfs[1])

# Scan for questions in Doc 1
questions_recent = []
for pno in range(len(doc1)):
    txt = doc1[pno].get_text()
    for m in re.finditer(r'(?:题|真题)\s*(\d+\.\d+)\s*\n\s*(202[1-6])\s*[・·]\s*(数[一二三])\s*[・·]\s*(\([^\)]+\)|\d+)', txt):
        qid = f"题{m.group(1)}"
        yr = m.group(2)
        sub = m.group(3)
        num = m.group(4)
        start_idx = m.start()
        questions_recent.append({
            'page': pno + 1,
            'qid': qid,
            'year': yr,
            'sub': sub,
            'num': num,
            'snippet': txt[start_idx:start_idx+300]
        })

print(f"Total 2021~2026 questions found in Doc 1: {len(questions_recent)}")
print("\nFirst 5 recent questions in Doc 1:")
for q in questions_recent[:5]:
    print(f"[{q['qid']}] {q['year']} {q['sub']} {q['num']} (Page {q['page']}):")
    print(q['snippet'].replace('\n', ' ')[:140])
    print("-" * 40)
