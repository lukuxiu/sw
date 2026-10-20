import json, sys

sys.stdout.reconfigure(encoding='utf-8')
data = json.load(open('scripts/exam_directory.json', encoding='utf-8'))
roots = data.get('data', {}).get('roots', [])
print("Total roots:", len(roots))

exam_papers = []
def walk(node, path):
    curr = path + [node.get('name')]
    children = node.get('children', [])
    if not children:
        exam_papers.append((node.get('id'), " / ".join(curr), node.get('total', 0)))
    else:
        for ch in children:
            walk(ch, curr)

for r in roots:
    walk(r, [])

print("Total leaf papers:", len(exam_papers))
for pid, pname, ptotal in exam_papers:
    if any(y in pname for y in ['2021', '2022', '2023', '2024', '2025', '2026']):
        print(f"[{pid}] {pname} (total={ptotal})")
