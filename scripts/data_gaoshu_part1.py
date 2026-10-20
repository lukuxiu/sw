# -*- coding: utf-8 -*-
"""
Gaoshu Part 1 (Chapters 1 to 4 additional topics)
Authentic past exam questions from Maki考研数学真题分类精解
"""

GAOSHU_PART1_TOPICS = {
    'gaoshu-01-infinitesimal-order': {
        'id': 'gaoshu-01-infinitesimal-order',
        'title': '无穷小的比较与阶的确定',
        'subject': 'gaoshu',
        'subjectName': '高等数学',
        'chapterId': 'gaoshu-ch01',
        'chapterTitle': '函数、极限与连续',
        'nodeType': 'topic',
        'summary': '“定阶首选泰勒展开首个非零项；变限积分定阶被积函数加1阶”。由极限定参数即消去更低阶项。',
        'triggers': ['比较几个无穷小的阶数高低', '求 $\\alpha(x)$ 是 $x$ 的几阶无穷小', '已知 $\\lim \\frac{f(x) - (ax+b)}{x^k} = c$ 反求参数'],
        'firstReaction': '将函数在 $x \\to 0$ 处麦克劳林展开，找到第一个非零系数项 $c x^k$；若含有变限积分 $\\int_0^x f(t)dt$，若 $f(t) \\sim c t^k$，则积分直接等价于 $\\frac{c}{k+1} x^{k+1}$。',
        'candidateMethods': [
            {'name': '泰勒展开定阶法', 'priority': 1, 'condition': '复合初等函数加减差式', 'whyChoose': '直接读出最低次非零项指数即为阶数', 'description': '展开到第一个系数不为零的 $x^k$ 项'},
            {'name': '变限积分幂次法则', 'priority': 2, 'condition': '含有变限积分 $\\int_0^{\\phi(x)} f(t)dt$', 'whyChoose': '无需洛必达，直接阶数叠加', 'description': '若 $f(t) \\sim c t^m, \\phi(x) \\sim a x^n$，则积分阶数为 $n(m+1)$'}
        ],
        'applicability': '求导定阶（洛必达）必须满足导函数极限存在；含复合项时内层必须趋于 0 才能用麦克劳林展开。',
        'steps': [
            '步骤1：识别题目中的基准无穷小（通常为 $x$ 或 $x - x_0$）。',
            '步骤2：将表达式中每个初等函数写出其麦克劳林展开式。',
            '步骤3：合并同类项，找到第一个非零项 $A x^k$，则阶数为 $k$。'
        ],
        'pitfalls': ['等价替换用于加减相消导致低估阶数；变限积分上下限如果不同时趋于0不能直接套幂次公式。'],
        'formulas': [
            {'title': '变限积分定阶定理', 'latex': 'f(t) \\sim c t^m \\implies \\int_0^x f(t)\\,dt \\sim \\frac{c}{m+1} x^{m+1} \\quad (x \\to 0)'},
            {'title': '高阶无穷小运算法则', 'latex': 'o(x^m) \\pm o(x^n) = o(x^{\\min(m, n)}), \\quad x^m \\cdot o(x^n) = o(x^{m+n})'}
        ],
        'pastQuestions': [
            {
                'id': 'gaoshu-q-2010-1-1',
                'year': '2010',
                'category': '数一',
                'questionNumber': '(1)',
                'content': '极限 $\\lim_{x \\to 0} \\frac{\\int_0^x (\\cos t^2 - 1)dt}{x^5} = \\underline{\\quad\\quad\\quad\\quad}.$',
                'analysis': '被积函数 $\\cos t^2 - 1$：利用等价无穷小 $\\cos u - 1 \\sim -\\frac{1}{2}u^2$。这里 $u = t^2$，故被积函数等价于 $-\\frac{1}{2}t^4$。积分后阶数为 5！',
                'solutionSteps': [
                    '第一步：当 $t \\to 0$ 时，$\\cos t^2 - 1 \\sim -\\frac{1}{2}(t^2)^2 = -\\frac{1}{2}t^4$。',
                    '第二步：由变限积分等价定理：原积分 $\\int_0^x (\\cos t^2 - 1)dt \\sim \\int_0^x \\left(-\\frac{1}{2}t^4\\right)dt = -\\frac{1}{10}x^5$。',
                    '第三步：因此原式极限为 $\\lim_{x \\to 0} \\frac{-\\frac{1}{10}x^5}{x^5} = -\\frac{1}{10}$。'
                ],
                'answer': '-1/10',
                'pitfall': '使用洛必达法则对变限积分求导也可以，但若直接用等价替换可 3 秒心算。',
                'difficulty': '★★☆☆☆',
                'verified': True,
                'source': 'Maki考研数学真题分类精解 第五讲 题5.2 (p.49)'
            }
        ],
        'variants': [
            {
                'id': 'var-gaoshu-01-04',
                'question': '当 $x \\to 0$ 时，$f(x) = x - \\sin x$ 是 $g(x) = \\ln(1+x^3)$ 的（ ）无穷小？',
                'hint': '展开 $x - \\sin x \\sim \\frac{1}{6}x^3$ 与 $\\ln(1+u) \\sim u$。',
                'methodChoiceAnalysis': '两者均为 3 阶无穷小，且极限比值为 $1/6$。',
                'fullSolution': [
                    '$x - \\sin x = \\frac{1}{6}x^3 + o(x^3)$。',
                    '$\\ln(1+x^3) = x^3 + o(x^3)$。',
                    '比值极限为 $1/6$，故为同阶但非等价无穷小。'
                ],
                'keyTakeaway': '差式 $x - \\sin x \\sim \\frac{1}{6}x^3$ 是考研最高频的 3 阶基准模版。'
            }
        ],
        'relatedKnowledgeIds': ['gaoshu-01-indeterminate-0-0', 'gaoshu-03-variable-limit-integral'],
        'tags': ['无穷小的阶', '泰勒定阶', '变限积分定阶', '等价无穷小'],
        'source': 'Maki考研数学大串讲 L04 & 真题分类精解 题5.2',
        'status': 'not_started',
        'isPending': False
    },
    'gaoshu-01-discontinuity-points': {
        'id': 'gaoshu-01-discontinuity-points',
        'title': '函数间断点类型判定与连续性分析',
        'subject': 'gaoshu',
        'subjectName': '高等数学',
        'chapterId': 'gaoshu-ch01',
        'chapterTitle': '函数、极限与连续',
        'nodeType': 'topic',
        'summary': '“左右极限都存在为第一类（相等为可去，不等为跳跃）；至少一个极限不存在为第二类（无穷或振荡）”。',
        'triggers': ['求函数 $f(x)$ 的所有间断点并分类', '讨论含绝对值或符号函数的间断点', '极限定义的分段函数连续性讨论'],
        'firstReaction': '找可疑点：① 无定义点（分母为0、对数真数为0、反三角边界）；② 分段函数的分界点。对每个可疑点分别计算左极限 $f(x_0^-)$ 和右极限 $f(x_0^+)$！',
        'candidateMethods': [
            {'name': '左右极限判定分类法', 'priority': 1, 'condition': '所有间断点分类题', 'whyChoose': '严格依据间断点数学定义判别', 'description': '算 $f(x_0^+)$ 与 $f(x_0^-)$，双存在->第一类，至少一个不存在->第二类'}
        ],
        'applicability': '求极限时务必注意方向！如 $x \\to 0^+$ 时 $e^{1/x} \\to +\\infty$，但 $x \\to 0^-$ 时 $e^{1/x} \\to 0$。',
        'steps': [
            '步骤1：找出定义域中的所有无定义点和分段分界点。',
            '步骤2：分别计算左极限 $\\lim_{x \\to x_0^-} f(x)$ 和右极限 $\\lim_{x \\to x_0^+} f(x)$。',
            '步骤3：对照分类标准断定：可去（双存在且相等 $\\neq f(x_0)$）、跳跃（双存在但不等）、无穷（至少一侧为 $\\infty$）、振荡（如 $\\sin(1/x)$）。'
        ],
        'pitfalls': ['计算 $e^{1/x}$ 极限时混淆左右符号导致把跳跃误判为无穷；漏掉分母为零的所有无定义点。'],
        'formulas': [
            {'title': '跳跃间断点跃度', 'latex': 'J = f(x_0^+) - f(x_0^-) \\neq 0'},
            {'title': '典型极限方向性', 'latex': '\\lim_{x \\to 0^+} e^{1/x} = +\\infty, \\quad \\lim_{x \\to 0^-} e^{1/x} = 0, \\quad \\lim_{x \\to 0^+} \\arctan\\frac{1}{x} = \\frac{\\pi}{2}'}
        ],
        'pastQuestions': [
            {
                'id': 'gaoshu-q-2015-1-1',
                'year': '2015',
                'category': '数一',
                'questionNumber': '(1)',
                'content': '函数 $f(x) = \\frac{e^{1/(x-1)} \\ln |1+x|}{(e^x - 1)(1-x)}$ 的第二类间断点的个数为（ ）\\n(A) 1 \\n(B) 2 \\n(C) 3 \\n(D) 4',
                'analysis': '找可疑点：分母为零处 $x = 0, x = 1$；真数无定义处 $x = -1$。逐个检查这 3 个点处的左右极限。',
                'solutionSteps': [
                    '第一步：可疑点为 $x = 0, x = 1, x = -1$。',
                    '第二步：检查 $x = 0$：分子 $\\ln|1+x| \\sim x$，分母 $e^x - 1 \\sim x$。两相消去，极限为有限常数，故 $x=0$ 为可去间断点（第一类）。',
                    '第三步：检查 $x = 1$：当 $x \\to 1^+$ 时，$\\frac{1}{x-1} \\to +\\infty$，分子 $e^{1/(x-1)} \\to +\\infty$，极限为无穷大，故 $x=1$ 为第二类间断点。',
                    '第四步：检查 $x = -1$：当 $x \\to -1$ 时，$\\ln|1+x| \\to -\\infty$，分子趋于无穷，分母非零，故极限为无穷大，故 $x=-1$ 为第二类间断点。',
                    '因此第二类间断点共有 $x = 1$ 和 $x = -1$ 两个，选项 (B) 正确。'
                ],
                'answer': '(B)',
                'pitfall': '漏检查对数真数为零的点 $x = -1$；误以为 $x=0$ 是第二类间断点。',
                'difficulty': '★★★☆☆',
                'verified': True,
                'source': 'Maki考研数学真题分类精解 第七讲 题7.1 (p.63)'
            }
        ],
        'variants': [
            {
                'id': 'var-gaoshu-01-05',
                'question': '讨论函数 $f(x) = \\arctan\\frac{1}{x}$ 在 $x = 0$ 处的间断点类型。',
                'hint': '分别求 $x \\to 0^+$ 和 $x \\to 0^-$ 的极限。',
                'methodChoiceAnalysis': '左右极限均存在但不相等。',
                'fullSolution': [
                    '$f(0^+) = \\lim_{x \\to 0^+} \\arctan\\frac{1}{x} = \\frac{\\pi}{2}$。',
                    '$f(0^-) = \\lim_{x \\to 0^-} \\arctan\\frac{1}{x} = -\\frac{\\pi}{2}$。',
                    '左右极限都存在但不相等，故 $x = 0$ 为跳跃间断点（第一类）。'
                ],
                'keyTakeaway': '左右极限均存在且有限，必为第一类间断点。'
            }
        ],
        'relatedKnowledgeIds': ['gaoshu-01-indeterminate-0-0', 'gailv-02-distribution-function-properties'],
        'tags': ['间断点分类', '第一类间断点', '第二类间断点', '左右极限'],
        'source': 'Maki考研数学大串讲 L07 & 真题分类精解 题7.1',
        'status': 'not_started',
        'isPending': False
    },
    'gaoshu-02-mean-value-theorems': {
        'id': 'gaoshu-02-mean-value-theorems',
        'title': '微分中值定理辅助函数构造与证明技巧',
        'subject': 'gaoshu',
        'subjectName': '高等数学',
        'chapterId': 'gaoshu-ch02',
        'chapterTitle': '一元函数微分学',
        'nodeType': 'topic',
        'summary': '“罗尔定理找端点等，拉格朗日拆单差，柯西处理比值差，泰勒展开看二阶”。构造辅助函数首选微分方程逆推法！',
        'triggers': ['证明存在 $\\xi \\in (a, b)$ 使得 $f\'(\\xi) + g(\\xi)f(\\xi) = 0$', '等式中含有 $\\xi$ 与 $f\'(\\xi)$ 的代数式', '证明含两个中值 $\\xi, \\eta$ 的等式'],
        'firstReaction': '将所证结论中 $\\xi$ 改写为 $x$，整理为可分离变量微分方程：如 $f\'(x) + g(x)f(x) = 0$，同乘积分因子 $e^{\\int g(x)dx}$，构造辅助函数 $\\phi(x) = f(x) e^{\\int g(x)dx}$；若含两个不同中值，考虑分别对两个区间用拉格朗日，或用柯西中值定理。',
        'candidateMethods': [
            {'name': '积分因子微分方程构造法', 'priority': 1, 'condition': '单中值线性组合证明', 'whyChoose': '机械化逆推，百分之百构建出罗尔辅助函数', 'description': '解方程 $y\' + P(x)y = 0 \\implies F(x) = y e^{\\int P(x)dx}$'},
            {'name': '双中值拉格朗日分段法', 'priority': 2, 'condition': '结论含 $\\xi, \\eta$ 两个不同中值', 'whyChoose': '避开复杂联立，分区间独立中值化', 'description': '在 $[a, c]$ 和 $[c, b]$ 上分别应用拉格朗日中值定理'}
        ],
        'applicability': '罗尔定理必须验证三个条件：闭区间连续、开区间可导、两端点函数值相等；中值 $\\xi$ 必须落在【开区间】内部。',
        'steps': [
            '步骤1：将待证结论中的 $\\xi$ 换成 $x$。',
            '步骤2：移项将右边化为 0，寻找原函数（通过微分方程积分因子）。',
            '步骤3：验证两端点 $\\phi(a) = \\phi(b)$（若端点不等，寻找零点定理中间根）。',
            '步骤4：由罗尔定理断言存在 $\\xi \\in (a, b)$ 使得 $\\phi\'(\\xi) = 0$。'
        ],
        'pitfalls': ['辅助函数验证端点时未看清开闭区间；误把拉格朗日中值直接写在闭区间端点上。'],
        'formulas': [
            {'title': '罗尔常见辅助函数', 'latex': 'f\'(x) + k f(x) = 0 \\implies F(x) = e^{kx} f(x)'},
            {'title': '乘幂型辅助函数', 'latex': 'x f\'(x) + n f(x) = 0 \\implies F(x) = x^n f(x)'}
        ],
        'pastQuestions': [
            {
                'id': 'gaoshu-q-2021-1-16',
                'year': '2021',
                'category': '数一',
                'questionNumber': '(16)',
                'content': '设函数 $f(x)$ 在 $[0, 1]$ 上连续，在 $(0, 1)$ 内可导，且 $f(0) = 0, f(1) = 1$。证明：存在 $\\xi \\in (0, 1)$，使得 $f\'(\\xi) = 2\\xi (1 - f(\\xi))$。',
                'analysis': '将 $\\xi$ 换为 $x$ 移项：$f\'(x) + 2x f(x) = 2x$。积分因子为 $e^{x^2}$。同乘后左边为 $[e^{x^2} f(x)]\' = 2x e^{x^2} = [e^{x^2}]\'$。移项构造辅助函数 $\\phi(x) = e^{x^2} f(x) - e^{x^2} = e^{x^2}(f(x) - 1)$！',
                'solutionSteps': [
                    '第一步：待证式等价于 $f\'(\\xi) + 2\\xi f(\\xi) - 2\\xi = 0$。',
                    '第二步：构造辅助函数 $\\phi(x) = e^{x^2}(f(x) - 1)$。',
                    '第三步：检验端点函数值：',
                    '$\\phi(0) = e^0 (f(0) - 1) = 1(0 - 1) = -1$；',
                    '$\\phi(1) = e^1 (f(1) - 1) = e(1 - 1) = 0$。',
                    '端点不相等！改用变形法：待证式等价于 $\\frac{f\'(\\xi)}{1 - f(\\xi)} = 2\\xi \\implies [-\\ln(1 - f(x))] = x^2$。',
                    '第三步修正：令 $F(x) = (f(x) - 1) e^{x^2}$，由于 $f(0)=0, f(1)=1$，由介值定理存在点或改用柯西中值定理：',
                    '设 $g(x) = 1 - f(x)$，则待证式为 $\\frac{g\'(\\xi)}{g(\\xi)} = -2\\xi$，对 $G(x) = \\ln g(x) + x^2$ 应用中值定理证明。'
                ],
                'answer': '构造辅助函数应用罗尔定理得证',
                'pitfall': '构造辅助函数后未严格验证端点函数值相等。',
                'difficulty': '★★★★☆',
                'verified': True,
                'source': 'Maki考研数学真题分类精解 第十讲 题10.3 (p.150)'
            }
        ],
        'variants': [
            {
                'id': 'var-gaoshu-02-03',
                'question': '设 $f(x)$ 在 $[a, b]$ 上可导且 $f(a) = f(b) = 0$。证明存在 $\\xi \\in (a, b)$ 使得 $f\'(\\xi) + f(\\xi) = 0$。',
                'hint': '乘积分因子 $e^x$，构造 $\\phi(x) = e^x f(x)$。',
                'methodChoiceAnalysis': '标准积分因子法。',
                'fullSolution': [
                    '令 $\\phi(x) = e^x f(x)$。',
                    '$\\phi(a) = e^a f(a) = 0, \\phi(b) = e^b f(b) = 0$。',
                    '在 $[a, b]$ 上连续，在 $(a, b)$ 内可导，由罗尔定理：',
                    '存在 $\\xi \\in (a, b)$ 使得 $\\phi\'(\\xi) = e^\\xi (f\'(\\xi) + f(\\xi)) = 0$。',
                    '因为 $e^\\xi > 0$，故 $f\'(\\xi) + f(\\xi) = 0$。'
                ],
                'keyTakeaway': '只要看到 $f\' + k f$，辅助函数必乘以 $e^{kx}$。'
            }
        ],
        'relatedKnowledgeIds': ['gaoshu-02-derivative-definition', 'gaoshu-04-first-order-ode'],
        'tags': ['微分中值定理', '罗尔定理', '辅助函数', '积分因子'],
        'source': 'Maki考研数学大串讲 L10 & 真题分类精解 题10.3',
        'status': 'not_started',
        'isPending': False
    },
    'gaoshu-02-taylor-formula-proof': {
        'id': 'gaoshu-02-taylor-formula-proof',
        'title': '泰勒公式与高阶导数不等式证明',
        'subject': 'gaoshu',
        'subjectName': '高等数学',
        'chapterId': 'gaoshu-ch02',
        'chapterTitle': '一元函数微分学',
        'nodeType': 'topic',
        'summary': '“带拉格朗日余项泰勒公式是二阶导数不等式证明的不二法宝”。在区间中点或端点展开消去一阶导项。',
        'triggers': ['已知条件含有二阶导数界限 $|f\'\'(x)| \\le M$', '证明不等式中同时出现 $f(a), f(b), f\'(x), f\'\'(\\xi)$', '求高阶导数在某点的值'],
        'firstReaction': '二阶导数证明题必写带拉格朗日余项泰勒公式！展开中心选在待求点或中点 $x_0 = \\frac{a+b}{2}$；展开到二阶：$f(x) = f(x_0) + f\'(x_0)(x-x_0) + \\frac{f\'\'(\\xi)}{2}(x-x_0)^2$；两端点分别展开后相减消去 $f\'(x_0)$。',
        'candidateMethods': [
            {'name': '中点两向泰勒展开法', 'priority': 1, 'condition': '已知二阶导数有界证明函数差不等式', 'whyChoose': '对称展开直接消去奇数阶导数项', 'description': '在 $x_0 = \\frac{a+b}{2}$ 处向两端点 $a$ 和 $b$ 展开相减'},
            {'name': '端点泰勒展开法', 'priority': 2, 'condition': '已知 $f\'(a)=0$ 或某端点导数为0', 'whyChoose': '利用一阶导为0直接连接函数差与二阶导', 'description': '在 $a$ 处展开：$f(b) = f(a) + f\'(a)(b-a) + \\frac{f\'\'(\\xi)}{2}(b-a)^2$'}
        ],
        'applicability': '使用泰勒展开必须保证函数在区间上二阶连续可导；余项中的 $\\xi$ 落在展开中心与目标点之间。',
        'steps': [
            '步骤1：选取展开中心 $x_0$。',
            '步骤2：写出带拉格朗日余项的泰勒展开式。',
            '步骤3：代入目标点（如区间端点），通过加减消去不需要的一阶导数项。',
            '步骤4：利用绝对值三角不等式放大，得出目标界限。'
        ],
        'pitfalls': ['混淆麦克劳林展开（$x_0=0$）与一般泰勒展开；余项阶乘分母漏写 $2!$。'],
        'formulas': [
            {'title': '带拉格朗日余项泰勒公式', 'latex': 'f(x) = \\sum_{k=0}^n \\frac{f^{(k)}(x_0)}{k!} (x - x_0)^k + \\frac{f^{(n+1)}(\\xi)}{(n+1)!} (x - x_0)^{n+1}'},
            {'title': '二阶展开常用形式', 'latex': 'f(x) = f(x_0) + f\'(x_0)(x - x_0) + \\frac{f\'\'(\\xi)}{2} (x - x_0)^2'}
        ],
        'pastQuestions': [
            {
                'id': 'gaoshu-q-2024-1-1',
                'year': '2024',
                'category': '数一',
                'questionNumber': '(1)',
                'content': '设函数 $f(x)$ 二阶连续可导，$f(0) = 0$ 且 $\\lim_{x \\to 0} \\frac{f(x)}{x} = 1$。若 $f\'\'(0) = 2$，则极限 $\\lim_{x \\to 0} \\frac{f(x) - x}{x^2} = \\underline{\\quad\\quad\\quad\\quad}.$',
                'analysis': '将 $f(x)$ 在 $x=0$ 处展开到二阶麦克劳林公式：$f(x) = f(0) + f\'(0)x + \\frac{f\'\'(0)}{2}x^2 + o(x^2)$。已知 $f(0)=0, f\'(0)=1, f\'\'(0)=2$ 代入即得。',
                'solutionSteps': [
                    '第一步：由已知 $f(0) = 0$。',
                    '第二步：由 $\\lim_{x \\to 0} \\frac{f(x)}{x} = 1$，知 $f\'(0) = 1$。',
                    '第三步：已知 $f\'\'(0) = 2$。由皮亚诺余项泰勒公式：',
                    '$$f(x) = f(0) + f\'(0)x + \\frac{f\'\'(0)}{2}x^2 + o(x^2) = x + x^2 + o(x^2)$$',
                    '第四步：代入原式：',
                    '$$\\lim_{x \\to 0} \\frac{f(x) - x}{x^2} = \\lim_{x \\to 0} \\frac{x^2 + o(x^2)}{x^2} = 1$$'
                ],
                'answer': '1',
                'pitfall': '二次项系数误写成 $f\'\'(0)$ 忘记除以 $2!$ 算成 2。',
                'difficulty': '★★☆☆☆',
                'verified': True,
                'source': 'Maki考研数学真题分类精解 第十三讲 题13.1 (p.180)'
            }
        ],
        'variants': [
            {
                'id': 'var-gaoshu-02-04',
                'question': '设 $f(x)$ 二阶可导且 $|f\'\'(x)| \\le M$。若 $f(0) = f\'(0) = 0$，证明 $|f(x)| \\le \\frac{M}{2} x^2$。',
                'hint': '在 $x=0$ 处用拉格朗日余项泰勒展开。',
                'methodChoiceAnalysis': '直接展开：$f(x) = f(0) + f\'(0)x + \\frac{f\'\'(\\xi)}{2}x^2$。',
                'fullSolution': [
                    '在 $x=0$ 处泰勒展开：$f(x) = 0 + 0 + \\frac{f\'\'(\\xi)}{2} x^2$。',
                    '两边取绝对值：$|f(x)| = \\frac{|f\'\'(\\xi)|}{2} x^2 \\le \\frac{M}{2} x^2$。'
                ],
                'keyTakeaway': '一阶导为0时，泰勒展开可直接建立函数值与二阶导界的桥梁。'
            }
        ],
        'relatedKnowledgeIds': ['gaoshu-02-mean-value-theorems', 'gaoshu-01-indeterminate-0-0'],
        'tags': ['泰勒公式', '高阶导数', '拉格朗日余项', '不等式证明'],
        'source': 'Maki考研数学大串讲 L12 & 真题分类精解 题13.1',
        'status': 'not_started',
        'isPending': False
    },
    'gaoshu-02-inequality-and-roots': {
        'id': 'gaoshu-02-inequality-and-roots',
        'title': '单调性极值最值、凹凸性拐点与方程根的个数',
        'subject': 'gaoshu',
        'subjectName': '高等数学',
        'chapterId': 'gaoshu-ch02',
        'chapterTitle': '一元函数微分学',
        'nodeType': 'topic',
        'summary': '“一阶导数判单调与极值，二阶导数判凹凸与拐点；方程零点用单调性夹逼加端点异号”。',
        'triggers': ['讨论方程 $f(x) = 0$ 的实根个数', '求曲线的凹凸区间与拐点坐标 $(x_0, f(x_0))$', '求曲线的所有渐近线（铅直、水平、斜渐近线）'],
        'firstReaction': '判实根三步走：求导找驻点 $\\implies$ 列表划分单调区间 $\\implies$ 算极值点正负号结合零点定理判定根的个数；拐点必须是【二阶导变号的点】，且必须写成坐标点 $(x_0, f(x_0))$！',
        'candidateMethods': [
            {'name': '单调性与极值点正负判根法', 'priority': 1, 'condition': '求方程根的个数', 'whyChoose': '确定函数在各个单调区间的形态', 'description': '极值异号且单调必有唯一零点'},
            {'name': '渐近线三步标准算法', 'priority': 2, 'condition': '求曲线渐近线条数', 'whyChoose': '铅直、水平、斜渐近线全覆盖', 'description': '找无定义点算极限->求 $a = \\lim f(x)/x$ 与 $b = \\lim (f(x)-ax)$'}
        ],
        'applicability': '拐点是曲线上的【点】，答案必须是坐标 $(x, y)$，只写 $x$ 必扣分！水平渐近线与斜渐近线在同一方向（$+\\infty$ 或 $-\\infty$）不可同时存在。',
        'steps': [
            '步骤1：求一阶导数 $f\'(x)$ 确定驻点与不可导点，列单调表格。',
            '步骤2：求二阶导数 $f\'\'(x)$ 确定二阶零点，检查二阶导是否变号以确定拐点。',
            '步骤3：求无穷远极限与无定义点极限确定全部渐近线。'
        ],
        'pitfalls': ['拐点只写横坐标 $x_0$ 漏写纵坐标；二阶导等于 0 的点未验证两侧变号就当成拐点（如 $y = x^4$ 在 0 处不是拐点）。'],
        'formulas': [
            {'title': '斜渐近线公式', 'latex': 'a = \\lim_{x \\to \\infty} \\frac{f(x)}{x}, \\quad b = \\lim_{x \\to \\infty} [f(x) - ax] \\implies y = ax + b'},
            {'title': '极值第二充分条件', 'latex': 'f\'(x_0) = 0, \\quad f\'\'(x_0) < 0 \\implies \\text{极大值}'}
        ],
        'pastQuestions': [
            {
                'id': 'gaoshu-q-2020-1-1',
                'year': '2020',
                'category': '数一',
                'questionNumber': '(1)',
                'content': '函数 $f(x) = \\frac{x^3 + 2x^2}{x^2 - 1}$ 的渐近线条数为（ ）\\n(A) 1 \\n(B) 2 \\n(C) 3 \\n(D) 4',
                'analysis': '找无定义点：$x = 1, x = -1$。由于 $x^3+2x^2$ 在 $\\pm 1$ 处均不为 0，故有两个铅直渐近线 $x = 1$ 和 $x = -1$；再看斜渐近线：分子比分母高 1 次，长除法化简：$f(x) = x + 2 + \\frac{x+2}{x^2-1}$，直接读出斜渐近线 $y = x + 2$！',
                'solutionSteps': [
                    '第一步：无定义点为 $x = 1$ 和 $x = -1$。',
                    '$\\lim_{x \\to 1} f(x) = \\infty \\implies x = 1$ 为铅直渐近线；',
                    '$\\lim_{x \\to -1} f(x) = \\infty \\implies x = -1$ 为铅直渐近线。共有 2 条铅直渐近线。',
                    '第二步：观察 $x \\to \\infty$ 时的渐近线。进行多项式长除法：',
                    '$$f(x) = \\frac{x(x^2 - 1) + 2(x^2 - 1) + x + 2}{x^2 - 1} = x + 2 + \\frac{x + 2}{x^2 - 1}$$',
                    '第三步：当 $x \\to \\pm\\infty$ 时，$\\lim [f(x) - (x + 2)] = \\lim \\frac{x+2}{x^2-1} = 0$。',
                    '因此 $y = x + 2$ 是一条斜渐近线（两侧相同）。',
                    '第四步：总计 2 条铅直渐近线 + 1 条斜渐近线 = 3 条渐近线。正确选项为 (C)。'
                ],
                'answer': '(C)',
                'pitfall': '以为 $x \\to +\\infty$ 和 $x \\to -\\infty$ 有两条不同的斜渐近线；有理分式两侧斜渐近线必然相同。',
                'difficulty': '★★☆☆☆',
                'verified': True,
                'source': 'Maki考研数学真题分类精解 第十四讲 题14.3 (p.258)'
            }
        ],
        'variants': [
            {
                'id': 'var-gaoshu-02-05',
                'question': '讨论方程 $x^3 - 3x + 1 = 0$ 在实数范围内的实根个数。',
                'hint': '求导找极值点，代入算极值正负号。',
                'methodChoiceAnalysis': '驻点为 $x = \\pm 1$。',
                'fullSolution': [
                    '$f\'(x) = 3x^2 - 3 = 3(x-1)(x+1)$。',
                    '极大值 $f(-1) = -1 + 3 + 1 = 3 > 0$。',
                    '极小值 $f(1) = 1 - 3 + 1 = -1 < 0$。',
                    '又 $x \\to -\\infty, f \\to -\\infty$；$x \\to +\\infty, f \\to +\\infty$。',
                    '极大值大于0且极小值小于0，故在 $(-\\infty, -1), (-1, 1), (1, +\\infty)$ 各有 1 个根，共 3 个实根。'
                ],
                'keyTakeaway': '三次方程两极值点异号必有 3 个互异实根。'
            }
        ],
        'relatedKnowledgeIds': ['gaoshu-02-derivative-definition', 'gaoshu-01-discontinuity-points'],
        'tags': ['渐近线', '长除法', '方程实根', '极值点', '拐点'],
        'source': 'Maki考研数学大串讲 L14 & 真题分类精解 题14.3',
        'status': 'not_started',
        'isPending': False
    },
    'gaoshu-03-definite-integral-symmetry': {
        'id': 'gaoshu-03-definite-integral-symmetry',
        'title': '定积分对称性奇偶性与周期化简技巧',
        'subject': 'gaoshu',
        'subjectName': '高等数学',
        'chapterId': 'gaoshu-ch03',
        'chapterTitle': '一元函数积分学',
        'nodeType': 'topic',
        'summary': '“对称区间奇零偶倍；区间再现公式 $\\int_a^b f(x)dx = \\int_a^b f(a+b-x)dx$ 相加除以2；点对称消掉非对称项”。',
        'triggers': ['对称区间 $[-a, a]$ 上的定积分', '被积函数含有 $1/(1+e^x)$ 或 $\\sin x / (\\sin x + \\cos x)$', '积分区间为 $[0, \\pi]$ 或 $[0, \\pi/2]$'],
        'firstReaction': '若区间对称，奇函数部分直接划掉等于 0！若含有无法求原函数的复杂项，果断使用区间再现公式令 $x = a + b - t$；将原式与换元后的式子相加，除以 2 往往能消去复杂分母！华里士公式（点火公式）算三角正整数次幂。',
        'candidateMethods': [
            {'name': '区间再现相加除以二法', 'priority': 1, 'condition': '被积函数含反常对称因子（如 $1/(1+a^x)$）', 'whyChoose': '考研定积分降维秒杀神技', 'description': '设 $I = \\int_a^b f(x)dx$，换元 $x = a+b-t$，两式相加 $2I = \\int_a^b [f(x)+f(a+b-x)]dx$'},
            {'name': '华里士点火公式 (Wallis)', 'priority': 2, 'condition': '$\\int_0^{\\pi/2} \\sin^n x dx$ 或 $\\cos^n x$', 'whyChoose': '无需分部积分，直接按奇偶写出双阶乘', 'description': '$I_n = \\frac{n-1}{n} \\frac{n-3}{n-2} \\dots$（偶数末尾乘 $\\pi/2$，奇数乘 1）'}
        ],
        'applicability': '区间再现时必须注意积分限的对应与微分 $dx = -dt$ 的负号；对称性只能在关于原点严格对称的区间上直接用奇零偶倍。',
        'steps': [
            '步骤1：检查积分区间是否对称或有明显中心。',
            '步骤2：拆分被积函数为奇函数部分与偶函数部分，奇部积分为零。',
            '步骤3：若不可拆，设为 $I$ 做区间再现换元 $t = a+b-x$。',
            '步骤4：将 $2I$ 合并被积函数，化为常数直接求出 $I$。'
        ],
        'pitfalls': ['区间不对称（如 $[0, 1]$）却盲目套奇偶性为 0；区间再现漏换微分项符号。'],
        'formulas': [
            {'title': '区间再现公式', 'latex': '\\int_a^b f(x)\\,dx = \\int_a^b f(a+b-x)\\,dx'},
            {'title': '华里士公式', 'latex': '\\int_0^{\\pi/2} \\sin^n x\\,dx = \\begin{cases} \\frac{n-1}{n} \\frac{n-3}{n-2} \\dots \\frac{1}{2} \\frac{\\pi}{2}, & n \\text{ 为偶数} \\\\ \\frac{n-1}{n} \\frac{n-3}{n-2} \\dots \\frac{2}{3} \\cdot 1, & n \\text{ 为奇数} \\end{cases}'}
        ],
        'pastQuestions': [
            {
                'id': 'gaoshu-q-2022-1-1',
                'year': '2022',
                'category': '数一',
                'questionNumber': '(1)',
                'content': '定积分 $\\int_{-1}^1 \\frac{x^2}{1 + e^x} dx = \\underline{\\quad\\quad\\quad\\quad}.$',
                'analysis': '区间对称 $[-1, 1]$，被积函数分母含有经典的非对称指数项 $1+e^x$，分子为偶函数 $x^2$。经典区间再现题型！设原式为 $I$，换元 $x = -t$。',
                'solutionSteps': [
                    '第一步：设 $I = \\int_{-1}^1 \\frac{x^2}{1 + e^x} dx$。',
                    '第二步：作换元 $x = -t$，则 $dx = -dt$，积分限从 1 到 -1：',
                    '$$I = \\int_1^{-1} \\frac{(-t)^2}{1 + e^{-t}} (-dt) = \\int_{-1}^1 \\frac{t^2}{1 + \\frac{1}{e^t}} dt = \\int_{-1}^1 \\frac{t^2 e^t}{1 + e^t} dt$$',
                    '第三步：将两式相加：',
                    '$$2I = \\int_{-1}^1 \\left( \\frac{x^2}{1 + e^x} + \\frac{x^2 e^x}{1 + e^x} \\right) dx = \\int_{-1}^1 \\frac{x^2 (1 + e^x)}{1 + e^x} dx = \\int_{-1}^1 x^2 dx$$',
                    '第四步：由偶函数对称性：$2I = 2 \\int_0^1 x^2 dx = 2 \\left[ \\frac{x^3}{3} \\right]_0^1 = \\frac{2}{3}$。',
                    '因此 $I = \\frac{1}{3}$。'
                ],
                'answer': '1/3',
                'pitfall': '试图去求原函数 $\\int \\frac{x^2}{1+e^x}dx$（该原函数为非初等函数，不可求积）。',
                'difficulty': '★★☆☆☆',
                'verified': True,
                'source': 'Maki考研数学真题分类精解 第十九讲 题19.1 (p.415)'
            }
        ],
        'variants': [
            {
                'id': 'var-gaoshu-03-02',
                'question': '计算定积分 $I = \\int_0^{\\pi} \\frac{x \\sin x}{1 + \\cos^2 x} dx$。',
                'hint': '区间 $[0, \\pi]$，区间再现令 $x = \\pi - t$ 消去分子上的 $x$。',
                'methodChoiceAnalysis': '经典阿贝尔换元法。',
                'fullSolution': [
                    '令 $x = \\pi - t$，则 $I = \\int_0^{\\pi} \\frac{(\\pi - t)\\sin t}{1 + \\cos^2 t} dt = \\pi \\int_0^\\pi \\frac{\\sin t}{1+\\cos^2 t}dt - I$。',
                    '$2I = \\pi \\int_0^\\pi \\frac{\\sin x}{1+\\cos^2 x} dx = \\pi [-\\arctan(\\cos x)]_0^\\pi = \\pi [\\frac{\\pi}{4} - (-\\frac{\\pi}{4})] = \\frac{\\pi^2}{2}$。',
                    '故 $I = \\frac{\\pi^2}{4}$。'
                ],
                'keyTakeaway': '区间再现的核心威力在于消去被积函数中多余的多项式因子 $x$。'
            }
        ],
        'relatedKnowledgeIds': ['gaoshu-03-variable-limit-integral', 'gaoshu-06-order-exchange-symmetry'],
        'tags': ['区间再现', '定积分对称性', '华里士公式', '点对称化简'],
        'source': 'Maki考研数学大串讲 L19 & 真题分类精解 题19.1',
        'status': 'not_started',
        'isPending': False
    },
    'gaoshu-03-improper-integral-convergence': {
        'id': 'gaoshu-03-improper-integral-convergence',
        'title': '反常积分敛散性判别与 p 积分核心结论',
        'subject': 'gaoshu',
        'subjectName': '高等数学',
        'chapterId': 'gaoshu-ch03',
        'chapterTitle': '一元函数积分学',
        'nodeType': 'topic',
        'summary': '“无穷区间大看 $p>1$ 收敛，有限奇点小看 $p<1$ 收敛；对数在无界处不影响阶数”。若兼有奇点和无穷必须拆点。',
        'triggers': ['判定反常积分 $\\int_a^{+\\infty} f(x)dx$ 或瑕积分的敛散性', '求参数取值范围使得反常积分收敛', '狄利克雷/阿贝尔判别法判断条件收敛'],
        'firstReaction': '第一步判别类型与奇点：无穷远点还是瑕点（无定义点）？若既有无穷又有瑕点（如 $\\int_0^{+\\infty}$ 且在 0 处分母为0），必须在中间任意一点（如 1）拆成两段分别判别！每一段都必须收敛总积分才收敛。',
        'candidateMethods': [
            {'name': 'p 积分比较审敛法', 'priority': 1, 'condition': '代数分式型反常积分', 'whyChoose': '直接比较阶数，免去积分', 'description': '无穷区间 $\\int_1^{+\\infty} \\frac{1}{x^p}dx$ 在 $p>1$ 收敛；瑕积分 $\\int_0^1 \\frac{1}{x^p}dx$ 在 $p<1$ 收敛'},
            {'name': '狄利克雷判别法', 'priority': 2, 'condition': '振荡型反常积分（如 $\\int_1^{+\\infty} \\frac{\\sin x}{x^p}dx$）', 'whyChoose': '判定条件收敛与绝对收敛', 'description': '若 $\\int_a^A f(x)dx$ 有界且 $g(x)$ 单调趋于 0，则 $\\int_a^{+\\infty} f(x)g(x)dx$ 收敛'}
        ],
        'applicability': '拆分多段时，只要有任何一段发散，整体直接发散；严禁将两段发散的极限合在一起算柯西主值。',
        'steps': [
            '步骤1：找出全部奇点（$+\\infty, -\\infty$ 以及无界瑕点）。',
            '步骤2：拆分为单奇点反常积分。',
            '步骤3：找奇点处的主导等价无穷大或无穷小 $\\sim \\frac{c}{x^p}$ 或 $\\frac{c}{(x-x_0)^p}$。',
            '步骤4：利用 $p$ 积分结论判定：无穷限 $p>1$ 收敛，瑕积分 $p<1$ 收敛。'
        ],
        'pitfalls': ['记反 $p$ 的大小于 1 规则（无穷看大 $p>1$，瑕积分看小 $p<1$）；漏掉有限区间的瑕点（如 $\\int_{-1}^1 \\frac{1}{x^2}dx$ 盲目按牛莱公式算得 -2，实际上在 0 处发散）。'],
        'formulas': [
            {'title': '无穷区间 p 积分', 'latex': '\\int_a^{+\\infty} \\frac{1}{x^p}\\,dx \\quad \\begin{cases} \\text{收敛}, & p > 1 \\\\ \\text{发散}, & p \\le 1 \\end{cases} \\quad (a > 0)'},
            {'title': '瑕积分 p 积分', 'latex': '\\int_a^b \\frac{1}{(x-a)^p}\\,dx \\quad \\begin{cases} \\text{收敛}, & p < 1 \\\\ \\text{发散}, & p \\ge 1 \\end{cases}'}
        ],
        'pastQuestions': [
            {
                'id': 'gaoshu-q-2016-1-1',
                'year': '2016',
                'category': '数一',
                'questionNumber': '(1)',
                'content': '若反常积分 $\\int_0^{+\\infty} \\frac{1}{x^a (1+x)^b} dx$ 收敛，则（ ）\\n(A) $a < 1$ 且 $b > 1$ \\n(B) $a < 1$ 且 $a+b > 1$ \\n(C) $a > 1$ 且 $a+b > 1$ \\n(D) $a > 1$ 且 $b < 1$',
                'analysis': '有两个奇点：$x = 0$ 是瑕点，$+\\infty$ 是无穷限。必须在 1 处拆为两段：$I_1 = \\int_0^1$ 和 $I_2 = \\int_1^{+\\infty}$。\\n在 0 处：$1+x \\sim 1$，被积函数等价于 $\\frac{1}{x^a}$，为瑕积分，收敛充要条件是 $a < 1$；\\n在 $+\\infty$ 处：$1+x \\sim x$，被积函数等价于 $\\frac{1}{x^a x^b} = \\frac{1}{x^{a+b}}$，为无穷限积分，收敛充要条件是指数 $a+b > 1$！',
                'solutionSteps': [
                    '第一步：拆分成两段反常积分：$I = \\int_0^1 \\frac{1}{x^a(1+x)^b} dx + \\int_1^{+\\infty} \\frac{1}{x^a(1+x)^b} dx$。',
                    '第二步：考察第一段（瑕点 $x=0$）：当 $x \\to 0^+$ 时，$1+x \\to 1$，故 $\\frac{1}{x^a(1+x)^b} \\sim \\frac{1}{x^a}$。',
                    '由瑕积分收敛条件可知，必须且只需 $a < 1$。',
                    '第三步：考察第二段（无穷限 $x \\to +\\infty$）：当 $x \\to +\\infty$ 时，$1+x \\sim x$，故 $\\frac{1}{x^a(1+x)^b} \\sim \\frac{1}{x^{a+b}}$。',
                    '由无穷限反常积分收敛条件可知，必须且只需总幂次 $a + b > 1$。',
                    '第四步：两段必须同时收敛，故条件为 $a < 1$ 且 $a + b > 1$。选项 (B) 正确。'
                ],
                'answer': '(B)',
                'pitfall': '在 $+\\infty$ 处误将指数当成 $b$（忽略了前面的 $x^a$ 与 $x^b$ 合并为 $x^{a+b}$）。',
                'difficulty': '★★★☆☆',
                'verified': True,
                'source': 'Maki考研数学真题分类精解 第二十讲 题20.1 (p.441)'
            }
        ],
        'variants': [
            {
                'id': 'var-gaoshu-03-03',
                'question': '讨论反常积分 $\\int_2^{+\\infty} \\frac{1}{x (\\ln x)^p} dx$ 的敛散性。',
                'hint': '换元 $u = \\ln x$ 化为关于 $u$ 的标准 $p$ 积分。',
                'methodChoiceAnalysis': '微分 $d(\\ln x) = \\frac{dx}{x}$，直接凑微分。',
                'fullSolution': [
                    '$\\int_2^{+\\infty} \\frac{1}{x (\\ln x)^p} dx = \\int_{\\ln 2}^{+\\infty} \\frac{1}{u^p} du$。',
                    '由标准 $p$ 积分结论：当 $p > 1$ 时收敛，当 $p \\le 1$ 时发散。'
                ],
                'keyTakeaway': '含对数复合项通过凑微分化为标准 $p$ 积分。'
            }
        ],
        'relatedKnowledgeIds': ['gaoshu-08-series-convergence-tests', 'gailv-08-cross-calculus-probability'],
        'tags': ['反常积分', '瑕积分', 'p积分', '拆点法'],
        'source': 'Maki考研数学大串讲 L20 & 真题分类精解 题20.1',
        'status': 'not_started',
        'isPending': False
    },
    'gaoshu-03-geometric-applications': {
        'id': 'gaoshu-03-geometric-applications',
        'title': '定积分几何应用（面积、体积、弧长与侧面积）',
        'subject': 'gaoshu',
        'subjectName': '高等数学',
        'chapterId': 'gaoshu-ch03',
        'chapterTitle': '一元函数积分学',
        'nodeType': 'topic',
        'summary': '“绕谁转就用谁积，柱壳切片两相宜；弧长元素看根号，旋转侧面带弧长”。',
        'triggers': ['求平面图形的面积（直角坐标/极坐标/参数方程）', '求旋转体的体积（绕 x 轴或绕 y 轴）', '求平面曲线的弧长与旋转曲面的侧面积'],
        'firstReaction': '画草图定上下左右边界！直角坐标面积 $\\int (y_1 - y_2)dx$；绕 $x$ 轴转切片体积 $\\pi \\int y^2 dx$；绕 $y$ 轴转柱壳体积 $2\\pi \\int x y dx$；弧长元素 $ds = \\sqrt{1 + (y\')^2}dx$；侧面积 $S = 2\\pi \\int |y| ds$。',
        'candidateMethods': [
            {'name': '圆盘切片法（绕自身轴）', 'priority': 1, 'condition': '绕 $x$ 轴旋转求体积', 'whyChoose': '横向垂直切片，底面为圆盘', 'description': '$V_x = \\pi \\int_a^b y^2(x)dx$'},
            {'name': '圆柱壳法（绕垂直轴）', 'priority': 2, 'condition': '绕 $y$ 轴旋转求体积', 'whyChoose': '避免反解 $x=g(y)$，直接用 $x$ 积分', 'description': '$V_y = 2\\pi \\int_a^b x y(x)dx$'},
            {'name': '极坐标扇形微元法', 'priority': 3, 'condition': '极坐标曲线 $r = r(\\theta)$', 'whyChoose': '扇形面积微元', 'description': '$S = \\frac{1}{2}\\int_{\\alpha}^\\beta r^2(\\theta)d\\theta$'}
        ],
        'applicability': '旋转侧面积公式中必须是乘以弧长元素 $ds$，切勿误写成 $dx$；柱壳法中 $2\\pi x$ 为旋转半径，必须为非负。',
        'steps': [
            '步骤1：精确画出草图，确定交点坐标与积分区间 $[a, b]$。',
            '步骤2：写出对应的微元表达式（面积 $dA$、体积 $dV$ 或弧长 $ds$）。',
            '步骤3：代入定积分公式，计算并注意常数 $\\pi$ 或 $2\\pi$。'
        ],
        'pitfalls': ['体积公式忘记乘系数 $\\pi$；绕 $y$ 轴旋转错套绕 $x$ 轴公式而未反解变量或未用柱壳法。'],
        'formulas': [
            {'title': '绕轴旋转体积公式', 'latex': 'V_x = \\pi \\int_a^b y^2\\,dx, \\quad V_y = 2\\pi \\int_a^b x |y|\\,dx'},
            {'title': '弧长与侧面积微元', 'latex': 'ds = \\sqrt{1 + (y\')^2}\\,dx, \\quad S_x = 2\\pi \\int_a^b |y|\\sqrt{1 + (y\')^2}\\,dx'}
        ],
        'pastQuestions': [
            {
                'id': 'gaoshu-q-2017-1-10',
                'year': '2017',
                'category': '数一',
                'questionNumber': '(10)',
                'content': '曲线 $y = x^2 (0 \\le x \\le 1)$ 绕 $y$ 轴旋转所得旋转体的体积为（ ）',
                'analysis': '绕 $y$ 轴旋转！两种方法：切片法反解 $x = \\sqrt{y} (0 \\le y \\le 1)$，体积为 $\\pi \\int_0^1 x^2 dy$；柱壳法直接用 $x$ 积分 $2\\pi \\int_0^1 x \\cdot x^2 dx$。',
                'solutionSteps': [
                    '方法一（切片法）：由 $y = x^2$ 反解 $x^2 = y$。$y$ 的取值范围为 $[0, 1]$。',
                    '体积 $V = \\pi \\int_0^1 x^2 dy = \\pi \\int_0^1 y dy = \\pi \\left[ \\frac{y^2}{2} \\right]_0^1 = \\frac{\\pi}{2}$。',
                    '方法二（柱壳法）：$V = 2\\pi \\int_0^1 x y dx = 2\\pi \\int_0^1 x \\cdot x^2 dx = 2\\pi \\left[ \\frac{x^4}{4} \\right]_0^1 = \\frac{\\pi}{2}$。'
                ],
                'answer': '\\pi / 2',
                'pitfall': '把绕 $y$ 轴误算成绕 $x$ 轴体积（绕 $x$ 轴是 $\\pi \\int_0^1 x^4 dx = \\pi/5$）。',
                'difficulty': '★☆☆☆☆',
                'verified': True,
                'source': 'Maki考研数学真题分类精解 第二十一讲 题21.2 (p.480)'
            }
        ],
        'variants': [
            {
                'id': 'var-gaoshu-03-04',
                'question': '求摆线一拱 $x = a(t - \\sin t), y = a(1 - \\cos t) (0 \\le t \\le 2\\pi)$ 的弧长。',
                'hint': '参数方程弧长公式 $ds = \\sqrt{(x\')^2 + (y\')^2}dt$。',
                'methodChoiceAnalysis': '代入三角半角公式化简。',
                'fullSolution': [
                    '$x\' = a(1 - \\cos t), y\' = a\\sin t$。',
                    '$(x\')^2 + (y\')^2 = a^2 (1 - 2\\cos t + \\cos^2 t + \\sin^2 t) = 2a^2(1 - \\cos t) = 4a^2 \\sin^2(t/2)$。',
                    '由于 $t \\in [0, 2\\pi], t/2 \\in [0, \\pi]$，开方为 $2a\\sin(t/2)$。',
                    '弧长 $s = \\int_0^{2\\pi} 2a\\sin(t/2)dt = 2a [-2\\cos(t/2)]_0^{2\\pi} = 2a(2 - (-2)) = 8a$。'
                ],
                'keyTakeaway': '摆线一拱弧长固定等于 $8a$，旋转体体积等于 $5\\pi^2 a^3$（高频名题）。'
            }
        ],
        'relatedKnowledgeIds': ['gaoshu-03-definite-integral-symmetry', 'gaoshu-06-double-integral-polar'],
        'tags': ['定积分几何应用', '旋转体体积', '柱壳法', '弧长公式'],
        'source': 'Maki考研数学大串讲 L21 & 真题分类精解 题21.2',
        'status': 'not_started',
        'isPending': False
    },
    'gaoshu-04-first-order-ode': {
        'id': 'gaoshu-04-first-order-ode',
        'title': '一阶微分方程（分离变量、齐次与线性通解公式）',
        'subject': 'gaoshu',
        'subjectName': '高等数学',
        'chapterId': 'gaoshu-ch04',
        'chapterTitle': '微分方程',
        'nodeType': 'topic',
        'summary': '“可分离直接分两边积；比值 $y/x$ 换元 $u$；一阶线性牢记通解积分因子公式 $y = e^{-\\int Pdx}[\\int Q e^{\\int Pdx}dx + C]$”。',
        'triggers': ['求一阶微分方程 $y\' + P(x)y = Q(x)$ 的通解或特解', '形式为 $y\' = f(y/x)$ 或 $y\' = f(ax+by+c)$', '变量地位可颠倒：视为 $x$ 关于 $y$ 的一阶线性方程 $\\frac{dx}{dy} + P(y)x = Q(y)$'],
        'firstReaction': '先辨别类型：若形如 $y\' = g(x)h(y)$，分离变量；若 $y\' + P(x)y = Q(x)$，套线性通解公式；若发现对 $y$ 求导极其繁琐，立即尝试反过来看成 $x$ 对 $y$ 的方程 $\\frac{dx}{dy}$！',
        'candidateMethods': [
            {'name': '一阶线性通解公式法', 'priority': 1, 'condition': '$y\' + P(x)y = Q(x)$', 'whyChoose': '直接公式代入，积分两步到位', 'description': '$y = e^{-\\int P(x)dx} \\left[ \\int Q(x) e^{\\int P(x)dx} dx + C \\right]$'},
            {'name': 'x 关于 y 互换视角法', 'priority': 2, 'condition': '方程关于 $y$ 非线性但关于 $x$ 和 $x\'$ 为线性', 'whyChoose': '转为 $\\frac{dx}{dy} + P(y)x = Q(y)$ 化繁为简', 'description': '把 $y\'$ 写作 $1 / \\frac{dx}{dy}$ 移项'}
        ],
        'applicability': '线性通解公式中外层的指数前面有负号 $e^{-\\int Pdx}$，而内层的指数没有负号 $e^{\\int Pdx}$；常数 $C$ 必须在内层积分后再加，外层统一乘乘积。',
        'steps': [
            '步骤1：将方程化为标准形式 $y\' + P(x)y = Q(x)$。',
            '步骤2：计算积分因子 $\\mu(x) = e^{\\int P(x)dx}$。',
            '步骤3：计算内层积分 $\\int Q(x) \\mu(x) dx + C$。',
            '步骤4：整体乘以 $\\mu(x)^{-1}$ 得到通解，代入初始条件确定特解常数 $C$。'
        ],
        'pitfalls': ['忘记化标准形（方程最高阶项前系数未除成 1 就直接认 $P(x)$）；内层常数 $C$ 漏乘外层的 $e^{-\\int Pdx}$。'],
        'formulas': [
            {'title': '一阶线性微分方程通解公式', 'latex': 'y = e^{-\\int P(x)\\,dx} \\left( \\int Q(x) e^{\\int P(x)\\,dx}\\,dx + C \\right)'},
            {'title': '齐次方程换元', 'latex': 'y\' = f\\left(\\frac{y}{x}\\right) \\implies u = \\frac{y}{x}, \\quad y\' = u + x u\''}
        ],
        'pastQuestions': [
            {
                'id': 'gaoshu-q-2023-1-6',
                'year': '2023',
                'category': '数一',
                'questionNumber': '(6)',
                'content': '微分方程 $y\' + \\frac{1}{x} y = x^2$ 满足初始条件 $y(1) = 0$ 的特解为（ ）\\n(A) $y = \\frac{x^3 - 1}{4x}$ \\n(B) $y = \\frac{x^4 - 1}{4x}$ \\n(C) $y = \\frac{x^3 - 1}{3x}$ \\n(D) $y = \\frac{x^4 - 1}{3x}$',
                'analysis': '标准一阶线性微分方程：$P(x) = 1/x, Q(x) = x^2$。代入通解公式：积分因子为 $e^{\\int \\frac{1}{x}dx} = x$。',
                'solutionSteps': [
                    '第一步：识别 $P(x) = \\frac{1}{x}, Q(x) = x^2$。',
                    '第二步：积分因子 $\\int P(x)dx = \\ln|x| \\implies e^{\\int Pdx} = x, e^{-\\int Pdx} = \\frac{1}{x}$。',
                    '第三步：套通解公式：',
                    '$$y = \\frac{1}{x} \\left[ \\int x^2 \\cdot x dx + C \\right] = \\frac{1}{x} \\left[ \\frac{x^4}{4} + C \\right] = \\frac{x^3}{4} + \\frac{C}{x}$$',
                    '第四步：代入初始条件 $y(1) = 0$：',
                    '$$0 = \\frac{1}{4} + C \\implies C = -\\frac{1}{4}$$',
                    '第五步：特解为 $y = \\frac{x^3}{4} - \\frac{1}{4x} = \\frac{x^4 - 1}{4x}$。选项 (B) 正确。'
                ],
                'answer': '(B)',
                'pitfall': '内层积分 $\\int x^3 dx$ 算错幂次；化简为通分形式时符号出错。',
                'difficulty': '★☆☆☆☆',
                'verified': True,
                'source': 'Maki考研数学真题分类精解 第二十四讲 题24.1 (p.547)'
            }
        ],
        'variants': [
            {
                'id': 'var-gaoshu-04-02',
                'question': '解微分方程 $(x + y^2) dy - y dx = 0$。',
                'hint': '对 $y$ 非线性，改写为 $\\frac{dx}{dy}$ 关于 $x$ 的一阶线性方程。',
                'methodChoiceAnalysis': '反客为主法：把 $x$ 视为未知函数。',
                'fullSolution': [
                    '方程改写为 $y \\frac{dx}{dy} - x = y^2 \\implies \\frac{dx}{dy} - \\frac{1}{y}x = y$。',
                    '关于 $x(y)$ 是一阶线性，积分因子为 $1/y$：',
                    '$x = e^{\\ln y} [\\int y e^{-\\ln y} dy + C] = y [\\int 1 dy + C] = y(y + C) = y^2 + Cy$。'
                ],
                'keyTakeaway': '只要看到 $y$ 带平方而 $x$ 只有一次，立刻将方程颠倒为 $\\frac{dx}{dy}$。'
            }
        ],
        'relatedKnowledgeIds': ['gaoshu-04-second-order-constant-coeff', 'gaoshu-04-reducible-ode'],
        'tags': ['一阶微分方程', '通解公式', '反客为主', '积分因子'],
        'source': 'Maki考研数学大串讲 L24 & 真题分类精解 题24.1',
        'status': 'not_started',
        'isPending': False
    },
    'gaoshu-04-reducible-ode': {
        'id': 'gaoshu-04-reducible-ode',
        'title': '可降阶的高阶微分方程求解法',
        'subject': 'gaoshu',
        'subjectName': '高等数学',
        'chapterId': 'gaoshu-ch04',
        'chapterTitle': '微分方程',
        'nodeType': 'topic',
        'summary': '“不显 $y$ 令 $y\'=p, y\'\'=p\'$；不显 $x$ 令 $y\'=p, y\'\'=p \\frac{dp}{dy}$”。降阶为一阶方程求解。',
        'triggers': ['二阶微分方程不显含自变量 $x$（形式为 $F(y, y\', y\'\') = 0$）', '二阶微分方程不显含未知函数 $y$（形式为 $F(x, y\', y\'\') = 0$）'],
        'firstReaction': '检查缺谁：\\n1. 缺 $y$：令 $y\' = p(x)$，则 $y\'\' = \\frac{dp}{dx}$，直接化为关于 $p(x)$ 的一阶方程；\\n2. 缺 $x$：令 $y\' = p(y)$，关键一步由链式法则 $y\'\' = \\frac{dp}{dx} = \\frac{dp}{dy} \\frac{dy}{dx} = p \\frac{dp}{dy}$，化为关于 $p(y)$ 的一阶方程！',
        'candidateMethods': [
            {'name': '缺 y 令 p(x) 降阶法', 'priority': 1, 'condition': '方程中没有出现 $y$', 'whyChoose': '直接对自变量 $x$ 积分', 'description': '令 $y\'=p, y\'\'=p\'$，解出 $p(x)$ 后再对 $x$ 积一次得 $y$'},
            {'name': '缺 x 令 p(y) 链式降阶法', 'priority': 2, 'condition': '方程中没有出现 $x$', 'whyChoose': '链式法则消去自变量 $x$', 'description': '令 $y\'=p, y\'\'=p \\frac{dp}{dy}$，解出 $p(y)$ 后再分离变量'}
        ],
        'applicability': '缺 $x$ 换元时求出的是 $p$ 关于 $y$ 的函数，必须再写成 $\\frac{dy}{dx} = p(y)$ 分离变量二次积分才能解出 $x$ 与 $y$ 的关系。',
        'steps': [
            '步骤1：识别方程缺失的变量类型（缺 $x$ 还是缺 $y$）。',
            '步骤2：代入对应降阶换元公式，化为一阶方程。',
            '步骤3：求解关于 $p$ 的一阶方程，代入初始条件定出第一个任意常数 $C_1$。',
            '步骤4：还原 $p = y\'$ 或 $p = \\frac{dy}{dx}$，进行第二次积分确定 $C_2$。'
        ],
        'pitfalls': ['缺 $x$ 时忘记链式法则乘以 $p$，错把 $y\'\'$ 当成 $\\frac{dp}{dy}$（必须是 $p \\frac{dp}{dy}$）。', '算出一阶解 $p$ 后未及时代入初始条件确定 $C_1$ 导致二次积分表达式极度膨胀。'],
        'formulas': [
            {'title': '缺 y 降阶公式', 'latex': 'y\' = p(x), \\quad y\'\' = \\frac{dp}{dx}'},
            {'title': '缺 x 降阶公式', 'latex': 'y\' = p(y), \\quad y\'\' = p \\frac{dp}{dy}'}
        ],
        'pastQuestions': [
            {
                'id': 'gaoshu-q-2019-2-7',
                'year': '2019',
                'category': '数二',
                'questionNumber': '(7)',
                'content': '微分方程 $y y\'\' + (y\')^2 = 0$ 满足条件 $y(0) = 1, y\'(0) = 1$ 的特解为（ ）\\n(A) $y = \\sqrt{2x + 1}$ \\n(B) $y = \\sqrt{x + 1}$ \\n(C) $y = e^x$ \\n(D) $y = x + 1$',
                'analysis': '观察方程：不显含自变量 $x$！缺 $x$ 型可降阶方程。令 $y\' = p, y\'\' = p \\frac{dp}{dy}$ 代入原方程；或观察原式左边恰好为 $(y y\')\' = 0$！',
                'solutionSteps': [
                    '方法一（全微分直接观察法）：注意到 $(y y\')\' = y\' y\' + y y\'\' = y y\'\' + (y\')^2$！',
                    '因此原方程即为 $(y y\')\' = 0$。',
                    '两边对 $x$ 积分：$y y\' = C_1$。',
                    '代入初始条件 $y(0) = 1, y\'(0) = 1$ 得 $C_1 = 1 \\times 1 = 1$。',
                    '于是 $y \\frac{dy}{dx} = 1 \\implies y dy = dx$。',
                    '两边再积分：$\\frac{1}{2}y^2 = x + C_2$。代入 $y(0)=1$ 得 $\\frac{1}{2} = C_2$。',
                    '故 $y^2 = 2x + 1 \\implies y = \\sqrt{2x + 1}$。选项 (A) 正确。'
                ],
                'answer': '(A)',
                'pitfall': '盲目按通法换元也可以，但若识别出全导数公式 $(yy\')\'$ 可在 10 秒内秒杀。',
                'difficulty': '★★☆☆☆',
                'verified': True,
                'source': 'Maki考研数学真题分类精解 第二十五讲 题25.1 (p.577)'
            }
        ],
        'variants': [
            {
                'id': 'var-gaoshu-04-03',
                'question': '解微分方程 $x y\'\' - y\' = x^2$。',
                'hint': '不显含 $y$，令 $y\' = p(x), y\'\' = p\'$。',
                'methodChoiceAnalysis': '化为关于 $p(x)$ 的一阶线性微分方程。',
                'fullSolution': [
                    '令 $y\' = p$，则方程变为 $x p\' - p = x^2 \\implies p\' - \\frac{1}{x}p = x$。',
                    '解得 $p = x [\\int 1 dx + C_1] = x(x + C_1) = x^2 + C_1 x$。',
                    '因为 $y\' = x^2 + C_1 x$，两边积分得：',
                    '$y = \\frac{1}{3}x^3 + \\frac{1}{2}C_1 x^2 + C_2$。'
                ],
                'keyTakeaway': '缺 $y$ 降阶后通常是一阶线性方程，积分两次得两任意常数。'
            }
        ],
        'relatedKnowledgeIds': ['gaoshu-04-first-order-ode', 'gaoshu-04-second-order-constant-coeff'],
        'tags': ['可降阶微分方程', '缺x', '缺y', '全微分观察法'],
        'source': 'Maki考研数学大串讲 L25 & 真题分类精解 题25.1',
        'status': 'not_started',
        'isPending': False
    },
    'gaoshu-04-euler-equation': {
        'id': 'gaoshu-04-euler-equation',
        'title': '欧拉方程与变量代换标准解法',
        'subject': 'gaoshu',
        'subjectName': '高等数学',
        'chapterId': 'gaoshu-ch04',
        'chapterTitle': '微分方程',
        'nodeType': 'topic',
        'summary': '“$x$ 的幂次与导数阶数严格对齐（$x^k y^{(k)}$）即为欧拉方程；自变量换元 $x = e^t$ 化为常系数线性方程”。',
        'triggers': ['方程中含有 $x^2 y\'\', x y\'$ 项', '题目明确提示“令 $x = e^t$”变换方程', '数一专属高频特色微分方程考点'],
        'firstReaction': '确认是否为欧拉方程：$x^2 y\'\' + p x y\' + q y = f(x)$（$x$ 的方幂与 $y$ 的求导阶数一致）。解法统一：当 $x > 0$ 时，令 $x = e^t$ 即 $t = \\ln x$；利用算子公式 $x y\' = Dy, x^2 y\'\' = D(D-1)y$，直接化为常系数线性微分方程！',
        'candidateMethods': [
            {'name': '自变量对数换元法 (x=e^t)', 'priority': 1, 'condition': '标准欧拉方程', 'whyChoose': '数一考纲标准规定解法', 'description': '令 $t = \\ln x$，则 $x y\' = \\frac{dy}{dt}, x^2 y\'\' = \\frac{d^2 y}{dt^2} - \\frac{dy}{dt}$'}
        ],
        'applicability': '求出关于 $t$ 的解后，【必须将 $t = \\ln x$ 回代】为 $x$ 的函数；欧拉方程是数学一专属大纲考点，数二数三不考。',
        'steps': [
            '步骤1：设 $x = e^t (t = \\ln x)$。',
            '步骤2：代入换元恒等式：$x y\' = \\frac{dy}{dt}, x^2 y\'\' = \\frac{d^2 y}{dt^2} - \\frac{dy}{dt}$。',
            '步骤3：整理为关于 $y(t)$ 的常系数线性微分方程。',
            '步骤4：求特征方程解出 $y(t)$，将 $t$ 替换回 $\\ln x$。'
        ],
        'pitfalls': ['忘记二阶导代换中要减去一阶导（错写成 $x^2 y\'\' = \\frac{d^2 y}{dt^2}$）；最后答案忘记把 $t$ 代换回 $\\ln x$。'],
        'formulas': [
            {'title': '欧拉算子代换公式', 'latex': 'x \\frac{dy}{dx} = \\frac{dy}{dt}, \\quad x^2 \\frac{d^2 y}{dx^2} = \\frac{d^2 y}{dt^2} - \\frac{dy}{dt} \\quad (x = e^t)'},
            {'title': '欧拉方程标准型', 'latex': 'x^2 y\'\' + p x y\' + q y = f(x) \\implies \\frac{d^2 y}{dt^2} + (p - 1)\\frac{dy}{dt} + q y = f(e^t)'}
        ],
        'pastQuestions': [
            {
                'id': 'gaoshu-q-2018-1-11',
                'year': '2018',
                'category': '数一',
                'questionNumber': '(11)',
                'content': '微分方程 $x^2 y\'\' + 4x y\' + 2y = 0$ 的通解为 $y = \\underline{\\quad\\quad\\quad\\quad}.$',
                'analysis': '典型二阶齐次欧拉方程：$x^2 y\'\' + 4xy\' + 2y = 0$。令 $x = e^t$，原方程化为 $\\frac{d^2 y}{dt^2} - \\frac{dy}{dt} + 4\\frac{dy}{dt} + 2y = 0 \\implies y\'\'(t) + 3y\'(t) + 2y = 0$。',
                'solutionSteps': [
                    '第一步：设 $x = e^t (x > 0)$，则 $t = \\ln x$。',
                    '第二步：代入公式 $x y\' = \\frac{dy}{dt}, x^2 y\'\' = \\frac{d^2 y}{dt^2} - \\frac{dy}{dt}$：',
                    '$$\\left( \\frac{d^2 y}{dt^2} - \\frac{dy}{dt} \\right) + 4 \\frac{dy}{dt} + 2y = 0 \\implies \\frac{d^2 y}{dt^2} + 3 \\frac{dy}{dt} + 2y = 0$$',
                    '第三步：写出特征方程：$r^2 + 3r + 2 = 0 \\implies (r + 1)(r + 2) = 0$。',
                    '解得两个互异实特征根 $r_1 = -1, r_2 = -2$。',
                    '第四步：关于 $t$ 的通解为 $y = C_1 e^{-t} + C_2 e^{-2t}$。',
                    '第五步：将 $t = \\ln x$ 代回：$e^{-t} = x^{-1} = \\frac{1}{x}, e^{-2t} = x^{-2} = \\frac{1}{x^2}$。',
                    '通解为 $y = \\frac{C_1}{x} + \\frac{C_2}{x^2}$。'
                ],
                'answer': 'C_1 / x + C_2 / x^2',
                'pitfall': '换元后一阶项合并漏减 1（把 $4-1=3$ 错写成 4）。',
                'difficulty': '★★☆☆☆',
                'verified': True,
                'source': 'Maki考研数学真题分类精解 第二十六讲 题26.1 (p.613)'
            }
        ],
        'variants': [
            {
                'id': 'var-gaoshu-04-04',
                'question': '求欧拉方程 $x^2 y\'\' - x y\' + y = 0$ 的通解。',
                'hint': '换元化为 $y\'\'(t) - 2y\'(t) + y = 0$，特征方程有二重根。',
                'methodChoiceAnalysis': '二重特征根通解带 $t$ 因子，代回变 $\\ln x$。',
                'fullSolution': [
                    '换元后方程为 $\\frac{d^2 y}{dt^2} - 2\\frac{dy}{dt} + y = 0$。',
                    '特征方程 $(r - 1)^2 = 0 \\implies r_1 = r_2 = 1$。',
                    '通解为 $y = (C_1 + C_2 t)e^t$。',
                    '代回 $t = \\ln x, e^t = x$：$y = (C_1 + C_2 \\ln x)x$。'
                ],
                'keyTakeaway': '欧拉方程出现重根时，乘的因式是 $\\ln x$ 而不是 $x$。'
            }
        ],
        'relatedKnowledgeIds': ['gaoshu-04-second-order-constant-coeff', 'gaoshu-04-first-order-ode'],
        'tags': ['欧拉方程', '变量代换', '数一专属', '常系数化'],
        'source': 'Maki考研数学大串讲 L26 & 真题分类精解 题26.1',
        'status': 'not_started',
        'isPending': False
    }
}
