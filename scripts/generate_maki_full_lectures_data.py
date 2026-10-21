import os, fitz, re, json, sys

sys.stdout.reconfigure(encoding='utf-8')

pdf_path = 'Maki考研数学一站式大串讲 -2026-version 1.0(1).pdf'
doc = fitz.open(pdf_path)
toc = doc.get_toc()

print("Extracting TOC and mapping lectures...")

part_names = {
    0: "第 0 编 预备",
    1: "第 1 编 一元函数微积分",
    2: "第 2 编 常微分方程与差分方程",
    3: "第 3 编 多元函数微积分",
    4: "第 4 编 无穷级数",
    5: "第 5 编 线性代数",
    6: "第 6 编 概率论与数理统计",
    7: "第 7 编 应试工程"
}

curr_part = 0
lectures = []
curr_lec = None

for lvl, title, page in toc:
    m_part = re.search(r'第\s*(\d+)\s*编', title)
    if m_part:
        curr_part = int(m_part.group(1))

    m_lec = re.search(r'L(\d+)\s+([^\s\[]+)', title)
    if m_lec:
        lec_num = int(m_lec.group(1))
        is_key = '重点讲' in title or 'MakiRed重点讲' in title
        is_compressed = '压缩讲' in title or 'MakiGray压缩讲' in title
        is_math1_only = '仅一' in title or 'MakiRed仅一' in title
        is_math2_heavy = '二重' in title or 'MakiOrange二重' in title
        is_math3_only = '仅三' in title or 'MakiGreen仅三' in title
        is_method = lec_num in [1, 2, 28, 53, 64, 65, 66]

        clean_title = re.sub(r'\[.*?\]', '', title)
        clean_title = re.sub(r'Maki[A-Za-z]+[^\s]*', '', clean_title).strip()
        clean_title = re.sub(r'^L\d+\s*', '', clean_title).strip()

        curr_lec = {
            'num': lec_num,
            'id': f'L{lec_num:02d}',
            'partNum': curr_part,
            'partTitle': part_names.get(curr_part, f"第 {curr_part} 编"),
            'title': clean_title,
            'page': page,
            'isKey': is_key,
            'isCompressed': is_compressed,
            'isMath1Only': is_math1_only,
            'isMath2Heavy': is_math2_heavy,
            'isMath3Only': is_math3_only,
            'isMethod': is_method,
            'subsections': [],
        }
        lectures.append(curr_lec)
    elif lvl >= 3 and curr_lec:
        clean_sub = re.sub(r'\[.*?\]', '', title)
        clean_sub = re.sub(r'Maki[A-Za-z]+[^\s]*', '', clean_sub).strip()
        if clean_sub not in curr_lec['subsections']:
            curr_lec['subsections'].append(clean_sub)

# Dedup
dedup_lecs = []
seen = set()
for l in lectures:
    if l['num'] not in seen:
        seen.add(l['num'])
        dedup_lecs.append(l)

dedup_lecs.sort(key=lambda x: x['num'])

# Set pageEnd
for i in range(len(dedup_lecs)):
    next_page = dedup_lecs[i+1]['page'] if i + 1 < len(dedup_lecs) else len(doc)
    dedup_lecs[i]['pageEnd'] = next_page

