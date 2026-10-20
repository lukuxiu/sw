import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('src/data/knowledgeBase.ts', 'r', encoding='utf-8') as f:
    text = f.read()

json_str = text.split('export const KNOWLEDGE_BASE: Record<string, KnowledgeNode> = ')[1].rstrip(';\n\r ')
kb = json.loads(json_str)

print(f"Total entries loaded: {len(kb)}")

queries = ['2025', '0/0', '格林公式', '贝叶斯', '伴随矩阵', '极大似然', '正定', '泰勒', '欧拉方程', '狄利克雷']

for q in queries:
    matched = []
    for k, v in kb.items():
        v_dump = json.dumps(v, ensure_ascii=False)
        if q in v_dump:
            matched.append(k)
    print(f"Query '{q}' -> {len(matched)} matches: {matched[:3]}...")
