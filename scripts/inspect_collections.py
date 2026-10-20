import urllib.request, re, sys

sys.stdout.reconfigure(encoding='utf-8')
for name in ['browseCollections-XNdkNNKc.js', 'questionLists-_tPfai6T.js']:
    url = f'https://cxyonly.fans/assets/{name}'
    try:
        content = urllib.request.urlopen(url, timeout=5).read().decode('utf-8')
        print(f"=== {name} ===")
        # search for API endpoints
        for m in re.finditer(r'/(?:api|v1|questions|categories|lists)[a-zA-Z0-9_\-\/]+', content):
            print("  endpoint:", m.group(0))
    except Exception as e:
        print(f"Err {name}:", e)
