import urllib.request, json, sys

sys.stdout.reconfigure(encoding='utf-8')

test_cids = [
    # multiples or near 1029
    1023, 1017, 1011, 1005, 999, 993, 987,
    1047, 1053, 1059, 1065,
    # let's try 1020-1045
    1021, 1022, 1024, 1025, 1026, 1027, 1028, 1030, 1031, 1032, 1033, 1034, 1036, 1037, 1038, 1039, 1040, 1042
]

for cid in test_cids:
    url = f'https://cxyonly.fans/api/questions?category_id={cid}&include_children=true&scope=exam'
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=3) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            items = data.get('data', {}).get('items', [])
            total = data.get('data', {}).get('total', 0)
            if total > 0 and len(items) > 0:
                p = items[0].get('category_full_path')
                if '真题' in p:
                    print(f"[{cid}] total={total}, path={p}")
    except Exception as e:
        pass
