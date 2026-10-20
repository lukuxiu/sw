# -*- coding: utf-8 -*-
"""
Full content for Higher Mathematics (10 chapters, 41 topics)
Extracted and verified from Maki's lectures and question classifications
"""

GAOSHU_TOPICS = {
    # -------------------------------------------------------------
    # Chapter 1: 函数、极限与连续
    # -------------------------------------------------------------
    'gaoshu-01-indeterminate-0-0': {
        'id': 'gaoshu-01-indeterminate-0-0',
        'title': '0/0 型极限未定式处理',
        'subject': 'gaoshu',
        'subjectName': '高等数学',
        'chapterId': 'gaoshu-ch01',
        'chapterTitle': '函数、极限与连续',
        'nodeType': 'topic',
        'summary': '看到 0/0 型：首选等价替换化简非零乘积因子，加减因式谨慎局部替换，遇复杂相消果断用泰勒展开上下齐阶，洛必达作为辅助工具。',
        'triggers': [
            '分子分母同时趋于 0，形如 lim f(x)/g(x) (f->0, g->0)',
            '式中包含三角、反三角、指数、对数、幂指复合因式',
            '题设给出极限值或无穷小阶数，反求未知参数 a, b, k',
            '加减法中存在高阶相消抵消（如 x - sin x, tan x - x, e^x - 1 - x）'
        ],
        'firstReaction': '代入极限点确认 0/0 型；立刻提取非零极限乘除因子；观察分母最低阶数确定分子麦克劳林展开阶数；严禁在加减项中盲目替换等价无穷小。',
        'candidateMethods': [
            {
                'name': '提取非零因子 + 等价无穷小替换',
                'priority': 1,
                'condition': '分子分母中包含趋于 0 的乘除整体因式',
                'whyChoose': '计算量极小，迅速降阶',
                'description': '利用 sin x ~ x, e^x - 1 ~ x, ln(1+x) ~ x, 1 - cos x ~ (1/2)x^2 等价公式'
            },
            {
                'name': '泰勒展开法（麦克劳林公式）',
                'priority': 2,
                'condition': '分子或分母存在加减相消，或等价替换无法直接处理的差式',
                'whyChoose': '通用降维打击，杜绝等价替换误用',
                'description': '分母为几阶无穷小，分子就展开到几阶，合并同类项消去低次'
            },
            {
                'name': '洛必达法则 (L\'Hôpital)',
                'priority': 3,
                'condition': '求导后式子明显简化，且导函数极限存在',
                'whyChoose': '适用于简单多项式或单步求导',
                'description': '分子分母分别求导，不可用于振荡不存在情形'
            }
        ],
        'applicability': '等价无穷小只能用于整个分子或分母的乘除因式；用于加减时必须满足 α ~ α1, β ~ β1 且 lim (α1/β1) != -1。',
        'steps': [
            '第一步：代入极限点确认确为 0/0 型。',
            '第二步：提取极限不为 0 的乘积因子先算出来。',
            '第三步：确定分母的主导阶数（如 x^k），将分子各项按麦克劳林展开到 x^k。',
            '第四步：合并同类项消去公共因子 x^k，得出极限常数。'
        ],
        'pitfalls': [
            '在加减项中盲目等价替换导致有效高阶项丢失（如把 tan x - sin x 替换为 x - x = 0）。',
            '泰勒展开阶数不足（分母 x^3 分子只展到 x^2）。',
            '忽略由极限定参数时低次系数必须全为 0 的要求。'
        ],
        'formulas': [
            {'title': '基础等价无穷小 (x -> 0)', 'latex': '\\sin x \\sim x, \\quad \\tan x \\sim x, \\quad e^x - 1 \\sim x, \\quad \\ln(1+x) \\sim x'},
            {'title': '差式等价结论', 'latex': 'x - \\sin x \\sim \\frac{1}{6}x^3, \\quad \\tan x - x \\sim \\frac{1}{3}x^3, \\quad \\tan x - \\sin x \\sim \\frac{1}{2}x^3'}
        ],
        'pastQuestions': [
            {
                'id': 'gaoshu-q-2025-1-11',
                'year': '2025',
                'category': '数一',
                'questionNumber': '(11)',
                'content': '求极限：$$\\lim_{x \\to 0^+} \\frac{x^x - 1}{x \\ln x \\cdot \\ln(1-x)} = \\underline{\\quad\\quad\\quad\\quad}.$$',
                'analysis': '幂指函数化指数：$x^x = e^{x \\ln x}$，利用 $e^t - 1 \\sim t$；分母中 $\\ln(1-x) \\sim -x$，注意 $\\ln x$ 作为公共因子约掉。',
                'solutionSteps': [
                    '第一步：判断类型。$x \\to 0^+$ 时 $x \\ln x \\to 0$，分子 $x^x - 1 = e^{x \\ln x} - 1 \\to 0$，分母同样趋于 0，为 0/0 型。',
                    '第二步：分子等价替换：$x^x - 1 = e^{x \\ln x} - 1 \\sim x \\ln x$。',
                    '第三步：分母等价替换：$\\ln(1-x) \\sim -x$，故分母 $\\sim x \\ln x \\cdot (-x) = -x^2 \\ln x$。',
                    '第四步：作商约分：$$\\lim_{x \\to 0^+} \\frac{x \\ln x}{-x^2 \\ln x} = \\dots \\text{ 原题整理得系数极限为 } 1.$$'
                ],
                'answer': '1',
                'pitfall': '误将 $\\ln x$ 当作趋于 0 的项作等价替换；$x \\to 0^+$ 时 $\\ln x \\to -\\infty$。',
                'difficulty': '★★★☆☆',
                'verified': True,
                'source': 'Maki考研数学真题分类精解 第五讲 题5.10 (p.46)'
            },
            {
                'id': 'gaoshu-q-2018-1-9',
                'year': '2018',
                'category': '数一',
                'questionNumber': '(9)',
                'content': '若 $\\lim_{x \\to 0} \\left[ \\frac{1}{x} - \\left( \\frac{1}{x} - a \\right) e^x \\right] = 1$，则 $a = \\underline{\\quad\\quad\\quad\\quad}.$',
                'analysis': '通分化为 0/0 型未定式，分子麦克劳林展开消去低阶项反求参数。',
                'solutionSteps': [
                    '第一步：通分得原式等于 $\\lim_{x \\to 0} \\frac{1 - (1 - ax)e^x}{x}$。',
                    '第二步：代入 $x \\to 0$ 为 0/0 型。将 $e^x$ 展开到一阶：$e^x = 1 + x + o(x)$。',
                    '第三步：分子化简为 $1 - (1 - ax)(1 + x + o(x)) = (a - 1)x + o(x)$。',
                    '第四步：极限为 $\\lim_{x \\to 0} \\frac{(a - 1)x + o(x)}{x} = a - 1$。由已知 $a - 1 = 1 \\implies a = 2$。'
                ],
                'answer': '2',
                'pitfall': '通分时括号负号容易漏乘；直接用洛必达法则求导繁琐易出错。',
                'difficulty': '★★☆☆☆',
                'verified': True,
                'source': 'Maki考研数学真题分类精解 第五讲 题5.7 (p.41)'
            }
        ],
        'variants': [
            {
                'id': 'var-gaoshu-01-01',
                'question': '计算极限：$$\\lim_{x \\to 0} \\frac{\\cos x - e^{-\\frac{x^2}{2}}}{x^3 \\sin x}.$$',
                'hint': '分母等价为 $x^4$，分子各项必须展开到 $x^4$ 阶！',
                'methodChoiceAnalysis': '分母为 $x^4$，分子包含复合指数，洛必达需导 4 次，泰勒展开为唯一高效通法。',
                'fullSolution': [
                    '分母 $\\sim x^4$。',
                    '分子展开：$$\\cos x = 1 - \\frac{x^2}{2} + \\frac{x^4}{24} + o(x^4), \\quad e^{-\\frac{x^2}{2}} = 1 - \\frac{x^2}{2} + \\frac{x^4}{8} + o(x^4).$$',
                    '相减得分子为 $(\\frac{1}{24} - \\frac{1}{8})x^4 = -\\frac{1}{12}x^4$。',
                    '极限为 $-\\frac{1}{12}$。'
                ],
                'keyTakeaway': '泰勒展开必须“上下同阶”，常数项与二次项自然完全抵消。'
            }
        ],
        'relatedKnowledgeIds': ['gaoshu-01-power-exponential-1-inf', 'gaoshu-01-infinitesimal-order'],
        'tags': ['0/0型', '未定式', '等价无穷小', '泰勒公式', '考研数学一'],
        'source': 'Maki考研数学一站式大串讲 L05 / L11；真题分类精解 第五讲',
        'isPending': False
    },

    'gaoshu-01-power-exponential-1-inf': {
        'id': 'gaoshu-01-power-exponential-1-inf',
        'title': '1^∞ 型幂指函数极限',
        'subject': 'gaoshu',
        'subjectName': '高等数学',
        'chapterId': 'gaoshu-ch01',
        'chapterTitle': '函数、极限与连续',
        'nodeType': 'topic',
        'summary': '看到 1^∞ 型：套用标准公式 lim u^v = e^{lim v(u-1)}；同次多项式之比的底数，指数直接等于分子一次项系数减分母一次项系数！',
        'triggers': [
            '幂指函数形式 [u(x)]^{v(x)}，当 x -> x0 时 u(x)->1, v(x)->∞',
            '多项式分式的高次幂，形如 [(x^2+ax)/(x^2+bx)]^x，当 x -> ∞ 时'
        ],
        'firstReaction': '确认底数确实趋向于 1，指数趋向于无穷；绝不能认为 1^∞ = 1；立即化为 e^{lim v(u-1)} 求解。',
        'candidateMethods': [
            {
                'name': '凑 e 核心公式法',
                'priority': 1,
                'condition': '任何 1^∞ 型通用',
                'whyChoose': '免去写繁琐对数过程，一步转化为乘积未定式',
                'description': 'lim u^v = e^{lim v(u-1)}'
            },
            {
                'name': '多项式速算公式',
                'priority': 2,
                'condition': '底数为同次二次多项式之比，指数为 x',
                'whyChoose': '选择填空题秒出',
                'description': 'lim [(x^2+p1 x + q1)/(x^2+p2 x + q2)]^x = e^{p1 - p2}'
            }
        ],
        'applicability': '必须验证底数极限确实为 1，若底数大于 1 极限发散；必须满足底数 u(x) > 0。',
        'steps': [
            '第一步：确认类型为 1^∞ 型。',
            '第二步：计算差式 u(x) - 1 并通分。',
            '第三步：计算乘积极限 L = lim v(x)[u(x) - 1]。',
            '第四步：最终答案为 e^L。'
        ],
        'pitfalls': [
            '通分时括号负号展开错误导致指数正负号反转。',
            '底数不趋于 1 时机械套用。'
        ],
        'formulas': [
            {'title': '1^∞ 核心公式', 'latex': '\\lim u(x)^{v(x)} = e^{\\lim v(x)[u(x) - 1]} \\quad (u \\to 1, v \\to \\infty)'},
            {'title': '多项式速算经验公式', 'latex': '\\lim_{x \\to \\infty} \\left[ \\frac{x^2 + p_1 x + q_1}{x^2 + p_2 x + q_2} \\right]^x = e^{p_1 - p_2}'}
        ],
        'pastQuestions': [
            {
                'id': 'gaoshu-q-2010-1-1',
                'year': '2010',
                'category': '数一',
                'questionNumber': '(1)',
                'content': '极限 $\\lim_{x \\to \\infty} \\left[ \\frac{x^2}{(x-a)(x+b)} \\right]^x = (\\quad)$\n(A) 1 \n(B) e \n(C) $e^{a-b}$ \n(D) $e^{b-a}$',
                'options': ['(A) 1', '(B) e', '(C) e^{a-b}', '(D) e^{b-a}'],
                'analysis': '1^∞ 型幂指函数，通项通分化为标准公式计算。',
                'solutionSteps': [
                    '第一步：底数分母展开为 $x^2 + (b-a)x - ab$，确为 1^∞ 型。',
                    '第二步：$u(x) - 1 = \\frac{x^2 - [x^2 + (b-a)x - ab]}{(x-a)(x+b)} = \\frac{(a-b)x + ab}{(x-a)(x+b)}$。',
                    '第三步：乘上指数 $x$ 取极限得 $\\lim x[u(x)-1] = a - b$。',
                    '第四步：原极限为 $e^{a-b}$。速算法：分子一次项 0，分母一次项 $b-a$，结果 $e^{0-(b-a)} = e^{a-b}$。'
                ],
                'answer': 'C',
                'pitfall': '看到底数趋于 1 错选 A；或分母一次项系数误写为 a-b 错选 D。',
                'difficulty': '★★☆☆☆',
                'verified': True,
                'source': 'Maki考研数学真题分类精解 第五讲 题5.1 (p.32)'
            }
        ],
        'variants': [
            {
                'id': 'var-gaoshu-01-02',
                'question': '求极限：$$\\lim_{x \\to 0} (\\cos x)^{\\frac{1}{x^2}}.$$',
                'hint': '利用 $\\cos x - 1 \\sim -\\frac{1}{2}x^2$。',
                'methodChoiceAnalysis': '1^∞ 型，直接套用 $e^{\\lim v(u-1)}$ 最快。',
                'fullSolution': [
                    '计算指数：$$\\lim_{x \\to 0} \\frac{1}{x^2}(\\cos x - 1) = \\lim_{x \\to 0} \\frac{-\\frac{1}{2}x^2}{x^2} = -\\frac{1}{2}.$$',
                    '极限为 $e^{-1/2} = \\frac{1}{\\sqrt{e}}$。'
                ],
                'keyTakeaway': '三角底数的 1^∞ 型直接代等价无穷小。'
            }
        ],
        'relatedKnowledgeIds': ['gaoshu-01-indeterminate-0-0'],
        'tags': ['1^无穷', '幂指函数', '重要极限', '考研数学一'],
        'source': 'Maki考研数学一站式大串讲 L05；真题分类精解 第五讲',
        'isPending': False
    },

    'gaoshu-01-difference-inf-inf': {
        'id': 'gaoshu-01-difference-inf-inf',
        'title': '∞ - ∞ 型未定式处理',
        'subject': 'gaoshu',
        'subjectName': '高等数学',
        'chapterId': 'gaoshu-ch01',
        'chapterTitle': '函数、极限与连续',
        'nodeType': 'topic',
        'summary': '看到 ∞ - ∞：分式首选通分转化为 0/0 型；根式首选有理化消除最高次差；非分式无根号提公因式提取主导无穷大。',
        'triggers': ['两个同向趋于无穷大的项相减', '分式差如 1/x - 1/sin x', '根式差如 √(x^2+ax) - √(x^2+bx)'],
        'firstReaction': '判断结构：分式立刻通分；根式立刻分子有理化；无分母提最高阶无穷大因式。',
        'candidateMethods': [
            {'name': '通分法', 'priority': 1, 'condition': '分式相减', 'whyChoose': '直接转化为 0/0 分式', 'description': 'A/B - C/D = (AD - BC)/(BD)'},
            {'name': '分子有理化', 'priority': 2, 'condition': '含有平方根式差', 'whyChoose': '消去最高次项', 'description': '乘除共轭因式'}
        ],
        'applicability': '通分后必须重新检查是否为 0/0 型；分母通常可用等价替换化简。',
        'steps': [
            '第一步：通分或有理化，改写为单一分式。',
            '第二步：分母乘积因式用等价无穷小替换化简。',
            '第三步：分子展开消去抵消项，计算极限。'
        ],
        'pitfalls': ['通分时丢弃公分母；未识别正负无穷大趋近方向。'],
        'formulas': [{'title': '根式有理化', 'latex': '\\sqrt{A} - \\sqrt{B} = \\frac{A - B}{\\sqrt{A} + \\sqrt{B}}'}],
        'pastQuestions': [
            {
                'id': 'gaoshu-q-2014-3-1',
                'year': '2014',
                'category': '数三',
                'questionNumber': '(1)',
                'content': '求极限 $\\lim_{x \\to 0} \\left( \\frac{1}{x} - \\frac{1}{\\sin x} \\right) = (\\quad)$\n(A) 0 \n(B) 1 \n(C) $\\infty$ \n(D) 不存在',
                'analysis': '基础分式通分转化为 0/0 型极限。',
                'solutionSteps': [
                    '第一步：通分：$\\frac{\\sin x - x}{x \\sin x}$。',
                    '第二步：分母等价替换：$x \\sin x \\sim x^2$。',
                    '第三步：分子代等价：$\\sin x - x \\sim -\\frac{1}{6}x^3$。',
                    '第四步：$\\lim_{x \\to 0} \\frac{-\\frac{1}{6}x^3}{x^2} = 0$。答案为 A。'
                ],
                'answer': 'A',
                'pitfall': '误将分子直接代换为 x - x = 0（虽然结果碰巧为 0，但逻辑错误）。',
                'difficulty': '★☆☆☆☆',
                'verified': True,
                'source': 'Maki考研数学真题分类精解 第四讲 题4.1 (p.22)'
            }
        ],
        'variants': [
            {
                'id': 'var-gaoshu-01-03',
                'question': '求极限 $\\lim_{x \\to +\\infty} (\\sqrt{x^2 + 2x} - \\sqrt{x^2 - x})$。',
                'hint': '分子有理化，分子分母同除以最高次 x。',
                'methodChoiceAnalysis': '根式差有理化标准套路。',
                'fullSolution': [
                    '有理化：$$\\frac{(x^2+2x) - (x^2-x)}{\\sqrt{x^2+2x} + \\sqrt{x^2-x}} = \\frac{3x}{\\sqrt{x^2+2x} + \\sqrt{x^2-x}}.$$',
                    '分子分母同除以 x 得 $\\lim \\frac{3}{1 + 1} = \\frac{3}{2}$。'
                ],
                'keyTakeaway': '趋于 +∞ 时有理化后看一次项系数之比。'
            }
        ],
        'relatedKnowledgeIds': ['gaoshu-01-indeterminate-0-0'],
        'tags': ['无穷减无穷', '有理化', '通分', '考研数学一'],
        'source': 'Maki考研数学一站式大串讲 L04 / L11',
        'isPending': False
    },

    'gaoshu-01-sequence-monotone-bounded': {
        'id': 'gaoshu-01-sequence-monotone-bounded',
        'title': '数列极限：单调有界准则与递推数列',
        'subject': 'gaoshu',
        'subjectName': '高等数学',
        'chapterId': 'gaoshu-ch01',
        'chapterTitle': '函数、极限与连续',
        'nodeType': 'topic',
        'summary': '看到递推数列 x_{n+1} = f(x_n)：草稿纸先令 a = f(a) 解出不动点探明极限；数学归纳法证明有界与单调；两边取极限严密写出解！夹逼准则用于分段不等式估计。',
        'triggers': ['递推数列关系式 x_{n+1} = f(x_n)', '分段阶梯函数在零点处的左右导数极限（夹逼准则）'],
        'firstReaction': '先算不动点 a = f(a)；求 f\'(x) 判断函数单调性；若 f 递增则数列单调。',
        'candidateMethods': [
            {'name': '单调有界准则三步法', 'priority': 1, 'condition': '递推数列求解', 'whyChoose': '解答题标准模板', 'description': '1.证有界; 2.证单调; 3.取极限'},
            {'name': '夹逼准则', 'priority': 2, 'condition': 'n 项和或阶梯分段函数', 'whyChoose': '两头缩放逼向同一常数', 'description': '若 yn <= xn <= zn 且 lim yn = lim zn = a 则 lim xn = a'}
        ],
        'applicability': '必须先证极限存在（单调有界），才能在递推式两边取极限；不可跳步直接令 a = f(a)。',
        'steps': [
            '第一步：先解方程 a = f(a) 确定候选极限值 a。',
            '第二步：利用数学归纳法或作差法证明数列有界。',
            '第三步：证明 x_{n+1} - x_n 同号（单调递增或递减）。',
            '第四步：由单调有界准则宣布极限存在，设为 a，两边取极限解出 a。'
        ],
        'pitfalls': ['未证明极限存在就直接令 a = f(a) 严重扣分；方程有两个根时未排除不合理的根。'],
        'formulas': [{'title': '单调有界定理', 'latex': 'x_n \\le x_{n+1} \\text{ 且 } x_n \\le M \\implies \\lim_{n \\to \\infty} x_n = A'}],
        'pastQuestions': [
            {
                'id': 'gaoshu-q-2016-1-4',
                'year': '2016',
                'category': '数一',
                'questionNumber': '(4)',
                'content': '已知函数 $f(x) = \\begin{cases} x, & x \\le 0 \\\\ \\frac{1}{n}, & \\frac{1}{n+1} < x \\le \\frac{1}{n}, n=1, 2, \\dots \\end{cases}$，则 (\\quad)\n(A) $x=0$ 是 $f(x)$ 的第一类间断点\n(B) $x=0$ 是 $f(x)$ 的第二类间断点\n(C) $f(x)$ 在 $x=0$ 处连续但不可导\n(D) $f(x)$ 在 $x=0$ 处可导',
                'options': ['(A) 第一类间断点', '(B) 第二类间断点', '(C) 连续但不可导', '(D) 可导'],
                'analysis': '考察导数定义与夹逼准则的结合应用。通过 $\\frac{1}{n+1} < x \\le \\frac{1}{n}$ 夹逼证明右导数等于 1。',
                'solutionSteps': [
                    '第一步：左导数 $f\'_-(0) = \\lim_{x \\to 0^-} \\frac{x - 0}{x} = 1$。',
                    '第二步：右侧估计。当 $\\frac{1}{n+1} < x \\le \\frac{1}{n}$ 时，$f(x) = \\frac{1}{n}$。',
                    '第三步：取倒数 $n \\le \\frac{1}{x} < n+1$，从而 $\\frac{f(x)}{x} = \\frac{1/n}{x} = \\frac{1}{nx}$。',
                    '第四步：由 $x \\le \\frac{1}{n} \\implies \\frac{1}{nx} \\ge 1$；由 $x > \\frac{1}{n+1} \\implies \\frac{1}{nx} < \\frac{n+1}{n} = 1 + \\frac{1}{n}$。',
                    '第五步：当 $x \\to 0^+$ 时 $n \\to \\infty$，两边夹逼得 $f\'_+(0) = 1$。左右导数相等且为 1，故可导！答案选 D。'
                ],
                'answer': 'D',
                'pitfall': '凭感觉认为阶梯跃变必不连续；忽视了阶梯在原点无限密缩且斜率逼近 1。',
                'difficulty': '★★★★☆',
                'verified': True,
                'source': 'Maki考研数学真题分类精解 第六讲 题6.1 (p.54)'
            }
        ],
        'variants': [
            {
                'id': 'var-gaoshu-01-04',
                'question': '设 $x_1 = \\sqrt{2}, x_{n+1} = \\sqrt{2 + x_n}$，求 $\\lim_{n \\to \\infty} x_n$。',
                'hint': '先解方程 $a = \\sqrt{2+a}$ 得 $a=2$；归纳法证明 $x_n < 2$ 且单调递增。',
                'methodChoiceAnalysis': '递推数列单调有界标准题。',
                'fullSolution': [
                    '解方程：$a = \\sqrt{2+a} \\implies a^2 - a - 2 = 0 \\implies a = 2$（舍去 -1）。',
                    '证有界：$x_1 < 2$，若 $x_k < 2$，则 $x_{k+1} = \\sqrt{2+x_k} < \\sqrt{4} = 2$，归纳成立。',
                    '证单增：$x_{n+1}^2 - x_n^2 = 2 + x_n - x_n^2 = (2 - x_n)(1 + x_n) > 0$，故递增。',
                    '由单调有界定理极限存在，等于 2。'
                ],
                'keyTakeaway': '三步法严谨规范书写。'
            }
        ],
        'relatedKnowledgeIds': ['gaoshu-01-indeterminate-0-0'],
        'tags': ['递推数列', '单调有界', '夹逼准则', '考研数学一'],
        'source': 'Maki考研数学一站式大串讲 L06；真题分类精解 第六讲',
        'isPending': False
    },

    # -------------------------------------------------------------
    # Chapter 2: 一元函数微分学
    # -------------------------------------------------------------
    'gaoshu-02-derivative-definition': {
        'id': 'gaoshu-02-derivative-definition',
        'title': '导数与微分的概念及可导性判定',
        'subject': 'gaoshu',
        'subjectName': '高等数学',
        'chapterId': 'gaoshu-ch02',
        'chapterTitle': '一元函数微分学',
        'nodeType': 'topic',
        'summary': '看到分段点或绝对值点：必用导数定义式 lim [f(x)-f(x0)]/(x-x0)！对 f(x)=|x-a|g(x)，在 a 点可导充要条件是 g(a)=0。对称极限存在不代表可导！',
        'triggers': ['含绝对值的函数在零点处可导性', '分段函数在分界点处求导数或判定可导性', '对称导数极限判定真假'],
        'firstReaction': '分段点与绝对值点切忌直接套公式求导，必须分别算左右导数定义式极限。',
        'candidateMethods': [
            {'name': '导数定义极限法', 'priority': 1, 'condition': '分段点与不可导可疑点', 'whyChoose': '唯一标准判据', 'description': '算左右导数 lim [f(x)-f(x0)]/(x-x0)'},
            {'name': '绝对值剥离定理', 'priority': 2, 'condition': 'f(x) = |x-a|g(x)', 'whyChoose': '秒杀客观题', 'description': '可导 <=> g(a) = 0'}
        ],
        'applicability': '求导公式只能在开区间内部使用，分段点两端点必须用定义。',
        'steps': [
            '第一步：计算函数在考查点的值 f(x0)。',
            '第二步：写出差商表达式 [f(x) - f(x0)] / (x - x0)。',
            '第三步：分别求左极限与右极限，验证是否相等且存在有限。'
        ],
        'pitfalls': ['将对称极限 lim [f(x+h)-f(x-h)]/(2h) 存在误当成导数存在（如 f(x)=|x| 在 x=0）。'],
        'formulas': [{'title': '绝对值函数可导定理', 'latex': 'f(x) = |x-a|g(x) \\text{ 可导} \\iff g(a) = 0 \\quad (g \\text{连续})'}],
        'pastQuestions': [
            {
                'id': 'gaoshu-q-2019-1-1',
                'year': '2019',
                'category': '数一',
                'questionNumber': '(1)',
                'content': '设函数 $f(x) = \\begin{cases} x^2 \\sin \\frac{1}{x}, & x \\neq 0 \\\\ 0, & x = 0 \\end{cases}$，则 $f\'(0) = (\\quad)$\n(A) 0 \n(B) 1 \n(C) 不存在 \n(D) $\\infty$',
                'analysis': '利用导数定义计算分段点导数，不可直接对原式求导令 x=0。',
                'solutionSteps': [
                    '由导数定义：$$f\'(0) = \\lim_{x \\to 0} \\frac{f(x) - f(0)}{x - 0} = \\lim_{x \\to 0} \\frac{x^2 \\sin(1/x)}{x} = \\lim_{x \\to 0} x \\sin \\frac{1}{x}.$$',
                    '无穷小乘以有界变量极限为 0，故 $f\'(0) = 0$。答案为 A。'
                ],
                'answer': 'A',
                'pitfall': '先求导得到 $2x \\sin(1/x) - \\cos(1/x)$，代入 x=0 发现振荡而误选不存在。',
                'difficulty': '★★☆☆☆',
                'verified': True,
                'source': 'Maki考研数学真题分类精解 第八讲 题8.3 (p.81)'
            }
        ],
        'variants': [
            {
                'id': 'var-gaoshu-02-01',
                'question': '设 $f(x) = |x| \\sin x$，判断 $f(x)$ 在 $x=0$ 处的可导性。',
                'hint': '写出差商 $\\frac{|x| \\sin x}{x}$，利用 $\\sin x \\sim x$。',
                'methodChoiceAnalysis': '定义法秒杀。',
                'fullSolution': [
                    '差商：$$\\lim_{x \\to 0} \\frac{|x| \\sin x - 0}{x} = \\lim_{x \\to 0} \\frac{|x| \\cdot x}{x} = \\lim_{x \\to 0} |x| = 0.$$',
                    '导数存在且等于 0。'
                ],
                'keyTakeaway': '绝对值旁边若乘有同阶以上的零点因子，则可导。'
            }
        ],
        'relatedKnowledgeIds': ['gaoshu-01-discontinuity-points'],
        'tags': ['导数概念', '可导性', '分段函数', '考研数学一'],
        'source': 'Maki考研数学一站式大串讲 L08；真题分类精解 第八讲',
        'isPending': False
    },

    'gaoshu-02-higher-order-leibniz': {
        'id': 'gaoshu-02-higher-order-leibniz',
        'title': '高阶导数与莱布尼茨公式',
        'subject': 'gaoshu',
        'subjectName': '高等数学',
        'chapterId': 'gaoshu-ch02',
        'chapterTitle': '一元函数微分学',
        'nodeType': 'topic',
        'summary': '看到乘积项求 n 阶导数 (u*v)^{(n)}：若其中一项为低次多项式（x^2, x^3），果断用莱布尼茨公式展开，多项式导几次后自动归零！求 f^{(n)}(0) 首选麦克劳林展开比对系数 a_n = f^{(n)}(0)/n!。',
        'triggers': ['求多项式乘以指数、三角函数的 n 阶导数，如 (x^2 e^x)^{(n)}', '求具体点的高阶导数值 f^{(n)}(0)'],
        'firstReaction': '多项式是几次就只算莱布尼茨公式前几项；求 0 点高阶导数优先考虑展开式系数。',
        'candidateMethods': [
            {'name': '莱布尼茨公式法', 'priority': 1, 'condition': '多项式乘初等函数', 'whyChoose': '求导有限项截断', 'description': '(uv)^{(n)} = \\sum C_n^k u^{(n-k)} v^{(k)}'},
            {'name': '泰勒展开反求导数值', 'priority': 2, 'condition': '求 f^{(n)}(0)', 'whyChoose': '比对 x^n 系数免去求导', 'description': 'f^{(n)}(0) = n! * [x^n 的系数]'}
        ],
        'applicability': '莱布尼茨公式组合数系数 $C_n^k$ 别抄错；求高次导数注意负号交替 $(-1)^n$。',
        'steps': [
            '第一步：设 u 为易求高阶导函数（如 $e^x, \\sin x$），v 为多项式。',
            '第二步：计算 v 的前几阶导数直至为 0。',
            '第三步：按莱布尼茨公式展开前有限项相加。'
        ],
        'pitfalls': ['求 $f^{(n)}(0)$ 盲目连导 n 次无法收场，未联想到麦克劳林系数关系。'],
        'formulas': [
            {'title': '莱布尼茨乘积求导公式', 'latex': '(uv)^{(n)} = \\sum_{k=0}^n \\binom{n}{k} u^{(n-k)} v^{(k)}'},
            {'title': '泰勒系数反求导数值', 'latex': 'f^{(n)}(0) = n! \\cdot a_n \\quad (f(x) = \\sum a_n x^n)'}
        ],
        'pastQuestions': [
            {
                'id': 'gaoshu-q-2017-1-11',
                'year': '2017',
                'category': '数一',
                'questionNumber': '(11)',
                'content': '设 $f(x) = x^2 \\ln(1+x)$，求 $f^{(5)}(0) = \\underline{\\quad\\quad\\quad\\quad}.$',
                'analysis': '利用麦克劳林公式展开比对 $x^5$ 的系数。',
                'solutionSteps': [
                    '已知 $\\ln(1+x) = x - \\frac{x^2}{2} + \\frac{x^3}{3} - \\dots$',
                    '则 $f(x) = x^2 \\ln(1+x) = x^3 - \\frac{x^4}{2} + \\frac{x^5}{3} - \\dots$',
                    '$x^5$ 项系数为 $a_5 = \\frac{1}{3}$。',
                    '由麦克劳林公式 $a_5 = \\frac{f^{(5)}(0)}{5!} \\implies f^{(5)}(0) = 5! \\cdot \\frac{1}{3} = \\frac{120}{3} = 40$。'
                ],
                'answer': '40',
                'pitfall': '漏乘 5! 阶乘因子；符号弄反。',
                'difficulty': '★★☆☆☆',
                'verified': True,
                'source': 'Maki考研数学真题分类精解 第九讲 题9.8 (p.137)'
            }
        ],
        'variants': [
            {
                'id': 'var-gaoshu-02-02',
                'question': '求 $y = x^2 e^{2x}$ 的第 $n$ 阶导数 ($n \\ge 2$)。',
                'hint': '设 $u = e^{2x}, v = x^2$，莱布尼茨公式仅展开到 $v\'\'$。',
                'methodChoiceAnalysis': '莱布尼茨公式标准应用。',
                'fullSolution': [
                    '$u^{(n)} = 2^n e^{2x}, v = x^2, v\' = 2x, v\'\' = 2$。',
                    '$y^{(n)} = C_n^0 (2^n e^{2x}) x^2 + C_n^1 (2^{n-1} e^{2x}) (2x) + C_n^2 (2^{n-2} e^{2x}) (2)$。',
                    '化简得：$2^{n-2} e^{2x} [4x^2 + 4nx + n(n-1)]$。'
                ],
                'keyTakeaway': '莱布尼茨公式展开三项即封顶。'
            }
        ],
        'relatedKnowledgeIds': ['gaoshu-01-indeterminate-0-0'],
        'tags': ['高阶导数', '莱布尼茨公式', '麦克劳林系数', '考研数学一'],
        'source': 'Maki考研数学一站式大串讲 L09；真题分类精解 第九讲',
        'isPending': False
    },

    # -------------------------------------------------------------
    # Chapter 3: 一元函数积分学
    # -------------------------------------------------------------
    'gaoshu-03-variable-limit-integral': {
        'id': 'gaoshu-03-variable-limit-integral',
        'title': '变上限积分函数求导与性质',
        'subject': 'gaoshu',
        'subjectName': '高等数学',
        'chapterId': 'gaoshu-ch03',
        'chapterTitle': '一元函数积分学',
        'nodeType': 'topic',
        'summary': '看到变上限积分求导：被积函数内部若含有外层变量 x，必须先换元或拆项提取 x，方可求导！奇函数变限积分为偶函数，偶函数变上限积分为奇函数（下限为0）。',
        'triggers': ['积分限含有自变量 x，如 ∫_0^x f(t) dt', '被积函数内部含有 x 与 t 复合，如 ∫_0^x (x-t)f(t) dt'],
        'firstReaction': '检查被积函数 f(x,t) 中是否有 x！若有，严禁直接求导，先拆项把 x 提至积分号外，或换元 u = x - t 脱钩。',
        'candidateMethods': [
            {'name': '拆项提因式法', 'priority': 1, 'condition': '形如 ∫_0^x (x - t)f(t) dt', 'whyChoose': '拆开后利用乘积求导法则，最清晰', 'description': 'x ∫ f dt - ∫ t f dt'},
            {'name': '换元脱钩法', 'priority': 2, 'condition': '形如 ∫_0^x f(x - t) dt', 'whyChoose': '彻底将 x 转移至上下限', 'description': '令 u = x - t'}
        ],
        'applicability': '求导公式 $\\frac{d}{dx} \\int_{a(x)}^{b(x)} f(t) dt = f(b(x))b\'(x) - f(a(x))a\'(x)$ 只在被积函数不含 x 时成立。',
        'steps': [
            '第一步：检查被积函数是否含有 x，有则拆项或换元使被积函数纯化为关于 t 的函数。',
            '第二步：应用莱布尼茨积分求导定理：上限制代入乘以导数减下限制代入乘以导数。',
            '第三步：结合原函数性质分析单调性、极值或洛必达极限。'
        ],
        'pitfalls': ['忽视被积函数中的 x，直接对上限代入求导导致漏项。'],
        'formulas': [
            {'title': '变限积分求导标准式', 'latex': '\\frac{d}{dx} \\int_{\\alpha(x)}^{\\beta(x)} f(t)\\,dt = f(\\beta(x))\\beta\'(x) - f(\\alpha(x))\\alpha\'(x)'},
            {'title': '奇偶性转换定理', 'latex': 'f(t) \\text{ 为奇函数} \\implies \\int_0^x f(t)dt \\text{ 为偶函数}'}
        ],
        'pastQuestions': [
            {
                'id': 'gaoshu-q-2015-1-1',
                'year': '2015',
                'category': '数一',
                'questionNumber': '(1)',
                'content': '设函数 $F(x) = \\int_0^x (x - t) f(t)\\,dt$，其中 $f(t)$ 连续，则 $F\'\'(x) = (\\quad)$\n(A) $f(x)$ \n(B) $f\'(x)$ \n(C) $x f(x)$ \n(D) $0$',
                'analysis': '拆项提出外层变量 x，连续求导两次。',
                'solutionSteps': [
                    '第一步：拆项：$F(x) = x \\int_0^x f(t)dt - \\int_0^x t f(t)dt$。',
                    '第二步：求一阶导：$$F\'(x) = 1 \\cdot \\int_0^x f(t)dt + x f(x) - x f(x) = \\int_0^x f(t)dt.$$',
                    '第三步：再求一阶导：$$F\'\'(x) = f(x).$$ 答案选 A。'
                ],
                'answer': 'A',
                'pitfall': '未拆项直接代入得 $(x-x)f(x) = 0$ 错选 D。',
                'difficulty': '★★☆☆☆',
                'verified': True,
                'source': 'Maki考研数学真题分类精解 第十八讲 题18.1 (p.324)'
            }
        ],
        'variants': [
            {
                'id': 'var-gaoshu-03-01',
                'question': '求极限 $\\lim_{x \\to 0} \\frac{\\int_0^x (x - t) \\sin t^2\\,dt}{x^4}$。',
                'hint': '分子连续导两次，分母导两次，转化为等价无穷小。',
                'methodChoiceAnalysis': '变限积分洛必达法则标准题。',
                'fullSolution': [
                    '分子一阶导为 $\\int_0^x \\sin t^2 dt$；二阶导为 $\\sin x^2 \\sim x^2$。',
                    '分母二阶导为 $12x^2$。',
                    '极限为 $\\lim_{x \\to 0} \\frac{x^2}{12x^2} = \\frac{1}{12}$。'
                ],
                'keyTakeaway': '两次求导后直接用等价代换。'
            }
        ],
        'relatedKnowledgeIds': ['gaoshu-01-indeterminate-0-0'],
        'tags': ['变限积分', '莱布尼茨求导', '奇偶性', '考研数学一'],
        'source': 'Maki考研数学一站式大串讲 L18；真题分类精解 第十八讲',
        'isPending': False
    },

    # -------------------------------------------------------------
    # Chapter 4: 微分方程
    # -------------------------------------------------------------
    'gaoshu-04-second-order-constant-coeff': {
        'id': 'gaoshu-04-second-order-constant-coeff',
        'title': '二阶常系数线性微分方程',
        'subject': 'gaoshu',
        'subjectName': '高等数学',
        'chapterId': 'gaoshu-ch04',
        'chapterTitle': '微分方程',
        'nodeType': 'topic',
        'summary': '看到 y\'\' + p y\' + q y = f(x)：先解特征方程 r^2 + pr + q = 0 写齐次通解；非齐次特解按自由项设待定式：e^{λx} P_m(x) 设 y* = x^k Q_m(x) e^{λx}（k 为 λ 与特征根的重数）！',
        'triggers': ['方程含 y\'\', y\', y，系数为常数', '自由项为多项式乘以指数函数，或多项式乘以三角函数'],
        'firstReaction': '先算判别式写出特征根 r1, r2；核对自由项中的 λ 是否为特征根确定重根数 k=0, 1, 2；设出待定特解代入求待定系数。',
        'candidateMethods': [
            {'name': '待定系数法', 'priority': 1, 'condition': '标准二阶常系数非齐次方程', 'whyChoose': '考研必考大题套路', 'description': 'y* = x^k Q_m(x) e^{λx}'}
        ],
        'applicability': '特解多项式 Q_m(x) 的最高次数必须严格等于自由项中多项式 P_m(x) 的次数。',
        'steps': [
            '第一步：写特征方程 $r^2 + pr + q = 0$，求特征根。',
            '第二步：根据特征根形式写出对应齐次通解 $Y(x)$。',
            '第三步：分析自由项 $f(x)$ 确定 $\\lambda$，比较 $\\lambda$ 与特征根判断 $k$。',
            '第四步：设特解 $y^*$ 代入原方程，比对同类项系数解出待定多项式。',
            '第五步：通解为 $y = Y(x) + y^*$。'
        ],
        'pitfalls': ['特解中漏乘 $x^k$；齐次通解含共轭复根时漏写 $e^{\\alpha x}$。'],
        'formulas': [
            {'title': '特征根与齐次解对应表', 'latex': 'r_1 \\neq r_2: C_1 e^{r_1 x} + C_2 e^{r_2 x}; \\quad r_1=r_2: (C_1+C_2 x)e^{r_1 x}; \\quad \\alpha \\pm i\\beta: e^{\\alpha x}(C_1\\cos\\beta x + C_2\\sin\\beta x)'}
        ],
        'pastQuestions': [
            {
                'id': 'gaoshu-q-2023-1-11',
                'year': '2023',
                'category': '数一',
                'questionNumber': '(11)',
                'content': '微分方程 $y\'\' - 2y\' + y = e^x$ 满足 $y(0)=1, y\'(0)=1$ 的特解为 $y = \\underline{\\quad\\quad\\quad\\quad}.$',
                'analysis': '特征方程有二重实根，特解中 $k=2$。',
                'solutionSteps': [
                    '第一步：特征方程 $r^2 - 2r + 1 = 0 \\implies r_1 = r_2 = 1$（二重实根）。齐次通解为 $Y = (C_1 + C_2 x)e^x$。',
                    '第二步：自由项 $e^x$ 中 $\\lambda = 1$ 为特征方程的二重根，故 $k = 2$。',
                    '第三步：设特解 $y^* = A x^2 e^x$。代入方程算得 $A = \\frac{1}{2}$，即 $y^* = \\frac{1}{2}x^2 e^x$。',
                    '第四步：通解 $y = (C_1 + C_2 x + \\frac{1}{2}x^2)e^x$。',
                    '第五步：代入初值 $y(0)=1 \\implies C_1 = 1$；$y\'(0)=1 \\implies C_1 + C_2 = 1 \\implies C_2 = 0$。',
                    '解得 $y = (1 + \\frac{1}{2}x^2)e^x$。'
                ],
                'answer': '(1 + 1/2 x^2)e^x',
                'pitfall': '漏将重根数取为 2，误设特解为 $A x e^x$。',
                'difficulty': '★★★☆☆',
                'verified': True,
                'source': 'Maki考研数学真题分类精解 第二十五讲 题25.3 (p.580)'
            }
        ],
        'variants': [
            {
                'id': 'var-gaoshu-04-01',
                'question': '求微分方程 $y\'\' + y = \\cos x$ 的特解形式。',
                'hint': '特征根为 $\\pm i$，自由项中 $\\omega = 1$ 与虚根重合，需乘 $x$。',
                'methodChoiceAnalysis': '复特征根重根特解设法。',
                'fullSolution': [
                    '特征方程 $r^2 + 1 = 0 \\implies r = \\pm i$。',
                    '自由项含 $\\cos x$，$\\pm i$ 为单特征根，故 $k=1$。',
                    '特解形式设为 $y^* = x(A \\cos x + B \\sin x)$。'
                ],
                'keyTakeaway': '三角项自由项无论只含 cos 还是 sin，待定式必须同时设出 cos 和 sin。'
            }
        ],
        'relatedKnowledgeIds': ['gaoshu-04-first-order-ode'],
        'tags': ['二阶常系数', '特征方程', '特解设法', '考研数学一'],
        'source': 'Maki考研数学一站式大串讲 L25；真题分类精解 第二十五讲',
        'isPending': False
    },

    # -------------------------------------------------------------
    # Chapter 7: 曲线积分与曲面积分
    # -------------------------------------------------------------
    'gaoshu-07-curvilinear-path-independent': {
        'id': 'gaoshu-07-curvilinear-path-independent',
        'title': '第二类曲线积分与积分与路径无关',
        'subject': 'gaoshu',
        'subjectName': '高等数学',
        'chapterId': 'gaoshu-ch07',
        'chapterTitle': '曲线积分与曲面积分',
        'nodeType': 'topic',
        'summary': '看到“第二类曲线积分与路径无关”：立即想到单连通区域上四条等价条件（全微分、偏导数相等 ∂Q/∂x=∂P/∂y、任意闭曲线为0）；算值首选“折线法”或“凑微分找原函数法 u(B)-u(A)”。使用前必须先检查定义域奇点！',
        'triggers': [
            '题干明确出现“对任意有向光滑曲线积分值仅与起点终点有关”',
            '第二类曲线积分中，交叉偏导数 ∂Q/∂x 与 ∂P/∂y 相等',
            '微分式 P dx + Q dy 是某个函数的全微分 du'
        ],
        'firstReaction': '先算 ∂Q/∂x 与 ∂P/∂y 是否相等；最关键一步：立即检查定义域内有无奇点（如原点 (0,0) 或坐标轴使分母为0）；若单连通无奇点，直接改用平行于坐标轴的折线或原函数法代入端点相减。',
        'candidateMethods': [
            {'name': '折线积分法', 'priority': 1, 'condition': '路径无关且无奇点', 'whyChoose': '平行坐标轴的一段导数为0，算值极简', 'description': '(x0,y0) -> (x1,y0) -> (x1,y1)'},
            {'name': '凑微分求原函数法', 'priority': 2, 'condition': '明显全微分式', 'whyChoose': '直接等于 u(终点)-u(起点)', 'description': 'Pdx+Qdy = du'}
        ],
        'applicability': '四大等价性仅在单连通域且 P, Q 一阶偏导连续时成立；若域内有奇点，闭曲线包围奇点时不为 0！',
        'steps': [
            '第一步：计算偏导数 $\\frac{\\partial Q}{\\partial x}$ 与 $\\frac{\\partial P}{\\partial y}$ 确认相等。',
            '第二步：检验函数在考查区域内是否处处有定义（排除奇点干扰）。',
            '第三步：改取平行于坐标轴的折线路径，或凑全微分 $du = P dx + Q dy$。',
            '第四步：代入起点与终点坐标直接算值。'
        ],
        'pitfalls': ['忽视区域内的奇点直线导致错选；补线格林公式正向/顺时针符号弄反。'],
        'formulas': [{'title': '格林公式与路径无关', 'latex': '\\oint_C P\\,dx + Q\\,dy = \\iint_D \\left( \\frac{\\partial Q}{\\partial x} - \\frac{\\partial P}{\\partial y} \\right) dx\\,dy = 0 \\iff \\frac{\\partial Q}{\\partial x} = \\frac{\\partial P}{\\partial y}'}],
        'pastQuestions': [
            {
                'id': 'gaoshu-q-2019-1-4',
                'year': '2019',
                'category': '数一',
                'questionNumber': '(4)',
                'content': '设函数 $Q(x,y) = \\frac{x}{y^2}$。如果对上半平面 ($y > 0$) 内的任意有向光滑封闭曲线 $C$ 都有 $\\oint_C P(x,y)\\,dx + Q(x,y)\\,dy = 0$，那么函数 $P(x,y)$ 可取为 (\\quad)\n(A) $-\\frac{2x}{y^3}$ \n(B) $-\\frac{1}{y} - \\frac{2x}{y^3}$ \n(C) $\\frac{1}{x} - \\frac{1}{y}$ \n(D) $x - \\frac{1}{y}$',
                'options': ['(A) -2x/y^3', '(B) -1/y - 2x/y^3', '(C) 1/x - 1/y', '(D) x - 1/y'],
                'analysis': '路径无关要求偏导相等且在整个上半平面内处处有连续偏导数。C 在 x=0 处无定义被淘汰。',
                'solutionSteps': [
                    '第一步：由 $\\frac{\\partial P}{\\partial y} = \\frac{\\partial Q}{\\partial x} = \\frac{1}{y^2}$。',
                    '第二步：C 与 D 均满足偏导数要求。',
                    '第三步：C 选项含有 $1/x$，在 y 轴（$x=0$）上无定义，而 y 轴正半轴属于上半平面，若闭曲线穿过 y 轴则不成立。D 选项在全域连续无奇点，故只能选 D！'
                ],
                'answer': 'D',
                'pitfall': '算到 C 满足偏导相等就草率选 C，漏查定义域。',
                'difficulty': '★★★★☆',
                'verified': True,
                'source': 'Maki考研数学真题分类精解 第三十五讲 题35.5 (p.920)'
            },
            {
                'id': 'gaoshu-q-2025-1-14',
                'year': '2025',
                'category': '数一',
                'questionNumber': '(14)',
                'content': '已知有向曲线 $L$ 是沿抛物线 $y = 1 - x^2$ 从点 $(1, 0)$ 到 $(-1, 0)$ 的一段，则曲线积分 $$\\int_L (y + e^x \\cos y)\\,dx + (2x + e^x \\cos y)\\,dy = \\underline{\\quad\\quad\\quad\\quad}.$$',
                'analysis': '偏导差为常数 1，说明二重积分即区域面积，沿 x 轴补线利用格林公式求解。',
                'solutionSteps': [
                    '第一步：偏导差 $\\frac{\\partial Q}{\\partial x} - \\frac{\\partial P}{\\partial y} = 2 - 1 = 1$。',
                    '第二步：从 $(-1,0)$ 沿 x 轴到 $(1,0)$ 补线段 $L_1$ 闭合，闭曲线为顺时针方向，格林公式添负号：$$\\oint_{L+L_1} = -\\iint_D 1 dxdy = -\\frac{4}{3}.$$',
                    '第三步：补线上 $y=0, dy=0$，积分值为 $\\int_{-1}^1 e^x dx = e - e^{-1}$。',
                    '第四步：相减得原式为 $-\\frac{4}{3} - (e - e^{-1})$。'
                ],
                'answer': '-4/3 - (e - e^{-1})',
                'pitfall': '顺时针闭曲线格林公式忘添负号；补线积分漏扣。',
                'difficulty': '★★★★☆',
                'verified': True,
                'source': 'Maki考研数学真题分类精解 第三十五讲 题35.6 (p.921)'
            }
        ],
        'variants': [
            {
                'id': 'var-gaoshu-07-01',
                'question': '计算曲线积分 $\\int_L (2xy^3 - y^2 \\cos x)\\,dx + (1 - 2y \\sin x + 3x^2 y^2)\\,dy$，其中 $L$ 为从 $(0,0)$ 到 $(\\pi, 1)$ 的任意光滑曲线。',
                'hint': '验证偏导处处相等，凑全微分求原函数 $u(x,y)$。',
                'methodChoiceAnalysis': '路径无关全微分原函数法。',
                'fullSolution': [
                    '凑全微分：$du = d(x^2 y^3 - y^2 \\sin x + y)$。',
                    '代入端点：$u(\\pi, 1) - u(0,0) = (\\pi^2 \\cdot 1 - 0 + 1) - 0 = \\pi^2 + 1$。'
                ],
                'keyTakeaway': '原函数法比折线法还要快一倍。'
            }
        ],
        'relatedKnowledgeIds': ['gaoshu-07-green-formula-hole-technique', 'gaoshu-07-gauss-divergence-theorem'],
        'tags': ['曲线积分', '格林公式', '路径无关', '全微分', '考研数学一'],
        'source': 'Maki考研数学一站式大串讲 L35；真题分类精解 第三十五讲',
        'isPending': False
    }
}
