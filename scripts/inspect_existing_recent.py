import json, re, sys

sys.stdout.reconfigure(encoding='utf-8')
data = json.load(open('scripts/extracted_questions.json', encoding='utf-8'))

existing_recent = []
for entry in data:
    qid = entry['item'].get('id', '')
    m = re.match(r'q-(202[1-6])-(\d+)-(\d+)', qid)
    if m:
        year, cat_num, q_num = m.group(1), m.group(2), m.group(3)
        existing_recent.append({
            'id': qid,
            'topicId': entry['topicId'],
            'year': year,
            'category': '数学一' if cat_num == '1' else ('数学二' if cat_num == '2' else '数学三'),
            'qnum': int(q_num),
            'content_snip': entry['item'].get('content', '')[:60].replace('\n', ' ')
        })

print(f"Total existing recent questions: {len(existing_recent)}")
# Let's see some samples
for ex in existing_recent[:10]:
    print(f"[{ex['id']}] {ex['year']} {ex['category']} Q{ex['qnum']} -> {ex['topicId']}")
