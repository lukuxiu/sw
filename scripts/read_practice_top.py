import urllib.request, re, sys

sys.stdout.reconfigure(encoding='utf-8')
content = urllib.request.urlopen('https://cxyonly.fans/assets/LearningPracticePage-WDlT79FY.js', timeout=10).read().decode('utf-8')

print("Top 1000 chars of LearningPracticePage:")
print(content[:1000])
