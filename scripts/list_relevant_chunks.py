import re, sys

sys.stdout.reconfigure(encoding='utf-8')
content = open('scripts/main.js', encoding='utf-8').read()
chunks = sorted(set(re.findall(r'[a-zA-Z0-9_\-]+\-[a-zA-Z0-9_\-]+\.js', content)))
for c in chunks:
    if any(k in c.lower() for k in ['practice', 'exam', 'question', 'catalog', 'category', 'paper']):
        print("Relevant chunk:", c)
