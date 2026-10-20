import urllib.request, ssl, re, sys

sys.stdout.reconfigure(encoding='utf-8')
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'https://cxyonly.fans/assets/web-DtPe6gsE.js'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
js = urllib.request.urlopen(req, context=ctx, timeout=10).read().decode('utf-8', errors='ignore')

# search chunk imports
chunks = re.findall(r'["\'](/assets/[^"\']+\.js)["\']', js)
print("Chunks referenced in web.js:", chunks)
