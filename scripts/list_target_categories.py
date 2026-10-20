import json, sys

sys.stdout.reconfigure(encoding='utf-8')
data = json.load(open('scripts/exam_directory.json', encoding='utf-8'))
roots = data.get('data', {}).get('roots', [])

for r in roots:
    print(f"=== {r.get('label')} (category_id={r.get('category_id')}) ===")
    for c in r.get('children', []):
        if c.get('label') in ['2021', '2022', '2023', '2024', '2025', '2026']:
            print(f"  {c.get('label')}: category_id={c.get('category_id')}, count={c.get('question_count')}")
