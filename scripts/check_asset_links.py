import json, sys

sys.stdout.reconfigure(encoding='utf-8')
data = json.load(open('scripts/cxy_2021_2026_raw.json', encoding='utf-8'))

cnt = 0
for q in data:
    exp = q.get('answer_explanation', '')
    if '### 原始参考答案' in exp or 'asset://' in exp:
        cnt += 1

print(f"Questions with original answer image attachment: {cnt}")
