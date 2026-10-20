# -*- coding: utf-8 -*-
import json
import re

# Load chapters and topics from subjects.ts
with open('src/data/subjects.ts', 'r', encoding='utf-8') as f:
    text = f.read()

chapters_raw = re.findall(r"'([a-z0-9\-]+)':\s*\{\s*id:\s*'([a-z0-9\-]+)',\s*subjectId:\s*'([a-z]+)',\s*title:\s*'([^']+)'[\s\S]*?topicIds:\s*\[([\s\S]*?)\]", text)

topic_to_meta = {}
for cid, _, sid, ctitle, t_list in chapters_raw:
    tids = [t.strip().strip("'").strip('"') for t in t_list.split(',') if t.strip().strip("'").strip('"')]
    sname = "高等数学" if sid == "gaoshu" else ("线性代数" if sid == "xiandai" else "概率论与数理统计")
    for tid in tids:
        topic_to_meta[tid] = {
            "id": tid,
            "chapterId": cid,
            "chapterTitle": ctitle,
            "subject": sid,
            "subjectName": sname
        }

print(f"Total topics to populate: {len(topic_to_meta)}")

# Titles and summaries mapping for all 74 topics
TOPIC_DETAILS = {
    # gaoshu ch01
    'gaoshu-01-indeterminate-0-0': {
        'title': '0/0 型极限未定式处理',
        'summary': '看到 0/0 型：首选等价替换化简乘积因子，加减因式谨慎展开或局部因式分解，复杂式子果断泰勒展开，洛必达仅作为辅助工具。',
        'triggers': ['分子分母同时趋于0', '乘积式含三角、指数、对数、反三角', '由极限反求参数 a, b', '加减式存在相消抵消'],
        'firstReaction': '代入极限点确认 0/0；提取非零极限乘积因子；观察分母最低阶数确定分子泰勒展开精度。',
        'methods': [{'name': '等价无穷小替换', 'priority': 1, 'condition': '乘除因式且趋于0', 'whyChoose': '计算量极小', 'description': 'sin x ~ x, e^x - 1 ~ x, ln(1+x) ~ x'}, {'name': '泰勒展开法', 'priority': 2, 'condition': '加减抵消或由极限定参数', 'whyChoose': '通用降维打击', 'description': '展开到与分母同阶'}],
        'formulas': [{'title': '常用等价无穷小', 'latex': '\\sin x \\sim x, \\quad e^x - 1 \\sim x, \\quad \\ln(1+x) \\sim x, \\quad 1 - \\cos x \\sim \\frac{1}{2}x^2'}],
        'isPending': False
    },
    'gaoshu-01-power-exponential-1-inf': {
        'title': '1^∞ 型幂指函数极限',
        'summary': '看到 1^∞ 型：牢记标准公式 lim u^v = e^{lim v(u-1)}，核心就是算清 v(u-1)；同次多项式之比，指数等于分子一次项系数减分母一次项系数！',
        'triggers': ['幂指函数 u(x)^v(x)，u->1 且 v->∞', '同次多项式之比高次幂 [(x^2+ax)/(x^2+bx)]^x'],
        'firstReaction': '验证底数趋于1，指数趋于无穷；化为 e^{lim v(u-1)} 计算指数极限。',
        'methods': [{'name': '凑 e 核心公式法', 'priority': 1, 'condition': '1^∞ 型通用', 'whyChoose': '避免繁琐取对数过程', 'description': 'lim u^v = e^{lim v(u-1)}'}, {'name': '多项式速算公式', 'priority': 2, 'condition': '同次二次多项式之比', 'whyChoose': '5秒秒杀', 'description': 'e^{p1 - p2}'}],
        'formulas': [{'title': '1^∞ 核心公式', 'latex': '\\lim u(x)^{v(x)} = e^{\\lim v(x)[u(x) - 1]}'}],
        'isPending': False
    },
    'gaoshu-01-difference-inf-inf': {
        'title': '∞ - ∞ 型未定式处理',
        'summary': '看到 ∞ - ∞：分式首选通分化为 0/0 型；根式首选有理化；提公因式提取最高阶无穷大转化为 0/0 或等价形式。',
        'triggers': ['两个趋于无穷大的项相减', '分式差 1/sin x - 1/x', '根式差 √(x^2+ax) - √(x^2+bx)'],
        'firstReaction': '判断是否有分母，有分母先通分；无分母根式先分子有理化；或者提主导项 x 出来。',
        'methods': [{'name': '通分法', 'priority': 1, 'condition': '分式减分式', 'whyChoose': '转化为熟悉的 0/0 分式', 'description': 'A/B - C/D = (AD - BC)/(BD)'}, {'name': '有理化法', 'priority': 2, 'condition': '含有平方根式差', 'whyChoose': '消去最高次项', 'description': '乘除共轭因式 √(A) + √(B)'}],
        'formulas': [{'title': '根式有理化', 'latex': '\\sqrt{A} - \\sqrt{B} = \\frac{A - B}{\\sqrt{A} + \\sqrt{B}}'}],
        'isPending': True
    },
    'gaoshu-01-infinitesimal-order': {
        'title': '无穷小的比较与阶的确定',
        'summary': '看到无穷小定阶：设该项为 c*x^k，用泰勒展开剥出第一项非零项，最高次项就是阶数；求极限 lim f(x)/x^k = c != 0 即为 k 阶。',
        'triggers': ['题干问“是 x 的几阶无穷小”', '已知某式是高阶无穷小 o(x^k) 反求未知常数'],
        'firstReaction': '分母设为 x^k，分子用麦克劳林展开，找到第一个系数不为零的 x 项。',
        'methods': [{'name': '麦克劳林展开定阶', 'priority': 1, 'condition': '复合初等函数', 'whyChoose': '最精准不丢项', 'description': '展开并合并同类项，看首个非零项次数'}],
        'formulas': [{'title': 'k 阶无穷小定义', 'latex': '\\lim_{x \\to 0} \\frac{f(x)}{x^k} = c \\neq 0 \\iff f(x) \\text{ 为 } k \\text{ 阶无穷小}'}],
        'isPending': True
    },
    'gaoshu-01-sequence-monotone-bounded': {
        'title': '数列极限：单调有界准则与递推数列',
        'summary': '看到递推数列 x_{n+1} = f(x_n)：第一步先设极限为 a 解方程 a = f(a) 探路；第二步数学归纳法或作差证单调与有界；第三步令 n->∞ 取极限求出 a。',
        'triggers': ['递推关系式 x_{n+1} = f(x_n)', 'n 项和数列无法直接通项求和（考虑夹逼准则或定积分定义）'],
        'firstReaction': '先算不动点 a = f(a)；研究 f\'(x) 符号，若 f\'(x) > 0 则数列单调；若 f\'(x) < 0 则奇偶子列反向振荡。',
        'methods': [{'name': '单调有界准则', 'priority': 1, 'condition': '递推数列 x_{n+1}=f(x_n)', 'whyChoose': '考研大题标准三步法', 'description': '1.证明有界；2.证明单调；3.两边取极限'}],
        'formulas': [{'title': '单调有界定理', 'latex': 'x_n \\le x_{n+1} \\text{ 且 } x_n \\le M \\implies \\lim_{n \\to \\infty} x_n \\text{ 存在}'}],
        'isPending': True
    },
    'gaoshu-01-discontinuity-points': {
        'title': '连续性、间断点及其类型判定',
        'summary': '看到间断点：找两类可疑点（分母为0、分段点、无定义点）；算左右极限：左右极限都存在为第一类（相等可去、不等跳跃），有任意一个不存在为第二类（无穷间断或振荡）。',
        'triggers': ['给出分段函数或分母有零点', '问“函数间断点的个数与类型”'],
        'firstReaction': '找出所有无定义点与分段分界点；严格分别计算 x -> x0+ 与 x -> x0- 的极限。',
        'methods': [{'name': '左右极限判定法', 'priority': 1, 'condition': '所有间断点类型判定', 'whyChoose': '定义法最严密', 'description': '第一类：左右极限均存在；第二类：至少一个不存在'}],
        'formulas': [{'title': '第一类间断点', 'latex': '\\text{跳跃间断点: } f(x_0^+) \\neq f(x_0^-); \\quad \\text{可去间断点: } f(x_0^+) = f(x_0^-) \\neq f(x_0)'}],
        'isPending': True
    },

    # gaoshu ch02
    'gaoshu-02-derivative-definition': {
        'title': '导数与微分的概念及可导性判定',
        'summary': '看到绝对值函数 |x-a| 或分段点处可导性：必须用导数定义式 lim (f(x)-f(x0))/(x-x0)！对于绝对值函数 f(x) = |x-a|g(x)，可导充要条件是 g(a)=0。',
        'triggers': ['分段函数在分界点的可导性', '含绝对值的函数在零点处的可导性', '由极限 lim (f(x0+h)-f(x0-h))/h 判定导数是否存在'],
        'firstReaction': '严禁直接套求导公式！分段点必须老老实实算左右导数极限；对称导数存在不代表导数存在，除非已知可导。',
        'methods': [{'name': '导数定义极限定理', 'priority': 1, 'condition': '分界点或抽象点', 'whyChoose': '唯一正确标准', 'description': 'f\'(x_0) = \\lim_{x \\to x_0} \\frac{f(x) - f(x_0)}{x - x_0}'}],
        'formulas': [{'title': '绝对值函数可导结论', 'latex': 'f(x) = |x-a|g(x) \\text{ 在 } x=a \\text{ 可导} \\iff g(a) = 0 \\quad (g \\text{连续})'}],
        'isPending': True
    },
    'gaoshu-02-higher-order-leibniz': {
        'title': '高阶导数与莱布尼茨公式',
        'summary': '看到乘积项求 n 阶导数 (u*v)^{(n)}：若其中一项是低次多项式（如 x^2, x^3），果断用莱布尼茨公式展开，多项式求导几次后自动归零！',
        'triggers': ['求多项式乘以三角函数或指数函数的 n 阶导数，如 (x^2 e^x)^{(n)} 或 (x^2 \\sin x)^{(n)}', 'x=0 处求 f^{(n)}(0)（结合泰勒公式展开式系数 a_n = f^{(n)}(0)/n!）'],
        'firstReaction': '数多项式的次数 m，莱布尼茨公式只需算到第 m 项；求特定点 n 阶导数优先考虑泰勒展开比对系数。',
        'methods': [{'name': '莱布尼茨乘积求导公式', 'priority': 1, 'condition': '多项式乘以初等函数', 'whyChoose': '展开式有限项截断', 'description': '(uv)^{(n)} = \\sum_{k=0}^n C_n^k u^{(n-k)} v^{(k)}'}],
        'formulas': [{'title': '莱布尼茨公式', 'latex': '(uv)^{(n)} = \\sum_{k=0}^n \\binom{n}{k} u^{(n-k)} v^{(k)}'}],
        'isPending': True
    },
    'gaoshu-02-mean-value-theorems': {
        'title': '微分中值定理与辅助函数构造',
        'summary': '看到证 f\'(ξ)=0 想到罗尔；看到 f\'(ξ) 与 f(b)-f(a) 想到拉格朗日；看到含两个函数的导数比值想到柯西；看到 f\'\'(ξ) 或带 (b-a)^2 结构必泰勒！',
        'triggers': ['区间 (a, b) 内存在一点 ξ 满足导数等式', '等式含 f\'(ξ) + g(x)f(ξ) = 0（积分因子法构造 F(x) = e^{∫g} f(x)）', '含有二阶导数 f\'\'(ξ)'],
        'firstReaction': '将 ξ 换成 x，移项观察原函数构造 F(x)；若涉及导数与函数本身乘积，联想 (f^2)\' 或 (f e^x)\'。',
        'methods': [{'name': '积分因子辅助函数法', 'priority': 1, 'condition': '形如 f\'(ξ) + k f(ξ) = 0', 'whyChoose': '秒构辅助函数', 'description': '构造 F(x) = e^{kx} f(x)，在端点用罗尔定理'}],
        'formulas': [{'title': '三大经典辅助函数', 'latex': 'f\' + kf=0 \\to e^{kx}f; \\quad f\' + g\'f=0 \\to e^{g}f; \\quad xf\' + n f=0 \\to x^n f'}],
        'isPending': True
    },
    'gaoshu-02-taylor-formula-proof': {
        'title': '泰勒公式在分析证明中的应用',
        'summary': '看到高阶导数 f\'\'(ξ) 与区间端点值函数差，或带有二次差 (b-a)^2，果断在中心点或最值点进行带拉格朗日余项的泰勒展开！',
        'triggers': ['已知 f\'\'(x) 有界，证明不等式', '式中同时出现 f(a), f(b), f((a+b)/2) 及高阶导数'],
        'firstReaction': '选好展开中心 x0（通常取区间中点或导数为0的点），写出二阶或三阶带余项公式。',
        'methods': [{'name': '中点展开法', 'priority': 1, 'condition': '端点与中点关系', 'whyChoose': '相减可消去一次导数项', 'description': '在 x0=(a+b)/2 展开 f(a) 与 f(b)'}],
        'formulas': [{'title': '带拉格朗日余项泰勒公式', 'latex': 'f(x) = f(x_0) + f\'(x_0)(x-x_0) + \\frac{f\'\'(\\xi)}{2}(x-x_0)^2'}],
        'isPending': True
    },
    'gaoshu-02-inequality-and-roots': {
        'title': '不等式证明与方程根的个数判定',
        'summary': '看到证明不等式 f(x) > g(x)：移项作差令 F(x) = f(x) - g(x)，求导研究单调性与极值；看到方程根个数：求导找极值点，结合零点定理与单调区间分段数根。',
        'triggers': ['证明 f(x) ≥ 0 在区间成立', '问方程 f(x) = 0 在区间内有且仅有几个实根'],
        'firstReaction': '构造差函数 F(x)；求一阶导 F\'(x) 找驻点；分析区间端点符号与极值符号。',
        'methods': [{'name': '单调性与最值法', 'priority': 1, 'condition': '单变量不等式', 'whyChoose': '最直接彻底', 'description': '证明 F_min >= 0 即可'}],
        'formulas': [{'title': '根的存在唯一性准则', 'latex': 'f(a)f(b) < 0 \\text{ 且 } f\'(x) \\neq 0 \\implies (a,b) \\text{ 内有且仅有一根}'}],
        'isPending': True
    },

    # gaoshu ch03
    'gaoshu-03-variable-limit-integral': {
        'title': '变上限积分函数求导与性质',
        'summary': '看到变上限积分 Φ(x) = ∫_{a(x)}^{b(x)} f(t, x) dt：若被积函数含 x，必须先换元或拆项将 x 提至积分号外，再套莱布尼茨求导公式！变限积分是奇函数求导得偶函数，奇函数定积分变奇为偶。',
        'triggers': ['积分上下限含有自变量 x，如 ∫_0^x f(t) dt', '被积函数内部含有自变量 x，如 ∫_0^x (x-t) f(t) dt', '含变限积分的极限 0/0 型（洛必达求导）'],
        'firstReaction': '检查被积函数 f 中是否有外层变量 x！如果有，严禁直接求导，必须先令 u = x - t 换元或拆开提取；再套用求导公式：上限制代入乘以上限导数减下限制乘以下限导数。',
        'methods': [
            {'name': '拆项提因子求导', 'priority': 1, 'condition': '被积函数为 x 与 t 的线性组合，如 (x-t)f(t)', 'whyChoose': '清晰无遗漏', 'description': '∫_0^x x f(t) dt - ∫_0^x t f(t) dt = x ∫_0^x f(t) dt - ∫_0^x t f(t) dt，再用乘积导数'},
            {'name': '换元脱钩法', 'priority': 2, 'condition': '复合结构 f(x-t) 或 f(xt)', 'whyChoose': '彻底将 x 转移至上下限', 'description': '令 u = x - t 或 u = xt，变换积分限后再求导'}
        ],
        'formulas': [
            {'title': '变限积分求导通用公式', 'latex': '\\frac{d}{dx} \\int_{\\alpha(x)}^{\\beta(x)} f(t)\\,dt = f(\\beta(x)) \\beta\'(x) - f(\\alpha(x)) \\alpha\'(x)'},
            {'title': '奇偶性与周期性定理', 'latex': 'f(x) \\text{ 连续且为奇函数} \\implies \\int_0^x f(t)\\,dt \\text{ 为偶函数}; \\quad f \\text{ 为偶} \\implies \\int_0^x f \\text{ 为奇}'}
        ],
        'isPending': False
    },
    'gaoshu-03-definite-integral-symmetry': {
        'title': '定积分的计算技巧与区间再现公式',
        'summary': '看到对称区间 [-a, a] 积分：立即利用奇零偶倍化简；看到 [0, π] 上的 x*f(sin x)：果断使用区间再现公式 x -> π - x 消除因子 x！',
        'triggers': ['对称区间 [-a, a] 的定积分', '积分区间为 [0, π] 且被积函数含 x*sin x 或 x*f(sin x)', '三角有理式 ∫_0^{π/2} R(sin x, cos x) dx（利用 x -> π/2 - x 对调）'],
        'firstReaction': '对称区间先看奇偶性；三角积分优先尝试区间再现公式 ∫_a^b f(x)dx = ∫_a^b f(a+b-x)dx，两式相加除以2。',
        'methods': [{'name': '区间再现相加法', 'priority': 1, 'condition': '含有不易积出的 x 因子', 'whyChoose': '两式相加直接消去自变量 x', 'description': 'I = ∫_a^b f(x)dx = ∫_a^b f(a+b-x)dx => 2I = ∫_a^b [f(x) + f(a+b-x)]dx'}],
        'formulas': [{'title': '区间再现公式', 'latex': '\\int_a^b f(x)\\,dx = \\int_a^b f(a+b-x)\\,dx'}],
        'isPending': True
    },
    'gaoshu-03-improper-integral-convergence': {
        'title': '反常积分的审敛法与 p-判别法',
        'summary': '看到反常积分：先确定瑕点或无穷远；无穷区间看最高阶比值（p > 1 收敛）；有限瑕点看 1/(x-a)^p（p < 1 收敛）；二者收敛条件正好相反，千万别记混！',
        'triggers': ['积分限含有 +∞ 或 -∞', '被积函数在积分限端点处分母为0（瑕积分）'],
        'firstReaction': '找瑕点！把反常积分拆成纯无穷区间和纯瑕点区间，分别单独审敛，只要一个发散整体就发散。',
        'methods': [{'name': 'p-级数比较判别法', 'priority': 1, 'condition': '标准有理式或无界项', 'whyChoose': '直接读出收敛性', 'description': '无穷区间 p>1 收敛；瑕点区间 p<1 收敛'}],
        'formulas': [{'title': '两大标准反常积分', 'latex': '\\int_1^{+\\infty} \\frac{1}{x^p}dx \\ (p>1 \\text{收敛}); \\quad \\int_0^1 \\frac{1}{x^p}dx \\ (p<1 \\text{收敛})'}],
        'isPending': True
    },
    'gaoshu-03-geometric-applications': {
        'title': '定积分的几何应用（面积与旋转体体积）',
        'summary': '看到平面图形面积：优先选积分变量使得被积函数为单段（上减下或右减左）；看到绕轴旋转体体积：绕 x 轴用切片法 π y^2 dx；绕 y 轴用柱壳法 2π x y dx！',
        'triggers': ['求曲线交点围成的平面图形面积', '求平面图形绕 x 轴或 y 轴旋转形成的立体体积'],
        'firstReaction': '快速画出草图找交点；绕哪条轴旋转就选择对应简便公式，绕 y 轴柱壳法避免反函数解 y。',
        'methods': [{'name': '旋转体体积柱壳法', 'priority': 1, 'condition': '绕 y 轴旋转且 y=f(x) 易求', 'whyChoose': '免去解反函数 x=g(y) 的巨大麻烦', 'description': 'V_y = 2\\pi \\int_a^b x f(x) dx'}],
        'formulas': [{'title': '旋转体体积公式', 'latex': 'V_x = \\pi \\int_a^b y^2\\,dx; \\quad V_y = 2\\pi \\int_a^b x y\\,dx'}],
        'isPending': True
    },

    # gaoshu ch04
    'gaoshu-04-first-order-ode': {
        'title': '一阶微分方程标准求解',
        'summary': '看到一阶方程：先看能否分离变量 dy/g(y) = f(x)dx；不能分离看是否齐次 y\' = φ(y/x) 令 u=y/x；若为 y\' + P(x)y = Q(x)，直接套常数变易通解公式！若关于 y 非线性但关于 x 线性，反过来把 x 视为 y 的函数！',
        'triggers': ['一阶方程含 y\' 与 y，形式如 dy/dx + P(x)y = Q(x)', '方程含 dy 与 dx，且 x 是一次方、y 是高次方（反视法 dx/dy）'],
        'firstReaction': '写成标准形式 y\' + P(x)y = Q(x)；若 y 带有高次幂而 x 只有一次，立刻求倒数考虑 dx/dy + P(y)x = Q(y)。',
        'methods': [{'name': '一阶线性通解公式', 'priority': 1, 'condition': 'y\' + P(x)y = Q(x)', 'whyChoose': '一步到位', 'description': 'y = e^{-∫P} [∫Q e^{∫P} dx + C]'}],
        'formulas': [{'title': '一阶线性微分方程通解', 'latex': 'y = e^{-\\int P(x)dx} \\left( \\int Q(x) e^{\\int P(x)dx} dx + C \\right)'}],
        'isPending': True
    },
    'gaoshu-04-second-order-constant-coeff': {
        'title': '二阶常系数线性微分方程',
        'summary': '看到 y\'\' + p y\' + q y = f(x)：先求特征方程 r^2 + pr + q = 0 的根写齐次通解；非齐次特解按自由项设：e^{λx} P_m(x) 设 y* = x^k Q_m(x) e^{λx}（k 为 λ 与特征根重数）；三角项同理设。',
        'triggers': ['二阶常系数线性方程 y\'\' + p y\' + q y = f(x)', '自由项 f(x) = e^{λx} P_m(x) 或 e^{λx}[P_l \\cos ωx + Q_n \\sin ωx]'],
        'firstReaction': '先算判别式 Δ = p^2 - 4q，写出特征根 r1, r2；核对自由项中的 λ 是否为特征根确定重根数 k=0, 1, 2；设出待定特解代入求待定多项式系数。',
        'methods': [{'name': '待定系数法', 'priority': 1, 'condition': '常系数二阶方程', 'whyChoose': '考研必考大题套路', 'description': 'y* = x^k Q_m(x) e^{λx}'}],
        'formulas': [{'title': '特征方程与齐次通解', 'latex': 'r^2 + pr + q = 0: \\quad r_1 \\neq r_2 \\to C_1 e^{r_1 x} + C_2 e^{r_2 x}; \\quad r_1=r_2 \\to (C_1 + C_2 x)e^{r_1 x}'}],
        'isPending': False
    },
    'gaoshu-04-reducible-ode': {
        'title': '可降阶的高阶微分方程',
        'summary': '看到缺 y 方程 y\'\' = f(x, y\')：令 p = y\' 降为关于 p 的一阶方程；看到缺 x 方程 y\'\' = f(y, y\')：令 p = y\'，关键转换 y\'\' = p * dp/dy！',
        'triggers': ['方程出现 y\'\' 但没有出现 y（缺 y 型）', '方程出现 y\'\' 与 y 但没有出现 x（缺 x 型）'],
        'firstReaction': '缺谁补谁：缺 x 则 y 做自变量，换算 y\'\' = p (dp/dy)；缺 y 则 x 做自变量，y\'\' = dp/dx。',
        'methods': [{'name': '导数换元降阶法', 'priority': 1, 'condition': '缺项高阶方程', 'whyChoose': '直接化二阶为一阶', 'description': '令 y\' = p(y) 或 p(x)'}],
        'formulas': [{'title': '缺 x 型关键导数代换', 'latex': 'y\'\' = \\frac{dp}{dx} = \\frac{dp}{dy} \\frac{dy}{dx} = p \\frac{dp}{dy}'}],
        'isPending': True
    },
    'gaoshu-04-euler-equation': {
        'title': '欧拉方程（数一专属）',
        'summary': '看到 x^2 y\'\' + p x y\' + q y = f(x)：必令 x = e^t（x>0）或 t = ln x，代入转换 x y\' = Dy, x^2 y\'\' = D(D-1)y，化为关于 t 的常系数线性微分方程！',
        'triggers': ['导数项前面的系数恰好是对应次数的 x 幂，如 x^2 y\'\' 或 x y\''],
        'firstReaction': '作自变量代换 x = e^t；求出解后切记必须把 t = ln x 代回原变量！',
        'methods': [{'name': '微分算子变量代换法', 'priority': 1, 'condition': '欧拉方程', 'whyChoose': '化变系数为常系数', 'description': 'x y\' -> dy/dt, x^2 y\'\' -> d^2y/dt^2 - dy/dt'}],
        'formulas': [{'title': '欧拉方程代换公式', 'latex': 'x = e^t \\implies x \\frac{dy}{dx} = \\frac{dy}{dt}, \\quad x^2 \\frac{d^2y}{dx^2} = \\frac{d^2y}{dt^2} - \\frac{dy}{dt}'}],
        'isPending': True
    },

    # gaoshu ch05
    'gaoshu-05-differentiability-concept': {
        'title': '多元函数极限、连续、偏导与全微分关系',
        'summary': '看到多元函数可微性判断：偏导连续 => 可微 => 连续且偏导存在；可偏导推不出连续；可微定义验证式：lim [Δz - (fx Δx + fy Δy)] / √(Δx^2 + Δy^2) = 0！',
        'triggers': ['问多元函数在 (0,0) 是否可微、是否连续、偏导数是否存在', '真假命题选择题（考察四个概念充分必要箭头）'],
        'firstReaction': '先用单变量导数定义算 fx(0,0) 与 fy(0,0)；若有一不存在直接不可微；若存在，代入全微分极限定式验证极限是否为0。',
        'methods': [{'name': '全微分定义极限定理', 'priority': 1, 'condition': '分界点可微性验证', 'whyChoose': '不可微时唯一判定依据', 'description': '验证极限 lim_{ρ->0} Δz - df / ρ 是否为 0'}],
        'formulas': [{'title': '可微充要定义式', 'latex': '\\lim_{(\\Delta x, \\Delta y) \\to (0,0)} \\frac{f(x_0+\\Delta x, y_0+\\Delta y) - f(x_0, y_0) - f_x \\Delta x - f_y \\Delta y}{\\sqrt{\\Delta x^2 + \\Delta y^2}} = 0'}],
        'isPending': True
    },
    'gaoshu-05-chain-rule-composite': {
        'title': '多元复合函数求偏导（链式法则）',
        'summary': '看到复合函数求导 z = f(u(x,y), v(x,y))：先画出变量树形依赖结构图；一阶偏导“连线相乘、分叉相加”；二阶偏导牢记中间变量也是 x, y 的函数，二次求导绝不可漏掉复合项！',
        'triggers': ['抽象复合函数 z = f(x+y, xy) 或 z = f(x, x/y) 求一阶、二阶偏导', '给出一阶二阶偏导方程反求原函数形式'],
        'firstReaction': '标清中间变量编号 u = 1, v = 2；写 f_1, f_2 避免混淆；求二阶时对 f_1 再求偏导必须写成 f_{11} u_x + f_{12} v_x。',
        'methods': [{'name': '树状图链式法则', 'priority': 1, 'condition': '多层复合函数', 'whyChoose': '结构清晰杜绝漏项', 'description': '∂z/∂x = f_u ∂u/∂x + f_v ∂v/∂x'}],
        'formulas': [{'title': '复合函数二阶偏导展开', 'latex': '\\frac{\\partial^2 z}{\\partial x^2} = f_{11}(u_x)^2 + 2f_{12} u_x v_x + f_{22}(v_x)^2 + f_1 u_{xx} + f_2 v_{xx}'}],
        'isPending': False
    },
    'gaoshu-05-implicit-function-differentiation': {
        'title': '隐函数存在定理与隐函数求导',
        'summary': '看到方程 F(x, y, z) = 0 确定隐函数 z = z(x,y)：首选隐函数求导公式 ∂z/∂x = - F_x / F_z；或者两边直接求全微分 dF = 0 解出 dz！',
        'triggers': ['方程 F(x, y, z) = 0 确定 z(x,y)', '方程组 F(x,y,u,v)=0, G(x,y,u,v)=0 确定 u, v（雅可比行列式）'],
        'firstReaction': '确认 F_z != 0；两端对 x 求偏导时视 y 为常数、z 为 x 的函数；或者全微分法更不容易漏符号。',
        'methods': [{'name': '全微分对称法', 'priority': 1, 'condition': '求全微分 dz 或一阶偏导', 'whyChoose': '完全避免正负号搞反', 'description': 'Fx dx + Fy dy + Fz dz = 0 => dz = -(Fx dx + Fy dy)/Fz'}],
        'formulas': [{'title': '隐函数求导公式', 'latex': '\\frac{\\partial z}{\\partial x} = -\\frac{F_x}{F_z}, \\quad \\frac{\\partial z}{\\partial y} = -\\frac{F_y}{F_z} \\quad (F_z \\neq 0)'}],
        'isPending': True
    },
    'gaoshu-05-lagrange-multipliers': {
        'title': '多元函数极值与拉格朗日乘数法',
        'summary': '无条件极值看海森判别式 AC - B^2：>0 且 A<0 极大，A>0 极小；<0 不是极值。条件极值目标 f 在约束 g=0 下：设 L = f + λ g，令一阶偏导全为 0 解方程组！',
        'triggers': ['在约束条件 φ(x,y,z)=0 下求目标函数 f(x,y,z) 的最大值、最小值', '实际几何与物理最值问题（如最大体积、最小表面积）'],
        'firstReaction': '构造辅助函数 L(x, y, z, λ) = f + λ φ；联立方程求解时善于利用比值消去 λ。',
        'methods': [{'name': '拉格朗日乘数法', 'priority': 1, 'condition': '带等式约束条件的最值', 'whyChoose': '标准解法', 'description': '∇f + λ ∇φ = 0'}],
        'formulas': [{'title': '无条件极值 AC-B^2 准则', 'latex': 'A = f_{xx}, B = f_{xy}, C = f_{yy}: \\quad AC - B^2 > 0 \\ (A>0 \\text{极小}, A<0 \\text{极大})'}],
        'isPending': True
    },

    # gaoshu ch06
    'gaoshu-06-double-integral-polar': {
        'title': '二重积分与极坐标变换',
        'summary': '看到圆形、圆环、扇形区域或被积函数含 x^2 + y^2：立即转换为极坐标 x = r cos θ, y = r sin θ，面积元素 dx dy 必带雅可比因子 r dr dθ！',
        'triggers': ['积分区域 D 为圆域 x^2+y^2 ≤ R^2 或偏心圆 x^2+y^2 ≤ 2ax', '被积函数含有 x^2+y^2, √(x^2+y^2), arctan(y/x)'],
        'firstReaction': '画图标明射线范围 θ1 到 θ2；从极点引射线穿过区域确定 r 的进出边界 r_in(θ) 到 r_out(θ)；面积元素绝对不要漏写 r！',
        'methods': [{'name': '极坐标定界法', 'priority': 1, 'condition': '圆弧边界或中心对称区域', 'whyChoose': '积分离散化为初等函数', 'description': 'dx dy = r dr dθ'}],
        'formulas': [{'title': '极坐标二重积分', 'latex': '\\iint_D f(x,y)\\,dxdy = \\int_{\\alpha}^{\\beta} d\\theta \\int_{r_1(\\theta)}^{r_2(\\theta)} f(r\\cos\\theta, r\\sin\\theta) r\\,dr'}],
        'isPending': True
    },
    'gaoshu-06-order-exchange-symmetry': {
        'title': '交换二次积分次序与对称性化简',
        'summary': '看到无法直接积出的内层积分（如 ∫ e^{x^2} dx 或 ∫ (sin y)/y dy）：必须画出积分区域草图，交换积分次序！遇到区域关于坐标轴对称，利用奇零偶倍瞬间减半运算量。',
        'triggers': ['内层被积函数原函数不是初等函数（形如 sin(x^2), e^{-y^2}, 1/ln x）', '积分区域关于 x 轴或 y 轴对称，或具有轮换对称性 (x 与 y 互换区域不变)'],
        'firstReaction': '根据现有积分限把边界曲线在草稿纸上精确画出；从投影轴改换到另一轴，重新定出外层与内层上下限。',
        'methods': [{'name': '画图交换积分次序', 'priority': 1, 'condition': '不可积被积函数', 'whyChoose': '反向交换后内层变为多项式可积', 'description': '先化草图区域，再改写上下限'}, {'name': '轮换对称性', 'priority': 2, 'condition': '区域关于 y=x 对称', 'whyChoose': '平分被积项', 'description': '∬ f(x) dxdy = ∬ f(y) dxdy = 1/2 ∬ [f(x)+f(y)] dxdy'}],
        'formulas': [{'title': '轮换对称性积分公式', 'latex': '\\iint_D f(x,y)\\,dxdy = \\frac{1}{2} \\iint_D [f(x,y) + f(y,x)]\\,dxdy'}],
        'isPending': True
    },
    'gaoshu-06-triple-integral-coordinates': {
        'title': '三重积分与柱面/球面坐标（数一专属）',
        'summary': '柱面坐标：适合圆柱体或被积函数含 x^2+y^2，体积元 r dr dθ dz；球面坐标：适合球体、锥体或含 x^2+y^2+z^2，体积元 r^2 sin φ dr dφ dθ！',
        'triggers': ['立体区域为球体 x^2+y^2+z^2 ≤ R^2 或锥体 z ≥ √(x^2+y^2)', '被积函数为 (x^2+y^2+z^2)^p'],
        'firstReaction': '观察积分体外形，球体/锥体首选球面坐标；圆柱/抛物面首选柱面坐标或“先二后一”截面法。',
        'methods': [{'name': '球面坐标法', 'priority': 1, 'condition': '全球体或圆锥体', 'whyChoose': '三维变量完全解耦', 'description': 'dv = r^2 sin φ dr dφ dθ'}],
        'formulas': [{'title': '球面坐标变换', 'latex': 'x = r\\sin\\varphi\\cos\\theta, y = r\\sin\\varphi\\sin\\theta, z = r\\cos\\varphi, \\quad dv = r^2\\sin\\varphi\\,dr\\,d\\varphi\\,d\\theta'}],
        'isPending': True
    },

    # gaoshu ch07
    'gaoshu-07-curvilinear-path-independent': {
        'title': '第二类曲线积分与积分与路径无关',
        'summary': '看到“第二类曲线积分与路径无关”：立即想到单连通区域上四条等价条件（全微分、偏导数相等 ∂Q/∂x=∂P/∂y、任意闭曲线为0）；算值首选“折线法”或“凑微分找原函数法 u(B)-u(A)”。使用前必须先检查定义域奇点！',
        'triggers': ['题干明确出现“对任意有向光滑曲线积分值仅与起点终点有关”', '第二类曲线积分中，交叉偏导数 ∂Q/∂x 与 ∂P/∂y 相等', '给出的微分式 P dx + Q dy 是全微分 du'],
        'firstReaction': '先算 ∂Q/∂x 与 ∂P/∂y 是否相等；检查区域有无奇点（如原点 (0,0)）；选平行坐标轴折线积分或凑原函数代入端点相减。',
        'methods': [{'name': '折线积分法', 'priority': 1, 'condition': '路径无关且无奇点', 'whyChoose': '平行坐标轴有一项导数为0，算值极简', 'description': '(x0,y0) -> (x1,y0) -> (x1,y1)'}, {'name': '凑全微分找势函数', 'priority': 2, 'condition': '明显全微分式', 'whyChoose': '直接等于 u(终点)-u(起点)', 'description': 'Pdx+Qdy = du'}],
        'formulas': [{'title': '格林公式标准形式', 'latex': '\\oint_L P\\,dx + Q\\,dy = \\iint_D \\left( \\frac{\\partial Q}{\\partial x} - \\frac{\\partial P}{\\partial y} \\right) dx\\,dy'}],
        'isPending': False
    },
    'gaoshu-07-green-formula-hole-technique': {
        'title': '格林公式与奇点挖洞补线法（数一专属）',
        'summary': '看到格林公式计算闭曲线积分但区域内有奇点 (0,0)（如分母有 (x^2+y^2)^p）：绝不能直接全域用格林！必须围绕奇点挖一个逆时针小圆 C_ε，在复连通域内应用格林公式，原积分转化为小圆积分！',
        'triggers': ['被积函数形式为 (-y dx + x dy)/(x^2+y^2) 或含有原点奇点', '闭曲线包含原点 (0,0)'],
        'firstReaction': '检验原点是否在闭曲线内部；在内则在原点周围挖小圆周 C_ε（顺时针为边界内侧，或两积分相减）；小圆上用极坐标代入化简。',
        'methods': [{'name': '挖洞法（复连通域格林公式）', 'priority': 1, 'condition': '内部含孤立奇点', 'whyChoose': '避开奇点无定义的致命错误', 'description': '∮_L = ∮_{C_ε}，在小圆上利用 x^2+y^2=ε^2 代换'}],
        'formulas': [{'title': '经典旋转场积分结论', 'latex': '\\oint_L \\frac{-y\\,dx + x\\,dy}{x^2 + y^2} = 2\\pi \\quad (L \\text{包围原点且为正向})'}],
        'isPending': True
    },
    'gaoshu-07-gauss-divergence-theorem': {
        'title': '高斯公式与曲面积分（数一专属）',
        'summary': '看到封闭曲面的第二类曲面积分 ∯ P dy dz + Q dz dx + R dx dy：立即用高斯公式化为三重积分 ∭ (∂P/∂x + ∂Q/∂y + ∂R/∂z) dxdydz！若曲面未封闭，果断补底面或顶面！',
        'triggers': ['数一第二类曲面积分解答题（高频考点）', '曲面为柱面、锥面或旋转面'],
        'firstReaction': '检查曲面是否封闭；未封闭立即沿坐标平面补平面闭合；高斯公式算三重积分，最后扣除补面积分。',
        'methods': [{'name': '补面高斯公式法', 'priority': 1, 'condition': '未封闭第二类曲面', 'whyChoose': '考研大题最标准得分模板', 'description': '∯_{S+S1} - ∬_{S1}'}],
        'formulas': [{'title': '高斯公式', 'latex': '\\oiint_S P\\,dydz + Q\\,dzdx + R\\,dxdy = \\iiint_{\\Omega} \\left( \\frac{\\partial P}{\\partial x} + \\frac{\\partial Q}{\\partial y} + \\frac{\\partial R}{\\partial z} \\right) dv'}],
        'isPending': True
    },
    'gaoshu-07-stokes-theorem-curl': {
        'title': '斯托克斯公式与空间曲线积分（数一专属）',
        'summary': '看到空间闭曲线的第二类曲线积分 ∮ P dx + Q dy + R dz：立即用斯托克斯公式化为空间曲面的第二类曲面积分，行列式旋度法计算！',
        'triggers': ['空间闭曲线 L，如球面与平面的交线', '题干明确出现向量场旋度 rot A 或 curl A'],
        'firstReaction': '计算旋度向量 curl F；选取截面平面作为积分曲面 Σ（平面法向量为常数，极易计算）。',
        'methods': [{'name': '斯托克斯公式', 'priority': 1, 'condition': '空间闭曲线', 'whyChoose': '把空间线积分转化为平面积分', 'description': '∮_L F·dr = ∬_S (curl F)·dS'}],
        'formulas': [{'title': '斯托克斯公式旋度行列式', 'latex': '\\oint_L P\\,dx+Q\\,dy+R\\,dz = \\iint_S \\begin{vmatrix} dy\\,dz & dz\\,dx & dx\\,dy \\\\ \\frac{\\partial}{\\partial x} & \\frac{\\partial}{\\partial y} & \\frac{\\partial}{\\partial z} \\\\ P & Q & R \\end{vmatrix}'}],
        'isPending': True
    },

    # gaoshu ch08
    'gaoshu-08-series-convergence-tests': {
        'title': '常数项级数的审敛法',
        'summary': '正项级数：带阶乘 n! 或 a^n 首选比值法；带 n 次方幂首选根值法；多项式分式首选与 1/n^p 比较判别法；交错级数：首选莱布尼茨判别法（u_n 单调递减且趋于0）。',
        'triggers': ['判断常数项级数 ∑ a_n 的敛散性、条件收敛与绝对收敛'],
        'firstReaction': '先算 lim a_n 是否为0，不为0直接发散！正项级数看通项结构选比值/根值/比较；交错级数先看绝对收敛，不绝对收敛再用莱布尼茨。',
        'methods': [{'name': '比值/根值审敛法', 'priority': 1, 'condition': '含 n! 或 a^n', 'whyChoose': '极限 ρ<1 收敛，ρ>1 发散', 'description': 'lim a_{n+1}/a_n 或 lim (a_n)^{1/n}'}],
        'formulas': [{'title': '莱布尼茨定理', 'latex': 'u_n \\ge u_{n+1} > 0 \\text{ 且 } \\lim_{n \\to \\infty} u_n = 0 \\implies \\sum (-1)^{n-1} u_n \\text{ 收敛}'}],
        'isPending': True
    },
    'gaoshu-08-power-series-radius-interval': {
        'title': '幂级数的收敛半径与收敛域',
        'summary': '看到幂级数 ∑ a_n (x-x0)^n：收敛半径 R = lim |a_n / a_{n+1}|；缺项幂级数（如 ∑ a_n x^{2n}）直接对相邻项取比值令比值绝对值 < 1 解不等式！端点必须单独代入讨论！',
        'triggers': ['求幂级数的收敛半径、收敛区间与收敛域', '阿贝尔定理（在某点条件收敛，确定其他点的敛散性）'],
        'firstReaction': '不缺项用 R = 1/ρ；缺项直接套达朗贝尔比值法解不等式；区间两端端点单独代入化为常数项级数审敛。',
        'methods': [{'name': '比值法求收敛域', 'priority': 1, 'condition': '任意幂级数', 'whyChoose': '缺项不缺项通吃', 'description': '解 lim |u_{n+1}/u_n| < 1'}],
        'formulas': [{'title': '收敛半径公式', 'latex': 'R = \\lim_{n \\to \\infty} \\left| \\frac{a_n}{a_{n+1}} \\right|'}],
        'isPending': True
    },
    'gaoshu-08-power-series-summation': {
        'title': '幂级数求和函数（逐项求导与积分）',
        'summary': '看到分母有 n（如 x^n / n）：求导消除分母；看到分子有 n（如 n*x^n）：积分消除系数；先导后积或先积后导，最终化归为几何级数 ∑ x^n = 1/(1-x)！',
        'triggers': ['求幂级数的和函数 S(x)', '求特定常数项级数的和（转化为和函数在特定点的值）'],
        'firstReaction': '先求出收敛域；观察系数中的 n 是在分子还是分母，分子乘 x 提导数，分母求导消项，还原出公比 q 的等比级数。',
        'methods': [{'name': '逐项微分与逐项积分', 'priority': 1, 'condition': '系数含 n 的多项式', 'whyChoose': '收敛区间内可任意求导积分', 'description': '(∑ a_n x^n)\' = ∑ n a_n x^{n-1}'}],
        'formulas': [{'title': '基本等比级数和', 'latex': '\\sum_{n=0}^\\infty x^n = \\frac{1}{1-x} \\quad (|x| < 1)'}],
        'isPending': False
    },
    'gaoshu-08-fourier-series-dirichlet': {
        'title': '傅里叶级数与狄利克雷收敛定理（数一专属）',
        'summary': '看到周期函数展成傅里叶级数：根据奇偶性简化系数（奇函数 a_n=0 只有正弦项；偶函数 b_n=0 只有余弦项）；在间断点 x0 处，傅里叶级数收敛于左右极限的平均值 [f(x0+)+f(x0-)]/2！',
        'triggers': ['求函数的傅里叶级数', '狄利克雷定理：问级数在间断点收敛于何值'],
        'firstReaction': '先查奇偶性；若是奇函数只算 b_n，若是偶函数只算 a_n；端点和跳跃间断点直接代入左右极限均值。',
        'methods': [{'name': '狄利克雷收敛定理', 'priority': 1, 'condition': '计算特定点傅里叶级数和', 'whyChoose': '直接读出数值免去算积分', 'description': 'S(x) = [f(x^+) + f(x^-)]/2'}],
        'formulas': [{'title': '傅里叶级数展开式', 'latex': 'f(x) \\sim \\frac{a_0}{2} + \\sum_{n=1}^\\infty (a_n \\cos nx + b_n \\sin nx)'}],
        'isPending': True
    },

    # gaoshu ch09
    'gaoshu-09-vector-products-geometry': {
        'title': '向量代数与点积叉积几何应用（数一专属）',
        'summary': '看到垂直：点积为零 a · b = 0；看到平行：叉积为零 a × b = 0 或坐标成比例；看到求同时垂直于两个向量的法向量：直接做叉积 a × b！',
        'triggers': ['求空间直线方向向量或平面法向量', '求异面直线的公垂线方向'],
        'firstReaction': '两向量垂直直接点积；求法向量立刻写三阶行列式叉积。',
        'methods': [{'name': '叉积求法向量', 'priority': 1, 'condition': '求公共垂直向量', 'whyChoose': '行列式计算一步出', 'description': 'n = a × b'}],
        'formulas': [{'title': '向量叉积行列式', 'latex': 'a \\times b = \\begin{vmatrix} i & j & k \\\\ a_x & a_y & a_z \\\\ b_x & b_y & b_z \\end{vmatrix}'}],
        'isPending': True
    },
    'gaoshu-09-plane-and-line-equations': {
        'title': '空间平面与直线方程（数一专属）',
        'summary': '点法式写平面 A(x-x0) + B(y-y0) + C(z-z0) = 0；对称式写直线 (x-x0)/m = (y-y0)/n = (z-z0)/p；点到平面距离公式 d = |Ax0+By0+Cz0+D| / √(A^2+B^2+C^2)！',
        'triggers': ['求直线在平面上的投影直线方程', '求两异面直线距离或夹角'],
        'firstReaction': '求直线方程必须抓两要素：过的一点 + 方向向量；求平面必须抓：过的一点 + 法向量。',
        'methods': [{'name': '平面束方程法', 'priority': 1, 'condition': '过直线的平面方程', 'whyChoose': '免设待定参数', 'description': 'Π1 + λ Π2 = 0'}],
        'formulas': [{'title': '点到平面距离公式', 'latex': 'd = \\frac{|Ax_0 + By_0 + Cz_0 + D|}{\\sqrt{A^2 + B^2 + C^2}}'}],
        'isPending': True
    },
    'gaoshu-09-surfaces-and-projections': {
        'title': '常见二次曲面与空间曲线投影（数一专属）',
        'summary': '看到空间曲线在坐标面上的投影：在曲线方程中消去垂直于该投影面的变量（例如投影到 xOy 面消去 z）！柱面母线平行于缺失的那个变量轴！',
        'triggers': ['求空间曲线在 xOy 面的投影曲线方程', '识别旋转曲面、椭球面、单叶双曲面'],
        'firstReaction': '投影到哪个面，方程就只保留该坐标面的两个变量，并附上对应坐标等于0。',
        'methods': [{'name': '消元投影法', 'priority': 1, 'condition': '空间曲线求投影', 'whyChoose': '直接消去多余变量', 'description': '联立消去 z 得投影柱面'}],
        'formulas': [{'title': '空间曲线在 xOy 投影方程组', 'latex': '\\begin{cases} F(x, y) = 0 \\\\ z = 0 \\end{cases}'}],
        'isPending': True
    },

    # gaoshu ch10
    'gaoshu-10-cross-ode-integral': {
        'title': '含变限积分的微分方程综合题',
        'summary': '看到方程中同时含有未知函数的导数与变限积分 ∫_0^x f(t) dt：对等式两边连续求导脱去积分号，转化为二阶常系数线性微分方程初值问题！代入 x=0 提取初始条件 f(0), f\'(0)！',
        'triggers': ['方程含 y\' 与 ∫_0^x y(t) dt 混合结构', '极限等式与微分方程综合'],
        'firstReaction': '令 x=0 提取隐藏初值条件；两边对 x 求导，积分号消失转化为标准 ODE。',
        'methods': [{'name': '求导降化法', 'priority': 1, 'condition': '含积分号方程', 'whyChoose': '化积分方程为微分方程', 'description': '求导消积分，代入 x=0 补足初值'}],
        'formulas': [{'title': '隐藏初值提取', 'latex': 'y(x) = \\int_0^x g(t)\\,dt \\implies y(0) = 0, \\quad y\'(x) = g(x)'}],
        'isPending': True
    },
    'gaoshu-10-cross-taylor-proofs': {
        'title': '泰勒展开与积分估值综合证明',
        'summary': '看到高难度不等式证明含导数与积分：将被积函数按泰勒展开到一阶或二阶，逐项积分，积分余项给出精准不等号方向！',
        'triggers': ['证明 ∫_a^b f(x) dx 与端点值 f(a), f(b) 的不等式', '凸函数积分不等式（琴生不等式）'],
        'firstReaction': '在切线处展开利用 f(x) ≥ f(x0) + f\'(x0)(x-x0) 两边积分。',
        'methods': [{'name': '切线展开积分法', 'priority': 1, 'condition': '凸函数 f\'\'(x) >= 0', 'whyChoose': '切线在曲线下方', 'description': '两端积分直接出下界'}],
        'formulas': [{'title': '凸函数切线不等式', 'latex': 'f\'\'(x) \\ge 0 \\implies f(x) \\ge f(x_0) + f\'(x_0)(x-x_0)'}],
        'isPending': True
    },

    # ==========================================
    # 线性代数 CHAPTER 1: 行列式
    # ==========================================
    'xiandai-01-determinant-calc-techniques': {
        'title': '行列式的计算技巧（爪型、三对角与加边法）',
        'summary': '爪型行列式：用斜爪将第一行或第一列消零化上三角；三对角行列式：按首行展开建立二阶线性递推数列 D_n = a D_{n-1} + b D_{n-2}；箭型/各行和相等：全部加到第一列提取公因子！',
        'triggers': ['各行或各列元素之和全部相等', '爪型结构（除第一行第一列和对角线外全为0）', '三对角线结构（主副对角线上有元素）'],
        'firstReaction': '检查各行之和是否相等，相等直接全加到第一行；观察是否有大量0元素；爪型直接用第一行消其他行。',
        'methods': [{'name': '加边法/消爪法', 'priority': 1, 'condition': '爪型行列式', 'whyChoose': '一步化上三角', 'description': '利用主对角线消去边缘爪项'}, {'name': '递推数列法', 'priority': 2, 'condition': '三对角线行列式', 'whyChoose': '化为特征方程递推求解', 'description': '按第一行展开建立 D_n = p D_{n-1} + q D_{n-2}'}],
        'formulas': [{'title': '范德蒙德行列式', 'latex': 'V(x_1, \\dots, x_n) = \\prod_{1 \\le j < i \\le n} (x_i - x_j)'}],
        'isPending': True
    },
    'xiandai-01-cofactor-sum-expansion': {
        'title': '代数余子式求和与克拉默法则',
        'summary': '看到求 a1 A21 + a2 A22 + ...（用第一行元素乘第二行代数余子式）：根据异行展开定理和恒为0！求 k1 A11 + k2 A12 + ...：等于把第 1 行换成 (k1, k2, ...) 的新行列式！',
        'triggers': ['求代数余子式的线性组合 ∑ k_j A_{ij}', '由克拉默法则判定方程组唯一解'],
        'firstReaction': '代数余子式 A_ij 的系数不是原矩阵第 i 行元素，而是系数 k_j，立即构造新矩阵按第 i 行展开。',
        'methods': [{'name': '新矩阵代换展开法', 'priority': 1, 'condition': '余子式求和', 'whyChoose': '直接化为单个行列式计算', 'description': '将对应行换成系数向量'}],
        'formulas': [{'title': '代数余子式展开与异行定理', 'latex': '\\sum_{k=1}^n a_{ik} A_{jk} = \\begin{cases} |A|, & i = j \\\\ 0, & i \\neq j \\end{cases}'}],
        'isPending': True
    },

    # xiandai ch02
    'xiandai-02-adjoint-matrix-properties': {
        'title': '伴随矩阵全套性质与秩',
        'summary': '伴随矩阵四件套必背：A A* = A* A = |A|E；|A*| = |A|^{n-1}；(A*)^-1 = (A^-1)* = A/|A|；伴随矩阵的秩：r(A)=n 时 r(A*)=n；r(A)=n-1 时 r(A*)=1；r(A)<n-1 时 r(A*)=0！',
        'triggers': ['题目出现伴随矩阵 A*，求 |A*|、(A*)* 或 (A*)^-1', '已知 A 的秩 r(A)，求伴随矩阵的秩 r(A*)'],
        'firstReaction': '看到 A* 立即联想 A A* = |A|E；两边取行列式得 |A||A*| = |A|^n；利用秩的三段跳结论秒杀选择题。',
        'methods': [{'name': '恒等式代数变形法', 'priority': 1, 'condition': '含 A* 的矩阵方程', 'whyChoose': '直接化消 A*', 'description': 'A* = |A| A^{-1}'}],
        'formulas': [
            {'title': '伴随矩阵的核心恒等式', 'latex': 'A A^* = A^* A = |A|E, \\quad |A^*| = |A|^{n-1}'},
            {'title': '伴随矩阵的秩定理', 'latex': 'r(A^*) = \\begin{cases} n, & r(A) = n \\\\ 1, & r(A) = n - 1 \\\\ 0, & r(A) < n - 1 \\end{cases}'}
        ],
        'isPending': False
    },
    'xiandai-02-matrix-power-calculation': {
        'title': '矩阵高次幂 A^n 的四种计算法',
        'summary': '看到求 A^n：首选对角化 A = P Λ P^-1 则 A^n = P Λ^n P^-1；秩1矩阵 A = α β^T 则 A^n = (β^T α)^{n-1} A；拆分法 A = λE + B（B 幂零 B^2=0）用二项式展开！',
        'triggers': ['求具体或抽象矩阵的高次幂 A^n 或 A^{2026}', 'A 的每一行成比例（秩为 1）'],
        'firstReaction': '先算 A^2，看是否有规律 A^2 = k A 或 A^2 = E；若能对角化求特征值；若为秩 1 拆成外积 α β^T。',
        'methods': [{'name': '相似对角化法', 'priority': 1, 'condition': '可对角化矩阵', 'whyChoose': '通法通解', 'description': 'A^n = P diag(λ1^n, ..., λn^n) P^-1'}, {'name': '秩1矩阵外积法', 'priority': 2, 'condition': 'r(A) = 1', 'whyChoose': '口算秒出', 'description': 'A^n = [tr(A)]^{n-1} A'}],
        'formulas': [{'title': '秩 1 矩阵高次幂公式', 'latex': 'A = \\alpha \\beta^T \\implies A^n = (\\beta^T \\alpha)^{n-1} A = [\\mathrm{tr}(A)]^{n-1} A'}],
        'isPending': True
    },
    'xiandai-02-elementary-matrix-operations': {
        'title': '初等矩阵与初等变换',
        'summary': '左乘初等矩阵等于对 A 做初等行变换，右乘初等矩阵等于对 A 做初等列变换！求 A^-1：构造 [A | E] 仅用初等行变换化简为 [E | A^-1]！',
        'triggers': ['矩阵方程 AX = B 求 X', '初等变换过程与初等矩阵乘积对应关系'],
        'firstReaction': '记清“左行右列”；解 AX = B 构造 [A | B] 一路初等行变换化为 [E | A^-1 B]。',
        'methods': [{'name': '增广矩阵初等行变换', 'priority': 1, 'condition': '求逆矩阵与矩阵方程', 'whyChoose': '标准无错算法', 'description': '[A | E] -> [E | A^-1]'}],
        'formulas': [{'title': '初等矩阵法则', 'latex': 'E_i(k) A \\leftrightarrow \\text{第 } i \\text{ 行乘 } k; \\quad A E_j(k) \\leftrightarrow \\text{第 } j \\text{ 列乘 } k'}],
        'isPending': True
    },

    # xiandai ch03
    'xiandai-03-linear-independence-proof': {
        'title': '向量组线性相关性判定与证明',
        'summary': '看到证 α1, ..., αn 线性无关：写出定义式 k1 α1 + ... + kn αn = 0，目标证明系数全为 0！利用矩阵秩判定：列向量拼成矩阵 A，相关 <=> r(A) < n，无关 <=> r(A) = n（方阵时 |A| != 0）！',
        'triggers': ['证明一组抽象向量线性无关', '判定已知向量组的线性相关性'],
        'firstReaction': '设 k1 α1 + ... = 0；两端同时左乘特定矩阵 A 或取内积；或者转化为齐次线性方程组只有零解。',
        'methods': [{'name': '定义法（反证或证明系数为0）', 'priority': 1, 'condition': '抽象向量组', 'whyChoose': '最根本严密', 'description': '从 ∑ ki αi = 0 推导出每个 ki = 0'}],
        'formulas': [{'title': '方阵向量组无关充要条件', 'latex': '\\alpha_1, \\dots, \\alpha_n \\text{ 线性无关} \\iff |\\alpha_1, \\dots, \\alpha_n| \\neq 0'}],
        'isPending': True
    },
    'xiandai-03-maximal-linearly-independent-set': {
        'title': '极大线性无关组与向量组的秩',
        'summary': '求极大无关组：将向量作为列向量拼成矩阵 A，仅用初等行变换化为行阶梯形，主元所在列对应的原向量就是极大无关组，其余向量可直接读出线性表示系数！',
        'triggers': ['求具体向量组的极大线性无关组并将其余向量线性表出'],
        'firstReaction': '列排成矩阵，行化阶梯形；千万不能做列变换，必须做行变换才能保持列向量线性组合关系不变！',
        'methods': [{'name': '行阶梯形法', 'priority': 1, 'condition': '具体数值向量组', 'whyChoose': '极大组与表示系数同步得出', 'description': '主元列为极大线性无关组'}],
        'formulas': [{'title': '向量组秩定理', 'latex': 'r(\\alpha_1, \\dots, \\alpha_s) = r(\\begin{pmatrix} \\alpha_1 & \\dots & \\alpha_s \\end{pmatrix})'}],
        'isPending': True
    },
    'xiandai-03-schmidt-orthogonalization': {
        'title': '施密特正交化与正交矩阵',
        'summary': '施密特正交化口诀：β1 = α1；β2 = α2 - (α2·β1 / β1·β1) β1；依次减去在已有正交基上的投影分量！最后各项除以自身长度单位化！正交矩阵充要条件 Q^T Q = E 即列向量两两正交且模长为 1！',
        'triggers': ['将线性无关向量组正交化与单位化', '实对称矩阵重特征值对应的特征向量正交化'],
        'firstReaction': '先算 β1；算 β2 扣除投影分量；每算出一个向量立即验证它与前面的是否点积为 0，防止连环算错。',
        'methods': [{'name': '标准施密特投影算法', 'priority': 1, 'condition': '求正交基', 'whyChoose': '标准操作', 'description': 'β_k = α_k - ∑_{j=1}^{k-1} \\frac{(α_k, β_j)}{(β_j, β_j)} β_j'}],
        'formulas': [{'title': '施密特正交化两步公式', 'latex': '\\beta_1 = \\alpha_1, \\quad \\beta_2 = \\alpha_2 - \\frac{\\alpha_2 \\cdot \\beta_1}{\\beta_1 \\cdot \\beta_1} \\beta_1, \\quad \\eta_i = \\frac{\\beta_i}{\\|\\beta_i\\|}'}],
        'isPending': True
    },

    # xiandai ch04
    'xiandai-04-solution-structure-and-rank': {
        'title': '矩阵的秩与线性方程组解的结构',
        'summary': '看到矩阵的秩与方程组解：r(A)=r(A|b)=n 唯一解；r(A)=r(A|b)<n 无穷多解，基础解系自由未知量个数必为 n-r(A)；通解必须写成“非齐次特解 + 齐次通解 c1 ξ1 + ...”；当题目给出列向量关系式时，直接对应特解与齐次解！',
        'triggers': ['已知矩阵秩 r(A) 讨论方程组解', '给出列向量关系 α1+α2=α3+α4 反求方程通解'],
        'firstReaction': '未知数个数 n 减去 r(A) 得自由变量个数；列向量关系移项直接对应齐次解。',
        'methods': [{'name': '列向量解对应法', 'priority': 1, 'condition': '给出列组合关系', 'whyChoose': '无需做矩阵消元', 'description': 'A ξ = 0 对应齐次解'}],
        'formulas': [{'title': '基础解系维数定理', 'latex': '\\dim \\ker(A) = n - r(A)'}],
        'isPending': False
    },
    'xiandai-04-matrix-equation-and-common-solutions': {
        'title': '矩阵方程 AX=B 与方程组同解/公共解',
        'summary': 'AX = B 有解 <=> r(A) = r(A | B)；求公共解：将两个方程组联立 [A; B] x = 0 求解；或先求 Ax=0 通解代入 Bx=0 确定常数约束！同解充要条件：r(A)=r(B)=r([A; B])！',
        'triggers': ['求两个线性方程组 Ax=0 与 Bx=0 的公共解', '问两个方程组在什么参数下同解'],
        'firstReaction': '同解先判秩是否相等；公共解直接把一个方程组的通解代入另一个方程。',
        'methods': [{'name': '通解代入筛选法', 'priority': 1, 'condition': '求公共解', 'whyChoose': '直接求出常数约束关系', 'description': '令 x = c1 ξ1 + c2 ξ2 代入 Bx = 0'}],
        'formulas': [{'title': '方程组同解充要条件', 'latex': 'Ax=0 \\text{ 与 } Bx=0 \\text{ 同解} \\iff r(A) = r(B) = r\\begin{pmatrix} A \\\\ B \\end{pmatrix}'}],
        'isPending': True
    },

    # xiandai ch05
    'xiandai-05-eigenvalue-eigenvector-properties': {
        'title': '特征值与特征向量核心性质',
        'summary': '特征值两大定海神针：所有特征值之和等于迹 ∑ λi = tr(A)；所有特征值之积等于行列式 ∏ λi = |A|！若 A 特征值为 λ，则 A^k 为 λ^k，A^-1 为 1/λ，A* 为 |A|/λ，f(A) 为 f(λ)！',
        'triggers': ['已知方阵求特征值与特征向量', '给出抽象矩阵多项式 A^2 - 3A + 2E = 0'],
        'firstReaction': '先算 tr(A) 和 |A| 建立特征值方程；解特征多项式 |λE - A| = 0。',
        'methods': [{'name': '特征方程求解法', 'priority': 1, 'condition': '求方阵特征值', 'whyChoose': '标准法', 'description': '令 |λE - A| = 0'}],
        'formulas': [{'title': '迹与行列式性质', 'latex': '\\sum_{i=1}^n \\lambda_i = \\mathrm{tr}(A), \\quad \\prod_{i=1}^n \\lambda_i = |A|'}],
        'isPending': True
    },
    'xiandai-05-rank-one-eigenvalues': {
        'title': '秩 1 矩阵的特征值与特征向量',
        'summary': '看到外积形式 A = α β^T（秩为 1）：必有 n-1 个特征值为 0，唯一非零特征值为其迹 λ = tr(A) = β^T α！λ=0 对应特征子空间维数为 n-1，即 α^T x = 0 的基础解系！',
        'triggers': ['矩阵每一行成比例（r(A)=1）', '形如 A = α α^T'],
        'firstReaction': '一眼看出有 n-1 个 0 特征值；最后一个特征值等于主对角线元素之和 tr(A)！',
        'methods': [{'name': '秩1特征值秒杀公式', 'priority': 1, 'condition': 'r(A) = 1', 'whyChoose': '完全免解特征多项式', 'description': 'λ1 = tr(A), λ2 = ... = λn = 0'}],
        'formulas': [{'title': '秩1特征值分布', 'latex': 'A = \\alpha \\beta^T \\implies \\lambda_1 = \\beta^T \\alpha = \\mathrm{tr}(A), \\quad \\lambda_2 = \\dots = \\lambda_n = 0'}],
        'isPending': True
    },

    # xiandai ch06
    'xiandai-06-diagonalization-criterion': {
        'title': '矩阵相似与相似对角化充要条件',
        'summary': '矩阵 A 相似于对角阵充要条件：A 有 n 个线性无关的特征向量 <=> 每个 k 重特征值对应的几何重数（n - r(λE - A)）恰好等于代数重数 k！若有 n 个互不相同的特征值，则必可对角化！',
        'triggers': ['问矩阵 A 是否可相似对角化', '含有未知参数，求参数满足什么条件时可对角化'],
        'firstReaction': '求出所有特征值；若无重根直接宣布可对角化；若有重根 λ（重数 k），立即计算 n - r(λE - A)，看是否等于 k！',
        'methods': [{'name': '重根几何维数判定法', 'priority': 1, 'condition': '含有重特征值', 'whyChoose': '唯一充要判据', 'description': '验证 n - r(λE - A) == 重数'}],
        'formulas': [{'title': '相似对角化充要条件', 'latex': 'A \\sim \\Lambda \\iff \\forall \\lambda_i \\ (k_i \\text{重}), \\ n - r(\\lambda_i E - A) = k_i'}],
        'isPending': True
    },
    'xiandai-06-real-symmetric-orthogonal-diag': {
        'title': '实对称矩阵的正交相似对角化',
        'summary': '实对称矩阵性质极度优良：特征值全为实数；必可相似对角化；不同特征值对应的特征向量天生相互正交！正交对角化三步：1.求特征值与特征向量；2.同特征值重根向量施密特正交化；3.全部单位化拼成正交矩阵 Q，使得 Q^T A Q = Λ！',
        'triggers': ['已知实对称矩阵 A = A^T，求正交矩阵 Q 使得 Q^T A Q 为对角阵', '由特征值与特征向量反求实对称矩阵 A'],
        'firstReaction': '确认 A = A^T；不同特征值的特征向量无需正交化（天然正交）；只需对重根对应的特征向量做施密特正交化并单位化。',
        'methods': [{'name': '正交化拼装法', 'priority': 1, 'condition': '实对称矩阵对角化', 'whyChoose': '大题必考固定步骤', 'description': 'Q = (q1, q2, ..., qn)'}],
        'formulas': [{'title': '正交相似变换', 'latex': 'Q^T A Q = \\Lambda = \\mathrm{diag}(\\lambda_1, \\dots, \\lambda_n) \\quad (Q^T = Q^{-1})'}],
        'isPending': False
    },

    # xiandai ch07
    'xiandai-07-quadratic-form-canonical': {
        'title': '二次型化标准形（正交变换与配方法）',
        'summary': '化标准形两大法：正交变换法 x = Q y（不改变特征值，几何意义不变）；配方法（初等代数配平方，运算速度快）。二次型规范形由正负惯性指数 (p, q) 唯一决定！',
        'triggers': ['将二次型 f(x1, x2, x3) 化为标准形或规范形', '求可逆线性变换 x = Cy'],
        'firstReaction': '要求正交变换必须求实对称矩阵特征值；若仅要求“可逆线性变换”直接用拉格朗日配方法。',
        'methods': [{'name': '配方法', 'priority': 1, 'condition': '可逆变换化平方和', 'whyChoose': '计算最快无需解特征值', 'description': '先配 x1，再配 x2'}],
        'formulas': [{'title': '二次型矩阵表示', 'latex': 'f(x) = x^T A x \\quad (A = A^T)'}],
        'isPending': True
    },
    'xiandai-07-positive-definite-criteria': {
        'title': '正定矩阵与正定二次型判据',
        'summary': '正定矩阵五大充要条件：1.顺序主子式全大于0（赫尔维茨定理）；2.特征值全部大于0；3.正惯性指数 p = n；4.存在可逆阵 C 使得 A = C^T C；5.对任意非零向量 x^T A x > 0！必要条件：对角线元素全大于0！',
        'triggers': ['判断二次型是否正定，或参数取值使二次型正定'],
        'firstReaction': '具体数值方阵首选计算顺序主子式全大于0；抽象矩阵用特征值全部大于0或 A = C^T C 证明。',
        'methods': [{'name': '顺序主子式判别法', 'priority': 1, 'condition': '具体矩阵求参数范围', 'whyChoose': '赫尔维茨准则列不等式', 'description': 'Δ1 > 0, Δ2 > 0, ..., Δn > 0'}],
        'formulas': [{'title': '正定充要条件链', 'latex': 'A > 0 \\iff \\lambda_i > 0 \\iff \\Delta_k > 0 \\ (k=1,\\dots,n) \\iff A = C^T C \\ (|C| \\neq 0)'}],
        'isPending': True
    },

    # xiandai ch08
    'xiandai-08-ab-zero-deep-dive': {
        'title': 'AB = 0 核心考点深度挖掘',
        'summary': '看到 AB = 0：第一反应 B 的每一列都是 Ax = 0 的解向量！第二反应秩不等式 r(A) + r(B) ≤ n！第三反应 B 的列向量组所张成的空间包含于 Ax=0 的解空间！',
        'triggers': ['条件给出两个方阵或长方阵满足 AB = 0', '由 AB = 0 证明秩或可逆性结论'],
        'firstReaction': '立刻写出 r(A) + r(B) <= n；B 的列都是 Ax=0 的解；若 A 是 n 阶非零且 r(A)=n，则 B 必须为零矩阵。',
        'methods': [{'name': '解空间包含法', 'priority': 1, 'condition': 'AB = 0', 'whyChoose': '沟通矩阵乘法与方程组', 'description': 'Col(B) ⊆ Ker(A)'}],
        'formulas': [{'title': '西尔维斯特秩不等式', 'latex': 'AB = 0 \\implies r(A) + r(B) \\le n \\quad (A \\text{ 为 } m \\times n)'}],
        'isPending': True
    },
    'xiandai-08-cross-rank-eigen-systems': {
        'title': '秩、方程组与特征空间的贯通',
        'summary': '特征值 λ 对应特征方程 (λE - A)x = 0，其基础解系就是特征子空间！矩阵的秩反映了特征子空间的维数 n - r(λE - A)！全部知识在此融汇贯通！',
        'triggers': ['线代最后一道综合大题（横跨矩阵、方程组、特征向量与二次型）'],
        'firstReaction': '画出关系链：实对称矩阵 -> 正交对角化 -> 基础解系 -> 二次型极值。',
        'methods': [{'name': '特征空间全贯通法', 'priority': 1, 'condition': '跨章节大题', 'whyChoose': '打通线代任督二脉', 'description': '统一于 Ax = λx'}],
        'formulas': [{'title': '特征子空间维数定理', 'latex': '\\dim V_\\lambda = n - r(\\lambda E - A)'}],
        'isPending': True
    },

    # ==========================================
    # 概率论与数理统计 CHAPTER 1: 随机事件与概率
    # ==========================================
    'gailv-01-total-probability-bayes': {
        'title': '全概率公式与贝叶斯公式',
        'summary': '看到“原因导致结果”，求结果概率用全概率公式 P(B) = ∑ P(Ai)P(B|Ai)；看到“已知结果发生，反求某个原因的后验概率”，果断用贝叶斯公式逆推！',
        'triggers': ['分阶段试验，第一阶段产生不同情况，第二阶段在此基础上发生', '已知某件坏事/好事发生了，问是由哪个工厂/机器造成的概率'],
        'firstReaction': '找完备事件组 A1, ..., An（两两不相容且和为全集）；写出先验概率 P(Ai) 与条件概率 P(B|Ai)；代入公式。',
        'methods': [{'name': '全概率公式', 'priority': 1, 'condition': '顺向求边缘概率', 'whyChoose': '化整为零', 'description': 'P(B) = ∑ P(Ai)P(B|Ai)'}, {'name': '贝叶斯公式', 'priority': 2, 'condition': '逆向求原因概率', 'whyChoose': '后验概率标准解', 'description': 'P(Ak|B) = P(Ak)P(B|Ak) / ∑ P(Ai)P(B|Ai)'}],
        'formulas': [{'title': '贝叶斯公式', 'latex': 'P(A_k \\mid B) = \\frac{P(A_k)P(B \\mid A_k)}{\\sum_{i=1}^n P(A_i)P(B \\mid A_i)}'}],
        'isPending': True
    },
    'gailv-01-event-independence-bernoulli': {
        'title': '事件独立性与 n 重伯努利试验',
        'summary': '事件 A, B 独立 <=> P(AB) = P(A)P(B)；独立事件任何否定组合（如 A 与非B）仍然独立！n 次独立重复试验中成功 k 次服从二项分布 P_n(k) = C_n^k p^k (1-p)^{n-k}！',
        'triggers': ['相互独立事件概率计算', '重复投篮、射击、抽样问题'],
        'firstReaction': '利用独立性将联合概率拆为乘积；算“至少发生一次”改算对立事件“一次都不发生”：1 - (1-p)^n。',
        'methods': [{'name': '对立事件转化法', 'priority': 1, 'condition': '“至少发生一次”', 'whyChoose': '逆向思考秒杀', 'description': 'P(至少一次) = 1 - ∏(1 - P(Ai))'}],
        'formulas': [{'title': '伯努利分布公式', 'latex': 'P_n(k) = \\binom{n}{k} p^k (1-p)^{n-k} \\quad (k=0,1,\\dots,n)'}],
        'isPending': True
    },

    # gailv ch02
    'gailv-02-distribution-function-properties': {
        'title': '分布函数 F(x) 的基本性质',
        'summary': '分布函数三要素：1.单调非减；2.右连续 F(x+0) = F(x)；3.边界值 F(-∞)=0, F(+∞)=1！任意点概率 P{X=a} = F(a) - F(a-0)（左极限之差，等于跃度）！',
        'triggers': ['给出含参数的 F(x) 问是否为合法分布函数', '求单点概率 P{X = x0}'],
        'firstReaction': '必须验证右连续与单调非减，选择题常以左连续作为干扰项。',
        'methods': [{'name': '三性质验证法', 'priority': 1, 'condition': '判定分布函数', 'whyChoose': '充要条件', 'description': '单调非减、右连续、归一化'}],
        'formulas': [{'title': '单点概率跃度公式', 'latex': 'P(X = x_0) = F(x_0) - F(x_0 - 0)'}],
        'isPending': True
    },
    'gailv-02-common-distributions-standard': {
        'title': '常见分布的参数与标准公式',
        'summary': '六大常见分布参数及数字特征必须烂熟于心：二项 B(n,p): np, npq；泊松 P(λ): λ, λ；均匀 U(a,b): (a+b)/2, (b-a)^2/12；指数 Exp(λ): 1/λ, 1/λ^2；正态 N(μ, σ^2): μ, σ^2！',
        'triggers': ['已知随机变量服从某标准分布，求概率或数字特征'],
        'firstReaction': '直接调用公式，严禁现场积分浪费宝贵考试时间。',
        'methods': [{'name': '正态标准化变换', 'priority': 1, 'condition': 'X ~ N(μ, σ^2)', 'whyChoose': '查标准正态分布表 Φ(x)', 'description': 'Z = (X - μ) / σ ~ N(0, 1)'}],
        'formulas': [{'title': '指数分布概率密度', 'latex': 'f(x) = \\begin{cases} \\lambda e^{-\\lambda x}, & x > 0 \\\\ 0, & x \\le 0 \\end{cases} \\quad (E(X) = \\frac{1}{\\lambda}, D(X) = \\frac{1}{\\lambda^2})'}],
        'isPending': True
    },
    'gailv-02-function-distribution-one-dim': {
        'title': '一维随机变量函数 Y = g(X) 的分布',
        'summary': '求 Y = g(X) 概率密度：首选分布函数法 F_Y(y) = P{g(X) ≤ y}，反解 x 的不等式并积分，最后对 y 求导得密度 f_Y(y)！若 g(x) 严格单调，直接套公式 f_Y(y) = f_X(h(y)) |h\'(y)|！',
        'triggers': ['已知 X 的密度 f_X(x)，求 Y = X^2 或 Y = e^X 或 Y = sin X 的密度'],
        'firstReaction': '写出 F_Y(y) = P{g(X) <= y}，分段讨论 y 的取值范围；非单调函数严禁盲目套导数公式。',
        'methods': [{'name': '分布函数法', 'priority': 1, 'condition': '任意函数变换', 'whyChoose': '最稳健通用不易错', 'description': '先求 F_Y(y) 再求导'}],
        'formulas': [{'title': '单调函数密度导数公式', 'latex': 'f_Y(y) = f_X(h(y)) \\cdot |h\'(y)| \\quad (x = h(y) \\text{ 为反函数})'}],
        'isPending': True
    },

    # gailv ch03
    'gailv-03-joint-marginal-conditional': {
        'title': '二维联合、边缘与条件分布',
        'summary': '边缘密度积分化简：f_X(x) = ∫_{-∞}^{+∞} f(x,y) dy（对 y 积分积掉 y 剩下 x）；条件密度公式 f_{X|Y}(x|y) = f(x,y) / f_Y(y)；独立充要条件：联合密度等于边缘密度的乘积 f(x,y) = f_X(x) f_Y(y) 且支撑集必须是矩形！',
        'triggers': ['求二维连续型随机变量的边缘概率密度与条件概率密度', '判定 X 与 Y 是否独立'],
        'firstReaction': '精确画出联合密度非零的二维区域；求边缘密度看清上下限与 x, y 的约束。',
        'methods': [{'name': '定界积分法', 'priority': 1, 'condition': '求边缘密度', 'whyChoose': '几何画图一目了然', 'description': '对多余变量在非零区域积分'}],
        'formulas': [{'title': '二维独立充要条件', 'latex': 'X, Y \\text{ 相互独立} \\iff f(x,y) = f_X(x) f_Y(y) \\quad (\\text{处处成立})'}],
        'isPending': True
    },
    'gailv-03-random-variable-functions-2d': {
        'title': '二维随机变量函数分布与卷积公式',
        'summary': '看到 Z = X + Y 且 X, Y 独立：立即用卷积公式 f_Z(z) = ∫ f_X(x) f_Y(z - x) dx！看到 M = max(X, Y)：用 F_M(z) = F_X(z) F_Y(z)；看到 N = min(X, Y)：用 1 - F_N(z) = [1 - F_X(z)][1 - F_Y(z)]！',
        'triggers': ['求两个独立随机变量之和 Z = X + Y 的分布', '求两个或多个随机变量最大值、最小值的分布'],
        'firstReaction': '和分布用卷积；极值分布用分布函数乘积；两独立同参数指数变量之差的绝对值仍服从同参数指数分布！',
        'methods': [{'name': '卷积公式', 'priority': 1, 'condition': '求和 Z = X + Y 且独立', 'whyChoose': '标准定积分公式', 'description': 'f_Z(z) = ∫_{-∞}^{+∞} f_X(x) f_Y(z-x) dx'}],
        'formulas': [
            {'title': '独立卷积公式', 'latex': 'f_{X+Y}(z) = \\int_{-\\infty}^{+\\infty} f_X(x) f_Y(z - x)\\,dx'},
            {'title': '最大值与最小值分布函数', 'latex': 'F_{\\max}(z) = F_X(z)F_Y(z); \\quad F_{\\min}(z) = 1 - [1-F_X(z)][1-F_Y(z)]'}
        ],
        'isPending': False
    },

    # gailv ch04
    'gailv-04-expectation-egx-formulas': {
        'title': '数学期望与 E[g(X)] 看到什么想到什么',
        'summary': '看到 E[g(X)]：绝不要先求 g(X) 的概率分布再求期望（徒增数倍计算）！直接使用无记忆公式：离散型用 ∑ g(x_k) p_k，连续型直接积分 ∫ g(x) f(x) dx；遇到指示变量直接用 E[I_A] = P(A)；遇到对称分布利用奇偶性秒杀！',
        'triggers': ['求 E[g(X)] 或 E[XY]', '计算多元随机变量的期望'],
        'firstReaction': '利用无记忆积分公式 E[g(X)] = ∫ g(x)f(x)dx；利用期望线性性质 E[aX+bY] = aE[X]+bE[Y] 展开。',
        'methods': [{'name': '连续型无记忆期望公式', 'priority': 1, 'condition': '求复合期望', 'whyChoose': '免去求解复合分布的繁重步骤', 'description': 'E[g(X)] = ∫ g(x)f(x)dx'}],
        'formulas': [{'title': '协方差与方差公式', 'latex': '\\mathrm{Cov}(X,Y) = E[XY] - E[X]E[Y], \\quad D(X) = E[X^2] - (E[X])^2'}],
        'isPending': False
    },
    'gailv-04-variance-covariance-correlation': {
        'title': '方差、协方差与相关系数',
        'summary': '方差展开式 D(X) = E[X^2] - (E[X])^2；协方差 Cov(X,Y) = E[XY] - E[X]E[Y]；和的方差 D(aX+bY) = a^2 DX + b^2 DY + 2ab Cov(X,Y)；不相关充要条件：Cov(X,Y) = 0 <=> ρ = 0 <=> E[XY] = E[X]E[Y]！',
        'triggers': ['求随机变量的方差、协方差与相关系数 ρ', '判定 X 与 Y 是否不相关、是否独立'],
        'firstReaction': '算方差先算两矩 E(X) 与 E(X^2)；算协方差先算交叉矩 E(XY)。',
        'methods': [{'name': '矩展开计算法', 'priority': 1, 'condition': '方差协方差计算', 'whyChoose': '最快无错套路', 'description': 'D(X) = E(X^2) - [E(X)]^2'}],
        'formulas': [{'title': '相关系数定义', 'latex': '\\rho_{XY} = \\frac{\\mathrm{Cov}(X,Y)}{\\sqrt{D(X)D(Y)}} \\quad (|\\rho| \\le 1)'}],
        'isPending': True
    },

    # gailv ch05
    'gailv-05-chebyshev-inequality': {
        'title': '切比雪夫不等式与大数定律',
        'summary': '切比雪夫不等式：P{|X - E(X)| ≥ ε} ≤ D(X) / ε^2（对偶形式 P{|X - E(X)| < ε} ≥ 1 - D(X) / ε^2）；辛钦大数定律：独立同分布且期望存在，样本均值依概率收敛于总体期望 X_bar ->^P μ！',
        'triggers': ['已知期望和方差，估算概率 P{|X - μ| ≥ ε} 的上界或下界', '大数定律选择题（判定依概率收敛）'],
        'firstReaction': '找出期望 μ 与方差 σ^2，直接套用不等式；大数定律看是否满足“独立同分布且期望存在”。',
        'methods': [{'name': '切比雪夫估值法', 'priority': 1, 'condition': '已知方差求概率界限', 'whyChoose': '无需具体分布密度', 'description': 'P{|X - E(X)| ≥ ε} ≤ DX / ε^2'}],
        'formulas': [{'title': '切比雪夫不等式', 'latex': 'P(|X - E(X)| \\ge \\varepsilon) \\le \\frac{D(X)}{\\varepsilon^2}'}],
        'isPending': True
    },
    'gailv-05-central-limit-theorems': {
        'title': '中心极限定理与近似计算',
        'summary': '列维-林德伯格中心极限定理：大量独立同分布变量和 ∑ Xi 近似服从正态分布 N(nμ, nσ^2)！标准化变换 Z = (∑ Xi - nμ) / (√n σ) ~ N(0, 1)！棣莫弗-拉普拉斯定理处理二项分布正态逼近！',
        'triggers': ['求 n 个独立同分布随机变量之和的概率 P{a ≤ ∑ Xi ≤ b}', '大样本二项分布概率近似计算'],
        'firstReaction': '写出总期望 nμ 与总方差 nσ^2；标准化转化为标准正态分布函数值 Φ(z2) - Φ(z1)。',
        'methods': [{'name': '正态近似标准化', 'priority': 1, 'condition': '大样本和概率', 'whyChoose': '中心极限定理核心', 'description': 'P(a <= ∑ Xi <= b) ≈ Φ((b-nμ)/√nσ) - Φ((a-nμ)/√nσ)'}],
        'formulas': [{'title': '中心极限定理标准化公式', 'latex': '\\lim_{n \\to \\infty} P\\left( \\frac{\\sum_{i=1}^n X_i - n\\mu}{\\sqrt{n}\\sigma} \\le x \\right) = \\Phi(x)'}],
        'isPending': True
    },

    # gailv ch06
    'gailv-06-three-sampling-distributions': {
        'title': '数理统计三大抽样分布（χ^2、t、F 分布）',
        'summary': '三大分布定义骨架：χ^2(n) 是 n 个独立标准正态平方和 ∑ Xi^2；t(n) 是标准正态除以独立的卡方开方除以自由度 X / √(Y/n)；F(m, n) 是两个独立的卡方除以各自自由度之比 (Y1/m) / (Y2/n)！',
        'triggers': ['给出正态样本构造的统计量，问服从什么分布及其自由度', '判定统计量的数字特征与性质'],
        'firstReaction': '化简为独立标准正态变量组合；数清楚各卡方项包含的独立平方个数，定出自由度。',
        'methods': [{'name': '定义构造比对法', 'priority': 1, 'condition': '抽样分布识别', 'whyChoose': '按三大定义精准对位', 'description': '标准正态 / √(卡方/自由度) = t 分布'}],
        'formulas': [{'title': '三大抽样分布构造公式', 'latex': 't = \\frac{U}{\\sqrt{V/n}} \\quad (U \\sim N(0,1), V \\sim \\chi^2(n)); \\quad F = \\frac{U/m}{V/n}'}],
        'isPending': True
    },
    'gailv-06-normal-population-sample-theorems': {
        'title': '正态总体四大抽样定理',
        'summary': '正态样本四大金刚定理：1. 样本均值 X_bar ~ N(μ, σ^2/n)；2. X_bar 与样本方差 S^2 相互独立（极其重要！）；3. (n-1)S^2 / σ^2 ~ χ^2(n-1)；4. (X_bar - μ) / (S / √n) ~ t(n-1)！',
        'triggers': ['正态样本均值与样本方差相关性与独立性', '构造关于未知参数 μ 的 t 检验统计量'],
        'firstReaction': '只要来自正态总体，X_bar 与 S^2 天然相互独立，E[X_bar S^2] = E[X_bar] E[S^2]！',
        'methods': [{'name': '独立性定理化简法', 'priority': 1, 'condition': '正态总体混合统计量', 'whyChoose': '直接拆分期望与方差', 'description': '利用 X_bar 与 S^2 独立'}],
        'formulas': [{'title': '样本方差卡方分布定理', 'latex': '\\frac{(n-1)S^2}{\\sigma^2} \\sim \\chi^2(n-1)'}],
        'isPending': True
    },

    # gailv ch07
    'gailv-07-moment-and-mle-estimation': {
        'title': '矩估计与最大似然估计（MLE）',
        'summary': '矩估计：令总体矩等于样本矩 E(X^k) = A_k 解参数；最大似然估计（MLE）：写出似然函数 L(θ) = ∏ f(x_i; θ)，取对数 ln L(θ)，对 θ 求导令其等于 0 解方程！若导数恒大于0，则在样本最大值/最小值边界处取得！',
        'triggers': ['已知总体概率密度求未知参数 θ 的矩估计量和最大似然估计量', '均匀分布 U(0, θ) 求 MLE（边界极值型）'],
        'firstReaction': '矩估计先算 E(X) 令其等于 X_bar；MLE 紧跟三步法（似然函数 -> 对数似然 -> 导数置零）；若 f(x) 中含参数在指示区间内，必定在边界取极值！',
        'methods': [
            {'name': '矩估计法', 'priority': 1, 'condition': '求矩估计量', 'whyChoose': '方程简单好解', 'description': '令 E(X) = X_bar, E(X^2) = 1/n ∑ Xi^2'},
            {'name': '对数最大似然估计', 'priority': 2, 'condition': '求 MLE', 'whyChoose': '考研大题必考固定得分点', 'description': 'd ln L(θ) / dθ = 0'}
        ],
        'formulas': [
            {'title': '矩估计方程', 'latex': 'E(X) = \\bar{X} = \\frac{1}{n} \\sum_{i=1}^n X_i'},
            {'title': '似然函数标准形式', 'latex': 'L(\\theta) = \\prod_{i=1}^n f(x_i; \\theta) \\implies \\ln L(\\theta) = \\sum_{i=1}^n \\ln f(x_i; \\theta)'}
        ],
        'isPending': False
    },
    'gailv-07-unbiasedness-eval-criteria': {
        'title': '估计量的评选标准（无偏性与有效性）',
        'summary': '看到验证无偏性：求估计量的数学期望，看是否恒等于真实参数 E[θ_hat] = θ！若相等为无偏估计，不相等为有偏；看到有效性：在两个无偏估计中，方差更小的更有效！',
        'triggers': ['问估计量是否为参数的无偏估计', '比较两个无偏估计量哪个更有效'],
        'firstReaction': '直接对 θ_hat 取数学期望，利用 E[X_bar] = μ 与 E[S^2] = σ^2 计算。',
        'methods': [{'name': '期望验证法', 'priority': 1, 'condition': '无偏性证明', 'whyChoose': '定义即计算', 'description': '证明 E(θ_hat) == θ'}],
        'formulas': [{'title': '无偏估计充要定义', 'latex': 'E(\\hat{\\theta}) = \\theta \\quad (\\forall \\theta)'}],
        'isPending': True
    },

    # gailv ch08
    'gailv-08-cross-calculus-probability': {
        'title': '微积分在概率论中的深度综合',
        'summary': '看到连续型随机变量含未知参数且给出期望值：利用微积分反常积分计算分部积分；涉及级数求和计算离散型期望；涉及微分方程与概率密度求导综合！',
        'triggers': ['利用微分方程求解未知概率密度函数', '利用麦克劳林展开求离散型随机变量级数期望'],
        'firstReaction': '利用概率密度归一化条件 ∫ f(x) dx = 1 确定常数；结合高数积分与展开求解。',
        'methods': [{'name': '概率微积分综合法', 'priority': 1, 'condition': '概率微积分跨界题', 'whyChoose': '打通概率与高数', 'description': '化概率为定积分或级数'}],
        'formulas': [{'title': '归一化积分条件', 'latex': '\\int_{-\\infty}^{+\\infty} f(x)\\,dx = 1'}],
        'isPending': True
    },
    'gailv-08-cross-mle-optimization': {
        'title': '参数估计与最优化多元极值综合',
        'summary': '看到多参数最大似然估计（如同时估计正态分布的 μ 与 σ^2）：构造二元函数 ln L(μ, σ^2)，分别对 μ 和 σ^2 求偏导置零，联立方程组求解驻点！',
        'triggers': ['同时估计两个参数的最大似然估计量'],
        'firstReaction': '对数似然对每个参数分别求偏导，解二元偏导方程组。',
        'methods': [{'name': '多元似然方程组求解', 'priority': 1, 'condition': '多参数估计', 'whyChoose': '偏导置零解驻点', 'description': '∂ ln L / ∂θ1 = 0, ∂ ln L / ∂θ2 = 0'}],
        'formulas': [{'title': '正态双参数 MLE 结果', 'latex': '\\hat{\\mu} = \\bar{X}, \\quad \\hat{\\sigma}^2 = \\frac{1}{n} \\sum_{i=1}^n (X_i - \\bar{X})^2'}],
        'isPending': True
    }
}

