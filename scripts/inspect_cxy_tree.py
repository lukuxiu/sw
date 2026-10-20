import json, sys

sys.stdout.reconfigure(encoding='utf-8')
data = json.load(open('scripts/cxy_categories.json', encoding='utf-8'))
for i, item in enumerate(data):
    print(f"Top {i}: id={item.get('id')}, name={item.get('name')}, children={len(item.get('children', []))}")

# Recursively search for 1029
def find_node(node, target_id):
    if node.get('id') == target_id:
        return [node.get('name')]
    for child in node.get('children', []):
        res = find_node(child, target_id)
        if res:
            return [node.get('name')] + res
    return None

for top in data:
    path = find_node(top, 1029)
    if path:
        print("Path to 1029:", " -> ".join(path))
