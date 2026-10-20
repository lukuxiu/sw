import json, sys

sys.stdout.reconfigure(encoding='utf-8')
data = json.load(open('scripts/exam_directory.json', encoding='utf-8'))
roots = data.get('data', {}).get('roots', [])
print("Root sample:", json.dumps(roots[0], ensure_ascii=False, indent=2)[:500])
