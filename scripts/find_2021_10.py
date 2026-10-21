with open('src/data/knowledgeBase.ts', 'r', encoding='utf-8') as f:
    text = f.read()

import re
pos = text.find('gaoshu-q-2021-1-10')
print(text[pos:pos+500])
