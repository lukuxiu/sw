import os, json, re, sys

sys.stdout.reconfigure(encoding='utf-8')

with open('src/data/knowledgeBase.ts', 'r', encoding='utf-8') as f:
    kb_text = f.read()

topic_ids = re.findall(r'^\s*["\']([a-z0-9_\-]+)["\']:\s*\{', kb_text, re.MULTILINE)
print(f"Total topics in KB: {len(topic_ids)}")

# Let's inspect topic titles and map them to L01~L66
topic_map = {}
for tid in topic_ids:
    pos = kb_text.find(f'"{tid}":')
    if pos != -1:
        end = kb_text.find('\n  },', pos)
        block = kb_text[pos:end+4]
        m_title = re.search(r'"title":\s*"([^"]+)"', block)
        m_subj = re.search(r'"subject":\s*"([^"]+)"', block)
        m_ch = re.search(r'"chapterId":\s*"([^"]+)"', block)
        topic_map[tid] = {
            'id': tid,
            'title': m_title.group(1) if m_title else '',
            'subject': m_subj.group(1) if m_subj else '',
            'chapterId': m_ch.group(1) if m_ch else ''
        }

print("Sample topics:")
for k, v in list(topic_map.items())[:10]:
    print(f"  {k} -> {v['title']} ({v['chapterId']})")
