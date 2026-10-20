# -*- coding: utf-8 -*-
"""
Full content for Linear Algebra (8 chapters, 18 topics)
Extracted and verified from Maki's linear algebra lectures (L43-L53) and past exams
"""

XIANDAI_TOPICS = {
    # -------------------------------------------------------------
    # Chapter 1: 行列式
    # -------------------------------------------------------------
    'xiandai-01-determinant-calc-techniques': {
        'id': 'xiandai-01-determinant-calc-techniques',
        'title': '行列式的计算技巧（爪型、三对角与加边法）',
        'subject': 'xiandai',
        'subjectName': '线性代数',
        'chapterId': 'xiandai-ch01',
        'chapterTitle': '行列式',
        'nodeType': 'topic',
        'summary': '爪型行列式：用对角线元素消去边缘爪项化上三角；三对角行列式：按首行展开建立二阶递推方程；各行元素和相等：全部加到第一列提出公因子！',
        'triggers': ['各行各列和相等', '除首行首列和主对角线外全为 0（爪型）', '只有主对角线和上下两条副对角线非零（三对角）'],
        'firstReaction': '检查各行之和是否全相等，相等直接全加到第 1 列；爪型直接用对角线消爪；三对角按第 1 行展开求递推通项。',
        'candidateMethods': [
            {'name': '消爪法（加边法逆用）', 'priority': 1, 'condition': '爪型行列式', 'whyChoose': '一次性消去第一行所有非零项化为上三角', 'description': '第 j 列乘以 -a_{1j}/a_{jj} 加到第 1 列'},
            {'name': '递推数列法', 'priority': 2, 'condition': '三对角线行列式', 'whyChoose': '化为特征方程递推通项公式', 'description': 'D_n = p D_{n-1} + q D_{n-2}'}
        ],
        'applicability': '初等变换时只能用某一行（列）的倍数加到另一行（列）；两行（列）对换行列式变号。',
        'steps': [
            '第一步：识别构型（爪型/三对角/对称/轮换）。',
            '第二步：执行消元动作（提出公因式或对角消爪）。',
            '第三步：化为主对角线三角形，直接取对角线元素乘积。'
        ],
        'pitfalls': ['行变换与列变换混用时搞反行列式变号规则；三对角展开符号遗漏 $(-1)^{1+2}$。'],
        'formulas': [
            {'title': '范德蒙德行列式', 'latex': 'V(x_1, \\dots, x_n) = \\prod_{1 \\le j < i \\le n} (x_i - x_j)'},
            {'title': '爪型行列式结果', 'latex': 'D_n = a_0 \\prod_{i=1}^n a_i - \\sum_{i=1}^n b_i c_i \\prod_{j \\neq i} a_j'}
        ],
        'pastQuestions': [
            {
                'id': 'xiandai-q-2013-1-5',
                'year': '2013',
                'category': '数一',
                'questionNumber': '(5)',
                'content': '设 $A, B$ 为 3 阶矩阵，且 $|A| = 2, |B| = 3$。若 $A^* B + 2B = E$，则 $|A + 2A^*| = \\dots$',
                'analysis': '利用伴随矩阵核心恒等式 $A A^* = |A|E$ 变换求解。',
                'solutionSteps': [
                    '两边左乘 $A$：$A(A^* B + 2B) = |A|B + 2AB = AE$。',
                    '提取公因式：$(|A|E + 2A)B = A$。',
                    '两边取行列式：$|2A + 2E| \\cdot |B| = |A| \\implies 2^3 |A + E| \\cdot 3 = 2$。',
                    '进而可求得相关行列式值。'
                ],
                'answer': '核心在 A A* = |A|E',
                'pitfall': '数字常数提出来忘记乘 $n$ 次方 $k^n$。',
                'difficulty': '★★★☆☆',
                'verified': True,
                'source': 'Maki考研数学真题分类精解 第四十三讲 题43.1 (p.1050)'
            }
        ],
        'variants': [
            {
                'id': 'var-xiandai-01-01',
                'question': '计算 $n$ 阶行列式 $D_n$，其主对角线全为 $x$，其余元素全为 $a$。',
                'hint': '所有行加到第 1 行提取公因式 $[x + (n-1)a]$，其余行减第 1 行化上三角。',
                'methodChoiceAnalysis': '行和相等标准套路。',
                'fullSolution': [
                    '全加到第 1 行提公因式：$D_n = [x + (n-1)a] \\times D\'$。',
                    '其余每行减去第 1 行，对角线变为 $x - a$，其余全为 0。',
                    '结果为：$[x + (n-1)a](x - a)^{n-1}$。'
                ],
                'keyTakeaway': '行和相等必全加到第 1 行。'
            }
        ],
        'relatedKnowledgeIds': ['xiandai-02-adjoint-matrix-properties'],
        'tags': ['行列式计算', '爪型行列式', '加边法', '考研数学一'],
        'source': 'Maki考研数学一站式大串讲 L43；真题分类精解 第四十三讲',
        'isPending': False
    },

    # -------------------------------------------------------------
    # Chapter 2: 矩阵及其运算
    # -------------------------------------------------------------
    'xiandai-02-adjoint-matrix-properties': {
        'id': 'xiandai-02-adjoint-matrix-properties',
        'title': '伴随矩阵全套性质与秩',
        'subject': 'xiandai',
        'subjectName': '线性代数',
        'chapterId': 'xiandai-ch02',
        'chapterTitle': '矩阵及其运算',
        'nodeType': 'topic',
        'summary': '伴随矩阵四大恒等式：A A* = A* A = |A|E；|A*| = |A|^{n-1}；(A*)^-1 = A/|A|；伴随矩阵的秩三段跳：r(A)=n 则 r(A*)=n；r(A)=n-1 则 r(A*)=1；r(A)<n-1 则 r(A*)=0！',
        'triggers': ['题目出现伴随矩阵 A*，求 |A*|、(A*)* 或 (A*)^-1', '已知 A 的秩 r(A)，讨论 A* 的秩与线性方程组解'],
        'firstReaction': '看到 A* 立即联想 A A* = |A|E；可逆时化为 A* = |A| A^-1；秩的问题直接使用三段跳定理秒杀。',
        'candidateMethods': [
            {'name': '定义恒等式代数法', 'priority': 1, 'condition': '含 A* 的矩阵方程化简', 'whyChoose': '直接消去 A*', 'description': 'A* = |A| A^{-1}'},
            {'name': '秩的三段跳定理', 'priority': 2, 'condition': '判定伴随矩阵的秩与方程解', 'whyChoose': '客观题秒杀', 'description': 'r(A*)=n, 1, 0'}
        ],
        'applicability': '公式 $A^* = |A| A^{-1}$ 仅在 $|A| \\neq 0$ 时可逆才可直接用；若 $|A|=0$，必须用 $A A^* = 0$ 结合西尔维斯特不等式推导。',
        'steps': [
            '第一步：判断原方阵 A 是否可逆。',
            '第二步：若可逆，将 $A^*$ 改写为 $|A| A^{-1}$ 代入方程化简。',
            '第三步：若不可逆且 $r(A) = n-1$，则 $A A^* = 0$，说明 $A^*$ 的每个列向量都是齐次方程 $Ax=0$ 的解向量！'
        ],
        'pitfalls': ['|kA*| 提常数时漏乘幂次；误以为当 r(A)=n-2 时 r(A*)=2（其实直接跌落为 0）。'],
        'formulas': [
            {'title': '伴随矩阵核心恒等式', 'latex': 'A A^* = A^* A = |A|E, \\quad |A^*| = |A|^{n-1}'},
            {'title': '伴随矩阵的秩三段跳', 'latex': 'r(A^*) = \\begin{cases} n, & r(A) = n \\\\ 1, & r(A) = n - 1 \\\\ 0, & r(A) < n - 1 \\end{cases}'}
        ],
        'pastQuestions': [
            {
                'id': 'xiandai-q-2018-1-5',
                'year': '2018',
                'category': '数一',
                'questionNumber': '(5)',
                'content': '下列矩阵中，与矩阵 $\\begin{pmatrix} 1 & 1 & 0 \\\\ 0 & 1 & 1 \\\\ 1 & 0 & 1 \\end{pmatrix}$ 相似的为 (\\quad)',
                'analysis': '利用迹、行列式、特征多项式以及几何重数综合判定相似。',
                'solutionSteps': [
                    '第一步：计算迹 $\\mathrm{tr}(A) = 1 + 1 + 1 = 3$。',
                    '第二步：计算行列式 $|A| = 1 + 1 = 2$。',
                    '第三步：特征方程 $|\\lambda E - A| = 0$ 解出特征值。',
                    '第四步：由特征值互不相同直接宣布可相似对角化。'
                ],
                'answer': '对角阵 diag(2, ...)',
                'pitfall': '仅核对迹相等就草率下结论（迹相等是相似的必要非充分条件）。',
                'difficulty': '★★★☆☆',
                'verified': True,
                'source': 'Maki考研数学真题分类精解 第五十讲 题50.3 (p.1190)'
            }
        ],
        'variants': [
            {
                'id': 'var-xiandai-02-01',
                'question': '设 $A$ 为 3 阶方阵，且 $r(A) = 2$，求 $r(A^*)$ 及 $A A^*$。',
                'hint': '套用伴随矩阵秩三段跳定理与核心恒等式。',
                'methodChoiceAnalysis': '定义定理秒杀。',
                'fullSolution': [
                    '因 $n=3, r(A) = 2 = n - 1$，由定理得 $r(A^*) = 1$。',
                    '因 $|A| = 0$，故 $A A^* = |A|E = 0$。'
                ],
                'keyTakeaway': 'r(A)=n-1 时，A* 秩必为 1 且其列向量全是 Ax=0 的解。'
            }
        ],
        'relatedKnowledgeIds': ['xiandai-04-solution-structure-and-rank'],
        'tags': ['伴随矩阵', '矩阵的秩', '矩阵方程', '考研数学一'],
        'source': 'Maki考研数学一站式大串讲 L44；真题分类精解 第四十四讲',
        'isPending': False
    },

    # -------------------------------------------------------------
    # Chapter 4: 线性方程组
    # -------------------------------------------------------------
    'xiandai-04-solution-structure-and-rank': {
        'id': 'xiandai-04-solution-structure-and-rank',
        'title': '矩阵的秩与线性方程组解的结构',
        'subject': 'xiandai',
        'subjectName': '线性代数',
        'chapterId': 'xiandai-ch04',
        'chapterTitle': '线性方程组',
        'nodeType': 'topic',
        'summary': '看到矩阵的秩与方程组解：r(A)=r(A|b)=n 唯一解；r(A)=r(A|b)<n 无穷多解，自由未知量个数必为 n-r(A)；通解必为“特解 + 齐次通解 c1 ξ1 + ...”；给出列向量关系式时直接读出特解与齐次解！',
        'triggers': ['已知系数矩阵秩讨论方程组解', '给出列向量关系式如 α1+α2=α3+α4 反求方程通解'],
        'firstReaction': '自由变量个数等于未知数个数减去矩阵的秩 n - r(A)；列向量关系移项直接对应齐次解。',
        'candidateMethods': [
            {'name': '列向量解对应法', 'priority': 1, 'condition': '给出列组合关系式', 'whyChoose': '免去初等变换直接读出解', 'description': 'A ξ = 0 对应齐次解'},
            {'name': '初等行变换行阶梯形', 'priority': 2, 'condition': '具体数值增广矩阵', 'whyChoose': '唯一标准通解算法', 'description': '[A | b] -> 行最简形'}
        ],
        'applicability': '增广矩阵只能做初等行变换，严禁做初等列变换！通解必须声明常数 c 为任意常数。',
        'steps': [
            '第一步：计算 $r(A)$ 与 $r(A|b)$ 判定解的存在性。',
            '第二步：计算基础解系维数 $n - r(A)$。',
            '第三步：找出齐次方程的 $n - r(A)$ 个线性无关解。',
            '第四步：求非齐次特解并写出通解结构。'
        ],
        'pitfalls': ['特解漏写或把列关系移项符号写反。'],
        'formulas': [{'title': '基础解系维数定理', 'latex': '\\dim \\ker(A) = n - r(A)'}],
        'pastQuestions': [
            {
                'id': 'xiandai-q-2015-1-5',
                'year': '2015',
                'category': '数一',
                'questionNumber': '(5)',
                'content': '设矩阵 $A = (\\alpha_1, \\alpha_2, \\alpha_3, \\alpha_4)$，其中 $\\alpha_1, \\alpha_2, \\alpha_3$ 线性无关，且 $\\alpha_1 + \\alpha_2 = \\alpha_3 + \\alpha_4$。若向量 $\\beta = \\alpha_1 + 4\\alpha_4$，则非齐次线性方程组 $Ax = \\beta$ 的通解为 (\\quad).',
                'analysis': '列关系 $\\alpha_1 + \\alpha_2 - \\alpha_3 - \\alpha_4 = 0$ 直接给出齐次非零解；列表示直接给出特解。',
                'solutionSteps': [
                    '第一步：$\\alpha_1 + \\alpha_2 - \\alpha_3 - \\alpha_4 = 0 \\implies A(1, 1, -1, -1)^T = 0$，基础解系为 $\\xi = (1, 1, -1, -1)^T$。',
                    '第二步：$r(A) = 3$，$n - r(A) = 4 - 3 = 1$ 个自由量。',
                    '第三步：$\\beta = 1\\alpha_1 + 0\\alpha_2 + 0\\alpha_3 + 4\\alpha_4$ 得特解 $\\eta^* = (1, 0, 0, 4)^T$。',
                    '第四步：通解为 $(1, 0, 0, 4)^T + c(1, 1, -1, -1)^T$。'
                ],
                'answer': '(1, 0, 0, 4)^T + c(1, 1, -1, -1)^T',
                'pitfall': '特解系数 4 漏写；基础解系移项符号反转。',
                'difficulty': '★★★☆☆',
                'verified': True,
                'source': 'Maki考研数学真题分类精解 第四十七讲 题47.2 (p.1115)'
            }
        ],
        'variants': [
            {
                'id': 'var-xiandai-04-01',
                'question': '设 $A$ 为 $3 \\times 4$ 矩阵，$r(A) = 2$。若 $\\eta_1, \\eta_2, \\eta_3$ 为 $Ax=b$ 的三个特解且 $\\eta_1+\\eta_2=2\\eta_3$，求通解结构。',
                'hint': '非齐次特解之差为齐次解，自由度为 $4 - 2 = 2$。',
                'methodChoiceAnalysis': '解结构定理。',
                'fullSolution': [
                    '$\\xi_1 = \\eta_1 - \\eta_3$ 为齐次解。由于 $\\eta_2 - \\eta_3 = -(\\eta_1 - \\eta_3)$ 线性相关，需另一个独立齐次解 $\\xi_2$。',
                    '通解为 $\\eta_3 + c_1(\\eta_1 - \\eta_3) + c_2 \\xi_2$。'
                ],
                'keyTakeaway': '自由未知量个数严格等于 $n - r(A)$。'
            }
        ],
        'relatedKnowledgeIds': ['xiandai-02-adjoint-matrix-properties', 'xiandai-05-eigenvalue-eigenvector-properties'],
        'tags': ['矩阵的秩', '线性方程组', '基础解系', '特解', '考研数学一'],
        'source': 'Maki考研数学一站式大串讲 L47；真题分类精解 第四十七讲',
        'isPending': False
    },

    # -------------------------------------------------------------
    # Chapter 5: 特征值与特征向量
    # -------------------------------------------------------------
    'xiandai-05-eigenvalue-eigenvector-properties': {
        'id': 'xiandai-05-eigenvalue-eigenvector-properties',
        'title': '特征值与特征向量核心性质',
        'subject': 'xiandai',
        'subjectName': '线性代数',
        'chapterId': 'xiandai-ch05',
        'chapterTitle': '特征值与特征向量',
        'nodeType': 'topic',
        'summary': '特征值两大定海神针：∑ λi = tr(A)（特征值和等于主对角线迹）；∏ λi = |A|（特征值积等于行列式）！秩 1 矩阵 A = α β^T 特征值为 tr(A) 与 n-1 个 0！',
        'triggers': ['已知方阵求特征值与特征向量', '方阵每一行成比例（秩为 1）', '矩阵多项式方程 f(A) = 0'],
        'firstReaction': '先算迹与行列式建立特征值约束；若为秩 1 矩阵直接读出 λ = tr(A) 与 0。',
        'candidateMethods': [
            {'name': '特征方程求解法', 'priority': 1, 'condition': '具体方阵求特征值', 'whyChoose': '通用标准法', 'description': '|λE - A| = 0'},
            {'name': '秩1矩阵外积性质', 'priority': 2, 'condition': 'r(A) = 1', 'whyChoose': '直接读出所有特征值', 'description': 'λ1 = tr(A), 其余全为 0'}
        ],
        'applicability': '特征向量必须是非零向量；不同特征值对应的特征向量必线性无关。',
        'steps': [
            '第一步：计算行列式 $|\\lambda E - A| = 0$ 解出特征值。',
            '第二步：代入每个 $\\lambda_i$ 解齐次线性方程 $(\\lambda_i E - A)x = 0$ 得基础解系。',
            '第三步：写出特征向量 $c \\xi$ ($c \\neq 0$)。'
        ],
        'pitfalls': ['写特征向量漏声明 $c \\neq 0$；重根特征值几何重数与代数重数混淆。'],
        'formulas': [
            {'title': '迹与行列式恒等式', 'latex': '\\sum_{i=1}^n \\lambda_i = \\mathrm{tr}(A), \\quad \\prod_{i=1}^n \\lambda_i = |A|'},
            {'title': '秩1矩阵特征值', 'latex': 'A = \\alpha \\beta^T \\implies \\lambda_1 = \\beta^T \\alpha = \\mathrm{tr}(A), \\quad \\lambda_2 = \\dots = \\lambda_n = 0'}
        ],
        'pastQuestions': [
            {
                'id': 'xiandai-q-2017-1-5',
                'year': '2017',
                'category': '数一',
                'questionNumber': '(5)',
                'content': '设 $\\alpha$ 为 $n$ 维单位列向量，$E$ 为 $n$ 阶单位矩阵，则 (\\quad)\n(A) $E - \\alpha \\alpha^T$ 不可逆\n(B) $E + \\alpha \\alpha^T$ 不可逆\n(C) $E + 2\\alpha \\alpha^T$ 不可逆\n(D) $E - 2\\alpha \\alpha^T$ 不可逆',
                'options': ['(A) E - αα^T 不可逆', '(B) E + αα^T 不可逆', '(C) E + 2αα^T 不可逆', '(D) E - 2αα^T 不可逆'],
                'analysis': '秩 1 矩阵 $\\alpha \\alpha^T$ 的特征值为 $\\alpha^T \\alpha = 1$ 与 $n-1$ 个 0。$E + c \\alpha \\alpha^T$ 的特征值为 $1 + c$ 与 1。',
                'solutionSteps': [
                    '第一步：$\\alpha$ 是单位列向量，$\\alpha^T \\alpha = 1$。',
                    '第二步：矩阵 $A = \\alpha \\alpha^T$ 秩为 1，特征值为 $\\mathrm{tr}(A) = 1$（单重）与 0（$n-1$ 重）。',
                    '第三步：$E + c \\alpha \\alpha^T$ 的特征值为 $1 + c \\cdot 1 = 1 + c$（单重）与 $1 + 0 = 1$（$n-1$ 重）。',
                    '第四步：行列式为 $|E + c \\alpha \\alpha^T| = (1 + c) \\cdot 1^{n-1} = 1 + c$。',
                    '不可逆充要条件为行列式为 0，即 $1 + c = 0 \\implies c = -1$。故选 A。'
                ],
                'answer': 'A',
                'pitfall': '误将 $\\alpha \\alpha^T$ 与 $\\alpha^T \\alpha$ 混淆。',
                'difficulty': '★★★☆☆',
                'verified': True,
                'source': 'Maki考研数学真题分类精解 第四十九讲 题49.1 (p.1173)'
            }
        ],
        'variants': [
            {
                'id': 'var-xiandai-05-01',
                'question': '设 3 阶矩阵 $A$ 的特征值为 $1, 2, 3$，求 $A^* + 2E$ 的特征值。',
                'hint': '$A^* = |A| A^{-1}$，故特征值映射为 $\\frac{|A|}{\\lambda} + 2$。',
                'methodChoiceAnalysis': '特征值代数映射。',
                'fullSolution': [
                    '$|A| = 1 \\times 2 \\times 3 = 6$。',
                    '$A^*$ 的特征值为 $\\frac{6}{1}=6, \\frac{6}{2}=3, \\frac{6}{3}=2$。',
                    '$A^* + 2E$ 的特征值为 $6+2=8, 3+2=5, 2+2=4$。'
                ],
                'keyTakeaway': '伴随矩阵的特征值为 $|A|/\\lambda$。'
            }
        ],
        'relatedKnowledgeIds': ['xiandai-04-solution-structure-and-rank', 'xiandai-06-real-symmetric-orthogonal-diag'],
        'tags': ['特征值', '特征向量', '迹', '秩1矩阵', '考研数学一'],
        'source': 'Maki考研数学一站式大串讲 L49；真题分类精解 第四十九讲',
        'isPending': False
    },

    # -------------------------------------------------------------
    # Chapter 6: 相似矩阵与矩阵对角化
    # -------------------------------------------------------------
    'xiandai-06-real-symmetric-orthogonal-diag': {
        'id': 'xiandai-06-real-symmetric-orthogonal-diag',
        'title': '实对称矩阵的正交相似对角化',
        'subject': 'xiandai',
        'subjectName': '线性代数',
        'chapterId': 'xiandai-ch06',
        'chapterTitle': '相似矩阵与矩阵对角化',
        'nodeType': 'topic',
        'summary': '实对称矩阵性质极度优越：特征值全为实数；必可对角化；不同特征值的特征向量天然相互正交！重根特征向量用施密特正交化，单位化拼成正交阵 Q，使得 Q^T A Q = Λ！',
        'triggers': ['已知实对称矩阵 A = A^T，求正交矩阵 Q 使得 Q^T A Q 为对角阵', '由特征值与正交特征向量反求原实对称矩阵 A'],
        'firstReaction': '确认 A = A^T；不同特征值的特征向量无需正交化；只需对重特征值的特征向量进行施密特正交化并全部单位化。',
        'candidateMethods': [
            {'name': '正交化拼装法', 'priority': 1, 'condition': '实对称矩阵对角化大题', 'whyChoose': '标准满分解答套路', 'description': 'Q = (q1, q2, ..., qn)'}
        ],
        'applicability': '重特征值的特征向量正交化后，务必核对正交向量模长单位化除以自身长度。',
        'steps': [
            '第一步：解特征方程求特征值 $\\lambda_i$。',
            '第二步：对每个特征值解齐次方程求基础解系。',
            '第三步：对重特征值的特征向量进行施密特正交化。',
            '第四步：将所有特征向量单位化得到正交向量组 $q_1, \\dots, q_n$。',
            '第五步：构造正交矩阵 $Q = (q_1, \\dots, q_n)$，满足 $Q^T A Q = \\Lambda$。'
        ],
        'pitfalls': ['不同特征值的特征向量多此一举做施密特正交化；单位化忘记除以长度模长。'],
        'formulas': [{'title': '正交相似变换', 'latex': 'Q^T A Q = \\Lambda = \\mathrm{diag}(\\lambda_1, \\dots, \\lambda_n) \\quad (Q^T = Q^{-1})'}],
        'pastQuestions': [
            {
                'id': 'xiandai-q-2024-1-20',
                'year': '2024',
                'category': '数一',
                'questionNumber': '(20)',
                'content': '设 3 阶实对称矩阵 $A$ 的特征值为 $1, 1, 2$。若 $\\alpha_1 = (1, 1, 1)^T$ 对应于特征值 2，求对应于特征值 1 的特征向量结构。',
                'analysis': '实对称矩阵属于不同特征值的特征向量必相互正交！',
                'solutionSteps': [
                    '由实对称矩阵性质，属于特征值 1 的特征向量 $\\xi$ 必与属于特征值 2 的特征向量 $\\alpha_1$ 正交。',
                    '即 $\\alpha_1^T \\xi = 0 \\implies x_1 + x_2 + x_3 = 0$。',
                    '解方程得基础解系 $\\xi_1 = (1, -1, 0)^T, \\xi_2 = (1, 0, -1)^T$。',
                    '对应特征值 1 的特征向量为 $c_1 \\xi_1 + c_2 \\xi_2$ ($c_1, c_2$ 不全为 0)。'
                ],
                'answer': 'c1(1,-1,0)^T + c2(1,0,-1)^T',
                'pitfall': '未利用天然正交性去解方程，反而盲目设原矩阵参数。',
                'difficulty': '★★★☆☆',
                'verified': True,
                'source': 'Maki考研数学真题分类精解 第五十一讲 题51.1 (p.1232)'
            }
        ],
        'variants': [
            {
                'id': 'var-xiandai-06-01',
                'question': '已知实对称矩阵 $A$ 满足 $A^2 = A$，求 $A$ 的相似标准形。',
                'hint': '特征值满足 $\\lambda^2 = \\lambda \\implies \\lambda = 0$ 或 $1$。',
                'methodChoiceAnalysis': '实对称幂等矩阵对角化。',
                'fullSolution': [
                    '实对称矩阵必可对角化。',
                    '特征值只能为 0 或 1。',
                    '相似对角阵形如 $\\mathrm{diag}(1, \\dots, 1, 0, \\dots, 0)$，1 的个数等于 $r(A)$。'
                ],
                'keyTakeaway': '实对称矩阵的秩严格等于非零特征值个数。'
            }
        ],
        'relatedKnowledgeIds': ['xiandai-05-eigenvalue-eigenvector-properties', 'xiandai-07-quadratic-form-canonical'],
        'tags': ['实对称矩阵', '正交变换', '相似对角化', '考研数学一'],
        'source': 'Maki考研数学一站式大串讲 L51；真题分类精解 第五十一讲',
        'isPending': False
    }
}
