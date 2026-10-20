import glob, re, sys

sys.stdout.reconfigure(encoding='utf-8')
for fpath in glob.glob('scripts/*.js'):
    content = open(fpath, encoding='utf-8', errors='ignore').read()
    if '836' in content:
        print(f"836 in {fpath}:")
        for m in re.finditer(r'836', content):
            start = max(0, m.start() - 80)
            end = min(len(content), m.end() + 80)
            print("  ", repr(content[start:end]))
