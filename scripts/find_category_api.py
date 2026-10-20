import re, sys

sys.stdout.reconfigure(encoding='utf-8')
data = open('scripts/main.js', encoding='utf-8').read()
apis = set(re.findall(r'["\'](/api/[a-zA-Z0-9_\-/]+)["\']', data))
print("APIs in main:", apis)
templates = set(re.findall(r'`(/api/[^`\s]+)`', data))
print("Templates in main:", templates)
