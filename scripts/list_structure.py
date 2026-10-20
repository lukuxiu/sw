import re, sys

sys.stdout.reconfigure(encoding='utf-8')
with open('src/data/subjects.ts', 'r', encoding='utf-8') as f:
    text = f.read()

chapters = re.findall(r"'([a-z]+-ch\d+)':\s*\{\s*id:\s*'[a-z]+-ch\d+',\s*subjectId:\s*'([a-z]+)',\s*title:\s*'([^']+)'", text)
print(f"Total chapters: {len(chapters)}")
for cid, sid, title in chapters:
    # find topicIds
    m = re.search(rf"'{cid}':\s*\{{[^}}]*topicIds:\s*\[([^\]]+)\]", text)
    topics = [t.strip().strip("'\"") for t in m.group(1).split(',') if t.strip()] if m else []
    print(f"{cid} ({sid}) {title}: {len(topics)} topics")
