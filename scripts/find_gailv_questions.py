import fitz
import sys
import re

sys.stdout.reconfigure(encoding='utf-8')
doc = fitz.open('Maki考研数学真题分类精解-2026-version 1.0.pdf')

def search_lecture(start_page, end_page, lecture_name):
    print(f"\n================ {lecture_name} (pp. {start_page}-{end_page}) ================")
    q_count = 0
    for pno in range(start_page-1, min(end_page, len(doc))):
        text = doc[pno].get_text()
        matches = list(re.finditer(r'(题\s*\d+\.\d+)[\s\n]+((?:19\d\d|20\d\d)\s*[·・\s]\s*数[一二三]\s*[·・\s]?\s*(?:\(\d+\)|\d+))', text))
        for m in matches:
            q_count += 1
            qid = m.group(1).replace(' ', '')
            meta = m.group(2).replace('\n', ' ')
            # grab first 300 chars of question text
            idx = m.end()
            q_preview = text[idx:idx+250].replace('\n', ' ').strip()
            print(f"[{qid}] {meta} (p.{pno+1}) -> {q_preview[:120]}...")
            if q_count >= 8:
                return

# Sample search for Lectures 54, 55, 57, 58, 59, 62
search_lecture(1302, 1325, "第五十四讲 随机事件与概率")
search_lecture(1326, 1342, "第五十五~五十六讲 一维随机变量")
search_lecture(1343, 1368, "第五十七~五十八讲 二维随机变量")
search_lecture(1369, 1441, "第五十九讲 数字特征")
search_lecture(1460, 1495, "第六十二讲 参数估计")
