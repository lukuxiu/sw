import os, fitz, re, json, sys

sys.stdout.reconfigure(encoding='utf-8')

doc = fitz.open('Maki考研数学一站式大串讲 -2026-version 1.0(1).pdf')

def parse_stats(p_start):
    text = doc[p_start].get_text() + "\n" + doc[p_start + 1].get_text()
    m_total = re.search(r'合计\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+)', text)
    if m_total:
        return {
            'independentQuestions': int(m_total.group(1)),
            'positions': int(m_total.group(2)),
            'choiceCount': int(m_total.group(3)),
            'blankCount': int(m_total.group(4)),
            'solutionCount': int(m_total.group(5)),
            'math1Score': int(m_total.group(6)),
            'math2Score': int(m_total.group(7)),
            'math3Score': int(m_total.group(8)),
        }
    return None

print("L05 stats:", parse_stats(68))
print("L09 stats:", parse_stats(132))
print("L10 stats:", parse_stats(154))
print("L13 stats:", parse_stats(200))
print("L33 stats:", parse_stats(562))