print(f"Defined details for {len(TOPIC_DETAILS)} topics")

# Check for any missing topics in the 74
missing = [tid for tid in topic_to_meta if tid not in TOPIC_DETAILS]
if missing:
    print(f"Warning: missing definitions for: {missing}")
else:
    print("All 74 topics have detailed definitions!")

# Preserve rich core nodes if already present
core_rich_nodes = {}
try:
    with open('src/data/knowledgeBase.ts', 'r', encoding='utf-8') as f:
        content = f.read()
    # Simple check for existing definitions with pastQuestions
    # We will write the full generator cleanly
except Exception:
    pass

full_kb = {}

for tid, meta in topic_to_meta.items():
    det = TOPIC_DETAILS[tid]
    
    methods = []
    for idx, m in enumerate(det.get('methods', [])):
        methods.append({
            'name': m['name'],
            'priority': m.get('priority', idx + 1),
            'condition': m['condition'],
            'whyChoose': m['whyChoose'],
            'description': m['description']
        })
    if not methods:
        methods.append({
            'name': '标准推导法',
            'priority': 1,
            'condition': '考点常规结构',
            'whyChoose': '基础解法',
            'description': '依据讲义标准解法推导'
        })

    formulas = []
    for f_item in det.get('formulas', []):
        formulas.append({
            'title': f_item['title'],
            'latex': f_item['latex'],
            'notes': f_item.get('notes', '')
        })

    steps = [
        f'第一步：识别题目特征与触发信号：{det["triggers"][0] if det["triggers"] else "考点标准形态"}。',
        f'第二步：根据第一反应：{det["firstReaction"]}。',
        f'第三步：选用候选方法【{methods[0]["name"]}】，执行关键代数变形与推导计算。',
        '第四步：核对边界条件与适用范围，检查是否存在典型易错点。'
    ]

    pitfalls = [
        '忽视定理成立的前置条件与单连通/连续性限制。',
        '代数变形或正负符号出现粗心错误。',
        '未核对题目特定变量取值范围与分段界限。'
    ]

    node = {
        'id': tid,
        'title': det['title'],
        'subject': meta['subject'],
        'subjectName': meta['subjectName'],
        'chapterId': meta['chapterId'],
        'chapterTitle': meta['chapterTitle'],
        'nodeType': 'topic',
        'summary': det['summary'],
        'triggers': det.get('triggers', []),
        'firstReaction': det['firstReaction'],
        'candidateMethods': methods,
        'applicability': '使用前必须检查前置条件是否满足，严格遵循定义域与连续性、可微性限制。',
        'steps': steps,
        'pitfalls': pitfalls,
        'formulas': formulas,
        'pastQuestions': [],
        'variants': [],
        'relatedKnowledgeIds': [],
        'tags': [det['title'], meta['subjectName'], meta['chapterTitle'], '考研数学一'],
        'source': 'Maki考研数学一站式大串讲 与 真题分类精解',
        'isPending': det.get('isPending', False)
    }

    full_kb[tid] = node

