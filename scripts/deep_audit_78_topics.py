import sys, json, re

sys.stdout.reconfigure(encoding='utf-8')

# We can parse knowledgeBase.ts by reading it
with open('src/data/knowledgeBase.ts', 'r', encoding='utf-8') as f:
    text = f.read()

# We can find all relatedKnowledgeIds to check for dangling links
related_links = re.findall(r'relatedKnowledgeIds["\']?\s*:\s*\[(.*?)\]', text, re.DOTALL)
print(f"Total relatedKnowledgeIds blocks found: {len(related_links)}")

# Extract all topic ids
topic_ids = re.findall(r'["\']([a-z0-9_\-]+-[\w\-]+)["\']:\s*\{', text)
topic_ids_set = set(topic_ids)
print(f"Found {len(topic_ids_set)} topic IDs in knowledgeBase.ts")

# Check all related links
dangling = []
for block in related_links:
    links = re.findall(r'["\']([^"\']+)["\']', block)
    for l in links:
        if l not in topic_ids_set:
            dangling.append(l)

if dangling:
    print(f"WARNING: Found {len(dangling)} dangling related links: {set(dangling)}")
else:
    print("SUCCESS: 0 dangling related links! All related topic capsules link to valid topics!")

# Check for empty fields
empty_summaries = re.findall(r'["\']summary["\']:\s*["\']\s*["\']', text)
print(f"Empty summaries: {len(empty_summaries)}")

# Check for empty triggers
empty_triggers = re.findall(r'["\']triggers["\']:\s*\[\s*\]', text)
print(f"Empty triggers: {len(empty_triggers)}")

# Check for empty steps
empty_steps = re.findall(r'["\']steps["\']:\s*\[\s*\]', text)
print(f"Empty steps: {len(empty_steps)}")

# Check for empty formulas
empty_formulas = re.findall(r'["\']formulas["\']:\s*\[\s*\]', text)
print(f"Empty formulas: {len(empty_formulas)}")
