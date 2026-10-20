# -*- coding: utf-8 -*-
"""
Gaoshu Part 2 (Chapters 5 to 7 topics)
Authentic past exam questions from Maki考研数学真题分类精解 (L29-L37)
"""

GAOSHU_PART2_TOPICS = {
    'gaoshu-05-differentiability-concept': {
        'id': 'gaoshu-05-differentiability-concept',
        'title': '多元函数连续、偏导存在与可微性判定',
        'subject': 'gaoshu',
        'subjectName': '高等数学',
        'chapterId': 'gaoshu-ch05',
        'chapterTitle': '多元函数微分学',
        'nodeType': 'topic',
        'summary': '“偏导连续必可微，可微必偏导且连续，偏导存在与连续互不相推；可微判别用定义极限式”。',
        'triggers': ['讨论分段多元函数在原点 $(0, 0)$ 的连续性、偏导数与可微性', '概念选择题判断多元微分各性质真假命题'],
        'firstReaction': '画逻辑关系图：偏导连续 $\\implies$ 可微 $\\implies$ (连续 且 偏导存在)；判定在 $(0, 0)$ 是否可微必须按定义验证极限：$\\lim_{\\Delta x, \\Delta y \\to 0} \\frac{\\Delta z - [f_x(0,0)\\Delta x + f_y(0,0)\\Delta y]}{\\sqrt{\\Delta x^2 + \\Delta y^2}} = 0$！',
        'candidateMethods': [
            {'name': '可微性定义极限检验法', 'priority': 1, 'condition': '在分段点或特殊点判定可微性', 'whyChoose': '不可用充分条件判定时唯一的充要裁决法', 'description': '算偏导数后代入 $\\frac{\\Delta z - A\\Delta x - B\\Delta y}{\\rho} \\to 0$ 极限式'}
        ],
        'applicability': '两个偏导数存在绝不能推出可微，甚至不能推出连续！可微极限分母必须是 $\\rho = \\sqrt{\\Delta x^2 + \\Delta y^2}$。',
        'steps': [
            '步骤1：按一元导数定义分别计算偏导数 $f_x(0, 0) = \\lim_{x \\to 0} \\frac{f(x, 0) - f(0, 0)}{x}$ 与 $f_y(0, 0)$。',
            '步骤2：写出全增量 $\\Delta z = f(\\Delta x, \\Delta y) - f(0, 0)$ 和线性主部 $A\\Delta x + B\\Delta y$。',
            '步骤3：计算极限 $\\lim_{(\\Delta x, \\Delta y) \\to (0, 0)} \\frac{\\Delta z - (A\\Delta x + B\\Delta y)}{\\sqrt{\\Delta x^2 + \\Delta y^2}}$。',
            '步骤4：极限为 0 则可微，不为 0 或不存在则不可微。'
        ],
        'pitfalls': ['求 $(0,0)$ 处偏导数用求导公式代入（在分段点必须用定义式）；误以为偏导数存在就一定连续。'],
        'formulas': [
            {'title': '可微充要条件极限式', 'latex': '\\lim_{(\\Delta x, \\Delta y) \\to (0, 0)} \\frac{f(x_0+\\Delta x, y_0+\\Delta y) - f(x_0, y_0) - f_x(x_0, y_0)\\Delta x - f_y(x_0, y_0)\\Delta y}{\\sqrt{\\Delta x^2 + \\Delta y^2}} = 0'},
            {'title': '偏导数定义', 'latex': 'f_x(x_0, y_0) = \\lim_{\\Delta x \\to 0} \\frac{f(x_0+\\Delta x, y_0) - f(x_0, y_0)}{\\Delta x}'}
        ],
        'pastQuestions': [
            {
                'id': 'gaoshu-q-2014-1-2',
                'year': '2014',
                'category': '数一',
                'questionNumber': '(2)',
                'content': '设函数 $f(x, y) = \\begin{cases} \\frac{x y}{\\sqrt{x^2 + y^2}}, & x^2 + y^2 \\neq 0 \\\\ 0, & x^2 + y^2 = 0 \\end{cases}$，则 $f(x, y)$ 在 $(0, 0)$ 处（ ）\\n(A) 连续且可微 \\n(B) 连续且偏导数存在，但不可微 \\n(C) 连续但偏导数不存在 \\n(D) 不连续',
                'analysis': '极坐标代入检验连续性：$f(r\\cos\\theta, r\\sin\\theta) = r\\cos\\theta\\sin\\theta \\to 0$，连续；沿坐标轴算偏导 $f(x, 0)=0 \\implies f_x(0,0)=0, f_y(0,0)=0$；检验可微性极限 $\\frac{xy}{\\rho \\cdot \\rho} = \\cos\\theta\\sin\\theta$ 与 $\\theta$ 有关不存在！',
                'solutionSteps': [
                    '第一步（连续性）：当 $(x, y) \\to (0, 0)$ 时，$|f(x, y)| = \\frac{|x||y|}{\\sqrt{x^2+y^2}} \\le \\frac{x^2+y^2}{2\\sqrt{x^2+y^2}} = \\frac{1}{2}\\sqrt{x^2+y^2} \\to 0$。',
                    '极限等于 $f(0, 0) = 0$，故函数在 $(0, 0)$ 处连续。',
                    '第二步（偏导数）：$f_x(0, 0) = \\lim_{x \\to 0} \\frac{f(x, 0) - 0}{x} = \\lim_{x \\to 0} \\frac{0}{x} = 0$。同理 $f_y(0, 0) = 0$。偏导数存在。',
                    '第三步（可微性）：考察极限 $\\lim_{(\\Delta x, \\Delta y) \\to (0, 0)} \\frac{f(\\Delta x, \\Delta y) - 0 - 0\\cdot\\Delta x - 0\\cdot\\Delta y}{\\sqrt{\\Delta x^2 + \\Delta y^2}}$。',
                    '$$= \\lim \\frac{\\Delta x \\Delta y}{\\Delta x^2 + \\Delta y^2}$$',
                    '令 $\\Delta y = k \\Delta x$，极限为 $\\frac{k}{1+k^2}$，随斜率 $k$ 改变，极限不存在！故不可微。选项 (B) 正确。'
                ],
                'answer': '(B)',
                'pitfall': '可微极限分子分母都是二次项，比值不为 0；必须严格判定极限是否恒为 0。',
                'difficulty': '★★★☆☆',
                'verified': True,
                'source': 'Maki考研数学真题分类精解 第二十九讲 题29.1 (p.648)'
            }
        ],
        'variants': [
            {
                'id': 'var-gaoshu-05-01',
                'question': '讨论函数 $f(x, y) = \\sqrt{|xy|}$ 在 $(0, 0)$ 处的可微性。',
                'hint': '偏导数均为 0，检验极限 $\\frac{\\sqrt{|\\Delta x \\Delta y|}}{\\sqrt{\\Delta x^2+\\Delta y^2}}$。',
                'methodChoiceAnalysis': '沿直线 $\\Delta y = \\Delta x$ 趋于 0，比值为 $1/\\sqrt{2} \\neq 0$。',
                'fullSolution': [
                    '$f_x(0, 0) = 0, f_y(0, 0) = 0$。',
                    '极限为 $\\lim \\frac{\\sqrt{|\\Delta x \\Delta y|}}{\\sqrt{\\Delta x^2+\\Delta y^2}}$。',
                    '沿 $\\Delta y = \\Delta x$ 趋近时，比值为 $\\frac{|\\Delta x|}{\\sqrt{2}|\\Delta x|} = \\frac{1}{\\sqrt{2}} \\neq 0$。',
                    '因此在 $(0, 0)$ 处不可微。'
                ],
                'keyTakeaway': '只要比值极限在某一方向不等于 0，即可断言不可微。'
            }
        ],
        'relatedKnowledgeIds': ['gaoshu-05-chain-rule-composite', 'gaoshu-01-discontinuity-points'],
        'tags': ['可微性', '偏导数定义', '连续性', '多元微分概念'],
        'source': 'Maki考研数学大串讲 L29 & 真题分类精解 题29.1',
        'status': 'not_started',
        'isPending': False
    },
    'gaoshu-05-chain-rule-composite': {
        'id': 'gaoshu-05-chain-rule-composite',
        'title': '多元复合函数偏导数与全微分链式法则',
        'subject': 'gaoshu',
        'subjectName': '高等数学',
        'chapterId': 'gaoshu-ch05',
        'chapterTitle': '多元函数微分学',
        'nodeType': 'topic',
        'summary': '“画树状结构图，分清自变量、中间变量与因变量；连线相乘分叉相加；全微分形式不变性”。',
        'triggers': ['求抽象复合函数 $z = f(u, v)$ 的偏导数 $\\frac{\\partial z}{\\partial x}$ 与高阶二阶偏导 $\\frac{\\partial^2 z}{\\partial x^2}$', '坐标变换下的二阶偏微分方程化简'],
        'firstReaction': '画变量结构树：自变量（底端 $x, y$） $\\to$ 中间变量（中层 $u, v$） $\\to$ 因变量（顶端 $z$）；求一阶导：“自顶向下，沿线乘，分叉加”；求二阶导注意乘积法则，且 $f_u\'$ 本身依然是关于中间变量 $u, v$ 的复合函数，必须再次套链式法则！',
        'candidateMethods': [
            {'name': '树状结构链式法则', 'priority': 1, 'condition': '复合偏导求解', 'whyChoose': '条理清晰，杜绝遗漏交叉分支', 'description': '$\\frac{\\partial z}{\\partial x} = f_u\' \\frac{\\partial u}{\\partial x} + f_v\' \\frac{\\partial v}{\\partial x}$'},
            {'name': '全微分形式不变性法', 'priority': 2, 'condition': '求全微分或隐函数偏导', 'whyChoose': '两边直接做微分 $d$，避免分别求偏导', 'description': '$dz = f_u\' du + f_v\' dv$'}
        ],
        'applicability': '求二阶混合偏导数时，若二阶偏导连续则有 $f_{uv}\'\' = f_{vu}\'\'$；对中间变量再次求导时千万不能把 $f_u\'$ 当作常数。',
        'steps': [
            '步骤1：明确画出函数与自变量间的依赖树状关系。',
            '步骤2：写出一阶偏导表达式。',
            '步骤3：求二阶偏导时，先按乘积法则展开，再对 $f_u\', f_v\'$ 逐个展开二次复合。',
            '步骤4：合并同类项（利用 $f_{uv}\'\' = f_{vu}\'\'$）。'
        ],
        'pitfalls': ['求二阶导 $\\frac{\\partial}{\\partial x}(f_u\')$ 时忘记链式展开，错写成 $f_{uu}\'\'$（漏了 $f_{uv}\'\' \\frac{\\partial v}{\\partial x}$ 项）。'],
        'formulas': [
            {'title': '多元复合一阶链式法则', 'latex': '\\frac{\\partial z}{\\partial x} = \\frac{\\partial z}{\\partial u} \\frac{\\partial u}{\\partial x} + \\frac{\\partial z}{\\partial v} \\frac{\\partial v}{\\partial x}'},
            {'title': '全微分形式不变性', 'latex': 'dz = A dx + B dy = f_1\' du + f_2\' dv'}
        ],
        'pastQuestions': [
            {
                'id': 'gaoshu-q-2021-1-10',
                'year': '2021',
                'category': '数一',
                'questionNumber': '(10)',
                'content': '设 $z = f(x+y, x-y, xy)$，其中 $f$ 具有二阶连续偏导数，则 $dz = \\underline{\\quad\\quad\\quad\\quad}.$',
                'analysis': '利用全微分形式不变性！令 $u = x+y, v = x-y, w = xy$。则 $dz = f_1\' du + f_2\' dv + f_3\' dw$。直接将 $du = dx+dy, dv = dx-dy, dw = y dx + x dy$ 代入合并。',
                'solutionSteps': [
                    '第一步：设 $u = x+y, v = x-y, w = xy$。',
                    '第二步：由全微分形式不变性：$dz = f_1\' du + f_2\' dv + f_3\' dw$。',
                    '第三步：分别计算自变量微分：',
                    '$du = dx + dy, \\quad dv = dx - dy, \\quad dw = y dx + x dy$。',
                    '第四步：代入并按 $dx, dy$ 合并同类项：',
                    '$$dz = f_1\'(dx + dy) + f_2\'(dx - dy) + f_3\'(y dx + x dy)$$',
                    '$$= (f_1\' + f_2\' + y f_3\') dx + (f_1\' - f_2\' + x f_3\') dy$$'
                ],
                'answer': '(f_1\' + f_2\' + y f_3\')dx + (f_1\' - f_2\' + x f_3\')dy',
                'pitfall': '分别去求偏导数 $\\frac{\\partial z}{\\partial x}$ 与 $\\frac{\\partial z}{\\partial y}$ 容易漏项；全微分微分形式不变性一步合并。',
                'difficulty': '★★☆☆☆',
                'verified': True,
                'source': 'Maki考研数学真题分类精解 第三十讲 题30.1 (p.674)'
            }
        ],
        'variants': [
            {
                'id': 'var-gaoshu-05-02',
                'question': '设 $z = f(x^2 - y^2)$，求 $\\frac{\\partial^2 z}{\\partial x \\partial y}$。',
                'hint': '令 $u = x^2 - y^2$，一阶偏导为 $z_x\' = f\'(u) \\cdot 2x$。',
                'methodChoiceAnalysis': '乘积法则加链式法则。',
                'fullSolution': [
                    '$z_x\' = 2x f\'(u)$。',
                    '对 $y$ 求偏导：$z_{xy}\'\' = 2x \\frac{\\partial}{\\partial y}[f\'(u)] = 2x [f\'\'(u) \\frac{\\partial u}{\\partial y}] = 2x [f\'\'(u) (-2y)] = -4xy f\'\'(x^2 - y^2)$。'
                ],
                'keyTakeaway': '求偏导时非求导变量直接看作常数。'
            }
        ],
        'relatedKnowledgeIds': ['gaoshu-05-implicit-function-differentiation', 'gaoshu-05-differentiability-concept'],
        'tags': ['链式法则', '全微分形式不变性', '树状图', '二阶偏导'],
        'source': 'Maki考研数学大串讲 L30 & 真题分类精解 题30.1',
        'status': 'not_started',
        'isPending': False
    },
    'gaoshu-05-implicit-function-differentiation': {
        'id': 'gaoshu-05-implicit-function-differentiation',
        'title': '隐函数求导公式法与方程组全微分法',
        'subject': 'gaoshu',
        'subjectName': '高等数学',
        'chapterId': 'gaoshu-ch05',
        'chapterTitle': '多元函数微分学',
        'nodeType': 'topic',
        'summary': '“隐函数求导三路径：公式法 $\\frac{\\partial z}{\\partial x} = -\\frac{F_x}{F_z}$；两边直接求导法；两边求微分 $d$ 消元”。方程组用全微分联立最稳妥。',
        'triggers': ['给出方程 $F(x, y, z) = 0$ 确定隐函数 $z = z(x, y)$ 求偏导', '由方程组 $\\begin{cases} F(x, y, u, v) = 0 \\\\ G(x, y, u, v) = 0 \\end{cases}$ 确定隐函数', '求隐函数的极值点'],
        'firstReaction': '单个隐函数首选公式法：$\\frac{\\partial z}{\\partial x} = -\\frac{F_x\'}{F_z\'}, \\frac{\\partial z}{\\partial y} = -\\frac{F_y\'}{F_z\'}$（负号与分母 $F_z\'$ 刻在骨髓里！）；隐函数方程组果断两边直接取微分 $d$，化为关于 $du, dv$ 的二元一次线性方程组用消元法求解。',
        'candidateMethods': [
            {'name': '隐函数偏导公式法', 'priority': 1, 'condition': '单一隐函数方程 $F(x, y, z)=0$', 'whyChoose': '直接偏导比值加负号', 'description': '$\\frac{\\partial z}{\\partial x} = -\\frac{F_x}{F_z}$'},
            {'name': '方程组全微分消元法', 'priority': 2, 'condition': '方程组确定多元隐函数', 'whyChoose': '把复杂的雅可比行列式转化为代数消元', 'description': '两边求微分 $d$，解关于 $du, dv$ 的线性方程组'}
        ],
        'applicability': '使用公式法分母偏导数 $F_z\' \\neq 0$；求二阶导时建议用两边直接求导法，比对公式商式再求导更不易出错。',
        'steps': [
            '步骤1：移项将方程写为 $F(x, y, z) = 0$。',
            '步骤2：分别将 $x, y, z$ 视为自变量求偏导 $F_x\', F_y\', F_z\'$。',
            '步骤3：代入公式写出偏导数；若求某点具体值，先将该点坐标代入求出偏导数值。'
        ],
        'pitfalls': ['公式中的负号遗漏；求 $F_x\'$ 时误把 $z$ 看作关于 $x$ 的函数（求大 $F$ 偏导时 $x, y, z$ 三者完全独立平等！）。'],
        'formulas': [
            {'title': '单方程隐函数导数公式', 'latex': '\\frac{\\partial z}{\\partial x} = -\\frac{F_x\'}{F_z\'}, \\quad \\frac{\\partial z}{\\partial y} = -\\frac{F_y\'}{F_z\'}'},
            {'title': '雅可比行列式公式', 'latex': '\\frac{\\partial(u, v)}{\\partial(x, y)} = \\begin{vmatrix} u_x & u_y \\\\ v_x & v_y \\end{vmatrix}'}
        ],
        'pastQuestions': [
            {
                'id': 'gaoshu-q-2023-1-17',
                'year': '2023',
                'category': '数一',
                'questionNumber': '(17)',
                'content': '设函数 $z = z(x, y)$ 由方程 $x^2 + 2y^2 + 3z^2 + xy - z - 9 = 0$ 确定。\\n(I) 求 $z = z(x, y)$ 的极值点；\\n(II) 判断极值点的极大值或极小值类型。',
                'analysis': '隐函数极值必要条件：偏导数为 0！由公式 $\\frac{\\partial z}{\\partial x} = -\\frac{F_x}{F_z} = 0 \\implies F_x = 0$；$\\frac{\\partial z}{\\partial y} = -\\frac{F_y}{F_z} = 0 \\implies F_y = 0$。联立 $F_x=0, F_y=0$ 与原方程求驻点；再求二阶偏导判别 $AC - B^2$。',
                'solutionSteps': [
                    '第一步：设 $F(x, y, z) = x^2 + 2y^2 + 3z^2 + xy - z - 9 = 0$。',
                    '由隐函数极值必要条件，极值点处必须满足：',
                    '$$F_x\' = 2x + y = 0, \\quad F_y\' = 4y + x = 0$$',
                    '第二步：解线性方程组 $\\begin{cases} 2x + y = 0 \\\\ x + 4y = 0 \\end{cases} \\implies x = 0, y = 0$。',
                    '第三步：将 $x=0, y=0$ 代入原方程：$3z^2 - z - 9 = 0$。',
                    '解得 $z = \\frac{1 \\pm \\sqrt{109}}{6}$。',
                    '第四步：由极值判别法计算二阶导：$A = z_{xx}\'\' = -\\frac{F_{xx}}{F_z} = -\\frac{2}{6z-1}$，$C = z_{yy}\'\' = -\\frac{4}{6z-1}$，$B = z_{xy}\'\' = -\\frac{1}{6z-1}$。',
                    '$$AC - B^2 = \\frac{8 - 1}{(6z-1)^2} = \\frac{7}{(6z-1)^2} > 0$$',
                    '第五步：当 $z = \\frac{1+\\sqrt{109}}{6}$ 时，$6z-1 = \\sqrt{109} > 0$，故 $A < 0$，取得极大值；',
                    '当 $z = \\frac{1-\\sqrt{109}}{6}$ 时，$6z-1 = -\\sqrt{109} < 0$，故 $A > 0$，取得极小值。'
                ],
                'answer': '(0, 0) 处分别取极大值与极小值',
                'pitfall': '解出 $x, y$ 忘了代回原方程求对应的 $z$；隐函数二阶导符号判定算错。',
                'difficulty': '★★★★☆',
                'verified': True,
                'source': 'Maki考研数学真题分类精解 第三十讲 题30.4 (p.710)'
            }
        ],
        'variants': [
            {
                'id': 'var-gaoshu-05-03',
                'question': '设 $e^z - x y z = 0$，求 $\\frac{\\partial z}{\\partial x}$。',
                'hint': '设 $F(x, y, z) = e^z - x y z = 0$ 套公式。',
                'methodChoiceAnalysis': '$F_x\' = -yz, F_z\' = e^z - xy$。',
                'fullSolution': [
                    '$\\frac{\\partial z}{\\partial x} = -\\frac{F_x\'}{F_z\'} = -\\frac{-yz}{e^z - xy} = \\frac{yz}{e^z - xy}$。'
                ],
                'keyTakeaway': '求大 F 偏导时各变量互为独立常数看待。'
            }
        ],
        'relatedKnowledgeIds': ['gaoshu-05-chain-rule-composite', 'gaoshu-05-lagrange-multipliers'],
        'tags': ['隐函数求导', '公式法', '隐函数极值', 'AC-B^2'],
        'source': 'Maki考研数学大串讲 L30 & 真题分类精解 题30.4',
        'status': 'not_started',
        'isPending': False
    },
    'gaoshu-05-lagrange-multipliers': {
        'id': 'gaoshu-05-lagrange-multipliers',
        'title': '多元极值、条件极值与拉格朗日乘数法',
        'subject': 'gaoshu',
        'subjectName': '高等数学',
        'chapterId': 'gaoshu-ch05',
        'chapterTitle': '多元函数微分学',
        'nodeType': 'topic',
        'summary': '“无条件看驻点 Hessian 矩阵 ($AC-B^2$)；条件极值构造辅助函数 $L = f + \\lambda g$ 偏导全置零；最值比较驻点与边界”。',
        'triggers': ['求函数 $f(x, y, z)$ 在约束条件 $g(x, y, z) = 0$ 下的最值', '空间曲面上点到平面或直线的最小距离', '闭区域上的最大值与最小值'],
        'firstReaction': '有约束必设拉格朗日函数 $L(x, y, z, \\lambda) = f(x, y, z) + \\lambda g(x, y, z)$；对 $x, y, z, \\lambda$ 分别求偏导令等于零解方程组；解方程组第一技巧：先消去乘子 $\\lambda$（用比值消去法），建立自变量之间的等式关系！',
        'candidateMethods': [
            {'name': '拉格朗日乘数法', 'priority': 1, 'condition': '带等式约束的极值最值问题', 'whyChoose': '标准解法，将几何约束转化为无约束梯度平行', 'description': '$\\nabla f + \\lambda \\nabla g = 0$ 联立方程组求解'},
            {'name': '无条件极值二阶充分条件', 'priority': 2, 'condition': '开区域内部求极值', 'whyChoose': '判别式判定极值类型', 'description': '$A = f_{xx}, B = f_{xy}, C = f_{yy}$；若 $AC-B^2>0$ 且 $A<0$ 极大，A>0 极小'}
        ],
        'applicability': '求出的驻点坐标必须满足约束条件；若在有界闭区域上求最值，只需比较区域内部驻点与边界上的所有极值点和端点，最大者即最大值，无需验证充分条件。',
        'steps': [
            '步骤1：列出目标函数 $f(x, y, z)$ 与约束条件 $g(x, y, z) = 0$。',
            '步骤2：构造辅助函数 $L = f + \\lambda g$。',
            '步骤3：求所有偏导数令为 0，消去 $\\lambda$ 求出驻点。',
            '步骤4：将驻点代回目标函数算函数值，与几何实际或边界值比较定最值。'
        ],
        'pitfalls': ['解拉格朗日非线性方程组时死算硬解；应优先用前两个偏导数相除消去 $\\lambda$；忘记验证约束条件。'],
        'formulas': [
            {'title': '拉格朗日辅助函数', 'latex': 'L(x, y, z, \\lambda) = f(x, y, z) + \\lambda g(x, y, z)'},
            {'title': '无条件极值判别式', 'latex': '\\Delta = AC - B^2 \\quad \\begin{cases} > 0 \\text{ 且 } A < 0, & \\text{极大值} \\\\ > 0 \\text{ 且 } A > 0, & \\text{极小值} \\\\ < 0, & \\text{非极值 (鞍点)} \\end{cases}'}
        ],
        'pastQuestions': [
            {
                'id': 'gaoshu-q-2020-1-17',
                'year': '2020',
                'category': '数一',
                'questionNumber': '(17)',
                'content': '求函数 $f(x, y, z) = x^2 + y^2 + z^2$ 在约束条件 $\\begin{cases} x + y + z = 1 \\\\ x^2 + y^2 = z \\end{cases}$ 下的最小值。',
                'analysis': '目标函数是原点到空间曲线的距离平方。有两个约束条件！构造拉格朗日乘数函数，引入两个乘子 $\\lambda, \\mu$；或者将第一个约束 $x+y = 1-z$ 代入第二个约束消元简化。',
                'solutionSteps': [
                    '方法（消元与拉格朗日结合）：由约束 $x+y = 1-z$，代入目标函数：',
                    '目标函数 $f = x^2 + y^2 + z^2 = z + z^2$（因为 $x^2+y^2 = z$）！',
                    '奇迹发生：目标函数竟然完全只取决于 $z$！',
                    '第二步：求 $z$ 的取值范围：由柯西不等式 $(x+y)^2 \\le 2(x^2+y^2)$，',
                    '$$(1-z)^2 \\le 2z \\implies 1 - 2z + z^2 \\le 2z \\implies z^2 - 4z + 1 \\le 0$$',
                    '解得 $2 - \\sqrt{3} \\le z \\le 2 + \\sqrt{3}$。',
                    '第三步：令 $g(z) = z^2 + z$。对称轴为 $z = -1/2$。',
                    '在区间 $[2-\\sqrt{3}, 2+\\sqrt{3}]$ 上，$g(z)$ 严格单调递增！',
                    '第四步：因此最小值在左端点 $z = 2 - \\sqrt{3}$ 处取得：',
                    '$$f_{\\min} = (2-\\sqrt{3})^2 + (2-\\sqrt{3}) = 7 - 4\\sqrt{3} + 2 - \\sqrt{3} = 9 - 5\\sqrt{3}$$'
                ],
                'answer': '9 - 5\\sqrt{3}',
                'pitfall': '盲目引入两个乘子列 5 元非线性方程组极难求解；利用几何与代数代换消元实现降维秒杀。',
                'difficulty': '★★★★☆',
                'verified': True,
                'source': 'Maki考研数学真题分类精解 第三十二讲 题32.3 (p.755)'
            }
        ],
        'variants': [
            {
                'id': 'var-gaoshu-05-04',
                'question': '求长方体在表面积为 $S$ 的条件下，体积的最大值。',
                'hint': '设长宽高为 $x, y, z$，$V = xyz$，约束 $2(xy+yz+zx) = S$。',
                'methodChoiceAnalysis': '由对称性或均值不等式，当且仅当立方体 $x=y=z$ 时体积最大。',
                'fullSolution': [
                    '由均值不等式：$S = 2(xy+yz+zx) \\ge 6 (xyz)^{2/3} = 6 V^{2/3}$。',
                    '$V^{2/3} \\le S/6 \\implies V \\le (S/6)^{3/2}$。',
                    '当且仅当 $x = y = z = \\sqrt{S/6}$ 时取等号，最大体积为 $(S/6)^{3/2}$。'
                ],
                'keyTakeaway': '完全对称约束最值题目，等号必在各变量相等时取得。'
            }
        ],
        'relatedKnowledgeIds': ['gaoshu-05-implicit-function-differentiation', 'gaoshu-09-plane-and-line-equations'],
        'tags': ['拉格朗日乘数法', '条件极值', '柯西不等式消元', '二阶充分条件'],
        'source': 'Maki考研数学大串讲 L32 & 真题分类精解 题32.3',
        'status': 'not_started',
        'isPending': False
    },
    'gaoshu-06-double-integral-polar': {
        'id': 'gaoshu-06-double-integral-polar',
        'title': '二重积分直角坐标与极坐标计算、换元积分',
        'subject': 'gaoshu',
        'subjectName': '高等数学',
        'chapterId': 'gaoshu-ch06',
        'chapterTitle': '二重积分与多重积分',
        'nodeType': 'topic',
        'summary': '“圆域扇形含 $x^2+y^2$ 果断极坐标；极坐标面积元素切记带 $r$ ($r dr d\\theta$)”。由内向外定积分限。',
        'triggers': ['积分区域为圆盘、环形、扇形或心形线', '被积函数含有 $x^2+y^2$ 或 $y/x$', '求包含圆周方程的二重积分'],
        'firstReaction': '极坐标口诀：“极点射出穿入穿出定 $r$，扫描夹角定 $\\theta$”；代换公式：$x = r\\cos\\theta, y = r\\sin\\theta, dx dy = r dr d\\theta$；若圆心不在原点（如偏心圆 $(x-a)^2 + y^2 = a^2$），极坐标方程为 $r = 2a\\cos\\theta, -\\pi/2 \\le \\theta \\le \\pi/2$。',
        'candidateMethods': [
            {'name': '极坐标化简积分法', 'priority': 1, 'condition': '圆形区域或被积函数含 $x^2+y^2$', 'whyChoose': '角度与半径完全分离为两个一重积分', 'description': '$\\iint f(x, y)dxdy = \\int_\\alpha^\\beta d\\theta \\int_{r_1(\\theta)}^{r_2(\\theta)} f(r\\cos\\theta, r\\sin\\theta) r dr$'},
            {'name': '直角坐标后积先积切换', 'priority': 2, 'condition': '多项式或容易找原函数的直角区域', 'whyChoose': '根据穿线方便选择 X 型或 Y 型', 'description': 'X型 $\\int dx \\int dy$；Y型 $\\int dy \\int dx$'}
        ],
        'applicability': '极坐标变换面积元素【绝对不能漏乘 $r$】！偏心圆的角度扫描范围必须严格从切线方向看（过原点的偏心圆角度跨度为 $\\pi$ 而不是 $2\\pi$）。',
        'steps': [
            '步骤1：精确画出积分区域 $D$，确定边界曲线极坐标方程。',
            '步骤2：从原点引射线，确定 $\\theta$ 的取值区间 $[\\alpha, \\beta]$。',
            '步骤3：沿射线方向看穿入曲线 $r_1(\\theta)$ 与穿出曲线 $r_2(\\theta)$。',
            '步骤4：代入公式，被积函数乘 $r$ 后完成积分。'
        ],
        'pitfalls': ['极坐标漏掉乘微元 $r$；偏心圆 $(x-1)^2+y^2 \\le 1$ 角度范围误写为 $[0, 2\\pi]$（正确为 $[-\\pi/2, \\pi/2]$）。'],
        'formulas': [
            {'title': '极坐标变换公式', 'latex': 'dx dy = r\\, dr d\\theta, \\quad x^2 + y^2 = r^2'},
            {'title': '偏心圆极坐标方程', 'latex': '(x - a)^2 + y^2 = a^2 \\iff r = 2a\\cos\\theta \\quad (-\\pi/2 \\le \\theta \\le \\pi/2)'}
        ],
        'pastQuestions': [
            {
                'id': 'gaoshu-q-2019-1-10',
                'year': '2019',
                'category': '数一',
                'questionNumber': '(10)',
                'content': '二重积分 $\\iint_D \\sqrt{x^2 + y^2} dx dy$，其中 $D = \\{(x, y) \\mid x^2 + y^2 \\le 2x\\}$ 的值为（ ）',
                'analysis': '区域 $D$ 是以 $(1, 0)$ 为圆心、半径为 1 的圆盘。被积函数为 $\\sqrt{x^2+y^2} = r$。极坐标化：边界方程 $r^2 \\le 2r\\cos\\theta \\implies r \\le 2\\cos\\theta$；角度 $-\\pi/2 \\le \\theta \\le \\pi/2$。',
                'solutionSteps': [
                    '第一步：画出区域 $D$，圆心 $(1, 0)$，半径 1，过原点。',
                    '极坐标下区域表示为：$-\\frac{\\pi}{2} \\le \\theta \\le \\frac{\\pi}{2}, \\quad 0 \\le r \\le 2\\cos\\theta$。',
                    '第二步：被积函数 $\\sqrt{x^2+y^2} = r$，面积元素 $dx dy = r dr d\\theta$。',
                    '第三步：列极坐标累次积分：',
                    '$$I = \\int_{-\\pi/2}^{\\pi/2} d\\theta \\int_0^{2\\cos\\theta} r \\cdot r dr = \\int_{-\\pi/2}^{\\pi/2} \\left[ \\frac{r^3}{3} \\right]_0^{2\\cos\\theta} d\\theta$$',
                    '$$= \\frac{8}{3} \\int_{-\\pi/2}^{\\pi/2} \\cos^3\\theta d\\theta = \\frac{16}{3} \\int_0^{\\pi/2} \\cos^3\\theta d\\theta$$',
                    '第四步：由华里士公式：$\\int_0^{\\pi/2} \\cos^3\\theta d\\theta = \\frac{2}{3} \\times 1 = \\frac{2}{3}$。',
                    '$$I = \\frac{16}{3} \\times \\frac{2}{3} = \\frac{32}{9}$$'
                ],
                'answer': '32/9',
                'pitfall': '被积函数乘微元漏乘 $r$ 算成 $r^2$ 的积分；华里士公式代错。',
                'difficulty': '★★☆☆☆',
                'verified': True,
                'source': 'Maki考研数学真题分类精解 第三十三讲 题33.2 (p.805)'
            }
        ],
        'variants': [
            {
                'id': 'var-gaoshu-06-01',
                'question': '计算 $\\iint_D e^{x^2+y^2} dx dy$，其中 $D: x^2 + y^2 \\le 1, x \\ge 0, y \\ge 0$。',
                'hint': '第一象限单位圆，$0 \\le \\theta \\le \\pi/2, 0 \\le r \\le 1$。',
                'methodChoiceAnalysis': '完全分离变量，极速口算。',
                'fullSolution': [
                    '$I = \\int_0^{\\pi/2} d\\theta \\int_0^1 e^{r^2} r dr = \\frac{\\pi}{2} [\\frac{1}{2} e^{r^2}]_0^1 = \\frac{\\pi}{4}(e - 1)$。'
                ],
                'keyTakeaway': '只要被积函数含 $r e^{r^2}$，凑微分 $\\frac{1}{2}d(r^2)$ 秒出原函数。'
            }
        ],
        'relatedKnowledgeIds': ['gaoshu-06-order-exchange-symmetry', 'gaoshu-03-definite-integral-symmetry'],
        'tags': ['二重积分', '极坐标', '偏心圆', '华里士公式'],
        'source': 'Maki考研数学大串讲 L33 & 真题分类精解 题33.2',
        'status': 'not_started',
        'isPending': False
    },
    'gaoshu-06-order-exchange-symmetry': {
        'id': 'gaoshu-06-order-exchange-symmetry',
        'title': '二重积分交换积分次序与对称性奇偶简化',
        'subject': 'gaoshu',
        'subjectName': '高等数学',
        'chapterId': 'gaoshu-ch06',
        'chapterTitle': '二重积分与多重积分',
        'nodeType': 'topic',
        'summary': '“内积积不动，果断换次序；区域关于坐标轴对称看奇偶，关于 $y=x$ 对称变量对调相加除以二”。',
        'triggers': ['计算形如 $\\int_0^1 dx \\int_x^1 \\sin(y^2) dy$（内层无法积出）', '题目明确要求“交换下列累次积分的积分次序”', '积分区域关于 $y=x$ 对称且被积函数含非对称项'],
        'firstReaction': '内层积不出必换次序！三步换次序：画出草图 $\\implies$ 确定交点与平面投影 $\\implies$ 改写不等式集合（横向穿线改竖向穿线）；若区域关于 $y=x$ 对称，交换 $x, y$ 两式相加除以2消项。',
        'candidateMethods': [
            {'name': '交换积分次序画图法', 'priority': 1, 'condition': '原次序不可积或题目要求换序', 'whyChoose': '不可积函数的唯一突破口', 'description': '画出 $D$，由 X 型改为 Y 型或由 Y 型改为 X 型'},
            {'name': '轮换对称性对调法 (y=x)', 'priority': 2, 'condition': '区域关于 $y=x$ 对称', 'whyChoose': '将非对称项化为常数', 'description': '$\\iint_D f(x, y)d\\sigma = \\iint_D f(y, x)d\\sigma = \\frac{1}{2}\\iint_D [f(x, y)+f(y, x)]d\\sigma$'}
        ],
        'applicability': '交换积分次序时外层积分限必须是【常数】；内层积分限必须是自变量的单值函数，若穿出线有多段必须拆成多个二重积分之和。',
        'steps': [
            '步骤1：从已有累次积分上下限读出不等式组，精确画出闭区域 $D$。',
            '步骤2：观察新外层变量的全局取值范围 $[c, d]$。',
            '步骤3：做垂直穿线，确定新内层变量的穿入函数与穿出函数。',
            '步骤4：写出新的累次积分并求解。'
        ],
        'pitfalls': ['换次序后外层积分限写成了变量（外限必须是常数！）；穿出曲线分段未拆开。'],
        'formulas': [
            {'title': '轮换对称性公式', 'latex': 'D \\text{ 关于 } y=x \\text{ 对称} \\implies \\iint_D f(x)d\\sigma = \\iint_D f(y)d\\sigma = \\frac{1}{2}\\iint_D [f(x)+f(y)]d\\sigma'},
            {'title': '普通对称性公式', 'latex': 'D \\text{ 关于 } y \\text{ 轴对称} \\implies \\iint_D f(x, y)d\\sigma = \\begin{cases} 0, & f(-x, y) = -f(x, y) \\\\ 2\\iint_{D_1} f(x, y)d\\sigma, & f(-x, y) = f(x, y) \\end{cases}'}
        ],
        'pastQuestions': [
            {
                'id': 'gaoshu-q-2022-1-9',
                'year': '2022',
                'category': '数一',
                'questionNumber': '(9)',
                'content': '累次积分 $\\int_0^1 dy \\int_y^1 \\frac{\\sin x}{x} dx = \\underline{\\quad\\quad\\quad\\quad}.$',
                'analysis': '内层 $\\int \\frac{\\sin x}{x} dx$ 是著名的非初等函数（正弦积分），直接积根本积不出来！必须交换积分次序！原区域为 $0 \\le y \\le 1, y \\le x \\le 1$，即三角形区域 $0 \\le y \\le x \\le 1$。',
                'solutionSteps': [
                    '第一步：根据积分限确定区域 $D$：$0 \\le y \\le 1, y \\le x \\le 1$。',
                    '画图可知 $D$ 是由直线 $y = 0, x = 1, y = x$ 围成的三角形。',
                    '第二步：改为先对 $y$ 积分，后对 $x$ 积分：',
                    '$x$ 的取值范围为 $[0, 1]$；对固定的 $x$，$y$ 从 0 穿入，到 $y = x$ 穿出。',
                    '即 $0 \\le x \\le 1, \\quad 0 \\le y \\le x$。',
                    '第三步：交换次序后累次积分为：',
                    '$$I = \\int_0^1 dx \\int_0^x \\frac{\\sin x}{x} dy = \\int_0^1 \\frac{\\sin x}{x} \\left( \\int_0^x 1 dy \\right) dx$$',
                    '$$= \\int_0^1 \\frac{\\sin x}{x} \\cdot x dx = \\int_0^1 \\sin x dx$$',
                    '第四步：分母 $x$ 被完全消去！直接积分：',
                    '$$I = [-\\cos x]_0^1 = 1 - \\cos 1$$'
                ],
                'answer': '1 - \\cos 1',
                'pitfall': '在草稿纸上试图分部积分求 $\\int \\frac{\\sin x}{x}dx$；只要内层积不出，100% 交换次序。',
                'difficulty': '★★☆☆☆',
                'verified': True,
                'source': 'Maki考研数学真题分类精解 第三十三讲 题33.1 (p.797)'
            }
        ],
        'variants': [
            {
                'id': 'var-gaoshu-06-02',
                'question': '交换累次积分 $\\int_0^1 dx \\int_{x^2}^x f(x, y) dy$ 的积分次序。',
                'hint': '区域由 $y = x^2$ 与 $y = x$ 围成，$y \\in [0, 1]$。',
                'methodChoiceAnalysis': '对固定 $y$，从左侧直线 $x = y$ 穿入，右侧抛物线 $x = \\sqrt{y}$ 穿出。',
                'fullSolution': [
                    '原区域为 $0 \\le x \\le 1, x^2 \\le y \\le x$。',
                    '改写为 $y$ 为外层：$0 \\le y \\le 1$；',
                    '对于每个 $y$，$x$ 从 $x = y$ 到 $x = \\sqrt{y}$。',
                    '交换后为 $\\int_0^1 dy \\int_y^{\\sqrt{y}} f(x, y) dx$。'
                ],
                'keyTakeaway': '先对谁积，就做平行于该轴的穿线看进出。'
            }
        ],
        'relatedKnowledgeIds': ['gaoshu-06-double-integral-polar', 'gaoshu-03-variable-limit-integral'],
        'tags': ['交换积分次序', '正弦积分', '轮换对称性', '穿线法'],
        'source': 'Maki考研数学大串讲 L33 & 真题分类精解 题33.1',
        'status': 'not_started',
        'isPending': False
    },
    'gaoshu-06-triple-integral-coordinates': {
        'id': 'gaoshu-06-triple-integral-coordinates',
        'title': '三重积分计算（投影法、截面法、柱面与球面坐标）',
        'subject': 'gaoshu',
        'subjectName': '高等数学',
        'chapterId': 'gaoshu-ch06',
        'chapterTitle': '二重积分与多重积分',
        'nodeType': 'topic',
        'summary': '“柱体投影法（先一后二），锥体截面法（先二后一）；含 $x^2+y^2$ 用柱坐标，含 $x^2+y^2+z^2$ 或锥顶角用球坐标”。',
        'triggers': ['计算空间立体 $\\Omega$ 上的三重积分 $\\iiint_\\Omega f(x, y, z) dV$', '区域为旋转抛物面、圆柱体或圆锥体', '积分区域为球体或被积函数含 $(x^2+y^2+z^2)^p$'],
        'firstReaction': '选坐标系：\\n1. 球面坐标：球体、半球、锥顶在原点的圆锥，面积元素 $r^2 \\sin\\phi dr d\\phi d\\theta$；\\n2. 柱面坐标：圆柱体、旋转抛物面，微元 $r dr d\\theta dz$；\\n3. 直角坐标先一后二：立体的 $xy$ 面投影 $D_{xy}$ 规则，竖直方向穿线 $z_1(x, y) \\to z_2(x, y)$。',
        'candidateMethods': [
            {'name': '柱面坐标法', 'priority': 1, 'condition': '区域投影为圆，且高为柱状或抛物面', 'whyChoose': '直接化极坐标，保留高 $z$', 'description': '$x = r\\cos\\theta, y = r\\sin\\theta, z = z, dV = r dr d\\theta dz$'},
            {'name': '球面坐标法', 'priority': 2, 'condition': '球体或含 $x^2+y^2+z^2$', 'whyChoose': '径向距离与角度彻底分离', 'description': '$x = r\\sin\\phi\\cos\\theta, y = r\\sin\\phi\\sin\\theta, z = r\\cos\\phi, dV = r^2\\sin\\phi dr d\\phi d\\theta$'},
            {'name': '先一后二投影法', 'priority': 3, 'condition': '上下底面明确的柱状直角区域', 'whyChoose': '先对 $z$ 积分转化为二重积分', 'description': '$\\iint_{D_{xy}} dxdy \\int_{z_1(x, y)}^{z_2(x, y)} f(x, y, z) dz$'}
        ],
        'applicability': '球面坐标中天顶角 $\\phi$ 是从正 $z$ 轴向下量取的角，范围只能在 $[0, \\pi]$ 内，千万不能写到 $2\\pi$！微元是 $r^2 \\sin\\phi$。',
        'steps': [
            '步骤1：画出空间立体 $\\Omega$ 及它在 $xy$ 平面的投影区域 $D_{xy}$。',
            '步骤2：根据对称性检查奇偶性（若区域关于 $xoy$ 面对称，$z$ 的奇函数积分为 0）。',
            '步骤3：选择柱面坐标或球面坐标，写出积分限。',
            '步骤4：按由内向外顺序完成三重定积分计算。'
        ],
        'pitfalls': ['球面坐标微元漏乘 $r^2 \\sin\\phi$；柱面坐标漏乘 $r$；天顶角 $\\phi$ 与方位角 $\\theta$ 范围混淆。'],
        'formulas': [
            {'title': '柱面坐标微元', 'latex': 'dV = r\\, dr d\\theta dz, \\quad x^2 + y^2 = r^2'},
            {'title': '球面坐标微元', 'latex': 'dV = r^2 \\sin\\phi\\, dr d\\phi d\\theta, \\quad x^2 + y^2 + z^2 = r^2'}
        ],
        'pastQuestions': [
            {
                'id': 'gaoshu-q-2021-1-11',
                'year': '2021',
                'category': '数一',
                'questionNumber': '(11)',
                'content': '三重积分 $\\iiint_\\Omega (x^2 + y^2) dV$，其中 $\\Omega$ 是由球面 $x^2 + y^2 + z^2 = R^2$ 所围成的闭区域，其值为（ ）',
                'analysis': '利用轮换对称性！由于 $\\Omega$ 是完全对称的球体，故 $\\iiint_\\Omega x^2 dV = \\iiint_\\Omega y^2 dV = \\iiint_\\Omega z^2 dV$。因此 $\\iiint_\\Omega (x^2+y^2)dV = \\frac{2}{3} \\iiint_\\Omega (x^2+y^2+z^2)dV$！用球面坐标一秒出结果。',
                'solutionSteps': [
                    '第一步：由区域 $\\Omega$ 的轮换对称性：',
                    '$$\\iiint_\\Omega x^2 dV = \\iiint_\\Omega y^2 dV = \\iiint_\\Omega z^2 dV$$',
                    '第二步：因此：',
                    '$$\\iiint_\\Omega (x^2 + y^2) dV = \\frac{2}{3} \\iiint_\\Omega (x^2 + y^2 + z^2) dV$$',
                    '第三步：采用球面坐标计算 $\\iiint_\\Omega r^2 dV$：',
                    '$$\\iiint_\\Omega r^2 \\cdot (r^2 \\sin\\phi dr d\\phi d\\theta) = \\int_0^{2\\pi} d\\theta \\int_0^\\pi \\sin\\phi d\\phi \\int_0^R r^4 dr$$',
                    '第四步：分别计算三个一重积分：',
                    '$\\int_0^{2\\pi} d\\theta = 2\\pi$；$\\int_0^\\pi \\sin\\phi d\\phi = 2$；$\\int_0^R r^4 dr = \\frac{R^5}{5}$。',
                    '积分为 $2\\pi \\times 2 \\times \\frac{R^5}{5} = \\frac{4\\pi R^5}{5}$。',
                    '第五步：代入原式：$\\frac{2}{3} \\times \\frac{4\\pi R^5}{5} = \\frac{8\\pi R^5}{15}$。'
                ],
                'answer': '8\\pi R^5 / 15',
                'pitfall': '不使用轮换对称性去硬算，计算量大 3 倍且容易在天顶角积分出错。',
                'difficulty': '★★☆☆☆',
                'verified': True,
                'source': 'Maki考研数学真题分类精解 第三十四讲 题34.1 (p.904)'
            }
        ],
        'variants': [
            {
                'id': 'var-gaoshu-06-03',
                'question': '用柱面坐标计算 $\\iiint_\\Omega z dV$，其中 $\\Omega$ 由圆锥面 $z = \\sqrt{x^2+y^2}$ 与平面 $z = 1$ 围成。',
                'hint': '柱坐标下圆锥面为 $z = r$，底面投影为单位圆 $0 \\le r \\le 1$。',
                'methodChoiceAnalysis': '柱面坐标：$0 \\le \\theta \\le 2\\pi, 0 \\le r \\le 1, r \\le z \\le 1$。',
                'fullSolution': [
                    '$I = \\int_0^{2\\pi} d\\theta \\int_0^1 r dr \\int_r^1 z dz = 2\\pi \\int_0^1 r [\\frac{1 - r^2}{2}] dr = \\pi \\int_0^1 (r - r^3) dr = \\pi [\\frac{1}{2} - \\frac{1}{4}] = \\frac{\\pi}{4}$。'
                ],
                'keyTakeaway': '锥体柱坐标积分限：从下表面 $z=r$ 穿入，到上底面 $z=1$ 穿出。'
            }
        ],
        'relatedKnowledgeIds': ['gaoshu-06-double-integral-polar', 'gaoshu-07-gauss-divergence-theorem'],
        'tags': ['三重积分', '球面坐标', '柱面坐标', '轮换对称性'],
        'source': 'Maki考研数学大串讲 L34 & 真题分类精解 题34.1',
        'status': 'not_started',
        'isPending': False
    },
    'gaoshu-07-green-formula-hole-technique': {
        'id': 'gaoshu-07-green-formula-hole-technique',
        'title': '格林公式与开曲线补线/挖洞法',
        'subject': 'gaoshu',
        'subjectName': '高等数学',
        'chapterId': 'gaoshu-ch07',
        'chapterTitle': '曲线积分与曲面积分',
        'nodeType': 'topic',
        'summary': '“闭合曲线逆时针用格林化二重积分；不闭合补直线段闭合，挖奇点小圆周环路积分”。',
        'triggers': ['计算平面第二类曲线积分 $\\oint_L P dx + Q dy$', '曲线不闭合但容易添加坐标轴线段使其闭合', '被积函数在原点 $(0, 0)$ 分母为零（奇点挖洞）'],
        'firstReaction': '先算交叉偏导：$\\frac{\\partial Q}{\\partial x} - \\frac{\\partial P}{\\partial y}$！若相等且无奇点，直接路径无关用端点求；若不相等且闭合，格林公式化二重积分 $\\iint (Q_x - P_y) dxdy$；若不闭合，补一条直线段使之闭合，最后减去补线的积分；若分母有奇点，在奇点处挖一小圆周 $L_\\varepsilon$！',
        'candidateMethods': [
            {'name': '格林公式标准闭合化', 'priority': 1, 'condition': '无奇点的闭合正向曲线', 'whyChoose': '把一维线积分转化为二维面积分', 'description': '$\\oint_L P dx + Q dy = \\iint_D \\left( \\frac{\\partial Q}{\\partial x} - \\frac{\\partial P}{\\partial y} \\right) dxdy$'},
            {'name': '开曲线补线法', 'priority': 2, 'condition': '非闭合曲线但两端点落在坐标轴上', 'whyChoose': '补直线段通常导数为0极易积分', 'description': '$\\int_L = \\oint_{L + L_\\text{补}} - \\int_{L_\\text{补}}$'},
            {'name': '奇点挖洞法', 'priority': 3, 'condition': '区域内含有分母为0的孤立奇点（如原点）', 'whyChoose': '隔离不可导奇点，外层变为路径无关', 'description': '围一顺时针小圆 $L_\\varepsilon$，$\\oint_L = \\oint_{L_\\varepsilon}$'}
        ],
        'applicability': '格林公式成立要求曲线方向必须是【正向】（人沿方向走，区域始终在左侧，外边界为逆时针）；若顺时针必须加负号；区域内绝不能包含偏导数不存在的奇点！',
        'steps': [
            '步骤1：检查曲线方向是否为逆时针正向，检查区域内是否有奇点。',
            '步骤2：计算核项 $\\frac{\\partial Q}{\\partial x} - \\frac{\\partial P}{\\partial y}$。',
            '步骤3：若不闭合，添加线段 $L_1$（写明方向与参数方程），套用格林公式。',
            '步骤4：计算二重积分并减去补线积分 $\\int_{L_1}$。'
        ],
        'pitfalls': ['正反方向搞错漏乘负号；忽视原点奇点盲目用格林公式得 0（经典大坑题，如 $\\frac{-y dx + x dy}{x^2+y^2}$ 绕原点一周积分恒为 $2\\pi$ 而非 0）。'],
        'formulas': [
            {'title': '格林公式', 'latex': '\\oint_L P\\,dx + Q\\,dy = \\iint_D \\left( \\frac{\\partial Q}{\\partial x} - \\frac{\\partial P}{\\partial y} \\right) dxdy'},
            {'title': '经典旋转场积分配方', 'latex': '\\oint_L \\frac{-y\\,dx + x\\,dy}{x^2 + y^2} = 2\\pi \\quad (L \\text{ 包含原点正向})'}
        ],
        'pastQuestions': [
            {
                'id': 'gaoshu-q-2022-1-11',
                'year': '2022',
                'category': '数一',
                'questionNumber': '(11)',
                'content': '计算曲线积分 $I = \\int_L (2xy - 1) dx + x^2 dy$，其中 $L$ 为抛物线 $y = x^2$ 从点 $(0, 0)$ 到点 $(1, 1)$ 的一段弧。',
                'analysis': '先算交叉偏导：$P = 2xy - 1 \\implies P_y = 2x$；$Q = x^2 \\implies Q_x = 2x$。\\n惊奇发现：$\\frac{\\partial Q}{\\partial x} = \\frac{\\partial P}{\\partial y}$ 在全平面恒成立！全平面单连通且无奇点，积分与路径完全无关！直接改用沿坐标轴折线积分或求原函数。',
                'solutionSteps': [
                    '第一步：计算偏导数：$P_y\' = 2x, \\quad Q_x\' = 2x$。',
                    '在整个 $\\mathbb{R}^2$ 平面上，$P_y\' = Q_x\'$ 恒成立，且全平面是单连通区域。',
                    '第二步：因此积分与路径无关！',
                    '第三步：改选最简单的直线路径：从 $(0, 0)$ 到 $(1, 1)$ 的直线 $y = x$，则 $dy = dx$。',
                    '$$I = \\int_0^1 [(2x \\cdot x - 1) dx + x^2 dx] = \\int_0^1 (3x^2 - 1) dx = [x^3 - x]_0^1 = 0$$',
                    '（或直接求原函数 $U(x, y) = x^2 y - x$，代入端点 $U(1, 1) - U(0, 0) = (1 - 1) - 0 = 0$）。'
                ],
                'answer': '0',
                'pitfall': '未验证路径无关性而老老实实代入抛物线方程积分，虽然能算出来但计算繁琐。',
                'difficulty': '★★☆☆☆',
                'verified': True,
                'source': 'Maki考研数学真题分类精解 第三十五讲 题35.2 (p.918)'
            }
        ],
        'variants': [
            {
                'id': 'var-gaoshu-07-02',
                'question': '计算 $\\oint_L \\frac{-y dx + x dy}{x^2 + y^2}$，其中 $L$ 为椭圆 $x^2 + 4y^2 = 4$ 逆时针方向。',
                'hint': '原点 $(0, 0)$ 是奇点，不能直接用格林公式得 0！挖洞法。',
                'methodChoiceAnalysis': '在原点内挖小圆 $x^2+y^2=\\varepsilon^2$，积分与椭圆完全相同。',
                'fullSolution': [
                    '在椭圆内部挖去小圆 $L_\\varepsilon: x = \\varepsilon \\cos t, y = \\varepsilon \\sin t (0 \\le t \\le 2\\pi)$。',
                    '在两曲线之间的复连通区域上偏导处处相等，故原积分等于小圆上的积分：',
                    '$\\oint_{L_\\varepsilon} \\frac{-(\\varepsilon\\sin t)(-\\varepsilon\\sin t) + (\\varepsilon\\cos t)(\\varepsilon\\cos t)}{\\varepsilon^2} dt = \\int_0^{2\\pi} 1 dt = 2\\pi$。'
                ],
                'keyTakeaway': '只要封闭曲线内部包裹原点，旋转势场线积分恒等于 $2\\pi$。'
            }
        ],
        'relatedKnowledgeIds': ['gaoshu-07-curvilinear-path-independent', 'gaoshu-07-gauss-divergence-theorem'],
        'tags': ['格林公式', '补线法', '挖洞法', '奇点积分', '路径无关'],
        'source': 'Maki考研数学大串讲 L35 & 真题分类精解 题35.2',
        'status': 'not_started',
        'isPending': False
    },
    'gaoshu-07-gauss-divergence-theorem': {
        'id': 'gaoshu-07-gauss-divergence-theorem',
        'title': '高斯散度公式与闭合曲面积分/补面法',
        'subject': 'gaoshu',
        'subjectName': '高等数学',
        'chapterId': 'gaoshu-ch07',
        'chapterTitle': '曲线积分与曲面积分',
        'nodeType': 'topic',
        'summary': '“封闭曲面外法线用高斯散度化三重积分；不封闭补平面封闭，注意散度公式加减补面”。',
        'triggers': ['计算第二类曲面积分 $\\oiint_\\Sigma P dy dz + Q dz dx + R dx dy$', '曲面为柱面、抛物面截顶等开曲面', '散度 $\\mathrm{div} F = P_x + Q_y + R_z$ 计算简单（为常数或简单多项式）'],
        'firstReaction': '先算散度：$\\mathrm{div} F = \\frac{\\partial P}{\\partial x} + \\frac{\\partial Q}{\\partial y} + \\frac{\\partial R}{\\partial z}$！若为常数，三重积分直接等于常数乘空间体积；若曲面不封闭，补平面（如底面 $z = 0$）使之封闭；补平面上外法向方向必须与体外侧一致，并在最后减去补面积分。',
        'candidateMethods': [
            {'name': '高斯公式化三重积分法', 'priority': 1, 'condition': '封闭曲面且偏导连续', 'whyChoose': '降维打击，直接化为简单多重积分或体积', 'description': '$\\oiint_\\Sigma P dydz + Q dzdx + R dxdy = \\iiint_\\Omega (P_x + Q_y + R_z) dV$'},
            {'name': '补面法 (平面补底)', 'priority': 2, 'condition': '开曲面但底面为坐标平面', 'whyChoose': '补底面通常法向量垂直坐标轴极好积分', 'description': '$\\iint_\\Sigma = \\oiint_{\\Sigma + \\Sigma_1} - \\iint_{\\Sigma_1}$'}
        ],
        'applicability': '高斯公式中封闭曲面必须取【外侧】；若取内侧必须整体加负号；补面的方向必须背离立体内部以保证是封闭闭合曲面的外侧。',
        'steps': [
            '步骤1：检查曲面是否封闭及侧向（外侧还是内侧）。',
            '步骤2：若不封闭，补上平面 $\\Sigma_1$（标明法向量方向，通常方向向下 $dxdy$ 取负）。',
            '步骤3：计算被积函数的散度 $P_x + Q_y + R_z$。',
            '步骤4：由高斯公式算三重积分，并计算补面 $\\Sigma_1$ 上的积分做差。'
        ],
        'pitfalls': ['补面法中补面方向搞反（补底面时外侧朝下，投影为 $-dxdy$ 容易漏负号）；误对有奇点的区域直接用高斯公式。'],
        'formulas': [
            {'title': '高斯公式', 'latex': '\\oiint_\\Sigma P\\,dydz + Q\\,dzdx + R\\,dxdy = \\iiint_\\Omega \\left( \\frac{\\partial P}{\\partial x} + \\frac{\\partial Q}{\\partial y} + \\frac{\\partial R}{\\partial z} \\right) dV'},
            {'title': '散度定义', 'latex': '\\mathrm{div}\\mathbf{F} = \\nabla \\cdot \\mathbf{F} = \\frac{\\partial P}{\\partial x} + \\frac{\\partial Q}{\\partial y} + \\frac{\\partial R}{\\partial z}'}
        ],
        'pastQuestions': [
            {
                'id': 'gaoshu-q-2021-1-18',
                'year': '2021',
                'category': '数一',
                'questionNumber': '(18)',
                'content': '计算曲面积分 $I = \\iint_\\Sigma x dydz + y dzdx + z dxdy$，其中 $\\Sigma$ 是抛物面 $z = 1 - x^2 - y^2 (z \\ge 0)$ 的上侧。',
                'analysis': '曲面不封闭！下底面在 $z=0$ 平面上。补上底面 $\\Sigma_1: z = 0 (x^2+y^2 \\le 1)$，方向朝下！此时 $\\Sigma + \\Sigma_1$ 构成封闭立体 $\\Omega$ 的外侧。散度 $P_x + Q_y + R_z = 1 + 1 + 1 = 3$！',
                'solutionSteps': [
                    '第一步：补上底面 $\\Sigma_1: z = 0, x^2 + y^2 \\le 1$，取下侧（外侧）。',
                    '第二步：由高斯公式：',
                    '$$\\iint_\\Sigma + \\iint_{\\Sigma_1} = \\iiint_\\Omega (1 + 1 + 1) dV = 3 V_\\Omega$$',
                    '第三步：计算抛物面立体的体积：',
                    '$$V_\\Omega = \\iint_{D_{xy}} (1 - x^2 - y^2) dxdy = \\int_0^{2\\pi} d\\theta \\int_0^1 (1 - r^2) r dr = 2\\pi \\left[ \\frac{r^2}{2} - \\frac{r^4}{4} \\right]_0^1 = \\frac{\\pi}{2}$$',
                    '故三重积分为 $3 \\times \\frac{\\pi}{2} = \\frac{3\\pi}{2}$。',
                    '第四步：计算补面 $\\Sigma_1$ 上的积分：在 $\\Sigma_1$ 上 $z = 0$，法向量朝下（$dydz = 0, dzdx = 0, dxdy$ 取负号）：',
                    '$$\\iint_{\\Sigma_1} x dydz + y dzdx + z dxdy = \\iint_{D_{xy}} 0 (-dxdy) = 0$$',
                    '第五步：移项得出所求积分：$I = \\frac{3\\pi}{2} - 0 = \\frac{3\\pi}{2}$。'
                ],
                'answer': '3\\pi / 2',
                'pitfall': '补底面时忘记在底面上 $z=0$ 可以直接代入化简；补面侧向漏负号。',
                'difficulty': '★★★☆☆',
                'verified': True,
                'source': 'Maki考研数学真题分类精解 第三十六讲 题36.2 (p.940)'
            }
        ],
        'variants': [
            {
                'id': 'var-gaoshu-07-03',
                'question': '计算 $\\oiint_\\Sigma x^3 dydz + y^3 dzdx + z^3 dxdy$，其中 $\\Sigma$ 为球面 $x^2 + y^2 + z^2 = R^2$ 外侧。',
                'hint': '散度为 $3(x^2+y^2+z^2)$，球面坐标或轮换对称性。',
                'methodChoiceAnalysis': '高斯公式化为 $3 \\iiint_\\Omega r^2 dV$。',
                'fullSolution': [
                    '由高斯公式：$I = \\iiint_\\Omega (3x^2 + 3y^2 + 3z^2) dV = 3 \\iiint_\\Omega r^2 dV$。',
                    '由球坐标：$\\iiint_\\Omega r^2 dV = 4\\pi \\int_0^R r^4 dr = \\frac{4\\pi R^5}{5}$。',
                    '故 $I = 3 \\times \\frac{4\\pi R^5}{5} = \\frac{12\\pi R^5}{5}$。'
                ],
                'keyTakeaway': '高斯公式配球面坐标是数一曲面积分最稳定大题得分点。'
            }
        ],
        'relatedKnowledgeIds': ['gaoshu-06-triple-integral-coordinates', 'gaoshu-07-stokes-theorem-curl'],
        'tags': ['高斯公式', '散度', '补面法', '曲面积分'],
        'source': 'Maki考研数学大串讲 L36 & 真题分类精解 题36.2',
        'status': 'not_started',
        'isPending': False
    },
    'gaoshu-07-stokes-theorem-curl': {
        'id': 'gaoshu-07-stokes-theorem-curl',
        'title': '斯托克斯公式与空间曲线积分/旋度',
        'subject': 'gaoshu',
        'subjectName': '高等数学',
        'chapterId': 'gaoshu-ch07',
        'chapterTitle': '曲线积分与曲面积分',
        'nodeType': 'topic',
        'summary': '“空间闭合曲线积分等于旋度沿曲面的曲面积分；右手法则定方向，旋度符号行列式”。',
        'triggers': ['空间闭合曲线积分 $\\oint_\\Gamma P dx + Q dy + R dz$', '已知向量场求其旋度 $\\mathbf{rot}\\,\\mathbf{F} = \\nabla \\times \\mathbf{F}$', '曲线位于某一平面上（如 $x+y+z=1$）'],
        'firstReaction': '空间闭线积分化面积分首选斯托克斯公式！旋度行列式：$\\mathrm{rot}\\,\\mathbf{F} = \\begin{vmatrix} \\mathbf{i} & \\mathbf{j} & \\mathbf{k} \\\\ \\partial_x & \\partial_y & \\partial_z \\\\ P & Q & R \\end{vmatrix}$；选最平坦的截面曲面 $\\Sigma$（特别是平面，法向量 $\\mathbf{n}$ 为常向量极易点乘！）。',
        'candidateMethods': [
            {'name': '斯托克斯公式平面投影法', 'priority': 1, 'condition': '空间闭合曲线且容易张成平面', 'whyChoose': '把空间曲线积分化为二重积分', 'description': '$\\oint_\\Gamma \\mathbf{F} \\cdot d\\mathbf{r} = \\iint_\\Sigma (\\nabla \\times \\mathbf{F}) \\cdot \\mathbf{n} dS$'}
        ],
        'applicability': '曲面法向 $\\mathbf{n}$ 与曲线方向必须满足右手法则：右手四指沿曲线方向弯曲，大拇指指向曲面的法向侧。',
        'steps': [
            '步骤1：计算向量场的旋度分量：$R_y - Q_z, P_z - R_x, Q_x - P_y$。',
            '步骤2：选取以 $\\Gamma$ 为边界的最简单空间曲面 $\\Sigma$（通常是平面）。',
            '步骤3：确定曲面单位法向量 $\\mathbf{n} = (\\cos\\alpha, \\cos\\beta, \\cos\\gamma)$。',
            '步骤4：化为第一类曲面积分或直接投影为二重积分求解。'
        ],
        'pitfalls': ['旋度符号次序颠倒（第一分量是 $R_y - Q_z$）；右手法则判断侧向方向出错。'],
        'formulas': [
            {'title': '斯托克斯公式', 'latex': '\\oint_\\Gamma P\\,dx + Q\\,dy + R\\,dz = \\iint_\\Sigma \\begin{vmatrix} dydz & dzdx & dxdy \\\\ \\frac{\\partial}{\\partial x} & \\frac{\\partial}{\\partial y} & \\frac{\\partial}{\\partial z} \\\\ P & Q & R \\end{vmatrix}'},
            {'title': '旋度定义', 'latex': '\\mathrm{rot}\\,\\mathbf{F} = \\left( \\frac{\\partial R}{\\partial y} - \\frac{\\partial Q}{\\partial z} \\right)\\mathbf{i} + \\left( \\frac{\\partial P}{\\partial z} - \\frac{\\partial R}{\\partial x} \\right)\\mathbf{j} + \\left( \\frac{\\partial Q}{\\partial x} - \\frac{\\partial P}{\\partial y} \\right)\\mathbf{k}'}
        ],
        'pastQuestions': [
            {
                'id': 'gaoshu-q-2016-1-11',
                'year': '2016',
                'category': '数一',
                'questionNumber': '(11)',
                'content': '设 $\\Gamma$ 为平面 $x + y + z = 1$ 与圆柱面 $x^2 + y^2 = 1$ 的交线，从 $z$ 轴正向往负向看为逆时针方向。计算曲线积分 $I = \\oint_\\Gamma (y - z) dx + (z - x) dy + (x - y) dz$。',
                'analysis': '斯托克斯公式绝配题目！曲线张成的曲面 $\\Sigma$ 就是平面 $x+y+z=1$ 落在圆柱面内的椭圆盘。曲面单位法向量朝上：$\\mathbf{n} = \\frac{1}{\\sqrt{3}}(1, 1, 1)$。计算旋度行列式。',
                'solutionSteps': [
                    '第一步：计算旋度分量：',
                    '$$P = y - z, \\quad Q = z - x, \\quad R = x - y$$',
                    '$$R_y\' - Q_z\' = -1 - 1 = -2$$',
                    '$$P_z\' - R_x\' = -1 - 1 = -2$$',
                    '$$Q_x\' - P_y\' = -1 - 1 = -2$$',
                    '因此旋度为 $\\mathrm{rot}\\,\\mathbf{F} = (-2, -2, -2)$。',
                    '第二步：曲面 $\\Sigma$ 选为平面 $x+y+z=1$，其法向朝上，单位法向量 $\\mathbf{n} = \\frac{(1, 1, 1)}{\\sqrt{3}}$。',
                    '第三步：由斯托克斯公式：',
                    '$$I = \\iint_\\Sigma (\\mathrm{rot}\\,\\mathbf{F} \\cdot \\mathbf{n}) dS = \\iint_\\Sigma (-2, -2, -2) \\cdot \\frac{(1, 1, 1)}{\\sqrt{3}} dS$$',
                    '$$= \\iint_\\Sigma \\frac{-6}{\\sqrt{3}} dS = -2\\sqrt{3} \\iint_\\Sigma dS = -2\\sqrt{3} \\cdot \\mathrm{Area}(\\Sigma)$$',
                    '第四步：由投影面积关系：$\\mathrm{Area}(\\Sigma) = \\frac{\\mathrm{Area}(D_{xy})}{\\cos\\gamma} = \\frac{\\pi \\cdot 1^2}{1/\\sqrt{3}} = \\sqrt{3}\\pi$。',
                    '因此 $I = -2\\sqrt{3} \\times (\\sqrt{3}\\pi) = -6\\pi$。'
                ],
                'answer': '-6\\pi',
                'pitfall': '曲面面积投影忘记除以 $\\cos\\gamma = 1/\\sqrt{3}$；逆时针方向对应法向朝上判定出错。',
                'difficulty': '★★★☆☆',
                'verified': True,
                'source': 'Maki考研数学真题分类精解 第三十七讲 题37.1 (p.968)'
            }
        ],
        'variants': [
            {
                'id': 'var-gaoshu-07-04',
                'question': '若向量场 $\\mathbf{F}$ 的旋度处处为零，且定义域单连通，证明沿任意闭曲线的环量积分为零。',
                'hint': '斯托克斯公式直接代入 $\\mathrm{rot}\\,\\mathbf{F} = 0$。',
                'methodChoiceAnalysis': '保守场（有势场）的基本性质。',
                'fullSolution': [
                    '由斯托克斯公式：$\\oint_\\Gamma \\mathbf{F} \\cdot d\\mathbf{r} = \\iint_\\Sigma (\\nabla \\times \\mathbf{F}) \\cdot \\mathbf{n} dS = \\iint_\\Sigma 0 dS = 0$。'
                ],
                'keyTakeaway': '无旋场必为有势场，环量恒为零。'
            }
        ],
        'relatedKnowledgeIds': ['gaoshu-07-green-formula-hole-technique', 'gaoshu-07-gauss-divergence-theorem'],
        'tags': ['斯托克斯公式', '旋度', '空间曲线积分', '环量'],
        'source': 'Maki考研数学大串讲 L37 & 真题分类精解 题37.1',
        'status': 'not_started',
        'isPending': False
    }
}