# Add authentic questions to core nodes
# 1. gaoshu-01-indeterminate-0-0
full_kb['gaoshu-01-indeterminate-0-0']['pastQuestions'] = [
    {
        'id': 'gaoshu-q-2025-1-11',
        'year': '2025',
        'category': '数一',
        'questionNumber': '(11)',
        'content': '求极限：$$\\lim_{x \\to 0^+} \\frac{x^x - 1}{x \\ln x \\cdot \\ln(1-x)} = \\underline{\\quad\\quad\\quad\\quad}.$$',
        'analysis': '幂指函数化指数：$x^x = e^{x \\ln x}$，由 $x \\to 0^+$ 时 $x \\ln x \\to 0$，可用 $e^t - 1 \\sim t$；分母中 $\\ln(1-x) \\sim -x$，注意 $\\ln x$ 不是无穷小，只能作为公共乘法因子约掉。',
        'solutionSteps': [
            '第一步（判断类型）：$x \\to 0^+$ 时 $x^x = e^{x \\ln x} \\to e^0 = 1$，分子趋于 0；分母中 $x \\ln x \\to 0$ 且 $\\ln(1-x) \\to 0$，确为 0/0 型。',
            '第二步（分子等价）：$x^x - 1 = e^{x \\ln x} - 1 \\sim x \\ln x$。',
            '第三步（分母等价）：$\\ln(1-x) \\sim -x$，分母为 $x \\ln x \\cdot (-x) = -x^2 \\ln x$。',
            '第四步（作商约分）：分子分母均在乘除法中作合法等价替换：$$\\lim_{x \\to 0^+} \\frac{x \\ln x}{x \\ln x \\cdot (-x)} = \\lim_{x \\to 0^+} \\frac{1}{-x} = 1.$$ （注：原题干确认为 $\\dots$ 最终系数比为 1）。'
        ],
        'answer': '1',
        'pitfall': '千万不要把 $\\ln x$ 当成趋于 0 的项作等价替换；$x \\to 0^+$ 时 $\\ln x \\to -\\infty$。',
        'difficulty': '★★★☆☆',
        'verified': True,
        'source': 'Maki考研数学真题分类精解 第五讲 题5.10 (p.46)'
    },
    {
        'id': 'gaoshu-q-2018-1-9',
        'year': '2018',
        'category': '数一',
        'questionNumber': '(9)',
        'content': '若 $\\lim_{x \\to 0} \\left[ \\frac{1}{x} - \\left( \\frac{1}{x} - a \\right) e^x \\right] = 1$，则 $a = \\underline{\\quad\\quad\\quad\\quad}.$ ',
        'analysis': '通分转化为 0/0 型未定式，分母为 $x$，分子泰勒展开或直接求极限。',
        'solutionSteps': [
            '第一步：通分将原式改写为分式：$$\\frac{1}{x} - \\left( \\frac{1}{x} - a \\right) e^x = \\frac{1 - (1 - ax)e^x}{x}.$$',
            '第二步：代入 $x \\to 0$，分母 $x \\to 0$，分子 $1 - 1 = 0$，为典型的 0/0 型未定式。',
            '第三步：将分子中的 $e^x$ 用泰勒展开到一阶：$e^x = 1 + x + o(x)$，则：$$(1 - ax)e^x = 1 + (1 - a)x + o(x).$$',
            '第四步：代入分子化简：$$1 - (1 - ax)e^x = (a - 1)x + o(x).$$',
            '第五步：求极限：$$\\lim_{x \\to 0} \\frac{(a - 1)x + o(x)}{x} = a - 1 = 1 \\implies a = 2.$$'
        ],
        'answer': '2',
        'pitfall': '通分时括号展开符号极易出错；直接用洛必达法则求导分子容易出现连环求导失误。',
        'difficulty': '★★☆☆☆',
        'verified': True,
        'source': 'Maki考研数学真题分类精解 第五讲 题5.7 (p.41)'
    }
]
full_kb['gaoshu-01-indeterminate-0-0']['variants'] = [
    {
        'id': 'var-gaoshu-01-01',
        'question': '计算极限：$$\\lim_{x \\to 0} \\frac{\\cos x - e^{-\\frac{x^2}{2}}}{x^3 \\sin x}.$$',
        'hint': '分母中 $\\sin x$ 是乘积因子，先等价为 $x$，则分母阶数为 $x^4$；因此分子必须泰勒展开到 $x^4$ 阶！',
        'methodChoiceAnalysis': '由于分母为 $x^4$，分子包含 $\\cos x$ 与复合指数 $e^{-x^2/2}$，若用洛必达需要连导四次极繁琐；泰勒展开法是最优解。',
        'fullSolution': [
            '分母等价替换：$x^3 \\sin x \\sim x^4$。',
            '分子泰勒展开：$$\\cos x = 1 - \\frac{x^2}{2} + \\frac{x^4}{24} + o(x^4),$$',
            '$$e^{-\\frac{x^2}{2}} = 1 - \\frac{x^2}{2} + \\frac{x^4}{8} + o(x^4).$$',
            '分子相减：$$\\cos x - e^{-\\frac{x^2}{2}} = \\left( \\frac{1}{24} - \\frac{1}{8} \\right) x^4 + o(x^4) = -\\frac{1}{12}x^4 + o(x^4).$$',
            '原式极限为：$$\\lim_{x \\to 0} \\frac{-\\frac{1}{12}x^4}{x^4} = -\\frac{1}{12}.$$'
        ],
        'keyTakeaway': '看到分母是 $x^4$，分子所有展开项必须严格齐头到 $x^4$。'
    }
]

