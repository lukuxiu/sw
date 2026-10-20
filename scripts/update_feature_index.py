with open('src/data/featureIndex.ts', 'r', encoding='utf-8') as f:
    text = f.read()

text = text.replace(
    "| '数理统计与参数估计';",
    "| '数理统计与参数估计'\n  | '应试工程与备考策略';"
)

old_cat = """  if (chapterTitle.includes('统计') || chapterTitle.includes('估计')) return '数理统计与参数估计';
  return '极限与连续';"""

new_cat = """  if (chapterTitle.includes('统计') || chapterTitle.includes('估计')) return '数理统计与参数估计';
  if (chapterTitle.includes('应试工程') || chapterTitle.includes('失误清单') || chapterTitle.includes('时间分配') || chapterTitle.includes('保命')) return '应试工程与备考策略';
  return '极限与连续';"""

text = text.replace(old_cat, new_cat)

with open('src/data/featureIndex.ts', 'w', encoding='utf-8') as f:
    f.write(text)

print("Updated featureIndex.ts with 应试工程与备考策略")
