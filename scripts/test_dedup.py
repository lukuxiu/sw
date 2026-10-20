import json, sys

sys.stdout.reconfigure(encoding='utf-8')
data = json.load(open('scripts/cxy_2021_2026_raw.json', encoding='utf-8'))

ids = {}
hashes = {}

for q in data:
    qid = q.get('id')
    chash = q.get('content_hash')
    src = q.get('source')
    p_yr = q.get('paper_year')
    p_sub = q.get('paper_subject')
    s_num = q.get('serial_number')
    
    if qid not in ids:
        ids[qid] = []
    ids[qid].append((p_yr, p_sub, s_num))
    
    if chash not in hashes:
        hashes[chash] = []
    hashes[chash].append((p_yr, p_sub, s_num))

dup_ids = {k: v for k, v in ids.items() if len(v) > 1}
dup_hashes = {k: v for k, v in hashes.items() if len(v) > 1}

print(f"Total entries: {len(data)}")
print(f"Unique question IDs: {len(ids)}")
print(f"Questions appearing in multiple papers by ID: {len(dup_ids)}")
print(f"Unique content hashes: {len(hashes)}")
print(f"Questions appearing in multiple papers by hash: {len(dup_hashes)}")

# Print a few samples of duplicates
print("\nSample duplicate questions:")
for k, v in list(dup_ids.items())[:8]:
    sample_q = [x for x in data if x.get('id') == k][0]
    print(f"ID={k}, source='{sample_q.get('source')}'")
    print(f"  Appeared in: {v}")
