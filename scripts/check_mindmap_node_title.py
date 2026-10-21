import sys

with open('src/components/MindmapView.tsx', 'r', encoding='utf-8') as f:
    text = f.read()

import re
matches = re.findall(r'topicId.*?\{node\.title\}', text)
print(f"Matches for node.title: {len(matches)}")

pos = text.find('node.title')
while pos != -1:
    print(text[pos-100:pos+150])
    print("="*40)
    pos = text.find('node.title', pos + 1)
