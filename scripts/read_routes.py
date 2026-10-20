import urllib.request, re, sys

sys.stdout.reconfigure(encoding='utf-8')
url = 'https://cxyonly.fans/assets/routes-B13Iyr_B.js'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
content = urllib.request.urlopen(req, timeout=10).read().decode('utf-8')

with open('scripts/routes.js', 'w', encoding='utf-8') as f:
    f.write(content)

# Find all path: "..." in routes
paths = re.findall(r'path:\s*["\']([^"\']+)["\']', content)
print("Route paths:", paths)

# Find any lazy-loaded components or dynamic imports
dynamic = re.findall(r'import\(["\']([^"\']+)["\']\)', content)
print("Dynamic in routes:", dynamic)
