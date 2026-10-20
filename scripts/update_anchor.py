import json, sys

sys.stdout.reconfigure(encoding='utf-8')

with open('scripts/add_preface_nodes_to_kb.py', 'r', encoding='utf-8') as f:
    code = f.read()

code = code.replace(
    'target = \'"isPending": false\\n  }\\n};\'' ,
    'target = "};\n\nimport { EXTRACTED_PAST_QUESTIONS }"'
)
code = code.replace(
    'text = text.replace(\'"isPending": false\\n  }\\n};\', \'"isPending": false\\n  }\' + insert_str + \'\\n};\')',
    'text = text.replace("};\n\nimport { EXTRACTED_PAST_QUESTIONS }", insert_str + "\\n};\\n\\nimport { EXTRACTED_PAST_QUESTIONS }")'
)

with open('scripts/add_preface_nodes_to_kb.py', 'w', encoding='utf-8') as f:
    f.write(code)

print("Updated anchor in add_preface_nodes_to_kb.py")
