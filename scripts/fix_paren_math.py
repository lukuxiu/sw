with open('src/data/knowledgeBase.ts', 'r', encoding='utf-8') as f:
    text = f.read()

text = text.replace(' = （　　）$', '$ = （　　）')
text = text.replace(' = （　　） $', '$ = （　　）')

with open('src/data/knowledgeBase.ts', 'w', encoding='utf-8', newline='\n') as f:
    f.write(text)

print("Parentheses moved outside math mode!")