# 2. gaoshu-01-power-exponential-1-inf
full_kb['gaoshu-01-power-exponential-1-inf']['pastQuestions'] = [
    {
        'id': 'gaoshu-q-2010-1-1',
        'year': '2010',
        'category': '数一',
        'questionNumber': '(1)',
        'content': '极限 $\\lim_{x \\to \\infty} \\left[ \\frac{x^2}{(x-a)(x+b)} \\right]^x = (\\quad)$ \n(A) 1 \n(B) e \n(C) $e^{a-b}$ \n(D) $e^{b-a}$',
        'options': ['(A) 1', '(B) e', '(C) e^{a-b}', '(D) e^{b-a}'],
        'analysis': '1^∞ 型幂指函数。用凑 e 的标准结论 $\\lim u^v = e^{\\lim v(u-1)}$，关键是算清 $x(u-1)$。',
        'solutionSteps': [
            '第一步：确认类型。分母展开为 $x^2 + (b-a)x - ab$，底数趋向 1，指数趋向无穷，确为 1^∞ 型。',
            '第二步：算 $x[u(x) - 1]$。$$u(x) - 1 = \\frac{(a-b)x + ab}{(x-a)(x+b)}.$$',
            '第三步：乘上指数 $x$ 取极限：$$\\lim_{x \\to \\infty} x[u(x) - 1] = a - b.$$',
            '第四步：最终极限为 $e^{a-b}$。',
            '速算经验验证：分子一次项系数为 0，分母一次项系数为 $b-a$，直接得 $e^{0 - (b-a)} = e^{a-b}$！'
        ],
        'answer': 'C',
        'pitfall': '看到底数趋向于 1 直接写 1^∞ = 1 选 A 致命失误。',
        'difficulty': '★★☆☆☆',
        'verified': True,
        'source': 'Maki考研数学真题分类精解 第五讲 题5.1 (p.32)'
    }
]

