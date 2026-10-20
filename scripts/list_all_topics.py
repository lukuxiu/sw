import re, json, sys

sys.stdout.reconfigure(encoding='utf-8')
with open('src/data/knowledgeBase.ts', 'r', encoding='utf-8') as f:
    text = f.read()

# Match each topic id and title
matches = re.findall(r'"([a-z0-9\-]+)":\s*\{\s*"id":\s*"([^"]+)",\s*"title":\s*"([^"]+)"', text)
print(f"Total topics in KNOWLEDGE_BASE: {len(matches)}")
for tid, _, title in matches:
    print(f"{tid}: {title}")
