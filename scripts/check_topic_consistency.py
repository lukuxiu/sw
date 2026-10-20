import json, sys

sys.stdout.reconfigure(encoding='utf-8')
data = json.load(open('scripts/cxy_2021_2026_raw.json', encoding='utf-8'))
mapping = json.load(open('scripts/test_cxy_mapping.py', encoding='utf-8')) if False else None

# Load mapping from earlier
import re
existing_data = json.load(open('scripts/extracted_questions.json', encoding='utf-8'))
mapping = {}
for entry in existing_data:
    qid = entry['item'].get('id', '')
    tid = entry['topicId']
    m = re.match(r'q-(202[1-6])-(\d+)-(\d+)', qid)
    if m:
        yr = m.group(1)
        sub = '数一' if m.group(2) == '1' else ('数二' if m.group(2) == '2' else '数三')
        qnum = int(m.group(3))
        mapping[(yr, sub, qnum)] = tid

unique_q = {}
for q in data:
    qid = q.get('id')
    if qid not in unique_q:
        unique_q[qid] = []
    unique_q[qid].append((q.get('paper_year'), q.get('paper_subject'), q.get('serial_number')))

diff_topics = []
for qid, papers in unique_q.items():
    topics = set(mapping.get(p) for p in papers if p in mapping)
    if len(topics) > 1:
        diff_topics.append((qid, papers, topics))

print(f"Total unique questions: {len(unique_q)}")
print(f"Questions mapped to multiple topics: {len(diff_topics)}")
for qid, papers, topics in diff_topics:
    print(f"ID {qid} ({papers}) -> {topics}")
