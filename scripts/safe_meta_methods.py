import re, json

with open('scripts/generate_full_meta_methods.py', 'r', encoding='utf-8') as f:
    content = f.read()

match = re.search(r'meta_methods_code\s*=\s*"""(.*?)"""', content, re.DOTALL)
if not match:
    print("Could not find meta_methods_code")
    exit(1)

code = match.group(1)
lines = code.split('\n')

new_lines = []
for idx, line in enumerate(lines):
    # Pattern 1: property with single quotes:
    # whitespace + key: + whitespace + ' + text + '(,?)\s*$
    prop_match = re.match(r'^(\s*[a-zA-Z0-9_]+:\s*)\'(.*)\'(,?)\s*$', line)
    # Pattern 2: array element with single quotes:
    # whitespace + ' + text + '(,?)\s*$
    arr_match = re.match(r'^(\s*)\'(.*)\'(,?)\s*$', line)
    
    if prop_match:
        prefix, val, comma = prop_match.groups()
        # Escape any unescaped single quotes inside val, OR turn into double quotes!
        # If we turn into double quotes:
        # Note: in Python string, LaTeX was \\\\int -> in code it has \\int.
        # If we use json.dumps for the val string:
        # json.dumps(val) will produce "..." with all quotes and backslashes safely escaped for JS!
        # But wait! Does val contain \\ or \ ?
        # Let's check!
        new_line = f"{prefix}{json.dumps(val, ensure_ascii=False)}{comma}"
        new_lines.append(new_line)
    elif arr_match and not line.strip().startswith('//') and not line.strip().startswith('/*') and not line.strip().startswith('*'):
        prefix, val, comma = arr_match.groups()
        new_line = f"{prefix}{json.dumps(val, ensure_ascii=False)}{comma}"
        new_lines.append(new_line)
    else:
        new_lines.append(line)

new_code = '\n'.join(new_lines)
with open('src/data/metaMethods.ts', 'w', encoding='utf-8') as f:
    f.write(new_code)

print("Saved safely to src/data/metaMethods.ts!")
