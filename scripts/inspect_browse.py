import urllib.request, re, sys

sys.stdout.reconfigure(encoding='utf-8')
for ch in ['LearningMathLayout-Bae6tojH.js', 'browse-CQ2uUAyP.js']:
    url = f'https://cxyonly.fans/assets/{ch}'
    content = urllib.request.urlopen(url, timeout=5).read().decode('utf-8')
    print(f"=== {ch} ===")
    for m in re.finditer(r'历年真题', content):
        start = max(0, m.start() - 150)
        end = min(len(content), m.end() + 150)
        print(repr(content[start:end]))
