import urllib.request, re, sys

sys.stdout.reconfigure(encoding='utf-8')
content = urllib.request.urlopen('https://cxyonly.fans/assets/LearningPracticePage-WDlT79FY.js', timeout=10).read().decode('utf-8')

for m in re.finditer(r'listId', content):
    start = max(0, m.start() - 100)
    end = min(len(content), m.end() + 100)
    print("--- listId match ---")
    print(repr(content[start:end]))
