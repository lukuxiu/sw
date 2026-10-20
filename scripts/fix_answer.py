with open('src/data/featureIndex.ts', 'r', encoding='utf-8') as f:
    c = f.read()

c = c.replace("answer: q.answer,", "answer: q.answer || '详见解析',")

with open('src/data/featureIndex.ts', 'w', encoding='utf-8') as f:
    f.write(c)

print("Updated answer fallback in featureIndex.ts")
