import urllib.request, re, sys

sys.stdout.reconfigure(encoding='utf-8')
url = 'https://cxyonly.fans/assets/web-DlRo4JP-.js'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
try:
    with urllib.request.urlopen(req, timeout=20) as resp:
        data = resp.read().decode('utf-8')
    print('web JS length:', len(data))
    with open('scripts/cxy_web.js', 'w', encoding='utf-8') as f:
        f.write(data)
    print('Saved scripts/cxy_web.js')
    
    # Search for api base or endpoints
    for m in re.finditer(r'(?:https?://[^"\'`\s]+|/api/[^"\'`\s]+)', data):
        print('Found URL:', m.group(0))
        if len(m.group(0)) > 5:
            pass
except Exception as e:
    print('Error:', e)