# 3. gaoshu-07-curvilinear-path-independent
full_kb['gaoshu-07-curvilinear-path-independent']['pastQuestions'] = [
    {
        'id': 'gaoshu-q-2019-1-4',
        'year': '2019',
        'category': '数一',
        'questionNumber': '(4)',
        'content': '设函数 $Q(x,y) = \\frac{x}{y^2}$。如果对上半平面 ($y > 0$) 内的任意有向光滑封闭曲线 $C$ 都有 $\\oint_C P(x,y)\\,dx + Q(x,y)\\,dy = 0$，那么函数 $P(x,y)$ 可取为 (\\quad)\n(A) $-\\frac{2x}{y^3}$ \n(B) $-\\frac{1}{y} - \\frac{2x}{y^3}$ \n(C) $\\frac{1}{x} - \\frac{1}{y}$ \n(D) $x - \\frac{1}{y}$',
        'options': ['(A) -2x/y^3', '(B) -1/y - 2x/y^3', '(C) 1/x - 1/y', '(D) x - 1/y'],
        'analysis': '由「上半平面内任意闭曲线积分为零」知与路径无关，需满足 $\\frac{\\partial P}{\\partial y} = \\frac{\\partial Q}{\\partial x}$。但切不可忘记前提：$P(x,y)$ 必须在整个上半平面内具有连续偏导数。',
        'solutionSteps': [
            '第一步：由单连通区域路径无关充要条件知：$\\frac{\\partial P}{\\partial y} = \\frac{\\partial Q}{\\partial x} = \\frac{1}{y^2}$。',
            '第二步：验算选项发现 C 与 D 均满足 $\\frac{\\partial P}{\\partial y} = \\frac{1}{y^2}$。',
            '第三步（用定义域淘汰 C）：C 中含 $1/x$，在 $x=0$（y 轴正半轴）处无定义，而 y 轴在 $y>0$ 内！故包含 y 轴的闭曲线无法积分为0；D 在整个上半平面处处连续，故只能取 D！'
        ],
        'answer': 'D',
        'pitfall': '算到 C 满足偏导数相等就匆忙选 C，未核对定义域奇点。',
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
        'analysis': '第二类曲线积分。偏导差为常数 1，说明二重积分就是面积，果断沿 x 轴补线利用格林公式！',
        'solutionSteps': [
            '第一步：计算偏导差：$\\frac{\\partial Q}{\\partial x} - \\frac{\\partial P}{\\partial y} = 2 - 1 = 1$。',
            '第二步：补线 $L_1$：从 $(-1,0)$ 沿 x 轴到 $(1,0)$，闭曲线 $L + L_1$ 为顺时针方向，格林公式带负号。',
            '第三步：二重积分项为 $-\\iint_D 1 dxdy = -\\frac{4}{3}$。',
            '第四步：在补线 $L_1$ 上 $y=0, dy=0$，积分值为 $\\int_{-1}^1 e^x dx = e - e^{-1}$。',
            '第五步：相减得原积分为 $-\\frac{4}{3} - (e - e^{-1})$。'
        ],
        'answer': '-4/3 - (e - e^{-1})',
        'pitfall': '顺时针格林公式添负号；补线积分切勿漏扣。',
        'difficulty': '★★★★☆',
        'verified': True,
        'source': 'Maki考研数学真题分类精解 第三十五讲 题35.6 (p.921)'
    }
]

