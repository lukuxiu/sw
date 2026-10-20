import re, sys

sys.stdout.reconfigure(encoding='utf-8')
data = open('scripts/routes.js', encoding='utf-8').read()
routes = re.findall(r'\{id:`([^`]+)`,pattern:([^,\}]+)', data)
for r in routes:
    print(r)
