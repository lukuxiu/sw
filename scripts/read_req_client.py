import sys

sys.stdout.reconfigure(encoding='utf-8')
data = open('scripts/requestClient-C0AlwyhF.js', encoding='utf-8').read() if False else None
# Let's read requestClient from cxy
import urllib.request
content = urllib.request.urlopen('https://cxyonly.fans/assets/requestClient-C0AlwyhF.js', timeout=10).read().decode('utf-8')
print("Len:", len(content))
for line in content.split(';'):
    if any(k in line for k in ['http', 'api', 'url', 'fetch', 'axios']):
        print("Line:", line[:120])