# Lecture to mapped topic IDs mapping
topic_mappings = {
    1: ['yingshi-64-exam-time-structure'],
    2: ['gaoshu-00-algebra-five-actions'],
    3: ['gaoshu-01-indeterminate-0-0', 'gaoshu-01-sequence-monotone-bounded'],
    4: ['gaoshu-01-indeterminate-0-0', 'gaoshu-01-infinitesimal-order'],
    5: ['gaoshu-01-indeterminate-0-0', 'gaoshu-01-infinitesimal-order', 'gaoshu-01-power-exponential-1-inf'],
    6: ['gaoshu-01-sequence-monotone-bounded'],
    7: ['gaoshu-01-discontinuity-points'],
    8: ['gaoshu-02-derivative-definition'],
    9: ['gaoshu-02-higher-order-leibniz', 'gaoshu-05-chain-rule-composite', 'gaoshu-05-implicit-function-differentiation'],
    10: ['gaoshu-02-mean-value-theorems'],
    11: ['gaoshu-01-indeterminate-0-0', 'gaoshu-01-difference-inf-inf'],
    12: ['gaoshu-02-taylor-formula-proof'],
    13: ['gaoshu-01-indeterminate-0-0', 'gaoshu-10-cross-taylor-proofs'],
    14: ['gaoshu-02-inequality-and-roots'],
    15: ['gaoshu-02-inequality-and-roots'],
    16: ['gaoshu-03-variable-limit-integral'],
    17: ['gaoshu-03-variable-limit-integral'],
    18: ['gaoshu-03-variable-limit-integral', 'gaoshu-03-definite-integral-symmetry'],
    19: ['gaoshu-03-definite-integral-symmetry'],
    20: ['gaoshu-03-improper-integral-convergence'],
    21: ['gaoshu-03-geometric-applications'],
    22: ['gaoshu-03-geometric-applications'],
    23: ['gaoshu-03-variable-limit-integral', 'gaoshu-03-definite-integral-symmetry'],
    24: ['gaoshu-04-first-order-ode'],
    25: ['gaoshu-04-second-order-constant-coeff', 'gaoshu-04-reducible-ode'],
    26: ['gaoshu-04-euler-equation'],
    27: ['gaoshu-04-first-order-ode', 'gaoshu-04-second-order-constant-coeff'],
    28: ['gaoshu-09-vectors-planes-lines', 'gaoshu-09-surfaces-and-projections'],
    29: ['gaoshu-05-differentiability-concept'],
    30: ['gaoshu-05-chain-rule-composite', 'gaoshu-05-implicit-function-differentiation'],
    31: ['gaoshu-05-directional-derivative-gradient'],
    32: ['gaoshu-05-lagrange-multipliers'],
    33: ['gaoshu-06-double-integral-polar', 'gaoshu-06-order-exchange-symmetry'],
    34: ['gaoshu-06-triple-integral-coordinates'],
    35: ['gaoshu-07-curvilinear-path-independent', 'gaoshu-07-green-formula-hole-technique'],
    36: ['gaoshu-07-gauss-divergence-theorem'],
    37: ['gaoshu-07-stokes-theorem-curl'],
    38: ['gaoshu-08-series-convergence-tests'],
    39: ['gaoshu-08-series-convergence-tests'],
    40: ['gaoshu-08-power-series-radius-interval'],
    41: ['gaoshu-08-power-series-summation'],
    42: ['gaoshu-10-fourier-series-dirichlet'],
    43: ['xiandai-01-determinant-properties-definition', 'xiandai-01-determinant-calc-techniques'],
    44: ['xiandai-02-matrix-multiplication-inverse', 'xiandai-02-adjoint-matrix-properties'],
    45: ['xiandai-02-elementary-matrix-operations', 'xiandai-02-matrix-rank-theorems'],
    46: ['xiandai-03-vector-linear-combination-dependence', 'xiandai-03-maximal-linearly-independent-set'],
    47: ['xiandai-04-linear-system-solvability', 'xiandai-04-homogeneous-fundamental-system'],
    48: ['xiandai-04-non-homogeneous-general-solution', 'xiandai-04-matrix-equation-and-common-solutions'],
    49: ['xiandai-05-eigenvalues-eigenvectors', 'xiandai-05-eigen-properties-special-matrices'],
    50: ['xiandai-06-similarity-diagonalization-criterion', 'xiandai-06-power-trace-applications'],
    51: ['xiandai-06-real-symmetric-orthogonal-diag'],
    52: ['xiandai-07-quadratic-form-matrix-representation', 'xiandai-07-canonical-standard-form-methods', 'xiandai-07-positive-definite-criteria'],
    53: ['xiandai-08-cross-linear-algebra-mastery'],
    54: ['gailv-01-random-events-conditional-prob', 'gailv-01-total-probability-bayes', 'gailv-01-event-independence-bernoulli'],
    55: ['gailv-02-cdf-properties', 'gailv-02-common-discrete-distributions', 'gailv-02-common-continuous-distributions'],
    56: ['gailv-02-distribution-function-method'],
    57: ['gailv-03-joint-marginal-distributions', 'gailv-03-conditional-distribution-independence'],
    58: ['gailv-03-discrete-continuous-mixed-variables', 'gailv-03-convolution-formula-sum'],
    59: ['gailv-04-expectation-variance-properties', 'gailv-04-covariance-correlation-coefficient', 'gailv-04-chebyshev-inequality'],
    60: ['gailv-05-law-of-large-numbers', 'gailv-05-central-limit-theorem'],
    61: ['gailv-06-population-sample-statistics', 'gailv-06-three-sampling-distributions'],
    62: ['gailv-07-moment-and-mle-estimation', 'gailv-07-unbiasedness-eval-criteria'],
    63: ['gailv-08-confidence-interval-hypothesis-test'],
    64: ['yingshi-64-exam-time-structure'],
    65: ['yingshi-65-calculation-mistakes-checklist'],
    66: ['yingshi-66-survival-and-advanced-checklist']
}

