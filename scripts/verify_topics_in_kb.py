import sys, re

sys.stdout.reconfigure(encoding='utf-8')

with open('src/data/subjects.ts', 'r', encoding='utf-8') as f:
    subj_text = f.read()

with open('src/data/knowledgeBase.ts', 'r', encoding='utf-8') as f:
    kb_text = f.read()

# Extract all topicIds in CHAPTERS
topic_ids_in_chapters = re.findall(r"['\"]([a-z0-9_\-]+-[\w\-]+)['\"]", subj_text)
# Filter out chapter ids and subject ids
topic_ids_in_chapters = [
    t for t in topic_ids_in_chapters 
    if not t.endswith(('-ch00', '-ch01', '-ch02', '-ch03', '-ch04', '-ch05', '-ch06', '-ch07', '-ch08', '-ch09', '-ch10', '-ch11'))
    and t not in ('gaoshu', 'xiandai', 'gailv')
]

# Dedup preserving order
seen = set()
unique_topics = []
for t in topic_ids_in_chapters:
    if t not in seen:
        seen.add(t)
        unique_topics.append(t)

print(f"Total Unique Topics referenced in subjects.ts: {len(unique_topics)}")

missing = []
for tid in unique_topics:
    # Check if tid is in knowledgeBase.ts
    if f'"{tid}":' not in kb_text and f"'{tid}':" not in kb_text:
        missing.append(tid)

if missing:
    print(f"CRITICAL ERROR: {len(missing)} topics missing from KNOWLEDGE_BASE:")
    for m in missing:
        print(f"  MISSING: {m}")
else:
    print("SUCCESS: 100% of topics in subjects.ts exist in KNOWLEDGE_BASE!")

# Check topic counts per subject
by_subj = {}
for t in unique_topics:
    prefix = t.split('-')[0]
    by_subj[prefix] = by_subj.get(prefix, 0) + 1

print("\nTopics by Subject in Mindmap:")
for p, c in by_subj.items():
    print(f"  {p}: {c} topics")
