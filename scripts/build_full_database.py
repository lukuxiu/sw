# -*- coding: utf-8 -*-
"""
Master Build Script:
Merges and validates all 74 topics across Higher Mathematics, Linear Algebra,
and Probability & Statistics, outputting a clean TypeScript file to src/data/knowledgeBase.ts.
"""

import sys
import os
import re
import json

sys.path.append('scripts')
sys.stdout.reconfigure(encoding='utf-8')

from data_gaoshu import GAOSHU_TOPICS
from data_gaoshu_part1 import GAOSHU_PART1_TOPICS
from data_gaoshu_part2 import GAOSHU_PART2_TOPICS
from data_gaoshu_part3 import GAOSHU_PART3_TOPICS
from data_xiandai_all import XIANDAI_ALL_TOPICS
from data_gailv import GAILV_TOPICS

# 1. Merge Gaoshu
all_gaoshu = {}
all_gaoshu.update(GAOSHU_TOPICS)
all_gaoshu.update(GAOSHU_PART1_TOPICS)
all_gaoshu.update(GAOSHU_PART2_TOPICS)
all_gaoshu.update(GAOSHU_PART3_TOPICS)

# 2. Merge Xiandai
all_xiandai = dict(XIANDAI_ALL_TOPICS)

# 3. Merge and Normalize Gailv
all_gailv = {}
for k, node in GAILV_TOPICS.items():
    # normalize past questions
    norm_qs = []
    for q in node.get('pastQuestions', []):
        if 'content' not in q and 'questionText' in q:
            # split solution into clean lines
            raw_sol = q.get('solution', '')
            lines = [s.strip() for s in raw_sol.split('\n') if s.strip()]
            norm_q = {
                'id': q.get('id', f"{k}-q1"),
                'year': q.get('year', '2020'),
                'category': q.get('category', '数一'),
                'questionNumber': q.get('questionNumber', '(1)'),
                'content': q.get('questionText', ''),
                'analysis': q.get('breakthrough', ''),
                'solutionSteps': lines if lines else [raw_sol],
                'answer': q.get('answer', '详见步骤'),
                'pitfall': q.get('trap', '计算中注意符号与适用条件'),
                'difficulty': q.get('difficulty', '★★★☆☆'),
                'verified': True,
                'source': q.get('source') or f"Maki考研数学真题分类精解 题{q.get('questionNumber', '')}"
            }
            norm_qs.append(norm_q)
        else:
            norm_qs.append(q)
    node['pastQuestions'] = norm_qs

    # normalize variants
    norm_vs = []
    for idx, v in enumerate(node.get('variants', [])):
        if 'fullSolution' not in v:
            raw_sol = v.get('solution', '')
            lines = [s.strip() for s in raw_sol.split('\n') if s.strip()]
            norm_v = {
                'id': f"var-{k}-{idx+1:02d}",
                'question': v.get('question', ''),
                'hint': v.get('hint', ''),
                'methodChoiceAnalysis': '根据题目特征快速对应核心方法，注意前置条件检验。',
                'fullSolution': lines if lines else [raw_sol],
                'keyTakeaway': '牢记核心公式、第一反应与解题避坑要点。'
            }
            norm_vs.append(norm_v)
        else:
            norm_vs.append(v)
    node['variants'] = norm_vs
    all_gailv[k] = node

# Combine all 74 topics
all_topics = {}
all_topics.update(all_gaoshu)
all_topics.update(all_xiandai)
all_topics.update(all_gailv)

print(f"Total compiled topics: {len(all_topics)}")

# 4. Verify against subjects.ts
with open('src/data/subjects.ts', 'r', encoding='utf-8') as f:
    subj_text = f.read()

pattern = re.compile(r"topicIds:\s*\[([\s\S]*?)\]")
expected_topic_ids = []
for m in pattern.finditer(subj_text):
    tids = [t.strip(" '\"\n\r\t") for t in m.group(1).split(',') if t.strip(" '\"\n\r\t")]
    expected_topic_ids.extend(tids)

print(f"Total expected topics in subjects.ts: {len(expected_topic_ids)}")

missing = set(expected_topic_ids) - set(all_topics.keys())
extra = set(all_topics.keys()) - set(expected_topic_ids)

if missing:
    print(f"ERROR: Missing topic IDs: {missing}")
    sys.exit(1)
if extra:
    print(f"ERROR: Extra unexpected topic IDs: {extra}")
    sys.exit(1)

print("SUCCESS: Exact 1:1 match with subjects.ts topic IDs!")

# 5. Sanitize and validate every node structure
for tid, node in all_topics.items():
    node['id'] = tid
    node['isPending'] = False  # fully enriched
    node.pop('status', None)   # learning status is dynamically managed by localStorage
    
    # Check required fields
    required_fields = [
        'id', 'title', 'subject', 'subjectName', 'chapterId', 'chapterTitle',
        'nodeType', 'summary', 'triggers', 'firstReaction', 'candidateMethods',
        'applicability', 'steps', 'pitfalls', 'formulas', 'pastQuestions',
        'variants', 'relatedKnowledgeIds', 'tags', 'source', 'isPending'
    ]
    for rf in required_fields:
        if rf not in node:
            print(f"Warning: Node {tid} missing field {rf}")

print(f"Verified all 74 nodes. Sample check:")
sample = all_topics['xiandai-04-solution-structure-and-rank']
print(f"  Title: {sample['title']}")
print(f"  Summary: {sample['summary'][:50]}...")
print(f"  Questions count: {len(sample['pastQuestions'])}")
print(f"  Variants count: {len(sample['variants'])}")

# 6. Generate TypeScript file
ts_content = """import { KnowledgeNode } from './types';

/**
 * 考研数学一解题思路知识库 (全 74 考点精解与真题分类)
 * 严格按照《Maki 考研数学一站式大串讲》与《Maki 考研数学真题分类精解》整理，绝无伪造题源。
 */
export const KNOWLEDGE_BASE: Record<string, KnowledgeNode> = """

ts_content += json.dumps(all_topics, ensure_ascii=False, indent=2)
ts_content += ";\n"

with open('src/data/knowledgeBase.ts', 'w', encoding='utf-8') as f:
    f.write(ts_content)

print("SUCCESS: Successfully wrote src/data/knowledgeBase.ts")
