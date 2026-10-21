import sys, re

sys.stdout.reconfigure(encoding='utf-8')

with open('src/data/knowledgeBase.ts', 'r', encoding='utf-8') as f:
    text = f.read()

target = "gaoshu-02-mean-value-theorems"
pos = text.find(f'"{target}":')
if pos != -1:
    end_pos = text.find('\n  },', pos)
    block = text[pos:end_pos+4]
    print(f"Topic: {target}, length: {len(block)}")
    print("--- CONTENT ---")
    print(block)
