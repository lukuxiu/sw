import urllib.request, re, sys

sys.stdout.reconfigure(encoding='utf-8')

for name in ['requestClient-C0AlwyhF.js', 'routes-B13Iyr_B.js']:
    url = f'https://cxyonly.fans/assets/{name}'
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            content = resp.read().decode('utf-8')
        print(f"=== {name} (len={len(content)}) ===")
        # Find baseURL, urls, apis
        for m in re.finditer(r'(?:baseURL|baseURL:|api/|https?://)[^\s,\'\"`\)\;]+', content):
            print(" ", m.group(0))
        for m in re.finditer(r'["\'](/[^"\'\s]+)["\']', content):
            if any(k in m.group(1) for k in ['exam', 'practice', 'question', 'math', 'paper', '1029']):
                print("  route/api:", m.group(1))
    except Exception as e:
        print(f"Error {name}:", e)