# Process all 66 lectures
print("Extracting full text and generating makiLectures...")
processed_lectures = []

for l in dedup_lecs:
    num = l['num']
    p_start = l['page'] - 1
    p_end = min(l['pageEnd'], len(doc))

    # Read first 4 pages of lecture text
    sample_text = ""
    for p in range(p_start, min(p_start + 4, p_end)):
        sample_text += doc[p].get_text() + "\n"

    # 1. Orientation
    m_orient = re.search(r'本讲定位[：:](.*?)(?:定理/公式|三卷的基本盘|本讲真题考频|三条局部性质|定义|一、|1\.|\n\n[^\n]{1,10}\n)', sample_text, re.DOTALL)
    if m_orient:
        orient = m_orient.group(1).strip()
        orient = re.sub(r'\s+', ' ', orient)
    else:
        orient = f"本讲为《Maki考研数学一站式大串讲》核心讲次，全方位剖析 {l['title']} 的考查主线与经典题型。"

    # 2. Stats
    m_total = re.search(r'合计\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+)', sample_text)
    if m_total:
        ind_q = int(m_total.group(1))
        pos = int(m_total.group(2))
        c_cnt = int(m_total.group(3))
        b_cnt = int(m_total.group(4))
        s_cnt = int(m_total.group(5))
        s1 = int(m_total.group(6))
        s2 = int(m_total.group(7))
        s3 = int(m_total.group(8))
    else:
        ind_q = 0; pos = 0; c_cnt = 0; b_cnt = 0; s_cnt = 0; s1 = 0; s2 = 0; s3 = 0

    p1 = f"{(s1 / 2550 * 100):.2f}%" if s1 > 0 else "0.00%"
    p2 = f"{(s2 / 2550 * 100):.2f}%" if s2 > 0 else "0.00%"
    p3 = f"{(s3 / 2550 * 100):.2f}%" if s3 > 0 else "0.00%"

    stats = {
        'independentQuestions': ind_q,
        'positions': pos,
        'choiceCount': c_cnt,
        'blankCount': b_cnt,
        'solutionCount': s_cnt,
        'math1Score': s1,
        'math2Score': s2,
        'math3Score': s3,
        'math1Percent': p1,
        'math2Percent': p2,
        'math3Percent': p3,
        'avgDifficulty': '★★★★☆' if s_cnt > 5 else ('★★★☆☆' if pos > 5 else '★★☆☆☆')
    }

    # 3. Tags
    tags = []
    if l['isKey']: tags.append('重点讲')
    if l['isCompressed']: tags.append('压缩讲')
    if l['isMethod']: tags.append('方法课')
    if l['isMath1Only']: tags.append('数一专属')
    if l['isMath2Heavy']: tags.append('数二重点')
    if l['isMath3Only']: tags.append('数三专属')
    if not (l['isMath1Only'] or l['isMath3Only']): tags.append('统考必考')

    # 4. Method Cards specific to lecture
    method_cards = []
    
    if num == 1:
        method_cards.append({
            'title': '180分钟全卷宏观骨架与真题账本',
            'subtitle': '选填80分 + 解答70分新格局',
            'content': '解答题砍至6道后单题分值大幅上升，综合性极强；选填占比过半，必须保证极高正确率。线代三卷同价（每年雷打不动32.5分），数二高数占比46%（打歼灭战），数一概率线面积分占比最高（扫大片）。'
        })
    elif num == 2:
        method_cards.append({
            'title': '五大代数变形动作总表',
            'subtitle': '配方 · 有理化 · 裂项 · 放缩 · 换元',
            'content': '配方（二次三项式开方或积分必备）、有理化（根式差消去）、裂项（分母乘积拆和差）、放缩（常用不等式 e^x >= 1+x, ln(1+x) <= x）、换元（对称与三角代换）。'
        })
    elif num == 9:
        method_cards.append({
            'title': '求导技术全家桶六条法则与真实权重',
            'subtitle': '手快手顺 · 一遍算对',
            'content': '复合函数一阶导（链式法则）、隐函数一阶导（遇y就带出y\'）、参数方程一阶导（先反解t或直接除法）、二阶导（参数式与隐函数主力）、相关变化率、高阶导与莱布尼茨公式。'
        })
    elif num == 10:
        method_cards.append({
            'title': '微分中值定理五大构造套路与构造总表',
            'subtitle': '机械化逆推 · 百分百构建罗尔辅助函数',
            'content': '套路一：逆用导数乘积法则；套路二：乘积分因子 e^{P(x)}；套路三：乘幂函数 x^k；套路四：两次罗尔推二阶导；套路五：积分还原法。'
        })
    elif num == 13:
        method_cards.append({
            'title': '泰勒展开极限攻略核心准则',
            'subtitle': '展开到几阶 · 上下齐阶 · 复合式展开',
            'content': '分母为 x^k 则分子所有加减项统一展开到 x^k+o(x^k)；遇复杂幂指型先化为 e^{g(x)ln f(x)} 后再展开；严禁加减项部分等价替换而部分展开。'
        })
    elif num == 16:
        method_cards.append({
            'title': '不定积分换元与分部决策树',
            'subtitle': '动笔前先看结构',
            'content': '决策树四步：1. 分段函数找分界点；2. 凑微分（第一类换元）；3. 根式与三角代换（第二类换元）；4. 反对幂指三分部积分法。'
        })
    elif num == 19:
        method_cards.append({
            'title': '定积分方法选择表与华里士区间再现',
            'subtitle': '区间变换 · 对称性 · 直接读面积',
            'content': '对称区间奇零偶倍；对称区间再现公式 ∫_0^π x f(sin x)dx = (π/2)∫_0^π f(sin x)dx；华里士点火公式计算 sin^n x 定积分。'
        })
    elif num == 25:
        method_cards.append({
            'title': '二阶常系数线性微分方程解法全表',
            'subtitle': '特征方程三种根 · 待定系数特解设法',
            'content': '特征根 r1!=r2、r1=r2 二重根、一对共轭复根 α±iβ 对应的三种齐次通解形式；非齐次项 Pm(x)e^{λx} 与 e^{λx}[Pl cos ωx + Qn sin ωx] 的设特解原则。'
        })
    elif num == 33:
        method_cards.append({
            'title': '二重积分计算选择表（数二每年15.8分第一大讲）',
            'subtitle': '直角坐标切片 · 极坐标雅可比 · 轮换对称性',
            'content': 'X型先y后x，Y型先x后y；圆域扇形或 x^2+y^2 果断转极坐标（面积微元 r dr dθ，切勿漏乘r）；轮换对称性 ∬_D f(x)dσ = ∬_D f(y)dσ 大幅消项。'
        })
    elif num == 53:
        method_cards.append({
            'title': '大串讲：五条主线的语言互译总表',
            'subtitle': '几何 ⇄ 向量 ⇄ 方程 ⇄ 矩阵 ⇄ 二次型',
            'content': '几何共线垂直 ⇄ 向量线性相关正交 ⇄ 方程组有非零解与解的结构 ⇄ 矩阵秩与初等变换相似对角化 ⇄ 二次型正负惯性指数合同正定。五套语言一一等价翻译。'
        })
    elif num == 64:
        method_cards.append({
            'title': '180分钟卷面黄金时间分配与踩分规范',
            'subtitle': '选填65分钟 · 大题85分钟 · 检查30分钟',
            'content': '选择填空单题控制在3-4分钟，卡壳超5分钟立刻跳过；大题按踩分点书写，首句写定理依据与设元，中间写核心变形，末句写最终答案。'
        })
    elif num == 65:
        method_cards.append({
            'title': '考场计算失误清单与交卷前动作表',
            'subtitle': '读题 · 建模 · 选方法 · 计算 · 书写 五步防漏',
            'content': '交卷前必做：1. 读题回头核对问极值还是极值点；2. 圈出二阶导与连续前置词；3. 极坐标检查r因子；4. 高斯公式核对曲面内外侧法向量定向；5. 矩阵初等变换左行右列。'
        })
    elif num == 66:
        method_cards.append({
            'title': '保命清单（60-90分）与进阶清单（120-140分）',
            'subtitle': '分档攻坚 · 冲刺收官',
            'content': '保命清单：等价无穷小、一元求导法则、基本积分表、齐次线性方程组基础解系、二次型配方法、数字特征期望方差速算；进阶清单：双中值证明、反常积分判敛、微分方程应用建模、空间曲线曲面积分。'
        })
    else:
        sub_list_str = "、".join(l['subsections'][:4])
        method_cards.append({
            'title': f'{l["title"]} 核心方法梳理',
            'subtitle': f'涵盖 {len(l["subsections"])} 个进阶小节',
            'content': f'本讲重点掌握 {sub_list_str} 等核心知识链路，严格对齐考研大纲要求与历年命题规律。'
        })

    pitfalls = [
        f"未看清本讲在三卷中的具体分值权重与适用标签（{'、'.join(tags)}）。",
        "忽略定理适用的前提条件（如开闭区间、可导性、正交性或独立性前提）。"
    ]

    mapped_ids = topic_mappings.get(num, [])

    processed_lectures.append({
        'id': l['id'],
        'num': l['num'],
        'title': l['title'],
        'partNum': l['partNum'],
        'partTitle': l['partTitle'],
        'page': l['page'],
        'pageEnd': l['pageEnd'],
        'isKey': l['isKey'],
        'isCompressed': l['isCompressed'],
        'isMath1Only': l['isMath1Only'],
        'isMath2Heavy': l['isMath2Heavy'],
        'isMath3Only': l['isMath3Only'],
        'isMethod': l['isMethod'],
        'tags': tags,
        'orientation': orient,
        'subsections': l['subsections'],
        'stats': stats,
        'methodCards': method_cards,
        'pitfalls': pitfalls,
        'mappedTopicIds': mapped_ids
    })

