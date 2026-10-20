import urllib.request, re, sys

sys.stdout.reconfigure(encoding='utf-8')
content = urllib.request.urlopen('https://cxyonly.fans/assets/LearningPracticePage-WDlT79FY.js', timeout=10).read().decode('utf-8')

# Search for /question-lists/ or /lists/ or /practice/
matches = set(re.findall(r'["\'](/[^"\'\s]+)["\']', content))
for m in sorted(matches):
    if any(k in m for k in ['question', 'list', 'category', 'directory', 'exam']):
        print("Match:", m)

templates = set(re.findall(r'`(/[^`\s]+)`', content))
for t in sorted(templates):
    if any(k in t for k in ['question', 'list', 'category', 'directory', 'exam']):
        print("Template:", t)
