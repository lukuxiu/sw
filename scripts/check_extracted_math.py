import json, re, sys

sys.stdout.reconfigure(encoding='utf-8')

data = json.load(open('scripts/extracted_questions.json', encoding='utf-8'))
print(f"Checking math formatting for {len(data)} items...")

error_count = 0
for i, q in enumerate(data):
    item = q['item']
    text = item['content'] + " " + item['analysis'] + " " + " ".join(item['solutionSteps']) + " " + item['pitfall']
    # Check for unmatched single $
    dollar_count = text.count('$')
    if dollar_count % 2 != 0:
        error_count += 1
        print(f"Unmatched $ in item {i}: {item['id']} ({item['year']} {item['category']} {item['questionNumber']})")

print(f"Total unmatched $ errors: {error_count}")
