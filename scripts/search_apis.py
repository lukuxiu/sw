import urllib.request, re, sys

sys.stdout.reconfigure(encoding='utf-8')
data = open('scripts/cxy_web.js', encoding='utf-8').read()

# Let's find all chunk filenames loaded
chunks = re.findall(r'["\']([a-zA-Z0-9_\-]+\-[a-zA-Z0-9_\-]+\.js)["\']', data)
print("Found chunks in cxy_web:", set(chunks))

for ch in set(chunks):
    try:
        url = f'https://cxyonly.fans/assets/{ch}'
        content = urllib.request.urlopen(url, timeout=5).read().decode('utf-8')
        # check if it mentions /api/ or questions or daguan
        apis = re.findall(r'/api/[a-zA-Z0-9_\-/]+', content)
        if apis:
            print(f"{ch} has APIs:", set(apis))
    except Exception as e:
        pass
