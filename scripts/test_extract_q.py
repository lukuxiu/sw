import fitz
import sys
import json
import re

sys.stdout.reconfigure(encoding='utf-8')
doc = fitz.open('Maki考研数学真题分类精解-2026-version 1.0.pdf')

def extract_question_by_keyword(keyword, max_results=3):
    results = []
    for pno in range(len(doc)):
        text = doc[pno].get_text()
        if keyword in text:
            # find question headers
            matches = re.finditer(r'(题\s*\d+\.\d+)[\s\n]+((?:19\d\d|20\d\d)\s*[·・\s]\s*数[一二三]\s*[·・\s]?\s*(?:\(\d+\)|\d+))', text)
            for m in matches:
                qid = m.group(1).replace(' ', '')
                meta = m.group(2).replace('\n', ' ')
                # get text on this page and next page
                raw = doc[pno].get_text() + '\n' + (doc[pno+1].get_text() if pno+1 < len(doc) else '')
                results.append({'qid': qid, 'meta': meta, 'page': pno+1, 'text': raw[:1200]})
                if len(results) >= max_results:
                    return results
    return results

print('Testing extraction for Lecture 6, 7, 8, 25, 33, 49, 62...')
for kw in ['单调有界', '连续性、间断点', '常系数线性微分方程', '极大无关组', '最大似然估计']:
    res = extract_question_by_keyword(kw, 1)
    for r in res:
        print(f"[{r['qid']} {r['meta']} (p.{r['page']})]")
