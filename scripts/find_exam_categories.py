import urllib.request, json, sys

sys.stdout.reconfigure(encoding='utf-8')

for q in [
    '?scope=exam',
    '?type=exam',
    '?mode=exam',
    '?kind=exam',
    '?tree_type=exam',
    '?category_type=exam',
    '?is_exam=true'
]:
    url = f'https://cxyonly.fans/api/categories{q}'
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=5) as resp:
            data = resp.read().decode('utf-8')
            print(f"URL: {url} -> len={len(data)}")
            obj = json.loads(data)
            # check if 1029 in data string
            if '1029' in data:
                print(f"  FOUND 1029 in {url}!")
                with open('scripts/exam_categories.json', 'w', encoding='utf-8') as f:
                    f.write(data)
    except Exception as e:
        print(f"Err {url}:", e)
