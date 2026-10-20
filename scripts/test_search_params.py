import urllib.request, json, sys

sys.stdout.reconfigure(encoding='utf-8')
for p in ['year=2026', 'q=2026', 'source=2026', 'search=2026', 'source_tags=2026', 'keyword=2026']:
    url = f'https://cxyonly.fans/api/questions?scope=exam&{p}&per_page=5'
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=5) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            print(f"{p}: total={data.get('data', {}).get('total')}")
            for it in data.get('data', {}).get('items', [])[:2]:
                print(f"   item source: {it.get('source')}")
    except Exception as e:
        print(f"{p}: err {e}")