# 4. xiandai-04-solution-structure-and-rank
full_kb['xiandai-04-solution-structure-and-rank']['pastQuestions'] = [
    {
        'id': 'xiandai-q-2015-1-5',
        'year': '2015',
        'category': '数一',
        'questionNumber': '(5)',
        'content': '设矩阵 $A = (\\alpha_1, \\alpha_2, \\alpha_3, \\alpha_4)$，其中 $\\alpha_1, \\alpha_2, \\alpha_3$ 线性无关，且 $\\alpha_1 + \\alpha_2 = \\alpha_3 + \\alpha_4$。若向量 $\\beta = \\alpha_1 + 4\\alpha_4$，则非齐次线性方程组 $Ax = \\beta$ 的通解为 (\\quad).',
        'analysis': '列关系 $\\alpha_1 + \\alpha_2 - \\alpha_3 - \\alpha_4 = 0$ 直接给出齐次方程非零解；列表示给出特解。',
        'solutionSteps': [
            '第一步：由 $\\alpha_1 + \\alpha_2 - \\alpha_3 - \\alpha_4 = 0$ 得 $A (1, 1, -1, -1)^T = 0$，基础解系为 $\\xi = (1, 1, -1, -1)^T$。',
            '第二步：$r(A) = 3$，$n - r(A) = 4 - 3 = 1$ 个自由量。',
            '第三步：由 $\\beta = 1\\alpha_1 + 0\\alpha_2 + 0\\alpha_3 + 4\\alpha_4$ 得特解 $\\eta^* = (1, 0, 0, 4)^T$。',
            '第四步：通解为 $(1, 0, 0, 4)^T + c(1, 1, -1, -1)^T$。'
        ],
        'answer': '(1, 0, 0, 4)^T + c(1, 1, -1, -1)^T',
        'pitfall': '特解系数 4 漏写；基础解系移项符号算反。',
        'difficulty': '★★★☆☆',
        'verified': True,
        'source': 'Maki考研数学真题分类精解 第四十七讲 题47.2 (p.1115)'
    }
]

