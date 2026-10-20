with open('src/components/FeatureLookupModal.tsx', 'r', encoding='utf-8') as f:
    text = f.read()

old_cat = "{ id: '数理统计与参数估计', label: '数理统计与估计' },"
new_cat = "{ id: '数理统计与参数估计', label: '数理统计与估计' },\n  { id: '应试工程与备考策略', label: '应试工程/失误/保命' },"

text = text.replace(old_cat, new_cat)

with open('src/components/FeatureLookupModal.tsx', 'w', encoding='utf-8') as f:
    f.write(text)

print("Updated FeatureLookupModal.tsx CATEGORIES successfully")
