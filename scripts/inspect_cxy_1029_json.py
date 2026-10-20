import json, sys

sys.stdout.reconfigure(encoding='utf-8')
data = json.load(open('scripts/cxy_1029.json', encoding='utf-8'))
print("Code:", data.get('code'))
print("Message:", data.get('message'))
items = data.get('data', [])
print("Type of data:", type(items))
if isinstance(items, dict):
    print("Dict keys:", items.keys())
    items = items.get('list', items.get('items', items.get('questions', [])))
if isinstance(items, list):
    print("Count of questions in 1029:", len(items))
    if len(items) > 0:
        first = items[0]
        print("First question keys:", first.keys() if isinstance(first, dict) else type(first))
        print("First question sample:")
        print(json.dumps(first, ensure_ascii=False, indent=2)[:800])
