import { SubjectInfo, ChapterInfo } from './types';

export const SUBJECTS: Record<string, SubjectInfo> = {
  gaoshu: {
    id: 'gaoshu',
    name: '高等数学',
    shortName: '高数',
    description: '考研数学一分值占比最高（约56%），涵盖微积分、微分方程、多元微积分、级数与空间几何。',
    color: {
      primary: '#0284c7', // sky-600
      light: '#f0f9ff',   // sky-50
      border: '#7dd3fc',  // sky-300
      text: '#0369a1',    // sky-700
      badge: 'bg-sky-100 text-sky-800 border-sky-300',
    },
    chapterIds: [
      'gaoshu-ch01',
      'gaoshu-ch02',
      'gaoshu-ch03',
      'gaoshu-ch04',
      'gaoshu-ch05',
      'gaoshu-ch06',
      'gaoshu-ch07',
      'gaoshu-ch08',
      'gaoshu-ch09',
      'gaoshu-ch10',
    ],
  },
  xiandai: {
    id: 'xiandai',
    name: '线性代数',
    shortName: '线代',
    description: '考研数学一核心支柱（约22%），结构严密、环环相扣，从矩阵/向量深入至特征空间与二次型。',
    color: {
      primary: '#7c3aed', // violet-600
      light: '#f5f3ff',   // violet-50
      border: '#c4b5fd',  // violet-300
      text: '#6d28d9',    // violet-700
      badge: 'bg-violet-100 text-violet-800 border-violet-300',
    },
    chapterIds: [
      'xiandai-ch01',
      'xiandai-ch02',
      'xiandai-ch03',
      'xiandai-ch04',
      'xiandai-ch05',
      'xiandai-ch06',
      'xiandai-ch07',
      'xiandai-ch08',
    ],
  },
  gailv: {
    id: 'gailv',
    name: '概率论与数理统计',
    shortName: '概率',
    description: '考研数学一重要组成（约22%），强调模型抽象、分布函数推导、数字特征计算与统计推断。',
    color: {
      primary: '#059669', // emerald-600
      light: '#ecfdf5',   // emerald-50
      border: '#6ee7b7',  // emerald-300
      text: '#047857',    // emerald-700
      badge: 'bg-emerald-100 text-emerald-800 border-emerald-300',
    },
    chapterIds: [
      'gailv-ch01',
      'gailv-ch02',
      'gailv-ch03',
      'gailv-ch04',
      'gailv-ch05',
      'gailv-ch06',
      'gailv-ch07',
      'gailv-ch08',
    ],
  },
};

