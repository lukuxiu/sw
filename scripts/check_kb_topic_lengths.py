import sys, json, re

sys.stdout.reconfigure(encoding='utf-8')

with open('src/data/knowledgeBase.ts', 'r', encoding='utf-8') as f:
    text = f.read()

# Match each topic key and its content
matches = re.findall(r'^\s*["\']([a-z0-9_\-]+)["\']:\s*\{(.*?)\n  \},', text, re.MULTILINE | re.DOTALL)
print(f"Matched {len(matches)} topics")

lengths = []
for tid, content in matches:
    # check formulas, steps, pitfalls, candidateMethods count
    f_count = content.count('"title":')
    s_count = content.count('步骤') + content.count('第一步')
    m_count = content.count('"priority":')
    lengths.append((tid, len(content), f_count, m_count))

lengths.sort(key=lambda x: x[1])

print("\nSmallest 15 topics by character length:")
for tid, l, f_c, m_c in lengths[:15]:
    print(f"  {tid}: {l} chars, {f_c} formulas, {m_c} methods")

print("\nLargest 15 topics by character length:")
for tid, l, f_c, m_c in lengths[-15:]:
    print(f"  {tid}: {l} chars, {f_c} formulas, {m_c} methods")
