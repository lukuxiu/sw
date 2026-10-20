import urllib.request, json, sys, time

sys.stdout.reconfigure(encoding='utf-8')

# Target categories:
target_papers = [
    # 数一
    {"year": "2026", "subject": "数一", "cid": 1029},
    {"year": "2025", "subject": "数一", "cid": 838},
    {"year": "2024", "subject": "数一", "cid": 839},
    {"year": "2023", "subject": "数一", "cid": 840},
    {"year": "2022", "subject": "数一", "cid": 841},
    {"year": "2021", "subject": "数一", "cid": 842},
    # 数二
    {"year": "2026", "subject": "数二", "cid": 1035},
    {"year": "2025", "subject": "数二", "cid": 856},
    {"year": "2024", "subject": "数二", "cid": 857},
    {"year": "2023", "subject": "数二", "cid": 858},
    {"year": "2022", "subject": "数二", "cid": 859},
    {"year": "2021", "subject": "数二", "cid": 860},
    # 数三
    {"year": "2026", "subject": "数三", "cid": 1041},
    {"year": "2025", "subject": "数三", "cid": 874},
    {"year": "2024", "subject": "数三", "cid": 875},
    {"year": "2023", "subject": "数三", "cid": 876},
    {"year": "2022", "subject": "数三", "cid": 877},
    {"year": "2021", "subject": "数三", "cid": 878},
]

all_cxy_questions = []

for p in target_papers:
    cid = p['cid']
    year = p['year']
    subj = p['subject']
    url = f'https://cxyonly.fans/api/questions?category_id={cid}&include_children=true&scope=exam&per_page=50'
    print(f"Fetching {year} {subj} (category_id={cid})...")
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            items = data.get('data', {}).get('items', [])
            print(f"  Got {len(items)} questions.")
            for it in items:
                it['paper_year'] = year
                it['paper_subject'] = subj
                it['paper_cid'] = cid
                all_cxy_questions.append(it)
        time.sleep(0.3)
    except Exception as e:
        print(f"  Error fetching {cid}:", e)

print(f"\nTotal fetched from cxy: {len(all_cxy_questions)} questions.")

with open('scripts/cxy_2021_2026_raw.json', 'w', encoding='utf-8') as f:
    json.dump(all_cxy_questions, f, ensure_ascii=False, indent=2)

print("Saved scripts/cxy_2021_2026_raw.json successfully!")
