import re, sys

sys.stdout.reconfigure(encoding='utf-8')
data = open('scripts/cxy_web.js', 'r', encoding='utf-8').read()
imports = re.findall(r'import\s*\(\s*["\']([^"\']+)["\']\s*\)', data)
print("Dynamic imports:", imports)
chunks = set(re.findall(r'[a-zA-Z0-9_\-]+\-[a-zA-Z0-9_\-]+\.js', data))
print("Chunks mentioned:", chunks)
