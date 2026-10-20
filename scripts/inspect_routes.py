import urllib.request, re, sys

sys.stdout.reconfigure(encoding='utf-8')
url = 'https://cxyonly.fans/assets/routes-B13Iyr_B.js'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
content = urllib.request.urlopen(req, timeout=10).read().decode('utf-8')

for m in re.finditer(r'[a-zA-Z0-9_\-]+\-[a-zA-Z0-9_\-]+\.js', content):
    print("referenced chunk:", m.group(0))
