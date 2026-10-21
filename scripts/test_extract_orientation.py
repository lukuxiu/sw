import os, fitz, re, json, sys

sys.stdout.reconfigure(encoding='utf-8')

doc = fitz.open('Maki考研数学一站式大串讲 -2026-version 1.0(1).pdf')

# Let's test on L01 to L15
from extract_all_66_lectures import dedup_lecs

for l in dedup_lecs[:15]:
    p = l['page'] - 1
    text = doc[p].get_text()
    if p + 1 < len(doc):
        text += doc[p + 1].get_text()
    
    # search for 本讲定位
    m_orient = re.search(r'本讲定位[：:](.*?)(?:定理/公式|三卷的基本盘|本讲真题考频|三条局部性质|定义|一、|1\.|\n\n)', text, re.DOTALL)
    orient = m_orient.group(1).strip() if m_orient else "无定位文本"
    orient = re.sub(r'\s+', ' ', orient)
    print(f"{l['id']} {l['title']}:")
    print(f"  定位: {orient[:120]}...")
