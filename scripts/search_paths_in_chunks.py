import urllib.request, re, sys

sys.stdout.reconfigure(encoding='utf-8')
for name in ['LearningQuestionBankPage-Dr2nLP2Y.js', 'knowledgeCatalog-DDoim7za.js', 'QuestionListsPage-ClI7ZIQG.js', 'CollectionKnowledgeFilter-YEmEQkcf.js']:
    url = f'https://cxyonly.fans/assets/{name}'
    try:
        content = urllib.request.urlopen(url, timeout=10).read().decode('utf-8')
        # find string literals starting with /
        matches = set(re.findall(r'["\'](/[^"\'\s]+)["\']', content))
        rel = [m for m in matches if any(k in m for k in ['category', 'categories', 'question', 'exam', 'concept', 'catalog', 'paper', 'list'])]
        print(f"=== {name} ===")
        for r in sorted(rel):
            print(" ", r)
        # also template literals
        templates = set(re.findall(r'`(/[^`\s]+)`', content))
        rel_t = [t for t in templates if any(k in t for k in ['category', 'question', 'exam', 'concept', 'catalog'])]
        for t in sorted(rel_t):
            print("  template:", t)
    except Exception as e:
        print(f"Error {name}:", e)
