import re, glob, sys

sys.stdout.reconfigure(encoding='utf-8')
for fpath in glob.glob('scripts/*.js'):
    text = open(fpath, encoding='utf-8', errors='ignore').read()
    if '1029' in text:
        print(f"Found 1029 in {fpath}")
    m = re.findall(r'/categories/[^\s"\'`\)]+', text)
    if m:
        print(f"Categories endpoints in {fpath}:", set(m))
