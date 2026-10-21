import os, fitz, re, json, sys

sys.stdout.reconfigure(encoding='utf-8')

doc = fitz.open('Maki考研数学一站式大串讲 -2026-version 1.0(1).pdf')

def check_freq_table(page):
    text = doc[page - 1].get_text() + doc[page].get_text()
    m = re.search(r'本讲真题考频.*?(?=合计|占|$)', text, re.DOTALL)
    if m:
        print(f"p.{page} Found freq table snippet:")
        print(m.group(0)[:500])
    else:
        print(f"p.{page} No freq table pattern matched")

check_freq_table(69) # L05
check_freq_table(133) # L09
check_freq_table(155) # L10
check_freq_table(201) # L13
