import json, sys

sys.stdout.reconfigure(encoding='utf-8')
data = json.load(open('scripts/exam_directory.json', encoding='utf-8'))
dir_data = data.get('data', {})
print("Directory keys:", dir_data.keys() if isinstance(dir_data, dict) else len(dir_data))

# Let's inspect the tree or structure
categories = dir_data.get('categories', dir_data.get('items', dir_data.get('tree', dir_data.get('groups', []))))
print("Type of categories:", type(categories), "len:", len(categories))

if isinstance(categories, list):
    for c in categories[:15]:
        print(c)
elif isinstance(dir_data, dict):
    for k, v in dir_data.items():
        print(f"Key: {k}, type: {type(v)}")
        if isinstance(v, list) and len(v) > 0:
            print("  first item:", v[0])
