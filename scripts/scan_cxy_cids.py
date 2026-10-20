import urllib.request, json, sys

sys.stdout.reconfigure(encoding='utf-8')

for cid in range(1015, 1045):
    url = f'https://cxyonly.fans/api/questions?category_id={cid}&include_children=true&scope=exam'
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=3) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            items = data.get('data', {}).get('items', [])
            total = data.get('data', {}).get('total', 0)
            if total > 0 and len(items) > 0:
                p = items[0].get('category_full_path')
                print(f"[{cid}] total={total}, path={p}")
    except Exception as e:
        pass
