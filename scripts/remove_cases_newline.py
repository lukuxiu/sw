for fn in ['src/data/knowledgeBase.ts', 'src/data/pastQuestionsData.ts']:
    with open(fn, 'r', encoding='utf-8') as f:
        text = f.read()

    # Replace literal newline before \end{cases}
    text = text.replace(',\\n\\end{cases}', '\\end{cases}')
    text = text.replace(',\n\\end{cases}', '\\end{cases}')
    text = text.replace('.\\n\\end{cases}', '\\end{cases}')
    text = text.replace('.\n\\end{cases}', '\\end{cases}')

    with open(fn, 'w', encoding='utf-8', newline='\n') as f:
        f.write(text)

print("Newline in cases removed!")
