import os, fitz, re, sys

sys.stdout.reconfigure(encoding='utf-8')
pdfs = sorted([f for f in os.listdir('.') if f.endswith('.pdf')])
doc0 = fitz.open(pdfs[0])

# Find positions of all "真题X.Y"
questions = []
for pno in range(len(doc0)):
    txt = doc0[pno].get_text()
    for m in re.finditer(r'真题\s*(\d+\.\d+)\s*\n\s*(20\d\d)\s*[・·]\s*(数[一二三])\s*[・·]\s*(\([^\)]+\)|\d+)', txt):
        q_id = f"真题{m.group(1)}"
        year = m.group(2)
        sub = m.group(3)
        num = m.group(4)
        start_idx = m.start()
        questions.append({
            'page': pno + 1,
            'qid': q_id,
            'year': year,
            'sub': sub,
            'num': num,
            'snippet': txt[start_idx:start_idx+400]
        })

print(f"Total questions found with regex: {len(questions)}")
print("\nFirst 3 questions:")
for q in questions[:3]:
    print(f"[{q['qid']}] {q['year']} {q['sub']} {q['num']} (Page {q['page']}):")
    print(q['snippet'])
    print("="*40)
