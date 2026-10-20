import urllib.request, json, sys

sys.stdout.reconfigure(encoding='utf-8')
endpoints = [
    '/api/v1/learning-concepts/collection-catalog',
    '/api/categories',
    '/api/questions/categories',
    '/api/categories/tree',
    '/api/learning-concepts',
    '/api/exam-papers',
    '/api/exam/papers',
    '/api/exams',
    '/api/questions/tags'
]

for ep in endpoints:
    url = f'https://cxyonly.fans{ep}'
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=5) as resp:
            data = resp.read().decode('utf-8')
            print(f"[OK] {ep}: len={len(data)}")
            try:
                obj = json.loads(data)
                print("   keys:", list(obj.keys()) if isinstance(obj, dict) else len(obj))
            except:
                pass
    except urllib.error.HTTPError as e:
        print(f"[{e.code}] {ep}")
    except Exception as e:
        print(f"[ERR] {ep}:", e)
