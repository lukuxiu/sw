import json, sys

sys.stdout.reconfigure(encoding='utf-8')
data = json.load(open('scripts/cxy_categories.json', encoding='utf-8'))

found = []
def search_all(node, path):
    curr_path = path + [f"{node.get('name')} (id={node.get('id')})"]
    if node.get('id') == 1029 or '1029' in str(node.get('id')):
        found.append(" -> ".join(curr_path))
    for child in node.get('children', []):
        search_all(child, curr_path)

for top in data:
    search_all(top, [])

print("Found 1029 occurrences:", found)
if not found:
    # print all leaf node IDs and names
    leafs = []
    def get_leafs(node, path):
        curr_path = path + [f"{node.get('name')} (id={node.get('id')})"]
        if not node.get('children'):
            leafs.append((node.get('id'), " -> ".join(curr_path)))
        else:
            for child in node.get('children'):
                get_leafs(child, curr_path)
    for top in data:
        get_leafs(top, [])
    print(f"Total leaf categories: {len(leafs)}")
    print("Sample leafs:")
    for lid, lp in leafs[:10]:
        print(f"  [{lid}] {lp}")
