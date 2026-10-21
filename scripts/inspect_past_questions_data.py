import os, sys, json, re
from collections import Counter

sys.stdout.reconfigure(encoding='utf-8')

with open('src/data/pastQuestionsData.ts', 'r', encoding='utf-8') as f:
    text = f.read()

q_years = re.findall(r'["\']year["\']:\s*["\'](\d{4})["\']', text)
print(f"Total questions in pastQuestionsData.ts: {len(q_years)}")

counts = Counter(q_years)
print("\nYear breakdown in pastQuestionsData.ts:")
for y in sorted(counts.keys(), reverse=True):
    print(f"  {y}: {counts[y]} questions")

# Count multi-paper badges (数一 / 数二 / 数三)
shared_papers = re.findall(r'["\']category["\']:\s*["\']([^"\']*/[^"\']*)["\']', text)
print(f"\nShared questions across multiple papers (e.g. 数一 / 数二): {len(shared_papers)}")

# Count distinct question IDs
q_ids = re.findall(r'["\']id["\']:\s*["\']([^"\']+)["\']', text)
print(f"Distinct question IDs: {len(set(q_ids))}")

# Check Maki vs CXY sources
sources = re.findall(r'["\']source["\']:\s*["\']([^"\']+)["\']', text)
maki_count = sum(1 for s in sources if 'Maki' in s)
cxy_count = sum(1 for s in sources if '202' in s or 'cxy' in s or '考研' in s)
print(f"\nSource distribution:")
print(f"  - Maki 精解例题: {maki_count} 道")
print(f"  - 2021~2026 最新去重全真题: {len(sources) - maki_count} 道")
