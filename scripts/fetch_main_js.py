import urllib.request, re, sys

sys.stdout.reconfigure(encoding='utf-8')
url = 'https://cxyonly.fans/assets/main-CLUXkQKR.js'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
try:
    with urllib.request.urlopen(req, timeout=15) as resp:
        content = resp.read().decode('utf-8')
    print('main JS length:', len(content))
    with open('scripts/main.js', 'w', encoding='utf-8') as f:
        f.write(content)
    apis = re.findall(r'/api/[a-zA-Z0-9_\-/]+', content)
    print('APIs in main:', set(apis))
    # find other chunks
    other_chunks = set(re.findall(r'[a-zA-Z0-9_\-]+\-[a-zA-Z0-9_\-]+\.js', content))
    print('Other chunks:', len(other_chunks))
    for c in sorted(other_chunks)[:20]:
        print(' ', c)
except Exception as e:
    print('Error:', e)
