# 1. Update KnowledgeDetailView.tsx
with open('src/components/KnowledgeDetailView.tsx', 'r', encoding='utf-8') as f:
    text = f.read()

text = text.replace(
    '<MathView content={m.condition} inline />',
    '<MathView content={m.condition || m.applicability || ""} inline />'
)
text = text.replace(
    '<MathView content={m.description} inline />',
    '<MathView content={m.description || m.limitations || ""} inline />'
)

with open('src/components/KnowledgeDetailView.tsx', 'w', encoding='utf-8') as f:
    f.write(text)

# 2. Update search.ts
with open('src/data/search.ts', 'r', encoding='utf-8') as f:
    s_text = f.read()

s_text = s_text.replace(
    'm.condition.toLowerCase().includes(clean)',
    '(m.condition || m.applicability || "").toLowerCase().includes(clean)'
)

with open('src/data/search.ts', 'w', encoding='utf-8') as f:
    f.write(s_text)

# 3. Update types.ts to add whyChooseMethod?: string;
with open('src/data/types.ts', 'r', encoding='utf-8') as f:
    t_text = f.read()

t_text = t_text.replace(
    'isPending?: boolean; // 是否待补充',
    'whyChooseMethod?: string;\n  isPending?: boolean; // 是否待补充'
)

with open('src/data/types.ts', 'w', encoding='utf-8') as f:
    f.write(t_text)

print("Updated KnowledgeDetailView.tsx, search.ts, and types.ts successfully.")
