import json, sys, re

sys.stdout.reconfigure(encoding='utf-8')
data = json.load(open('scripts/cxy_2021_2026_raw.json', encoding='utf-8'))

for i, q in enumerate(data[:15]):
    exp = q.get('answer_explanation', '')
    steps = [s.strip() for s in re.split(r'\n{2,}', exp) if s.strip()]
    print(f"[{q.get('paper_year')} {q.get('paper_subject')} Q{q.get('serial_number')}] len={len(exp)}, steps count={len(steps)}")
    if i < 3:
        for si, st in enumerate(steps[:3]):
            print(f"   Step {si+1}: {st[:80]}...")
