import json, sys

sys.stdout.reconfigure(encoding='utf-8')
data = json.load(open('scripts/cxy_2021_2026_raw.json', encoding='utf-8'))

unique_questions = {}
for q in data:
    qid = q.get('id')
    if qid not in unique_questions:
        unique_questions[qid] = {
            'cxy_id': qid,
            'source': q.get('source'),
            'original_source': q.get('original_source'),
            'stem': q.get('stem'),
            'option_a': q.get('option_a'),
            'option_b': q.get('option_b'),
            'option_c': q.get('option_c'),
            'option_d': q.get('option_d'),
            'correct_answer': q.get('correct_answer'),
            'answer_explanation': q.get('answer_explanation'),
            'papers': [(q.get('paper_year'), q.get('paper_subject'), q.get('serial_number'))]
        }
    else:
        unique_questions[qid]['papers'].append((q.get('paper_year'), q.get('paper_subject'), q.get('serial_number')))

print(f"Total unique questions: {len(unique_questions)}")

# Check question types
mc = 0
fill = 0
big = 0
for q in unique_questions.values():
    if q['option_a']:
        mc += 1
    elif q['papers'][0][2] <= 16:
        fill += 1
    else:
        big += 1

print(f"Multiple choice: {mc}")
print(f"Fill-in-the-blank (Q11-Q16): {fill}")
print(f"Big questions (Q17-Q22): {big}")

# Sample question from each type
print("\n--- SAMPLE MC ---")
s_mc = [q for q in unique_questions.values() if q['option_a']][0]
print("Stem:", s_mc['stem'])
print("A:", s_mc['option_a'])
print("Ans:", s_mc['correct_answer'])
print("Papers:", s_mc['papers'])

print("\n--- SAMPLE FILL ---")
s_fill = [q for q in unique_questions.values() if not q['option_a'] and q['papers'][0][2] <= 16][0]
print("Stem:", s_fill['stem'])
print("Ans:", s_fill['correct_answer'])
print("Papers:", s_fill['papers'])

print("\n--- SAMPLE BIG ---")
s_big = [q for q in unique_questions.values() if not q['option_a'] and q['papers'][0][2] > 16][0]
print("Stem:", s_big['stem'][:100])
print("Ans:", s_big['correct_answer'])
print("Explanation preview:", s_big['answer_explanation'][:200])
print("Papers:", s_big['papers'])
