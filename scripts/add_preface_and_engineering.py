import json, sys

sys.stdout.reconfigure(encoding='utf-8')

# 1. Update src/data/subjects.ts to include gaoshu-ch00 and gaoshu-ch11
with open('src/data/subjects.ts', 'r', encoding='utf-8') as f:
    subj_code = f.read()

# Add gaoshu-ch00 and gaoshu-ch11 to gaoshu.chapterIds
old_chapter_ids = """    chapterIds: [
      'gaoshu-ch01',
      'gaoshu-ch02',
      'gaoshu-ch03',
      'gaoshu-ch04',
      'gaoshu-ch05',
      'gaoshu-ch06',
      'gaoshu-ch07',
      'gaoshu-ch08',
      'gaoshu-ch09',
      'gaoshu-ch10',
    ],"""

new_chapter_ids = """    chapterIds: [
      'gaoshu-ch00',
      'gaoshu-ch01',
      'gaoshu-ch02',
      'gaoshu-ch03',
      'gaoshu-ch04',
      'gaoshu-ch05',
      'gaoshu-ch06',
      'gaoshu-ch07',
      'gaoshu-ch08',
      'gaoshu-ch09',
      'gaoshu-ch10',
      'gaoshu-ch11',
    ],"""

if old_chapter_ids in subj_code:
    subj_code = subj_code.replace(old_chapter_ids, new_chapter_ids)

# Add chapter definitions before CHAPTERS end
new_chapters_def = """  'gaoshu-ch00': {
    id: 'gaoshu-ch00',
    subjectId: 'gaoshu',
    title: '第 0 编 预备：高中补丁与代数动作',
    order: 0,
    description: '对齐 Maki 大串讲 L01~L02：三角公式体系、指数对数底数转化、五大代数变形动作（配方、有理化、裂项、放缩、换元）与高中函数性质补丁。',
    goals: [
      '熟练运用五大代数变形动作（配方38处、有理化7处、裂项10处）',
      '牢记三角倍角半角积化和差公式与常用不等式 ex >= 1+x, ln(1+x) <= x',
      '识别初等函数在分段点处的单调性与值域范围'
    ],
    topicIds: [
      'gaoshu-00-algebra-five-actions'
    ]
  },
  'gaoshu-ch11': {
    id: 'gaoshu-ch11',
    subjectId: 'gaoshu',
    title: '第 7 编 应试工程：卷面分配与保命进阶清单',
    order: 11,
    description: '对齐 Maki 大串讲 L64~L66：卷面结构与180分钟时间分配、四大失误清单（读题/建模/方法选择/计算）与60-90分保命清单及120-140分进阶清单。',
    goals: [
      '掌握考场 180 分钟黄金时间分配（选填 65 分钟、大题 85 分钟、检查 30 分钟）',
      '熟记读题、建模、方法与计算四大高频踩坑点并形成交卷前自查反射',
      '精准对号入座保命基本盘与高分进阶攻坚考点'
    ],
    topicIds: [
      'yingshi-64-exam-time-structure',
      'yingshi-65-calculation-mistakes-checklist',
      'yingshi-66-survival-and-advanced-checklist'
    ]
  },
"""

if "'gaoshu-ch00':" not in subj_code:
    subj_code = subj_code.replace("export const CHAPTERS: Record<string, ChapterInfo> = {", "export const CHAPTERS: Record<string, ChapterInfo> = {\n" + new_chapters_def)

with open('src/data/subjects.ts', 'w', encoding='utf-8') as f:
    f.write(subj_code)

print("Updated subjects.ts with L01~L02 and L64~L66 chapters.")
