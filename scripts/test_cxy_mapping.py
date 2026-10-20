import json, re, sys

sys.stdout.reconfigure(encoding='utf-8')

# 1. Existing mappings
existing_data = json.load(open('scripts/extracted_questions.json', encoding='utf-8'))
mapping = {}
cat_map = {'1': '数一', '2': '数二', '3': '数三', '数学一': '数一', '数学二': '数二', '数学三': '数三'}

for entry in existing_data:
    qid = entry['item'].get('id', '')
    tid = entry['topicId']
    m = re.match(r'q-(202[1-6])-(\d+)-(\d+)', qid)
    if m:
        yr = m.group(1)
        sub = '数一' if m.group(2) == '1' else ('数二' if m.group(2) == '2' else '数三')
        qnum = int(m.group(3))
        mapping[(yr, sub, qnum)] = tid
    else:
        # Check source field
        src = entry['item'].get('source', '')
        sm = re.search(r'(202[1-6])\s*(数一|数二|数三|全国[一二三]|数学[一二三])', src)
        qnum_val = entry['item'].get('questionNumber', '')
        qm = re.search(r'(\d+)', str(qnum_val))
        if sm and qm:
            yr = sm.group(1)
            raw_sub = sm.group(2)
            sub = '数一' if '一' in raw_sub else ('数二' if '二' in raw_sub else '数三')
            qnum = int(qm.group(1))
            mapping[(yr, sub, qnum)] = tid

print(f"Total mapped (year, sub, qnum) in existing DB: {len(mapping)}")

# 2. Check cxy questions
cxy_data = json.load(open('scripts/cxy_2021_2026_raw.json', encoding='utf-8'))
mapped_count = 0
unmapped = []

for q in cxy_data:
    yr = q.get('paper_year')
    sub = q.get('paper_subject')
    qnum = q.get('serial_number')
    key = (yr, sub, qnum)
    if key in mapping:
        mapped_count += 1
    else:
        unmapped.append((yr, sub, qnum, q.get('source'), q.get('stem')[:40]))

print(f"CXY questions directly mapped: {mapped_count} / {len(cxy_data)}")
print(f"Unmapped count: {len(unmapped)}")
if unmapped:
    print("Sample unmapped:")
    for u in unmapped[:10]:
        print(" ", u)
