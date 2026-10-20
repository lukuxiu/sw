import json
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('src/data/knowledgeBase.ts', 'r', encoding='utf-8') as f:
    text = f.read()

# strip 'import ...' and 'export const KNOWLEDGE_BASE: Record<string, KnowledgeNode> = ' and trailing ';'
json_part = text.split('export const KNOWLEDGE_BASE: Record<string, KnowledgeNode> = ')[1].rstrip(';\n\r ')
kb = json.loads(json_part)

print(f"Total entries in knowledgeBase: {len(kb)}")
pending = [k for k, v in kb.items() if v.get('isPending', False)]
with_q = [k for k, v in kb.items() if len(v.get('pastQuestions', [])) > 0]
print(f"With questions: {len(with_q)}")
print(f"Pending: {len(pending)}")

# List how many topics per subject
counts = {}
for k, v in kb.items():
    sub = v.get('subject', 'unknown')
    counts[sub] = counts.get(sub, 0) + 1
print("Counts by subject:", counts)
