import urllib.request, re, sys

sys.stdout.reconfigure(encoding='utf-8')
chunks = [
    'LearningPracticePage-WDlT79FY.js',
    'LearningQuestionPage-Buj13ma7.js',
    'QuestionSolutionPage-Yt9IS_ZU.js',
    'LearningQuestionCard-koXxKD7J.js',
    'knowledgeCatalog-DDoim7za.js'
]

for ch in chunks:
    try:
        url = f'https://cxyonly.fans/assets/{ch}'
        content = urllib.request.urlopen(url, timeout=10).read().decode('utf-8')
        print(f"=== {ch} ({len(content)}) ===")
        # Find paths passed to api
        for m in re.finditer(r'["\'](/api/[^"\'\s]+)["\']', content):
            print("  API string:", m.group(1))
        # Find template literals with api
        for m in re.finditer(r'`(/api/[^`\s]+)`', content):
            print("  API template:", m.group(1))
        # Find mentions of exam or questions
        for m in re.finditer(r'`/(?:practice|questions|exam)[^`\s]+`', content):
            print("  Path template:", m.group(0))
    except Exception as e:
        print(f"Error {ch}:", e)
