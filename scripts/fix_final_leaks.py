# 1. Fix knowledgeBase.ts
with open('src/data/knowledgeBase.ts', 'r', encoding='utf-8') as f:
    kb_text = f.read()

kb_text = kb_text.replace(r"f_1\'", "f_1'").replace(r"f_2\'", "f_2'").replace(r"f_3\'", "f_3'")
kb_text = kb_text.replace(r"\\'", "'")

with open('src/data/knowledgeBase.ts', 'w', encoding='utf-8', newline='\n') as f:
    f.write(kb_text)

# 2. Fix pastQuestionsData.ts
with open('src/data/pastQuestionsData.ts', 'r', encoding='utf-8') as f:
    pq_text = f.read()

pq_text = pq_text.replace(r'x\le1,\n\end{cases}', r'x\le1\end{cases}')
pq_text = pq_text.replace(r'X\gt100,\n\end{cases}', r'X\gt100\end{cases}')
pq_text = pq_text.replace(r'x\le0.\n\end{cases}', r'x\le0\end{cases}')

with open('src/data/pastQuestionsData.ts', 'w', encoding='utf-8', newline='\n') as f:
    f.write(pq_text)

print("Final leaks fixed!")
