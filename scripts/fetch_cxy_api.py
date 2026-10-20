import urllib.request, re, sys

sys.stdout.reconfigure(encoding='utf-8')
url = 'https://cxyonly.fans/assets/index-84KKf4wc.js'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
try:
    with urllib.request.urlopen(req, timeout=15) as resp:
        data = resp.read().decode('utf-8')
    print('JS length:', len(data))
    apis = set(re.findall(r'["\'](/(?:api|math|exam|practice|static)[^"\']+)["\']', data))
    print('APIs found:', len(apis))
    for a in sorted(apis)[:50]:
        print(' ', a)
    # Also find any mentions of 1029 or exam endpoint
    for m in re.finditer(r'(?:exam|practice|all)/\d+', data):
        print('Pattern match:', m.group(0))
except Exception as e:
    print('Error:', e)
