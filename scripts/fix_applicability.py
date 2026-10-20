# 1. Update types.ts to make applicability optional
with open('src/data/types.ts', 'r', encoding='utf-8') as f:
    text = f.read()

text = text.replace('applicability: string;', 'applicability?: string;')

with open('src/data/types.ts', 'w', encoding='utf-8') as f:
    f.write(text)

# 2. Add applicability to the 4 nodes in knowledgeBase.ts
with open('src/data/knowledgeBase.ts', 'r', encoding='utf-8') as f:
    kb_text = f.read()

nodes_to_patch = [
    "gaoshu-00-algebra-five-actions",
    "yingshi-64-exam-time-structure",
    "yingshi-65-calculation-mistakes-checklist",
    "yingshi-66-survival-and-advanced-checklist"
]

for nid in nodes_to_patch:
    target = f'"{nid}": {{\n    "id": "{nid}",'
    replacement = f'"{nid}": {{\n    "id": "{nid}",\n    "applicability": "全国硕士研究生招生考试数学一、二、三全卷适用",'
    if target in kb_text:
        kb_text = kb_text.replace(target, replacement)

with open('src/data/knowledgeBase.ts', 'w', encoding='utf-8') as f:
    f.write(kb_text)

print("Updated applicability in types.ts and knowledgeBase.ts")
