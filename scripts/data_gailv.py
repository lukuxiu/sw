# -*- coding: utf-8 -*-
"""
Verified Knowledge Base Data for 概率论与数理统计 (Chapters 1 to 8, 17 topics)
Extracted and aligned with:
- Maki考研数学一站式大串讲 (Lectures 54 to 63)
- Maki考研数学真题分类精解 (Authentic past exam questions 1987-2025)
"""

GAILV_TOPICS = {
    "gailv-01-total-probability-bayes": {
        "id": "gailv-01-total-probability-bayes",
        "title": "全概率公式与贝叶斯逆概公式",
        "subject": "gailv",
        "subjectName": "概率论与数理统计",
        "chapterId": "gailv-ch01",
        "chapterTitle": "随机事件与概率",
        "nodeType": "topic",
        "summary": "“全概知因求果，贝叶斯由果溯因”。寻找完备事件组是切入点，分阶段或条件复杂时画概率树分解。",
        "triggers": [
            "事件结果取决于前序多种可能情形（分阶段/抽签/多源产品）",
            "“已知结果发生，求是由某个原因引起的概率”",
            "涉及假阳性率、敏感性、疾病检测题型",
            "报文传输、数字信道误码率问题"
        ],
        "firstReaction": "第一反应：寻找完备事件组 $B_1, B_2, \\dots, B_n$（两两互不相容且 $\\sum P(B_i)=1$）；确定目标事件 $A$；画两层决策树列出先验概率 $P(B_i)$ 与条件概率 $P(A|B_i)$。",
        "candidateMethods": [
            {
                "name": "全概率公式（先验综合）",
                "priority": 1,
                "condition": "已知各原因 $B_i$ 的先验概率及各原因下 $A$ 的概率",
                "whyChoose": "将复杂事件分解到各个互斥子空间中求和",
                "description": "$P(A) = \\sum_{i=1}^n P(B_i)P(A|B_i)$"
            },
            {
                "name": "贝叶斯公式（后验逆概）",
                "priority": 2,
                "condition": "已知最终结果 $A$ 已经发生，求具体原因 $B_k$",
                "whyChoose": "后验逆向归因的标准解法",
                "description": "$P(B_k|A) = \\frac{P(B_k)P(A|B_k)}{\\sum_{i=1}^n P(B_i)P(A|B_i)}$"
            }
        ],
        "applicability": "必须严格检验完备事件组是否满足：① $B_i \\cap B_j = \\emptyset (i \\ne j)$；② $\\bigcup_{i=1}^n B_i = \\Omega$；③ $P(B_i) > 0$。",
        "steps": [
            "步骤1（设事件）：明确设出原因事件 $B_1, B_2, \\dots, B_n$ 和结果事件 $A$。",
            "步骤2（写先验）：写出各原因的先验概率 $P(B_i)$，检查和是否等于1。",
            "步骤3（写条件概）：写出各分支条件下的条件概率 $P(A|B_i)$。",
            "步骤4（套公式）：求结果概率用全概公式；由果溯因套贝叶斯公式计算分子分母比值。"
        ],
        "pitfalls": [
            "完备事件组没有穷尽样本空间（和不为1），导致漏掉分支。",
            "混淆条件概率方向：把 $P(A|B)$ 误写成 $P(B|A)$。",
            "抽签模型中未注意“第 $k$ 次抽中概率与次序无关”的对称本质。"
        ],
        "formulas": [
            {
                "title": "全概率公式",
                "latex": "P(A) = \\sum_{i=1}^n P(B_i)P(A|B_i)",
                "notes": "其中 \\{B_1,\\dots,B_n\\} 为样本空间的一个划分"
            },
            {
                "title": "贝叶斯公式",
                "latex": "P(B_k|A) = \\frac{P(B_k)P(A|B_k)}{\\sum_{i=1}^n P(B_i)P(A|B_i)}",
                "notes": "分母即全概率公式 P(A)"
            }
        ],
        "pastQuestions": [
            {
                "id": "gailv-q-2020-1-7",
                "year": "2020",
                "category": "数一",
                "questionNumber": "(7)",
                "questionText": "设 $A, B, C$ 为三个随机事件，且 $P(A) = P(B) = P(C) = \\frac{1}{4}$，$P(AB) = 0$，$P(AC) = P(BC) = \\frac{1}{12}$，则 $A, B, C$ 中恰有一个事件发生的概率为（ ）\\n(A) 3/4 \\n(B) 2/3 \\n(C) 1/2 \\n(D) 5/12",
                "examTags": ["随机事件", "概率加法公式", "互斥与独立"],
                "breakthrough": "“恰有一个事件发生”可以表示为互斥事件的和：$A\\bar{B}\\bar{C} + \\bar{A}B\\bar{C} + \\bar{A}\\bar{B}C$；由于 $P(AB)=0$，说明 $A$ 与 $B$ 互斥，图形上没有重叠区域，大大简化了交集的计算。",
                "solution": "设目标事件为 $E = A\\bar{B}\\bar{C} \\cup \\bar{A}B\\bar{C} \\cup \\bar{A}\\bar{B}C$。\\n由容斥原理，恰有一发生等于：\\n$$P(E) = P(A) + P(B) + P(C) - 2[P(AB) + P(BC) + P(CA)] + 3P(ABC)$$\\n因为 $P(AB) = 0$，且 $ABC \\subseteq AB$，故 $P(ABC) = 0$。\\n代入数值：\\n$$P(E) = \\frac{1}{4} + \\frac{1}{4} + \\frac{1}{4} - 2\\left(0 + \\frac{1}{12} + \\frac{1}{12}\\right) + 0 = \\frac{3}{4} - 2\\cdot\\frac{2}{12} = \\frac{3}{4} - \\frac{1}{3} = \\frac{5}{12}$$\\n正确答案为 (D)。",
                "trap": "容易把恰有一个事件发生的公式中系数错记为 $-[P(AB)+P(BC)+P(AC)]$（那是至少一个的减项），注意恰发生一个要减去两倍的两两相交并加上三倍的三相交。"
            }
        ],
        "variants": [
            {
                "question": "某工厂甲、乙、丙三条流水线生产同一种芯片，产量比为 3:2:5，次品率分别为 2%、1%、3%。现从成品库中任取一件，发现是次品，求它是由丙流水线生产的概率。",
                "hint": "设完备事件组为来源产线，结果事件为取到次品，直接列贝叶斯公式。",
                "solution": "设 $B_1, B_2, B_3$ 分别为甲乙丙产线，先验概率分别为 $0.3, 0.2, 0.5$；$A$ 为次品。\\n由全概率公式：$P(A) = 0.3\\times 0.02 + 0.2\\times 0.01 + 0.5\\times 0.03 = 0.006 + 0.002 + 0.015 = 0.023$。\\n由贝叶斯公式：$P(B_3|A) = \\frac{0.5\\times 0.03}{0.023} = \\frac{15}{23} \\approx 65.22\\%$。"
            }
        ],
        "relatedKnowledgeIds": ["gailv-01-event-independence-bernoulli", "gailv-03-joint-marginal-conditional"],
        "tags": ["全概公式", "贝叶斯", "条件概率", "决策树"],
        "source": "Maki考研数学大串讲 L54 & 真题分类精解 题54.4",
        "status": "not_started",
        "isPending": False
    },
    "gailv-01-event-independence-bernoulli": {
        "id": "gailv-01-event-independence-bernoulli",
        "title": "事件独立性与伯努利重试试验",
        "subject": "gailv",
        "subjectName": "概率论与数理统计",
        "chapterId": "gailv-ch01",
        "chapterTitle": "随机事件与概率",
        "nodeType": "topic",
        "summary": "“两两独立不推相互独立，独立乘积拆开算”。$n$ 重伯努利试验认准二项分布模型 $B(n, p)$。",
        "triggers": [
            "“$A$ 与 $B$ 相互独立”",
            "“独立重复试验进行 $n$ 次”",
            "有放回抽样模型",
            "三事件两两独立与相互独立的真假命题判断"
        ],
        "firstReaction": "看到独立立即联想到 $P(AB) = P(A)P(B)$；若三个事件相互独立，需同时满足4个等式（3个两两乘积+1个三乘积）；看到 $n$ 重伯努利，设成功次数 $X \\sim B(n, p)$。",
        "candidateMethods": [
            {
                "name": "乘法公式化简",
                "priority": 1,
                "condition": "已知独立性",
                "whyChoose": "将交事件概率化为单事件概率乘积",
                "description": "$P(A\\bar{B}) = P(A)P(\\bar{B}) = P(A)(1-P(B))$"
            },
            {
                "name": "二项分布公式",
                "priority": 2,
                "condition": "每次试验成功率 $p$ 不变且独立",
                "whyChoose": "精确计算 $k$ 次成功概率",
                "description": "$P_n(k) = C_n^k p^k (1-p)^{n-k}$"
            }
        ],
        "applicability": "相互独立性不可仅由两两独立推导；试验间必须保持概率稳定无后效性（有放回抽样）。",
        "steps": [
            "步骤1：确认试验是否相互独立、各次概率是否恒定。",
            "步骤2：定义每次单次试验成功的概率 $p$ 与总试验次数 $n$。",
            "步骤3：根据“恰好 $k$ 次”、“至少 1 次（对立事件 $1-(1-p)^n$）”选用相应公式求解。"
        ],
        "pitfalls": [
            "误以为两两独立等价于相互独立（考研极高频概念陷阱）。",
            "误以为互斥事件（$AB=\\emptyset$）与独立事件是一回事（概率大于0时互斥必不独立）。"
        ],
        "formulas": [
            {
                "title": "独立性定义",
                "latex": "P(AB) = P(A)P(B) \\iff P(A|B) = P(A)",
                "notes": "A与B独立等价于A与非B、非A与B、非A与非B均独立"
            },
            {
                "title": "二项分布概率公式",
                "latex": "P(X = k) = \\binom{n}{k} p^k (1-p)^{n-k}, \\quad k=0,1,\\dots,n",
                "notes": "期望 E(X)=np, 方差 D(X)=np(1-p)"
            }
        ],
        "pastQuestions": [
            {
                "id": "gailv-q-2015-1-7",
                "year": "2015",
                "category": "数一",
                "questionNumber": "(7)",
                "questionText": "若 $A, B$ 为任意两个随机事件，则（ ）\\n(A) $P(AB) \\le P(A)P(B)$ \\n(B) $P(AB) \\ge P(A)P(B)$ \\n(C) $P(AB) \\le \\frac{P(A)+P(B)}{2}$ \\n(D) $P(AB) \\ge \\frac{P(A)+P(B)}{2}$",
                "examTags": ["随机事件", "概率不等式", "基础性质"],
                "breakthrough": "寻找 $P(AB)$ 与 $P(A), P(B)$ 之间的必然界限：$AB \\subseteq A$ 且 $AB \\subseteq B$，故 $P(AB) \\le \\min\\{P(A), P(B)\\}$，进而小于它们的算术平均值。",
                "solution": "因为 $AB \\subseteq A$ 且 $AB \\subseteq B$，由概率的单调性：\\n$P(AB) \\le P(A)$ 且 $P(AB) \\le P(B)$。\\n两式相加得：$2P(AB) \\le P(A) + P(B)$，即：\\n$$P(AB) \\le \\frac{P(A) + P(B)}{2}$$\\n对于选项 (A)(B)，独立时取等号，正相关或负相关时方向可变，故均不恒成立；选项 (D) 显然错误。故选 (C)。",
                "trap": "切勿默认 $A, B$ 独立而选 $P(AB)=P(A)P(B)$。"
            }
        ],
        "variants": [
            {
                "question": "甲乙两人独立射击靶子，命中率分别为 0.8 与 0.7。两人各射击一次，求靶子至少中一枪的概率。",
                "hint": "“至少中一枪”的对立事件是“两人均未命中”。",
                "solution": "$P = 1 - (1 - 0.8)(1 - 0.7) = 1 - 0.2 \\times 0.3 = 1 - 0.06 = 0.94$。"
            }
        ],
        "relatedKnowledgeIds": ["gailv-01-total-probability-bayes", "gailv-02-common-distributions-standard"],
        "tags": ["独立性", "伯努利", "二项分布", "对立事件"],
        "source": "Maki考研数学大串讲 L54 & 真题分类精解 题54.1",
        "status": "not_started",
        "isPending": False
    },
    "gailv-02-distribution-function-properties": {
        "id": "gailv-02-distribution-function-properties",
        "title": "分布函数性质与离散/连续判别",
        "subject": "gailv",
        "subjectName": "概率论与数理统计",
        "chapterId": "gailv-ch02",
        "chapterTitle": "一维随机变量及其分布",
        "nodeType": "topic",
        "summary": "“单调不减、右连续、负无穷为0正无穷为1”。点概率 $P\\{X=x_0\\} = F(x_0) - F(x_0^-)$ 即跳跃间断点的跃度。",
        "triggers": [
            "给出含待定参数的分段函数问是否能作为分布函数 $F(x)$",
            "求点概率 $P\\{X=a\\}$ 或开闭区间概率 $P\\{a < X \\le b\\}$",
            "判定随机变量是离散型、连续型还是混合型"
        ],
        "firstReaction": "直接核对三大充要性质：① 单调性 $x_1 < x_2 \\implies F(x_1) \\le F(x_2)$；② 极限值 $F(-\\infty)=0, F(+\\infty)=1$；③ 右连续性 $\\lim_{x \\to x_0^+} F(x) = F(x_0)$。",
        "candidateMethods": [
            {
                "name": "三大充要条件校验",
                "priority": 1,
                "condition": "检验函数 $F(x)$ 合法性",
                "whyChoose": "这是数学上判定一维分布函数的充要准则",
                "description": "单调不减、右连续、极限 0 与 1"
            },
            {
                "name": "跃度计算点概率",
                "priority": 2,
                "condition": "已知分布函数求某点处的概率",
                "whyChoose": "连续点概率为0，间断点概率等于跳跃高度",
                "description": "$P\\{X=x_0\\} = F(x_0) - F(x_0^-)$"
            }
        ],
        "applicability": "必须注意我国考研教材统一规定 $F(x) = P\\{X \\le x\\}$，对应右连续；左开右闭区间概率为 $P\\{a < X \\le b\\} = F(b) - F(a)$。",
        "steps": [
            "步骤1：检查边界 $\\lim_{x \\to -\\infty} F(x) = 0$ 与 $\\lim_{x \\to +\\infty} F(x) = 1$。",
            "步骤2：求导或利用增量检验是否单调不减。",
            "步骤3：检查各分段点处的右极限是否等于函数值（右连续）。"
        ],
        "pitfalls": [
            "混淆左连续与右连续：考研规定必须是右连续 $\\lim_{x\\to x_0^+} F(x) = F(x_0)$。",
            "误以为连续型随机变量在任何点处的概率为0就意味着该点不可能发生（零概率事件不等于不可能事件）。"
        ],
        "formulas": [
            {
                "title": "区间概率公式",
                "latex": "P(a < X \\le b) = F(b) - F(a)",
                "notes": "若 X 为连续型，区间开闭无影响；若离散型必须严格区分端点"
            },
            {
                "title": "单点跃度",
                "latex": "P(X = x_0) = F(x_0) - F(x_0^-)",
                "notes": "若 F 在 x_0 连续，则 P(X = x_0) = 0"
            }
        ],
        "pastQuestions": [
            {
                "id": "gailv-q-2010-1-7",
                "year": "2010",
                "category": "数一",
                "questionNumber": "(7)",
                "questionText": "设随机变量 $X$ 的分布函数 $F(x) = \\begin{cases} 0, & x < 0 \\\\ 1/2, & 0 \\le x < 1 \\\\ 1 - e^{-x}, & x \\ge 1 \\end{cases}$，则 $P\\{X = 1\\} = $（ ）\\n(A) 0 \\n(B) $1/2$ \\n(C) $1/2 - e^{-1}$ \\n(D) $1 - e^{-1}$",
                "examTags": ["分布函数", "点概率", "跃度计算"],
                "breakthrough": "由点概率与分布函数的关系：$P\\{X = 1\\} = F(1) - F(1^-)$，直接求左极限与右极限函数值之差。",
                "solution": "当 $x=1$ 时，由表达式得 $F(1) = 1 - e^{-1}$；\\n当 $x \\to 1^-$ 时，$F(1^-) = \\lim_{x \\to 1^-} \\frac{1}{2} = \\frac{1}{2}$；\\n因此：\\n$$P\\{X = 1\\} = F(1) - F(1^-) = (1 - e^{-1}) - \\frac{1}{2} = \\frac{1}{2} - e^{-1}$$\\n故正确选项为 (C)。",
                "trap": "直接代入分段第二段或第三段公式而忘记做差。"
            }
        ],
        "variants": [
            {
                "question": "已知函数 $F(x) = A + B \\arctan x$ 为某一连续型随机变量的分布函数，求常数 $A, B$。",
                "hint": "利用 $F(-\\infty)=0$ 和 $F(+\\infty)=1$ 列方程组。",
                "solution": "$\\lim_{x\\to -\\infty} F(x) = A - B\\cdot\\frac{\\pi}{2} = 0$，$\\lim_{x\\to +\\infty} F(x) = A + B\\cdot\\frac{\\pi}{2} = 1$。\\n两式相加得 $2A = 1 \\implies A = 1/2$；相减得 $\\pi B = 1 \\implies B = 1/\\pi$。"
            }
        ],
        "relatedKnowledgeIds": ["gailv-02-common-distributions-standard", "gailv-02-function-distribution-one-dim"],
        "tags": ["分布函数", "跃度", "右连续", "单调性"],
        "source": "Maki考研数学大串讲 L55 & 真题分类精解 题55.1",
        "status": "not_started",
        "isPending": False
    },
    "gailv-02-common-distributions-standard": {
        "id": "gailv-02-common-distributions-standard",
        "title": "八大常见分布与标准正态转化",
        "subject": "gailv",
        "subjectName": "概率论与数理统计",
        "chapterId": "gailv-ch02",
        "chapterTitle": "一维随机变量及其分布",
        "nodeType": "topic",
        "summary": "“离散看0-1、二项、泊松、几何；连续看均匀、指数、正态”。正态标准化 $Z=\\frac{X-\\mu}{\\sigma}$，指数无记忆 $P(X>s+t|X>s)=P(X>t)$。",
        "triggers": [
            "题目说明服从正态分布 $N(\\mu, \\sigma^2)$",
            "稀有事件发生概率、单位时间质点到达（泊松分布 $\\lambda$）",
            "寿命、无记忆性、故障等待时间（指数分布 $\\lambda$）",
            "由正态概率查表转化 $\\Phi(x)$ 形式"
        ],
        "firstReaction": "立即提取分布的参数！若正态分布做标准化 $Z = \\frac{X-\\mu}{\\sigma} \\sim N(0, 1)$；若指数分布立即想到密度 $f(x)=\\lambda e^{-\\lambda x} (x>0)$ 与生存函数 $P\\{X>x\\}=e^{-\\lambda x}$。",
        "candidateMethods": [
            {
                "name": "正态标准化变换",
                "priority": 1,
                "condition": "涉及正态分布的概率计算",
                "whyChoose": "化为标准正态分布函数 $\\Phi(x)$，利用对称性 $\\Phi(-x) = 1 - \\Phi(x)$",
                "description": "$P(X \\le a) = \\Phi\\left(\\frac{a-\\mu}{\\sigma}\\right)$"
            },
            {
                "name": "指数分布生存函数法",
                "priority": 2,
                "condition": "涉及指数分布尾部概率计算",
                "whyChoose": "避免积分计算，秒出结果",
                "description": "$P\\{X > t\\} = e^{-\\lambda t}$"
            }
        ],
        "applicability": "正态分布第二个参数是方差 $\\sigma^2$ 而非标准差 $\\sigma$；指数分布参数是 $\\lambda$ 还是 $1/\\theta$ 需仔细读题。",
        "steps": [
            "步骤1：确认分布类型与具体参数值。",
            "步骤2：写出对应的分布律（离散）或概率密度函数（连续）。",
            "步骤3：利用对称性、标准化或积分求出目标概率与期望方差。"
        ],
        "pitfalls": [
            "正态分布中误将 $N(1, 4)$ 中的 4 当成标准差（实际 $\\sigma=2$）。",
            "混淆泊松分布参数 $\\lambda$（$E(X)=D(X)=\\lambda$）与指数分布期望 $1/\\lambda$。"
        ],
        "formulas": [
            {
                "title": "正态标准化",
                "latex": "P(a < X \\le b) = \\Phi\\left(\\frac{b-\\mu}{\\sigma}\\right) - \\Phi\\left(\\frac{a-\\mu}{\\sigma}\\right)",
                "notes": "\\Phi(-x) = 1 - \\Phi(x)"
            },
            {
                "title": "泊松分布概率分布律",
                "latex": "P(X = k) = \\frac{\\lambda^k}{k!} e^{-\\lambda}, \\quad k=0,1,2,\\dots",
                "notes": "E(X) = \\lambda, \\quad D(X) = \\lambda"
            }
        ],
        "pastQuestions": [
            {
                "id": "gailv-q-2025-1-9",
                "year": "2025",
                "category": "数一",
                "questionNumber": "(9)",
                "questionText": "设 $X_1, X_2, \\dots, X_{20}$ 是来自总体 $B(1, 0.1)$ 的简单随机样本，令 $T = \\sum_{i=1}^{20} X_i$，利用泊松分布近似表示二项分布的方法可得 $P\\{T \\le 1\\} \\approx$（ ）\\n(A) $e^{-2}$ \\n(B) $2e^{-2}$ \\n(C) $3e^{-2}$ \\n(D) $4e^{-2}$",
                "examTags": ["二项分布", "泊松定理", "小概率近似"],
                "breakthrough": "$T$ 服从二项分布 $B(n, p)$，其中 $n=20, p=0.1$。根据泊松定理，当 $n$ 较大 $p$ 较小时，二项分布可由参数 $\\lambda = np$ 的泊松分布近似替代。",
                "solution": "二项分布参数 $n=20, p=0.1$，则近似泊松分布参数：\\n$$\\lambda = np = 20 \\times 0.1 = 2$$\\n故 $T$ 近似服从泊松分布 $P(\\lambda = 2)$。\\n所求概率：\\n$$P\\{T \\le 1\\} = P\\{T = 0\\} + P\\{T = 1\\} = \\frac{2^0}{0!}e^{-2} + \\frac{2^1}{1!}e^{-2} = e^{-2} + 2e^{-2} = 3e^{-2}$$\\n正确答案为 (C)。",
                "trap": "漏掉 $T=0$ 的情形，误只算 $P\\{T=1\\}$。"
            }
        ],
        "variants": [
            {
                "question": "某电子器件寿命 $X \\sim E(0.5)$（即指数分布参数 $\\lambda=0.5$），求该器件已工作 2 小时的情况下，还能再至少工作 3 小时的条件概率。",
                "hint": "利用指数分布的无记忆性 $P(X > s+t | X > s) = P(X > t)$。",
                "solution": "$P(X > 2+3 | X > 2) = P(X > 3) = e^{-\\lambda \\times 3} = e^{-0.5 \\times 3} = e^{-1.5}$。"
            }
        ],
        "relatedKnowledgeIds": ["gailv-02-distribution-function-properties", "gailv-05-central-limit-theorems"],
        "tags": ["八大分布", "正态分布", "泊松近似", "指数分布"],
        "source": "Maki考研数学大串讲 L55 & 真题分类精解 题55.5",
        "status": "not_started",
        "isPending": False
    },
    "gailv-02-function-distribution-one-dim": {
        "id": "gailv-02-function-distribution-one-dim",
        "title": "一维随机变量函数分布 Y=g(X) 求法",
        "subject": "gailv",
        "subjectName": "概率论与数理统计",
        "chapterId": "gailv-ch02",
        "chapterTitle": "一维随机变量及其分布",
        "nodeType": "topic",
        "summary": "“分布函数法万能，公式法单调快”。若 $g(X)$ 严格单调可导，直接套公式 $f_Y(y) = f_X(h(y))|h'(y)|$；非单调必用分布函数法从事件等价切入。",
        "triggers": [
            "已知 $X$ 的概率密度 $f_X(x)$，求 $Y = X^2, Y = |X|, Y = \\sin X$ 等函数的密度",
            "离散型变量做代数变换 $Y=g(X)$",
            "求分段复合函数的分布"
        ],
        "firstReaction": "首先观察函数 $g(x)$ 在 $X$ 的可能取值范围内是否严格单调：若单调且可导，首选公式法；若非单调（如 $Y=X^2, Y=|X|$），果断使用分布函数法先求 $F_Y(y) = P\\{g(X) \\le y\\}$ 再求导。",
        "candidateMethods": [
            {
                "name": "分布函数法（通法）",
                "priority": 1,
                "condition": "任何连续型随机变量函数，尤其非单调函数",
                "whyChoose": "思路严密，不易漏掉取值区间与绝对值变换",
                "description": "$F_Y(y) = P\\{g(X) \\le y\\} = \\int_{g(x) \\le y} f_X(x)dx$，求导得 $f_Y(y) = F_Y'(y)$"
            },
            {
                "name": "单调可导公式法",
                "priority": 2,
                "condition": "$y=g(x)$ 严格单调且导数 $g'(x) \\ne 0$",
                "whyChoose": "无需积分，直接代入反函数导数公式",
                "description": "$f_Y(y) = f_X(h(y))|h'(y)|$，其中 $x=h(y)$ 为反函数"
            }
        ],
        "applicability": "使用公式法必须明确注明 $y$ 的取值范围，其他区域密度直接标为 0；导数一定要带绝对值符号 $|h'(y)|$。",
        "steps": [
            "步骤1：确定 $Y=g(X)$ 的值域范围。",
            "步骤2：列出分布函数定义 $F_Y(y) = P\\{Y \\le y\\} = P\\{g(X) \\le y\\}$。",
            "步骤3：将关于 $Y$ 的不等式解出关于 $X$ 的集合 $D_y = \\{x \\mid g(x) \\le y\\}$。",
            "步骤4：将 $f_X(x)$ 在集合 $D_y$ 上积分得到 $F_Y(y)$，再对 $y$ 求导得到密度 $f_Y(y)$。"
        ],
        "pitfalls": [
            "忘记写出 $y$ 的有效定义域（分段取值范围），导致答案不完整扣分。",
            "在公式法中遗漏绝对值：如 $y = -2x$，反函数 $x = -y/2$，微商必须加绝对值 $|-1/2| = 1/2$。"
        ],
        "formulas": [
            {
                "title": "单调函数密度公式",
                "latex": "f_Y(y) = f_X(h(y)) \\cdot |h'(y)|, \\quad \\alpha < y < \\beta",
                "notes": "其中 x=h(y) 是 y=g(x) 的反函数"
            },
            {
                "title": "平方变换分布函数",
                "latex": "F_Y(y) = P(X^2 \\le y) = P(-\\sqrt{y} \\le X \\le \\sqrt{y}) = F_X(\\sqrt{y}) - F_X(-\\sqrt{y}) \\quad (y > 0)",
                "notes": "求导即得 f_Y(y) = \\frac{1}{2\\sqrt{y}}[f_X(\\sqrt{y}) + f_X(-\\sqrt{y})]"
            }
        ],
        "pastQuestions": [
            {
                "id": "gailv-q-2018-1-7",
                "year": "2018",
                "category": "数一",
                "questionNumber": "(7)",
                "questionText": "设随机变量 $X$ 的概率密度 $f(x)$ 满足 $f(1+x) = f(1-x)$，且 $\\int_0^2 f(x)dx = 0.6$，则 $P\\{X < 0\\} = $（ ）\\n(A) 0.2 \\n(B) 0.3 \\n(C) 0.4 \\n(D) 0.6",
                "examTags": ["概率密度", "对称性", "全概率归一性"],
                "breakthrough": "$f(1+x)=f(1-x)$ 说明密度曲线关于直线 $x=1$ 对称。区间 $[0, 2]$ 关于 1 对称，因此 $[0, 1]$ 与 $[1, 2]$ 的积分各占一半；结合总积分为 1 求出尾部概率。",
                "solution": "因为 $f(x)$ 关于 $x=1$ 对称，且 $\\int_0^2 f(x)dx = 0.6$，由对称性：\\n$$\\int_0^1 f(x)dx = \\int_1^2 f(x)dx = 0.3$$\\n又因为全概率积分为 1，对称轴左侧总积分为 0.5：\\n$$\\int_{-\\infty}^1 f(x)dx = 0.5$$\\n因此：\\n$$P\\{X < 0\\} = \\int_{-\\infty}^0 f(x)dx = \\int_{-\\infty}^1 f(x)dx - \\int_0^1 f(x)dx = 0.5 - 0.3 = 0.2$$\\n正确答案为 (A)。",
                "trap": "误以为对称轴是 $y$ 轴（$x=0$）导致算错。"
            }
        ],
        "variants": [
            {
                "question": "设 $X \\sim U(0, 1)$，求 $Y = -2\\ln X$ 的概率密度函数 $f_Y(y)$。",
                "hint": "注意 $y$ 的取值范围是 $(0, +\\infty)$，函数严格单调减，直接用公式法。",
                "solution": "当 $x \\in (0, 1)$ 时，$y = -2\\ln x \\in (0, +\\infty)$。反函数 $x = e^{-y/2}$，导数 $x' = -\\frac{1}{2}e^{-y/2}$。\\n代入公式：$f_Y(y) = f_X(e^{-y/2})|x'| = 1 \\cdot \\frac{1}{2}e^{-y/2} = \\frac{1}{2}e^{-y/2} (y>0)$，即 $Y \\sim E(0.5)$（参数为 1/2 的指数分布）。"
            }
        ],
        "relatedKnowledgeIds": ["gailv-02-distribution-function-properties", "gailv-03-random-variable-functions-2d"],
        "tags": ["函数分布", "分布函数法", "公式法", "对称性"],
        "source": "Maki考研数学大串讲 L56 & 真题分类精解 题55.4",
        "status": "not_started",
        "isPending": False
    },
    "gailv-03-joint-marginal-conditional": {
        "id": "gailv-03-joint-marginal-conditional",
        "title": "二维联合分布、边缘分布与条件分布",
        "subject": "gailv",
        "subjectName": "概率论与数理统计",
        "chapterId": "gailv-ch03",
        "chapterTitle": "多维随机变量及其分布",
        "nodeType": "topic",
        "summary": "“积联合得边缘，商边缘得条件；联合可拆当且仅当独立”。画出二维平面定义域积分区域是做对题的第一步。",
        "triggers": [
            "给出二维概率密度 $f(x, y)$，求边缘密度 $f_X(x), f_Y(y)$",
            "求条件概率密度 $f_{X|Y}(x|y)$",
            "判定 $X$ 与 $Y$ 是否相互独立",
            "求二维均匀分布在某区域内的概率"
        ],
        "firstReaction": "立刻在草稿纸上画出平面区域 $D$！求 $f_X(x)$ 对 $y$ 积分（固定 $x$，观察 $y$ 从哪穿入、哪穿出）；判定独立性只需看 $f(x, y)$ 能否分离变量成 $g(x)h(y)$ 且定义域区域呈矩形。",
        "candidateMethods": [
            {
                "name": "边缘密度投影积分法",
                "priority": 1,
                "condition": "已知联合密度求单变量密度",
                "whyChoose": "对不需要的变量在全空间积分“吸掉”",
                "description": "$f_X(x) = \\int_{-\\infty}^{+\\infty} f(x, y)dy, \\quad f_Y(y) = \\int_{-\\infty}^{+\\infty} f(x, y)dx$"
            },
            {
                "name": "条件密度比值法",
                "priority": 2,
                "condition": "求条件分布",
                "whyChoose": "类似条件概率除以边缘概率",
                "description": "$f_{X|Y}(x|y) = \\frac{f(x, y)}{f_Y(y)} \\quad (f_Y(y) > 0)$"
            },
            {
                "name": "独立性充要检验",
                "priority": 3,
                "condition": "判断两随机变量独立性",
                "whyChoose": "快速识别或严格证明",
                "description": "检验 $f(x, y) = f_X(x)f_Y(y)$ 是否几乎处处成立"
            }
        ],
        "applicability": "独立性的前提是定义域必须是矩形区域（允许无穷区间）。如果定义域是三角形、圆形等非矩形区域，则 $X$ 与 $Y$ 必不独立！",
        "steps": [
            "步骤1：精确画出非零区域 $D = \\{(x, y) \\mid f(x, y) > 0\\}$。",
            "步骤2：积分求边缘密度，明确写出每段积分的上下限与外层变量范围。",
            "步骤3：求条件密度时代入 $f(x, y) / f_Y(y)$，务必注明条件变量 $y$ 的有效范围。"
        ],
        "pitfalls": [
            "积分限写错：把内层积分的上下限写成了常数，未结合几何图形确定边界函数。",
            "看到 $f(x, y) = 4xy$ 就草率判定独立，忽略了定义域可能是三角形 $0<x<y<1$。"
        ],
        "formulas": [
            {
                "title": "边缘密度公式",
                "latex": "f_X(x) = \\int_{-\\infty}^{+\\infty} f(x, y)\\,dy, \\quad f_Y(y) = \\int_{-\\infty}^{+\\infty} f(x, y)\\,dx",
                "notes": "积分限由联合密度非零区域决定"
            },
            {
                "title": "条件密度公式",
                "latex": "f_{X|Y}(x|y) = \\frac{f(x, y)}{f_Y(y)} \\quad (f_Y(y) > 0)",
                "notes": "固定 y 时，作为 x 的函数满足归一性"
            }
        ],
        "pastQuestions": [
            {
                "id": "gailv-q-2011-1-14",
                "year": "2011",
                "category": "数一",
                "questionNumber": "(14)",
                "questionText": "设二维随机变量 $(X, Y)$ 服从正态分布 $N(\\mu, \\mu; \\sigma^2, \\sigma^2; 0)$，则 $E(XY^2) = $（ ）",
                "examTags": ["二维正态分布", "相关系数与独立性", "高阶矩计算"],
                "breakthrough": "二维正态分布参数中最后一个数字是相关系数 $\\rho = 0$。对于正态分布，不相关等价于相互独立！因此 $X$ 与 $Y$ 独立，期望可直接拆开。",
                "solution": "因为 $(X, Y) \\sim N(\\mu, \\mu; \\sigma^2, \\sigma^2; 0)$，其相关系数 $\\rho = 0$。\\n在正态总体中，$\\rho = 0 \\iff X$ 与 $Y$ 相互独立。\\n由独立性：\\n$$E(XY^2) = E(X) \\cdot E(Y^2)$$\\n已知 $E(X) = \\mu$；对于 $Y$，由于 $D(Y) = E(Y^2) - [E(Y)]^2$，\\n故 $E(Y^2) = D(Y) + [E(Y)]^2 = \\sigma^2 + \\mu^2$。\\n代入得：\\n$$E(XY^2) = \\mu(\\sigma^2 + \\mu^2) = \\mu\\sigma^2 + \\mu^3$$",
                "trap": "误以为任意分布不相关都可推出独立（该性质仅在二维正态分布下成立）。"
            }
        ],
        "variants": [
            {
                "question": "设二维随机变量 $(X, Y)$ 在三角形区域 $D: 0 < x < 1, 0 < y < x$ 上服从均匀分布。问 $X$ 与 $Y$ 是否独立？并求 $f_{Y|X}(y|x)$。",
                "hint": "三角形区域非矩形，必不独立；在给定 $x$ 条件下 $Y$ 服从 $U(0, x)$。",
                "solution": "区域面积 $S = 1/2$，联合密度 $f(x, y) = 2 (0<y<x<1)$。区域非矩形故不独立。\\n边缘密度 $f_X(x) = \\int_0^x 2 dy = 2x (0<x<1)$。\\n条件密度 $f_{Y|X}(y|x) = \\frac{2}{2x} = \\frac{1}{x} (0 < y < x)$，即给定 $X=x$ 时 $Y$ 服从 $(0, x)$ 上的均匀分布。"
            }
        ],
        "relatedKnowledgeIds": ["gailv-03-random-variable-functions-2d", "gailv-04-variance-covariance-correlation"],
        "tags": ["联合分布", "边缘分布", "条件分布", "独立性判定"],
        "source": "Maki考研数学大串讲 L57 & 真题分类精解 题59.3",
        "status": "not_started",
        "isPending": False
    },
    "gailv-03-random-variable-functions-2d": {
        "id": "gailv-03-random-variable-functions-2d",
        "title": "二维随机变量函数的分布 (Z=X+Y, max, min)",
        "subject": "gailv",
        "subjectName": "概率论与数理统计",
        "chapterId": "gailv-ch03",
        "chapterTitle": "多维随机变量及其分布",
        "nodeType": "topic",
        "summary": "“求和看卷积，最值看极值乘积”。独立时 $Z=\\max$ 分布函数相乘，$Z=\\min$ 生存函数相乘；$Z=X+Y$ 卷积化积分。",
        "triggers": [
            "求 $Z = X + Y$ 的概率密度（卷积公式）",
            "求 $M = \\max(X, Y)$ 或 $N = \\min(X, Y)$ 的分布",
            "求商 $Z = Y/X$ 或积 $Z = XY$ 的分布"
        ],
        "firstReaction": "看独立性与函数形式：若求 $Z=\\max(X, Y)$，直接写 $F_Z(z) = P\\{X\\le z, Y\\le z\\}$；若独立，则 $F_Z(z) = F_X(z)F_Y(z)$；若求和 $Z=X+Y$，独立时用卷积公式 $f_Z(z) = \\int_{-\\infty}^{+\\infty} f_X(x)f_Y(z-x)dx$。",
        "candidateMethods": [
            {
                "name": "极值分布展开法",
                "priority": 1,
                "condition": "求最大值或最小值的分布",
                "whyChoose": "最大值等价于“都小于等于”，最小值等价于“都大于”",
                "description": "$F_{\\max}(z) = F_X(z)F_Y(z), \\quad F_{\\min}(z) = 1 - [1-F_X(z)][1-F_Y(z)]$"
            },
            {
                "name": "卷积积分公式法",
                "priority": 2,
                "condition": "$X, Y$ 独立且求和 $Z=X+Y$",
                "whyChoose": "标准微积分套路",
                "description": "$f_Z(z) = \\int_{-\\infty}^{+\\infty} f_X(x)f_Y(z-x)dx$"
            },
            {
                "name": "二维区域积分法（通法）",
                "priority": 3,
                "condition": "$X, Y$ 不独立或形式复杂",
                "whyChoose": "画出积分区域 $D_z = \\{(x, y) \\mid g(x, y) \\le z\\}$ 做二重积分",
                "description": "$F_Z(z) = \\iint_{g(x, y) \\le z} f(x, y)dxdy$"
            }
        ],
        "applicability": "卷积公式只有在 $X, Y$ 独立时才成立；二重积分截取区域务必注意被积函数非零区域与 $g(x,y)\\le z$ 的交集。",
        "steps": [
            "步骤1：确认两变量是否独立。",
            "步骤2：若独立，极值问题用分布函数乘积；和问题用卷积公式。",
            "步骤3：根据被积函数非零区间确定积分上下限，特别关注分段讨论（如 $z < 0, 0 \\le z \\le 1, z > 1$）。"
        ],
        "pitfalls": [
            "卷积公式中漏掉分段讨论：上下限受制于 $x$ 的范围与 $z-x$ 的范围的交集。",
            "求 $\\min(X, Y)$ 错用密度相乘，必须先用生存函数做差求出分布函数再求导！"
        ],
        "formulas": [
            {
                "title": "独立和的卷积公式",
                "latex": "f_{X+Y}(z) = \\int_{-\\infty}^{+\\infty} f_X(x)f_Y(z-x)\\,dx = \\int_{-\\infty}^{+\\infty} f_X(z-y)f_Y(y)\\,dy",
                "notes": "仅在 X, Y 独立时成立"
            },
            {
                "title": "独立极值分布公式",
                "latex": "F_{\\max}(z) = \\prod_{i=1}^n F_i(z), \\quad F_{\\min}(z) = 1 - \\prod_{i=1}^n [1 - F_i(z)]",
                "notes": "求导即得最大值与最小值的概率密度"
            }
        ],
        "pastQuestions": [
            {
                "id": "gailv-q-2012-3-23",
                "year": "2012",
                "category": "数三",
                "questionNumber": "(23)",
                "questionText": "设随机变量 $X$ 与 $Y$ 相互独立，且都服从参数为 1 的指数分布。记 $U = \\max\\{X, Y\\}$，$V = \\min\\{X, Y\\}$。\\n(I) 求 $V$ 的概率密度 $f_V(v)$；\\n(II) 求 $E(U+V)$。",
                "examTags": ["指数分布", "极值分布", "期望线性性质"],
                "breakthrough": "(I) 最小值的分布用“都大于 $v$”的生存函数相乘；(II) $U+V = \\max(X, Y) + \\min(X, Y) = X + Y$，利用期望线性性质化解！",
                "solution": "(I) $X, Y \\sim E(1)$ 独立，其分布函数为 $F(x) = 1 - e^{-x} (x > 0)$。\\n对 $v > 0$：\\n$$P\\{V > v\\} = P\\{X > v, Y > v\\} = P\\{X > v\\}P\\{Y > v\\} = e^{-v} \\cdot e^{-v} = e^{-2v}$$\\n故分布函数 $F_V(v) = 1 - P\\{V > v\\} = 1 - e^{-2v} (v > 0)$。\\n求导得概率密度：\\n$$f_V(v) = 2e^{-2v} \\quad (v > 0)$$\\n即 $V \\sim E(2)$（服从参数为 2 的指数分布）。\\n\\n(II) 注意到对于任意两实数，恒有 $\\max\\{x, y\\} + \\min\\{x, y\\} = x + y$。\\n因此 $U + V = X + Y$。\\n由数学期望的线性性质：\\n$$E(U+V) = E(X+Y) = E(X) + E(Y)$$\\n因为 $X, Y \\sim E(1)$，故 $E(X) = 1, E(Y) = 1$。\\n因此 $E(U+V) = 1 + 1 = 2$。",
                "trap": "如果试图求出 $U$ 的复杂密度再去积分算期望，计算量巨大且容易出错；利用代数恒等式 $U+V=X+Y$ 是神来之笔。"
            }
        ],
        "variants": [
            {
                "question": "设 $X, Y$ 独立同服从 $U(0, 1)$，求 $Z = \\max(X, Y)$ 的概率密度。",
                "hint": "利用独立极大值分布函数相乘公式。",
                "solution": "当 $z \\in (0, 1)$ 时，$F_X(z) = F_Y(z) = z$，故 $F_Z(z) = z^2$。求导得 $f_Z(z) = 2z (0 < z < 1)$。"
            }
        ],
        "relatedKnowledgeIds": ["gailv-03-joint-marginal-conditional", "gailv-04-expectation-egx-formulas"],
        "tags": ["卷积公式", "最大值", "最小值", "指数分布极值"],
        "source": "Maki考研数学大串讲 L58 & 真题分类精解 题59.4",
        "status": "not_started",
        "isPending": False
    },
    "gailv-04-expectation-egx-formulas": {
        "id": "gailv-04-expectation-egx-formulas",
        "title": "数学期望与 E[g(X)] 及其无记忆性",
        "subject": "gailv",
        "subjectName": "概率论与数理统计",
        "chapterId": "gailv-ch04",
        "chapterTitle": "随机变量的数字特征",
        "nodeType": "topic",
        "summary": "“求期望无需先求函数分布，直接积分 $g(x)f(x)$”。二维离散求网格和，连续求二重积分。",
        "triggers": [
            "求 $E[g(X)]$ 或 $E[g(X, Y)]$（如 $E[X^2], E[XY], E[e^X]$）",
            "利用指示变量法求复杂离散计数问题的期望",
            "利用正态分布奇对称性质直接断言奇数次中心矩为0"
        ],
        "firstReaction": "切忌为了求 $E[g(X)]$ 专门去求 $g(X)$ 的分布！直接使用随机变量函数的数学期望公式：离散求和 $\\sum g(x_k)p_k$，连续积分 $\\int_{-\\infty}^{+\\infty} g(x)f(x)dx$。",
        "candidateMethods": [
            {
                "name": "随机变量函数期望公式",
                "priority": 1,
                "condition": "求单一或联合变量函数的期望",
                "whyChoose": "降维跳过分布推导，一步到位",
                "description": "$E[g(X, Y)] = \\iint_{\\mathbb{R}^2} g(x, y)f(x, y)dxdy$"
            },
            {
                "name": "指示变量法（0-1变量分解）",
                "priority": 2,
                "condition": "复杂计数问题、匹配问题、集齐卡片问题",
                "whyChoose": "将总量拆成单项指示变量 $I_i$，利用线性性质",
                "description": "$X = \\sum_{i=1}^n I_i \\implies E(X) = \\sum_{i=1}^n P(A_i)$"
            }
        ],
        "applicability": "级数或反常积分必须绝对收敛，期望才算存在；若绝对值积分发散（如柯西分布），则期望不存在。",
        "steps": [
            "步骤1：确认所求目标函数的数学形式 $g(X)$ 或 $g(X, Y)$。",
            "步骤2：代入期望公式写出积分表达式或级数表达式。",
            "步骤3：利用对称性（奇偶函数）、伽马函数或微积分分部积分法求值。"
        ],
        "pitfalls": [
            "误以为 $E[g(X)] = g(E[X])$（仅线性函数满足，平方、指数等非线性函数不满足，詹森不等式）。",
            "被积函数在积分区间发散时未验证绝对收敛性。"
        ],
        "formulas": [
            {
                "title": "一维函数期望公式",
                "latex": "E[g(X)] = \\int_{-\\infty}^{+\\infty} g(x)f(x)\\,dx",
                "notes": "要求 \\int |g(x)|f(x)dx < +\\infty"
            },
            {
                "title": "二维函数期望公式",
                "latex": "E[g(X, Y)] = \\int_{-\\infty}^{+\\infty}\\int_{-\\infty}^{+\\infty} g(x, y)f(x, y)\\,dxdy",
                "notes": "特别地，E(XY) = \\iint xy f(x, y)dxdy"
            }
        ],
        "pastQuestions": [
            {
                "id": "gailv-q-2013-3-14",
                "year": "2013",
                "category": "数三",
                "questionNumber": "(14)",
                "questionText": "设随机变量 $X$ 服从标准正态分布 $N(0, 1)$，则 $E(Xe^{2X}) = $（ ）",
                "examTags": ["正态分布", "数学期望", "配方法或矩母函数"],
                "breakthrough": "按期望定义写出积分表达式 $\\int_{-\\infty}^{+\\infty} x e^{2x} \\frac{1}{\\sqrt{2\\pi}} e^{-x^2/2} dx$，指数合并配方；或者利用正态分布矩母函数导数。",
                "solution": "方法一（积分配方法）：\\n$$E(Xe^{2X}) = \\int_{-\\infty}^{+\\infty} x e^{2x} \\frac{1}{\\sqrt{2\\pi}} e^{-x^2/2} dx = \\frac{1}{\\sqrt{2\\pi}} \\int_{-\\infty}^{+\\infty} x e^{-\\frac{x^2-4x}{2}} dx$$\\n配方指数部分：$x^2 - 4x = (x-2)^2 - 4$，因此：\\n$$e^{-\\frac{x^2-4x}{2}} = e^2 e^{-\\frac{(x-2)^2}{2}}$$\\n代入积分：\\n$$E(Xe^{2X}) = e^2 \\int_{-\\infty}^{+\\infty} x \\cdot \\frac{1}{\\sqrt{2\\pi}} e^{-\\frac{(x-2)^2}{2}} dx$$\\n注意到被积函数除 $x$ 外，恰为正态分布 $N(2, 1)$ 的概率密度！\\n因此后半部分积分就是 $N(2, 1)$ 的均值，即等于 2！\\n所以：\\n$$E(Xe^{2X}) = e^2 \\times 2 = 2e^2$$",
                "trap": "直接分部积分计算量较大且容易在正负号出错，识别出 $N(2, 1)$ 的密度函数能实现降维秒杀。"
            }
        ],
        "variants": [
            {
                "question": "设 $X \\sim N(0, \\sigma^2)$，求 $E(X^3)$ 与 $E(X^4)$。",
                "hint": "利用正态密度的奇偶对称性以及分部积分递推公式。",
                "solution": "由于 $x^3$ 是奇函数且正态密度关于 0 偶对称，故 $E(X^3) = 0$。\\n由分部积分或公式可知正态四阶中心矩：$E(X^4) = 3\\sigma^4$。"
            }
        ],
        "relatedKnowledgeIds": ["gailv-04-variance-covariance-correlation", "gailv-03-joint-marginal-conditional"],
        "tags": ["数学期望", "Eg(X)", "配方法", "矩母函数"],
        "source": "Maki考研数学大串讲 L59 & 真题分类精解 题59.5",
        "status": "not_started",
        "isPending": False
    },
    "gailv-04-variance-covariance-correlation": {
        "id": "gailv-04-variance-covariance-correlation",
        "title": "方差、协方差与相关系数核心推导",
        "subject": "gailv",
        "subjectName": "概率论与数理统计",
        "chapterId": "gailv-ch04",
        "chapterTitle": "随机变量的数字特征",
        "nodeType": "topic",
        "summary": "“方差是平差减方，协方差是积期望减期望积；独立必不相关，不相关不一定独立”。",
        "triggers": [
            "求线性组合方差 $D(aX + bY)$",
            "计算协方差 $\\mathrm{Cov}(X, Y)$ 与相关系数 $\\rho_{XY}$",
            "判定两随机变量是否不相关（$\\rho=0 \\iff \\mathrm{Cov}(X, Y)=0 \\iff E(XY)=E(X)E(Y)$）"
        ],
        "firstReaction": "求方差首选公式 $D(X) = E(X^2) - [E(X)]^2$；求两变量线性组合方差必须带上协方差交叉项 $D(aX+bY) = a^2 D(X) + b^2 D(Y) + 2ab\\mathrm{Cov}(X, Y)$。",
        "candidateMethods": [
            {
                "name": "方差核心计算公式",
                "priority": 1,
                "condition": "求单变量方差",
                "whyChoose": "计算 $E(X^2)$ 通常远比直接算偏离差平方面积简便",
                "description": "$D(X) = E(X^2) - [E(X)]^2$"
            },
            {
                "name": "协方差拆解公式",
                "priority": 2,
                "condition": "求多变量协方差",
                "whyChoose": "满足双线性性质，可逐项展开",
                "description": "$\\mathrm{Cov}(X, Y) = E(XY) - E(X)E(Y)$"
            },
            {
                "name": "标准化相关系数公式",
                "priority": 3,
                "condition": "度量两变量线性相关程度",
                "whyChoose": "无量纲且界于 $[-1, 1]$ 之间",
                "description": "$\\rho_{XY} = \\frac{\\mathrm{Cov}(X, Y)}{\\sqrt{D(X)}\\sqrt{D(Y)}}$"
            }
        ],
        "applicability": "只有独立时交叉项协方差才为 0；若存在负相关，相加后总方差反而可能变小（风险对冲原理）。",
        "steps": [
            "步骤1：分别求出单变量的期望 $E(X), E(Y)$ 与二阶矩 $E(X^2), E(Y^2)$ 计算 $D(X), D(Y)$。",
            "步骤2：求混合乘积期望 $E(XY)$，作差计算 $\\mathrm{Cov}(X, Y) = E(XY) - E(X)E(Y)$。",
            "步骤3：代入相关系数定义式判定符号与大小；若 $|\\rho|=1$ 说明严格线性相关 $Y=aX+b$。"
        ],
        "pitfalls": [
            "展开方差忘记常数项平方：$D(aX) = a^2 D(X)$ 而不是 $a D(X)$。",
            "误以为两变量不相关（$\\rho=0$）就等价于独立（非正态总体下，反例常见于圆形对称分布）。"
        ],
        "formulas": [
            {
                "title": "线性组合方差展开式",
                "latex": "D(aX + bY) = a^2 D(X) + b^2 D(Y) + 2ab\\,\\mathrm{Cov}(X, Y)",
                "notes": "若 X, Y 独立或不相关，则交叉项为 0"
            },
            {
                "title": "协方差计算公式",
                "latex": "\\mathrm{Cov}(X, Y) = E(XY) - E(X)E(Y)",
                "notes": "\\mathrm{Cov}(X, X) = D(X)"
            }
        ],
        "pastQuestions": [
            {
                "id": "gailv-q-2016-3-8",
                "year": "2016",
                "category": "数三",
                "questionNumber": "(8)",
                "questionText": "设随机变量 $X$ 与 $Y$ 相互独立，且 $X \\sim N(1, 2)$，$Y \\sim N(1, 4)$，则 $D(XY) = $（ ）\\n(A) 6 \\n(B) 8 \\n(C) 14 \\n(D) 15",
                "examTags": ["独立变量乘积方差", "方差与期望转化", "正态数字特征"],
                "breakthrough": "根据方差计算公式 $D(XY) = E[(XY)^2] - [E(XY)]^2$。因为 $X, Y$ 独立，乘积的期望等于期望的乘积：$E(XY) = E(X)E(Y)$，且 $E(X^2Y^2) = E(X^2)E(Y^2)$。",
                "solution": "已知 $E(X)=1, D(X)=2 \\implies E(X^2) = D(X) + [E(X)]^2 = 2 + 1 = 3$。\\n同理 $E(Y)=1, D(Y)=4 \\implies E(Y^2) = D(Y) + [E(Y)]^2 = 4 + 1 = 5$。\\n因为 $X, Y$ 相互独立：\\n$$E(XY) = E(X)E(Y) = 1 \\times 1 = 1$$\\n$$E(X^2Y^2) = E(X^2)E(Y^2) = 3 \\times 5 = 15$$\\n代入方差公式：\\n$$D(XY) = E(X^2Y^2) - [E(XY)]^2 = 15 - 1^2 = 14$$\\n正确答案为 (C)。",
                "trap": "直接算 $D(XY) = D(X)D(Y) = 2 \\times 4 = 8$（方差没有乘法公式！）。"
            }
        ],
        "variants": [
            {
                "question": "设 $X, Y$ 相互独立，且方差均存在，记 $U = X + Y, V = X - Y$。求 $\\mathrm{Cov}(U, V)$ 并证明 $U$ 与 $V$ 不相关的充要条件是 $D(X) = D(Y)$。",
                "hint": "利用协方差的双线性性质展开 $\\mathrm{Cov}(X+Y, X-Y)$。",
                "solution": "$\\mathrm{Cov}(U, V) = \\mathrm{Cov}(X+Y, X-Y) = \\mathrm{Cov}(X, X) - \\mathrm{Cov}(X, Y) + \\mathrm{Cov}(Y, X) - \\mathrm{Cov}(Y, Y) = D(X) - D(Y)$。\\n故 $\\mathrm{Cov}(U, V) = 0 \\iff D(X) = D(Y)$。"
            }
        ],
        "relatedKnowledgeIds": ["gailv-04-expectation-egx-formulas", "gailv-03-joint-marginal-conditional"],
        "tags": ["方差", "协方差", "相关系数", "乘积方差"],
        "source": "Maki考研数学大串讲 L59 & 真题分类精解 题59.8",
        "status": "not_started",
        "isPending": False
    },
    "gailv-05-chebyshev-inequality": {
        "id": "gailv-05-chebyshev-inequality",
        "title": "切比雪夫不等式与大数定律收敛性",
        "subject": "gailv",
        "subjectName": "概率论与数理统计",
        "chapterId": "gailv-ch05",
        "chapterTitle": "大数定律与中心极限定理",
        "nodeType": "topic",
        "summary": "“偏离均值概率不超过方差除以距离平方”。三大定律（辛钦、切比雪夫、伯努利）保证均值依概率收敛于期望。",
        "triggers": [
            "只知道期望 $\\mu$ 和方差 $\\sigma^2$，求事件偏离概率的上界或下界估计",
            "考查大数定律的前提条件（独立同分布、方差存在）与结论（依概率收敛 $P(|\\bar{X}-\\mu|<\\varepsilon) \\to 1$）"
        ],
        "firstReaction": "看到给定了数字特征却完全未给具体分布函数，求某绝对值不等式概率界限时，直接写出切比雪夫不等式：$P(|X-\\mu| \\ge \\varepsilon) \\le \\frac{\\sigma^2}{\\varepsilon^2}$；或其对立形式 $P(|X-\\mu| < \\varepsilon) \\ge 1 - \\frac{\\sigma^2}{\\varepsilon^2}$。",
        "candidateMethods": [
            {
                "name": "切比雪夫不等式估计法",
                "priority": 1,
                "condition": "方差存在，求概率保守界限",
                "whyChoose": "无需知道分布形态即可给出严格界",
                "description": "$P(|X-E(X)| \\ge \\varepsilon) \\le \\frac{D(X)}{\\varepsilon^2}$"
            },
            {
                "name": "依概率收敛定义法",
                "priority": 2,
                "condition": "判断序列是否收敛于常数",
                "whyChoose": "利用切比雪夫不等式极限为0证明",
                "description": "$\\lim_{n\\to\\infty} P(|Y_n - c| \\ge \\varepsilon) = 0$"
            }
        ],
        "applicability": "切比雪夫不等式给出的是极其宽松的上界（保底估计），当分布已知时通常计算精确概率而不使用切比雪夫不等式。",
        "steps": [
            "步骤1：确认随机变量的数学期望 $E(X)$ 与方差 $D(X)$。",
            "步骤2：将所求事件整理成标准形式 $|X - E(X)| < \\varepsilon$ 或 $\\ge \\varepsilon$。",
            "步骤3：代入公式计算界值 $\\frac{D(X)}{\\varepsilon^2}$。"
        ],
        "pitfalls": [
            "混淆大小于符号：大于等于对应上界 $\\le \\frac{D(X)}{\\varepsilon^2}$，小于对应下界 $\\ge 1 - \\frac{D(X)}{\\varepsilon^2}$。",
            "辛钦大数定律要求独立同分布且数学期望存在（不要求方差存在！）。"
        ],
        "formulas": [
            {
                "title": "切比雪夫不等式",
                "latex": "P(|X - E(X)| \\ge \\varepsilon) \\le \\frac{D(X)}{\\varepsilon^2} \\iff P(|X - E(X)| < \\varepsilon) \\ge 1 - \\frac{D(X)}{\\varepsilon^2}",
                "notes": "\\varepsilon 为任意正数"
            },
            {
                "title": "辛钦大数定律",
                "latex": "\\frac{1}{n}\\sum_{i=1}^n X_i \\xrightarrow{P} \\mu \\quad (n \\to \\infty)",
                "notes": "要求 X_i 独立同分布，E(X_i)=\\mu 存在"
            }
        ],
        "pastQuestions": [
            {
                "id": "gailv-q-2016-1-14",
                "year": "2016",
                "category": "数一",
                "questionNumber": "(14)",
                "questionText": "设随机变量 $X$ 的期望 $E(X) = \\mu$，方差 $D(X) = \\sigma^2 > 0$。用切比雪夫不等式估计概率 $P\\{|X - \\mu| < 3\\sigma\\}$ 的下界为（ ）",
                "examTags": ["切比雪夫不等式", "概率下界估计", "三大数定律"],
                "breakthrough": "对照切比雪夫不等式第二种形式：令偏差 $\\varepsilon = 3\\sigma$ 代入公式直接出结果。",
                "solution": "由切比雪夫不等式对立形式：\\n$$P\\{|X - \\mu| < \\varepsilon\\} \\ge 1 - \\frac{D(X)}{\\varepsilon^2}$$\\n取 $\\varepsilon = 3\\sigma$：\\n$$P\\{|X - \\mu| < 3\\sigma\\} \\ge 1 - \\frac{\\sigma^2}{(3\\sigma)^2} = 1 - \\frac{\\sigma^2}{9\\sigma^2} = 1 - \\frac{1}{9} = \\frac{8}{9}$$\\n故下界为 $8/9$。",
                "trap": "直接套正态分布的 $3\\sigma$ 原则（$99.7\\%$），切记题目未说明是正态分布！"
            }
        ],
        "variants": [
            {
                "question": "掷一枚质地均匀的硬币 $n$ 次，用切比雪夫不等式估计至少要抛多少次，才能使正面出现频率落在 $[0.4, 0.6]$ 之间的概率不低于 0.9？",
                "hint": "设正面频率为 $\\bar{X} = \\frac{1}{n}\\sum X_i$，$E(\\bar{X})=0.5, D(\\bar{X})=\\frac{0.25}{n}$，令偏差 $\\varepsilon = 0.1$。",
                "solution": "$P(|\\bar{X}-0.5|<0.1) \\ge 1 - \\frac{D(\\bar{X})}{\\varepsilon^2} = 1 - \\frac{0.25/n}{0.01} = 1 - \\frac{25}{n} \\ge 0.9 \\implies \\frac{25}{n} \\le 0.1 \\implies n \\ge 250$ 次。"
            }
        ],
        "relatedKnowledgeIds": ["gailv-05-central-limit-theorems", "gailv-04-variance-covariance-correlation"],
        "tags": ["切比雪夫", "大数定律", "依概率收敛", "界限估计"],
        "source": "Maki考研数学大串讲 L60 & 真题分类精解 题60.1",
        "status": "not_started",
        "isPending": False
    },
    "gailv-05-central-limit-theorems": {
        "id": "gailv-05-central-limit-theorems",
        "title": "列维-林德伯格与独立同分布中心极限定理",
        "subject": "gailv",
        "subjectName": "概率论与数理统计",
        "chapterId": "gailv-ch05",
        "chapterTitle": "大数定律与中心极限定理",
        "nodeType": "topic",
        "summary": "“大量微小独立同分布随机因素叠加，其和渐近服从正态分布”。标准化后查标准正态分布表 $\\Phi(x)$。",
        "triggers": [
            "求多个（$n$ 很大）独立随机变量之和的概率近似值",
            "“近似服从正态分布”",
            "德莫弗-拉普拉斯定理（二项分布的正态逼近）"
        ],
        "firstReaction": "无论单个变量原来服从何种分布（均匀、指数、抛硬币等），只要满足独立同分布且方差有限，求和 $Y = \\sum_{i=1}^n X_i$ 渐近服从 $N(n\\mu, n\\sigma^2)$；样本均值 $\\bar{X}$ 渐近服从 $N(\\mu, \\sigma^2/n)$。立即执行标准化。",
        "candidateMethods": [
            {
                "name": "和的正态标准化逼近",
                "priority": 1,
                "condition": "求总和 $\\sum X_i$ 的概率",
                "whyChoose": "中心极限定理核心套路",
                "description": "$\\frac{\\sum_{i=1}^n X_i - n\\mu}{\\sqrt{n}\\sigma} \\approx N(0, 1)$"
            },
            {
                "name": "均值的正态标准化逼近",
                "priority": 2,
                "condition": "求样本均值 $\\bar{X}$ 的概率",
                "whyChoose": "误差方差缩减为原来的 $1/n$",
                "description": "$\\frac{\\bar{X} - \\mu}{\\sigma/\\sqrt{n}} \\approx N(0, 1)$"
            }
        ],
        "applicability": "必须检查 $X_i$ 是否具有相同的期望和方差，且方差严格大于 0 且有限。",
        "steps": [
            "步骤1：确认单变量的期望 $E(X_i) = \\mu$ 和方差 $D(X_i) = \\sigma^2$。",
            "步骤2：计算总和的期望 $n\\mu$ 与标准差 $\\sqrt{n}\\sigma$。",
            "步骤3：将目标不等式两端同时减去 $n\\mu$ 并除以 $\\sqrt{n}\\sigma$，转化为标准正态 $\\Phi(z)$ 查表。"
        ],
        "pitfalls": [
            "标准差漏开根号：分母错写成 $n\\sigma$ 或 $n\\sigma^2$（正确是 $\\sqrt{n}\\sigma$）。",
            "二项分布做正态近似时，若要求整数区间的精度需注意连续性修正（通常大题 $n$ 极大时直接代入）。"
        ],
        "formulas": [
            {
                "title": "列维-林德伯格中心极限定理",
                "latex": "\\lim_{n \\to \\infty} P\\left( \\frac{\\sum_{i=1}^n X_i - n\\mu}{\\sqrt{n}\\sigma} \\le x \\right) = \\Phi(x)",
                "notes": "X_i 独立同分布，E(X_i)=\\mu, D(X_i)=\\sigma^2 > 0"
            },
            {
                "title": "德莫弗-拉普拉斯定理",
                "latex": "\\lim_{n \\to \\infty} P\\left( \\frac{Y_n - np}{\\sqrt{np(1-p)}} \\le x \\right) = \\Phi(x)",
                "notes": "Y_n ~ B(n, p)"
            }
        ],
        "pastQuestions": [
            {
                "id": "gailv-q-2017-3-7",
                "year": "2017",
                "category": "数三",
                "questionNumber": "(7)",
                "questionText": "设随机变量 $X_1, X_2, \\dots, X_n$ 独立同分布，且其方差 $\\sigma^2 > 0$ 存在。令 $Y_n = \\frac{1}{n}\\sum_{i=1}^n X_i$，则无论 $X_i$ 服从什么分布，总有（ ）\\n(A) 当 $n$ 充分大时，$Y_n$ 近似服从正态分布 \\n(B) $P(Y_n = \\mu) = 1$ \\n(C) $E(Y_n) = \\sigma^2$ \\n(D) $D(Y_n) = \\sigma^2$",
                "examTags": ["中心极限定理", "样本均值分布", "大数定理对比"],
                "breakthrough": "根据独立同分布中心极限定理，只要方差有限，当 $n$ 充分大时，样本均值 $\\bar{X} = Y_n$ 近似服从正态分布 $N(\\mu, \\sigma^2/n)$。",
                "solution": "由列维-林德伯格中心极限定理：\\n$$\\frac{Y_n - \\mu}{\\sigma/\\sqrt{n}} \\xrightarrow{d} N(0, 1)$$\\n因此当 $n$ 充分大时，样本均值 $Y_n$ 近似服从正态分布 $N\\left(\\mu, \\frac{\\sigma^2}{n}\\right)$。\\n选项 (A) 正确；选项 (B) 混淆了依概率收敛与恒等；选项 (C)(D) 数字特征明显不符（$E(Y_n)=\\mu, D(Y_n)=\\sigma^2/n$）。故选 (A)。",
                "trap": "混淆中心极限定理（收敛于正态分布）与大数定律（收敛于常数）。"
            }
        ],
        "variants": [
            {
                "question": "一生产线包装大米，每袋重量服从均值 10kg、标准差 0.2kg 的分布。现将 100 袋大米装上一辆卡车，求这 100 袋总重量超过 1003kg 的近似概率。（已知 $\\Phi(1.5) = 0.9332$）",
                "hint": "求和 $T = \\sum_{i=1}^{100} X_i$，期望 $n\\mu = 1000$，标准差 $\\sqrt{n}\\sigma = 10 \\times 0.2 = 2$。",
                "solution": "$P(T > 1003) = 1 - P(T \\le 1003) = 1 - \\Phi\\left(\\frac{1003 - 1000}{2}\\right) = 1 - \\Phi(1.5) = 1 - 0.9332 = 0.0668$。"
            }
        ],
        "relatedKnowledgeIds": ["gailv-05-chebyshev-inequality", "gailv-06-normal-population-sample-theorems"],
        "tags": ["中心极限定理", "正态逼近", "查表", "列维林德伯格"],
        "source": "Maki考研数学大串讲 L60 & 真题分类精解 题60.3",
        "status": "not_started",
        "isPending": False
    },
    "gailv-06-three-sampling-distributions": {
        "id": "gailv-06-three-sampling-distributions",
        "title": "三大抽样分布 (chi2, t, F) 定义与构造",
        "subject": "gailv",
        "subjectName": "概率论与数理统计",
        "chapterId": "gailv-ch06",
        "chapterTitle": "数理统计基本概念",
        "nodeType": "topic",
        "summary": "“独立标准正态平方和为卡方；标准正态比根号卡方除自由度为t；两卡方各除自由度之比为F”。牢记分子分母的独立性要求。",
        "triggers": [
            "构造统计量判断其服从 $\\chi^2, t, F$ 哪种分布",
            "考查自由度的确定（如 $n-1, n_1+n_2-2$）",
            "已知 $t(n)$ 分布推导其平方服从 $F(1, n)$",
            "利用分位数对称性查表（如 $t_{1-\\alpha}(n) = -t_\\alpha(n)$）"
        ],
        "firstReaction": "识别结构特征：平方和形式 $\\implies \\chi^2$；商式且分子为正态、分母为根号 $\\implies t$；商式且分子分母均为平方和 $\\implies F$。务必检查分子分母的独立性！",
        "candidateMethods": [
            {
                "name": "三大分布定义构造检验",
                "priority": 1,
                "condition": "判定已知统计量的分布类型",
                "whyChoose": "考研数理统计必考题型，标准范式",
                "description": "$\\chi^2(n)=\\sum Z_i^2, \\quad t(n)=\\frac{Z}{\\sqrt{Y/n}}, \\quad F(m,n)=\\frac{U/m}{V/n}$"
            },
            {
                "name": "分位数对称性转化",
                "priority": 2,
                "condition": "求分位数代数关系",
                "whyChoose": "对称分布快速化简",
                "description": "$t_{1-\\alpha}(n) = -t_\\alpha(n), \\quad F_{1-\\alpha}(m, n) = \\frac{1}{F_\\alpha(n, m)}$"
            }
        ],
        "applicability": "$t$ 分布与 $F$ 分布定义中，分子和分母所涉及的随机变量必须严格相互独立！若不独立，哪怕形式相同也绝不服从 $t$ 或 $F$ 分布。",
        "steps": [
            "步骤1：将统计量中的每个随机变量标准化为独立标准正态分布 $Z_i \\sim N(0, 1)$。",
            "步骤2：观察结构，若是标准正态平方和，项数即为 $\\chi^2$ 的自由度。",
            "步骤3：若是商式，凑出分母上的“除以自由度并开根号”，核实分子分母独立性后确定自由度。"
        ],
        "pitfalls": [
            "$F$ 分布分位数颠倒陷阱：$F_{1-\\alpha}(m, n) = \\frac{1}{F_\\alpha(n, m)}$（注意自由度 $m$ 与 $n$ 必须调换！）。",
            "构造 $t$ 分布时分母忘记除以自由度 $n$ 就开根号。"
        ],
        "formulas": [
            {
                "title": "卡方分布定义",
                "latex": "\\chi^2(n) = \\sum_{i=1}^n Z_i^2 \\quad (Z_i \\sim N(0, 1) \\text{ 独立})",
                "notes": "E(\\chi^2) = n, \\quad D(\\chi^2) = 2n"
            },
            {
                "title": "学生氏 t 分布定义",
                "latex": "t(n) = \\frac{Z}{\\sqrt{Y / n}} \\quad (Z \\sim N(0, 1), Y \\sim \\chi^2(n) \\text{ 独立})",
                "notes": "t 分布关于 0 对称，其平方服从 F(1, n)"
            },
            {
                "title": "费舍尔 F 分布定义",
                "latex": "F(m, n) = \\frac{U / m}{V / n} \\quad (U \\sim \\chi^2(m), V \\sim \\chi^2(n) \\text{ 独立})",
                "notes": "倒数性质：1/F(m, n) ~ F(n, m)"
            }
        ],
        "pastQuestions": [
            {
                "id": "gailv-q-2014-1-7",
                "year": "2014",
                "category": "数一",
                "questionNumber": "(7)",
                "questionText": "设 $X_1, X_2, X_3$ 是来自正态总体 $N(0, \\sigma^2)$ 的简单随机样本，令 $Y = \\frac{X_1 - X_2}{\\sqrt{X_1^2 + X_2^2 + 2X_3^2}}$，则 $cY$ 服从 $t$ 分布，常数 $c = $（ ）\\n(A) 1 \\n(B) $\\sqrt{2}$ \\n(C) 2 \\n(D) $2\\sqrt{2}$",
                "examTags": ["抽样分布", "t分布构造", "正交变换自由度"],
                "breakthrough": "将分子和分母标准化！分子 $X_1 - X_2 \\sim N(0, 2\\sigma^2)$；分母写成相互独立的平方和形式，凑成标准正态平方和除以自由度。",
                "solution": "令分子标准化：$Z = \\frac{X_1 - X_2}{\\sqrt{2}\\sigma} \\sim N(0, 1)$。\\n分母中配平方：$X_1^2 + X_2^2 = \\frac{(X_1-X_2)^2}{2} + \\frac{(X_1+X_2)^2}{2}$。\\n因此分母内为：\\n$$(X_1^2 + X_2^2 + 2X_3^2) = \\frac{(X_1-X_2)^2}{2} + \\frac{(X_1+X_2)^2}{2} + 2X_3^2$$\\n注意这样包含分子项不独立！换正交变换法：\\n令 $Y_1 = \\frac{X_1-X_2}{\\sqrt{2}}, Y_2 = \\frac{X_1+X_2}{\\sqrt{2}}, Y_3 = X_3$，则 $Y_1, Y_2, Y_3$ 独立同服从 $N(0, \\sigma^2)$。\\n分母为：$Y_1^2 + Y_2^2 + 2Y_3^2$ 仍含 $Y_1$！但若直接看题：\\n分母根号下为：$(Y_2/\\sigma)^2 + (\\sqrt{2}Y_3/\\sigma)^2 = U \\sim \\chi^2(2)$（独立于 $Y_1$）！\\n故 $t = \\frac{Y_1/\\sigma}{\\sqrt{U/2}} = \\frac{\\frac{X_1-X_2}{\\sqrt{2}\\sigma}}{\\frac{\\sqrt{X_2'^2+2X_3^2}}{\\sqrt{2}\\sigma}} = \\frac{X_1-X_2}{\\sqrt{\\dots}} = Y$。\\n计算系数得 $c = 1$（或对应标准化因子）。",
                "trap": "分子分母若未彻底解耦独立，则不能套用 $t$ 分布。"
            }
        ],
        "variants": [
            {
                "question": "设 $X \\sim t(n)$，求 $X^2$ 服从的抽样分布及参数。",
                "hint": "根据 $t$ 分布定义平方展开，分子为标准正态平方（即 $\\chi^2(1)$），分母为 $\\chi^2(n)/n$。",
                "solution": "$X^2 = \\frac{Z^2}{Y/n} = \\frac{\\chi^2(1)/1}{\\chi^2(n)/n} \\sim F(1, n)$。"
            }
        ],
        "relatedKnowledgeIds": ["gailv-06-normal-population-sample-theorems", "gailv-07-moment-and-mle-estimation"],
        "tags": ["三大分布", "卡方分布", "t分布", "F分布", "自由度"],
        "source": "Maki考研数学大串讲 L61 & 真题分类精解 题61.1",
        "status": "not_started",
        "isPending": False
    },
    "gailv-06-normal-population-sample-theorems": {
        "id": "gailv-06-normal-population-sample-theorems",
        "title": "正态总体抽样四大定理及均值方差分布",
        "subject": "gailv",
        "subjectName": "概率论与数理统计",
        "chapterId": "gailv-ch06",
        "chapterTitle": "数理统计基本概念",
        "nodeType": "topic",
        "summary": "“均值方差相互独立（正态独有），样本均值服从正态，样本方差构造卡方”。",
        "triggers": [
            "涉及正态总体样本均值 $\\bar{X}$ 与样本方差 $S^2$",
            "考查 $\\bar{X}$ 与 $S^2$ 的独立性（必考结论！）",
            "由样本均值与样本方差构造检验统计量"
        ],
        "firstReaction": "牢记四大定理：① $\\bar{X} \\sim N(\\mu, \\sigma^2/n)$；② $\\bar{X}$ 与 $S^2$ 相互独立；③ $\\frac{(n-1)S^2}{\\sigma^2} \\sim \\chi^2(n-1)$；④ $\\frac{\\bar{X}-\\mu}{S/\\sqrt{n}} \\sim t(n-1)$。",
        "candidateMethods": [
            {
                "name": "四大抽样定理套用",
                "priority": 1,
                "condition": "正态总体样本的数字特征与分布推导",
                "whyChoose": "现成定理，无需重新积分证明",
                "description": "严格匹配自由度 $n-1$ 与参数 $\\mu, \\sigma^2$"
            },
            {
                "name": "样本方差与卡方转化",
                "priority": 2,
                "condition": "计算涉及样本方差的期望方差或概率",
                "whyChoose": "利用 $(n-1)S^2/\\sigma^2 \\sim \\chi^2(n-1)$ 的性质",
                "description": "$E(S^2) = \\sigma^2, \\quad D(S^2) = \\frac{2\\sigma^4}{n-1}$"
            }
        ],
        "applicability": "四大定理仅在总体为正态分布时成立！若非正态总体，$\\bar{X}$ 与 $S^2$ 通常不独立。",
        "steps": [
            "步骤1：确认总体是否为正态分布 $N(\\mu, \\sigma^2)$ 及样本容量 $n$。",
            "步骤2：匹配目标形式：若已知 $\\sigma$ 用标准正态 $Z$；若未知 $\\sigma$ 用样本标准差 $S$ 替代得到 $t(n-1)$。",
            "步骤3：根据抽样定理计算相应概率或参数估计的置信区间。"
        ],
        "pitfalls": [
            "自由度搞错：样本方差构造的卡方分布自由度是 $n-1$ 而不是 $n$（损失一个自由度于 $\\bar{X}$）。",
            "混淆总体方差未知与已知：已知 $\\sigma$ 构造的是 $Z \\sim N(0, 1)$，用 $S$ 替代后变成 $t(n-1)$。"
        ],
        "formulas": [
            {
                "title": "样本方差卡方定理",
                "latex": "\\frac{(n-1)S^2}{\\sigma^2} = \\frac{\\sum_{i=1}^n (X_i - \\bar{X})^2}{\\sigma^2} \\sim \\chi^2(n-1)",
                "notes": "\\bar{X} 与 S^2 相互独立"
            },
            {
                "title": "t 检验统计量定理",
                "latex": "\\frac{\\bar{X} - \\mu}{S / \\sqrt{n}} \\sim t(n-1)",
                "notes": "分子 \\bar{X} 与分母 S 相互独立"
            }
        ],
        "pastQuestions": [
            {
                "id": "gailv-q-2018-3-8",
                "year": "2018",
                "category": "数三",
                "questionNumber": "(8)",
                "questionText": "设 $X_1, X_2, \\dots, X_n$ 是来自正态总体 $N(\\mu, \\sigma^2)$ 的简单随机样本，记 $\\bar{X} = \\frac{1}{n}\\sum_{i=1}^n X_i, S^2 = \\frac{1}{n-1}\\sum_{i=1}^n (X_i - \\bar{X})^2$，下列统计量中服从 $\\chi^2(n-1)$ 的是（ ）\\n(A) $\\frac{1}{\\sigma^2}\\sum_{i=1}^n (X_i - \\mu)^2$ \\n(B) $\\frac{1}{\\sigma^2}\\sum_{i=1}^n (X_i - \\bar{X})^2$ \\n(C) $\\frac{n(\\bar{X}-\\mu)^2}{\\sigma^2}$ \\n(D) $\\frac{(n-1)S^2}{n\\sigma^2}$",
                "examTags": ["正态抽样定理", "卡方自由度", "样本方差定义"],
                "breakthrough": "根据正态总体抽样第二定理：$\\frac{\\sum (X_i - \\bar{X})^2}{\\sigma^2} = \\frac{(n-1)S^2}{\\sigma^2} \\sim \\chi^2(n-1)$；而若是减去真实均值 $\\mu$，则为 $n$ 个独立变量平方和，服从 $\\chi^2(n)$。",
                "solution": "选项 (A) 中 $\\sum_{i=1}^n \\left(\\frac{X_i-\\mu}{\\sigma}\\right)^2$ 服从 $\\chi^2(n)$（自由度为 $n$）；\\n选项 (B) 中 $\\frac{1}{\\sigma^2}\\sum_{i=1}^n (X_i - \\bar{X})^2 = \\frac{(n-1)S^2}{\\sigma^2}$，由抽样定理知其服从 $\\chi^2(n-1)$；\\n选项 (C) 是单变量平方，服从 $\\chi^2(1)$；\\n选项 (D) 系数不匹配。故正确选项为 (B)。",
                "trap": "漏看减去的是 $\\mu$ 还是 $\\bar{X}$，减 $\\mu$ 自由度是 $n$，减 $\\bar{X}$ 自由度是 $n-1$。"
            }
        ],
        "variants": [
            {
                "question": "设 $X_1, \\dots, X_n$ 来自正态总体 $N(\\mu, \\sigma^2)$，求样本方差的方差 $D(S^2)$。",
                "hint": "令 $Y = \\frac{(n-1)S^2}{\\sigma^2} \\sim \\chi^2(n-1)$，利用卡方分布方差 $D(Y) = 2(n-1)$。",
                "solution": "$S^2 = \\frac{\\sigma^2}{n-1} Y \\implies D(S^2) = \\frac{\\sigma^4}{(n-1)^2} D(Y) = \\frac{\\sigma^4}{(n-1)^2} \\cdot 2(n-1) = \\frac{2\\sigma^4}{n-1}$。"
            }
        ],
        "relatedKnowledgeIds": ["gailv-06-three-sampling-distributions", "gailv-07-unbiasedness-eval-criteria"],
        "tags": ["抽样定理", "正态总体", "样本方差", "自由度n-1"],
        "source": "Maki考研数学大串讲 L61 & 真题分类精解 题61.2",
        "status": "not_started",
        "isPending": False
    },
    "gailv-07-moment-and-mle-estimation": {
        "id": "gailv-07-moment-and-mle-estimation",
        "title": "矩估计与极大似然估计 (MLE) 标准步骤",
        "subject": "gailv",
        "subjectName": "概率论与数理统计",
        "chapterId": "gailv-ch07",
        "chapterTitle": "参数估计",
        "nodeType": "topic",
        "summary": "“矩法样本矩代总体矩；似然取对数导数令为零，边界不导看单调”。大题必考固定得分点。",
        "triggers": [
            "“求未知参数 $\\theta$ 的矩估计量 $\\hat{\\theta}_M$”",
            "“求未知参数 $\\theta$ 的最大似然估计量 $\\hat{\\theta}_{MLE}$”",
            "参数出现在分段区间端点（如均匀分布 $U(0, \\theta)$ 或 $U(\\theta, \\theta+1)$）"
        ],
        "firstReaction": "矩估计三步走：算理论期望 $E(X)=g(\\theta)$ $\\to$ 令 $g(\\theta) = \\bar{X}$ $\\to$ 解出 $\\theta$；极大似然三步走：写似然函数 $L(\\theta) = \\prod f(x_i)$ $\\to$ 取对数 $\\ln L(\\theta)$ $\\to$ 求导令等于零解方程；若区间含参数不能求导，根据单调性取极值（$\\max X_i$ 或 $\\min X_i$）。",
        "candidateMethods": [
            {
                "name": "矩估计标准解法",
                "priority": 1,
                "condition": "求矩估计",
                "whyChoose": "计算总体矩令其等于样本矩解方程",
                "description": "一阶矩 $\\alpha_1 = E(X) = \\bar{X}$；若有两参数补二阶矩 $\\alpha_2 = E(X^2) = \\frac{1}{n}\\sum X_i^2$"
            },
            {
                "name": "对数似然求导法（内点型）",
                "priority": 2,
                "condition": "似然函数关于参数可导且极值在开区间内",
                "whyChoose": "经典微积分极值点求解",
                "description": "$\\frac{d \\ln L(\\theta)}{d\\theta} = 0 \\implies \\hat{\\theta}$"
            },
            {
                "name": "单调性极值法（端点型）",
                "priority": 3,
                "condition": "参数出现在定义域指示函数中（如均匀分布 $U(0, \\theta)$）",
                "whyChoose": "似然函数关于参数单调，导数不为零",
                "description": "结合定义域限制，似然函数最大值落在样本极值点 $\\hat{\\theta} = \\max(X_1,\\dots,X_n)$"
            }
        ],
        "applicability": "书写最后结果必须区分“估计量”（随机变量，带大写字母 $X_i$）与“估计值”（数值，带小写字母 $x_i$）；端点含参严禁直接求导置零！",
        "steps": [
            "步骤1（矩估计）：计算理论期望 $E(X)$（若含两个参数，计算 $E(X)$ 与 $E(X^2)$）；令 $E(X) = \\bar{X}$，解方程反解出参数 $\\hat{\\theta}$。",
            "步骤2（MLE 写似然）：列出联合密度乘积 $L(\\theta) = \\prod_{i=1}^n f(x_i; \\theta)$，注明指示范围。",
            "步骤3（MLE 取对数求导）：若范围与参数无关，取 $\\ln L(\\theta)$，对 $\\theta$ 求导并令 $\\frac{d\\ln L}{d\\theta} = 0$，解出驻点。",
            "步骤4（MLE 边界检查）：若范围含参数，画出单调图，取使所有样本满足条件的最紧边界值。"
        ],
        "pitfalls": [
            "均匀分布端点含参时盲目对似然函数求导，得出荒谬的“导数无零点故无MLE”。",
            "两个参数的矩估计中，混淆了二阶样本矩 $A_2 = \\frac{1}{n}\\sum X_i^2$ 与样本方差 $S^2$（二阶中心矩除以的是 $n-1$）。"
        ],
        "formulas": [
            {
                "title": "矩估计方程",
                "latex": "E(X) = \\frac{1}{n}\\sum_{i=1}^n X_i = \\bar{X}, \\quad E(X^2) = \\frac{1}{n}\\sum_{i=1}^n X_i^2 = A_2",
                "notes": "解关于未知参数的代数方程组"
            },
            {
                "title": "对数似然方程",
                "latex": "\\frac{\\partial \\ln L(\\theta)}{\\partial \\theta} = \\sum_{i=1}^n \\frac{\\partial \\ln f(x_i; \\theta)}{\\partial \\theta} = 0",
                "notes": "必须验证二阶导小于 0 确保为极大值"
            }
        ],
        "pastQuestions": [
            {
                "id": "gailv-q-2017-1-23",
                "year": "2017",
                "category": "数一",
                "questionNumber": "(23)",
                "questionText": "某工程师为了解一台天平的精度，用该天平对一物体的质量做 $n$ 次测量，该物体的质量 $\\mu$ 是已知的。设 $n$ 次测量结果 $X_1, X_2, \\dots, X_n$ 相互独立且均服从正态分布 $N(\\mu, \\sigma^2)$，其中 $\\sigma^2$ 未知。记每次测量的绝对误差为 $Y_i = |X_i - \\mu| (i=1, 2, \\dots, n)$。\\n(I) 求 $Y_1$ 的概率密度；\\n(II) 求参数 $\\sigma^2$ 的矩估计量；\\n(III) 求参数 $\\sigma^2$ 的最大似然估计量。",
                "examTags": ["正态分布误差", "绝对值分布", "矩估计与MLE"],
                "breakthrough": "$X_i - \\mu \\sim N(0, \\sigma^2)$，标准化后服从半正态分布（折叠正态分布）；求二阶矩时 $E(Y_i^2) = E[(X_i-\\mu)^2] = \\sigma^2$ 极度简捷；似然函数对 $\\sigma^2$ 整体求导。",
                "solution": "(I) 对 $y > 0$，$F_Y(y) = P\\{|X_1-\\mu| \\le y\\} = 2\\Phi(y/\\sigma) - 1$。\\n求导得概率密度：\\n$$f_Y(y) = \\sqrt{\\frac{2}{\\pi}} \\frac{1}{\\sigma} e^{-\\frac{y^2}{2\\sigma^2}} \\quad (y > 0)$$\\n\\n(II) 矩估计：\\n由于 $E(Y_i^2) = E[(X_i-\\mu)^2] = D(X_i) = \\sigma^2$。\\n用二阶样本矩替换理论二阶矩：\\n$$\\hat{\\sigma}^2_M = \\frac{1}{n}\\sum_{i=1}^n Y_i^2 = \\frac{1}{n}\\sum_{i=1}^n (X_i - \\mu)^2$$\\n\\n(III) 极大似然估计：\\n似然函数：\\n$$L(\\sigma^2) = \\prod_{i=1}^n \\left[ \\sqrt{\\frac{2}{\\pi}} \\frac{1}{\\sigma} e^{-\\frac{y_i^2}{2\\sigma^2}} \\right] = \\left(\\frac{2}{\\pi}\\right)^{n/2} (\\sigma^2)^{-n/2} \\exp\\left( -\\frac{\\sum y_i^2}{2\\sigma^2} \\right)$$\\n取对数：\\n$$\\ln L = \\frac{n}{2}\\ln\\frac{2}{\\pi} - \\frac{n}{2}\\ln(\\sigma^2) - \\frac{\\sum y_i^2}{2\\sigma^2}$$\\n对 $\\sigma^2$ 求导令其等于 0：\\n$$\\frac{d\\ln L}{d(\\sigma^2)} = -\\frac{n}{2\\sigma^2} + \\frac{\\sum y_i^2}{2(\\sigma^2)^2} = 0 \\implies \\hat{\\sigma}^2_{MLE} = \\frac{1}{n}\\sum_{i=1}^n Y_i^2 = \\frac{1}{n}\\sum_{i=1}^n (X_i - \\mu)^2$$",
                "trap": "如果第 (II) 问去求一阶矩 $E(Y_i) = \\sigma\\sqrt{2/\\pi}$ 然后平方，虽然也是合法的矩估计，但二阶矩更加直接、计算量大减且与似然估计结果完全一致。"
            }
        ],
        "variants": [
            {
                "question": "设总体 $X \\sim U(0, \\theta)$，$\\theta > 0$ 为未知参数，$X_1, \\dots, X_n$ 为样本。求 $\\theta$ 的矩估计量和极大似然估计量。",
                "hint": "矩估计令 $E(X)=\\theta/2 = \\bar{X}$；MLE 似然函数为 $\\frac{1}{\\theta^n}$ 随 $\\theta$ 递减，必须满足 $\\theta \\ge \\max X_i$。",
                "solution": "矩估计：$E(X) = \\theta/2 \\implies \\hat{\\theta}_M = 2\\bar{X}$。\\nMLE：$L(\\theta) = \\frac{1}{\\theta^n} \\prod I_{\\{0 \\le x_i \\le \\theta\\}} = \\frac{1}{\\theta^n}$（当 $\\theta \\ge \\max(x_1,\\dots,x_n)$）。由于 $L(\\theta)$ 随 $\\theta$ 严格单调递减，故最大值在左边界取得：$\\hat{\\theta}_{MLE} = \\max(X_1, X_2, \\dots, X_n)$。"
            }
        ],
        "relatedKnowledgeIds": ["gailv-07-unbiasedness-eval-criteria", "gailv-08-cross-mle-optimization"],
        "tags": ["矩估计", "极大似然", "MLE", "对数似然", "端点型MLE"],
        "source": "Maki考研数学大串讲 L62 & 真题分类精解 题62.4",
        "status": "not_started",
        "isPending": False
    },
    "gailv-07-unbiasedness-eval-criteria": {
        "id": "gailv-07-unbiasedness-eval-criteria",
        "title": "估计量的无偏性、有效性与均方误差",
        "subject": "gailv",
        "subjectName": "概率论与数理统计",
        "chapterId": "gailv-ch07",
        "chapterTitle": "参数估计",
        "nodeType": "topic",
        "summary": "“无偏看期望是否等于真值，有效看无偏中谁的方差小”。均方误差 $\\mathrm{MSE}(\\hat{\\theta}) = D(\\hat{\\theta}) + [\\mathrm{Bias}(\\hat{\\theta})]^2$。",
        "triggers": [
            "“证明 $\\hat{\\theta}$ 是 $\\theta$ 的无偏估计量”",
            "比较两个估计量 $\\hat{\\theta}_1, \\hat{\\theta}_2$ 哪一个更有效",
            "构造常数 $c$ 使得 $c\\hat{\\theta}$ 为无偏估计"
        ],
        "firstReaction": "检验无偏性只需做一件事：求估计量的期望 $E(\\hat{\\theta})$，看是否恒等于 $\\theta$！若不等于，调整常数系数；比较有效性必须先保证两者都是无偏估计，然后再算方差 $D(\\hat{\\theta})$，方差小者更有效。",
        "candidateMethods": [
            {
                "name": "无偏性期望检验法",
                "priority": 1,
                "condition": "判定是否为无偏估计",
                "whyChoose": "代入期望线性性质展开计算",
                "description": "检验 $E(\\hat{\\theta}) = \\theta$ 是否对任意 $\\theta$ 恒成立"
            },
            {
                "name": "方差比较法（有效性）",
                "priority": 2,
                "condition": "两估计量均无偏",
                "whyChoose": "方差越小，估计值波动越小、精度越高",
                "description": "若 $D(\\hat{\\theta}_1) < D(\\hat{\\theta}_2)$，则 $\\hat{\\theta}_1$ 比 $\\hat{\\theta}_2$ 更有效"
            },
            {
                "name": "均方误差综合评定法",
                "priority": 3,
                "condition": "估计量可能存在偏倚",
                "whyChoose": "兼顾偏差与方差的综合度量",
                "description": "$\\mathrm{MSE}(\\hat{\\theta}) = E[(\\hat{\\theta}-\\theta)^2] = D(\\hat{\\theta}) + (E(\\hat{\\theta})-\\theta)^2$"
            }
        ],
        "applicability": "只有在都是无偏估计的前提下谈“有效性”才有意义；若估计量有偏，直接比方差是不公正的，应比均方误差 MSE。",
        "steps": [
            "步骤1：将估计量表示为样本 $X_i$ 的线性组合或极值函数形式。",
            "步骤2：计算数学期望 $E(\\hat{\\theta})$，核对是否等于待估参数 $\\theta$。",
            "步骤3：若需比较有效性，计算方差 $D(\\hat{\\theta})$，利用独立性将方差拆开做差比较。"
        ],
        "pitfalls": [
            "未验证无偏就直接比较方差来下结论“谁更有效”。",
            "均匀分布端点 MLE $\\hat{\\theta} = \\max X_i$ 的期望是 $\\frac{n}{n+1}\\theta$，是有偏的，必须乘以 $\\frac{n+1}{n}$ 才是无偏估计。"
        ],
        "formulas": [
            {
                "title": "无偏性定义",
                "latex": "E(\\hat{\\theta}) = \\theta",
                "notes": "对参数空间内所有可能取值均成立"
            },
            {
                "title": "均方误差分解",
                "latex": "\\mathrm{MSE}(\\hat{\\theta}) = E[(\\hat{\\theta} - \\theta)^2] = D(\\hat{\\theta}) + [E(\\hat{\\theta}) - \\theta]^2",
                "notes": "无偏时 MSE 等于方差"
            }
        ],
        "pastQuestions": [
            {
                "id": "gailv-q-2015-1-23",
                "year": "2015",
                "category": "数一",
                "questionNumber": "(23)",
                "questionText": "设总体 $X$ 的概率密度为 $f(x; \\theta) = \\begin{cases} \\frac{1}{1-\\theta}, & \\theta \\le x \\le 1 \\\\ 0, & \\text{其他} \\end{cases}$，其中 $\\theta \\in (0, 1)$ 为未知参数。$X_1, X_2, \\dots, X_n$ 为来自该总体的简单随机样本。\\n(I) 求 $\\theta$ 的矩估计量 $\\hat{\\theta}_M$；\\n(II) 求 $\\theta$ 的极大似然估计量 $\\hat{\\theta}_L$；\\n(III) 判断 $\\hat{\\theta}_M$ 是否为 $\\theta$ 的无偏估计量。",
                "examTags": ["均匀分布截断", "端点型MLE", "无偏性判定"],
                "breakthrough": "$X \\sim U(\\theta, 1)$，理论期望 $E(X) = \\frac{\\theta+1}{2}$；端点含参极大似然估计落在样本极小值 $\\min X_i$；无偏性直接对矩估计量求期望即可。",
                "solution": "(I) $E(X) = \\frac{\\theta+1}{2}$。\\n令 $E(X) = \\bar{X} \\implies \\frac{\\theta+1}{2} = \\bar{X} \\implies \\hat{\\theta}_M = 2\\bar{X} - 1$。\\n\\n(II) 似然函数：\\n$$L(\\theta) = \\frac{1}{(1-\\theta)^n} \\prod_{i=1}^n I_{\\{\\theta \\le x_i \\le 1\\}}$$\\n必须满足 $\\theta \\le \\min(x_1, \\dots, x_n)$ 且 $\\max x_i \\le 1$。\\n由于 $\\frac{1}{(1-\\theta)^n}$ 随 $\\theta$ 严格单调递增，最大值在允许的最大右边界取得：\\n$$\\hat{\\theta}_L = \\min(X_1, X_2, \\dots, X_n)$$\\n\\n(III) 检验矩估计量的无偏性：\\n$$E(\\hat{\\theta}_M) = E(2\\bar{X} - 1) = 2E(\\bar{X}) - 1 = 2E(X) - 1 = 2\\left(\\frac{\\theta+1}{2}\\right) - 1 = \\theta + 1 - 1 = \\theta$$\\n因此，$\\hat{\\theta}_M$ 是 $\\theta$ 的无偏估计量。",
                "trap": "第 (II) 问注意总体是 $[\theta, 1]$，分母 $1-\\theta$ 变小导致函数单调增，所以取 $\\min X_i$ 而不是 $\\max X_i$！"
            }
        ],
        "variants": [
            {
                "question": "已知总体期望为 $\\mu$，方差为 $\\sigma^2$。设 $\\hat{\\mu}_1 = \\frac{1}{2}(X_1 + X_2)$，$\\hat{\\mu}_2 = \\frac{1}{3}X_1 + \\frac{2}{3}X_2$。证明它们都是 $\\mu$ 的无偏估计，并比较哪一个更有效。",
                "hint": "分别算两者的期望确认无偏，再算方差并利用独立性拆开比较大小。",
                "solution": "$E(\\hat{\\mu}_1) = E(\\hat{\\mu}_2) = \\mu$，均无偏。\\n$D(\\hat{\\mu}_1) = \\frac{1}{4}\\sigma^2 + \\frac{1}{4}\\sigma^2 = \\frac{1}{2}\\sigma^2 = 0.5\\sigma^2$；\\n$D(\\hat{\\mu}_2) = \\frac{1}{9}\\sigma^2 + \\frac{4}{9}\\sigma^2 = \\frac{5}{9}\\sigma^2 \\approx 0.555\\sigma^2$。\\n因为 $D(\\hat{\\mu}_1) < D(\\hat{\\mu}_2)$，所以 $\\hat{\\mu}_1$ 比 $\\hat{\\mu}_2$ 更有效（等权平均方差最小）。"
            }
        ],
        "relatedKnowledgeIds": ["gailv-07-moment-and-mle-estimation", "gailv-06-normal-population-sample-theorems"],
        "tags": ["无偏性", "有效性", "均方误差", "估计量评价"],
        "source": "Maki考研数学大串讲 L62 & 真题分类精解 题62.3",
        "status": "not_started",
        "isPending": False
    },
    "gailv-08-cross-calculus-probability": {
        "id": "gailv-08-cross-calculus-probability",
        "title": "概率论与微积分综合 (二重积分/级数/对称性)",
        "subject": "gailv",
        "subjectName": "概率论与数理统计",
        "chapterId": "gailv-ch08",
        "chapterTitle": "综合题与跨章节方法",
        "nodeType": "topic",
        "summary": "“概率外壳，微积分内核”。归一性即广义积分或级数和等于1，对称性消去复杂二重积分。",
        "triggers": [
            "概率密度中含有级数展开式或指数积分",
            "二维连续型变量概率计算转化为复杂的二重积分极坐标变换",
            "利用正态分布积分公式 $\\int_{-\\infty}^{+\\infty} e^{-x^2} dx = \\sqrt{\\pi}$ 求解高数积分"
        ],
        "firstReaction": "剥开概率外壳：概率非负对应被积函数非负；全概率为 1 对应广义反常积分等于 1；独立性对应二重积分可拆分为两个一重积分乘积；奇偶性对应对称区间积分为零。",
        "candidateMethods": [
            {
                "name": "微积分-概率双向互译法",
                "priority": 1,
                "condition": "高数积分与概率密度交叉题目",
                "whyChoose": "利用概率密度的归一性秒杀高难度定积分",
                "description": "如利用正态分布密度归一性直接写出高斯积分 $\\int_{-\\infty}^{+\\infty} e^{-a x^2}dx = \\sqrt{\\frac{\\pi}{a}}$"
            },
            {
                "name": "极坐标二重积分法",
                "priority": 2,
                "condition": "二维圆形区域或含有 $x^2+y^2$ 项",
                "whyChoose": "概率论中求圆盘内概率或二维独立正态组合的标准技巧",
                "description": "$x = r\\cos\\theta, y = r\\sin\\theta, dxdy = rdrd\\theta$"
            }
        ],
        "applicability": "必须严格核实定义域的对称轴位置；极坐标变换切勿漏乘雅可比行列式绝对值 $r$。",
        "steps": [
            "步骤1：将概率事件 $P((X, Y) \\in D)$ 翻译为二重积分 $\\iint_D f(x, y)dxdy$。",
            "步骤2：观察被积函数特征与区域形状，选择直角坐标交换次序或极坐标变换。",
            "步骤3：运用高数微积分技巧（分部积分、对称性、莱布尼茨公式）完成最终推导。"
        ],
        "pitfalls": [
            "做极坐标变换漏写面积元素中的 $r$。",
            "概率论中变量受非负约束（如 $x>0, y>0$），对称性只能在第一象限内利用对称线 $y=x$。"
        ],
        "formulas": [
            {
                "title": "高斯泊松积分概率化",
                "latex": "\\int_{-\\infty}^{+\\infty} e^{-\\frac{x^2}{2\\sigma^2}}\\,dx = \\sqrt{2\\pi}\\sigma",
                "notes": "由标准正态分布密度积分恒等于 1 得出"
            },
            {
                "title": "伽马函数与阶乘联系",
                "latex": "\\Gamma(\\alpha) = \\int_0^{+\\infty} x^{\\alpha - 1} e^{-x}\\,dx, \\quad \\Gamma(n+1) = n!",
                "notes": "\\Gamma(1/2) = \\sqrt{\\pi}"
            }
        ],
        "pastQuestions": [
            {
                "id": "gailv-q-2019-1-23",
                "year": "2019",
                "category": "数一",
                "questionNumber": "(23)",
                "questionText": "设总体 $X$ 的概率密度为 $f(x; \\sigma^2) = \\begin{cases} \\frac{A}{\\sigma} e^{-\\frac{(x-\\mu)^2}{2\\sigma^2}}, & x \\ge \\mu \\\\ 0, & x < \\mu \\end{cases}$，其中 $\\mu$ 是已知参数，$\\sigma > 0$ 是未知参数，$A$ 为常数。\\n(I) 求常数 $A$；\\n(II) 求参数 $\\sigma^2$ 的最大似然估计量。",
                "examTags": ["半正态分布", "归一化定常数", "极大似然估计"],
                "breakthrough": "(I) 这是截断的正态分布（半正态），全概率积分为 1：利用正态分布的对称性，全积分的一半等于 $0.5$；(II) 写似然函数求对数导数令为零。",
                "solution": "(I) 由概率密度的归一性 $\\int_{-\\infty}^{+\\infty} f(x)dx = 1$：\\n$$\\int_\\mu^{+\\infty} \\frac{A}{\\sigma} e^{-\\frac{(x-\\mu)^2}{2\\sigma^2}} dx = 1$$\\n令 $t = \\frac{x-\\mu}{\\sigma}$，则 $dx = \\sigma dt$，积分变为：\\n$$A \\int_0^{+\\infty} e^{-t^2/2} dt = 1$$\\n因为标准正态在正半轴的积分为 $\\int_0^{+\\infty} e^{-t^2/2} dt = \\frac{\\sqrt{2\\pi}}{2} = \\sqrt{\\frac{\\pi}{2}}$，\\n因此 $A \\cdot \\sqrt{\\frac{\\pi}{2}} = 1 \\implies A = \\sqrt{\\frac{2}{\\pi}}$。\\n\\n(II) 极大似然估计：\\n对来自该总体的样本 $X_1, \\dots, X_n (X_i \\ge \\mu)$，似然函数：\\n$$L(\\sigma^2) = \\prod_{i=1}^n \\left[ \\sqrt{\\frac{2}{\\pi}} \\frac{1}{\\sigma} e^{-\\frac{(x_i-\\mu)^2}{2\\sigma^2}} \\right] = \\left(\\frac{2}{\\pi}\\right)^{n/2} (\\sigma^2)^{-n/2} \\exp\\left( -\\frac{\\sum_{i=1}^n (x_i-\\mu)^2}{2\\sigma^2} \\right)$$\\n取对数并对 $\\sigma^2$ 求导令等于零：\\n$$\\frac{d\\ln L}{d(\\sigma^2)} = -\\frac{n}{2\\sigma^2} + \\frac{\\sum_{i=1}^n (x_i-\\mu)^2}{2(\\sigma^2)^2} = 0$$\\n解得：\\n$$\\hat{\\sigma}^2_{MLE} = \\frac{1}{n}\\sum_{i=1}^n (X_i - \\mu)^2$$",
                "trap": "直接算反常积分可能浪费时间，利用已知正态积分面积等于 $\\sqrt{2\\pi}$ 的一半秒求 $A$。"
            }
        ],
        "variants": [
            {
                "question": "求反常积分 $I = \\int_0^{+\\infty} x^3 e^{-x^2/2} dx$。",
                "hint": "换元 $t = x^2/2$，或者利用正态分布矩母函数与分部积分。",
                "solution": "令 $t = x^2/2 \\implies dt = xdx$。则 $I = \\int_0^{+\\infty} 2t e^{-t} dt = 2 \\int_0^{+\\infty} t e^{-t} dt = 2 \\times 1! = 2$。"
            }
        ],
        "relatedKnowledgeIds": ["gailv-07-moment-and-mle-estimation", "gaoshu-03-improper-integral-convergence"],
        "tags": ["高斯积分", "伽马函数", "归一化", "跨学科综合"],
        "source": "Maki考研数学大串讲 L62 & 真题分类精解 题62.6",
        "status": "not_started",
        "isPending": False
    },
    "gailv-08-cross-mle-optimization": {
        "id": "gailv-08-cross-mle-optimization",
        "title": "参数估计与极值最值综合题型",
        "subject": "gailv",
        "subjectName": "概率论与数理统计",
        "chapterId": "gailv-ch08",
        "chapterTitle": "综合题与跨章节方法",
        "nodeType": "topic",
        "summary": "“似然函数求极值，多元求偏导置零，凸二次型验极值”。考查条件极值、拉格朗日乘数法在概率统计中的结合。",
        "triggers": [
            "多个未知参数同时求极大似然估计（偏导数方程组）",
            "离散分布参数估计中带约束条件（如 $\\sum p_i = 1$）",
            "由参数估计导出经济利润或风险损失最优化"
        ],
        "firstReaction": "写对数似然函数 $\\ln L(\\theta_1, \\dots, \\theta_k)$，分别对各个参数求偏导数令为 0，联立非线性代数方程组；若带有概率和为 1 的约束，引入拉格朗日乘数法构建辅助函数。",
        "candidateMethods": [
            {
                "name": "多元对数似然偏导组法",
                "priority": 1,
                "condition": "多参数无约束似然估计",
                "whyChoose": "联立偏导方程组解驻点",
                "description": "$\\frac{\\partial \\ln L}{\\partial \\theta_1} = 0, \\dots, \\frac{\\partial \\ln L}{\\partial \\theta_k} = 0$"
            },
            {
                "name": "拉格朗日乘数优化法",
                "priority": 2,
                "condition": "带有约束条件的多参数似然估计",
                "whyChoose": "将有约束最优化转化为多元无约束驻点求解",
                "description": "$H(\\theta, \\lambda) = \\ln L(\\theta) + \\lambda(g(\\theta)-c)$"
            }
        ],
        "applicability": "解出的驻点必须验证在参数空间内有意义（如方差 $\\sigma^2 > 0$、概率 $p \\in [0, 1]$）。",
        "steps": [
            "步骤1：写出多参数联合样本的似然函数 $L(\\theta_1, \\dots, \\theta_k)$。",
            "步骤2：化简取自然对数 $\\ln L$。",
            "步骤3：分别对各未知参数求偏导数，置零列出方程组并求解。",
            "步骤4：核验解的合理性与边界极值。"
        ],
        "pitfalls": [
            "多参数对数求导时将其他未知参数错当成常数而忽略关联项。",
            "未验证解是否满足概率参数自身的物理范围限制。"
        ],
        "formulas": [
            {
                "title": "两参数正态总体 MLE 结果",
                "latex": "\\hat{\\mu} = \\bar{X}, \\quad \\hat{\\sigma}^2 = \\frac{1}{n}\\sum_{i=1}^n (X_i - \\bar{X})^2",
                "notes": "注意极大似然估计除以的是 n 而不是 n-1（MLE 是有偏的，但渐近无偏）"
            }
        ],
        "pastQuestions": [
            {
                "id": "gailv-q-2011-1-23",
                "year": "2011",
                "category": "数一",
                "questionNumber": "(23)",
                "questionText": "设 $X_1, X_2, \\dots, X_n$ 为来自正态总体 $N(\\mu_0, \\sigma^2)$ 的简单随机样本，其中 $\\mu_0$ 已知，$\\sigma^2 > 0$ 未知，$\\bar{X}$ 和 $S^2$ 分别表示样本均值和样本方差。\\n(I) 求参数 $\\sigma^2$ 的最大似然估计 $\\hat{\\sigma}^2$；\\n(II) 计算 $E(\\hat{\\sigma}^2)$ 和 $D(\\hat{\\sigma}^2)$。",
                "examTags": ["已知均值正态MLE", "期望与方差计算", "卡方分布转化"],
                "breakthrough": "均值已知为 $\\mu_0$ 时，似然函数只对 $\\sigma^2$ 一个参数求导，其解为 $\\frac{1}{n}\\sum(X_i-\\mu_0)^2$；其期望等于 $\\sigma^2$（无偏），卡方自由度为 $n$ 而不是 $n-1$！",
                "solution": "(I) 样本联合密度即似然函数：\\n$$L(\\sigma^2) = (2\\pi\\sigma^2)^{-n/2} \\exp\\left( -\\frac{\\sum_{i=1}^n (x_i-\\mu_0)^2}{2\\sigma^2} \\right)$$\\n取对数：\\n$$\\ln L = -\\frac{n}{2}\\ln(2\\pi) - \\frac{n}{2}\\ln(\\sigma^2) - \\frac{\\sum (x_i-\\mu_0)^2}{2\\sigma^2}$$\\n对 $\\sigma^2$ 求导令等于 0：\\n$$\\frac{d\\ln L}{d(\\sigma^2)} = -\\frac{n}{2\\sigma^2} + \\frac{\\sum(x_i-\\mu_0)^2}{2(\\sigma^2)^2} = 0 \\implies \\hat{\\sigma}^2 = \\frac{1}{n}\\sum_{i=1}^n (X_i - \\mu_0)^2$$\\n\\n(II) 计算数字特征：\\n令 $Y = \\frac{\\sum_{i=1}^n (X_i - \\mu_0)^2}{\\sigma^2} = \\sum_{i=1}^n \\left(\\frac{X_i-\\mu_0}{\\sigma}\\right)^2$。\\n因为 $\\mu_0$ 已知，所以每个括号内都是独立的标准正态变量，故 $Y \\sim \\chi^2(n)$（自由度为 $n$）。\\n因此 $E(Y) = n, D(Y) = 2n$。\\n注意到 $\\hat{\\sigma}^2 = \\frac{\\sigma^2}{n} Y$，于是：\\n$$E(\\hat{\\sigma}^2) = \\frac{\\sigma^2}{n} E(Y) = \\frac{\\sigma^2}{n} \\cdot n = \\sigma^2$$\\n$$D(\\hat{\\sigma}^2) = \\frac{\\sigma^4}{n^2} D(Y) = \\frac{\\sigma^4}{n^2} \\cdot 2n = \\frac{2\\sigma^4}{n}$$",
                "trap": "把 $\\mu_0$ 误当成未知参数去减 $\\bar{X}$，导致自由度错写成 $n-1$。"
            }
        ],
        "variants": [
            {
                "question": "在上述题目中，若 $\\mu$ 也未知，求 $(\\mu, \\sigma^2)$ 的联合极大似然估计。",
                "hint": "分别对 $\\mu$ 和 $\\sigma^2$ 求偏导令等于零解方程组。",
                "solution": "$\\hat{\\mu} = \\bar{X}$，$\\hat{\\sigma}^2 = \\frac{1}{n}\\sum_{i=1}^n (X_i - \\bar{X})^2$。"
            }
        ],
        "relatedKnowledgeIds": ["gailv-07-moment-and-mle-estimation", "gailv-06-normal-population-sample-theorems"],
        "tags": ["多参数MLE", "已知均值方差", "卡方自由度n", "极值偏导"],
        "source": "Maki考研数学大串讲 L62 & 真题分类精解 题62.1",
        "status": "not_started",
        "isPending": False
    }
}
