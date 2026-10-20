import os, fitz, re, sys

sys.stdout.reconfigure(encoding='utf-8')
doc1 = fitz.open(sorted([f for f in os.listdir('.') if f.endswith('.pdf')])[1])

toc1 = doc1.get_toc()
lectures1 = []
chinese_num_map = {
    '一': 1, '二': 2, '三': 3, '四': 4, '五': 5, '六': 6, '七': 7, '八': 8, '九': 9, '十': 10,
    '十一': 11, '十二': 12, '十三': 13, '十四': 14, '十五': 15, '十六': 16, '十七': 17, '十八': 18, '十九': 19, '二十': 20,
    '二十一': 21, '二十二': 22, '二十三': 23, '二十四': 24, '二十五': 25, '二十六': 26, '二十七': 27, '二十八': 28, '二十九': 29, '三十': 30,
    '三十一': 31, '三十二': 32, '三十三': 33, '三十四': 34, '三十五': 35, '三十六': 36, '三十七': 37, '三十八': 38, '三十九': 39, '四十': 40,
    '四十一': 41, '四十二': 42, '四十三': 43, '四十四': 44, '四十五': 45, '四十六': 46, '四十七': 47, '四十八': 48, '四十九': 49, '五十': 50,
    '五十一': 51, '五十二': 52, '五十三': 53, '五十四': 54, '五十五': 55, '五十六': 56, '五十七': 57, '五十八': 58, '五十九': 59, '六十': 60,
    '六十一': 61, '六十二': 62, '六十三': 63, '六十四': 64, '六十五': 65, '六十六': 66
}

for item in toc1:
    lvl, title, page = item
    m = re.search(r'第([一二三四五六七八九十]+)讲\s+([^\s]+)', title)
    if m:
        c_num = m.group(1)
        num = chinese_num_map.get(c_num, 0)
        name = m.group(2)
        lectures1.append({'num': num, 'c_num': c_num, 'name': name, 'start_page': page})

for i in range(len(lectures1)):
    if i + 1 < len(lectures1):
        lectures1[i]['end_page'] = lectures1[i+1]['start_page'] - 1
    else:
        lectures1[i]['end_page'] = len(doc1)

print(f"Total lectures detected in Doc 1: {len(lectures1)}")
print("Sample lectures with page ranges in Doc 1:")
for l in lectures1[:10]:
    print(f"L{l['num']:02d} (第{l['c_num']}讲): {l['name']} (p.{l['start_page']} ~ p.{l['end_page']})")
