with open('src/data/knowledgeBase.ts', 'r', encoding='utf-8') as f:
    text = f.read()

# Fix gaoshu-q-2021-1-10 answer: remove backslash before apostrophe
text = text.replace(r"f_1\'", "f_1'").replace(r"f_2\'", "f_2'").replace(r"f_3\'", "f_3'")

# Fix newline inside cases in q-2025-1-12 and q-2025-1-22
text = text.replace(r'x\le1,\n\end{cases}', r'x\le1\end{cases}')
text = text.replace(r'X\gt100,\n\end{cases}', r'X\gt100\end{cases}')
text = text.replace(r'x\le0.\n\end{cases}', r'x\le0\end{cases}')

with open('src/data/knowledgeBase.ts', 'w', encoding='utf-8', newline='\n') as f:
    f.write(text)

with open('src/data/pastQuestionsData.ts', 'r', encoding='utf-8') as f:
    text2 = f.read()

text2 = text2.replace(r'x\le1,\n\end{cases}', r'x\le1\end{cases}')
text2 = text2.replace(r'X\gt100,\n\end{cases}', r'X\gt100\end{cases}')
text2 = text2.replace(r'x\le0.\n\end{cases}', r'x\le0\end{cases}')

with open('src/data/pastQuestionsData.ts', 'w', encoding='utf-8', newline='\n') as f:
    f.write(text2)

print('Updated both knowledgeBase.ts and pastQuestionsData.ts successfully!')
