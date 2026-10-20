import json, re, sys

sys.stdout.reconfigure(encoding='utf-8')
data = open('src/data/pastQuestionsData.ts', encoding='utf-8').read()
cats = set(re.findall(r'"category":\s*"([^"]+)"', data))
print('Categories:', cats)
