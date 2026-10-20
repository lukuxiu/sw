import json, sys

sys.stdout.reconfigure(encoding='utf-8')

with open('scripts/add_preface_nodes_to_kb.py', 'r', encoding='utf-8') as f:
    code = f.read()

code = code.replace('"isPending": false', '"isPending": False')

with open('scripts/add_preface_nodes_to_kb.py', 'w', encoding='utf-8') as f:
    f.write(code)

print("Fixed boolean in script.")
