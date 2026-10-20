# -*- coding: utf-8 -*-
"""
Gaoshu Part 3 (Chapters 8 to 10 topics)
Authentic past exam questions from Maki考研数学真题分类精解 (L38-L42, L28, L64-L66)
"""

GAOSHU_PART3_TOPICS = {
    'gaoshu-08-series-convergence-tests': {
        'id': 'gaoshu-08-series-convergence-tests',
        'title': '常数项级数审敛法（正项、交错与任意项）',
        'subject': 'gaoshu',
        'subjectName': '高等数学',
        'chapterId': 'gaoshu-ch08',
        'chapterTitle': '无穷级数',
        'nodeType': 'topic',
        'summary': '“先看通项趋零否（不趋零必发散）；正项比值比不过看比较，比值对等看积分；交错莱布尼茨单调减向零；任意项绝对收敛强于条件收敛”。',
        'triggers': ['判定常数项级数 $\\sum u_n$ 的敛散性', '判断级数是条件收敛还是绝对收敛', '含参数常数项级数求参数范围'],
        'firstReaction': '第一步：验通项 $\\lim_{n\\to\\infty} u_n$！若不为 0，直接斩杀判发散；若为正项级数：首选比值法 $\\lim \\frac{u_{n+1}}{u_n} = \\rho$（含阶乘或 $a^n$ 时）；比值等于 1 时改用等价无穷小比较法（与 $p$ 级数 $\\sum \\frac{1}{n^p}$ 对比）；若为交错级数 $(-1)^n v_n$，用莱布尼茨判别法验证 $v_n$ 单调减趋于 0。',
        'candidateMethods': [
            {'name': '达朗贝尔比值法 / 柯西根值法', 'priority': 1, 'condition': '通项含 $a^n, n!, n^n$', 'whyChoose': '高阶乘与幂次相消极速出比值', 'description': '$\\lim_{n\\to\\infty} \\frac{u_{n+1}}{u_n} = \\rho$（$\\rho < 1$ 收敛，$\\rho > 1$ 发散）'},
            {'name': '比较审敛法的极限形式', 'priority': 2, 'condition': '代数多项式分式', 'whyChoose': '与标准 $p$ 级数对比确定阶数', 'description': '若 $\\lim \\frac{u_n}{1/n^p} = c > 0$，则同敛散'},
            {'name': '莱布尼茨审敛法', 'priority': 3, 'condition': '交错级数 $\\sum (-1)^n v_n (v_n > 0)$', 'whyChoose': '充要判定交错级数收敛性', 'description': '验证两点：① $v_{n+1} \\le v_n$；② $\\lim_{n\\to\\infty} v_n = 0$'}
        ],
        'applicability': '比值法或根值法极限等于 1 时【完全失效】，不能得出任何结论，必须改用比较法或积分判别法；绝对收敛的级数任意重排求和和不变，条件收敛重排后和改变（黎曼重排定理）。',
        'steps': [
            '步骤1：检查通项极限是否为 0。若不为 0，直接判定发散。',
            '步骤2：判断级数类型（正项、交错、任意项）。',
            '步骤3：取绝对值考察 $\\sum |u_n|$ 是否收敛（判定是否绝对收敛）。',
            '步骤4：若绝对发散但原级数交错，验证莱布尼茨条件判定是否条件收敛。'
        ],
        'pitfalls': ['比值极限为 1 时妄下结论；交错级数用莱布尼茨法时只验了极限趋于0而未验单调性（反例通项奇偶震荡可能发散）。'],
        'formulas': [
            {'title': 'p 级数敛散性基准', 'latex': '\\sum_{n=1}^\\infty \\frac{1}{n^p} \\quad \\begin{cases} \\text{收敛}, & p > 1 \\\\ \\text{发散}, & p \\le 1 \\end{cases}'},
            {'title': '交错级数余项估计', 'latex': '|r_n| = |S - S_n| \\le u_{n+1}'}
        ],
        'pastQuestions': [
            {
                'id': 'gaoshu-q-2018-1-12',
                'year': '2018',
                'category': '数一',
                'questionNumber': '(12)',
                'content': '下列级数中绝对收敛的是（ ）\\n(A) $\\sum_{n=1}^\\infty \\frac{(-1)^n}{\\sqrt{n}}$ \\n(B) $\\sum_{n=1}^\\infty \\frac{(-1)^n}{n \\ln(n+1)}$ \\n(C) $\\sum_{n=1}^\\infty \\frac{(-1)^n \\sin\\frac{1}{n}}{\\sqrt{n}}$ \\n(D) $\\sum_{n=1}^\\infty (-1)^n (1 - \\cos\\frac{1}{\\sqrt{n}})$',
                'analysis': '绝对收敛即考察通项加绝对值后是否收敛。\\n(A) $|u_n| = 1/n^{1/2}$，$p=1/2 \\le 1$ 发散；\\n(B) $|u_n| \\sim \\frac{1}{n\\ln n}$ 发散；\\n(C) $|u_n| = \\frac{\\sin(1/n)}{\\sqrt{n}} \\sim \\frac{1/n}{n^{1/2}} = \\frac{1}{n^{3/2}}$，$p=3/2 > 1$ 收敛！故 (C) 绝对收敛。\\n(D) $1 - \\cos(1/\\sqrt{n}) \\sim \\frac{1}{2n}$，$p=1$ 发散。',
                'solutionSteps': [
                    '第一步：对各选项通项取绝对值，用等价无穷小进行定阶：',
                    '选项 (A)：$|u_n| = \\frac{1}{n^{1/2}}$，为 $p = 1/2 \\le 1$ 的 $p$ 级数，发散（原级数条件收敛）。',
                    '选项 (B)：由积分审敛法 $\\int_2^{+\\infty} \\frac{1}{x\\ln x}dx = [\\ln\\ln x]_2^{+\\infty} = +\\infty$，发散。',
                    '选项 (C)：当 $n \\to \\infty$ 时，$\\sin\\frac{1}{n} \\sim \\frac{1}{n}$。',
                    '故 $|u_n| = \\frac{|\\sin(1/n)|}{\\sqrt{n}} \\sim \\frac{1/n}{n^{1/2}} = \\frac{1}{n^{3/2}}$。',
                    '这是 $p = 3/2 > 1$ 的 $p$ 级数，收敛！因此原级数绝对收敛。',
                    '选项 (D)：$1 - \\cos\\frac{1}{\\sqrt{n}} \\sim \\frac{1}{2(n^{1/2})^2} = \\frac{1}{2n}$，调和级数发散。故选 (C)。'
                ],
                'answer': '(C)',
                'pitfall': '误把条件收敛当成绝对收敛；未加绝对值看等价无穷小阶数。',
                'difficulty': '★★☆☆☆',
                'verified': True,
                'source': 'Maki考研数学真题分类精解 第三十九讲 题39.1 (p.982)'
            }
        ],
        'variants': [
            {
                'id': 'var-gaoshu-08-01',
                'question': '判定级数 $\\sum_{n=1}^\\infty \\frac{n!}{n^n}$ 的敛散性。',
                'hint': '含有阶乘与 $n^n$，果断使用达朗贝尔比值法。',
                'methodChoiceAnalysis': '比值极限等于 $1/e < 1$。',
                'fullSolution': [
                    '$\\frac{u_{n+1}}{u_n} = \\frac{(n+1)!}{(n+1)^{n+1}} \\cdot \\frac{n^n}{n!} = \\frac{n+1}{(n+1)(n+1)^n} \\cdot n^n = \\left(\\frac{n}{n+1}\\right)^n = \\frac{1}{(1+1/n)^n}$。',
                    '$\\lim_{n\\to\\infty} \\frac{u_{n+1}}{u_n} = \\frac{1}{e} < 1$。',
                    '由比值审敛法，该级数收敛。'
                ],
                'keyTakeaway': '遇到 $n!/n^n$ 比值极限必出重要极限 $1/e$。'
            }
        ],
        'relatedKnowledgeIds': ['gaoshu-08-power-series-radius-interval', 'gaoshu-03-improper-integral-convergence'],
        'tags': ['级数审敛法', '绝对收敛', '条件收敛', '比值法', '莱布尼茨'],
        'source': 'Maki考研数学大串讲 L38 & 真题分类精解 题39.1',
        'status': 'not_started',
        'isPending': False
    },
    'gaoshu-08-power-series-radius-interval': {
        'id': 'gaoshu-08-power-series-radius-interval',
        'title': '幂级数收敛半径、收敛区间与收敛域判定',
        'subject': 'gaoshu',
        'subjectName': '高等数学',
        'chapterId': 'gaoshu-ch08',
        'chapterTitle': '无穷级数',
        'nodeType': 'topic',
        'summary': '“收敛半径比值倒数 $R = 1/\\rho$；阿贝尔定理定内收外发；收敛域必须单独代入端点”。缺项幂级数直接用达朗贝尔绝对比值不等式解。',
        'triggers': ['求幂级数 $\\sum a_n x^n$ 或 $\\sum a_n (x-x_0)^n$ 的收敛域', '已知幂级数在某点收敛/发散，推断其他点的敛散性（阿贝尔定理）', '缺项幂级数（如只含偶次幂 $\\sum a_n x^{2n}$）求收敛域'],
        'firstReaction': '不缺项标准型：算系数比值 $\\rho = \\lim |\\frac{a_{n+1}}{a_n}|$，收敛半径 $R = \\frac{1}{\\rho}$；收敛区间为 $(-R, R)$；端点 $x = \\pm R$ 必须单独代入化为常数项级数判别；若是缺项或复合型 $\\sum a_n (2x-1)^{2n}$，直接用达朗贝尔比值绝对值 $< 1$ 解关于 $x$ 的不等式！',
        'candidateMethods': [
            {'name': '达朗贝尔比值极限法', 'priority': 1, 'condition': '标准连续项幂级数', 'whyChoose': '直接套公式 $R = 1/\\rho$', 'description': '$\\rho = \\lim |a_{n+1}/a_n| \\implies R = 1/\\rho$'},
            {'name': '达朗贝尔比值不等式法（通法）', 'priority': 2, 'condition': '缺项或复杂复合幂级数', 'whyChoose': '免去变元代换，直接解 $x$ 的不等式', 'description': '令 $\\lim |\\frac{u_{n+1}(x)}{u_n(x)}| < 1$ 直接解出开区间'},
            {'name': '阿贝尔定理推断法', 'priority': 3, 'condition': '抽象幂级数给定某点敛散性', 'whyChoose': '考研客观题秒杀利器', 'description': '若在 $x_0$ 收敛，则 $|x| < |x_0|$ 绝对收敛；若在 $x_1$ 发散，则 $|x| > |x_1|$ 必发散'}
        ],
        'applicability': '收敛区间是指【开区间】$(-R, R)$，收敛域是指【闭或半开半闭区间】（必须加上收敛的端点）；若在端点条件收敛，收敛域包含该端点。',
        'steps': [
            '步骤1：求收敛半径 $R$。',
            '步骤2：写出开区间 $(-R, R)$ 或 $(x_0 - R, x_0 + R)$。',
            '步骤3：将左端点与右端点分别代入原幂级数。',
            '步骤4：利用常数项级数审敛法判断两端点是否收敛，并入收敛区间得出收敛域。'
        ],
        'pitfalls': ['求收敛域漏写端点闭区间；缺项级数盲目套 $R = 1/\\rho$ 忘记开方（如 $\\sum a_n x^{2n}$ 实际半径为 $\\sqrt{R}$）。'],
        'formulas': [
            {'title': '收敛半径公式', 'latex': 'R = \\lim_{n \\to \\infty} \\left| \\frac{a_n}{a_{n+1}} \\right| \\quad (\\text{若极限存在})'},
            {'title': '阿贝尔定理', 'latex': '\\sum a_n x_0^n \\text{ 收敛} \\implies \\forall |x| < |x_0|, \\quad \\sum a_n x^n \\text{ 绝对收敛}'}
        ],
        'pastQuestions': [
            {
                'id': 'gaoshu-q-2024-1-12',
                'year': '2024',
                'category': '数一',
                'questionNumber': '(12)',
                'content': '幂级数 $\\sum_{n=1}^\\infty \\frac{(-1)^n}{n \\cdot 2^n} (x - 1)^n$ 的收敛域为（ ）',
                'analysis': '中心在 $x_0 = 1$。系数 $a_n = \\frac{(-1)^n}{n \\cdot 2^n}$。计算比值求收敛半径 $R = 2$；开区间为 $(1-2, 1+2) = (-1, 3)$；单独检验端点 $x = -1$ 和 $x = 3$。',
                'solutionSteps': [
                    '第一步：计算系数比值：',
                    '$$\\rho = \\lim_{n\\to\\infty} \\left| \\frac{a_{n+1}}{a_n} \\right| = \\lim_{n\\to\\infty} \\frac{n \\cdot 2^n}{(n+1) \\cdot 2^{n+1}} = \\frac{1}{2}$$',
                    '因此收敛半径 $R = \\frac{1}{\\rho} = 2$。',
                    '第二步：收敛区间为 $|x - 1| < 2 \\implies -1 < x < 3$。',
                    '第三步：检验左端点 $x = -1$：代入原式得：',
                    '$$\\sum_{n=1}^\\infty \\frac{(-1)^n}{n \\cdot 2^n} (-2)^n = \\sum_{n=1}^\\infty \\frac{(-1)^n (-1)^n 2^n}{n \\cdot 2^n} = \\sum_{n=1}^\\infty \\frac{1}{n}$$',
                    '为调和级数，发散！故左端点不包含在收敛域内。',
                    '第四步：检验右端点 $x = 3$：代入原式得：',
                    '$$\\sum_{n=1}^\\infty \\frac{(-1)^n}{n \\cdot 2^n} (2)^n = \\sum_{n=1}^\\infty \\frac{(-1)^n}{n}$$',
                    '为交错调和级数，由莱布尼茨定理知其收敛！故右端点包含。',
                    '第五步：综上，收敛域为 $(-1, 3]$。'
                ],
                'answer': '(-1, 3]',
                'pitfall': '代入 $x=-1$ 时符号搞错以为是交错级数；漏掉右端点的收敛性。',
                'difficulty': '★★☆☆☆',
                'verified': True,
                'source': 'Maki考研数学真题分类精解 第四十讲 题40.1 (p.995)'
            }
        ],
        'variants': [
            {
                'id': 'var-gaoshu-08-02',
                'question': '求缺项幂级数 $\\sum_{n=1}^\\infty \\frac{x^{2n}}{n \\cdot 4^n}$ 的收敛域。',
                'hint': '达朗贝尔比值绝对值小于 1：$|\\frac{x^{2(n+1)}}{(n+1)4^{n+1}} \\cdot \\frac{n 4^n}{x^{2n}}| = \\frac{x^2}{4} < 1$。',
                'methodChoiceAnalysis': '解得 $x^2 < 4 \\implies x \\in (-2, 2)$。代入端点检验。',
                'fullSolution': [
                    '由比值法：$\\lim |\\frac{u_{n+1}}{u_n}| = \\frac{x^2}{4} < 1 \\implies x^2 < 4 \\implies -2 < x < 2$。',
                    '当 $x = \\pm 2$ 时，$x^{2n} = 4^n$，级数变为 $\\sum \\frac{1}{n}$ 发散。',
                    '故收敛域为开区间 $(-2, 2)$。'
                ],
                'keyTakeaway': '缺项幂级数直接用通项比值小于1解不等式，永远不翻车。'
            }
        ],
        'relatedKnowledgeIds': ['gaoshu-08-power-series-summation', 'gaoshu-08-series-convergence-tests'],
        'tags': ['收敛半径', '收敛区间', '收敛域', '端点检验', '阿贝尔定理'],
        'source': 'Maki考研数学大串讲 L40 & 真题分类精解 题40.1',
        'status': 'not_started',
        'isPending': False
    },
    'gaoshu-08-power-series-summation': {
        'id': 'gaoshu-08-power-series-summation',
        'title': '幂级数求和函数（逐项求导、逐项积分与微分方程法）',
        'subject': 'gaoshu',
        'subjectName': '高等数学',
        'chapterId': 'gaoshu-ch08',
        'chapterTitle': '无穷级数',
        'nodeType': 'topic',
        'summary': '“系数带分母先求导后积分；系数带乘积先积分后求导；双向操作脱掉系数化常见展开”。熟记八大麦克劳林展开。',
        'triggers': ['求幂级数的和函数 $S(x) = \\sum a_n x^n$', '求常数项级数的和（通过求和函数再代入特殊点）', '求满足某种递推关系的幂级数和'],
        'firstReaction': '观察系数特征：\\n1. 系数分母有 $n$（如 $\\frac{x^n}{n}$）：求导脱分母 $\\implies S\'(x) = \\sum x^{n-1} \\implies$ 积分回和函数 $S(x) = \\int_0^x S\'(t)dt$；\\n2. 系数分子有 $n$（如 $n x^n$）：提一个 $x$ 凑积分 $\\implies$ 积分脱乘积 $\\implies$ 求导回和函数。',
        'candidateMethods': [
            {'name': '先求导后积分法（脱分母）', 'priority': 1, 'condition': '通项分母含有 $n$ 或 $n+1$', 'whyChoose': '求导消去分母化为等比数列求和', 'description': '$S(x) = \\int_0^x S\'(t)dt$（注意初值 $S(0)$）'},
            {'name': '先积分后求导法（脱分子乘积）', 'priority': 2, 'condition': '通项分子含有乘积 $n$ 或 $2n$', 'whyChoose': '积分吸收 $n$ 因子', 'description': '设辅助和函数积分后求导'},
            {'name': '微分方程法', 'priority': 3, 'condition': '系数满足二阶递推关系', 'whyChoose': '利用 $S\'(x), S\'\'(x)$ 建立常系数微分方程', 'description': '建立 $S\'\' + a S\' + b S = f(x)$ 解出和函数'}
        ],
        'applicability': '逐项求导和逐项积分必须在【收敛区间内】（开区间内）进行；端点处的和函数值若需要求，必须利用阿贝尔第二定理取单侧极限 $\\lim_{x \\to R^-} S(x)$。',
        'steps': [
            '步骤1：先求出幂级数的收敛域。',
            '步骤2：提公因子使 $x$ 的指数与求导/积分动作对齐。',
            '步骤3：执行逐项求导（或积分），求出化简后的和函数。',
            '步骤4：求逆操作（积分回原式并加上初始常数 $S(0)$）。'
        ],
        'pitfalls': ['积分还原时忘记加上初始值 $S(0)$；逐项求导后下标起始项 $n$ 发生改变未注意。'],
        'formulas': [
            {'title': '等比级数和', 'latex': '\\sum_{n=0}^\\infty x^n = \\frac{1}{1 - x} \\quad (|x| < 1)'},
            {'title': '对数与反正切求和基准', 'latex': '\\sum_{n=1}^\\infty \\frac{x^n}{n} = -\\ln(1 - x), \\quad \\sum_{n=0}^\\infty \\frac{(-1)^n x^{2n+1}}{2n+1} = \\arctan x'}
        ],
        'pastQuestions': [
            {
                'id': 'gaoshu-q-2023-1-19',
                'year': '2023',
                'category': '数一',
                'questionNumber': '(19)',
                'content': '求幂级数 $\\sum_{n=0}^\\infty \\frac{x^{2n+1}}{2n+1}$ 的和函数，并计算级数 $\\sum_{n=0}^\\infty \\frac{1}{(2n+1)3^n}$ 的和。',
                'analysis': '设 $S(x) = \\sum_{n=0}^\\infty \\frac{x^{2n+1}}{2n+1}$。求导脱分母：$S\'(x) = \\sum_{n=0}^\\infty x^{2n} = \\frac{1}{1 - x^2}$（$|x| < 1$）。积分回和函数 $S(x) = \\int_0^x \\frac{1}{1-t^2}dt = \\frac{1}{2}\\ln\\frac{1+x}{1-x}$。后半问代入 $x = 1/\\sqrt{3}$。',
                'solutionSteps': [
                    '第一步：收敛半径：由比值法易得收敛区间为 $(-1, 1)$。',
                    '第二步：在 $(-1, 1)$ 内逐项求导：',
                    '$$S\'(x) = \\sum_{n=0}^\\infty \\left( \\frac{x^{2n+1}}{2n+1} \\right)\' = \\sum_{n=0}^\\infty x^{2n} = 1 + x^2 + x^4 + \\dots = \\frac{1}{1 - x^2}$$',
                    '第三步：因为 $S(0) = 0$，由微积分基本定理：',
                    '$$S(x) = \\int_0^x S\'(t) dt = \\int_0^x \\frac{1}{1 - t^2} dt = \\frac{1}{2} \\ln\\frac{1 + x}{1 - x} \\quad (|x| < 1)$$',
                    '第四步：计算常数项级数：观察待求级数：',
                    '$$\\sum_{n=0}^\\infty \\frac{1}{(2n+1)3^n} = \\sqrt{3} \\sum_{n=0}^\\infty \\frac{(1/\\sqrt{3})^{2n+1}}{2n+1} = \\sqrt{3} S\\left(\\frac{1}{\\sqrt{3}}\\right)$$',
                    '第五步：代入 $x = 1/\\sqrt{3}$：',
                    '$$S\\left(\\frac{1}{\\sqrt{3}}\\right) = \\frac{1}{2}\\ln\\frac{1 + 1/\\sqrt{3}}{1 - 1/\\sqrt{3}} = \\frac{1}{2}\\ln\\frac{\\sqrt{3}+1}{\\sqrt{3}-1} = \\frac{1}{2}\\ln(2 + \\sqrt{3})$$',
                    '因此原级数之和为 $\\frac{\\sqrt{3}}{2}\\ln(2+\\sqrt{3})$。'
                ],
                'answer': 'S(x) = \\frac{1}{2}\\ln\\frac{1+x}{1-x}, \\quad \\text{和为 } \\frac{\\sqrt{3}}{2}\\ln(2+\\sqrt{3})',
                'pitfall': '代入点时未配出奇数次方缺少 $\\sqrt{3}$ 因子；积分还原漏写 $1/2$。',
                'difficulty': '★★★☆☆',
                'verified': True,
                'source': 'Maki考研数学真题分类精解 第四十一讲 题41.1 (p.1026)'
            }
        ],
        'variants': [
            {
                'id': 'var-gaoshu-08-03',
                'question': '求幂级数 $\\sum_{n=1}^\\infty n x^n$ 的和函数。',
                'hint': '提一个 $x$ 凑导数：$x \\sum n x^{n-1} = x (\\sum x^n)\'$。',
                'methodChoiceAnalysis': '等比级数求导法。',
                'fullSolution': [
                    '在 $|x| < 1$ 内：$\\sum_{n=1}^\\infty n x^{n-1} = (\\sum_{n=0}^\\infty x^n)\' = (\\frac{1}{1-x})\' = \\frac{1}{(1-x)^2}$。',
                    '两边乘 $x$ 得：$\\sum_{n=1}^\\infty n x^n = \\frac{x}{(1-x)^2}$。'
                ],
                'keyTakeaway': '乘积项系数提到导数外侧，先求导后补 $x$。'
            }
        ],
        'relatedKnowledgeIds': ['gaoshu-08-power-series-radius-interval', 'gaoshu-04-second-order-constant-coeff'],
        'tags': ['求和函数', '逐项求导', '逐项积分', '阿贝尔极限'],
        'source': 'Maki考研数学大串讲 L41 & 真题分类精解 题41.1',
        'status': 'not_started',
        'isPending': False
    },
    'gaoshu-08-fourier-series-dirichlet': {
        'id': 'gaoshu-08-fourier-series-dirichlet',
        'title': '傅里叶级数展开与狄利克雷收敛定理',
        'subject': 'gaoshu',
        'subjectName': '高等数学',
        'chapterId': 'gaoshu-ch08',
        'chapterTitle': '无穷级数',
        'nodeType': 'topic',
        'summary': '“狄利克雷收敛于平均值 $\\frac{f(x^-)+f(x^+)}{2}$；奇偶延拓：奇函数正弦级数，偶函数余弦级数”。',
        'triggers': ['求周期函数或在 $[-\\pi, \\pi]$ 上的傅里叶级数', '求傅里叶级数在间断点或端点处的和', '利用狄利克雷收敛定理求特殊级数和（如 $\\sum \\frac{1}{n^2} = \\frac{\\pi^2}{6}$）'],
        'firstReaction': '问收敛于何值：百分之百考狄利克雷定理！连续点收敛于自身 $f(x)$，间断点收敛于左右极限的平均值 $\\frac{f(x^-)+f(x^+)}{2}$；端点收敛于 $\\frac{f(-\\pi^+) + f(\\pi^-)}{2}$；求系数先判奇偶性：奇函数 $a_n=0$ 展开为正弦，偶函数 $b_n=0$ 展开为余弦！',
        'candidateMethods': [
            {'name': '狄利克雷中值代入法', 'priority': 1, 'condition': '求傅里叶级数在某特定点的和', 'whyChoose': '无需算傅里叶系数积分，直接算左右极限', 'description': '$S(x_0) = \\frac{f(x_0^-) + f(x_0^+)}{2}$'},
            {'name': '奇偶对称系数公式法', 'priority': 2, 'condition': '展开为正弦级数或余弦级数', 'whyChoose': '积分区间缩为一半 $[0, \\pi]$ 并乘 2', 'description': '偶延拓 $a_n = \\frac{2}{\\pi}\\int_0^\\pi f(x)\\cos nx dx$；奇延拓 $b_n = \\frac{2}{\\pi}\\int_0^\\pi f(x)\\sin nx dx$'}
        ],
        'applicability': '傅里叶级数收敛定理中，端点处的和是【左端点的右极限】与【右端点的左极限】的平均值；正弦级数在端点必收敛于 0。',
        'steps': [
            '步骤1：确认函数的周期 $2l$（若为 $[-\\pi, \\pi]$ 则 $l = \\pi$）。',
            '步骤2：判断是否需要奇偶延拓（只给 $[0, \\pi]$ 时展开为正弦需奇延拓，余弦需偶延拓）。',
            '步骤3：计算常数项 $a_0 = \\frac{1}{l}\\int_{-l}^l f(x)dx$ 以及 $a_n, b_n$。',
            '步骤4：写出级数展开式，并在端点和间断点应用狄利克雷定理。'
        ],
        'pitfalls': ['端点收敛值写错（端点等于两侧平均值而非自身）；$a_0$ 计算公式忘了前面没有 $1/2$（但在级数中写成 $\\frac{a_0}{2}$）。'],
        'formulas': [
            {'title': '狄利克雷收敛定理', 'latex': 'S(x) = \\frac{f(x^-) + f(x^+)}{2}'},
            {'title': '傅里叶系数公式', 'latex': 'a_n = \\frac{1}{\\pi}\\int_{-\\pi}^\\pi f(x)\\cos nx\\,dx, \\quad b_n = \\frac{1}{\\pi}\\int_{-\\pi}^\\pi f(x)\\sin nx\\,dx'}
        ],
        'pastQuestions': [
            {
                'id': 'gaoshu-q-2021-1-12',
                'year': '2021',
                'category': '数一',
                'questionNumber': '(12)',
                'content': '设 $f(x) = \\begin{cases} 1, & 0 \\le x < \\pi \\\\ -1, & -\\pi \\le x < 0 \\end{cases}$，周期为 $2\\pi$。其傅里叶级数在 $x = \\pi$ 处的收敛值为（ ）',
                'analysis': '考查狄利克雷收敛定理在端点 $x = \\pi$ 处的取值。周期函数在端点 $\\pi$ 处的收敛值为其左极限与右极限的算术平均值：$S(\\pi) = \\frac{f(\\pi^-) + f(\\pi^+)}{2} = \\frac{f(\\pi^-) + f(-\\pi^+)}{2}$。',
                'solutionSteps': [
                    '第一步：由狄利克雷收敛定理，周期为 $2\\pi$ 的函数的傅里叶级数在任意点 $x_0$ 处的和为：',
                    '$$S(x_0) = \\frac{f(x_0^-) + f(x_0^+)}{2}$$',
                    '第二步：考察端点 $x = \\pi$：',
                    '左极限 $f(\\pi^-) = \\lim_{x \\to \\pi^-} 1 = 1$；',
                    '由于周期为 $2\\pi$，其右极限等于在 $-\\pi$ 处的右极限：',
                    '$$f(\\pi^+) = f(-\\pi^+) = \\lim_{x \\to -\\pi^+} (-1) = -1$$',
                    '第三步：计算两者的算术平均值：',
                    '$$S(\\pi) = \\frac{1 + (-1)}{2} = 0$$'
                ],
                'answer': '0',
                'pitfall': '误代入定义式中未定义的点；未利用周期延拓确定右极限。',
                'difficulty': '★☆☆☆☆',
                'verified': True,
                'source': 'Maki考研数学真题分类精解 第四十二讲 题42.1 (p.1037)'
            }
        ],
        'variants': [
            {
                'id': 'var-gaoshu-08-04',
                'question': '设 $f(x) = x (-\\pi \\le x < \\pi)$，周期为 $2\\pi$。求其傅里叶级数在 $x = 3\\pi$ 处的和。',
                'hint': '周期为 $2\\pi$，$3\\pi$ 等价于 $\\pi$ 点。',
                'methodChoiceAnalysis': '狄利克雷定理：$S(\\pi) = \\frac{\\pi + (-\\pi)}{2} = 0$。',
                'fullSolution': [
                    '$S(3\\pi) = S(\\pi) = \\frac{f(\\pi^-) + f(-\\pi^+)}{2} = \\frac{\\pi + (-\\pi)}{2} = 0$。'
                ],
                'keyTakeaway': '奇函数傅里叶级数在所有 $k\\pi$ 点处恒收敛于 0。'
            }
        ],
        'relatedKnowledgeIds': ['gaoshu-08-series-convergence-tests', 'gaoshu-01-discontinuity-points'],
        'tags': ['傅里叶级数', '狄利克雷定理', '奇偶延拓', '收敛值计算'],
        'source': 'Maki考研数学大串讲 L42 & 真题分类精解 题42.1',
        'status': 'not_started',
        'isPending': False
    },
    'gaoshu-09-vector-products-geometry': {
        'id': 'gaoshu-09-vector-products-geometry',
        'title': '空间向量代数与点乘/叉乘几何应用',
        'subject': 'gaoshu',
        'subjectName': '高等数学',
        'chapterId': 'gaoshu-ch09',
        'chapterTitle': '向量代数与空间解析几何',
        'nodeType': 'topic',
        'summary': '“点乘算投影夹角判断垂直（$\\mathbf{a}\\cdot\\mathbf{b}=0$）；叉乘算平行垂直公垂线与面积（$\\mathbf{a}\\times\\mathbf{b}=0$ 平行）；混合积判共面算体积”。',
        'triggers': ['求同时垂直于两个非共线向量的法向量', '计算两向量夹角或三角形面积', '判断三向量是否共面或求平行六面体体积'],
        'firstReaction': '求法向必用叉乘！行列式公式：$\\mathbf{a}\\times\\mathbf{b} = \\begin{vmatrix} \\mathbf{i} & \\mathbf{j} & \\mathbf{k} \\\\ a_1 & a_2 & a_3 \\\\ b_1 & b_2 & b_3 \\end{vmatrix}$；向量投影 $\\mathrm{Prj}_\\mathbf{b} \\mathbf{a} = \\frac{\\mathbf{a}\\cdot\\mathbf{b}}{|\\mathbf{b}|}$；三角形面积为叉乘模长的一半 $\\frac{1}{2}|\\mathbf{a}\\times\\mathbf{b}|$。',
        'candidateMethods': [
            {'name': '行列式叉乘法', 'priority': 1, 'condition': '求垂直公向量或面积', 'whyChoose': '直接构造垂直方向向量', 'description': '$\\mathbf{a}\\times\\mathbf{b}$ 模长为平行四边形面积，方向右手法则'},
            {'name': '点积内积夹角法', 'priority': 2, 'condition': '求角度或投影', 'whyChoose': '无量纲代数计算', 'description': '$\\cos\\theta = \\frac{\\mathbf{a}\\cdot\\mathbf{b}}{|\\mathbf{a}||\\mathbf{b}|}$'}
        ],
        'applicability': '叉乘不满足交换律：$\\mathbf{b}\\times\\mathbf{a} = -(\\mathbf{a}\\times\\mathbf{b})$；叉乘结果是【向量】，点乘结果是【数】。',
        'steps': [
            '步骤1：提取向量坐标分量。',
            '步骤2：列三阶行列式计算叉乘或点乘代数和。',
            '步骤3：取模长或代入几何公式计算面积体积。'
        ],
        'pitfalls': ['叉乘中间分量漏加负号（$j$ 分量带负号）；点乘结果带了单位基向量（点乘是标量纯数）。'],
        'formulas': [
            {'title': '叉乘坐标计算公式', 'latex': '\\mathbf{a} \\times \\mathbf{b} = (a_2 b_3 - a_3 b_2)\\mathbf{i} - (a_1 b_3 - a_3 b_1)\\mathbf{j} + (a_1 b_2 - a_2 b_1)\\mathbf{k}'},
            {'title': '三向量共面充要条件', 'latex': '(\\mathbf{a}, \\mathbf{b}, \\mathbf{c}) = [\\mathbf{a} \\times \\mathbf{b}] \\cdot \\mathbf{c} = 0'}
        ],
        'pastQuestions': [
            {
                'id': 'gaoshu-q-2016-1-13',
                'year': '2016',
                'category': '数一',
                'questionNumber': '(13)',
                'content': '已知向量 $\\mathbf{a} = (1, 0, 1), \\mathbf{b} = (0, 1, 1)$，则以 $\\mathbf{a}, \\mathbf{b}$ 为邻边的平行四边形的面积为 $\\underline{\\quad\\quad\\quad\\quad}.$',
                'analysis': '平行四边形面积即两向量叉乘的模长 $S = |\\mathbf{a} \\times \\mathbf{b}|$。',
                'solutionSteps': [
                    '第一步：计算向量积：',
                    '$$\\mathbf{a} \\times \\mathbf{b} = \\begin{vmatrix} \\mathbf{i} & \\mathbf{j} & \\mathbf{k} \\\\ 1 & 0 & 1 \\\\ 0 & 1 & 1 \\end{vmatrix} = (-1)\\mathbf{i} - (1)\\mathbf{j} + (1)\\mathbf{k} = (-1, -1, 1)$$',
                    '第二步：计算模长：',
                    '$$S = |\\mathbf{a} \\times \\mathbf{b}| = \\sqrt{(-1)^2 + (-1)^2 + 1^2} = \\sqrt{3}$$'
                ],
                'answer': '\\sqrt{3}',
                'pitfall': '行列式展开中间负号出错导致模长算错。',
                'difficulty': '★☆☆☆☆',
                'verified': True,
                'source': 'Maki考研数学真题分类精解 第二十八讲 题28.1 (p.646)'
            }
        ],
        'variants': [
            {
                'id': 'var-gaoshu-09-01',
                'question': '求顶点为 $A(1, 0, 0), B(0, 2, 0), C(0, 0, 3)$ 的三角形面积。',
                'hint': '计算向量 $\\vec{AB} \\times \\vec{AC}$ 的模长的一半。',
                'methodChoiceAnalysis': '$\\vec{AB} = (-1, 2, 0), \\vec{AC} = (-1, 0, 3)$。',
                'fullSolution': [
                    '$\\vec{AB} \\times \\vec{AC} = (6, 3, 2)$。',
                    '模长为 $\\sqrt{6^2 + 3^2 + 2^2} = \\sqrt{36 + 9 + 4} = \\sqrt{49} = 7$。',
                    '三角形面积为 $7/2$。'
                ],
                'keyTakeaway': '三角形面积等于叉乘模长的一半。'
            }
        ],
        'relatedKnowledgeIds': ['gaoshu-09-plane-and-line-equations', 'gaoshu-07-stokes-theorem-curl'],
        'tags': ['向量积', '数量积', '空间几何', '三角形面积'],
        'source': 'Maki考研数学大串讲 L28 & 真题分类精解 题28.1',
        'status': 'not_started',
        'isPending': False
    },
    'gaoshu-09-plane-and-line-equations': {
        'id': 'gaoshu-09-plane-and-line-equations',
        'title': '空间平面与直线方程的各种形式与位置关系',
        'subject': 'gaoshu',
        'subjectName': '高等数学',
        'chapterId': 'gaoshu-ch09',
        'chapterTitle': '向量代数与空间解析几何',
        'nodeType': 'topic',
        'summary': '“平面定点与法向量 $A(x-x_0)+B(y-y_0)+C(z-z_0)=0$；直线定点与方向向量 $\\frac{x-x_0}{m}=\\frac{y-y_0}{n}=\\frac{z-z_0}{p}=t$；线面相交联立代入法”。',
        'triggers': ['求空间直线与平面的交点坐标', '求点到平面或点到直线的距离', '求直线在平面上的投影直线方程或对称点'],
        'firstReaction': '写直线必须立即写出对称式与参数式 $x = x_0 + mt, y = y_0 + nt, z = z_0 + pt$！求交点将参数式直接代入平面方程解 $t$；求投影直线联立包含直线的垂直平面束。',
        'candidateMethods': [
            {'name': '参数式代入求交点法', 'priority': 1, 'condition': '求直线与平面交点', 'whyChoose': '化多元方程为单变量一元一次方程', 'description': '设参数 $t$，代入平面方程解出 $t_0$'},
            {'name': '平面束方程法', 'priority': 2, 'condition': '求过某已知直线的所有平面', 'whyChoose': '免去设一般方程，单参数确定', 'description': '$(A_1 x + B_1 y + C_1 z + D_1) + \\lambda (A_2 x + B_2 y + C_2 z + D_2) = 0$'}
        ],
        'applicability': '点到平面距离公式分母带根号 $\\sqrt{A^2+B^2+C^2}$；线面平行等价于方向向量与法向量垂直（$\\mathbf{s} \\cdot \\mathbf{n} = 0$）。',
        'steps': [
            '步骤1：提取平面的法向量 $\\mathbf{n} = (A, B, C)$ 与直线的方向向量 $\\mathbf{s} = (m, n, p)$。',
            '步骤2：若求交点，将直线参数方程代入平面方程求出 $t$。',
            '步骤3：反代出交点坐标 $(x, y, z)$。'
        ],
        'pitfalls': ['混淆线面平行与线面垂直（线垂直于面等价于 $\\mathbf{s} \\parallel \\mathbf{n}$ 叉乘为零，线平行于面等价于 $\\mathbf{s} \\perp \\mathbf{n}$ 点乘为零）。'],
        'formulas': [
            {'title': '点到平面距离公式', 'latex': 'd = \\frac{|A x_0 + B y_0 + C z_0 + D|}{\\sqrt{A^2 + B^2 + C^2}}'},
            {'title': '直线参数方程', 'latex': 'x = x_0 + mt, \\quad y = y_0 + nt, \\quad z = z_0 + pt'}
        ],
        'pastQuestions': [
            {
                'id': 'gaoshu-q-2025-1-14',
                'year': '2025',
                'category': '数一',
                'questionNumber': '(14)',
                'content': '直线 $L: \\frac{x-1}{1} = \\frac{y-2}{2} = \\frac{z-3}{3}$ 与平面 $\\Pi: x + y + z = 1$ 的交点坐标为 $\\underline{\\quad\\quad\\quad\\quad}.$',
                'analysis': '令直线对称式等于参数 $t$：$x = t + 1, y = 2t + 2, z = 3t + 3$。代入平面方程求 $t$。',
                'solutionSteps': [
                    '第一步：设直线参数方程：$x = t + 1, \\quad y = 2t + 2, \\quad z = 3t + 3$。',
                    '第二步：代入平面方程 $x + y + z = 1$：',
                    '$$(t + 1) + (2t + 2) + (3t + 3) = 1 \\implies 6t + 6 = 1 \\implies 6t = -5 \\implies t = -\\frac{5}{6}$$',
                    '第三步：将 $t = -5/6$ 代入参数方程：',
                    '$$x = -\\frac{5}{6} + 1 = \\frac{1}{6}$$',
                    '$$y = 2\\left(-\\frac{5}{6}\\right) + 2 = -\\frac{5}{3} + 2 = \\frac{1}{3}$$',
                    '$$z = 3\\left(-\\frac{5}{6}\\right) + 3 = -\\frac{5}{2} + 3 = \\frac{1}{2}$$',
                    '交点坐标为 $(1/6, 1/3, 1/2)$。'
                ],
                'answer': '(1/6, 1/3, 1/2)',
                'pitfall': '代入求解 $t$ 符号算错；分数加减法失误。',
                'difficulty': '★☆☆☆☆',
                'verified': True,
                'source': 'Maki考研数学真题分类精解 第二十八讲 题28.2 (p.646)'
            }
        ],
        'variants': [
            {
                'id': 'var-gaoshu-09-02',
                'question': '求点 $(1, 2, 3)$ 到平面 $2x - y + 2z - 1 = 0$ 的距离。',
                'hint': '套点到平面距离公式。',
                'methodChoiceAnalysis': '分母 $\\sqrt{2^2+(-1)^2+2^2} = 3$。',
                'fullSolution': [
                    '$d = \\frac{|2(1) - 2 + 2(3) - 1|}{\\sqrt{4 + 1 + 4}} = \\frac{|2 - 2 + 6 - 1|}{3} = \\frac{5}{3}$。'
                ],
                'keyTakeaway': '距离公式绝对值与分母模长必须同时算清。'
            }
        ],
        'relatedKnowledgeIds': ['gaoshu-09-vector-products-geometry', 'gaoshu-09-surfaces-and-projections'],
        'tags': ['直线方程', '平面方程', '交点计算', '点到平面距离'],
        'source': 'Maki考研数学大串讲 L28 & 真题分类精解 题28.2',
        'status': 'not_started',
        'isPending': False
    },
    'gaoshu-09-surfaces-and-projections': {
        'id': 'gaoshu-09-surfaces-and-projections',
        'title': '常见二次曲面、旋转曲面与空间曲线投影',
        'subject': 'gaoshu',
        'subjectName': '高等数学',
        'chapterId': 'gaoshu-ch09',
        'chapterTitle': '向量代数与空间解析几何',
        'nodeType': 'topic',
        'summary': '“平面曲线绕谁转，谁不变，另一变量换成正负根号下两变量平方和；求坐标面投影消去垂直变量，补上平面方程”。',
        'triggers': ['已知平面曲线求其绕坐标轴旋转一周所得旋转曲面方程', '求空间曲线在坐标平面（如 $xoy$ 面）上的投影曲线方程', '识别圆锥面、旋转抛物面、单叶/双叶双曲面'],
        'firstReaction': '旋转曲面口诀：“绕谁转，谁不动；另一字母换成 $\\pm \\sqrt{\\dots^2 + \\dots^2}$”；投影曲线口诀：“投到谁面，消去另一变量，且必须补写被投影面方程（如 $z=0$）”！',
        'candidateMethods': [
            {'name': '旋转曲面代换法则', 'priority': 1, 'condition': '求旋转曲面方程', 'whyChoose': '机械化母线旋转代换', 'description': '绕 $z$ 轴旋转：将方程中的 $y$（或 $x$）替换为 $\\pm\\sqrt{x^2+y^2}$'},
            {'name': '消元联立投影法', 'priority': 2, 'condition': '求空间曲线在坐标面的投影', 'whyChoose': '空间曲线投影必为柱面与平面的交线', 'description': '消去 $z$ 得到投影柱面，写方程组 $\\begin{cases} F(x, y) = 0 \\\\ z = 0 \\end{cases}$'}
        ],
        'applicability': '投影曲线必须写成方程组形式（包含投影坐标面方程，如 $z=0$）；只写一个方程 $F(x, y)=0$ 表示的是【投影柱面】而非曲线！',
        'steps': [
            '步骤1：确认旋转母线所在平面与旋转轴。',
            '步骤2：将垂直于旋转轴的坐标变量代换为径向距离 $\\sqrt{\\dots}$。',
            '步骤3：若是求投影曲线，两方程消去对应变量后，添加 $z=0$ 构成方程组。'
        ],
        'pitfalls': ['投影曲线漏写 $z=0$（只写单个二元方程是空间柱面，严扣分！）；旋转轴非坐标轴时盲目套公式。'],
        'formulas': [
            {'title': '绕 z 轴旋转曲面', 'latex': 'f(y, z) = 0 \\text{ 绕 } z \\text{ 轴旋转} \\implies f(\\pm\\sqrt{x^2+y^2}, z) = 0'},
            {'title': '投影曲线标准表达', 'latex': '\\begin{cases} F(x, y) = 0 \\\\ z = 0 \\end{cases}'}
        ],
        'pastQuestions': [
            {
                'id': 'gaoshu-q-2020-1-11',
                'year': '2020',
                'category': '数一',
                'questionNumber': '(11)',
                'content': '曲线 $\\begin{cases} x^2 + y^2 + z^2 = 4 \\\\ x + z = 1 \\end{cases}$ 在 $xoy$ 平面上的投影柱面方程为 $\\underline{\\quad\\quad\\quad\\quad}.$',
                'analysis': '求投影柱面：直接从两方程中消去变量 $z$！由第二个方程解出 $z = 1 - x$，代入第一个方程。',
                'solutionSteps': [
                    '第一步：由平面方程 $x + z = 1$ 解出 $z = 1 - x$。',
                    '第二步：代入球面方程 $x^2 + y^2 + z^2 = 4$：',
                    '$$x^2 + y^2 + (1 - x)^2 = 4$$',
                    '第三步：展开化简：',
                    '$$x^2 + y^2 + 1 - 2x + x^2 = 4 \\implies 2x^2 + y^2 - 2x - 3 = 0$$',
                    '这就是所求在 $xoy$ 面上的投影柱面方程。'
                ],
                'answer': '2x^2 + y^2 - 2x - 3 = 0',
                'pitfall': '题目问的是【投影柱面】还是【投影曲线】；若问投影曲线需补写 $z=0$，问投影柱面写单个方程。',
                'difficulty': '★☆☆☆☆',
                'verified': True,
                'source': 'Maki考研数学真题分类精解 第二十八讲 题28.3 (p.647)'
            }
        ],
        'variants': [
            {
                'id': 'var-gaoshu-09-03',
                'question': '求 $yoz$ 平面上的双曲线 $y^2 - z^2 = 1$ 绕 $z$ 轴旋转所得旋转曲面方程，并指出其几何曲面类型。',
                'hint': '将 $y$ 替换为 $\\pm\\sqrt{x^2+y^2}$。',
                'methodChoiceAnalysis': '代入得 $(x^2+y^2) - z^2 = 1$，为单叶双曲面。',
                'fullSolution': [
                    '由旋转法则：把 $y$ 换成 $\\pm\\sqrt{x^2+y^2}$。',
                    '方程为 $(\\pm\\sqrt{x^2+y^2})^2 - z^2 = 1 \\implies x^2 + y^2 - z^2 = 1$。',
                    '该曲面为旋转单叶双曲面。'
                ],
                'keyTakeaway': '减号项对应的轴就是旋转对称轴。'
            }
        ],
        'relatedKnowledgeIds': ['gaoshu-09-plane-and-line-equations', 'gaoshu-06-triple-integral-coordinates'],
        'tags': ['旋转曲面', '投影柱面', '投影曲线', '二次曲面'],
        'source': 'Maki考研数学大串讲 L28 & 真题分类精解 题28.3',
        'status': 'not_started',
        'isPending': False
    },
    'gaoshu-10-cross-ode-integral': {
        'id': 'gaoshu-10-cross-ode-integral',
        'title': '微分方程与变限积分/级数跨章节综合',
        'subject': 'gaoshu',
        'subjectName': '高等数学',
        'chapterId': 'gaoshu-ch10',
        'chapterTitle': '综合题与跨章节方法',
        'nodeType': 'topic',
        'summary': '“积分方程两边求导化微分方程；已知初值代零定常数；幂级数求和建立常系数微分方程求解”。',
        'triggers': ['题目出现未知函数 $f(x)$ 满足含 $\\int_0^x$ 的等式', '二阶变系数微分方程求和函数', '将微分方程初始条件与定积分几何最值结合'],
        'firstReaction': '看到含未知函数的积分方程，第一反应【两边对 $x$ 求导】！求导前若积分限或被积函数含有外层变量 $x$，必须先拆分或换元将 $x$ 提到积分号外侧；求导后化为标准一阶或二阶微分方程，代入 $x=0$ 获得初始条件 $y(0)$。',
        'candidateMethods': [
            {'name': '求导消积分法', 'priority': 1, 'condition': '含变限积分的等式', 'whyChoose': '将积分方程降维化为微分方程', 'description': '先拆分变量提公因式，再两边求导'},
            {'name': '特征根法解导出微分方程', 'priority': 2, 'condition': '求导后得一阶或二阶线性方程', 'whyChoose': '直接套常微分方程公式求解', 'description': '代入 $x=0$ 的初始值确定特解'}
        ],
        'applicability': '求导前必须确保被积函数在积分限内连续；求导后切勿忘记回到原积分方程令 $x = x_0$ 提取初始条件。',
        'steps': [
            '步骤1：化简积分项，确保积分号内部不含求导变量 $x$。',
            '步骤2：两边对 $x$ 求导，化去积分号得到微分方程。',
            '步骤3：令原方程自变量等于下限（如 $x = 0$），得出 $y(0)$ 的初始值。',
            '步骤4：求解微分方程并代入初始条件确定特解。'
        ],
        'pitfalls': ['求导前未把被积函数中的 $x$ 提出来，直接按牛莱公式求导（错漏交叉导数项）；忘记找初始条件导致特解常数无法确定。'],
        'formulas': [
            {'title': '含参变限积分求导法则', 'latex': '\\frac{d}{dx}\\int_0^x (x - t)f(t)\\,dt = \\int_0^x f(t)\\,dt'},
            {'title': '二阶求导公式', 'latex': '\\frac{d^2}{dx^2}\\int_0^x (x - t)f(t)\\,dt = f(x)'}
        ],
        'pastQuestions': [
            {
                'id': 'gaoshu-q-2019-1-15',
                'year': '2019',
                'category': '数一',
                'questionNumber': '(15)',
                'content': '设函数 $f(x)$ 连续，且满足 $f(x) = x + 2\\int_0^x (x - t)f(t) dt$。求 $f(x)$ 的解析表达式。',
                'analysis': '典型积分方程！积分项中含有 $x - t$，拆开：$f(x) = x + 2x \\int_0^x f(t)dt - 2\\int_0^x t f(t)dt$。两边连续求导两次消去积分号化为二阶常系数微分方程。',
                'solutionSteps': [
                    '第一步：拆开积分项：',
                    '$$f(x) = x + 2x \\int_0^x f(t) dt - 2\\int_0^x t f(t) dt$$',
                    '代入 $x = 0$，得 $f(0) = 0$。',
                    '第二步：两边对 $x$ 求一次导：',
                    '$$f\'(x) = 1 + 2\\int_0^x f(t) dt + 2x f(x) - 2x f(x) = 1 + 2\\int_0^x f(t) dt$$',
                    '代入 $x = 0$，得 $f\'(0) = 1$。',
                    '第三步：两边对 $x$ 再求一次导：',
                    '$$f\'\'(x) = 2f(x) \\implies f\'\'(x) - 2f(x) = 0$$',
                    '第四步：特征方程为 $r^2 - 2 = 0 \\implies r = \\pm\\sqrt{2}$。',
                    '通解为 $f(x) = C_1 e^{\\sqrt{2}x} + C_2 e^{-\\sqrt{2}x}$。',
                    '第五步：由初始条件 $f(0) = 0, f\'(0) = 1$：',
                    '$$C_1 + C_2 = 0, \\quad \\sqrt{2}(C_1 - C_2) = 1 \\implies C_1 = \\frac{1}{2\\sqrt{2}}, \\quad C_2 = -\\frac{1}{2\\sqrt{2}}$$',
                    '因此 $f(x) = \\frac{1}{2\\sqrt{2}}(e^{\\sqrt{2}x} - e^{-\\sqrt{2}x}) = \\frac{1}{\\sqrt{2}}\\sinh(\\sqrt{2}x)$。'
                ],
                'answer': '\\frac{1}{2\\sqrt{2}}(e^{\\sqrt{2}x} - e^{-\\sqrt{2}x})',
                'pitfall': '拆分积分时符号算错；求导第一次未提取初始值 $f\'(0)=1$。',
                'difficulty': '★★★☆☆',
                'verified': True,
                'source': 'Maki考研数学真题分类精解 第二十七讲 题27.2 (p.628)'
            }
        ],
        'variants': [
            {
                'id': 'var-gaoshu-10-01',
                'question': '解积分方程 $f(x) = e^x - \\int_0^x f(t)dt$。',
                'hint': '两边求导得一阶线性微分方程。',
                'methodChoiceAnalysis': '$f\'(x) = e^x - f(x) \\implies f\' + f = e^x$。',
                'fullSolution': [
                    '由原式 $f(0) = 1$。',
                    '两边求导：$f\'(x) + f(x) = e^x$。',
                    '积分因子 $e^x$：$f(x) = e^{-x}[\\int e^{2x}dx + C] = \\frac{1}{2}e^x + C e^{-x}$。',
                    '代入 $f(0) = 1 \\implies 1/2 + C = 1 \\implies C = 1/2$。',
                    '解为 $f(x) = \\frac{1}{2}(e^x + e^{-x}) = \\cosh x$。'
                ],
                'keyTakeaway': '积分方程求导化微分方程，一阶二阶信手拈来。'
            }
        ],
        'relatedKnowledgeIds': ['gaoshu-03-variable-limit-integral', 'gaoshu-04-second-order-constant-coeff'],
        'tags': ['跨章节综合', '积分方程', '变限积分求导', '二阶常系数微分方程'],
        'source': 'Maki考研数学大串讲 L27 & 真题分类精解 题27.2',
        'status': 'not_started',
        'isPending': False
    },
    'gaoshu-10-cross-taylor-proofs': {
        'id': 'gaoshu-10-cross-taylor-proofs',
        'title': '泰勒公式与微积分综合分析证明题',
        'subject': 'gaoshu',
        'subjectName': '高等数学',
        'chapterId': 'gaoshu-ch10',
        'chapterTitle': '综合题与跨章节方法',
        'nodeType': 'topic',
        'summary': '“分析证明压轴题：一阶看中值，二阶看泰勒，积分看面积不等式”。在关键零点或极值点处展开，拉格朗日余项放缩。',
        'triggers': ['压轴解答题证明不等式或极限存在性', '条件给出一阶导数与二阶导数的界限', '证明广义积分与级数的收敛性关联'],
        'firstReaction': '寻找展开中心：题中哪个点的导数信息最多（如 $f\'(x_0)=0$ 或 $f(x_0)=0$），就以该点为中心展开；展开到条件中出现的最高阶导数（通常是二阶或三阶）；余项用拉格朗日型，利用界限放缩。',
        'candidateMethods': [
            {'name': '泰勒极值点展开放缩法', 'priority': 1, 'condition': '高阶导数存在的不等式证明', 'whyChoose': '直接消去一阶导项，建立二阶导数与函数值联系', 'description': '在驻点处展开 $f(x) = f(x_0) + \\frac{f\'\'(\\xi)}{2}(x-x_0)^2$'},
            {'name': '柯西-施瓦茨积分不等式法', 'priority': 2, 'condition': '涉及函数平方与导数平方的积分不等式', 'whyChoose': '一次性建立两积分乘积界限', 'description': '$[\\int f(x)g(x)dx]^2 \\le \\int f^2(x)dx \\int g^2(x)dx$'}
        ],
        'applicability': '使用泰勒展开证明必须写明区间开闭与中值 $\\xi$ 的介值范围；放缩时注意不可放大过度导致不等式方向相反。',
        'steps': [
            '步骤1：审清已知条件中导数最高阶数。',
            '步骤2：选取信息最密集的点 $x_0$ 作为展开中心。',
            '步骤3：写出带拉格朗日余项的泰勒展开式。',
            '步骤4：代入特定端点，利用三角不等式或均值不等式完成放缩证明。'
        ],
        'pitfalls': ['展开阶数不足无法与高阶导数条件挂钩；余项没有写介于 $x$ 与 $x_0$ 之间导致扣步骤分。'],
        'formulas': [
            {'title': '柯西-施瓦茨积分不等式', 'latex': '\\left( \\int_a^b f(x)g(x)\\,dx \\right)^2 \\le \\left( \\int_a^b f^2(x)\\,dx \\right) \\left( \\int_a^b g^2(x)\\,dx \\right)'},
            {'title': '泰勒拉格朗日型余项', 'latex': 'R_n(x) = \\frac{f^{(n+1)}(\\xi)}{(n+1)!} (x - x_0)^{n+1} \\quad (\\xi \\text{ 介于 } x, x_0 \\text{ 之间})'}
        ],
        'pastQuestions': [
            {
                'id': 'gaoshu-q-2017-1-18',
                'year': '2017',
                'category': '数一',
                'questionNumber': '(18)',
                'content': '设函数 $f(x)$ 在 $[0, 1]$ 上具有二阶连续导数，且 $f(0) = f(1) = 0$，$\\min_{x \\in [0, 1]} f(x) = -1$。证明：$\\max_{x \\in [0, 1]} f\'\'(x) \\ge 8$。',
                'analysis': '极值点展开！函数在 $[0, 1]$ 上取到最小值 -1，设极小值点为 $x_0 \\in (0, 1)$。由费马引理：$f\'(x_0) = 0$ 且 $f(x_0) = -1$。分别在 $x_0$ 处向两个端点 $0$ 和 $1$ 进行带二阶拉格朗日余项的泰勒展开！',
                'solutionSteps': [
                    '第一步：由条件，函数在内部取到最小值，设在 $x_0 \\in (0, 1)$ 处 $f(x_0) = -1$。',
                    '由极值必要条件可知 $f\'(x_0) = 0$。',
                    '第二步：在 $x_0$ 处作带拉格朗日余项的泰勒展开：',
                    '$$f(x) = f(x_0) + f\'(x_0)(x - x_0) + \\frac{f\'\'(\\xi)}{2}(x - x_0)^2 = -1 + \\frac{f\'\'(\\xi)}{2}(x - x_0)^2$$',
                    '第三步：分别代入端点 $x = 0$ 和 $x = 1$（已知 $f(0) = f(1) = 0$）：',
                    '代入 $x = 0$：$0 = -1 + \\frac{f\'\'(\\xi_1)}{2} x_0^2 \\implies f\'\'(\\xi_1) = \\frac{2}{x_0^2}$；',
                    '代入 $x = 1$：$0 = -1 + \\frac{f\'\'(\\xi_2)}{2} (1 - x_0)^2 \\implies f\'\'(\\xi_2) = \\frac{2}{(1 - x_0)^2}$。',
                    '第四步：记 $M = \\max_{x \\in [0, 1]} f\'\'(x)$。则 $M \\ge f\'\'(\\xi_1) = \\frac{2}{x_0^2}$ 且 $M \\ge f\'\'(\\xi_2) = \\frac{2}{(1 - x_0)^2}$。',
                    '因此 $M \\ge \\max\\left\\{ \\frac{2}{x_0^2}, \\frac{2}{(1-x_0)^2} \\right\\}$。',
                    '第五步：因为 $\\min\\{x_0, 1 - x_0\\} \\le 1/2$，两点中至少有一个距离端点不超过 $1/2$！',
                    '取较小者：$\\max\\left\\{ \\frac{2}{x_0^2}, \\frac{2}{(1-x_0)^2} \\right\\} \\ge \\frac{2}{(1/2)^2} = 8$。',
                    '故必有 $\\max_{x \\in [0, 1]} f\'\'(x) \\ge 8$ 证毕！'
                ],
                'answer': '在极小值点泰勒展开证毕',
                'pitfall': '未识别出在极小值点处一阶导等于 0 的费马引理；未利用对称鸽巢原理说明 $\\min\\{x_0, 1-x_0\\} \\le 1/2$。',
                'difficulty': '★★★★★',
                'verified': True,
                'source': 'Maki考研数学真题分类精解 第十二讲 题12.1 (p.173)'
            }
        ],
        'variants': [
            {
                'id': 'var-gaoshu-10-02',
                'question': '设 $f(x)$ 二阶可导且 $f(0) = 0, f(1) = 1, f\'(0) = f\'(1) = 0$。证明存在 $\\xi \\in (0, 1)$ 使得 $|f\'\'(\\xi)| \\ge 4$。',
                'hint': '分别在中点 $1/2$ 处向两端展开相减。',
                'methodChoiceAnalysis': '泰勒展开双向相减法。',
                'fullSolution': [
                    '在 0 和 1 处分别展开：$f(1/2) = f(0) + f\'(0)(1/2) + \\frac{f\'\'(\\xi_1)}{2}(1/4) = \\frac{f\'\'(\\xi_1)}{8}$。',
                    '$f(1/2) = f(1) + f\'(1)(-1/2) + \\frac{f\'\'(\\xi_2)}{2}(1/4) = 1 + \\frac{f\'\'(\\xi_2)}{8}$。',
                    '两式相减：$1 + \\frac{f\'\'(\\xi_2)}{8} - \\frac{f\'\'(\\xi_1)}{8} = 0 \\implies f\'\'(\\xi_1) - f\'\'(\\xi_2) = 8$。',
                    '由三角不等式：$|f\'\'(\\xi_1)| + |f\'\'(\\xi_2)| \\ge 8 \\implies$ 至少有一个 $|f\'\'(\\xi)| \\ge 4$。'
                ],
                'keyTakeaway': '二阶导数证明大题，端点泰勒展开相减是满分标准模板。'
            }
        ],
        'relatedKnowledgeIds': ['gaoshu-02-taylor-formula-proof', 'gaoshu-02-mean-value-theorems'],
        'tags': ['泰勒展开', '压轴题', '二阶导数界限', '分析证明'],
        'source': 'Maki考研数学大串讲 L12 & 真题分类精解 题12.1',
        'status': 'not_started',
        'isPending': False
    }
}
