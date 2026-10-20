import re

with open('src/data/subjects.ts', 'r', encoding='utf-8') as f:
    text = f.read()

chapters = re.findall(r"'([a-z0-9\-]+)':\s*\{\s*id:\s*'([a-z0-9\-]+)',\s*subjectId:\s*'([a-z]+)',\s*title:\s*'([^']+)'[\s\S]*?topicIds:\s*\[([\s\S]*?)\]", text)

print(f'Total chapters found: {len(chapters)}')
all_topics = []
for cid, _, sid, title, t_list in chapters:
    tids = [t.strip().strip("'").strip('"') for t in t_list.split(',') if t.strip().strip("'").strip('"')]
    all_topics.extend(tids)
    print(f'{cid} ({title}) -> {len(tids)} topics: {", ".join(tids)}')

print(f'Total topics: {len(all_topics)}')
