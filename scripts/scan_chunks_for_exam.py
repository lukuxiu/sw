import urllib.request, re, sys, concurrent.futures

sys.stdout.reconfigure(encoding='utf-8')
data = open('scripts/main.js', encoding='utf-8').read()
chunks = sorted(set(re.findall(r'[a-zA-Z0-9_\-]+\-[a-zA-Z0-9_\-]+\.js', data)))
print(f"Total chunks to scan: {len(chunks)}")

def check_chunk(ch):
    try:
        url = f'https://cxyonly.fans/assets/{ch}'
        content = urllib.request.urlopen(url, timeout=5).read().decode('utf-8')
        matches = []
        if '1029' in content:
            matches.append('1029')
        if '历年真题' in content:
            matches.append('历年真题')
        if '全国硕士研究生' in content:
            matches.append('全国硕士研究生')
        if matches:
            return ch, matches
    except:
        pass
    return None

with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
    for res in executor.map(check_chunk, chunks):
        if res:
            print(f"Chunk {res[0]} contains: {res[1]}")
