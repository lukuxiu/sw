import json, re, sys

sys.stdout.reconfigure(encoding='utf-8')

# Read knowledgeBase nodes
with open('src/data/knowledgeBase.ts', 'r', encoding='utf-8') as f:
    txt = f.read()

# match "id": "...", "title": "...", "source": "..."
nodes = re.findall(r'"([a-z0-9\-]+)":\s*\{\s*"id":\s*"([^"]+)",\s*"title":\s*"([^"]+)"[\s\S]*?"source":\s*"([^"]+)"', txt)
print(f"Total topics in KNOWLEDGE_BASE: {len(nodes)}")

mapped_lecs = set()
for tid, _, title, src in nodes:
    m = re.findall(r'L(\d+)', src)
    for l in m:
        mapped_lecs.add(int(l))

print(f"Lectures directly referenced in source ({len(mapped_lecs)}):", sorted(mapped_lecs))
missing_lecs = [i for i in range(3, 64) if i not in mapped_lecs]
print(f"Lectures not directly referenced in source tag (L03~L63): {missing_lecs}")
