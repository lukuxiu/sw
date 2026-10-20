import json, sys

sys.stdout.reconfigure(encoding='utf-8')
data = json.load(open('scripts/extracted_questions.json', encoding='utf-8'))
assigned_topics = set(q['topicId'] for q in data)

with open('src/data/knowledgeBase.ts', 'r', encoding='utf-8') as f:
    import re
    all_topics = set(re.findall(r'"([a-z0-9\-]+)":\s*\{\s*"id":\s*"[^"]+",\s*"title":', f.read()))

print(f"Total topics in KB: {len(all_topics)}")
print(f"Topics with extracted questions: {len(assigned_topics)}")
missing = all_topics - assigned_topics
print(f"Topics without extracted questions ({len(missing)}):")
for t in sorted(missing):
    print(" ", t)
