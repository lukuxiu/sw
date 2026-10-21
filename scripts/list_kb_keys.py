import sys, re

sys.stdout.reconfigure(encoding='utf-8')

with open('src/data/knowledgeBase.ts', 'r', encoding='utf-8') as f:
    text = f.read()

# Find all keys in export const KNOWLEDGE_BASE: Record<string, KnowledgeNode> = { ... }
keys = re.findall(r'^\s*["\']([a-z0-9_\-]+)["\']:\s*\{', text, re.MULTILINE)
print(f"Total keys found: {len(keys)}")
for k in keys[:30]:
    print(k)