print("Generated 66 lectures. Generating Maki War Map...")

war_map = {
    'topLectures': [
        {
            'paper': '数一',
            'totalScorePercent': '51.3%',
            'annualAvgPoints': '77.0 分',
            'list': [
                {'rank': 1, 'lectureId': 'L59', 'lectureTitle': '数字特征', 'scorePercent': '7.76%', 'annualPoints': '11.6分'},
                {'rank': 2, 'lectureId': 'L62', 'lectureTitle': '参数估计', 'scorePercent': '6.43%', 'annualPoints': '9.6分'},
                {'rank': 3, 'lectureId': 'L18', 'lectureTitle': '定积分与变限积分', 'scorePercent': '5.70%', 'annualPoints': '8.6分'},
                {'rank': 4, 'lectureId': 'L52', 'lectureTitle': '二次型', 'scorePercent': '5.40%', 'annualPoints': '8.1分'},
                {'rank': 5, 'lectureId': 'L36', 'lectureTitle': '曲面积分 (数一专属)', 'scorePercent': '5.31%', 'annualPoints': '8.0分'},
                {'rank': 6, 'lectureId': 'L50', 'lectureTitle': '相似对角化', 'scorePercent': '4.82%', 'annualPoints': '7.2分'},
                {'rank': 7, 'lectureId': 'L30', 'lectureTitle': '复合与隐函数求导', 'scorePercent': '4.24%', 'annualPoints': '6.4分'},
                {'rank': 8, 'lectureId': 'L40', 'lectureTitle': '幂级数', 'scorePercent': '4.00%', 'annualPoints': '6.0分'},
                {'rank': 9, 'lectureId': 'L14', 'lectureTitle': '导数的应用', 'scorePercent': '3.88%', 'annualPoints': '5.8分'},
                {'rank': 10, 'lectureId': 'L35', 'lectureTitle': '曲线积分 (数一专属)', 'scorePercent': '3.53%', 'annualPoints': '5.3分'},
            ]
        },
        {
            'paper': '数二',
            'totalScorePercent': '59.8%',
            'annualAvgPoints': '89.7 分',
            'list': [
                {'rank': 1, 'lectureId': 'L33', 'lectureTitle': '二重积分', 'scorePercent': '10.56%', 'annualPoints': '15.8分'},
                {'rank': 2, 'lectureId': 'L18', 'lectureTitle': '定积分与变限积分', 'scorePercent': '10.33%', 'annualPoints': '15.5分'},
                {'rank': 3, 'lectureId': 'L14', 'lectureTitle': '导数的应用', 'scorePercent': '5.98%', 'annualPoints': '9.0分'},
                {'rank': 4, 'lectureId': 'L21', 'lectureTitle': '定积分几何应用', 'scorePercent': '5.77%', 'annualPoints': '8.7分'},
                {'rank': 5, 'lectureId': 'L30', 'lectureTitle': '复合与隐函数求导', 'scorePercent': '5.49%', 'annualPoints': '8.2分'},
                {'rank': 6, 'lectureId': 'L52', 'lectureTitle': '二次型', 'scorePercent': '5.10%', 'annualPoints': '7.7分'},
                {'rank': 7, 'lectureId': 'L50', 'lectureTitle': '相似对角化', 'scorePercent': '4.78%', 'annualPoints': '7.2分'},
                {'rank': 8, 'lectureId': 'L47', 'lectureTitle': '线性方程组（一）', 'scorePercent': '4.55%', 'annualPoints': '6.8分'},
                {'rank': 9, 'lectureId': 'L25', 'lectureTitle': '二阶常系数线性方程', 'scorePercent': '4.35%', 'annualPoints': '6.5分'},
                {'rank': 10, 'lectureId': 'L13', 'lectureTitle': '泰勒展开求极限', 'scorePercent': '3.45%', 'annualPoints': '5.2分'},
            ]
        },
        {
            'paper': '数三',
            'totalScorePercent': '50.6%',
            'annualAvgPoints': '75.8 分',
            'list': [
                {'rank': 1, 'lectureId': 'L59', 'lectureTitle': '数字特征', 'scorePercent': '8.74%', 'annualPoints': '13.1分'},
                {'rank': 2, 'lectureId': 'L33', 'lectureTitle': '二重积分', 'scorePercent': '8.27%', 'annualPoints': '12.4分'},
                {'rank': 3, 'lectureId': 'L18', 'lectureTitle': '定积分与变限积分', 'scorePercent': '5.59%', 'annualPoints': '8.4分'},
                {'rank': 4, 'lectureId': 'L62', 'lectureTitle': '参数估计', 'scorePercent': '5.14%', 'annualPoints': '7.7分'},
                {'rank': 5, 'lectureId': 'L52', 'lectureTitle': '二次型', 'scorePercent': '4.98%', 'annualPoints': '7.5分'},
                {'rank': 6, 'lectureId': 'L50', 'lectureTitle': '相似对角化', 'scorePercent': '4.71%', 'annualPoints': '7.1分'},
                {'rank': 7, 'lectureId': 'L13', 'lectureTitle': '泰勒展开求极限', 'scorePercent': '4.01%', 'annualPoints': '6.0分'},
                {'rank': 8, 'lectureId': 'L47', 'lectureTitle': '线性方程组（一）', 'scorePercent': '3.80%', 'annualPoints': '5.7分'},
                {'rank': 9, 'lectureId': 'L30', 'lectureTitle': '复合与隐函数求导', 'scorePercent': '3.25%', 'annualPoints': '4.9分'},
                {'rank': 10, 'lectureId': 'L57', 'lectureTitle': '二维随机变量', 'scorePercent': '3.06%', 'annualPoints': '4.6分'},
            ]
        }
    ],
    'zeroExamTopics': [
        {
            'code': '6.1',
            'title': '单调有界准则与数列极限存在性',
            'lectureId': 'L06',
            'fact': '17年 0 道独立题。',
            'strategy': '准则本身不单独出题，它是递推数列题（6.2）里的固定一步，跟着递推题练骨架即可，无需单独做抽象证明训练。'
        },
        {
            'code': '7.2',
            'title': '零点定理与介值定理的应用',
            'lectureId': 'L07',
            'fact': '17年 0 道独立题。',
            'strategy': '从不单独命题，只作为方程根、不等式证明大题（L15）的第一步“造点”出现。会套用即可。'
        },
        {
            'code': '28.1',
            'title': '向量的运算与几何意义',
            'lectureId': 'L28',
            'fact': '17年 0 道独立题。',
            'strategy': '只留数量积、向量积、混合积三张公式，作为 L31、L35、L36 的前置计算工具，不做纯几何推导。'
        },
        {
            'code': '28.2',
            'title': '平面与直线的方程及位置关系',
            'lectureId': 'L28',
            'fact': '17年 0 道独立题。',
            'strategy': '压缩成一页速查表，不设例题，不做位置关系的复杂分类讨论训练。'
        },
        {
            'code': '28.3',
            'title': '曲面、空间曲线及其投影',
            'lectureId': 'L28',
            'fact': '17年 0 道独立题。',
            'strategy': '只保留常见二次曲面的立体图形与投影柱面的写法，服务于三重积分与曲面积分定限。'
        },
        {
            'code': '43.3',
            'title': '行列式与矩阵、特征值的联系',
            'lectureId': 'L43',
            'fact': '17年 0 道独立题。',
            'strategy': '只记 |A|=∏λi 与 tr(A)=∑λi 两条核心结论；其余题型均归入 L44 矩阵变形与 L50 对角化。'
        },
        {
            'code': '44.4',
            'title': '矩阵高次幂计算',
            'lectureId': 'L44',
            'fact': '17年 0 道独立题。',
            'strategy': '真题中求 A^n 一律以相似对角化 A=PΛP^{-1} 的形式出现，归在 L50.1 名下系统训练。'
        },
        {
            'code': '50.2',
            'title': '由特征信息反求矩阵',
            'lectureId': 'L50',
            'fact': '17年 0 道独立题。',
            'strategy': '真题给出的一律是实对称矩阵情形，整道题直接在 L51.2（实对称正交化）名下攻坚。'
        },
        {
            'code': '58.2',
            'title': '极值与顺序统计量分布',
            'lectureId': 'L58',
            'fact': '17年 0 道独立题。',
            'strategy': '只记 Fmax=F^n 与 Fmin=1-(1-F)^n；它总是数字特征（L59）与似然估计（L62）的中间步骤。'
        },
        {
            'code': '62.1',
            'title': '矩估计法',
            'lectureId': 'L62',
            'fact': '17年 0 道独立题。',
            'strategy': '只留“样本矩=总体矩”一步方程；核心精力全力攻坚最大似然估计（数一85分、数三79分）。'
        }
    ],
    'difficultyRanks': [
        {'lectureId': 'L10', 'lectureTitle': '微分中值定理（一）', 'difficulty': '3.44 星', 'reason': '14个题位里12个是解答题，全书区分度最高的一讲，必须掌握五大构造套路。'},
        {'lectureId': 'L06', 'lectureTitle': '递推数列极限', 'difficulty': '3.40 星', 'reason': '综合性强，单调有界+导数放缩+极限方程，解答题常客。'},
        {'lectureId': 'L15', 'lectureTitle': '不等式证明与方程根', 'difficulty': '3.44 星', 'reason': '12个题位里8个解答题，四条证明路线决策。'},
        {'lectureId': 'L36', 'lectureTitle': '曲面积分 (数一)', 'difficulty': '3.38 星', 'reason': '空间几何想象力与高斯散度外侧补底面计算量大。'},
        {'lectureId': 'L51', 'lectureTitle': '实对称矩阵', 'difficulty': '3.25 星', 'reason': '施密特正交化与特征向量方程组联立，步骤繁琐易失误。'}
    ],
    'shortestPaths': [
        {
            'paper': '数一',
            'lecturesCount': 66,
            'keyLecturesCount': 18,
            'estimatedHours': '约 35 小时',
            'strategySummary': '66 讲全覆盖，重点攻坚 18 讲重点讲。重心在第 3 编多元与线面积分（23.8%）及概率统计（21.6%）。'
        },
        {
            'paper': '数二',
            'lecturesCount': 44,
            'keyLecturesCount': 13,
            'estimatedHours': '约 24 小时',
            'strategySummary': '砍掉级数与概率，讲次最少但密度最大！高数吃掉 68.6% 分数。重点打歼灭战：吃透 L33、L18、L14、L21、L30 四讲即稳拿 42 分！'
        },
        {
            'paper': '数三',
            'lecturesCount': 57,
            'keyLecturesCount': 16,
            'estimatedHours': '约 31 小时',
            'strategySummary': '分布最平均的一卷，概率（L59、L62）、高数（L33、L18）、线代（L50、L52）三足鼎立。'
        }
    ]
}

