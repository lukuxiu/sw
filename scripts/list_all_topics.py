import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('src/data/subjects.ts', 'r', encoding='utf-8') as f:
    text = f.read()

pattern = re.compile(r"id:\s*'([^']+)',\s*subjectId:\s*'([^']+)',\s*title:\s*'([^']+)'[\s\S]*?topicIds:\s*\[([\s\S]*?)\]")
matches = pattern.findall(text)

with open('src/data/knowledgeBase.ts', 'r', encoding='utf-8') as f:
    kb_text = f.read()

# find all id: '...' and title: '...'
kb_nodes = {}
for m in re.finditer(r"id:\s*'([^']+)',\s*title:\s*'([^']+)'", kb_text):
    kb_nodes[m.group(1)] = m.group(2)

for cid, sub, ctitle, topic_str in matches:
    tids = [t.strip(" '\"\n\r\t") for t in topic_str.split(',') if t.strip(" '\"\n\r\t")]
    print(f"\n=== {cid}: {ctitle} ({sub}) ===")
    for tid in tids:
        title = kb_nodes.get(tid, 'UNKNOWN')
        print(f"  {tid} -> {title}")
