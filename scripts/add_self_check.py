with open('src/data/types.ts', 'r', encoding='utf-8') as f:
    text = f.read()

text = text.replace(
    'whyChooseMethod?: string;',
    'whyChooseMethod?: string;\n  selfCheckList?: string[];'
)

with open('src/data/types.ts', 'w', encoding='utf-8') as f:
    f.write(text)

print("Added selfCheckList to KnowledgeNode in types.ts")
