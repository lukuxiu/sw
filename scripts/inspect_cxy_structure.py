import json, sys

sys.stdout.reconfigure(encoding='utf-8')
data = json.load(open('scripts/cxy_2021_2026_raw.json', encoding='utf-8'))
print(f"Total questions: {len(data)}")

# Inspect a question
q = data[0]
print("Keys:", list(q.keys()))
print("Sample:")
print("  source:", q.get('source'))
print("  source_tags:", q.get('source_tags'))
print("  original_source:", q.get('original_source'))
print("  serial_number:", q.get('serial_number'))
print("  stem:", q.get('stem')[:100])
print("  option_a:", q.get('option_a'))
print("  option_b:", q.get('option_b'))
print("  correct_answer:", q.get('correct_answer'))
print("  answer_explanation:", q.get('answer_explanation')[:150])
