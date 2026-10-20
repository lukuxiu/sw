import json, sys

sys.stdout.reconfigure(encoding='utf-8')
data = json.load(open('scripts/cxy_categories.json', encoding='utf-8'))
def find_id(node, target):
    if node.get('id') == target:
        return node
    for ch in node.get('children', []):
        res = find_id(ch, target)
        if res: return res
    return None

found = False
for top in data:
    node = find_id(top, 836)
    if node:
        found = True
        print('Found 836:', node.get('name'))
        for c in node.get('children', []):
            print(f"  [{c.get('id')}] {c.get('name')}")
        break

if not found:
    print('836 not in categories.json')
