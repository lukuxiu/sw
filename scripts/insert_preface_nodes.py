import json, sys, os

sys.stdout.reconfigure(encoding='utf-8')
sys.path.append(os.path.abspath('scripts'))

import add_preface_nodes_to_kb as mod
new_nodes = mod.new_nodes

# Read knowledgeBase.ts
with open('src/data/knowledgeBase.ts', 'r', encoding='utf-8') as f:
    text = f.read()

# find the import statement
idx = text.find('import { EXTRACTED_PAST_QUESTIONS }')
if idx == -1:
    print("Could not find import statement!")
    sys.exit(1)

# Find the last '};' before this import
semi_idx = text.rfind('};', 0, idx)
if semi_idx == -1:
    print("Could not find }; before import")
    sys.exit(1)

insert_str = ""
for k, v in new_nodes.items():
    if f'"{k}":' not in text:
        insert_str += f',\n  "{k}": ' + json.dumps(v, ensure_ascii=False, indent=2)

new_text = text[:semi_idx] + insert_str + "\n" + text[semi_idx:]

with open('src/data/knowledgeBase.ts', 'w', encoding='utf-8') as f:
    f.write(new_text)

print(f"Inserted {len(new_nodes)} new nodes successfully! Total nodes in KB now.")
