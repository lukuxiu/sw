import re, sys

sys.stdout.reconfigure(encoding='utf-8')

with open('src/data/knowledgeBase.ts', 'r', encoding='utf-8') as f:
    text = f.read()

# Replace applicability with condition
text = text.replace('"applicability":', '"condition":')
# Replace limitations with description
text = text.replace('"limitations":', '"description":')

# In CandidateMethod objects under gaoshu-00 and yingshi-, add priority: 1, 2, ...
def fix_candidate_methods(block):
    # add "priority": 1, 2, 3 if missing
    def repl(m):
        return m.group(1) + '\n        "priority": 1,'
    return re.sub(r'(\{\s*"name":\s*"[^"]+",)', repl, block)

# Also in coreFormulas replace "name": with "title":
lines = text.split('\n')
in_core = False
for i, line in enumerate(lines):
    if '"coreFormulas":' in line:
        in_core = True
    elif in_core:
        if ']' in line:
            in_core = False
        elif '"name":' in line:
            lines[i] = line.replace('"name":', '"title":')

text = '\n'.join(lines)

# Ensure CandidateMethod has priority and description
# For CandidateMethod without priority:
text = re.sub(r'(\{\s*"name":\s*"[^"]+",)(?!\s*"priority")', r'\1\n        "priority": 1,', text)

with open('src/data/knowledgeBase.ts', 'w', encoding='utf-8') as f:
    f.write(text)

print("Fixed candidateMethod and formulaItem fields in knowledgeBase.ts")
