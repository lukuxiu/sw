with open('src/data/knowledgeBase.ts', 'r', encoding='utf-8') as f:
    text = f.read()

# Revert condition back to applicability
text = text.replace('"condition":', '"applicability":')

# In the 4 new nodes (gaoshu-00 and yingshi-), fix steps, formulas, variants
text = text.replace('"standardSteps":', '"steps":')
text = text.replace('"coreFormulas":', '"formulas":')
text = text.replace('"variantExercises":', '"variants":')

# In CandidateMethod inside the 4 new nodes, ensure priority and description
# Remove any duplicate priority
text = text.replace('"priority": 1,\n        "priority": 1,', '"priority": 1,')

with open('src/data/knowledgeBase.ts', 'w', encoding='utf-8') as f:
    f.write(text)

print("Exact types in knowledgeBase.ts restored and aligned with KnowledgeNode interface.")