export const CHAPTERS: Record<string, ChapterInfo> = {
  // 高等数学 (10章)
  'gaoshu-ch01': {
    id: 'gaoshu-ch01',
    subjectId: 'gaoshu',
    title: '函数、极限与连续',
    order: 1,
    description: '极限与未定式计算是高数基石，重点突破七大未定式、等价替换、泰勒展开与递推数列极限。',
    goals: [
      '熟练识别 0/0、1^∞、∞-∞ 等未定式并秒出对应化简路线',
      '牢记常用等价无穷小及其适用边界（仅乘除因式可替）',
      '掌握单调有界准则与夹逼准则证明数列极限',
      '准确判定函数的间断点类型与连续性'
    ],
    topicIds: [
      'gaoshu-01-indeterminate-0-0',
      'gaoshu-01-power-exponential-1-inf',
      'gaoshu-01-difference-inf-inf',
      'gaoshu-01-infinitesimal-order',
      'gaoshu-01-sequence-monotone-bounded',
      'gaoshu-01-discontinuity-points'
    ]
  },
  'gaoshu-ch02': {
    id: 'gaoshu-ch02',
    subjectId: 'gaoshu',
    title: '一元函数微分学',
    order: 2,
    description: '导数定义、求导技术、微分中值定理（罗尔/拉格朗日/柯西/泰勒）及不等式证明与单调极值凹凸性。',
    goals: [
      '掌握绝对值函数、分段函数在分界点的可导性定义判定',
      '熟练运用高阶导数莱布尼茨公式与参数方程求导',
      '熟练构造辅助函数证明中值定理与方程根的个数',
      '熟练运用导数研究函数极值、最值与拐点曲率'
    ],
    topicIds: [
      'gaoshu-02-derivative-definition',
      'gaoshu-02-higher-order-leibniz',
      'gaoshu-02-mean-value-theorems',
      'gaoshu-02-taylor-formula-proof',
      'gaoshu-02-inequality-and-roots'
    ]
  },
  'gaoshu-ch03': {
    id: 'gaoshu-ch03',
    subjectId: 'gaoshu',
    title: '一元函数积分学',
    order: 3,
    description: '不定积分换元分部、定积分性质与变限积分求导求极值、反常积分审敛与几何物理应用。',
    goals: [
      '秒识凑微分与分部积分的优先级，掌握有理函数拆项',
      '熟练处理变上限积分求导（含变量在上下限及被积函数内部）',
      '熟练运用对称性与区间再现公式化简定积分',
      '掌握旋转体体积、表面积及反常积分 p-判别法'
    ],
    topicIds: [
      'gaoshu-03-variable-limit-integral',
      'gaoshu-03-definite-integral-symmetry',
      'gaoshu-03-improper-integral-convergence',
      'gaoshu-03-geometric-applications'
    ]
  },
  'gaoshu-ch04': {
    id: 'gaoshu-ch04',
    subjectId: 'gaoshu',
    title: '微分方程',
    order: 4,
    description: '一阶可分离/齐次/线性方程、二阶常系数线性方程、可降阶方程与欧拉方程及实际应用建模。',
    goals: [
      '熟练应用一阶线性方程常数变易公式与伯努利变换',
      '熟练通过特征方程写出齐次通解，并设出非齐次特解形式',
      '熟练掌握三种可降阶微分方程的降阶手法',
      '掌握欧拉方程自变量代换法与几何应用建模'
    ],
    topicIds: [
      'gaoshu-04-first-order-ode',
      'gaoshu-04-second-order-constant-coeff',
      'gaoshu-04-reducible-ode',
      'gaoshu-04-euler-equation'
    ]
  },
  'gaoshu-ch05': {
    id: 'gaoshu-ch05',
    subjectId: 'gaoshu',
    title: '多元函数微分学',
    order: 5,
    description: '极限连续偏导全微分四者关系、复合函数与隐函数链式法则、无条件极值与拉格朗日乘数法。',
    goals: [
      '透彻理解多元连续、可偏导、可微与偏导连续的充分必要关系',
      '熟练运用链式法则与矩阵形式求多元复合高阶偏导',
      '熟练运用隐函数存在定理求偏导与全微分',
      '掌握海森矩阵判定无条件极值与拉格朗日乘数法'
    ],
    topicIds: [
      'gaoshu-05-differentiability-concept',
      'gaoshu-05-chain-rule-composite',
      'gaoshu-05-implicit-function-differentiation',
      'gaoshu-05-lagrange-multipliers'
    ]
  },
  'gaoshu-ch06': {
    id: 'gaoshu-ch06',
    subjectId: 'gaoshu',
    title: '二重积分与多重积分',
    order: 6,
    description: '直角坐标与极坐标二重积分、对称性与奇偶性奇偶化简、三重积分直角/柱面/球坐标计算。',
    goals: [
      '根据积分区域边界与被积函数结构择优选择极坐标或直角坐标',
      '充分利用普通对称性与轮换对称性简化积分',
      '掌握交换二重积分次序的标准画图定界法',
      '熟练掌握三重积分截面法与球面/柱面坐标计算'
    ],
    topicIds: [
      'gaoshu-06-double-integral-polar',
      'gaoshu-06-order-exchange-symmetry',
      'gaoshu-06-triple-integral-coordinates'
    ]
  },
  'gaoshu-ch07': {
    id: 'gaoshu-ch07',
    subjectId: 'gaoshu',
    title: '曲线积分与曲面积分',
    order: 7,
    description: '第一/二类曲线与曲面积分、格林公式、高斯公式、斯托克斯公式、散度与旋度、路径无关。',
    goals: [
      '秒辨四类线面积分物理背景与计算公式投影法',
      '深刻理解格林公式的单连通条件与奇点挖洞补线法',
      '掌握路径无关的四条等价判据与势函数原函数法',
      '熟练应用高斯公式计算闭曲面积分及斯托克斯公式'
    ],
    topicIds: [
      'gaoshu-07-curvilinear-path-independent',
      'gaoshu-07-green-formula-hole-technique',
      'gaoshu-07-gauss-divergence-theorem',
      'gaoshu-07-stokes-theorem-curl'
    ]
  },
  'gaoshu-ch08': {
    id: 'gaoshu-ch08',
    subjectId: 'gaoshu',
    title: '无穷级数',
    order: 8,
    description: '常数项级数正项/交错审敛法、幂级数收敛半径与区间、幂级数逐项求导积分求和与麦克劳林展开、傅里叶级数。',
    goals: [
      '熟练运用比值法、根值法、比较判别法与莱布尼茨判别法',
      '牢记标准幂级数和函数（ln, exp, sin, cos, arctan等）',
      '熟练使用先导后积或先积后导转化求幂级数和函数',
      '掌握傅里叶系数公式与狄利克雷收敛定理'
    ],
    topicIds: [
      'gaoshu-08-series-convergence-tests',
      'gaoshu-08-power-series-radius-interval',
      'gaoshu-08-power-series-summation',
      'gaoshu-08-fourier-series-dirichlet'
    ]
  },
  'gaoshu-ch09': {
    id: 'gaoshu-ch09',
    subjectId: 'gaoshu',
    title: '向量代数与空间解析几何',
    order: 9,
    description: '向量数量积向量积混合积、平面与直线方程、点面距离与线面夹角、常见二次曲面与空间曲线投影。',
    goals: [
      '熟练用点积判垂直、叉积判平行与法向量构建',
      '掌握点到平面与点到直线的距离公式',
      '熟练求解投影曲线柱面与母线平行方程',
      '掌握旋转曲面方程建立法则'
    ],
    topicIds: [
      'gaoshu-09-vector-products-geometry',
      'gaoshu-09-plane-and-line-equations',
      'gaoshu-09-surfaces-and-projections'
    ]
  },
  'gaoshu-ch10': {
    id: 'gaoshu-ch10',
    subjectId: 'gaoshu',
    title: '综合题与跨章节方法',
    order: 10,
    description: '极限与积分综合题、微分方程与级数综合、积分与微分中值综合构造、多元与极值综合问题。',
    goals: [
      '打通微积分各章节之间的桥梁，形成综合解题反应',
      '识别含变限积分的微分方程初值问题解法',
      '综合利用泰勒展开与积分估值完成复杂分析证明'
    ],
    topicIds: [
      'gaoshu-10-cross-ode-integral',
      'gaoshu-10-cross-taylor-proofs'
    ]
  },

  // 线性代数 (8章)
  'xiandai-ch01': {
    id: 'xiandai-ch01',
    subjectId: 'xiandai',
    title: '行列式',
    order: 1,
    description: '行列式概念与性质、展开定理（拉普拉斯展开）、范德蒙德行列式、三对角与爪型行列式化简。',
    goals: [
      '熟练运用初等行/列变换消零化上三角计算行列式',
      '掌握加边法、递推法与拆项法计算特定构型行列式',
      '牢记代数余子式求和公式及克拉默法则'
    ],
    topicIds: [
      'xiandai-01-determinant-calc-techniques',
      'xiandai-01-cofactor-sum-expansion'
    ]
  },
  'xiandai-ch02': {
    id: 'xiandai-ch02',
    subjectId: 'xiandai',
    title: '矩阵及其运算',
    order: 2,
    description: '矩阵乘法与幂运算、逆矩阵求法、伴随矩阵性质、分块矩阵运算、初等矩阵与初等变换。',
    goals: [
      '掌握伴随矩阵 A* 的全套核心公式 (|A*|, (A*)^-1, r(A*))',
      '熟练计算可对角化矩阵与秩1矩阵的高次幂 A^n',
      '熟练利用初等行变换 [A | E] -> [E | A^-1] 求逆矩阵',
      '掌握分块对角矩阵与分块下三角矩阵的性质'
    ],
    topicIds: [
      'xiandai-02-adjoint-matrix-properties',
      'xiandai-02-matrix-power-calculation',
      'xiandai-02-elementary-matrix-operations'
    ]
  },
  'xiandai-ch03': {
    id: 'xiandai-ch03',
    subjectId: 'xiandai',
    title: '向量组与线性相关性',
    order: 3,
    description: '向量组线性表出与线性相关、极大线性无关组与秩、Schmidt正交化、两组向量等价判定。',
    goals: [
      '看到齐次方程 Ax=0 只有零解立即等价于列向量线性无关',
      '熟练掌握向量组秩与矩阵秩的关系及 Sylvester 秩不等式',
      '掌握施密特正交化步骤与正交矩阵性质'
    ],
    topicIds: [
      'xiandai-03-linear-independence-proof',
      'xiandai-03-maximal-linearly-independent-set',
      'xiandai-03-schmidt-orthogonalization'
    ]
  },
  'xiandai-ch04': {
    id: 'xiandai-ch04',
    subjectId: 'xiandai',
    title: '线性方程组',
    order: 4,
    description: '齐次/非齐次线性方程组解的判定、基础解系与通解结构、矩阵方程 AX=B 与公共解/同解。',
    goals: [
      '根据 r(A) 与 r(A|b) 的关系秒判无解、唯一解或无穷解',
      '熟练通过行最简形求出齐次基础解系与非齐次特解',
      '掌握联立方程组求公共解与由基础解系反求方程组'
    ],
    topicIds: [
      'xiandai-04-solution-structure-and-rank',
      'xiandai-04-matrix-equation-and-common-solutions'
    ]
  },
  'xiandai-ch05': {
    id: 'xiandai-ch05',
    subjectId: 'xiandai',
    title: '特征值与特征向量',
    order: 5,
    description: '特征方程与特征值性质（迹与行列式）、特征向量求解与几何重数、矩阵多项式特征值。',
    goals: [
      '牢记特征值两大法宝：∑λi = tr(A)，∏λi = |A|',
      '掌握矩阵多项式 f(A) 与 A*、A^-1 的特征值映射规律',
      '熟练根据基础解系求对应特征子空间维数'
    ],
    topicIds: [
      'xiandai-05-eigenvalue-eigenvector-properties',
      'xiandai-05-rank-one-eigenvalues'
    ]
  },
  'xiandai-ch06': {
    id: 'xiandai-ch06',
    subjectId: 'xiandai',
    title: '相似矩阵与矩阵对角化',
    order: 6,
    description: '相似矩阵的必要条件、相似对角化的充要条件、实对称矩阵必可正交对角化。',
    goals: [
      '秒判相似的必要条件：同秩、同行列式、同迹、同特征多项式',
      '掌握 n 阶矩阵可对角化的充要条件：每个重特征值的几何重数等于代数重数',
      '熟练运用正交矩阵正交相似对角化实对称矩阵'
    ],
    topicIds: [
      'xiandai-06-diagonalization-criterion',
      'xiandai-06-real-symmetric-orthogonal-diag'
    ]
  },
  'xiandai-ch07': {
    id: 'xiandai-ch07',
    subjectId: 'xiandai',
    title: '二次型',
    order: 7,
    description: '二次型矩阵表示、正交变换与配方法化标准形、惯性定理与规范形、正定矩阵充要判据。',
    goals: [
      '熟练写出二次型矩阵并用正交变换或配方法化为平方和',
      '掌握正定矩阵的五大等价充要条件（顺序主子式全大于0、特征值全正等）',
      '透彻理解等价、相似与合同三者关系的异同'
    ],
    topicIds: [
      'xiandai-07-quadratic-form-canonical',
      'xiandai-07-positive-definite-criteria'
    ]
  },
  'xiandai-ch08': {
    id: 'xiandai-ch08',
    subjectId: 'xiandai',
    title: '综合题与跨章节方法',
    order: 8,
    description: 'AB=0 深度挖掘、秩与解与特征向量全线贯通、实对称矩阵反求参数、几何直观综合题。',
    goals: [
      '见到 AB=0 立即反应出 B 的列向量全是 Ax=0 的解，r(A)+r(B)<=n',
      '灵活串联特征向量、方程组特解与极大无关组'
    ],
    topicIds: [
      'xiandai-08-ab-zero-deep-dive',
      'xiandai-08-cross-rank-eigen-systems'
    ]
  },

  // 概率论与数理统计 (8章)
  'gailv-ch01': {
    id: 'gailv-ch01',
    subjectId: 'gailv',
    title: '随机事件与概率',
    order: 1,
    description: '事件关系与运算律、条件概率、全概率公式与贝叶斯公式、事件独立性与伯努利试验。',
    goals: [
      '熟练用德摩根律与集合运算简化复杂事件概率表达式',
      '看到“原因导致结果”秒用全概，看到“已知结果反求原因”秒用贝叶斯',
      '掌握两两独立与相互独立的区别及条件独立性质'
    ],
    topicIds: [
      'gailv-01-total-probability-bayes',
      'gailv-01-event-independence-bernoulli'
    ]
  },
  'gailv-ch02': {
    id: 'gailv-ch02',
    subjectId: 'gailv',
    title: '一维随机变量及其分布',
    order: 2,
    description: '分布函数性质、离散型分布律、连续型概率密度、常见分布（0-1、二项、泊松、均匀、指数、正态）。',
    goals: [
      '牢记分布函数 F(x) 的右连续、单调非减与归一化性质',
      '牢记指数分布的无记忆性与正态分布标准正态转化',
      '熟练求解一维随机变量函数 Y=g(X) 的分布函数法与导数公式'
    ],
    topicIds: [
      'gailv-02-distribution-function-properties',
      'gailv-02-common-distributions-standard',
      'gailv-02-function-distribution-one-dim'
    ]
  },
  'gailv-ch03': {
    id: 'gailv-ch03',
    subjectId: 'gailv',
    title: '多维随机变量及其分布',
    order: 3,
    description: '二维联合分布函数与密度、边缘分布与条件分布、独立性判定、二维随机变量函数分布（Z=X+Y, max, min）。',
    goals: [
      '熟练画出二维积分区域计算边缘密度与条件密度',
      '掌握独立性判定充要条件 f(x,y)=f_X(x)f_Y(y)',
      '熟练运用卷积公式计算 Z=X+Y，及求 max(X,Y)、min(X,Y) 分布'
    ],
    topicIds: [
      'gailv-03-joint-marginal-conditional',
      'gailv-03-random-variable-functions-2d'
    ]
  },
  'gailv-ch04': {
    id: 'gailv-ch04',
    subjectId: 'gailv',
    title: '随机变量的数字特征',
    order: 4,
    description: '期望、方差、协方差、相关系数、常见分布数字特征表、不相关与独立的联系。',
    goals: [
      '熟练运用 E[g(X)] 与 E[g(X,Y)] 的积分/求和求法，无需先求 g(X) 密度',
      '牢记方差性质 D(aX+bY) = a^2DX + b^2DY + 2abCov(X,Y)',
      '深刻理解不相关 (Cov=0, ρ=0) 与独立的区别（二维正态下两者等价）'
    ],
    topicIds: [
      'gailv-04-expectation-egx-formulas',
      'gailv-04-variance-covariance-correlation'
    ]
  },
  'gailv-ch05': {
    id: 'gailv-ch05',
    subjectId: 'gailv',
    title: '大数定律与中心极限定理',
    order: 5,
    description: '切比雪夫不等式、切比雪夫大数定律、辛钦大数定律、独立同分布中心极限定理与棣莫弗-拉普拉斯定理。',
    goals: [
      '掌握切比雪夫不等式 P{|X-E(X)|>=ε} <= DX/ε^2 估值与变形',
      '熟练识别依概率收敛的形式与大数定律适用条件',
      '掌握用列维-林德伯格中心极限定理标准化近似计算概率'
    ],
    topicIds: [
      'gailv-05-chebyshev-inequality',
      'gailv-05-central-limit-theorems'
    ]
  },
  'gailv-ch06': {
    id: 'gailv-ch06',
    subjectId: 'gailv',
    title: '数理统计基本概念',
    order: 6,
    description: '总体与样本、统计量（样本均值、样本方差）、三大抽样分布（χ^2 分布、t 分布、F 分布）与正态总体抽样定理。',
    goals: [
      '牢记三大抽样分布的标准形式定义构造',
      '掌握正态总体四个抽样定理（X_bar 与 S^2 独立、(n-1)S^2/σ^2 ~ χ^2(n-1) 等）',
      '熟练计算由正态样本构造的统计量的数字特征'
    ],
    topicIds: [
      'gailv-06-three-sampling-distributions',
      'gailv-06-normal-population-sample-theorems'
    ]
  },
  'gailv-ch07': {
    id: 'gailv-ch07',
    subjectId: 'gailv',
    title: '参数估计',
    order: 7,
    description: '矩估计法、最大似然估计法（MLE）、估计量的评选标准（无偏性、有效性、相合性）、区间估计。',
    goals: [
      '熟练写出矩估计方程 E(X^k) = A_k 求解参数',
      '熟练掌握似然函数 L(θ) 建立、取对数求导与边界极大值讨论',
      '掌握验证无偏性 E[θ_hat] = θ 的标准计算'
    ],
    topicIds: [
      'gailv-07-moment-and-mle-estimation',
      'gailv-07-unbiasedness-eval-criteria'
    ]
  },
  'gailv-ch08': {
    id: 'gailv-ch08',
    subjectId: 'gailv',
    title: '综合题与跨章节方法',
    order: 8,
    description: '概率论与高等数学微积分综合（变限积分概率、级数求期望）、矩阵二次型与多元正态分布。',
    goals: [
      '掌握利用泰勒展开与极限定积分求解连续型概率分布问题',
      '掌握用微积分极值方法求解最大似然估计与最小方差'
    ],
    topicIds: [
      'gailv-08-cross-calculus-probability',
      'gailv-08-cross-mle-optimization'
    ]
  }
};
