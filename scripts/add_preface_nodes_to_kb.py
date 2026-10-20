import json, sys

sys.stdout.reconfigure(encoding='utf-8')

new_nodes = {
  "gaoshu-00-algebra-five-actions": {
    "id": "gaoshu-00-algebra-five-actions",
    "title": "代数变形五大动作与高中公式补丁 (L01~L02)",
    "subject": "gaoshu",
    "subjectName": "高等数学",
    "chapterId": "gaoshu-ch00",
    "chapterTitle": "第 0 编 预备：高中补丁与代数动作",
    "nodeType": "topic",
    "summary": "Maki 预备篇核心：高等数学计算卡壳 80% 源于代数变形不熟练。必须掌握五大动作（配方、有理化、裂项、放缩、换元）与高中三角/指数不等式补丁。",
    "triggers": [
      "式中含二次三项式形如 x^2 + px + q（反常积分、二次型、有理积分）",
      "含根号差式形如 \\sqrt{A} - \\sqrt{B} 处于分子或分母",
      "数列或级数通项形如 \\frac{1}{n(n+k)} 或 \\frac{1}{n(n+1)(n+2)}",
      "极限与不等式证明中出现 e^x, \\ln(1+x), \\sin x, \\tan x 混合",
      "初等函数定义域、反函数与初等三角积化和差与和差化积"
    ],
    "firstReaction": "第一反应：不要死算！先观察属于五大代数动作的哪一种：遇二次式想配方，遇根号差想有理化，遇分式乘积想裂项，遇超越函数想切线放缩。",
    "candidateMethods": [
      {
        "name": "配方法（真题调用 38 处第一高频）",
        "applicability": "出现 $x^2 + px + q$ 或多变量二次型",
        "whyChoose": "配成 $(x + \\frac{p}{2})^2 + (q - \\frac{p^2}{4})$ 转化为标准变量代换（如 $\\int \\frac{1}{x^2+2x+5}dx$ 换元为 $\\arctan$ 积分）。",
        "limitations": "配方时注意括号外常数符号，切忌符号抄错。"
      },
      {
        "name": "有理化（共轭无理式脱根号）",
        "applicability": "根号相减未定式、渐近线斜率求 $b$、分母根号化简",
        "whyChoose": "乘共轭式 $(\\sqrt{A}+\\sqrt{B})$ 将无理差化为有理差 $(A-B)$，迅速暴露主要无穷小阶数。",
        "limitations": "只有两项为同阶无穷大或同阶差时才能有效消去主要项。"
      },
      {
        "name": "裂项相消（级数求和与数列极限利器）",
        "applicability": "分母为因式连乘乘积形式",
        "whyChoose": "待定系数拆分 $\\frac{1}{n(n+1)} = \\frac{1}{n} - \\frac{1}{n+1}$，相加后中间全部抵消仅余首尾两项。",
        "limitations": "注意核对拆分系数 $\\frac{1}{k}$ 是否遗漏。"
      },
      {
        "name": "常用经典不等式放缩",
        "applicability": "夹逼准则、单调有界证明、不等式放缩",
        "whyChoose": "牢记切线不等式：$e^x \\ge 1+x$（$x=0$ 取等）、$\\ln(1+x) \\le x$（$x>-1$）、$\\sin x < x < \\tan x$（$x \\in (0, \\pi/2)$）。",
        "limitations": "放缩必须保留主部，不可放得过粗导致极限不一致。"
      }
    ],
    "standardSteps": [
      "第一步：识别结构特征（二次式、根号差、连乘分母、超越因式）。",
      "第二步：执行五大动作之一：配方、有理化、裂项、放缩或整体换元。",
      "第三步：核验高中三角补丁：倍角公式 $\\cos 2x = 2\\cos^2 x - 1 = 1 - 2\\sin^2 x$ 与降幂公式。",
      "第四步：带入微积分主干算法（求极限、求导、求积分、特征多项式分解）。"
    ],
    "coreFormulas": [
      {
        "name": "核心不等式放缩链",
        "latex": "e^x \\ge 1+x,\\quad \\ln(1+x) \\le x,\\quad \\frac{x}{1+x} \\le \\ln(1+x) \\le x",
        "notes": "考研高数四大金刚不等式，常用于夹逼与单调性分析"
      },
      {
        "name": "二倍角与降幂公式",
        "latex": "\\sin^2 x = \\frac{1-\\cos 2x}{2},\\quad \\cos^2 x = \\frac{1+\\cos 2x}{2}",
        "notes": "三角积分与定积分计算的基石转化公式"
      }
    ],
    "pitfalls": [
      "有理化时盲目分子分母同乘，没有先提取公因子，导致多项式越来越庞大",
      "配方时忽视二次项系数不为 1 的情形，提取负号时常数项忘记变号",
      "裂项相消时漏写相消后保留的最后几项与负号"
    ],
    "whyChooseMethod": "L02 归纳的五个代数动作用在后面 60 多讲的真题演练里，是保证运算顺畅的基础基本功。",
    "pastQuestions": [],
    "variantExercises": [],
    "selfCheckList": [
      "能否在 5 秒内默写出 e^x >= 1+x 与 ln(1+x) <= x 的等号成立条件？",
      "遇到 1/(x^2 + 2x + 5) 是否能瞬间本能完成配方 (x+1)^2 + 4？",
      "遇到 \\sqrt{x^2+x} - x 是否能迅速有理化得到极限为 1/2？"
    ],
    "relatedKnowledgeIds": [
      "gaoshu-01-indeterminate-0-0",
      "gaoshu-03-variable-limit-integral"
    ],
    "tags": ["五大动作", "配方", "有理化", "裂项", "不等式放缩"],
    "source": "Maki考研数学大串讲 L01 & L02",
    "isPending": False
  },
  "yingshi-64-exam-time-structure": {
    "id": "yingshi-64-exam-time-structure",
    "title": "卷面结构与 180 分钟时间分配方案 (L64)",
    "subject": "gaoshu",
    "subjectName": "高等数学",
    "chapterId": "gaoshu-ch11",
    "chapterTitle": "第 7 编 应试工程：卷面分配与保命进阶清单",
    "nodeType": "topic",
    "summary": "Maki 应试工程篇 L64：考研数学卷面由 10 道选择（50分）、6 道填空（30分）、6 道解答（70分）构成。考场 180 分钟必须建立精准的时间红线意识，绝不可在一道选择题上死磕超过 8 分钟。",
    "triggers": [
      "考场实战模考、全真模拟卷训练、冲刺套卷测试",
      "做题慢、卡在难题上导致后面大题写不完、填空计算超时",
      "选择题与填空题时间分配不均，前 16 题耗时超过 90 分钟"
    ],
    "firstReaction": "第一反应：考场时间就是分数！选填题每题平均 4~5 分钟，总计控制在 65~70 分钟；大题平均每题 12~14 分钟，总计控制在 80~85 分钟；必须留出 25~30 分钟进行全局核验与填涂卡检查！",
    "candidateMethods": [
      {
        "name": "65-85-30 黄金时间分配律",
        "applicability": "全国硕士研究生数学统考 180 分钟全卷",
        "whyChoose": "前 65 分钟保住 80 分选填题；中间 85 分钟拿下 6 道综合解答大题；最后 30 分钟复查高危计算与填涂，将失误率降至最低。",
        "limitations": "严格设置单题止损点：选填题 6 分钟无进展必须先标记跳过。"
      },
      {
        "name": "选择题四大特化得分术",
        "applicability": "单项选择题 1~10 题",
        "whyChoose": "结合排除法、特值法（特殊函数 $f(x)=x, x^2$、特殊矩阵 $A=E, O$）、极值反例法，秒杀不需分步过程的选择题。",
        "limitations": "特值法验证只能用于否定错误选项，只有唯一合法项剩余时方可敲定。"
      }
    ],
    "standardSteps": [
      "第一阶段（0~65分钟）：全神贯注完成 1~16 题（10 选择 + 6 填空），遇阻卡壳立即画圈跳过。",
      "第二阶段（65~150分钟）：集中精力推进 17~22 题（6 道综合大题），按步拿分，步骤规范。",
      "第三阶段（150~180分钟）：返回攻坚此前画圈标记的卡壳题，并按清单重点核查计算易错项。"
    ],
    "coreFormulas": [
      {
        "name": "考卷分值结构比",
        "latex": "\\text{选填: } 16 \\times 5 = 80\\text{分 (53.3\\%)}, \\quad \\text{解答: } 6\\text{题} = 70\\text{分 (46.7\\%)}",
        "notes": "选填占半壁江山，得选填者得天下"
      }
    ],
    "pitfalls": [
      "在某一道 5 分的选择题上苦思冥想 15 分钟，导致后面 12 分的大题没有时间看题",
      "解答题草稿纸上算对，抄到答题卡上时符号或指数抄错",
      "没有留出足够时间检查填空题的定义域与开闭区间"
    ],
    "whyChooseMethod": "把控时间节奏是发挥平时真实水平的决定性前提，严格执行止损与分段策略。",
    "pastQuestions": [],
    "variantExercises": [],
    "selfCheckList": [
      "模考时能否在 70 分钟内完成前 16 题？",
      "是否有单题耗时超过 8 分钟立即跳过的果断止损纪律？",
      "是否留出了至少 20 分钟用于检查高频符号错误？"
    ],
    "relatedKnowledgeIds": [
      "yingshi-65-calculation-mistakes-checklist",
      "yingshi-66-survival-and-advanced-checklist"
    ],
    "tags": ["时间分配", "卷面结构", "模考策略", "止损纪律"],
    "source": "Maki考研数学大串讲 L64",
    "isPending": False
  },
  "yingshi-65-calculation-mistakes-checklist": {
    "id": "yingshi-65-calculation-mistakes-checklist",
    "title": "考研数学四大失误清单与交卷前自查 (L65)",
    "subject": "gaoshu",
    "subjectName": "高等数学",
    "chapterId": "gaoshu-ch11",
    "chapterTitle": "第 7 编 应试工程：卷面分配与保命进阶清单",
    "nodeType": "topic",
    "summary": "Maki 应试工程篇 L65：考研数学的扣分点有 60% 不是因为‘不会’，而是因为‘四大失误’（读题失误、建模失误、方法失误、计算失误）。考前必须形成强有力的防错雷达与交卷前自查习惯。",
    "triggers": [
      "平时做题总能看懂解析，但自己算总是在符号、常数上扣分",
      "定义域看错、开闭区间看漏、题干问极小值误写成极小值点",
      "二重积分积分区域上下限写颠倒、矩阵乘法不满足交换律却擅自交换"
    ],
    "firstReaction": "第一反应：交卷前 20 分钟启动‘四查雷达’：一查题干问什么（点还是值？），二查定义域与符号（分母非零、底数大于0），三查二重积分投影与格林公式方向，四查特征向量是否非零！",
    "candidateMethods": [
      {
        "name": "四大失误雷达自查法",
        "applicability": "所有大题演算与填空题核对",
        "whyChoose": "针对性排查：读题错误（问点还是值？齐次还是非齐次？）、建模错误（旋转体绕 x 轴还是 y 轴？）、方法错误（加减法误代无穷小）、计算错误（分母通分移项变号）。",
        "limitations": "必须在脑海中条理化列出检查项，不可泛泛扫视。"
      }
    ],
    "standardSteps": [
      "第一项（读题自查）：重新扫一眼题干第一句和问句末尾，核对题设条件（如独立？连续？正定？非零？）。",
      "第二项（极限自查）：核对等价无穷小是否仅用于乘积项；洛必达是否确认是 0/0 或 \\infty/\\infty。",
      "第三项（积分自查）：二重积分奇偶对称性是否包含原点；格林公式曲线是否为逆时针正向（顺时针必须加负号）。",
      "第四项（线代自查）：伴随矩阵公式 $A^{-1} = \\frac{1}{|A|}A^*$ 的分母 $|A|$ 有无漏除；特征向量写成基础解系是否注明 $k_1, k_2$ 不同时为 0。",
      "第五项（概率自查）：概率密度积分为 1 的全域检查；方差公式 $DX = E(X^2) - [E(X)]^2$ 有无忘扣平方。"
    ],
    "coreFormulas": [
      {
        "name": "四大高危陷阱公式",
        "latex": "DX = E(X^2) - [E(X)]^2,\\quad A^{-1} = \\frac{1}{|A|}A^*,\\quad \\oint_L = -\\oint_{L^-}",
        "notes": "考场失误最高频的三大符号与常数漏记点"
      }
    ],
    "pitfalls": [
      "题干问‘极值’却写成了自变量坐标 $x=x_0$；问‘极值点’却写成了函数值 $f(x_0)$",
      "格林公式与高斯公式中，未检查曲面或曲线的方向，顺时针或内侧遗漏负号",
      "矩阵乘法 $AB=AC$ 在 $|A| \\ne 0$ 未满足时擅自约去 $A$ 得到 $B=C$"
    ],
    "whyChooseMethod": "考前每消除一种习惯性失误，考场上就能多拿 5~10 分，是产出比极高的提分手段。",
    "pastQuestions": [],
    "variantExercises": [],
    "selfCheckList": [
      "算完方差是否核验过 DX >= 0？若算成负数是否能立刻意识到公式写错？",
      "求格林公式是否先画草图检查边界是逆时针（正向）还是顺时针（负向）？",
      "求特征向量通解是否写了 'c 为任意非零常数'？"
    ],
    "relatedKnowledgeIds": [
      "yingshi-64-exam-time-structure",
      "yingshi-66-survival-and-advanced-checklist"
    ],
    "tags": ["四大失误", "读题错误", "计算失误", "符号检查", "自查清单"],
    "source": "Maki考研数学大串讲 L65",
    "isPending": False
  },
  "yingshi-66-survival-and-advanced-checklist": {
    "id": "yingshi-66-survival-and-advanced-checklist",
    "title": "保命清单 (60~90分) 与 进阶提分清单 (120~140分) (L66)",
    "subject": "gaoshu",
    "subjectName": "高等数学",
    "chapterId": "gaoshu-ch11",
    "chapterTitle": "第 7 编 应试工程：卷面分配与保命进阶清单",
    "nodeType": "topic",
    "summary": "Maki 应试工程篇 L66：将考研数学考点划分为两大作战军团：保命清单（必须稳拿的 80~90 分基本盘）与进阶清单（拉开分差冲击 120~140 分的高难度考点）。考前两周按清单分类逐项突破，有的放矢。",
    "triggers": [
      "考前最后 1~2 个月复习规划、知识点查漏补缺",
      "目标分数在 80~100 分（过线求稳）或 120~140 分（冲刺名校）",
      "感觉考点太多抓不住主次重点，需要清晰的优先级阶梯"
    ],
    "firstReaction": "第一反应：先保基本盘，再攻进阶堡垒！保命清单上的 25 个送分考点必须达到 100% 零失误；在此坚实基础上，攻坚 15 个高阶综合题型以争取 120+ 高分。",
    "candidateMethods": [
      {
        "name": "阶梯式分类推进策略",
        "applicability": "考研数学一整体复习与冲刺复盘",
        "whyChoose": "把有限的备考精力精准投放到产出比最高的考点上，避免在冷门极难偏题上浪费时间而丢失基本分。",
        "limitations": "保命盘未稳时切忌盲目硬啃极难证明题。"
      }
    ],
    "standardSteps": [
      "第一层（60~90分保命清单）：七大未定式极限计算、导数与复合/隐函数求导、可分离变量方程与二阶常系数齐次方程、定积分换元分部、基础解系与相似对角化、八大常见分布与均值方差公式。",
      "第二层（90~120分强化清单）：泰勒公式展开定阶、单调有界递推数列、微分中值定理辅助函数、变限积分求导与反常积分收敛性、多元极值拉格朗日乘数、二重积分极坐标、施密特正交与二次型化标准形、二维联合分布求边缘与条件概率、矩估计与似然估计。",
      "第三层（120~140分进阶清单）：曲线曲面积分（格林、高斯、斯托克斯、场论）、三重积分切片法、幂级数求和与傅里叶展开、抽象分块矩阵方程与秩定理、二维随机变量函数分布（卷积公式与最大最小值分布）、估计量的无偏性与有效性证明、跨章节综合分析证明题。"
    ],
    "coreFormulas": [
      {
        "name": "得分目标梯队",
        "latex": "\\text{保命盘: } 85\\text{分} \\to \\text{强化盘: } 115\\text{分} \\to \\text{进阶盘: } 135+\\text{分}",
        "notes": "考研数学阶梯式目标管理"
      }
    ],
    "pitfalls": [
      "基础未牢固就盲目追求高深技巧，结果最简单的极限与导数丢分严重",
      "只刷题不总结方法卡与特征归纳，做一道忘一道",
      "忽视最后两周的模拟考全真掐表训练，考场上缺乏时间压迫感应对能力"
    ],
    "whyChooseMethod": "考前两周依清单对号入座，实现复习收益最大化。",
    "pastQuestions": [],
    "variantExercises": [],
    "selfCheckList": [
      "保命清单上的 25 个题型是否能做到提笔即出答案？",
      "进阶清单上的重点考点（拉格朗日乘数、格林公式、正交对角化、MLE）是否有标准的推导模版？",
      "最后两周是否安排了至少 3 次全真 180 分钟模考测试？"
    ],
    "relatedKnowledgeIds": [
      "yingshi-64-exam-time-structure",
      "yingshi-65-calculation-mistakes-checklist"
    ],
    "tags": ["保命清单", "进阶清单", "提分规划", "优先级", "冲刺复习"],
    "source": "Maki考研数学大串讲 L66",
    "isPending": False
  }
}

# Read knowledgeBase.ts
with open('src/data/knowledgeBase.ts', 'r', encoding='utf-8') as f:
    text = f.read()

# Locate where to insert the new nodes
target = '"isPending": False\n  }\n};'
if target in text:
    insert_str = ""
    for k, v in new_nodes.items():
        if f'"{k}":' not in text:
            insert_str += f',\n  "{k}": ' + json.dumps(v, ensure_ascii=False, indent=2)
    
    text = text.replace('"isPending": False\n  }\n};', '"isPending": False\n  }' + insert_str + '\n};')
    with open('src/data/knowledgeBase.ts', 'w', encoding='utf-8') as f:
        f.write(text)
    print("Added L01~L02 and L64~L66 nodes to knowledgeBase.ts successfully!")
else:
    print("Target anchor not found in knowledgeBase.ts")
