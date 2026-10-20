import urllib.request, json, sys

sys.stdout.reconfigure(encoding='utf-8')
endpoints = [
    '/api/categories/836',
    '/api/categories?listId=exam',
    '/api/categories?list_id=exam',
    '/api/categories?root_id=836',
    '/api/categories?root_category_id=836',
    '/api/categories?parent_id=836',
    '/api/categories/tree?root_id=836',
    '/api/lists/exam',
    '/api/question-lists/exam'
]

for ep in endpoints:
    url = f'https://cxyonly.fans{ep}'
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=5) as resp:
            data = resp.read().decode('utf-8')
            print(f"[OK] {ep}: len={len(data)}")
            if len(data) < 2000:
                print("   data:", data[:300])
    except urllib.error.HTTPError as e:
        print(f"[{e.code}] {ep}")
    except Exception as e:
        print(f"[ERR] {ep}:", e)
