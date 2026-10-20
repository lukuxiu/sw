import os, fitz, re, json, sys
from test_full_parser_logic import (
    doc0, doc1, lec_ranges0, lec_ranges1, DEFAULT_LEC_TOPIC,
    parse_questions_from_text
)

sys.stdout.reconfigure(encoding='utf-8')

all_extracted = []

print("Extracting questions from Doc 0 (大串讲)...")
for lr in lec_ranges0:
    l_num = lr['num']
    if l_num not in DEFAULT_LEC_TOPIC:
        continue
    default_tid = DEFAULT_LEC_TOPIC[l_num]
    
    # Read text of all pages in this lecture
    lec_text = ""
    for p in range(lr['start'] - 1, lr['end']):
        if p < len(doc0):
            lec_text += "\n" + doc0[p].get_text()
            
    res = parse_questions_from_text(lec_text, l_num, default_tid, source_type="doc0")
    all_extracted.extend(res)
    print(f"Doc0 L{l_num:02d} ({lr['name']}): extracted {len(res)} questions")

print(f"\nTotal extracted from Doc 0: {len(all_extracted)}")

print("\nExtracting 2021~2026 questions from Doc 1 (分类精解)...")
doc1_count = 0
for lr in lec_ranges1:
    l_num = lr['num']
    if l_num not in DEFAULT_LEC_TOPIC:
        continue
    default_tid = DEFAULT_LEC_TOPIC[l_num]
    
    lec_text = ""
    for p in range(lr['start'] - 1, lr['end']):
        if p < len(doc1):
            lec_text += "\n" + doc1[p].get_text()
            
    res = parse_questions_from_text(lec_text, l_num, default_tid, source_type="doc1")
    # Filter only 2021~2026 questions
    recent_res = [q for q in res if q['item']['year'] in ['2021', '2022', '2023', '2024', '2025', '2026']]
    all_extracted.extend(recent_res)
    doc1_count += len(recent_res)
    if len(recent_res) > 0:
        print(f"Doc1 L{l_num:02d} ({lr['name']}): extracted {len(recent_res)} questions from 2021~2026")

print(f"\nTotal extracted from Doc 1 (2021~2026): {doc1_count}")
print(f"Grand Total questions extracted: {len(all_extracted)}")

# Deduplicate by (year, category, questionNumber, topicId)
seen = set()
unique_questions = []
for q in all_extracted:
    item = q['item']
    key = (item['year'], item['category'], item['questionNumber'], q['topicId'])
    if key not in seen:
        seen.add(key)
        unique_questions.append(q)

print(f"Unique questions after deduplication: {len(unique_questions)}")

# Save to JSON
with open('scripts/extracted_questions.json', 'w', encoding='utf-8') as f:
    json.dump(unique_questions, f, ensure_ascii=False, indent=2)

print("Saved to scripts/extracted_questions.json")