# Create inverted topic to lecture mapping
topic_to_lecture = {}
for l in processed_lectures:
    for tid in l['mappedTopicIds']:
        topic_to_lecture[tid] = {
            'lectureId': l['id'],
            'lectureTitle': l['title']
        }

# Generate TypeScript code using standard string format
header = """/**
 * Maki 考研数学一站式大串讲 (2026-version 1.0) 完整 66 讲全讲次数据库
 * 包含：L01~L66 完整讲次定位、考频面板数据 (51套真题实测统计)、细分小节、独家方法卡与作战地图
 */

export interface MakiLectureStats {
  independentQuestions: number;
  positions: number;
  choiceCount: number;
  blankCount: number;
  solutionCount: number;
  math1Score: number;
  math2Score: number;
  math3Score: number;
  math1Percent: string;
  math2Percent: string;
  math3Percent: string;
  avgDifficulty: string;
}

export interface MakiMethodCard {
  title: string;
  subtitle?: string;
  content: string;
  keySteps?: string[];
  formulaLatex?: string;
}

export interface MakiLecture {
  id: string; // e.g. 'L01'
  num: number;
  title: string;
  partNum: number;
  partTitle: string;
  page: number;
  pageEnd: number;
  isKey: boolean;
  isCompressed: boolean;
  isMath1Only: boolean;
  isMath2Heavy: boolean;
  isMath3Only: boolean;
  isMethod: boolean;
  tags: string[];
  orientation: string;
  subsections: string[];
  stats: MakiLectureStats;
  methodCards: MakiMethodCard[];
  pitfalls: string[];
  mappedTopicIds: string[];
}

export interface MakiWarMap {
  topLectures: {
    paper: '数一' | '数二' | '数三';
    totalScorePercent: string;
    annualAvgPoints: string;
    list: { rank: number; lectureId: string; lectureTitle: string; scorePercent: string; annualPoints: string }[];
  }[];
  zeroExamTopics: {
    code: string;
    title: string;
    lectureId: string;
    fact: string;
    strategy: string;
  }[];
  difficultyRanks: {
    lectureId: string;
    lectureTitle: string;
    difficulty: string;
    reason: string;
  }[];
  shortestPaths: {
    paper: '数一' | '数二' | '数三';
    lecturesCount: number;
    keyLecturesCount: number;
    estimatedHours: string;
    strategySummary: string;
  }[];
}

"""

body = "export const MAKI_WAR_MAP: MakiWarMap = " + json.dumps(war_map, ensure_ascii=False, indent=2) + ";\n\n"
body += "export const TOPIC_TO_LECTURE: Record<string, { lectureId: string; lectureTitle: string }> = " + json.dumps(topic_to_lecture, ensure_ascii=False, indent=2) + ";\n\n"
body += "export const MAKI_LECTURES: MakiLecture[] = " + json.dumps(processed_lectures, ensure_ascii=False, indent=2) + ";\n"

with open('src/data/makiLectures.ts', 'w', encoding='utf-8') as f:
    f.write(header + body)

print("Saved src/data/makiLectures.ts with TOPIC_TO_LECTURE successfully!")
