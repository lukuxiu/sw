with open('src/components/KnowledgeDetailView.tsx', 'r', encoding='utf-8') as f:
    text = f.read()

text = text.replace(
    '<MathView content={node.applicability} inline />',
    '<MathView content={node.applicability || "适用于考研数学相关考点题型"} inline />'
)

with open('src/components/KnowledgeDetailView.tsx', 'w', encoding='utf-8') as f:
    f.write(text)

print("Fixed node.applicability fallback in KnowledgeDetailView.tsx")
