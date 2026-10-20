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
            idx = m.end()
            q_preview = text[idx:idx+250].replace('\n', ' ').strip()
            print(f"[{qid}] {meta} (p.{pno+1}) -> {q_preview[:120]}...")
            if q_count >= 6:
                return

search_lecture(1048, 1062, "第四十三讲 行列式")
search_lecture(1063, 1095, "第四十四~四十五讲 矩阵运算与秩")
search_lecture(1096, 1113, "第四十六讲 向量组线性相关性")
search_lecture(1114, 1172, "第四十七~四十八讲 线性方程组")
search_lecture(1173, 1229, "第四十九~五十讲 特征值与相似对角化")
search_lecture(1244, 1299, "第五十二讲 二次型")
