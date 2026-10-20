import urllib.request, json, sys

sys.stdout.reconfigure(encoding='utf-8')
url = 'https://cxyonly.fans/api/categories'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
with urllib.request.urlopen(req, timeout=10) as resp:
    data = resp.read().decode('utf-8')
with open('scripts/cxy_categories.json', 'w', encoding='utf-8') as f:
    f.write(data)

obj = json.loads(data)
print("Keys:", obj.keys() if isinstance(obj, dict) else len(obj))
cats = obj.get('data', [])
print("Categories count:", len(cats))
if len(cats) > 0:
    print("Sample category:", json.dumps(cats[0], ensure_ascii=False, indent=2))
    # find category 1029
    c1029 = [c for c in cats if c.get('id') == 1029 or c.get('category_id') == 1029]
    print("1029 match:", c1029)
