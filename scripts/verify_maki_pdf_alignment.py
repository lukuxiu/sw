import os, fitz, re, json, sys

sys.stdout.reconfigure(encoding='utf-8')

pdf_path = "Maki考研数学一站式大串讲 -2026-version 1.0(1).pdf"
if not os.path.exists(pdf_path):
    # find pdf
    pdfs = [f for f in os.listdir('.') if f.endswith('.pdf') and '大串讲' in f]
    pdf_path = pdfs[0]

doc = fitz.open(pdf_path)
print(f"Opened PDF: {pdf_path}")
print(f"Total Pages: {len(doc)}")

toc = doc.get_toc()
print(f"TOC entries: {len(toc)}")

# Extract all chapters / lectures
lectures = []
for lvl, title, page in toc:
    m = re.search(r'L(\d+)\s+([^\s\[]+)', title)
    if m:
        num = int(m.group(1))
        lectures.append((num, title.strip(), page))

print(f"\nExtracted {len(lectures)} Lectures from PDF TOC:")
for num, title, page in lectures:
    print(f"  L{num:02d} (p.{page}): {title}")