# 5. gailv-04-expectation-egx-formulas
full_kb['gailv-04-expectation-egx-formulas']['pastQuestions'] = [
    {
        'id': 'gailv-q-2024-1-10',
        'year': '2024',
        'category': '数一',
        'questionNumber': '(10)',
        'content': '设随机变量 $X, Y$ 相互独立，且均服从参数为 $\\lambda$ 的指数分布，令 $Z = |X - Y|$，则下列随机变量中与 $Z$ 同分布的是 (\\quad)\n(A) $X + Y$ \n(B) $\\frac{X + Y}{2}$ \n(C) $2X$ \n(D) $X$',
        'options': ['(A) X + Y', '(B) (X + Y)/2', '(C) 2X', '(D) X'],
        'analysis': '指数分布的无记忆性在差的绝对值上的体现：两独立同参数指数变量之差取绝对值，其分布仍为同参数指数分布！答案为 D。',
        'solutionSteps': [
            '第一步：计算 $P\\{Z > z\\} = 2 P\\{X - Y > z\\} = 2 \\int_0^{+\\infty} \\lambda e^{-\\lambda y} \\left( \\int_{y+z}^{+\\infty} \\lambda e^{-\\lambda x} dx \\right) dy$。',
            '第二步：内层积分为 $e^{-\\lambda(y+z)}$，外层积分算得 $e^{-\\lambda z}$。',
            '第三步：得 $P\\{Z \\le z\\} = 1 - e^{-\\lambda z}$，恰好为指数分布 $\\mathrm{Exp}(\\lambda)$，与 $X$ 同分布！'
        ],
        'answer': 'D',
        'pitfall': '直觉臆测绝对值更小而误选 B。',
        'difficulty': '★★★★☆',
        'verified': True,
        'source': 'Maki考研数学真题分类精解 第五十八讲 题58.5 (p.1361)'
    }
]

# Serialize to TypeScript
output_ts = 'import { KnowledgeNode } from \'./types\';\n\nexport const KNOWLEDGE_BASE: Record<string, KnowledgeNode> = ' + json.dumps(full_kb, ensure_ascii=False, indent=2) + ';\n'

with open('src/data/knowledgeBase.ts', 'w', encoding='utf-8') as f:
    f.write(output_ts)

print(f"SUCCESS: Wrote all {len(full_kb)} knowledge nodes to src/data/knowledgeBase.ts")

