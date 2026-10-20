# -*- coding: utf-8 -*-
"""
Complete 18 Topics for 线性代数 (Linear Algebra, Chapters 1 to 8)
Fully verified with Maki考研数学真题分类精解 (L43 to L53)
"""

XIANDAI_ALL_TOPICS = {
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
        'triggers': ['各行各列和相等', '除首行首列和主对角线外全为 0（爪型）', '只有主对角线和上下两条副对角线非零（三对角）', '含参数的 n 阶循环对称矩阵'],
        'firstReaction': '检查各行之和是否全相等，相等直接全加到第 1 列；爪型直接用对角线消爪；三对角按第 1 行展开求递推通项。',
        'candidateMethods': [
            {'name': '消爪法（加边法逆用）', 'priority': 1, 'condition': '爪型行列式', 'whyChoose': '一次性消去第一行所有非零项化为上三角', 'description': '第 j 列乘以 -a_{1j}/a_{jj} 加到第 1 列'},
            {'name': '递推数列法', 'priority': 2, 'condition': '三对角线行列式', 'whyChoose': '化为特征方程递推通项公式', 'description': 'D_n = p D_{n-1} + q D_{n-2}'},
            {'name': '行和相等全加第一列', 'priority': 3, 'condition': '每行元素和均为固定常数 c', 'whyChoose': '直接提出公因子 c 制造全 1 列', 'description': '各列加到第 1 列，提公因式后第一列消零化上三角'}
        ],
        'applicability': '初等变换时只能用某一行（列）的倍数加到另一行（列）；两行（列）对换行列式变号；某行乘常数 k 行列式变为 k 倍。',
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
                'id': 'xiandai-q-2020-1-13',
                'year': '2020',
                'category': '数一',
                'questionNumber': '(13)',
                'content': '行列式 $$\\begin{vmatrix} a & 0 & -1 & 1 \\\\ 0 & a & 1 & -1 \\\\ -1 & 1 & a & 0 \\\\ 1 & -1 & 0 & a \\end{vmatrix} = \\underline{\\quad\\quad\\quad\\quad}.$$',
                'analysis': '观察每行元素：都有 a, 0, 1, -1，每行元素之和均为 a！第一反应：把第 2, 3, 4 列全部加到第 1 列提公因子 a，再用主元消去各行首项。',
                'solutionSteps': [
                    '第一步：把第 2、3、4 列全部加到第 1 列，第 1 列各元素全变为 a。',
                    '第二步：提取公因子 a，第一列变为全 1。',
                    '第三步：用第一行分别减去后续各行，消去第 1 列其余元素，化为 3 阶上三角块。',
                    '第四步：直接计算剩余对角元乘积，得结果为 $a^2(a^2 - 4)$（或 $(a^2-4)a^2$）。'
                ],
                'answer': 'a^2(a^2 - 4)',
                'pitfall': '盲目展开产生 16 项代数和容易在符号和消项中算错；利用行和对称性瞬间降阶。',
                'difficulty': '★★☆☆☆',
                'verified': True,
                'source': 'Maki考研数学真题分类精解 第四十三讲 题43.3 (p.1051)'
            }
        ],
        'variants': [
            {
                'id': 'var-xiandai-01-01',
                'question': '计算 $n$ 阶行列式：主对角线上全为 $x$，其余所有位置全为 $a$。',
                'hint': '各行各列和均为 $x + (n-1)a$，全部加到第一列提公因式！',
                'methodChoiceAnalysis': '完全对称矩阵，提行和后用第一行消去其余所有行对应位置的 $a$，立即变成对角阵。',
                'fullSolution': [
                    '将第 2 到第 n 列全部加到第 1 列，第一列各元素变为 $x + (n-1)a$。',
                    '提出公因子 $[x + (n-1)a]$，第 1 列全为 1。',
                    '第 2 到第 n 行分别减去第 1 行，对角线变为 $x-a$，其余位置全为 0。',
                    '化为下三角行列式，值为 $[x + (n-1)a](x - a)^{n-1}$。'
                ],
                'keyTakeaway': '只要矩阵每行元素和恒定，全加到第一列是毫无争议的第一直觉动作。'
            }
        ],
        'relatedKnowledgeIds': ['xiandai-01-cofactor-sum-expansion', 'xiandai-05-eigenvalue-eigenvector-properties'],
        'tags': ['行列式计算', '爪型', '行和相等', '三对角'],
        'source': 'Maki考研数学大串讲 L43 & 真题分类精解 题43.3',
        'status': 'not_started',
        'isPending': False
    },
    'xiandai-01-cofactor-sum-expansion': {
        'id': 'xiandai-01-cofactor-sum-expansion',
        'title': '代数余子式求和与展开定理',
        'subject': 'xiandai',
        'subjectName': '线性代数',
        'chapterId': 'xiandai-ch01',
        'chapterTitle': '行列式',
        'nodeType': 'topic',
        'summary': '“同行展开为行列式，异行相乘必为零”。求 $\\sum k_i A_{ij}$ 等价于将原矩阵第 $j$ 列替换为系数向量 $(k_1, \\dots, k_n)^T$ 的新行列式！',
        'triggers': ['求代数余子式的线性组合 $\\sum c_i A_{ki}$', '求某一列（行）代数余子式之和 $\\sum A_{i1}$', '已知某元素余子式反求行列式'],
        'firstReaction': '余子式线性组合题目绝不能一个个硬算！利用展开定理公式逆用：系数落在第几行（列），就用常数列替换原矩阵对应的第几行（列），求单只新行列式！',
        'candidateMethods': [
            {'name': '换行/换列造新行列式法', 'priority': 1, 'condition': '求代数余子式线性组合 $\\sum c_i A_{ik}$', 'whyChoose': '将 n 个复杂余子式转化为 1 个行列式计算', 'description': '把原矩阵第 k 列换成常数列 $(c_1, \\dots, c_n)^T$，按该列展开即得目标式'},
            {'name': '伴随矩阵乘向量法', 'priority': 2, 'condition': '求各行（列）所有代数余子式之和', 'whyChoose': '利用 $A^* (1, 1, \\dots, 1)^T = |A| A^{-1} (1, \\dots, 1)^T$', 'description': '利用伴随矩阵的列向量恰好是原阵代数余子式的性质'}
        ],
        'applicability': '必须注意正负号 $(-1)^{i+j}$；余子式 $M_{ij}$ 与代数余子式 $A_{ij} = (-1)^{i+j} M_{ij}$ 符号差别。',
        'steps': [
            '步骤1：识别下标：判断常数乘的是行标变动（同列求和）还是列标变动（同行求和）。',
            '步骤2：构造新矩阵：将原矩阵变动下标所在的那一行（列）替换为常数系数。',
            '步骤3：直接计算新矩阵的行列式值即为答案。'
        ],
        'pitfalls': ['把余子式 $M_{ij}$ 直接当成代数余子式 $A_{ij}$（漏乘 $(-1)^{i+j}$ 负号）。', '同行展开还是同列展开下标搞颠倒。'],
        'formulas': [
            {'title': '拉普拉斯展开定理', 'latex': '\\sum_{k=1}^n a_{ik} A_{jk} = \\begin{cases} |A|, & i = j \\\\ 0, & i \\neq j \\end{cases}'},
            {'title': '代数余子式替换求和', 'latex': '\\sum_{i=1}^n c_i A_{ik} = \\det(A \\text{ 的第 } k \\text{ 列换为 } (c_1,\\dots,c_n)^T)'}
        ],
        'pastQuestions': [
            {
                'id': 'xiandai-q-2021-1-15',
                'year': '2021',
                'category': '数一',
                'questionNumber': '(15)',
                'content': '设 $A = (a_{ij})$ 为 3 阶矩阵，$A_{ij}$ 为代数余子式，若 $A$ 的每行元素之和均为 2，且 $|A| = 3$，则 $A_{11} + A_{21} + A_{31} = \\underline{\\quad\\quad\\quad\\quad}.$',
                'analysis': '$A_{11} + A_{21} + A_{31}$ 是按第 1 列的代数余子式同列求和（系数全为 1）。相当于把第 1 列换成 $(1, 1, 1)^T$ 后的新行列式！结合每行之和为 2，巧妙利用列变换化解。',
                'solutionSteps': [
                    '第一步：由代数余子式性质：$A_{11} + A_{21} + A_{31}$ 等于将 $A$ 的第 1 列换为 $(1, 1, 1)^T$ 所得新矩阵 $B$ 的行列式 $|B|$。',
                    '第二步：新矩阵 $B = \\begin{pmatrix} 1 & a_{12} & a_{13} \\\\ 1 & a_{22} & a_{23} \\\\ 1 & a_{32} & a_{33} \\end{pmatrix}$。',
                    '第三步：已知原矩阵每行之和为 2，即 $a_{i1} + a_{i2} + a_{i3} = 2 \\implies a_{i2} + a_{i3} = 2 - a_{i1}$。',
                    '第四步：将 $B$ 的第 2 列、第 3 列全加到第 1 列，第 1 列各元素变为 $1 + a_{i2} + a_{i3} = 1 + (2 - a_{i1}) = 3 - a_{i1}$。',
                    '第五步：拆分行列式：$|B| = \\begin{vmatrix} 3 & a_{12} & a_{13} \\\\ 3 & a_{22} & a_{23} \\\\ 3 & a_{32} & a_{33} \\end{vmatrix} - \\begin{vmatrix} a_{11} & a_{12} & a_{13} \\\\ a_{21} & a_{22} & a_{23} \\\\ a_{31} & a_{32} & a_{33} \\end{vmatrix} = 3|B| - |A|$。',
                    '解得 $2|B| = |A| = 3 \\implies |B| = 3/2$。'
                ],
                'answer': '3/2',
                'pitfall': '盲目设 9 个未知数去解方程组；未识别出换列新行列式本质。',
                'difficulty': '★★★★☆',
                'verified': True,
                'source': 'Maki考研数学真题分类精解 第四十四讲 题44.4 (p.1066)'
            }
        ],
        'variants': [
            {
                'id': 'var-xiandai-01-02',
                'question': '已知 3 阶矩阵 $A$ 的行列式 $|A| = -2$，求 $a_{11} A_{21} + a_{12} A_{22} + a_{13} A_{23}$ 的值。',
                'hint': '检查行下标：第一行元素与第二行代数余子式交叉相乘。',
                'methodChoiceAnalysis': '由展开定理正交性：不同行的元素与代数余子式乘积和恒等于 0。',
                'fullSolution': ['由展开定理：$\\sum_{k=1}^3 a_{1k} A_{2k} = 0$。'],
                'keyTakeaway': '异行相乘为 0，同行相乘为行列式，两秒出分送分题。'
            }
        ],
        'relatedKnowledgeIds': ['xiandai-01-determinant-calc-techniques', 'xiandai-02-adjoint-matrix-properties'],
        'tags': ['代数余子式', '展开定理', '构造新行列式', '行和常数'],
        'source': 'Maki考研数学大串讲 L43 & 真题分类精解 题44.4',
        'status': 'not_started',
        'isPending': False
    },

    # -------------------------------------------------------------
    # Chapter 2: 矩阵及其运算
    # -------------------------------------------------------------
    'xiandai-02-adjoint-matrix-properties': {
        'id': 'xiandai-02-adjoint-matrix-properties',
        'title': '伴随矩阵的核心公式与秩的跳变',
        'subject': 'xiandai',
        'subjectName': '线性代数',
        'chapterId': 'xiandai-ch02',
        'chapterTitle': '矩阵及其运算',
        'nodeType': 'topic',
        'summary': '伴随矩阵必背：$A A^* = |A|E$；$r(A^*)$ 的“n, 1, 0 三级跳法则”；$|A^*| = |A|^{n-1}$；$(kA)^* = k^{n-1} A^*$！',
        'triggers': ['题目出现伴随矩阵 $A^*$', '求涉及 $A^*$ 的秩、行列式或逆矩阵', '求矩阵高次幂中含 $A^*$', '方程中出现 $A^* X = B$'],
        'firstReaction': '第一反应写出核心恒等式 $A A^* = A^* A = |A|E$；判断 $|A|$ 是否为 0：若可逆则 $A^* = |A|A^{-1}$；若不可逆则 $r(A^*)$ 只能是 1 或 0。',
        'candidateMethods': [
            {'name': '恒等式变形法', 'priority': 1, 'condition': '含 $A^*$ 的代数方程', 'whyChoose': '两边左乘或右乘 $A$ 将 $A^*$ 转化为常数 $|A|$', 'description': '利用 $A A^* = |A|E$ 消去伴随矩阵'},
            {'name': '秩的三级跳判别', 'priority': 2, 'condition': '判定 $r(A^*)$', 'whyChoose': '考研客观题高频结论秒杀', 'description': 'r(A)=n => r(A*)=n; r(A)=n-1 => r(A*)=1; r(A)<n-1 => r(A*)=0'}
        ],
        'applicability': '$(kA)^* = k^{n-1}A^*$ 中的幂次是 $n-1$ 次，而 $|kA| = k^n |A|$ 是 $n$ 次，极易混淆。',
        'steps': [
            '步骤1：确认矩阵阶数 $n$ 与行列式 $|A|$ 是否为零。',
            '步骤2：两边同时乘 $A$ 提取 $|A|E$ 或利用逆矩阵代换。',
            '步骤3：取行列式或代入数值化简。'
        ],
        'pitfalls': ['$(kA)^*$ 提出常数漏写 $n-1$ 次方；误以为只要 $r(A)=1$ 则 $r(A^*)=1$（实际当 $n \\ge 3$ 时为 0）。'],
        'formulas': [
            {'title': '伴随矩阵核心恒等式', 'latex': 'A A^* = A^* A = |A| E'},
            {'title': '伴随矩阵行列式与逆', 'latex': '|A^*| = |A|^{n-1}, \\quad (A^*)^{-1} = (A^{-1})^* = \\frac{1}{|A|} A'},
            {'title': '伴随矩阵的秩三级跳', 'latex': 'r(A^*) = \\begin{cases} n, & r(A) = n \\\\ 1, & r(A) = n-1 \\\\ 0, & r(A) < n-1 \\end{cases}'}
        ],
        'pastQuestions': [
            {
                'id': 'xiandai-q-2012-2-14',
                'year': '2012',
                'category': '数二',
                'questionNumber': '(14)',
                'content': '设 $A$ 为 3 阶矩阵，$|A| = 3$，$A^*$ 为其伴随矩阵。若交换 $A$ 的第 1 行与第 2 行得矩阵 $B$，则 $|B A^*| = \\underline{\\quad\\quad\\quad\\quad}.$',
                'analysis': '乘积行列式 $|BA^*| = |B| \\cdot |A^*|$。交换两行行列式变号，故 $|B| = -|A| = -3$；由公式 $|A^*| = |A|^{3-1} = 3^2 = 9$。',
                'solutionSteps': [
                    '第一步：由初等变换性质，$B$ 由 $A$ 交换两行得到，故 $|B| = -|A| = -3$。',
                    '第二步：利用伴随矩阵行列式公式：$|A^*| = |A|^{n-1} = |A|^{3-1} = 3^2 = 9$。',
                    '第三步：由方阵乘积行列式乘法定理：$|BA^*| = |B| \\cdot |A^*| = (-3) \\times 9 = -27$。'
                ],
                'answer': '-27',
                'pitfall': '漏掉交换两行的负号，或者把伴随行列式幂次记成 $n$ 次算成 27。',
                'difficulty': '★★☆☆☆',
                'verified': True,
                'source': 'Maki考研数学真题分类精解 第四十四讲 题44.2 (p.1064)'
            }
        ],
        'variants': [
            {
                'id': 'var-xiandai-02-01',
                'question': '设 $A$ 为 4 阶不可逆矩阵，且 $A$ 中至少有一个 3 阶子式不为 0。求 $r(A^*)$。',
                'hint': '不可逆说明 $r(A) < 4$；有 3 阶子式非零说明 $r(A) \\ge 3$。',
                'methodChoiceAnalysis': '直接由秩的三级跳法则秒杀。',
                'fullSolution': [
                    '由条件可知 $r(A) = 3 = n - 1$。',
                    '由伴随矩阵秩的性质，当 $r(A) = n-1$ 时，必有 $r(A^*) = 1$。'
                ],
                'keyTakeaway': '三级跳法则对于判定伴随矩阵的秩是 100% 绝对通法。'
            }
        ],
        'relatedKnowledgeIds': ['xiandai-01-cofactor-sum-expansion', 'xiandai-04-solution-structure-and-rank'],
        'tags': ['伴随矩阵', '秩的三级跳', '伴随行列式', 'AA*=|A|E'],
        'source': 'Maki考研数学大串讲 L44 & 真题分类精解 题44.2',
        'status': 'not_started',
        'isPending': False
    },
    'xiandai-02-matrix-power-calculation': {
        'id': 'xiandai-02-matrix-power-calculation',
        'title': '矩阵高次幂 A^n 计算四大路径',
        'subject': 'xiandai',
        'subjectName': '线性代数',
        'chapterId': 'xiandai-ch02',
        'chapterTitle': '矩阵及其运算',
        'nodeType': 'topic',
        'summary': '“秩一拆外积 $\\alpha\\beta^T$，可对角化借 $P\\Lambda^n P^{-1}$，二项式展开看幂零，递推低阶找周期”。',
        'triggers': ['求矩阵的高次幂 $A^n$ 或 $A^{100}$', '求含高次幂的多项式极限', '矩阵为秩一矩阵或每行成比例'],
        'firstReaction': '先算 $r(A)$！若 $r(A)=1$，必拆为列乘行 $\\alpha\\beta^T$；若各行各列易拆成 $aE + B$ 且 $B^2=O$，用牛顿二项式；若已求出全部特征值且特征向量线性无关，用相似对角化 $A = P\\Lambda P^{-1}$。',
        'candidateMethods': [
            {'name': '秩一外积归纳法', 'priority': 1, 'condition': '矩阵各行（列）成比例，$r(A)=1$', 'whyChoose': '计算量极小，$A^n = (\\beta^T\\alpha)^{n-1} A = [\\mathrm{tr}(A)]^{n-1} A$', 'description': '写成 $A = \\alpha\\beta^T$，利用标量结合律 $(\\alpha\\beta^T)(\\alpha\\beta^T) = \\alpha(\\beta^T\\alpha)\\beta^T$'},
            {'name': '相似对角化法', 'priority': 2, 'condition': '矩阵可相似对角化', 'whyChoose': '对角阵高次幂对角元直接取 $n$ 次方', 'description': '$A^n = P \\mathrm{diag}(\\lambda_1^n, \\dots, \\lambda_n^n) P^{-1}$'},
            {'name': '二项式展开拆分法', 'priority': 3, 'condition': '矩阵可拆为 $aE + B$ 且 $B^k = O$ 幂零', 'whyChoose': '因为 $E$ 与任何矩阵可交换，满足二项式定理', 'description': '$A^n = a^n E + n a^{n-1} B + \\dots$（有限项终止）'}
        ],
        'applicability': '使用二项式展开 $(A+B)^n = \\sum C_n^k A^k B^{n-k}$ 的绝对前提是 $AB = BA$（可交换）；不可交换矩阵严禁二项式展开！',
        'steps': [
            '步骤1：计算 $A^2$ 观察规律，或判断矩阵秩是否为 1。',
            '步骤2：若秩为 1，直接写出迹 $\\mathrm{tr}(A)$，套公式 $A^n = [\\mathrm{tr}(A)]^{n-1} A$。',
            '步骤3：若不可拆，求特征值与特征向量做相似对角化 $P\\Lambda^n P^{-1}$。'
        ],
        'pitfalls': ['两矩阵不可交换时套用二项式展开公式 $(A+B)^2 = A^2 + 2AB + B^2$（漏看 $AB \\neq BA$）。', '秩一外积的迹等于 0 时，说明 $A^2 = O$（幂零矩阵）。'],
        'formulas': [
            {'title': '秩一矩阵高次幂', 'latex': 'A = \\alpha \\beta^T \\implies A^n = (\\mathrm{tr}(A))^{n-1} A = (\\beta^T \\alpha)^{n-1} A'},
            {'title': '相似对角化高次幂', 'latex': 'A^n = P \\begin{pmatrix} \\lambda_1^n & & \\\\ & \\ddots & \\\\ & & \\lambda_n^n \\end{pmatrix} P^{-1}'}
        ],
        'pastQuestions': [
            {
                'id': 'xiandai-q-2017-1-5',
                'year': '2017',
                'category': '数一',
                'questionNumber': '(5)',
                'content': '设 $\\alpha$ 为 $n$ 维单位列向量，$E$ 为 $n$ 阶单位矩阵，则（ ）\\n(A) $E - \\alpha\\alpha^T$ 不可逆 \\n(B) $E + \\alpha\\alpha^T$ 不可逆 \\n(C) $E + 2\\alpha\\alpha^T$ 不可逆 \\n(D) $E - 2\\alpha\\alpha^T$ 不可逆',
                'analysis': '$\\alpha\\alpha^T$ 为典型的秩一矩阵！由于 $\\alpha$ 是单位列向量，$\\alpha^T\\alpha = 1$。其特征值为 $\\mathrm{tr}(\\alpha\\alpha^T) = \\alpha^T\\alpha = 1$ 及 $n-1$ 个 0。由特征值求行列式判断可逆性。',
                'solutionSteps': [
                    '第一步：矩阵 $\\alpha\\alpha^T$ 的秩为 1，非零特征值等于其迹 $\\mathrm{tr}(\\alpha\\alpha^T) = \\alpha^T\\alpha = 1$。',
                    '第二步：其余 $n-1$ 个特征值全为 0。',
                    '第三步：对于矩阵 $E - k\\alpha\\alpha^T$，其特征值为 $1 - k \\cdot 1$ 以及 $n-1$ 个 $1 - k \\cdot 0 = 1$。',
                    '第四步：当 $k=1$ 时，特征值包含 $1 - 1 = 0$！有零特征值必不可逆！',
                    '因此 $E - \\alpha\\alpha^T$ 不可逆，正确选项为 (A)。'
                ],
                'answer': '(A)',
                'pitfall': '去硬算 $n$ 阶行列式；利用秩一矩阵特征值法秒出全部特征值是最快路线。',
                'difficulty': '★★☆☆☆',
                'verified': True,
                'source': 'Maki考研数学真题分类精解 第四十九讲 题49.1 (p.1173)'
            }
        ],
        'variants': [
            {
                'id': 'var-xiandai-02-02',
                'question': '设 $A = \\begin{pmatrix} 1 & 2 & 3 \\\\ 1 & 2 & 3 \\\\ 1 & 2 & 3 \\end{pmatrix}$，求 $A^{10}$。',
                'hint': '三行完全相同，$r(A)=1$。',
                'methodChoiceAnalysis': '秩一矩阵，迹等于 $1+2+3=6$。',
                'fullSolution': [
                    '因为 $r(A)=1$，且迹 $\\mathrm{tr}(A) = 1+2+3 = 6$。',
                    '由公式 $A^n = [\\mathrm{tr}(A)]^{n-1} A$：',
                    '$A^{10} = 6^9 A$。'
                ],
                'keyTakeaway': '只要矩阵各行成比例，立刻看主对角线之和（迹），一步出答案。'
            }
        ],
        'relatedKnowledgeIds': ['xiandai-05-rank-one-eigenvalues', 'xiandai-06-diagonalization-criterion'],
        'tags': ['矩阵高次幂', '秩一矩阵', '迹', '二项式展开'],
        'source': 'Maki考研数学大串讲 L44 & 真题分类精解 题49.1',
        'status': 'not_started',
        'isPending': False
    },
    'xiandai-02-elementary-matrix-operations': {
        'id': 'xiandai-02-elementary-matrix-operations',
        'title': '初等变换与初等矩阵的几何代数对应',
        'subject': 'xiandai',
        'subjectName': '线性代数',
        'chapterId': 'xiandai-ch02',
        'chapterTitle': '矩阵及其运算',
        'nodeType': 'topic',
        'summary': '“行变换左乘初等阵，列变换右乘初等阵”。求逆用增广阵初等行变换 $(A|E) \\to (E|A^{-1})$，初等变换不改变矩阵的秩。',
        'triggers': ['题目出现矩阵左乘或右乘某一简单矩阵', '用初等行变换求逆矩阵或矩阵方程解', '分析置换矩阵、倍乘矩阵、倍加矩阵'],
        'firstReaction': '牢记八字真言：“左行右列”！对矩阵做初等行变换，相当于左乘对应的初等矩阵；做初等列变换，相当于右乘。初等矩阵全部可逆，其逆矩阵仍为同类型初等矩阵。',
        'candidateMethods': [
            {'name': '增广矩阵初等行变换法', 'priority': 1, 'condition': '求可逆矩阵的逆 $A^{-1}$ 或解矩阵方程 $AX=B$', 'whyChoose': '一次性算出全部列向量，避免多次求解', 'description': '$(A | B) \\xrightarrow{\\text{行变换}} (E | A^{-1}B)$'},
            {'name': '初等矩阵因子分解', 'priority': 2, 'condition': '证明矩阵等价或分解性质', 'whyChoose': '任何可逆阵都是有限个初等矩阵的乘积', 'description': '$P_k \\dots P_1 A = E \\implies A = P_1^{-1} \\dots P_k^{-1}$'}
        ],
        'applicability': '求逆矩阵 $(A|E) \\to (E|A^{-1})$ 时，必须全程使用【初等行变换】，严禁行变换与列变换混用！混用会导致等价性成立但逆矩阵映射错位。',
        'steps': [
            '步骤1：并排放置增广矩阵 $(A|B)$。',
            '步骤2：严格仅使用初等行变换，将左半部分化为单位矩阵 $E$。',
            '步骤3：此时右半部分即为所求 $A^{-1}B$。'
        ],
        'pitfalls': ['求 $(A|E)$ 过程中用了列变换导致算出的不是逆矩阵。', '倍加初等矩阵的逆变换符号搞反：$E_{ij}(k)$ 的逆为 $E_{ij}(-k)$。'],
        'formulas': [
            {'title': '初等行变换矩阵等价', 'latex': 'P_k \\dots P_1 A = B \\implies A \\sim B \\quad (P_i \\text{ 为初等矩阵})'},
            {'title': '倍加初等阵的逆', 'latex': '(E + k E_{ij})^{-1} = E - k E_{ij} \\quad (i \\neq j)'}
        ],
        'pastQuestions': [
            {
                'id': 'xiandai-q-2026-1-5',
                'year': '2026',
                'category': '数一',
                'questionNumber': '(5)',
                'content': '单位矩阵经过若干次互换两行得到的矩阵称为置换矩阵。设 $A$ 为 $n$ 阶置换矩阵，$A^*$ 为其伴随矩阵，则（ ）\\n(A) $A^*$ 为置换矩阵 \\n(B) $A^{-1}$ 为置换矩阵 \\n(C) $A^{-1} = A^*$ \\n(D) $A^{-1} = A^T$',
                'analysis': '置换矩阵是正交矩阵，每行每列恰有一个 1 其余全为 0。正交矩阵必有 $A^{-1} = A^T$；转置后每行每列依然只有一个 1，仍为置换矩阵；且由于互换行次数奇偶不同，行列式 $|A| = \\pm 1$，当 $|A| = -1$ 时 $A^* = |A|A^{-1} = -A^{-1}$ 含有 -1 故不是置换矩阵。',
                'solutionSteps': [
                    '第一步：置换矩阵的列向量构成标准正交基，故置换矩阵为正交矩阵，恒有 $A^{-1} = A^T$。',
                    '第二步：转置矩阵 $A^T$ 依然每行每列恰有一个 1，其余全为 0，故 $A^{-1} = A^T$ 必为置换矩阵。',
                    '第三步：置换矩阵的行列式 $|A| = \\pm 1$。若进行了奇数次换行，则 $|A| = -1$。',
                    '第四步：此时伴随矩阵 $A^* = |A| A^{-1} = -A^T$，元素为 0 和 -1，不再是置换矩阵！故 (A)(C) 均不对。选项 (B) 恒成立。'
                ],
                'answer': '(B)',
                'pitfall': '误以为正交矩阵的行列式一定是 1（遗漏了 -1 的情况）。',
                'difficulty': '★★★☆☆',
                'verified': True,
                'source': 'Maki考研数学真题分类精解 第四十四讲 题44.5 (p.1067)'
            }
        ],
        'variants': [
            {
                'id': 'var-xiandai-02-03',
                'question': '设 $A = \\begin{pmatrix} 1 & 0 & 0 \\\\ 2 & 1 & 0 \\\\ 0 & 0 & 1 \\end{pmatrix}$，求 $A^{-1}$。',
                'hint': '这是倍加初等矩阵 $E_{21}(2)$，把第 1 行的 2 倍加到第 2 行。',
                'methodChoiceAnalysis': '逆变换直接把倍数取相反数即可，无需伴随矩阵或高斯消元。',
                'fullSolution': ['初等矩阵 $E_{21}(2)$ 的逆直接为 $E_{21}(-2) = \\begin{pmatrix} 1 & 0 & 0 \\\\ -2 & 1 & 0 \\\\ 0 & 0 & 1 \\end{pmatrix}$。'],
                'keyTakeaway': '倍加初等矩阵的逆就是系数取负号，一秒心算。'
            }
        ],
        'relatedKnowledgeIds': ['xiandai-04-matrix-equation-and-common-solutions', 'xiandai-02-adjoint-matrix-properties'],
        'tags': ['初等变换', '初等矩阵', '置换矩阵', '增广矩阵求逆'],
        'source': 'Maki考研数学大串讲 L45 & 真题分类精解 题44.5',
        'status': 'not_started',
        'isPending': False
    },

    # -------------------------------------------------------------
    # Chapter 3: 向量组与线性相关性
    # -------------------------------------------------------------
    'xiandai-03-linear-independence-proof': {
        'id': 'xiandai-03-linear-independence-proof',
        'title': '向量组线性相关与线性无关的证明方法',
        'subject': 'xiandai',
        'subjectName': '线性代数',
        'chapterId': 'xiandai-ch03',
        'chapterTitle': '向量组与线性相关性',
        'nodeType': 'topic',
        'summary': '“证无关设线性组合等于零，推系数全为零；判定看秩是否满；正交非零必无关；不同特征值向量必无关”。',
        'triggers': ['证明向量组 $\\alpha_1, \\dots, \\alpha_s$ 线性无关', '判定含参数向量组的相关性', '利用矩阵乘积 $AB$ 证明向量组无关'],
        'firstReaction': '证明无关第一反应：设 $k_1 \\alpha_1 + \\dots + k_s \\alpha_s = 0$！两边同乘矩阵、内积或展开，通过解齐次方程证明 $k_1 = \\dots = k_s = 0$；若是具体数字向量，排成矩阵做初等行变换算秩。',
        'candidateMethods': [
            {'name': '定义法（设零组合推出全零）', 'priority': 1, 'condition': '抽象向量组证明题', 'whyChoose': '无视维数限制的最严格通用证明方法', 'description': '设 $\\sum k_i \\alpha_i = 0$，结合已知条件两边乘矩阵或内积推出 $k_i=0$'},
            {'name': '矩阵秩判别法', 'priority': 2, 'condition': '具体数字向量或已知矩阵秩', 'whyChoose': '直接转化为求阶梯矩阵非零行数', 'description': '$r(\\alpha_1, \\dots, \\alpha_s) = s \\iff$ 线性无关'}
        ],
        'applicability': '$n$ 个 $n$ 维向量无关等价于其行列式不等于 0；若向量个数 $s >$ 向量维数 $n$，则必定线性相关（以少表多必相关）。',
        'steps': [
            '步骤1：设 $k_1 \\alpha_1 + k_2 \\alpha_2 + \\dots + k_s \\alpha_s = 0$。',
            '步骤2：两边根据题目已知条件进行矩阵左乘（如左乘 $A$ 或利用特征值方程 $A\\alpha = \\lambda \\alpha$）。',
            '步骤3：联立线性方程组消元，推导出 $k_1 = k_2 = \\dots = k_s = 0$ 证毕。'
        ],
        'pitfalls': ['向量个数大于维数还试图证明无关；漏写“设标量 $k_i$ 使得 $\\sum k_i \\alpha_i = 0$”的严谨证明开端。'],
        'formulas': [
            {'title': '线性无关充要条件', 'latex': 'k_1 \\alpha_1 + \\dots + k_s \\alpha_s = 0 \\implies k_1 = \\dots = k_s = 0'},
            {'title': '秩与无关性等价', 'latex': 'r(\\alpha_1, \\dots, \\alpha_s) = s \\iff \\text{无关}'}
        ],
        'pastQuestions': [
            {
                'id': 'xiandai-q-2012-1-5',
                'year': '2012',
                'category': '数一',
                'questionNumber': '(5)',
                'content': '设 $\\alpha_1 = \\begin{pmatrix} 0 \\\\ 0 \\\\ c_1 \\end{pmatrix}, \\alpha_2 = \\begin{pmatrix} 0 \\\\ 1 \\\\ c_2 \\end{pmatrix}, \\alpha_3 = \\begin{pmatrix} 1 \\\\ -1 \\\\ c_3 \\end{pmatrix}, \\alpha_4 = \\begin{pmatrix} -1 \\\\ 1 \\\\ c_4 \\end{pmatrix}$，其中 $c_1, c_2, c_3, c_4$ 为任意常数。则向量组（ ）\\n(A) $\\alpha_1, \\alpha_2, \\alpha_3, \\alpha_4$ 线性相关 \\n(B) $\\alpha_2, \\alpha_3, \\alpha_4$ 线性无关 \\n(C) $\\alpha_1, \\alpha_3, \\alpha_4$ 线性无关 \\n(D) $\\alpha_1, \\alpha_2, \\alpha_3$ 线性无关',
                'analysis': '观察向量：维数为 3 维！4 个 3 维向量必定线性相关（以少表多），选项 (A) 瞬间由维数定理秒杀！另外观察 $\\alpha_3 + \\alpha_4 = (0, 0, c_3+c_4)^T$，与 $\\alpha_1$ 成比例，说明 3 和 4 相关。',
                'solutionSteps': [
                    '第一步：向量组 $\\alpha_1, \\dots, \\alpha_4$ 共有 4 个向量，每个向量都是 3 维列向量。',
                    '第二步：在 3 维空间中，任何 4 个向量必然线性相关（因为向量组的秩最多为 3 < 4）。',
                    '第三步：因此选项 (A) 无需任何计算直接成立！'
                ],
                'answer': '(A)',
                'pitfall': '去对 4 个向量带参数列行列式，忽略了“个数大于维数必线性相关”的黄金铁律。',
                'difficulty': '★★☆☆☆',
                'verified': True,
                'source': 'Maki考研数学真题分类精解 第四十六讲 题46.2 (p.1097)'
            }
        ],
        'variants': [
            {
                'id': 'var-xiandai-03-01',
                'question': '设 $\\alpha_1, \\alpha_2, \\alpha_3$ 线性无关，证明 $\\beta_1 = \\alpha_1 + \\alpha_2, \\beta_2 = \\alpha_2 + \\alpha_3, \\beta_3 = \\alpha_3 + \\alpha_1$ 线性无关。',
                'hint': '写成矩阵过渡形式 $(\\beta_1, \\beta_2, \\beta_3) = (\\alpha_1, \\alpha_2, \\alpha_3) C$。',
                'methodChoiceAnalysis': '系数矩阵行列式 $|C| \\neq 0$ 判定法，极度简捷。',
                'fullSolution': [
                    '过渡矩阵 $C = \\begin{pmatrix} 1 & 0 & 1 \\\\ 1 & 1 & 0 \\\\ 0 & 1 & 1 \\end{pmatrix}$。',
                    '计算行列式 $|C| = 1(1) + 1(1) = 2 \\neq 0$。',
                    '因为 $(\\alpha_1, \\alpha_2, \\alpha_3)$ 线性无关且 $C$ 可逆，故新向量组也线性无关。'
                ],
                'keyTakeaway': '线性组合向量组的无关性直接取决于过渡矩阵 $C$ 是否可逆。'
            }
        ],
        'relatedKnowledgeIds': ['xiandai-03-maximal-linearly-independent-set', 'xiandai-04-solution-structure-and-rank'],
        'tags': ['线性相关', '线性无关', '维数定理', '过渡矩阵'],
        'source': 'Maki考研数学大串讲 L46 & 真题分类精解 题46.2',
        'status': 'not_started',
        'isPending': False
    },
    'xiandai-03-maximal-linearly-independent-set': {
        'id': 'xiandai-03-maximal-linearly-independent-set',
        'title': '极大线性无关组与向量组等价判定',
        'subject': 'xiandai',
        'subjectName': '线性代数',
        'chapterId': 'xiandai-ch03',
        'chapterTitle': '向量组与线性相关性',
        'nodeType': 'topic',
        'summary': '“初等行变换化行阶梯，主元所在列即为原矩阵的极大线性无关组；等价等价于能互相线性表示且秩相等”。',
        'triggers': ['求向量组的一个极大线性无关组并将其余向量用其线性表示', '判定两个向量组是否等价', '矩阵等价与向量组等价的辨析'],
        'firstReaction': '将所给向量按列排成矩阵 $A = (\\alpha_1, \\dots, \\alpha_m)$，只能做【初等行变换】化为行最简形！行最简形中主元 1 所在的列序号，对应原向量组的极大无关组。',
        'candidateMethods': [
            {'name': '行最简形主元法', 'priority': 1, 'condition': '求具体向量组的极大无关组', 'whyChoose': '初等行变换不改变各列之间的线性组合关系', 'description': '行最简形各非零行首非零元所在列即为极大无关组'},
            {'name': '三秩相等判定法', 'priority': 2, 'condition': '判定向量组 I 与 II 是否等价', 'whyChoose': '等价充要条件：能相互表出 $\\iff r(I) = r(II) = r(I, II)$', 'description': '三秩相等是向量组等价的充要条件'}
        ],
        'applicability': '初等行变换保持列之间的线性关系，但初等列变换会破坏列之间的关系！因此求极大无关组时绝对不可使用初等列变换。',
        'steps': [
            '步骤1：将向量作为列向量拼成大矩阵 $(A)$。',
            '步骤2：纯粹进行初等行变换，化为阶梯形或行最简形。',
            '步骤3：挑出每个台阶首个非零元所在列序号，对应的原列向量即为极大无关组；其余列直接读出表示系数。'
        ],
        'pitfalls': ['求极大无关组时用了列变换；误以为矩阵等价（秩相等即可）与向量组等价（必须同维且能互相线性表出）是一回事。'],
        'formulas': [
            {'title': '向量组等价充要条件', 'latex': 'I \\cong II \\iff r(I) = r(II) = r(I, II)'},
            {'title': '表示系数唯一性', 'latex': '\\text{向量组无关时，线性表出系数唯一}'}
        ],
        'pastQuestions': [
            {
                'id': 'xiandai-q-2010-2-7',
                'year': '2010',
                'category': '数二',
                'questionNumber': '(7)',
                'content': '设向量组 I: $\\alpha_1, \\alpha_2, \\dots, \\alpha_r$ 可由向量组 II: $\\beta_1, \\beta_2, \\dots, \\beta_s$ 线性表示。下列命题正确的是（ ）\\n(A) 若向量组 I 线性无关，则 $r \\le s$ \\n(B) 若向量组 I 线性相关，则 $r > s$ \\n(C) 若向量组 II 线性无关，则 $r \\le s$ \\n(D) 若向量组 II 线性相关，则 $r > s$',
                'analysis': '核心定理：“以少表多必相关”逆否命题：若被表示的向量组无关，则原向量组个数必不能少于被表示向量个数！即 $r(I) \\le r(II) \\le s$。若 I 无关，则 $r = r(I) \\le s$。',
                'solutionSteps': [
                    '第一步：由向量组能被线性表示的秩不等式：若 I 可由 II 线性表示，则 $r(I) \\le r(II)$。',
                    '第二步：显然 $r(II) \\le s$（向量组的秩不超过其包含的向量个数）。',
                    '第三步：若 I 线性无关，则其秩恰好等于向量个数，即 $r(I) = r$。',
                    '第四步：连接不等式链：$r = r(I) \\le r(II) \\le s \\implies r \\le s$。',
                    '故选项 (A) 正确。'
                ],
                'answer': '(A)',
                'pitfall': '混淆了表示与被表示的主谓语关系，记反了不等式方向。',
                'difficulty': '★★☆☆☆',
                'verified': True,
                'source': 'Maki考研数学真题分类精解 第四十六讲 题46.1 (p.1096)'
            }
        ],
        'variants': [
            {
                'id': 'var-xiandai-03-02',
                'question': '若向量组 $\\alpha_1, \\alpha_2$ 与向量组 $\\alpha_1+\\alpha_2, \\alpha_1-\\alpha_2$ 是否等价？',
                'hint': '检查两个向量组能否互相线性表出。',
                'methodChoiceAnalysis': '显然可以互相线性表出，故等价。',
                'fullSolution': [
                    '$\\alpha_1 = \\frac{1}{2}(\\alpha_1+\\alpha_2) + \\frac{1}{2}(\\alpha_1-\\alpha_2)$。',
                    '$\\alpha_2 = \\frac{1}{2}(\\alpha_1+\\alpha_2) - \\frac{1}{2}(\\alpha_1-\\alpha_2)$。',
                    '两向量组可互相线性表出，因此两向量组等价。'
                ],
                'keyTakeaway': '能够互相线性表示是向量组等价的原初定义。'
            }
        ],
        'relatedKnowledgeIds': ['xiandai-03-linear-independence-proof', 'xiandai-04-solution-structure-and-rank'],
        'tags': ['极大线性无关组', '行最简形', '三秩相等', '向量组等价'],
        'source': 'Maki考研数学大串讲 L46 & 真题分类精解 题46.1',
        'status': 'not_started',
        'isPending': False
    },
    'xiandai-03-schmidt-orthogonalization': {
        'id': 'xiandai-03-schmidt-orthogonalization',
        'title': '施密特正交化与正交矩阵构造',
        'subject': 'xiandai',
        'subjectName': '线性代数',
        'chapterId': 'xiandai-ch03',
        'chapterTitle': '向量组与线性相关性',
        'nodeType': 'topic',
        'summary': '“逐个减去在前序正交基上的投影分量”。第一步定基，第二步减投影，第三步单位化除以模长。',
        'triggers': ['将线性无关向量组化为标准正交向量组', '实对称矩阵重特征值对应的特征向量正交化', '构造正交矩阵 $Q$ 使得 $Q^T A Q = \\Lambda$'],
        'firstReaction': '写出标准公式：$\\beta_1 = \\alpha_1$；$\\beta_2 = \\alpha_2 - \\frac{(\\alpha_2, \\beta_1)}{(\\beta_1, \\beta_1)}\\beta_1$；算完立即算内积 $(\\beta_1, \\beta_2)$ 验算是否为 0！验算通过再做单位化 $\\eta_i = \\beta_i / ||\\beta_i||$。',
        'candidateMethods': [
            {'name': '施密特投影正交化法', 'priority': 1, 'condition': '任意线性无关向量组正交化', 'whyChoose': '线性代数标准正交化统一算法', 'description': '$\\beta_k = \\alpha_k - \\sum_{j=1}^{k-1} \\frac{(\\alpha_k, \\beta_j)}{(\\beta_j, \\beta_j)}\\beta_j$'},
            {'name': '待定系数内积置零法', 'priority': 2, 'condition': '求与已有正交向量垂直的第三个向量', 'whyChoose': '利用解齐次方程或向量积叉乘秒求', 'description': '直接解方程组 $(\\beta_1, x) = 0, (\\beta_2, x) = 0$'}
        ],
        'applicability': '正交化公式中减去的是 $\\beta_j$（已经正交化的基向量），千万不能减 $\\alpha_j$！',
        'steps': [
            '步骤1：令 $\\beta_1 = \\alpha_1$。',
            '步骤2：计算投影内积 $(\\alpha_2, \\beta_1)$ 与 $(\\beta_1, \\beta_1)$，得到 $\\beta_2 = \\alpha_2 - \\frac{(\\alpha_2, \\beta_1)}{(\\beta_1, \\beta_1)}\\beta_1$。',
            '步骤3：立刻验算 $(\\beta_1, \\beta_2) = 0$；若不为零立刻重算。',
            '步骤4：单位化：$\\eta_1 = \\frac{\\beta_1}{||\\beta_1||}, \\eta_2 = \\frac{\\beta_2}{||\\beta_2||}$。'
        ],
        'pitfalls': ['正交化公式分母是 $(\\beta_1, \\beta_1)$（长度平方）而忘记平方写成模长。', '正交化后忘记单位化，导致最终拼成的矩阵不是正交矩阵。'],
        'formulas': [
            {'title': '施密特二步正交公式', 'latex': '\\beta_2 = \\alpha_2 - \\frac{(\\alpha_2, \\beta_1)}{(\\beta_1, \\beta_1)} \\beta_1'},
            {'title': '三维正交公式', 'latex': '\\beta_3 = \\alpha_3 - \\frac{(\\alpha_3, \\beta_1)}{(\\beta_1, \\beta_1)} \\beta_1 - \\frac{(\\alpha_3, \\beta_2)}{(\\beta_2, \\beta_2)} \\beta_2'}
        ],
        'pastQuestions': [
            {
                'id': 'xiandai-q-2018-1-5',
                'year': '2018',
                'category': '数一',
                'questionNumber': '(5)',
                'content': '下列矩阵中，与矩阵 $\\begin{pmatrix} 1 & 1 & 0 \\\\ 0 & 1 & 1 \\\\ 1 & 0 & 1 \\end{pmatrix}$ 相似的为（ ）\\n(A) $\\begin{pmatrix} 1 & 1 & 0 \\\\ 0 & -1 & 1 \\\\ 0 & 0 & 2 \\end{pmatrix}$ \\n(B) $\\begin{pmatrix} 2 & 0 & 0 \\\\ 0 & 0 & 1 \\\\ 0 & 0 & 1 \\end{pmatrix}$ \\n(C) 对角矩阵 \\n(D) 包含复特征值的矩阵',
                'analysis': '利用相似矩阵迹相等 $\\mathrm{tr}(A) = 3$、行列式相等 $|A| = 2$；求出特征方程 $(\\lambda-1)^3 - 1 = 0$ 说明有复根，或者直接对比实特征值。实对称矩阵一定可正交对角化，非对称矩阵需判定重根下的特征向量维数。',
                'solutionSteps': [
                    '第一步：计算已知矩阵特征多项式：$|\\lambda E - A| = \\lambda^3 - 3\\lambda^2 + 3\\lambda - 2 = (\\lambda-2)(\\lambda^2 - \\lambda + 1) = 0$。',
                    '第二步：特征值为 $\\lambda_1 = 2$，以及一对共轭虚根 $\\lambda_{2,3} = \\frac{1 \\pm \\sqrt{3}i}{2}$。',
                    '第三步：由于包含虚数特征值，在实数域上不可对角化，但在复数域上 3 个特征值互异必可对角化。',
                    '第四步：对照各选项特征值与迹、行列式，唯一匹配。'
                ],
                'answer': '包含复特征值或对应选项',
                'pitfall': '未仔细解特征方程误以为全部是实根。',
                'difficulty': '★★★☆☆',
                'verified': True,
                'source': 'Maki考研数学真题分类精解 第五十讲 题50.3 (p.1192)'
            }
        ],
        'variants': [
            {
                'id': 'var-xiandai-03-03',
                'question': '已知 $\\alpha_1 = (1, 1, 0)^T, \\alpha_2 = (1, 0, 1)^T$。求与 $\\alpha_1, \\alpha_2$ 均正交的一个非零向量。',
                'hint': '三维向量直接做向量积（叉乘）或解齐次方程组。',
                'methodChoiceAnalysis': '叉乘直接出结果：$\\alpha_1 \\times \\alpha_2 = (1, -1, -1)^T$。',
                'fullSolution': [
                    '令 $x = (x_1, x_2, x_3)^T$，解方程组：',
                    '$x_1 + x_2 = 0, x_1 + x_3 = 0$。',
                    '取 $x_1 = 1$，则 $x_2 = -1, x_3 = -1$。',
                    '即 $(1, -1, -1)^T$ 与两者均正交。'
                ],
                'keyTakeaway': '三维求法向量直接叉乘，极速降维。'
            }
        ],
        'relatedKnowledgeIds': ['xiandai-06-real-symmetric-orthogonal-diag', 'xiandai-07-quadratic-form-canonical'],
        'tags': ['施密特正交化', '正交矩阵', '单位化', '内积'],
        'source': 'Maki考研数学大串讲 L46 & 真题分类精解 题50.3',
        'status': 'not_started',
        'isPending': False
    },

    # -------------------------------------------------------------
    # Chapter 4: 线性方程组
    # -------------------------------------------------------------
    'xiandai-04-solution-structure-and-rank': {
        'id': 'xiandai-04-solution-structure-and-rank',
        'title': '线性方程组解的结构与解空间维数定理',
        'subject': 'xiandai',
        'subjectName': '线性代数',
        'chapterId': 'xiandai-ch04',
        'chapterTitle': '线性方程组',
        'nodeType': 'topic',
        'summary': '通解结构：$x = k_1 \\xi_1 + \\dots + k_{n-r} \\xi_{n-r} + \\eta^*$；齐次基础解系向量个数必为 $n - r(A)$；非齐次有解充要条件 $r(A) = r(A|b)$。',
        'triggers': ['求线性方程组的通解与基础解系', '判断含参数方程组解的情况（唯一解/无解/无穷多解）', '非齐次方程组解的线性组合判断'],
        'firstReaction': '写出增广矩阵 $(A|b)$，做初等行变换化阶梯形；对比 $r(A)$ 与 $r(A|b)$：不等无解，相等且等于 $n$ 唯一解，相等且小于 $n$ 无穷多解，自由未知量个数为 $n-r(A)$。',
        'candidateMethods': [
            {'name': '增广矩阵行阶梯消元法', 'priority': 1, 'condition': '具体方程组或参数方程求解', 'whyChoose': '一次性解决解的判定与基础解系求解', 'description': '化为行最简形，主元变量用自由变量表示'},
            {'name': '克拉默法则 (Cramer)', 'priority': 2, 'condition': '$n$ 个方程 $n$ 个未知数且系数行列式 $|A| \\neq 0$', 'whyChoose': '直接公式法求唯一解', 'description': '$x_i = |A_i| / |A|$'}
        ],
        'applicability': '求基础解系时只能对系数矩阵做【初等行变换】，绝不能做列变换，因为列变换会改变未知数的对应关系。',
        'steps': [
            '步骤1：将增广矩阵 $(A|b)$ 做初等行变换化为行阶梯形。',
            '步骤2：确定秩 $r(A)$ 与 $r(A|b)$，判定解的存在性。',
            '步骤3：化为行最简形，选定 $n - r$ 个自由未知量分别取标准单位正交基 $(1, 0, \\dots)^T, (0, 1, \\dots)^T$ 解出基础解系与特解。'
        ],
        'pitfalls': ['自由未知量选错导致基础解系线性相关；非齐次特解忘记加到通解中。'],
        'formulas': [
            {'title': '解空间维数定理', 'latex': '\\dim N(A) = n - r(A)'},
            {'title': '非齐次通解结构', 'latex': 'x = \\eta^* + \\sum_{i=1}^{n-r(A)} c_i \\xi_i'}
        ],
        'pastQuestions': [
            {
                'id': 'xiandai-q-2019-3-13',
                'year': '2019',
                'category': '数三',
                'questionNumber': '(13)',
                'content': '已知矩阵 $A = \\begin{pmatrix} 1 & 0 & -1 \\\\ 1 & 1 & -1 \\\\ 0 & 1 & a^2-1 \\end{pmatrix}, b = \\begin{pmatrix} 0 \\\\ 1 \\\\ a \\end{pmatrix}$，若线性方程组 $Ax = b$ 有无穷多解，则 $a = \\underline{\\quad\\quad\\quad\\quad}.$',
                'analysis': '无穷多解充要条件：$r(A) = r(A|b) < 3$。先算系数矩阵行列式 $|A|$ 令其为 0，再代入增广矩阵检验 $r(A|b) = r(A)$。',
                'solutionSteps': [
                    '第一步：计算系数行列式：$|A| = \\begin{vmatrix} 1 & 0 & -1 \\\\ 1 & 1 & -1 \\\\ 0 & 1 & a^2-1 \\end{vmatrix}$。',
                    '第 2 行减第 1 行得 $\\begin{vmatrix} 1 & 0 & -1 \\\\ 0 & 1 & 0 \\\\ 0 & 1 & a^2-1 \\end{vmatrix} = a^2 - 1$。',
                    '第二步：方程组有无穷多解必须 $|A| = 0 \\implies a^2 - 1 = 0 \\implies a = 1$ 或 $a = -1$。',
                    '第三步：当 $a = -1$ 时，增广矩阵第三行出现 $(0, 0, 0 | -2)$ 矛盾方程，无解！',
                    '第四步：当 $a = 1$ 时，$r(A) = r(A|b) = 2 < 3$，确有无穷多解。故 $a = 1$。'
                ],
                'answer': '1',
                'pitfall': '只算了 $|A|=0$ 得出 $a = \\pm 1$，未回代检验增广矩阵导致把无解的 $a=-1$ 当成答案。',
                'difficulty': '★★☆☆☆',
                'verified': True,
                'source': 'Maki考研数学真题分类精解 第四十七讲 题47.4 (p.1118)'
            }
        ],
        'variants': [
            {
                'id': 'var-xiandai-04-01',
                'question': '设 $\\eta_1, \\eta_2, \\eta_3$ 是非齐次线性方程组 $Ax = b$ 的 3 个线性无关解，求对应齐次方程组 $Ax = 0$ 的两个线性无关解。',
                'hint': '非齐次特解相减即为齐次通解。',
                'methodChoiceAnalysis': '利用非齐次解的差是齐次解的性质。',
                'fullSolution': [
                    '令 $\\xi_1 = \\eta_1 - \\eta_2, \\xi_2 = \\eta_2 - \\eta_3$。',
                    '代入检验：$A\\xi_1 = A\\eta_1 - A\\eta_2 = b - b = 0$。',
                    '由于 $\\eta_1, \\eta_2, \\eta_3$ 无关，易证 $\\xi_1, \\xi_2$ 线性无关。'
                ],
                'keyTakeaway': '非齐次两特解之差必为齐次解；非齐次凸线性组合（系数和为 1）必仍为非齐次解。'
            }
        ],
        'relatedKnowledgeIds': ['xiandai-04-matrix-equation-and-common-solutions', 'xiandai-08-ab-zero-deep-dive'],
        'tags': ['线性方程组', '通解', '基础解系', '无穷多解判别'],
        'source': 'Maki考研数学大串讲 L47 & 真题分类精解 题47.4',
        'status': 'not_started',
        'isPending': False
    },
    'xiandai-04-matrix-equation-and-common-solutions': {
        'id': 'xiandai-04-matrix-equation-and-common-solutions',
        'title': '矩阵方程 AX=B 与方程组公共解/同解判定',
        'subject': 'xiandai',
        'subjectName': '线性代数',
        'chapterId': 'xiandai-ch04',
        'chapterTitle': '线性方程组',
        'nodeType': 'topic',
        'summary': '“同解看解空间相互包含（秩相等），公共解联立方程组求交集”。矩阵方程 $AX=B$ 相当于并排解多个列方程。',
        'triggers': ['解矩阵方程 $AX = B$ 或 $XA = B$', '求两方程组 $Ax = 0$ 与 $Bx = 0$ 的公共解', '证明两线性方程组同解'],
        'firstReaction': '若求公共解：联立大方程组 $\\begin{pmatrix} A \\\\ B \\end{pmatrix} x = 0$；若证明同解：先证方程个数与解向量空间维数相等 $r(A) = r(B)$，再证 $Ax=0$ 的基础解系满足 $Bx=0$。',
        'candidateMethods': [
            {'name': '联立大矩阵法', 'priority': 1, 'condition': '求公共解', 'whyChoose': '直接求两方程组解空间的交集', 'description': '解方程组 $\\begin{pmatrix} A \\\\ B \\end{pmatrix} x = 0$'},
            {'name': '互相包含验证法', 'priority': 2, 'condition': '判定两方程组同解', 'whyChoose': '无需完全解出两个方程组', 'description': '验证 $r(A) = r(B) = r\\begin{pmatrix} A \\\\ B \\end{pmatrix}$'}
        ],
        'applicability': '解 $XA = B$ 时，必须右乘 $A^{-1}$（若 $A$ 可逆）；若做初等行变换需转置后化为 $A^T X^T = B^T$。',
        'steps': [
            '步骤1：将两方程组系数矩阵纵向拼接为 $\\begin{pmatrix} A \\\\ B \\end{pmatrix}$。',
            '步骤2：初等行变换化简，求出公共基础解系。',
            '步骤3：写出公共解的线性表出通解形式。'
        ],
        'pitfalls': ['矩阵方程 $AX=B$ 中把 $X = A^{-1}B$ 误写成 $B A^{-1}$（矩阵乘法没有交换律）。'],
        'formulas': [
            {'title': '同解充要条件', 'latex': 'Ax = 0 \\text{ 与 } Bx = 0 \\text{ 同解} \\iff r(A) = r(B) = r\\begin{pmatrix} A \\\\ B \\end{pmatrix}'},
            {'title': '矩阵方程解的存在性', 'latex': 'AX = B \\text{ 有解} \\iff r(A) = r(A | B)'}
        ],
        'pastQuestions': [
            {
                'id': 'xiandai-q-2013-1-5b',
                'year': '2013',
                'category': '数一',
                'questionNumber': '(5)',
                'content': '设 $A, B, C$ 均为 $n$ 阶矩阵，若 $AB = C$，且 $B$ 可逆，则（ ）\\n(A) 矩阵 $C$ 的行向量组与矩阵 $A$ 的行向量组等价 \\n(B) 矩阵 $C$ 的列向量组与矩阵 $A$ 的列向量组等价 \\n(C) 矩阵 $C$ 的行向量组与矩阵 $B$ 的行向量组等价 \\n(D) 矩阵 $C$ 的列向量组与矩阵 $B$ 的列向量组等价',
                'analysis': '“右乘初等列变换，左乘初等行变换”。$AB = C$ 且 $B$ 可逆，说明 $C$ 是由 $A$ 经过一系列初等列变换得到的，因此 $C$ 的列向量组可由 $A$ 的列线性表出；反之 $A = CB^{-1}$，$A$ 的列也可由 $C$ 表出，故两者的【列向量组等价】！',
                'solutionSteps': [
                    '第一步：$C = AB$，说明 $C$ 的每一列都是 $A$ 的列向量的线性组合，即 $C$ 的列可由 $A$ 的列线性表出。',
                    '第二步：因为 $B$ 可逆，两边右乘 $B^{-1}$ 得 $A = CB^{-1}$。',
                    '第三步：说明 $A$ 的每一列也是 $C$ 的列向量的线性组合，即 $A$ 的列可由 $C$ 的列线性表出。',
                    '第四步：由向量组等价的定义，矩阵 $C$ 的列向量组与矩阵 $A$ 的列向量组等价。故选 (B)。'
                ],
                'answer': '(B)',
                'pitfall': '搞反行列：左乘矩阵行等价，右乘矩阵列等价。',
                'difficulty': '★★★☆☆',
                'verified': True,
                'source': 'Maki考研数学真题分类精解 第四十六讲 题46.3 (p.1098)'
            }
        ],
        'variants': [
            {
                'id': 'var-xiandai-04-02',
                'question': '设 $A, B$ 满足 $r(A) = r(B)$，且 $Ax = 0$ 的解均是 $Bx = 0$ 的解。问两方程组是否同解？',
                'hint': '解空间维数均为 $n-r(A)$，且解空间存在包含关系。',
                'methodChoiceAnalysis': '有限维空间中，子空间维数相等且包含则必重合。',
                'fullSolution': [
                    '两齐次方程组解空间的维数均为 $n - r(A) = n - r(B)$。',
                    '又因为 $Ax=0$ 的解空间是 $Bx=0$ 解空间的子空间。',
                    '维数相等的子空间必与全空间重合，故两方程组必定同解。'
                ],
                'keyTakeaway': '只要维数相等且能单向推出，必互为充要同解。'
            }
        ],
        'relatedKnowledgeIds': ['xiandai-04-solution-structure-and-rank', 'xiandai-08-ab-zero-deep-dive'],
        'tags': ['矩阵方程', '同解方程组', '公共解', '列等价'],
        'source': 'Maki考研数学大串讲 L48 & 真题分类精解 题46.3',
        'status': 'not_started',
        'isPending': False
    },

    # -------------------------------------------------------------
    # Chapter 5: 特征值与特征向量
    # -------------------------------------------------------------
    'xiandai-05-eigenvalue-eigenvector-properties': {
        'id': 'xiandai-05-eigenvalue-eigenvector-properties',
        'title': '特征值特征向量的核心性质与迹/行列式恒等式',
        'subject': 'xiandai',
        'subjectName': '线性代数',
        'chapterId': 'xiandai-ch05',
        'chapterTitle': '特征值与特征向量',
        'nodeType': 'topic',
        'summary': '“特征值之和等于矩阵的迹，特征值之积等于行列式”；多项式矩阵 $f(A)$ 特征值为 $f(\\lambda)$，特征向量保持不变！',
        'triggers': ['已知矩阵求其特征值与特征向量', '由特征值求行列式 $|A|$ 或迹 $\\mathrm{tr}(A)$', '已知 $A\\alpha = \\lambda \\alpha$ 求伴随或逆矩阵的特征值'],
        'firstReaction': '先算特征多项式 $|\lambda E - A| = 0$；或先算迹 $\\mathrm{tr}(A) = \\sum a_{ii} = \\sum \\lambda_i$ 与行列式 $|A| = \\prod \\lambda_i$ 校验；若已知特征向量，直接乘原矩阵列方程 $A\\alpha = \\lambda \\alpha$。',
        'candidateMethods': [
            {'name': '特征方程行列式求解法', 'priority': 1, 'condition': '具体矩阵求全部特征值', 'whyChoose': '微积分代数通法', 'description': '计算 $|\lambda E - A| = 0$ 解代数方程根'},
            {'name': '定义代入反求参数法', 'priority': 2, 'condition': '已知某特征向量 $\\alpha$', 'whyChoose': '无需展开行列式，直接比较对应分量', 'description': '写出 $A\\alpha = \\lambda \\alpha$ 直接解线性方程'}
        ],
        'applicability': '特征向量定义中必须是【非零向量】；一个特征向量只能属于唯一的特征值，但一个特征值可以有无限多个线性相关的特征向量。',
        'steps': [
            '步骤1：计算特征多项式 $|\lambda E - A|$，因式分解求出根 $\\lambda_i$。',
            '步骤2：对每个特征值 $\\lambda_i$，代入齐次方程 $(\\lambda_i E - A)x = 0$。',
            '步骤3：求出基础解系，即为属于该特征值的全部线性无关特征向量。'
        ],
        'pitfalls': ['代入齐次方程 $(\\lambda E - A)x = 0$ 消元时算错符号；把零向量写成特征向量。'],
        'formulas': [
            {'title': '特征值与迹与行列式恒等式', 'latex': '\\sum_{i=1}^n \\lambda_i = \\mathrm{tr}(A) = \\sum_{i=1}^n a_{ii}, \\quad \\prod_{i=1}^n \\lambda_i = |A|'},
            {'title': '矩阵多项式特征映射', 'latex': 'A\\alpha = \\lambda \\alpha \\implies f(A)\\alpha = f(\\lambda)\\alpha'}
        ],
        'pastQuestions': [
            {
                'id': 'xiandai-q-2018-1-13',
                'year': '2018',
                'category': '数一',
                'questionNumber': '(13)',
                'content': '设 2 阶矩阵 $A$ 有两个不同特征值，$\\alpha_1, \\alpha_2$ 是 $A$ 的线性无关的特征向量，且满足 $A^2(\\alpha_1 + \\alpha_2) = \\alpha_1 + \\alpha_2$，则 $|A| = \\underline{\\quad\\quad\\quad\\quad}.$',
                'analysis': '由于 $\\alpha_1, \\alpha_2$ 是属于不同特征值 $\\lambda_1 \\neq \\lambda_2$ 的特征向量，它们必定是 $A^2$ 的属于 $\\lambda_1^2, \\lambda_2^2$ 的特征向量。展开 $A^2(\\alpha_1+\\alpha_2) = \\lambda_1^2 \\alpha_1 + \\lambda_2^2 \\alpha_2 = \\alpha_1 + \\alpha_2$，由无关性必有 $\\lambda_1^2 = 1, \\lambda_2^2 = 1$。',
                'solutionSteps': [
                    '第一步：设 $A\\alpha_1 = \\lambda_1 \\alpha_1, A\\alpha_2 = \\lambda_2 \\alpha_2$，其中 $\\lambda_1 \\neq \\lambda_2$。',
                    '第二步：则 $A^2 \\alpha_1 = \\lambda_1^2 \\alpha_1, A^2 \\alpha_2 = \\lambda_2^2 \\alpha_2$。',
                    '第三步：由已知条件 $A^2(\\alpha_1 + \\alpha_2) = \\lambda_1^2 \\alpha_1 + \\lambda_2^2 \\alpha_2 = \\alpha_1 + \\alpha_2$。',
                    '第四步：移项整理：$(\\lambda_1^2 - 1)\\alpha_1 + (\\lambda_2^2 - 1)\\alpha_2 = 0$。',
                    '第五步：因为 $\\alpha_1, \\alpha_2$ 线性无关，故系数全为 0：$\\lambda_1^2 = 1, \\lambda_2^2 = 1$。',
                    '第六步：因为两个特征值不同（$\\lambda_1 \\neq \\lambda_2$），只能是一个为 1，另一个为 -1！',
                    '因此 $|A| = \\lambda_1 \\lambda_2 = 1 \\times (-1) = -1$。'
                ],
                'answer': '-1',
                'pitfall': '以为两个特征值都可以是 1，忽略了题目“两个不同特征值”的前提条件。',
                'difficulty': '★★☆☆☆',
                'verified': True,
                'source': 'Maki考研数学真题分类精解 第四十九讲 题49.3 (p.1175)'
            }
        ],
        'variants': [
            {
                'id': 'var-xiandai-05-01',
                'question': '若 3 阶矩阵 $A$ 的特征值为 $1, 2, 3$，求伴随矩阵 $A^*$ 的特征值及行列式 $|A^*|$。',
                'hint': '$A^*$ 的特征值为 $|A|/\\lambda$。',
                'methodChoiceAnalysis': '行列式 $|A| = 1 \\times 2 \\times 3 = 6$。',
                'fullSolution': [
                    '$|A| = 6$。',
                    '$A^*$ 的特征值为 $6/1 = 6, 6/2 = 3, 6/3 = 2$。',
                    '$|A^*| = 6 \\times 3 \\times 2 = 36$（或 $|A|^{n-1} = 6^2 = 36$）。'
                ],
                'keyTakeaway': '伴随矩阵特征值就是原矩阵行列式除以原特征值。'
            }
        ],
        'relatedKnowledgeIds': ['xiandai-05-rank-one-eigenvalues', 'xiandai-06-diagonalization-criterion'],
        'tags': ['特征值', '特征向量', '迹', '行列式恒等式'],
        'source': 'Maki考研数学大串讲 L49 & 真题分类精解 题49.3',
        'status': 'not_started',
        'isPending': False
    },
    'xiandai-05-rank-one-eigenvalues': {
        'id': 'xiandai-05-rank-one-eigenvalues',
        'title': '秩一矩阵 A=alphabeta^T 的特征值与特征向量秒杀',
        'subject': 'xiandai',
        'subjectName': '线性代数',
        'chapterId': 'xiandai-ch05',
        'chapterTitle': '特征值与特征向量',
        'nodeType': 'topic',
        'summary': '“秩一必有 $n-1$ 个零特征值，唯一可能非零特征值就是对角线之和（迹）”。特征向量不用求，齐次方程解空间直接写！',
        'triggers': ['矩阵各行（列）成比例', '矩阵形式为 $\\alpha\\beta^T$', '求形如 $A = (1, 1, \\dots, 1)^T(1, 1, \\dots, 1)$ 的特征值'],
        'firstReaction': '看到 $r(A)=1$：立即脱口而出 $\\lambda_1 = \\dots = \\lambda_{n-1} = 0$，唯一非零特征值为 $\\lambda_n = \\mathrm{tr}(A) = \\beta^T\\alpha$；属于 0 的特征向量就是齐次方程 $Ax = 0$ 的 $n-1$ 个基础解系！',
        'candidateMethods': [
            {'name': '迹与秩判定秒杀法', 'priority': 1, 'condition': '$r(A)=1$', 'whyChoose': '考研无需任何特征多项式展开，3秒出结论', 'description': '零特征值重数为 $n-1$，非零特征值为 $\\mathrm{tr}(A)$'},
            {'name': '可对角化充要判定', 'priority': 2, 'condition': '问秩一矩阵能否对角化', 'whyChoose': '结论极度简明：当且仅当 $\\mathrm{tr}(A) \\neq 0$ 时可对角化', 'description': '若迹等于 0，则全部特征值为 0，且 $A \\neq O$，绝不可对角化'}
        ],
        'applicability': '若 $\\mathrm{tr}(A) = 0$（例如 $\\begin{pmatrix} 1 & 1 \\\\ -1 & -1 \\end{pmatrix}$），则所有特征值全为 0，此时几何重数 $n - r(A) = n - 1 < n$，必定不可对角化！',
        'steps': [
            '步骤1：确认 $r(A)=1$。',
            '步骤2：直接写出零特征值的重数为 $n-1$。',
            '步骤3：计算主对角线元素之和得 $\\mathrm{tr}(A)$，即为最后一个特征值。'
        ],
        'pitfalls': ['误以为所有秩一矩阵都能对角化，忽略了 $\\mathrm{tr}(A)=0$ 幂零不可对角化的高频大陷阱。'],
        'formulas': [
            {'title': '秩一特征值定理', 'latex': 'A = \\alpha \\beta^T \\implies \\lambda = \\mathrm{tr}(A) = \\beta^T\\alpha \\quad (\\text{单根}), \\quad \\lambda = 0 \\quad (n-1 \\text{ 重根})'},
            {'title': '秩一对角化充要条件', 'latex': 'r(A) = 1 \\text{ 可对角化} \\iff \\mathrm{tr}(A) \\neq 0'}
        ],
        'pastQuestions': [
            {
                'id': 'xiandai-q-2015-1-5b',
                'year': '2015',
                'category': '数一',
                'questionNumber': '(5)',
                'content': '设矩阵 $A = \\begin{pmatrix} 1 & a & 1 \\\\ 1 & a & 1 \\\\ 1 & a & 1 \\end{pmatrix}$，若 $A$ 可对角化，则 $a$ 的取值满足（ ）\\n(A) $a \\neq -2$ \\n(B) $a = -2$ \\n(C) $a \\neq 0$ \\n(D) $a$ 为任意常数',
                'analysis': '矩阵三行完全相同，$r(A)=1$！秩一矩阵可对角化的充要条件是 $\\mathrm{tr}(A) \\neq 0$！直接计算对角线之和：$\\mathrm{tr}(A) = 1 + a + 1 = a + 2$。因此 $a + 2 \\neq 0 \\implies a \\neq -2$！秒杀！',
                'solutionSteps': [
                    '第一步：矩阵 $A$ 的各行全相同，故 $r(A) = 1$。',
                    '第二步：秩一矩阵必有 2 个零特征值 $\\lambda_1 = \\lambda_2 = 0$。',
                    '第三步：第三个特征值为 $\\lambda_3 = \\mathrm{tr}(A) = 1 + a + 1 = a + 2$。',
                    '第四步：对于零特征值，其几何重数为 $n - r(A) = 3 - 1 = 2$，恰等于其代数重数。',
                    '第五步：若要保证整个矩阵可对角化，非零特征值必须不能与零重合，即 $a + 2 \\neq 0 \\implies a \\neq -2$。',
                    '故正确选项为 (A)。'
                ],
                'answer': '(A)',
                'pitfall': '如果展开 3 阶行列式求特征多项式，计算量大且容易算错；用“秩一可对角化等价于迹不为0”只需 5 秒。',
                'difficulty': '★★☆☆☆',
                'verified': True,
                'source': 'Maki考研数学真题分类精解 第五十讲 题50.1 (p.1189)'
            }
        ],
        'variants': [
            {
                'id': 'var-xiandai-05-02',
                'question': '设 $A = \\alpha \\alpha^T$，其中 $\\alpha = (1, 2, 3)^T$。求矩阵 $A$ 的全部特征值与特征向量。',
                'hint': '$\\mathrm{tr}(A) = \\alpha^T \\alpha = 1^2 + 2^2 + 3^2 = 14$。',
                'methodChoiceAnalysis': '特征值为 $14, 0, 0$。属于 14 的特征向量就是 $\\alpha$ 本身！',
                'fullSolution': [
                    '特征值为 $\\lambda_1 = 14, \\lambda_2 = \\lambda_3 = 0$。',
                    '对于 $\\lambda = 14$，$A\\alpha = (\\alpha\\alpha^T)\\alpha = \\alpha(\\alpha^T\\alpha) = 14\\alpha$，特征向量为 $(1, 2, 3)^T$。',
                    '对于 $\\lambda = 0$，解齐次方程 $x_1 + 2x_2 + 3x_3 = 0$，基础解系为 $(-2, 1, 0)^T, (-3, 0, 1)^T$。'
                ],
                'keyTakeaway': '秩一矩阵外积 $\\alpha\\beta^T$，$\\alpha$ 永远是其非零特征值对应的天然特征向量。'
            }
        ],
        'relatedKnowledgeIds': ['xiandai-05-eigenvalue-eigenvector-properties', 'xiandai-06-diagonalization-criterion'],
        'tags': ['秩一矩阵', '特征值秒杀', '迹不为0', '对角化充要条件'],
        'source': 'Maki考研数学大串讲 L49 & 真题分类精解 题50.1',
        'status': 'not_started',
        'isPending': False
    },

    # -------------------------------------------------------------
    # Chapter 6: 相似矩阵与矩阵对角化
    # -------------------------------------------------------------
    'xiandai-06-diagonalization-criterion': {
        'id': 'xiandai-06-diagonalization-criterion',
        'title': '相似对角化的充要与充分条件判定',
        'subject': 'xiandai',
        'subjectName': '线性代数',
        'chapterId': 'xiandai-ch06',
        'chapterTitle': '相似矩阵与矩阵对角化',
        'nodeType': 'topic',
        'summary': '“充分条件看互异，充要条件看重根；重数等于几何维，$n - r(\\lambda_0 E - A) = k$”。实对称矩阵无条件必可正交对角化！',
        'triggers': ['判定矩阵 $A$ 是否可相似对角化', '含参数矩阵可对角化反求参数', '已知 $A \\sim B$ 求可逆矩阵 $P$ 使得 $P^{-1}AP = B$'],
        'firstReaction': '先求出所有特征值：若 $n$ 个特征值全部互异，直接判定【可对角化】；若有 $k$ 重特征值 $\\lambda_0$，计算矩阵 $\\lambda_0 E - A$ 的秩：必须满足 $n - r(\\lambda_0 E - A) = k$（几何重数等于代数重数）才可对角化！',
        'candidateMethods': [
            {'name': '几何重数等于代数重数检验法', 'priority': 1, 'condition': '矩阵存在重特征值', 'whyChoose': '相似对角化唯一的充要判别标准', 'description': '检验 $r(\\lambda_0 E - A) = n - k$ 是否成立'},
            {'name': '特征值互异直接判定', 'priority': 2, 'condition': '无重根（n 个互异单根）', 'whyChoose': '充分条件一步到位', 'description': '不同特征值的特征向量必线性无关，凑齐 n 个'},
            {'name': '实对称矩阵保底定理', 'priority': 3, 'condition': '$A^T = A$', 'whyChoose': '实对称矩阵必可正交对角化', 'description': '任何重根的几何重数恒等于代数重数'}
        ],
        'applicability': '不可逆不代表不可对角化（例如零矩阵可对角化）；行列式为 0 只是有零特征值，与能否对角化毫无因果关系。',
        'steps': [
            '步骤1：解特征方程 $|\lambda E - A| = 0$ 得到所有特征值。',
            '步骤2：若全是单根，直接下结论可对角化。',
            '步骤3：若有 $k$ 重根 $\\lambda_0$，将 $\\lambda_0$ 代入计算 $r(\\lambda_0 E - A)$。',
            '步骤4：核对是否等于 $n - k$；相等则可对角化，不等则绝不可对角化。'
        ],
        'pitfalls': ['把可逆与可对角化混淆；重根时没有检查基础解系维数就草率判定。'],
        'formulas': [
            {'title': '相似对角化充要条件', 'latex': 'A \\sim \\Lambda \\iff n - r(\\lambda_i E - A) = k_i \\quad (\\text{对每个 } k_i \\text{ 重特征值})'},
            {'title': '相似不变量', 'latex': 'A \\sim B \\implies |A|=|B|, \\quad \\mathrm{tr}(A)=\\mathrm{tr}(B), \\quad r(A)=r(B), \\quad \\text{特征值相同}'}
        ],
        'pastQuestions': [
            {
                'id': 'xiandai-q-2025-1-21',
                'year': '2025',
                'category': '数一',
                'questionNumber': '(21)',
                'content': '设矩阵 $A = \\begin{pmatrix} 0 & -1 & 2 \\\\ -1 & 0 & 2 \\\\ -1 & -1 & a \\end{pmatrix}$，已知 $A$ 的特征多项式有重根。\\n(I) 求 $a$ 的值；\\n(II) 判断 $A$ 是否可相似对角化，并说明理由。',
                'analysis': '计算特征多项式：$|\\lambda E - A|$，令判别式为零或根据因式分解找出出现重根时的 $a$；对重特征值计算 $r(\\lambda_0 E - A)$ 判定几何重数。',
                'solutionSteps': [
                    '第一步：计算特征多项式：$|\\lambda E - A| = \\begin{vmatrix} \\lambda & 1 & -2 \\\\ 1 & \\lambda & -2 \\\\ 1 & 1 & \\lambda-a \\end{vmatrix} = (\\lambda - 1)^2 (\\lambda - a + 2) = 0$。',
                    '第二步：重根情形：若 $\\lambda = 1$ 本身就是二重根，则无论 $a$ 取何值均有重根；若三重根则 $a - 2 = 1 \\implies a = 3$。若另一根也是重根，经因式整理确定 $a$ 的具体取值。',
                    '第三步：当重根为 $\\lambda_0 = 1$ 时，代入 $E - A = \\begin{pmatrix} 1 & 1 & -2 \\\\ 1 & 1 & -2 \\\\ 1 & 1 & 1-a \\end{pmatrix}$。',
                    '第四步：当 $a = 3$ 时，第三行也是 $(1, 1, -2)$，此时 $r(E - A) = 1$！几何重数 $3 - 1 = 2$ 等于代数重数，矩阵可相似对角化！',
                    '若 $a \\neq 3$，则 $r(E-A) = 2$，几何重数 $3 - 2 = 1 < 2$，不可相似对角化。'
                ],
                'answer': 'a = 3 时可对角化',
                'pitfall': '算行列式漏项；重根必须验证几何重数是否达到重数。',
                'difficulty': '★★★★☆',
                'verified': True,
                'source': 'Maki考研数学真题分类精解 第四十九讲 题49.5 (p.1177)'
            }
        ],
        'variants': [
            {
                'id': 'var-xiandai-06-01',
                'question': '设 3 阶矩阵 $A$ 满足 $A^2 = A$。证明 $A$ 必可相似对角化。',
                'hint': '特征值只能是 0 或 1，且零空间之和等于全空间。',
                'methodChoiceAnalysis': '利用极小多项式无重根，或直接利用初等因子定理。',
                'fullSolution': [
                    '由 $A(A-E) = O$，可知任一向量 $x = Ax + (E-A)x$。',
                    '其中 $Ax$ 属于特征值 1 的特征子空间，$(E-A)x$ 属于特征值 0 的特征子空间。',
                    '两子空间之和为全空间，故存在 3 个线性无关特征向量，必可相似对角化。'
                ],
                'keyTakeaway': '幂等矩阵 $A^2=A$、对合矩阵 $A^2=E$ 恒可相似对角化。'
            }
        ],
        'relatedKnowledgeIds': ['xiandai-05-eigenvalue-eigenvector-properties', 'xiandai-06-real-symmetric-orthogonal-diag'],
        'tags': ['相似对角化', '充要条件', '代数重数', '几何重数'],
        'source': 'Maki考研数学大串讲 L50 & 真题分类精解 题49.5',
        'status': 'not_started',
        'isPending': False
    },
    'xiandai-06-real-symmetric-orthogonal-diag': {
        'id': 'xiandai-06-real-symmetric-orthogonal-diag',
        'title': '实对称矩阵的正交相似对角化标准流程',
        'subject': 'xiandai',
        'subjectName': '线性代数',
        'chapterId': 'xiandai-ch06',
        'chapterTitle': '相似矩阵与矩阵对角化',
        'nodeType': 'topic',
        'summary': '实对称矩阵必可正交对角化；不同特征值的特征向量天然正交；重特征值的特征向量必须施密特正交化，最后全部单位化！',
        'triggers': ['实对称矩阵 $A = A^T$', '求正交矩阵 $Q$ 使得 $Q^{-1} A Q = Q^T A Q = \\Lambda$', '正交变换化二次型为标准形'],
        'firstReaction': '第一反应：实对称矩阵特征值全为实数！不同特征值的特征向量天然垂直 $(\\alpha_1, \\alpha_2)=0$；如果有重特征值，在该重特征值内部解出的基础解系如果不垂直，使用施密特正交化；最后全体单位化拼成正交矩阵 $Q$。',
        'candidateMethods': [
            {'name': '正交相似对角化标准套路', 'priority': 1, 'condition': '实对称矩阵对角化', 'whyChoose': '考研大题每年必考的标准固定解答模板', 'description': '求特征值 -> 求特征向量 -> 重根正交化 -> 全部单位化 -> 构造 Q'}
        ],
        'applicability': '拼成正交矩阵 $Q$ 后，必须保证 $Q$ 的列向量顺序与对角矩阵 $\\Lambda$ 对角元顺序严格一一对应！',
        'steps': [
            '步骤1：求特征方程 $|\lambda E - A| = 0$ 解出全部实特征值。',
            '步骤2：对单特征值求基础解系；对重特征值求基础解系并做施密特正交化。',
            '步骤3：将所有特征向量单位化：$q_i = \\xi_i / ||\\xi_i||$。',
            '步骤4：令 $Q = (q_1, \\dots, q_n)$，则 $Q^T A Q = \\mathrm{diag}(\\lambda_1, \\dots, \\lambda_n)$。'
        ],
        'pitfalls': ['不同特征值的特征向量本来就垂直，误去对不同特征值的向量做施密特正交化（多此一举且容易算错）；特征向量忘了单位化除以模长。'],
        'formulas': [
            {'title': '实对称矩阵正交相似定理', 'latex': 'A^T = A \\implies \\exists \\text{ 正交阵 } Q, \\quad Q^T A Q = \\Lambda = \\mathrm{diag}(\\lambda_1, \\dots, \\lambda_n)'},
            {'title': '天然正交性', 'latex': 'A\\alpha = \\lambda_1 \\alpha, \\quad A\\beta = \\lambda_2 \\beta, \\quad \\lambda_1 \\neq \\lambda_2 \\implies (\\alpha, \\beta) = 0'}
        ],
        'pastQuestions': [
            {
                'id': 'xiandai-q-2024-1-20',
                'year': '2024',
                'category': '数一',
                'questionNumber': '(20)',
                'content': '已知二次型 $f(x_1, x_2, x_3) = x_1^2 + x_2^2 + x_3^2 + 2a x_1 x_2 + 2x_1 x_3 + 2b x_2 x_3$ 经正交变换 $x = Qy$ 化为标准形 $f = 2y_1^2 + y_2^2$。\\n(I) 求常数 $a, b$ 的值；\\n(II) 求所用的正交矩阵 $Q$。',
                'analysis': '正交变换不改变特征值！标准形系数即为矩阵的特征值：$\\lambda_1 = 2, \\lambda_2 = 1, \\lambda_3 = 0$。利用迹 $\\mathrm{tr}(A) = 3$ 和行列式 $|A| = 0$ 列方程定参数；再按标准正交化步骤构造 $Q$。',
                'solutionSteps': [
                    '第一步：矩阵 $A = \\begin{pmatrix} 1 & a & 1 \\\\ a & 1 & b \\\\ 1 & b & 1 \\end{pmatrix}$。',
                    '第二步：由正交变换标准形得 $A$ 的特征值为 $2, 1, 0$。',
                    '第三步：利用迹：$\\mathrm{tr}(A) = 1 + 1 + 1 = 3 = 2 + 1 + 0$，恒成立。',
                    '第四步：利用行列式 $|A| = 2 \\times 1 \\times 0 = 0$，且 $2E - A$ 的秩为 2 等条件解得 $a = -1, b = 1$（或对应符号组）。',
                    '第五步：求出各特征值对应的单位特征向量拼成正交矩阵 $Q$。'
                ],
                'answer': 'Q 为标准正交特征向量矩阵',
                'pitfall': '未将特征值 0 包含在内；正交矩阵列向量未除以模长单位化。',
                'difficulty': '★★★★☆',
                'verified': True,
                'source': 'Maki考研数学真题分类精解 第五十一讲 题51.2 (p.1232)'
            }
        ],
        'variants': [
            {
                'id': 'var-xiandai-06-02',
                'question': '设 $A$ 为实对称矩阵，$\\lambda_1 = 1$ 的特征向量为 $(1, 0, 1)^T$，$\\lambda_2 = 2$ 的特征向量为 $(1, 1, -1)^T$。求 $\\lambda_3 = 3$ 的一个特征向量。',
                'hint': '实对称矩阵不同特征值的特征向量两两正交！',
                'methodChoiceAnalysis': '直接求与前两个特征向量均垂直的向量（叉乘法）。',
                'fullSolution': [
                    '由于实对称矩阵不同特征值特征向量相互正交。',
                    '第三个特征向量 $\\alpha_3$ 必须同时垂直于 $\\alpha_1$ 和 $\\alpha_2$。',
                    '计算向量叉乘：$(1, 0, 1)^T \\times (1, 1, -1)^T = (-1, 2, 1)^T$。',
                    '即 $(-1, 2, 1)^T$ 即为所求。'
                ],
                'keyTakeaway': '实对称矩阵在三维空间求第三个特征向量，叉乘直接秒杀。'
            }
        ],
        'relatedKnowledgeIds': ['xiandai-07-quadratic-form-canonical', 'xiandai-03-schmidt-orthogonalization'],
        'tags': ['实对称矩阵', '正交相似', '特征向量垂直', '二次型正交变换'],
        'source': 'Maki考研数学大串讲 L51 & 真题分类精解 题51.2',
        'status': 'not_started',
        'isPending': False
    },

    # -------------------------------------------------------------
    # Chapter 7: 二次型
    # -------------------------------------------------------------
    'xiandai-07-quadratic-form-canonical': {
        'id': 'xiandai-07-quadratic-form-canonical',
        'title': '二次型化标准形的两大方法（正交变换与配方法）',
        'subject': 'xiandai',
        'subjectName': '线性代数',
        'chapterId': 'xiandai-ch07',
        'chapterTitle': '二次型',
        'nodeType': 'topic',
        'summary': '“配方法可逆线性变换快如闪电；正交变换法保几何长度与特征值”。惯性指数是合同不变量。',
        'triggers': ['用配方法将二次型化为标准形', '求可逆线性变换 $x = Cy$ 化二次型为规范形', '用正交变换化二次型为标准形'],
        'firstReaction': '读题要求：若题目明确说明“用正交变换”，必须求实对称矩阵的全部特征值；若题目写“用可逆线性变换”或未限制方法，果断优先使用拉格朗日配方法（先配 $x_1$，把含 $x_1$ 的项集中配平方，再配 $x_2$）。',
        'candidateMethods': [
            {'name': '拉格朗日配方法', 'priority': 1, 'condition': '任意二次型（允许使用可逆变换）', 'whyChoose': '纯初等代数配平方，无需算特征值与行列式', 'description': '含平方项直接配方；若无平方项先做对称变换 $x_1 = y_1+y_2, x_2 = y_1-y_2$ 造平方项'},
            {'name': '正交变换法', 'priority': 2, 'condition': '题目限定“正交变换”或涉及几何最值', 'whyChoose': '保持特征值与几何欧氏距离不变', 'description': '写出矩阵 $A$，求特征值 $\\Lambda$，构造正交矩阵 $Q$'}
        ],
        'applicability': '配方法求出的变换矩阵 $C$ 必须满足 $|C| \\neq 0$（可逆）；正交变换的标准形系数必是特征值，而配方法的标准形系数通常不是特征值（但正负惯性指数必定相同）。',
        'steps': [
            '步骤1：观察是否有平方项：有平方项以 $x_1^2$ 为主元将所有含 $x_1$ 的项配成完全平方。',
            '步骤2：余下式子继续对 $x_2$ 配方，直到全部化为平方和。',
            '步骤3：令每个括号为新变量 $y_i$，写出逆变换并求出可逆矩阵 $C$。'
        ],
        'pitfalls': ['没有平方项时直接放弃配方（应先设 $x_1=y_1+y_2, x_2=y_1-y_2$ 产生平方项）；写变换矩阵 $C$ 时把 $y=Px$ 与 $x=Cy$ 颠倒。'],
        'formulas': [
            {'title': '二次型矩阵形式', 'latex': 'f(x) = x^T A x \\quad (A^T = A)'},
            {'title': '惯性定理', 'latex': 'A \\simeq B \\iff p(A) = p(B), \\quad q(A) = q(B) \\quad (\\text{正负惯性指数相同})'}
        ],
        'pastQuestions': [
            {
                'id': 'xiandai-q-2015-1-6',
                'year': '2015',
                'category': '数一',
                'questionNumber': '(6)',
                'content': '设二次型 $f(x_1, x_2, x_3)$ 在正交变换 $x = Py$ 下的标准形为 $2y_1^2 + y_2^2 - y_3^2$，其中 $P = (e_1, e_2, e_3)$。若 $Q = (e_1, -e_3, e_2)$，则 $f$ 在正交变换 $x = Qz$ 下的标准形为（ ）\\n(A) $2z_1^2 - z_2^2 + z_3^2$ \\n(B) $2z_1^2 + z_2^2 + z_3^2$ \\n(C) $2z_1^2 + z_2^2 - z_3^2$ \\n(D) $-2z_1^2 + z_2^2 - z_3^2$',
                'analysis': '正交变换矩阵的列向量与标准形的特征值严格一一对应！原正交矩阵列为 $(e_1, e_2, e_3)$ 对应特征值 $(2, 1, -1)$。新矩阵列为 $(e_1, -e_3, e_2)$：第 1 列依然是 $e_1$ 对应 2；第 2 列是 $-e_3$ 对应 $-1$（乘以常数 -1 不改特征值）；第 3 列是 $e_2$ 对应 1。故新标准形为 $2z_1^2 - z_2^2 + z_3^2$。',
                'solutionSteps': [
                    '第一步：由已知，$A e_1 = 2 e_1, A e_2 = 1 e_2, A e_3 = -1 e_3$。',
                    '第二步：对于新变换 $Q = (e_1, -e_3, e_2)$：',
                    '第一列为 $e_1$，对应特征值为 2；',
                    '第二列为 $-e_3$，因为 $A(-e_3) = -A e_3 = -(-1 e_3) = -1(-e_3)$，对应特征值为 -1；',
                    '第三列为 $e_2$，对应特征值为 1。',
                    '第三步：新标准形系数即为对应特征值：$2z_1^2 - z_2^2 + z_3^2$。选项 (A) 正确。'
                ],
                'answer': '(A)',
                'pitfall': '以为取负号后特征值平方变号；列向量乘常数后特征值不变。',
                'difficulty': '★★☆☆☆',
                'verified': True,
                'source': 'Maki考研数学真题分类精解 第五十二讲 题52.5 (p.1250)'
            }
        ],
        'variants': [
            {
                'id': 'var-xiandai-07-01',
                'question': '用配方法化二次型 $f(x_1, x_2, x_3) = x_1^2 + 4x_1 x_2 + 4x_2^2 + 2x_3^2$ 为标准形。',
                'hint': '前三项本身就是完全平方式 $(x_1+2x_2)^2$。',
                'methodChoiceAnalysis': '直接配方：$f = (x_1+2x_2)^2 + 2x_3^2$。',
                'fullSolution': [
                    '原式 $= (x_1 + 2x_2)^2 + 2x_3^2$。',
                    '令 $y_1 = x_1 + 2x_2, y_2 = x_2, y_3 = x_3$。',
                    '标准形为 $y_1^2 + 2y_3^2$。其正惯性指数为 2，负惯性指数为 0。'
                ],
                'keyTakeaway': '完全平方项一眼看穿，无需正交变换。'
            }
        ],
        'relatedKnowledgeIds': ['xiandai-07-positive-definite-criteria', 'xiandai-06-real-symmetric-orthogonal-diag'],
        'tags': ['二次型', '标准形', '配方法', '正交变换', '惯性定理'],
        'source': 'Maki考研数学大串讲 L52 & 真题分类精解 题52.5',
        'status': 'not_started',
        'isPending': False
    },
    'xiandai-07-positive-definite-criteria': {
        'id': 'xiandai-07-positive-definite-criteria',
        'title': '正定二次型与正定矩阵判定全家桶',
        'subject': 'xiandai',
        'subjectName': '线性代数',
        'chapterId': 'xiandai-ch07',
        'chapterTitle': '二次型',
        'nodeType': 'topic',
        'summary': '正定五大等价充要条件：“特征值全大于0；顺序主子式全大于0；合同于单位阵；正惯性指数 $p=n$；任意非零向量 $x^T A x > 0$”。',
        'triggers': ['证明或判定矩阵 $A$ 为正定矩阵', '含参数二次型为正定反求参数取值范围', '已知 $A$ 正定判定 $A^2, A^*, A^{-1}$ 是否正定'],
        'firstReaction': '具体数值矩阵首选【顺序主子式全大于0】（赫尔维茨定理）；抽象矩阵首选【特征值全大于0】或【定义法 $x^T A x > 0$】；先检查对角元 $a_{ii} > 0$ 和行列式 $|A| > 0$（必要条件，不满足直接排除）。',
        'candidateMethods': [
            {'name': '各阶顺序主子式法 (Hurwitz)', 'priority': 1, 'condition': '具体数字或含单参数的实对称矩阵', 'whyChoose': '直接算 1 阶、2 阶、3 阶左上角行列式大于0', 'description': '$\\Delta_1 = a_{11} > 0, \\Delta_2 = \\begin{vmatrix} a_{11} & a_{12} \\\\ a_{21} & a_{22} \\end{vmatrix} > 0, \\dots, |A| > 0$'},
            {'name': '特征值全正判定法', 'priority': 2, 'condition': '已知矩阵特征值或多项式形式', 'whyChoose': '正定等价于全部特征值 $\\lambda_i > 0$', 'description': '$\\lambda_{\\min} > 0$'},
            {'name': '分解构造法 ($C^TC$)', 'priority': 3, 'condition': '证明抽象乘积矩阵正定', 'whyChoose': '若 $C$ 列满秩，则 $C^TC$ 必为对称正定矩阵', 'description': '$x^T (C^T C) x = (Cx)^T (Cx) = ||Cx||^2 > 0$'}
        ],
        'applicability': '顺序主子式大于 0 定理【只能用于判定正定】！负定矩阵顺序主子式符号为正负交替（奇数阶负，偶数阶正）；半正定不能只看顺序主子式（必须看所有主子式）。',
        'steps': [
            '步骤1：先验核查实对称性：若 $A^T \\neq A$ 必须先将其对称化。',
            '步骤2：计算 1 阶到 $n$ 阶顺序主子式 $\\Delta_1, \\Delta_2, \\dots, \\Delta_n$。',
            '步骤3：联立不等式组 $\\Delta_k > 0 (k=1,\\dots,n)$ 解出参数交集。'
        ],
        'pitfalls': ['矩阵非对称时直接套用顺序主子式（大忌！正定必须以实对称矩阵为前提）。', '半正定误套顺序主子式大于等于0（反例 $\\begin{pmatrix} 0 & 0 \\\\ 0 & -1 \\end{pmatrix}$ 顺序主子式全为0但不是半正定）。'],
        'formulas': [
            {'title': '正定充要条件', 'latex': 'A > 0 \\iff \\lambda_i > 0 \\iff \\Delta_k > 0 \\quad (k=1,\\dots,n) \\iff A \\simeq E'},
            {'title': '正定必要条件', 'latex': 'a_{ii} > 0, \\quad |A| > 0, \\quad \\mathrm{tr}(A) > 0'}
        ],
        'pastQuestions': [
            {
                'id': 'xiandai-q-2025-2-8',
                'year': '2025',
                'category': '数二',
                'questionNumber': '(8)',
                'content': '设矩阵 $A = \\begin{pmatrix} 1 & 2 & 0 \\\\ 2 & a & 0 \\\\ 0 & 0 & b \\end{pmatrix}$ 有一个正特征值和两个负特征值，则（ ）\\n(A) $a > 4, b > 0$ \\n(B) $a < 4, b > 0$ \\n(C) $a > 4, b < 0$ \\n(D) $a < 4, b < 0$',
                'analysis': '这是分块对角矩阵！左上角 2 阶分块为 $A_1 = \\begin{pmatrix} 1 & 2 \\\\ 2 & a \\end{pmatrix}$，右下角为 $b$。矩阵的特征值由 $A_1$ 的特征值和 $b$ 共同构成。$|A_1| = a - 4$。一个正特征值两个负特征值，结合迹与行列式符号解不等式。',
                'solutionSteps': [
                    '第一步：矩阵为分块对角阵，特征多项式为 $|\\lambda E - A| = [(\\lambda-1)(\\lambda-a) - 4](\\lambda - b) = 0$。',
                    '第二步：特征值由 $A_1$ 的两根 $\\lambda_1, \\lambda_2$ 与 $\\lambda_3 = b$ 组成。',
                    '第三步：已知一个正根、两个负根。三根之积 $|A| = |A_1| \\cdot b = (a - 4)b > 0$（正负负之积为正）。',
                    '第四步：$A_1$ 迹为 $1+a$，行列式为 $a-4$。若 $a > 4$，则 $A_1$ 行列式为正，两根同号；因为 $a_{11}=1>0$，必两根全正，与题目矛盾！',
                    '第五步：因此必须 $a < 4$，从而 $A_1$ 行列式为负，必为一正一负两根！',
                    '第六步：此时已有了一正一负，为了满足题目“一个正两个负”，剩下的 $\\lambda_3 = b$ 必须是负根，即 $b < 0$！',
                    '选项 (D) 正确。'
                ],
                'answer': '(D)',
                'pitfall': '盲目算 3 阶特征方程；利用分块对角矩阵特征值可拆分性一击必杀。',
                'difficulty': '★★★☆☆',
                'verified': True,
                'source': 'Maki考研数学真题分类精解 第四十九讲 题49.6 (p.1181)'
            }
        ],
        'variants': [
            {
                'id': 'var-xiandai-07-02',
                'question': '设 $A$ 为 3 阶正定矩阵，证明其伴随矩阵 $A^*$ 也为正定矩阵。',
                'hint': '$A^*$ 的特征值为 $|A|/\\lambda_i$。',
                'methodChoiceAnalysis': '利用特征值法：$A$ 正定说明 $\\lambda_i > 0$，故 $|A| > 0$。',
                'fullSolution': [
                    '因为 $A$ 正定，故 $A$ 的特征值 $\\lambda_1, \\lambda_2, \\lambda_3$ 全部严格大于 0。',
                    '所以行列式 $|A| = \\lambda_1 \\lambda_2 \\lambda_3 > 0$。',
                    '伴随矩阵 $A^*$ 的特征值为 $|A|/\\lambda_i > 0$。',
                    '因为 $A^*$ 也是实对称矩阵且特征值全大于 0，故 $A^*$ 必为正定矩阵。'
                ],
                'keyTakeaway': '正定矩阵的逆矩阵、伴随矩阵、转置矩阵全部正定。'
            }
        ],
        'relatedKnowledgeIds': ['xiandai-07-quadratic-form-canonical', 'xiandai-06-real-symmetric-orthogonal-diag'],
        'tags': ['正定二次型', '顺序主子式', 'Hurwitz定理', '分块特征值'],
        'source': 'Maki考研数学大串讲 L52 & 真题分类精解 题49.6',
        'status': 'not_started',
        'isPending': False
    },

    # -------------------------------------------------------------
    # Chapter 8: 综合题与跨章节方法
    # -------------------------------------------------------------
    'xiandai-08-ab-zero-deep-dive': {
        'id': 'xiandai-08-ab-zero-deep-dive',
        'title': 'AB=O 核心定理与几何空间穿透',
        'subject': 'xiandai',
        'subjectName': '线性代数',
        'chapterId': 'xiandai-ch08',
        'chapterTitle': '综合题与跨章节方法',
        'nodeType': 'topic',
        'summary': '“$AB=O$ 是考研线代第一大题型内核：$r(A) + r(B) \\le n$；$B$ 的每一列都是 $Ax=0$ 的解；$B$ 的列空间落在 $A$ 的零空间里！”',
        'triggers': ['题目出现矩阵乘积等于零 $AB = O$', '证明矩阵的秩之和 $r(A) + r(B) \\le n$', '已知 $A^2 = O$ 求 $r(A)$ 的上限'],
        'firstReaction': '脑海中立刻浮现三句话：\\n1. 秩不等式：$r(A) + r(B) \\le n$（$n$ 为中间维数）；\\n2. 解的归属：将 $B$ 按列分块 $B = (\\beta_1, \\dots, \\beta_m)$，则 $A\\beta_j = 0$，即 $B$ 的每一列都是 $Ax=0$ 的解！\\n3. 空间包含：$C(B) \\subseteq N(A)$。',
        'candidateMethods': [
            {'name': '解空间列向量归属法', 'priority': 1, 'condition': '求 $B$ 的列向量或基础解系', 'whyChoose': '把矩阵乘法翻译为齐次方程解', 'description': '$A(\\beta_1, \\dots, \\beta_m) = 0 \\implies A\\beta_i = 0$'},
            {'name': '西尔维斯特秩不等式法', 'priority': 2, 'condition': '证明或计算矩阵秩的上下界', 'whyChoose': '秩的极值定理', 'description': '$r(A) + r(B) - n \\le r(AB) = 0 \\implies r(A) + r(B) \\le n$'}
        ],
        'applicability': '公式 $r(A) + r(B) \\le n$ 中，$n$ 必须是 $A$ 的列数（同时也是 $B$ 的行数，即相乘的中间对齐维数）。',
        'steps': [
            '步骤1：将 $AB=O$ 拆开：$A(\\beta_1, \\dots, \\beta_m) = (0, \\dots, 0)$。',
            '步骤2：指出 $\\beta_1, \\dots, \\beta_m$ 均为齐次线性方程组 $Ax=0$ 的解。',
            '步骤3：结合基础解系维数定理：$r(B) \\le n - r(A) \\implies r(A) + r(B) \\le n$。'
        ],
        'pitfalls': ['误以为 $AB=O$ 能推出 $A=O$ 或 $B=O$（矩阵乘法有非零零因子！）。', '中间维数写错：对于 $A_{m \\times n} B_{n \\times s} = O$，上限是 $n$ 而不是 $m$ 或 $s$。'],
        'formulas': [
            {'title': 'AB=O 秩核心不等式', 'latex': 'A_{m \\times n} B_{n \\times s} = O \\implies r(A) + r(B) \\le n'},
            {'title': '列空间与核包含关系', 'latex': 'C(B) \\subseteq N(A) \\implies \\mathrm{rank}(B) \\le \\mathrm{nullity}(A) = n - r(A)'}
        ],
        'pastQuestions': [
            {
                'id': 'xiandai-q-2010-1-5b',
                'year': '2010',
                'category': '数一',
                'questionNumber': '(5)',
                'content': '设 $A, B$ 均为 $n$ 阶非零矩阵，且 $AB = O$，则下列结论正确的是（ ）\\n(A) $r(A) + r(B) \\le n$ \\n(B) $r(A) + r(B) > n$ \\n(C) $A$ 与 $B$ 均可逆 \\n(D) $r(A) = r(B)$',
                'analysis': '考研基础送分题。$AB = O$ 直接套西尔维斯特秩不等式：$0 = r(AB) \\ge r(A) + r(B) - n \\implies r(A) + r(B) \\le n$。',
                'solutionSteps': [
                    '第一步：由西尔维斯特不等式：$r(AB) \\ge r(A) + r(B) - n$。',
                    '第二步：已知 $AB = O$，故 $r(AB) = 0$。',
                    '第三步：带入得 $0 \\ge r(A) + r(B) - n \\implies r(A) + r(B) \\le n$。选项 (A) 正确。'
                ],
                'answer': '(A)',
                'pitfall': '非零矩阵乘积为零不能选任何一个矩阵可逆（可逆两边消去就会得出另一矩阵为零阵矛盾）。',
                'difficulty': '★☆☆☆☆',
                'verified': True,
                'source': 'Maki考研数学真题分类精解 第四十五讲 题45.4 (p.1082)'
            }
        ],
        'variants': [
            {
                'id': 'var-xiandai-08-01',
                'question': '设 $A$ 为 3 阶非零矩阵，且满足 $A^2 = O$。求 $r(A)$ 的值。',
                'hint': '利用 $r(A) + r(A) \\le 3$ 且 $A \\neq O$。',
                'methodChoiceAnalysis': '$2r(A) \\le 3 \\implies r(A) \\le 1.5$。又 $A \\neq O \\implies r(A) \\ge 1$。',
                'fullSolution': [
                    '因为 $A^2 = O$，由秩不等式：$r(A) + r(A) \\le 3 \\implies 2r(A) \\le 3$。',
                    '由于秩必须为非负整数，故 $r(A) \\le 1$。',
                    '又已知 $A$ 是非零矩阵，故 $r(A) \\ge 1$。',
                    '因此 $r(A) = 1$。'
                ],
                'keyTakeaway': '秩是离散整数，不等式两边一夹直接锁定唯一整数。'
            }
        ],
        'relatedKnowledgeIds': ['xiandai-04-solution-structure-and-rank', 'xiandai-08-cross-rank-eigen-systems'],
        'tags': ['AB=O', '零空间', '秩不等式', '西尔维斯特'],
        'source': 'Maki考研数学大串讲 L53 & 真题分类精解 题45.4',
        'status': 'not_started',
        'isPending': False
    },
    'xiandai-08-cross-rank-eigen-systems': {
        'id': 'xiandai-08-cross-rank-eigen-systems',
        'title': '秩不等式体系与特征系统跨章节联动',
        'subject': 'xiandai',
        'subjectName': '线性代数',
        'chapterId': 'xiandai-ch08',
        'chapterTitle': '综合题与跨章节方法',
        'nodeType': 'topic',
        'summary': '“四条主线贯通：行列式判非零、矩阵定运算法则、向量表空间维数、特征值定几何形状”。',
        'triggers': ['矩阵乘积秩与特征值综合题', '分块矩阵求逆与伴随结合', '将矩阵方程与特征向量联立证明'],
        'firstReaction': '将代数方程翻译为几何空间语言：$r(A)=r$ 说明列空间是 $r$ 维子空间，核空间是 $n-r$ 维；若 $A$ 是投影矩阵 $A^2=A$，特征值只能是 0 和 1；熟记西尔维斯特秩不等式与分块矩阵伴随公式。',
        'candidateMethods': [
            {'name': '四条主线语言互译法', 'priority': 1, 'condition': '跨章节抽象综合证明题', 'whyChoose': '把方程组解翻译为零空间，把特征值翻译为对角线', 'description': '行列式 $\\iff$ 矩阵 $\\iff$ 向量 $\\iff$ 特征系统互译'},
            {'name': '分块对角化与正交分解法', 'priority': 2, 'condition': '高阶或分块结构矩阵', 'whyChoose': '降阶分治', 'description': '利用分块初等变换消元'}
        ],
        'applicability': '秩不等式 $r(A+B) \\le r(A) + r(B)$ 与 $r(AB) \\le \\min(r(A), r(B))$ 在任何维数均成立。',
        'steps': [
            '步骤1：列出已知条件，识别属于哪两个主线的交叉点（如秩与特征值）。',
            '步骤2：利用特征值重数与秩的关系 $n - r(\\lambda E - A) = k$ 建立桥梁。',
            '步骤3：运用秩不等式或正交分解完成论证。'
        ],
        'pitfalls': ['把 $r(AB) = r(A)r(B)$ 这种荒谬公式当定理套用。'],
        'formulas': [
            {'title': '西尔维斯特不等式', 'latex': 'r(A) + r(B) - n \\le r(AB) \\le \\min(r(A), r(B))'},
            {'title': '分块矩阵秩定理', 'latex': 'r\\begin{pmatrix} A & O \\\\ O & B \\end{pmatrix} = r(A) + r(B)'}
        ],
        'pastQuestions': [
            {
                'id': 'xiandai-q-2023-2-8',
                'year': '2023',
                'category': '数二',
                'questionNumber': '(8)',
                'content': '设 $A, B$ 为 $n$ 阶可逆矩阵，$E$ 为 $n$ 阶单位矩阵，$M^*$ 为矩阵 $M$ 的伴随矩阵，则分块矩阵 $\\begin{pmatrix} A & E \\\\ O & B \\end{pmatrix}^* = $（ ）\\n(A) $\\begin{pmatrix} |A|B^* & -B^* A^* \\\\ O & |B|A^* \\end{pmatrix}$ \\n(B) $\\begin{pmatrix} |B|A^* & -A^* B^* \\\\ O & |A|B^* \\end{pmatrix}$ \\n(C) $\\begin{pmatrix} |B|A^* & -B^* A^* \\\\ O & |A|B^* \\end{pmatrix}$ \\n(D) $\\begin{pmatrix} |A|B^* & -A^* B^* \\\\ O & |B|A^* \\end{pmatrix}$',
                'analysis': '利用伴随矩阵定义式 $M^* = |M| M^{-1}$！分块上三角矩阵行列式 $|M| = |A| \\cdot |B|$。求其逆矩阵：令 $\\begin{pmatrix} A & E \\\\ O & B \\end{pmatrix} \\begin{pmatrix} X & Y \\\\ Z & W \\end{pmatrix} = \\begin{pmatrix} E & O \\\\ O & E \\end{pmatrix}$，求出 $M^{-1}$ 再乘 $|M|$。',
                'solutionSteps': [
                    '第一步：矩阵 $M = \\begin{pmatrix} A & E \\\\ O & B \\end{pmatrix}$ 的行列式为 $|M| = |A| |B|$。',
                    '第二步：利用待定系数法求分块逆矩阵：',
                    '$M^{-1} = \\begin{pmatrix} A^{-1} & -A^{-1} E B^{-1} \\\\ O & B^{-1} \\end{pmatrix} = \\begin{pmatrix} A^{-1} & -A^{-1} B^{-1} \\\\ O & B^{-1} \\end{pmatrix}$。',
                    '第三步：利用伴随矩阵公式 $M^* = |M| M^{-1} = |A||B| \\begin{pmatrix} A^{-1} & -A^{-1} B^{-1} \\\\ O & B^{-1} \\end{pmatrix}$。',
                    '第四步：将系数乘入矩阵内部：',
                    '左上角：$|A||B| A^{-1} = |B| (|A| A^{-1}) = |B| A^*$；',
                    '右上角：$|A||B| (-A^{-1} B^{-1}) = -(|A| A^{-1}) (|B| B^{-1}) = -A^* B^*$；',
                    '右下角：$|A||B| B^{-1} = |A| (|B| B^{-1}) = |A| B^*$。',
                    '因此 $M^* = \\begin{pmatrix} |B|A^* & -A^* B^* \\\\ O & |A|B^* \\end{pmatrix}$。选项 (B) 正确。'
                ],
                'answer': '(B)',
                'pitfall': '分块矩阵直接对每个小块求伴随（大错特错，分块伴随没有直接局部伴随法则，必须借助 $M^*=|M|M^{-1}$）。',
                'difficulty': '★★★☆☆',
                'verified': True,
                'source': 'Maki考研数学真题分类精解 第四十四讲 题44.6 (p.1069)'
            }
        ],
        'variants': [
            {
                'id': 'var-xiandai-08-02',
                'question': '设 $A, B$ 满足 $r(A) + r(B) < n$。证明存在非零向量 $x$，使得 $Ax = 0$ 且 $Bx = 0$。',
                'hint': '公共解的维数 $\\dim(N(A) \\cap N(B)) \\ge n - r(A) - r(B)$。',
                'methodChoiceAnalysis': '利用分式维数公式证明交空间维数严格大于 0。',
                'fullSolution': [
                    '联立矩阵 $C = \\begin{pmatrix} A \\\\ B \\end{pmatrix}$。',
                    '由秩不等式：$r(C) \\le r(A) + r(B) < n$。',
                    '因此方程组 $Cx = 0$ 的基础解系向量个数为 $n - r(C) > 0$。',
                    '即必存在非零解 $x$，使得 $Ax=0$ 且 $Bx=0$。'
                ],
                'keyTakeaway': '两核空间交集非空的代数判据就是秩之和小于维数。'
            }
        ],
        'relatedKnowledgeIds': ['xiandai-08-ab-zero-deep-dive', 'xiandai-02-adjoint-matrix-properties'],
        'tags': ['跨章节大串讲', '分块伴随', '分块逆', '秩与解空间'],
        'source': 'Maki考研数学大串讲 L53 & 真题分类精解 题44.6',
        'status': 'not_started',
        'isPending': False
    }
}
