import sys, re

sys.stdout.reconfigure(encoding='utf-8')

with open('src/data/subjects.ts', 'r', encoding='utf-8') as f:
    subj_text = f.read()

chapters = re.findall(r'id:\s*["\']([^"\']+)["\'],\s*title:\s*["\']([^"\']+)["\'],\s*subject:\s*["\']([^"\']+)["\']', subj_text)

print(f"Total Chapters defined in subjects.ts: {len(chapters)}")
for cid, ctitle, csubj in chapters:
    print(f"  [{csubj}] {cid}: {ctitle}")
