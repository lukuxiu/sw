import urllib.request, json, sys

sys.stdout.reconfigure(encoding='utf-8')
url = 'https://cxyonly.fans/api/categories?scope=exam'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
with urllib.request.urlopen(req, timeout=10) as resp:
    data = json.loads(resp.read().decode('utf-8'))

with open('scripts/exam_categories_dump.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("Type of data:", type(data))
print("Len:", len(data))
for i, item in enumerate(data):
    print(f"Top {i}: id={item.get('id')}, name={item.get('name')}")
