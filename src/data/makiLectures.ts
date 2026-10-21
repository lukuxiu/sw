/**
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

export const MAKI_WAR_MAP: MakiWarMap = {
  "topLectures": [
    {
      "paper": "数一",
      "totalScorePercent": "51.3%",
      "annualAvgPoints": "77.0 分",
      "list": [
        {
          "rank": 1,
          "lectureId": "L59",
          "lectureTitle": "数字特征",
          "scorePercent": "7.76%",
          "annualPoints": "11.6分"
        },
        {
          "rank": 2,
          "lectureId": "L62",
          "lectureTitle": "参数估计",
          "scorePercent": "6.43%",
          "annualPoints": "9.6分"
        },
        {
          "rank": 3,
          "lectureId": "L18",
          "lectureTitle": "定积分与变限积分",
          "scorePercent": "5.70%",
          "annualPoints": "8.6分"
        },
        {
          "rank": 4,
          "lectureId": "L52",
          "lectureTitle": "二次型",
          "scorePercent": "5.40%",
          "annualPoints": "8.1分"
        },
        {
          "rank": 5,
          "lectureId": "L36",
          "lectureTitle": "曲面积分 (数一专属)",
          "scorePercent": "5.31%",
          "annualPoints": "8.0分"
        },
        {
          "rank": 6,
          "lectureId": "L50",
          "lectureTitle": "相似对角化",
          "scorePercent": "4.82%",
          "annualPoints": "7.2分"
        },
        {
          "rank": 7,
          "lectureId": "L30",
          "lectureTitle": "复合与隐函数求导",
          "scorePercent": "4.24%",
          "annualPoints": "6.4分"
        },
        {
          "rank": 8,
          "lectureId": "L40",
          "lectureTitle": "幂级数",
          "scorePercent": "4.00%",
          "annualPoints": "6.0分"
        },
        {
          "rank": 9,
          "lectureId": "L14",
          "lectureTitle": "导数的应用",
          "scorePercent": "3.88%",
          "annualPoints": "5.8分"
        },
        {
          "rank": 10,
          "lectureId": "L35",
          "lectureTitle": "曲线积分 (数一专属)",
          "scorePercent": "3.53%",
          "annualPoints": "5.3分"
        }
      ]
    },
    {
      "paper": "数二",
      "totalScorePercent": "59.8%",
      "annualAvgPoints": "89.7 分",
      "list": [
        {
          "rank": 1,
          "lectureId": "L33",
          "lectureTitle": "二重积分",
          "scorePercent": "10.56%",
          "annualPoints": "15.8分"
        },
        {
          "rank": 2,
          "lectureId": "L18",
          "lectureTitle": "定积分与变限积分",
          "scorePercent": "10.33%",
          "annualPoints": "15.5分"
        },
        {
          "rank": 3,
          "lectureId": "L14",
          "lectureTitle": "导数的应用",
          "scorePercent": "5.98%",
          "annualPoints": "9.0分"
        },
        {
          "rank": 4,
          "lectureId": "L21",
          "lectureTitle": "定积分几何应用",
          "scorePercent": "5.77%",
          "annualPoints": "8.7分"
        },
        {
          "rank": 5,
          "lectureId": "L30",
          "lectureTitle": "复合与隐函数求导",
          "scorePercent": "5.49%",
          "annualPoints": "8.2分"
        },
        {
          "rank": 6,
          "lectureId": "L52",
          "lectureTitle": "二次型",
          "scorePercent": "5.10%",
          "annualPoints": "7.7分"
        },
        {
          "rank": 7,
          "lectureId": "L50",
          "lectureTitle": "相似对角化",
          "scorePercent": "4.78%",
          "annualPoints": "7.2分"
        },
        {
          "rank": 8,
          "lectureId": "L47",
          "lectureTitle": "线性方程组（一）",
          "scorePercent": "4.55%",
          "annualPoints": "6.8分"
        },
        {
          "rank": 9,
          "lectureId": "L25",
          "lectureTitle": "二阶常系数线性方程",
          "scorePercent": "4.35%",
          "annualPoints": "6.5分"
        },
        {
          "rank": 10,
          "lectureId": "L13",
          "lectureTitle": "泰勒展开求极限",
          "scorePercent": "3.45%",
          "annualPoints": "5.2分"
        }
      ]
    },
    {
      "paper": "数三",
      "totalScorePercent": "50.6%",
      "annualAvgPoints": "75.8 分",
      "list": [
        {
          "rank": 1,
          "lectureId": "L59",
          "lectureTitle": "数字特征",
          "scorePercent": "8.74%",
          "annualPoints": "13.1分"
        },
        {
          "rank": 2,
          "lectureId": "L33",
          "lectureTitle": "二重积分",
          "scorePercent": "8.27%",
          "annualPoints": "12.4分"
        },
        {
          "rank": 3,
          "lectureId": "L18",
          "lectureTitle": "定积分与变限积分",
          "scorePercent": "5.59%",
          "annualPoints": "8.4分"
        },
        {
          "rank": 4,
          "lectureId": "L62",
          "lectureTitle": "参数估计",
          "scorePercent": "5.14%",
          "annualPoints": "7.7分"
        },
        {
          "rank": 5,
          "lectureId": "L52",
          "lectureTitle": "二次型",
          "scorePercent": "4.98%",
          "annualPoints": "7.5分"
        },
        {
          "rank": 6,
          "lectureId": "L50",
          "lectureTitle": "相似对角化",
          "scorePercent": "4.71%",
          "annualPoints": "7.1分"
        },
        {
          "rank": 7,
          "lectureId": "L13",
          "lectureTitle": "泰勒展开求极限",
          "scorePercent": "4.01%",
          "annualPoints": "6.0分"
        },
        {
          "rank": 8,
          "lectureId": "L47",
          "lectureTitle": "线性方程组（一）",
          "scorePercent": "3.80%",
          "annualPoints": "5.7分"
        },
        {
          "rank": 9,
          "lectureId": "L30",
          "lectureTitle": "复合与隐函数求导",
          "scorePercent": "3.25%",
          "annualPoints": "4.9分"
        },
        {
          "rank": 10,
          "lectureId": "L57",
          "lectureTitle": "二维随机变量",
          "scorePercent": "3.06%",
          "annualPoints": "4.6分"
        }
      ]
    }
  ],
  "zeroExamTopics": [
    {
      "code": "6.1",
      "title": "单调有界准则与数列极限存在性",
      "lectureId": "L06",
      "fact": "17年 0 道独立题。",
      "strategy": "准则本身不单独出题，它是递推数列题（6.2）里的固定一步，跟着递推题练骨架即可，无需单独做抽象证明训练。"
    },
    {
      "code": "7.2",
      "title": "零点定理与介值定理的应用",
      "lectureId": "L07",
      "fact": "17年 0 道独立题。",
      "strategy": "从不单独命题，只作为方程根、不等式证明大题（L15）的第一步“造点”出现。会套用即可。"
    },
    {
      "code": "28.1",
      "title": "向量的运算与几何意义",
      "lectureId": "L28",
      "fact": "17年 0 道独立题。",
      "strategy": "只留数量积、向量积、混合积三张公式，作为 L31、L35、L36 的前置计算工具，不做纯几何推导。"
    },
    {
      "code": "28.2",
      "title": "平面与直线的方程及位置关系",
      "lectureId": "L28",
      "fact": "17年 0 道独立题。",
      "strategy": "压缩成一页速查表，不设例题，不做位置关系的复杂分类讨论训练。"
    },
    {
      "code": "28.3",
      "title": "曲面、空间曲线及其投影",
      "lectureId": "L28",
      "fact": "17年 0 道独立题。",
      "strategy": "只保留常见二次曲面的立体图形与投影柱面的写法，服务于三重积分与曲面积分定限。"
    },
    {
      "code": "43.3",
      "title": "行列式与矩阵、特征值的联系",
      "lectureId": "L43",
      "fact": "17年 0 道独立题。",
      "strategy": "只记 |A|=∏λi 与 tr(A)=∑λi 两条核心结论；其余题型均归入 L44 矩阵变形与 L50 对角化。"
    },
    {
      "code": "44.4",
      "title": "矩阵高次幂计算",
      "lectureId": "L44",
      "fact": "17年 0 道独立题。",
      "strategy": "真题中求 A^n 一律以相似对角化 A=PΛP^{-1} 的形式出现，归在 L50.1 名下系统训练。"
    },
    {
      "code": "50.2",
      "title": "由特征信息反求矩阵",
      "lectureId": "L50",
      "fact": "17年 0 道独立题。",
      "strategy": "真题给出的一律是实对称矩阵情形，整道题直接在 L51.2（实对称正交化）名下攻坚。"
    },
    {
      "code": "58.2",
      "title": "极值与顺序统计量分布",
      "lectureId": "L58",
      "fact": "17年 0 道独立题。",
      "strategy": "只记 Fmax=F^n 与 Fmin=1-(1-F)^n；它总是数字特征（L59）与似然估计（L62）的中间步骤。"
    },
    {
      "code": "62.1",
      "title": "矩估计法",
      "lectureId": "L62",
      "fact": "17年 0 道独立题。",
      "strategy": "只留“样本矩=总体矩”一步方程；核心精力全力攻坚最大似然估计（数一85分、数三79分）。"
    }
  ],
  "difficultyRanks": [
    {
      "lectureId": "L10",
      "lectureTitle": "微分中值定理（一）",
      "difficulty": "3.44 星",
      "reason": "14个题位里12个是解答题，全书区分度最高的一讲，必须掌握五大构造套路。"
    },
    {
      "lectureId": "L06",
      "lectureTitle": "递推数列极限",
      "difficulty": "3.40 星",
      "reason": "综合性强，单调有界+导数放缩+极限方程，解答题常客。"
    },
    {
      "lectureId": "L15",
      "lectureTitle": "不等式证明与方程根",
      "difficulty": "3.44 星",
      "reason": "12个题位里8个解答题，四条证明路线决策。"
    },
    {
      "lectureId": "L36",
      "lectureTitle": "曲面积分 (数一)",
      "difficulty": "3.38 星",
      "reason": "空间几何想象力与高斯散度外侧补底面计算量大。"
    },
    {
      "lectureId": "L51",
      "lectureTitle": "实对称矩阵",
      "difficulty": "3.25 星",
      "reason": "施密特正交化与特征向量方程组联立，步骤繁琐易失误。"
    }
  ],
  "shortestPaths": [
    {
      "paper": "数一",
      "lecturesCount": 66,
      "keyLecturesCount": 18,
      "estimatedHours": "约 35 小时",
      "strategySummary": "66 讲全覆盖，重点攻坚 18 讲重点讲。重心在第 3 编多元与线面积分（23.8%）及概率统计（21.6%）。"
    },
    {
      "paper": "数二",
      "lecturesCount": 44,
      "keyLecturesCount": 13,
      "estimatedHours": "约 24 小时",
      "strategySummary": "砍掉级数与概率，讲次最少但密度最大！高数吃掉 68.6% 分数。重点打歼灭战：吃透 L33、L18、L14、L21、L30 四讲即稳拿 42 分！"
    },
    {
      "paper": "数三",
      "lecturesCount": 57,
      "keyLecturesCount": 16,
      "estimatedHours": "约 31 小时",
      "strategySummary": "分布最平均的一卷，概率（L59、L62）、高数（L33、L18）、线代（L50、L52）三足鼎立。"
    }
  ]
};

export const TOPIC_TO_LECTURE: Record<string, { lectureId: string; lectureTitle: string }> = {
  "yingshi-64-exam-time-structure": {
    "lectureId": "L64",
    "lectureTitle": "卷面结构与时间分配"
  },
  "gaoshu-00-algebra-five-actions": {
    "lectureId": "L02",
    "lectureTitle": "高中补丁一次打完"
  },
  "gaoshu-01-indeterminate-0-0": {
    "lectureId": "L13",
    "lectureTitle": "极限计算总攻略（二）：泰勒展开"
  },
  "gaoshu-01-sequence-monotone-bounded": {
    "lectureId": "L06",
    "lectureTitle": "数列极限：单调有界准则与递推数列"
  },
  "gaoshu-01-infinitesimal-order": {
    "lectureId": "L05",
    "lectureTitle": "两个重要极限与等价无穷小"
  },
  "gaoshu-01-power-exponential-1-inf": {
    "lectureId": "L05",
    "lectureTitle": "两个重要极限与等价无穷小"
  },
  "gaoshu-01-discontinuity-points": {
    "lectureId": "L07",
    "lectureTitle": "连续、间断与零点定理"
  },
  "gaoshu-02-derivative-definition": {
    "lectureId": "L08",
    "lectureTitle": "导数与微分"
  },
  "gaoshu-02-higher-order-leibniz": {
    "lectureId": "L09",
    "lectureTitle": "求导技术全家桶"
  },
  "gaoshu-05-chain-rule-composite": {
    "lectureId": "L30",
    "lectureTitle": "复合函数与隐函数求导"
  },
  "gaoshu-05-implicit-function-differentiation": {
    "lectureId": "L30",
    "lectureTitle": "复合函数与隐函数求导"
  },
  "gaoshu-02-mean-value-theorems": {
    "lectureId": "L10",
    "lectureTitle": "微分中值定理（一）"
  },
  "gaoshu-01-difference-inf-inf": {
    "lectureId": "L11",
    "lectureTitle": "极限计算总攻略（一）：洛必达与未定式"
  },
  "gaoshu-02-taylor-formula-proof": {
    "lectureId": "L12",
    "lectureTitle": "微分中值定理（二）：泰勒公式"
  },
  "gaoshu-10-cross-taylor-proofs": {
    "lectureId": "L13",
    "lectureTitle": "极限计算总攻略（二）：泰勒展开"
  },
  "gaoshu-02-inequality-and-roots": {
    "lectureId": "L15",
    "lectureTitle": "不等式证明与方程根的个数"
  },
  "gaoshu-03-variable-limit-integral": {
    "lectureId": "L23",
    "lectureTitle": "第一编串讲：积分等式与不等式的证明"
  },
  "gaoshu-03-definite-integral-symmetry": {
    "lectureId": "L23",
    "lectureTitle": "第一编串讲：积分等式与不等式的证明"
  },
  "gaoshu-03-improper-integral-convergence": {
    "lectureId": "L20",
    "lectureTitle": "反常积分"
  },
  "gaoshu-03-geometric-applications": {
    "lectureId": "L22",
    "lectureTitle": "定积分的物理与经济应用"
  },
  "gaoshu-04-first-order-ode": {
    "lectureId": "L27",
    "lectureTitle": "微分方程应用题"
  },
  "gaoshu-04-second-order-constant-coeff": {
    "lectureId": "L27",
    "lectureTitle": "微分方程应用题"
  },
  "gaoshu-04-reducible-ode": {
    "lectureId": "L25",
    "lectureTitle": "可降阶方程与二阶常系数线性方程"
  },
  "gaoshu-04-euler-equation": {
    "lectureId": "L26",
    "lectureTitle": "高阶线性与欧拉方程／差分方程"
  },
  "gaoshu-09-vectors-planes-lines": {
    "lectureId": "L28",
    "lectureTitle": "向量代数与空间解析几何"
  },
  "gaoshu-09-surfaces-and-projections": {
    "lectureId": "L28",
    "lectureTitle": "向量代数与空间解析几何"
  },
  "gaoshu-05-differentiability-concept": {
    "lectureId": "L29",
    "lectureTitle": "多元函数的极限、连续、偏导与全微分"
  },
  "gaoshu-05-directional-derivative-gradient": {
    "lectureId": "L31",
    "lectureTitle": "方向导数、梯度与几何应用"
  },
  "gaoshu-05-lagrange-multipliers": {
    "lectureId": "L32",
    "lectureTitle": "隐函数确定的函数求极值（本讲与 L32 的接口）"
  },
  "gaoshu-06-double-integral-polar": {
    "lectureId": "L33",
    "lectureTitle": "二重积分"
  },
  "gaoshu-06-order-exchange-symmetry": {
    "lectureId": "L33",
    "lectureTitle": "二重积分"
  },
  "gaoshu-06-triple-integral-coordinates": {
    "lectureId": "L34",
    "lectureTitle": "三重积分"
  },
  "gaoshu-07-curvilinear-path-independent": {
    "lectureId": "L35",
    "lectureTitle": "曲线积分"
  },
  "gaoshu-07-green-formula-hole-technique": {
    "lectureId": "L35",
    "lectureTitle": "曲线积分"
  },
  "gaoshu-07-gauss-divergence-theorem": {
    "lectureId": "L36",
    "lectureTitle": "曲面积分"
  },
  "gaoshu-07-stokes-theorem-curl": {
    "lectureId": "L37",
    "lectureTitle": "场论初步"
  },
  "gaoshu-08-series-convergence-tests": {
    "lectureId": "L39",
    "lectureTitle": "交错级数与任意项级数"
  },
  "gaoshu-08-power-series-radius-interval": {
    "lectureId": "L40",
    "lectureTitle": "幂级数"
  },
  "gaoshu-08-power-series-summation": {
    "lectureId": "L41",
    "lectureTitle": "函数展开与级数求和"
  },
  "gaoshu-10-fourier-series-dirichlet": {
    "lectureId": "L42",
    "lectureTitle": "傅里叶级数"
  },
  "xiandai-01-determinant-properties-definition": {
    "lectureId": "L43",
    "lectureTitle": "行列式"
  },
  "xiandai-01-determinant-calc-techniques": {
    "lectureId": "L43",
    "lectureTitle": "行列式"
  },
  "xiandai-02-matrix-multiplication-inverse": {
    "lectureId": "L44",
    "lectureTitle": "矩阵运算与逆矩阵"
  },
  "xiandai-02-adjoint-matrix-properties": {
    "lectureId": "L44",
    "lectureTitle": "矩阵运算与逆矩阵"
  },
  "xiandai-02-elementary-matrix-operations": {
    "lectureId": "L45",
    "lectureTitle": "初等变换、初等矩阵与秩"
  },
  "xiandai-02-matrix-rank-theorems": {
    "lectureId": "L45",
    "lectureTitle": "初等变换、初等矩阵与秩"
  },
  "xiandai-03-vector-linear-combination-dependence": {
    "lectureId": "L46",
    "lectureTitle": "向量组的线性相关性"
  },
  "xiandai-03-maximal-linearly-independent-set": {
    "lectureId": "L46",
    "lectureTitle": "向量组的线性相关性"
  },
  "xiandai-04-linear-system-solvability": {
    "lectureId": "L47",
    "lectureTitle": "线性方程组（一）：消元、判定与通解"
  },
  "xiandai-04-homogeneous-fundamental-system": {
    "lectureId": "L47",
    "lectureTitle": "线性方程组（一）：消元、判定与通解"
  },
  "xiandai-04-non-homogeneous-general-solution": {
    "lectureId": "L48",
    "lectureTitle": "线性方程组（二）：矩阵方程、同解与向量空间"
  },
  "xiandai-04-matrix-equation-and-common-solutions": {
    "lectureId": "L48",
    "lectureTitle": "线性方程组（二）：矩阵方程、同解与向量空间"
  },
  "xiandai-05-eigenvalues-eigenvectors": {
    "lectureId": "L49",
    "lectureTitle": "特征值与特征向量"
  },
  "xiandai-05-eigen-properties-special-matrices": {
    "lectureId": "L49",
    "lectureTitle": "特征值与特征向量"
  },
  "xiandai-06-similarity-diagonalization-criterion": {
    "lectureId": "L50",
    "lectureTitle": "相似对角化"
  },
  "xiandai-06-power-trace-applications": {
    "lectureId": "L50",
    "lectureTitle": "相似对角化"
  },
  "xiandai-06-real-symmetric-orthogonal-diag": {
    "lectureId": "L51",
    "lectureTitle": "实对称矩阵"
  },
  "xiandai-07-quadratic-form-matrix-representation": {
    "lectureId": "L52",
    "lectureTitle": "二次型"
  },
  "xiandai-07-canonical-standard-form-methods": {
    "lectureId": "L52",
    "lectureTitle": "二次型"
  },
  "xiandai-07-positive-definite-criteria": {
    "lectureId": "L52",
    "lectureTitle": "二次型"
  },
  "xiandai-08-cross-linear-algebra-mastery": {
    "lectureId": "L53",
    "lectureTitle": "大串讲：五条主线的语言互译"
  },
  "gailv-01-random-events-conditional-prob": {
    "lectureId": "L54",
    "lectureTitle": "随机事件与概率"
  },
  "gailv-01-total-probability-bayes": {
    "lectureId": "L54",
    "lectureTitle": "随机事件与概率"
  },
  "gailv-01-event-independence-bernoulli": {
    "lectureId": "L54",
    "lectureTitle": "随机事件与概率"
  },
  "gailv-02-cdf-properties": {
    "lectureId": "L55",
    "lectureTitle": "一维随机变量及其分布"
  },
  "gailv-02-common-discrete-distributions": {
    "lectureId": "L55",
    "lectureTitle": "一维随机变量及其分布"
  },
  "gailv-02-common-continuous-distributions": {
    "lectureId": "L55",
    "lectureTitle": "一维随机变量及其分布"
  },
  "gailv-02-distribution-function-method": {
    "lectureId": "L56",
    "lectureTitle": "随机变量函数的分布"
  },
  "gailv-03-joint-marginal-distributions": {
    "lectureId": "L57",
    "lectureTitle": "二维随机变量"
  },
  "gailv-03-conditional-distribution-independence": {
    "lectureId": "L57",
    "lectureTitle": "二维随机变量"
  },
  "gailv-03-discrete-continuous-mixed-variables": {
    "lectureId": "L58",
    "lectureTitle": "二维随机变量函数的分布"
  },
  "gailv-03-convolution-formula-sum": {
    "lectureId": "L58",
    "lectureTitle": "二维随机变量函数的分布"
  },
  "gailv-04-expectation-variance-properties": {
    "lectureId": "L59",
    "lectureTitle": "数字特征"
  },
  "gailv-04-covariance-correlation-coefficient": {
    "lectureId": "L59",
    "lectureTitle": "数字特征"
  },
  "gailv-04-chebyshev-inequality": {
    "lectureId": "L59",
    "lectureTitle": "数字特征"
  },
  "gailv-05-law-of-large-numbers": {
    "lectureId": "L60",
    "lectureTitle": "大数定律与中心极限定理"
  },
  "gailv-05-central-limit-theorem": {
    "lectureId": "L60",
    "lectureTitle": "大数定律与中心极限定理"
  },
  "gailv-06-population-sample-statistics": {
    "lectureId": "L61",
    "lectureTitle": "数理统计基础"
  },
  "gailv-06-three-sampling-distributions": {
    "lectureId": "L61",
    "lectureTitle": "数理统计基础"
  },
  "gailv-07-moment-and-mle-estimation": {
    "lectureId": "L62",
    "lectureTitle": "参数估计"
  },
  "gailv-07-unbiasedness-eval-criteria": {
    "lectureId": "L62",
    "lectureTitle": "参数估计"
  },
  "gailv-08-confidence-interval-hypothesis-test": {
    "lectureId": "L63",
    "lectureTitle": "区间估计与假设检验"
  },
  "yingshi-65-calculation-mistakes-checklist": {
    "lectureId": "L65",
    "lectureTitle": "计算失误清单"
  },
  "yingshi-66-survival-and-advanced-checklist": {
    "lectureId": "L66",
    "lectureTitle": "保命清单与进阶清单"
  }
};

export const MAKI_LECTURES: MakiLecture[] = [
  {
    "id": "L01",
    "num": 1,
    "title": "规则说明与本课使用方法",
    "partNum": 0,
    "partTitle": "第 0 编 预备",
    "page": 35,
    "pageEnd": 39,
    "isKey": false,
    "isCompressed": false,
    "isMath1Only": false,
    "isMath2Heavy": false,
    "isMath3Only": false,
    "isMethod": true,
    "tags": [
      "方法课",
      "统考必考"
    ],
    "orientation": "开课第一讲。不讲数学，只把账本摊开：这张卷子由什么构成、哪一编在哪一卷值钱、 每道题号固定考什么。本讲的所有数字都来自2010–2026 年数一二三的51 套真题卷、1155 个卷 面题位，不是大纲口径的估算，是实际卷面的清点结果。第一讲就把账看懂，后面65 讲的取舍才 有依据。",
    "subsections": [
      "三卷的基本盘",
      "题号分布",
      "这本讲义怎么用",
      "计算基本功自查"
    ],
    "stats": {
      "independentQuestions": 0,
      "positions": 0,
      "choiceCount": 0,
      "blankCount": 0,
      "solutionCount": 0,
      "math1Score": 0,
      "math2Score": 0,
      "math3Score": 0,
      "math1Percent": "0.00%",
      "math2Percent": "0.00%",
      "math3Percent": "0.00%",
      "avgDifficulty": "★★☆☆☆"
    },
    "methodCards": [
      {
        "title": "180分钟全卷宏观骨架与真题账本",
        "subtitle": "选填80分 + 解答70分新格局",
        "content": "解答题砍至6道后单题分值大幅上升，综合性极强；选填占比过半，必须保证极高正确率。线代三卷同价（每年雷打不动32.5分），数二高数占比46%（打歼灭战），数一概率线面积分占比最高（扫大片）。"
      }
    ],
    "pitfalls": [
      "未看清本讲在三卷中的具体分值权重与适用标签（方法课、统考必考）。",
      "忽略定理适用的前提条件（如开闭区间、可导性、正交性或独立性前提）。"
    ],
    "mappedTopicIds": [
      "yingshi-64-exam-time-structure"
    ]
  },
  {
    "id": "L02",
    "num": 2,
    "title": "高中补丁一次打完",
    "partNum": 0,
    "partTitle": "第 0 编 预备",
    "page": 39,
    "pageEnd": 49,
    "isKey": false,
    "isCompressed": false,
    "isMath1Only": false,
    "isMath2Heavy": false,
    "isMath3Only": false,
    "isMethod": true,
    "tags": [
      "方法课",
      "统考必考"
    ],
    "orientation": "本讲把整门课要用到的高中知识一次补齐。不求理解推导，只求会用——这些是工具， 不是考点。之后不再回头讲。 本讲是全书唯一没有真题归属的知识讲：2010–2026 的846 道真题里，没有任何一道考高中 内容。但每一道题都在用它。所以本讲的每一节末尾都会点名：这条公式在哪几道真题的详解里 被直接调用过。下面这些次数是把846 道题的自撰详解逐份检索得到的，不是估计。 易错/ 提醒 先看结论。真正会卡住你的高中欠账只有四块，按被调用的频次排：",
    "subsections": [
      "三角公式体系",
      "指数与对数",
      "常用不等式",
      "初等函数图像与性质",
      "五个代数动作"
    ],
    "stats": {
      "independentQuestions": 0,
      "positions": 0,
      "choiceCount": 0,
      "blankCount": 0,
      "solutionCount": 0,
      "math1Score": 0,
      "math2Score": 0,
      "math3Score": 0,
      "math1Percent": "0.00%",
      "math2Percent": "0.00%",
      "math3Percent": "0.00%",
      "avgDifficulty": "★★☆☆☆"
    },
    "methodCards": [
      {
        "title": "五大代数变形动作总表",
        "subtitle": "配方 · 有理化 · 裂项 · 放缩 · 换元",
        "content": "配方（二次三项式开方或积分必备）、有理化（根式差消去）、裂项（分母乘积拆和差）、放缩（常用不等式 e^x >= 1+x, ln(1+x) <= x）、换元（对称与三角代换）。"
      }
    ],
    "pitfalls": [
      "未看清本讲在三卷中的具体分值权重与适用标签（方法课、统考必考）。",
      "忽略定理适用的前提条件（如开闭区间、可导性、正交性或独立性前提）。"
    ],
    "mappedTopicIds": [
      "gaoshu-00-algebra-five-actions"
    ]
  },
  {
    "id": "L03",
    "num": 3,
    "title": "极限的定义、左右极限与海涅定理",
    "partNum": 1,
    "partTitle": "第 1 编 一元函数微积分",
    "page": 49,
    "pageEnd": 57,
    "isKey": false,
    "isCompressed": true,
    "isMath1Only": false,
    "isMath2Heavy": false,
    "isMath3Only": false,
    "isMethod": false,
    "tags": [
      "压缩讲",
      "统考必考"
    ],
    "orientation": "17 年真题里本讲名下只有3 道独立题、4 个卷面题位，数一占0.2%、数二0.39%、数 三0.16%——数三17 年一共只从这一讲拿走过4 分（一道选择题）。这是全书最该少花时间的几 讲之一，按压缩讲读。 但“少花时间”不等于“不看”：这3 道题的平均难度是3.0，比隔壁L05（2.1）还高。原因很 简单——本讲考的从来不是“算极限”，而是判断极限存不存在，4 个题位全是选择题，全是“下 列命题正确的是”这种要靠反例排除的形态。ε-N 与ε-δ 语言2010–2026 一次都没有直接命过题。",
    "subsections": [
      "定义：看懂就走",
      "左右极限与六种趋近",
      "海涅定理与子列：本讲唯一的命题点",
      "存在准则：单调有界",
      "本讲小结"
    ],
    "stats": {
      "independentQuestions": 3,
      "positions": 4,
      "choiceCount": 4,
      "blankCount": 0,
      "solutionCount": 0,
      "math1Score": 5,
      "math2Score": 10,
      "math3Score": 4,
      "math1Percent": "0.20%",
      "math2Percent": "0.39%",
      "math3Percent": "0.16%",
      "avgDifficulty": "★★☆☆☆"
    },
    "methodCards": [
      {
        "title": "极限的定义、左右极限与海涅定理 核心方法梳理",
        "subtitle": "涵盖 5 个进阶小节",
        "content": "本讲重点掌握 定义：看懂就走、左右极限与六种趋近、海涅定理与子列：本讲唯一的命题点、存在准则：单调有界 等核心知识链路，严格对齐考研大纲要求与历年命题规律。"
      }
    ],
    "pitfalls": [
      "未看清本讲在三卷中的具体分值权重与适用标签（压缩讲、统考必考）。",
      "忽略定理适用的前提条件（如开闭区间、可导性、正交性或独立性前提）。"
    ],
    "mappedTopicIds": [
      "gaoshu-01-indeterminate-0-0",
      "gaoshu-01-sequence-monotone-bounded"
    ]
  },
  {
    "id": "L04",
    "num": 4,
    "title": "极限的性质与运算法则",
    "partNum": 1,
    "partTitle": "第 1 编 一元函数微积分",
    "page": 57,
    "pageEnd": 69,
    "isKey": false,
    "isCompressed": true,
    "isMath1Only": false,
    "isMath2Heavy": false,
    "isMath3Only": false,
    "isMethod": false,
    "tags": [
      "压缩讲",
      "统考必考"
    ],
    "orientation": "一个数据就能定调：本讲17 年6 道独立题、7 个卷面题位，7 个题位全部是选择题， 填空0 道、解答0 道。这意味着本讲的产出形态只有一种——在四个命题里挑真假，既不用写过 程，也不用算数值，靠的是反例库而不是推导能力。 分值极低且不平均：数三0.67%（17 分）、数二0.35%（9 分），数一只有0.2%——17 年里数 一只在2022 年考过本讲一次，一道选择题5 分。更细一点看：本讲的“无穷小的阶”那个考点， 数一17 年是0 分。",
    "subsections": [
      "三条局部性质",
      "四则运算法则与“存在／不存在”组合",
      "无穷小与无穷大",
      "无穷小的阶：本讲只考“命题真假”",
      "本讲小结"
    ],
    "stats": {
      "independentQuestions": 6,
      "positions": 7,
      "choiceCount": 7,
      "blankCount": 0,
      "solutionCount": 0,
      "math1Score": 5,
      "math2Score": 9,
      "math3Score": 17,
      "math1Percent": "0.20%",
      "math2Percent": "0.35%",
      "math3Percent": "0.67%",
      "avgDifficulty": "★★★☆☆"
    },
    "methodCards": [
      {
        "title": "极限的性质与运算法则 核心方法梳理",
        "subtitle": "涵盖 5 个进阶小节",
        "content": "本讲重点掌握 三条局部性质、四则运算法则与“存在／不存在”组合、无穷小与无穷大、无穷小的阶：本讲只考“命题真假” 等核心知识链路，严格对齐考研大纲要求与历年命题规律。"
      }
    ],
    "pitfalls": [
      "未看清本讲在三卷中的具体分值权重与适用标签（压缩讲、统考必考）。",
      "忽略定理适用的前提条件（如开闭区间、可导性、正交性或独立性前提）。"
    ],
    "mappedTopicIds": [
      "gaoshu-01-indeterminate-0-0",
      "gaoshu-01-infinitesimal-order"
    ]
  },
  {
    "id": "L05",
    "num": 5,
    "title": "两个重要极限与等价无穷小",
    "partNum": 1,
    "partTitle": "第 1 编 一元函数微积分",
    "page": 69,
    "pageEnd": 89,
    "isKey": false,
    "isCompressed": false,
    "isMath1Only": false,
    "isMath2Heavy": false,
    "isMath3Only": false,
    "isMethod": false,
    "tags": [
      "统考必考"
    ],
    "orientation": "本讲是极限板块里性价比最高的一讲：14 道独立题、16 个卷面题位，数三",
    "subsections": [
      "两个重要极限与 1 公式",
      "等价无穷小表",
      "适用边界：只能代乘除因子",
      "无穷小定阶：数二专属的一族",
      "本讲小结"
    ],
    "stats": {
      "independentQuestions": 14,
      "positions": 16,
      "choiceCount": 5,
      "blankCount": 9,
      "solutionCount": 2,
      "math1Score": 17,
      "math2Score": 26,
      "math3Score": 39,
      "math1Percent": "0.67%",
      "math2Percent": "1.02%",
      "math3Percent": "1.53%",
      "avgDifficulty": "★★★☆☆"
    },
    "methodCards": [
      {
        "title": "两个重要极限与等价无穷小 核心方法梳理",
        "subtitle": "涵盖 5 个进阶小节",
        "content": "本讲重点掌握 两个重要极限与 1 公式、等价无穷小表、适用边界：只能代乘除因子、无穷小定阶：数二专属的一族 等核心知识链路，严格对齐考研大纲要求与历年命题规律。"
      }
    ],
    "pitfalls": [
      "未看清本讲在三卷中的具体分值权重与适用标签（统考必考）。",
      "忽略定理适用的前提条件（如开闭区间、可导性、正交性或独立性前提）。"
    ],
    "mappedTopicIds": [
      "gaoshu-01-indeterminate-0-0",
      "gaoshu-01-infinitesimal-order",
      "gaoshu-01-power-exponential-1-inf"
    ]
  },
  {
    "id": "L06",
    "num": 6,
    "title": "数列极限：单调有界准则与递推数列",
    "partNum": 1,
    "partTitle": "第 1 编 一元函数微积分",
    "page": 89,
    "pageEnd": 101,
    "isKey": false,
    "isCompressed": false,
    "isMath1Only": false,
    "isMath2Heavy": false,
    "isMath3Only": false,
    "isMethod": false,
    "tags": [
      "统考必考"
    ],
    "orientation": "这是一讲小而硬的课。17 年真题里本讲名下只有5 道独立题、7 个卷面题位，数三 0.76%（19 分）、数一0.56%（14 分）、数二0.56%（14 分）——题量是极限板块里最少的。但7 个题位里3 个是解答题，平均难度3.4，“数列极限与递推数列”这个考点排在全书难度榜的第7 位。 题少、分不多、难度高，所以本讲的目标只有一个：把递推数列的三步法写到闭眼能出。它 是一道10–12 分的解答题，2018 年三卷同时考——不会写就是整题空白，会写就是模板分。 注意分工：两条存在准则都在本讲讲完，但n 项和极限的真题在L18——那里有独立的一个 考点、9 个题位，主刀的是定积分",
    "subsections": [
      "两条存在准则：单调有界与夹逼",
      "递推数列三步法：本讲的全部分数",
      "通项型数列：先化简，再判断",
      "本讲小结"
    ],
    "stats": {
      "independentQuestions": 5,
      "positions": 7,
      "choiceCount": 3,
      "blankCount": 1,
      "solutionCount": 3,
      "math1Score": 14,
      "math2Score": 14,
      "math3Score": 19,
      "math1Percent": "0.55%",
      "math2Percent": "0.55%",
      "math3Percent": "0.75%",
      "avgDifficulty": "★★★☆☆"
    },
    "methodCards": [
      {
        "title": "数列极限：单调有界准则与递推数列 核心方法梳理",
        "subtitle": "涵盖 4 个进阶小节",
        "content": "本讲重点掌握 两条存在准则：单调有界与夹逼、递推数列三步法：本讲的全部分数、通项型数列：先化简，再判断、本讲小结 等核心知识链路，严格对齐考研大纲要求与历年命题规律。"
      }
    ],
    "pitfalls": [
      "未看清本讲在三卷中的具体分值权重与适用标签（统考必考）。",
      "忽略定理适用的前提条件（如开闭区间、可导性、正交性或独立性前提）。"
    ],
    "mappedTopicIds": [
      "gaoshu-01-sequence-monotone-bounded"
    ]
  },
  {
    "id": "L07",
    "num": 7,
    "title": "连续、间断与零点定理",
    "partNum": 1,
    "partTitle": "第 1 编 一元函数微积分",
    "page": 101,
    "pageEnd": 113,
    "isKey": false,
    "isCompressed": false,
    "isMath1Only": false,
    "isMath2Heavy": false,
    "isMath3Only": false,
    "isMethod": false,
    "tags": [
      "统考必考"
    ],
    "orientation": "一个数据把这一讲的练法完全定死了：17 年8 道独立题、11 个卷面题位，11 个全部 是选择题——填空0 道、解答0 道。 所以本讲只有一种考法：判断间断点类型。本讲挂着两个考点，第二个“零点定理与介值定 理的应用”2010–2026 未单独命题：它从来不自己出题，只作为大题的第一步出现。那类“证明 存在ξ”的大题归在L15 （考点15.1 方程根的存在性与个数，7 个题位）和L10 （微分中值定 理，14 个解答题位）。本讲只负责认间断点。 分值：数二0.98%（25 分）、数三0.67%（17 分）、数一0.16%（17 年只有4 分，一道选择 题）。平均难度2.5——不难，但极易被“漏掉一个可疑点”扣掉整题的分。",
    "subsections": [
      "连续与分段函数定参数",
      "间断点分类与计数（本讲主力）",
      "由极限定义的函数",
      "零点定理与介值定理：闭区间上连续函数的四大性质",
      "本讲小结"
    ],
    "stats": {
      "independentQuestions": 8,
      "positions": 11,
      "choiceCount": 11,
      "blankCount": 0,
      "solutionCount": 0,
      "math1Score": 4,
      "math2Score": 25,
      "math3Score": 17,
      "math1Percent": "0.16%",
      "math2Percent": "0.98%",
      "math3Percent": "0.67%",
      "avgDifficulty": "★★★☆☆"
    },
    "methodCards": [
      {
        "title": "连续、间断与零点定理 核心方法梳理",
        "subtitle": "涵盖 5 个进阶小节",
        "content": "本讲重点掌握 连续与分段函数定参数、间断点分类与计数（本讲主力）、由极限定义的函数、零点定理与介值定理：闭区间上连续函数的四大性质 等核心知识链路，严格对齐考研大纲要求与历年命题规律。"
      }
    ],
    "pitfalls": [
      "未看清本讲在三卷中的具体分值权重与适用标签（统考必考）。",
      "忽略定理适用的前提条件（如开闭区间、可导性、正交性或独立性前提）。"
    ],
    "mappedTopicIds": [
      "gaoshu-01-discontinuity-points"
    ]
  },
  {
    "id": "L08",
    "num": 8,
    "title": "导数与微分",
    "partNum": 1,
    "partTitle": "第 1 编 一元函数微积分",
    "page": 113,
    "pageEnd": 133,
    "isKey": false,
    "isCompressed": false,
    "isMath1Only": false,
    "isMath2Heavy": false,
    "isMath3Only": false,
    "isMethod": false,
    "tags": [
      "统考必考"
    ],
    "orientation": "17 年真题里本讲名下有12 道独立题、19 个卷面题位，数二占",
    "subsections": [
      "导数的定义及其三种变形",
      "够用的求导公式（读懂本讲真题就靠这些）",
      "可导与连续",
      "由极限条件反求导数（解答题的落点）",
      "微分",
      "本讲小结"
    ],
    "stats": {
      "independentQuestions": 12,
      "positions": 19,
      "choiceCount": 15,
      "blankCount": 1,
      "solutionCount": 3,
      "math1Score": 32,
      "math2Score": 42,
      "math3Score": 26,
      "math1Percent": "1.25%",
      "math2Percent": "1.65%",
      "math3Percent": "1.02%",
      "avgDifficulty": "★★★☆☆"
    },
    "methodCards": [
      {
        "title": "导数与微分 核心方法梳理",
        "subtitle": "涵盖 6 个进阶小节",
        "content": "本讲重点掌握 导数的定义及其三种变形、够用的求导公式（读懂本讲真题就靠这些）、可导与连续、由极限条件反求导数（解答题的落点） 等核心知识链路，严格对齐考研大纲要求与历年命题规律。"
      }
    ],
    "pitfalls": [
      "未看清本讲在三卷中的具体分值权重与适用标签（统考必考）。",
      "忽略定理适用的前提条件（如开闭区间、可导性、正交性或独立性前提）。"
    ],
    "mappedTopicIds": [
      "gaoshu-02-derivative-definition"
    ]
  },
  {
    "id": "L09",
    "num": 9,
    "title": "求导技术全家桶",
    "partNum": 1,
    "partTitle": "第 1 编 一元函数微积分",
    "page": 133,
    "pageEnd": 155,
    "isKey": true,
    "isCompressed": false,
    "isMath1Only": false,
    "isMath2Heavy": false,
    "isMath3Only": false,
    "isMethod": false,
    "tags": [
      "重点讲",
      "统考必考"
    ],
    "orientation": "全书填空题密度最高的一讲。17 年真题里本讲名下26 道独立题、28 个卷面题位，其 中25 个是填空、3 个选择，解答题一道都没有。分值上三卷差得极远：数二3.06%（78 分，平 均每年4.6 分），数一0.71%（18 分）、数三",
    "subsections": [
      "全家桶总览：六条法则与它们的真实权重",
      "复合函数一阶导：链式法则先落地",
      "隐函数一阶导：遇 y 就带出 y'",
      "参数方程一阶导：先反解 t，再套公式",
      "二阶导：参数式与隐函数（本讲主力）",
      "相关变化率",
      "高阶导与莱布尼茨公式",
      "本讲小结"
    ],
    "stats": {
      "independentQuestions": 26,
      "positions": 28,
      "choiceCount": 3,
      "blankCount": 25,
      "solutionCount": 0,
      "math1Score": 18,
      "math2Score": 78,
      "math3Score": 26,
      "math1Percent": "0.71%",
      "math2Percent": "3.06%",
      "math3Percent": "1.02%",
      "avgDifficulty": "★★★☆☆"
    },
    "methodCards": [
      {
        "title": "求导技术全家桶六条法则与真实权重",
        "subtitle": "手快手顺 · 一遍算对",
        "content": "复合函数一阶导（链式法则）、隐函数一阶导（遇y就带出y'）、参数方程一阶导（先反解t或直接除法）、二阶导（参数式与隐函数主力）、相关变化率、高阶导与莱布尼茨公式。"
      }
    ],
    "pitfalls": [
      "未看清本讲在三卷中的具体分值权重与适用标签（重点讲、统考必考）。",
      "忽略定理适用的前提条件（如开闭区间、可导性、正交性或独立性前提）。"
    ],
    "mappedTopicIds": [
      "gaoshu-02-higher-order-leibniz",
      "gaoshu-05-chain-rule-composite",
      "gaoshu-05-implicit-function-differentiation"
    ]
  },
  {
    "id": "L10",
    "num": 10,
    "title": "微分中值定理（一）",
    "partNum": 1,
    "partTitle": "第 1 编 一元函数微积分",
    "page": 155,
    "pageEnd": 177,
    "isKey": true,
    "isCompressed": false,
    "isMath1Only": false,
    "isMath2Heavy": false,
    "isMath3Only": false,
    "isMethod": false,
    "tags": [
      "重点讲",
      "统考必考"
    ],
    "orientation": "全书区分度最高的一讲，数据可以证明这一点。17 年真题里本讲名下只有9 道独立题， 却占了14 个卷面题位，而这14 个题位里12 个是解答题——本讲几乎不出选填（17 年里只有一 道选择、一道填空）。平均难度3.44，在全书107 个有真题的考点里排第12 高，而排在它前面 的11 个考点，解答题题位没有一个超过10 个，本讲有12 个——论“又难又常出大题”，本讲是 第一。分值：数二2.25%（每年3.4 分）、数一",
    "subsections": [
      "三个中值定理",
      "一条推理链：五步，每道题都走它",
      "第 3 步的门槛：先把点造出来",
      "套路一：逆用求导法则（真题第一主力）",
      "套路二：乘 ex（积分因子）",
      "套路三：乘幂函数 xk",
      "套路四：两次罗尔",
      "套路五：还原法（想不出来时的保底）",
      "复盘：构造总表",
      "两道不靠构造的硬题",
      "全讲最后一道：“双中值”综合题",
      "本讲小结"
    ],
    "stats": {
      "independentQuestions": 9,
      "positions": 14,
      "choiceCount": 1,
      "blankCount": 1,
      "solutionCount": 12,
      "math1Score": 43,
      "math2Score": 57,
      "math3Score": 37,
      "math1Percent": "1.69%",
      "math2Percent": "2.24%",
      "math3Percent": "1.45%",
      "avgDifficulty": "★★★★☆"
    },
    "methodCards": [
      {
        "title": "微分中值定理五大构造套路与构造总表",
        "subtitle": "机械化逆推 · 百分百构建罗尔辅助函数",
        "content": "套路一：逆用导数乘积法则；套路二：乘积分因子 e^{P(x)}；套路三：乘幂函数 x^k；套路四：两次罗尔推二阶导；套路五：积分还原法。"
      }
    ],
    "pitfalls": [
      "未看清本讲在三卷中的具体分值权重与适用标签（重点讲、统考必考）。",
      "忽略定理适用的前提条件（如开闭区间、可导性、正交性或独立性前提）。"
    ],
    "mappedTopicIds": [
      "gaoshu-02-mean-value-theorems"
    ]
  },
  {
    "id": "L11",
    "num": 11,
    "title": "极限计算总攻略（一）：洛必达与未定式",
    "partNum": 1,
    "partTitle": "第 1 编 一元函数微积分",
    "page": 177,
    "pageEnd": 189,
    "isKey": false,
    "isCompressed": false,
    "isMath1Only": false,
    "isMath2Heavy": false,
    "isMath3Only": false,
    "isMethod": false,
    "tags": [
      "统考必考"
    ],
    "orientation": "本讲5 道独立题、9 个卷面题位，其中3 个是解答题位。分值三卷完全持平：数",
    "subsections": [
      "七种未定式",
      "洛必达法则",
      "初等手段：五个动作",
      "反问题：由极限定参数（本讲主体）",
      "本讲小结"
    ],
    "stats": {
      "independentQuestions": 5,
      "positions": 9,
      "choiceCount": 5,
      "blankCount": 1,
      "solutionCount": 3,
      "math1Score": 18,
      "math2Score": 18,
      "math3Score": 18,
      "math1Percent": "0.71%",
      "math2Percent": "0.71%",
      "math3Percent": "0.71%",
      "avgDifficulty": "★★★☆☆"
    },
    "methodCards": [
      {
        "title": "极限计算总攻略（一）：洛必达与未定式 核心方法梳理",
        "subtitle": "涵盖 5 个进阶小节",
        "content": "本讲重点掌握 七种未定式、洛必达法则、初等手段：五个动作、反问题：由极限定参数（本讲主体） 等核心知识链路，严格对齐考研大纲要求与历年命题规律。"
      }
    ],
    "pitfalls": [
      "未看清本讲在三卷中的具体分值权重与适用标签（统考必考）。",
      "忽略定理适用的前提条件（如开闭区间、可导性、正交性或独立性前提）。"
    ],
    "mappedTopicIds": [
      "gaoshu-01-indeterminate-0-0",
      "gaoshu-01-difference-inf-inf"
    ]
  },
  {
    "id": "L12",
    "num": 12,
    "title": "微分中值定理（二）：泰勒公式",
    "partNum": 1,
    "partTitle": "第 1 编 一元函数微积分",
    "page": 189,
    "pageEnd": 201,
    "isKey": false,
    "isCompressed": true,
    "isMath1Only": false,
    "isMath2Heavy": false,
    "isMath3Only": false,
    "isMethod": false,
    "tags": [
      "压缩讲",
      "统考必考"
    ],
    "orientation": "题量很小，但每一题都很贵：17 年51 套卷里本讲名下只有3 道独立题、5 个卷面题 位（3 个解答、2 个选择），平均难度2.67。分值：数",
    "subsections": [
      "第一块：求指定阶的泰勒多项式",
      "第二块：用带余项的泰勒公式证明中值等式",
      "边界说明：本讲讲的是有限阶",
      "本讲小结"
    ],
    "stats": {
      "independentQuestions": 3,
      "positions": 5,
      "choiceCount": 2,
      "blankCount": 0,
      "solutionCount": 3,
      "math1Score": 17,
      "math2Score": 17,
      "math3Score": 12,
      "math1Percent": "0.67%",
      "math2Percent": "0.67%",
      "math3Percent": "0.47%",
      "avgDifficulty": "★★☆☆☆"
    },
    "methodCards": [
      {
        "title": "微分中值定理（二）：泰勒公式 核心方法梳理",
        "subtitle": "涵盖 4 个进阶小节",
        "content": "本讲重点掌握 第一块：求指定阶的泰勒多项式、第二块：用带余项的泰勒公式证明中值等式、边界说明：本讲讲的是有限阶、本讲小结 等核心知识链路，严格对齐考研大纲要求与历年命题规律。"
      }
    ],
    "pitfalls": [
      "未看清本讲在三卷中的具体分值权重与适用标签（压缩讲、统考必考）。",
      "忽略定理适用的前提条件（如开闭区间、可导性、正交性或独立性前提）。"
    ],
    "mappedTopicIds": [
      "gaoshu-02-taylor-formula-proof"
    ]
  },
  {
    "id": "L13",
    "num": 13,
    "title": "极限计算总攻略（二）：泰勒展开",
    "partNum": 1,
    "partTitle": "第 1 编 一元函数微积分",
    "page": 201,
    "pageEnd": 225,
    "isKey": true,
    "isCompressed": false,
    "isMath1Only": false,
    "isMath2Heavy": false,
    "isMath3Only": false,
    "isMethod": false,
    "tags": [
      "重点讲",
      "统考必考"
    ],
    "orientation": "整个极限板块最大的一讲，没有之一。本讲27 道独立题、35 个卷面题位，其中12 个 解答、12 个选择、11 个填空——L03 到L13 十一讲加起来的解答题位，有一半在这里。平均难度 2.78。 分值也压倒性：数三4.01%（102 分，全书第8）、数二3.45%（88 分，全书第11）、数一",
    "subsections": [
      "为什么必须是泰勒",
      "工具：有限阶麦克劳林公式",
      "第一段：展开到几阶",
      "第二段：复合式与抵消",
      "第三段：幂指型",
      "第四段：x 先换元 t=1x",
      "第五段：定阶与反求参数",
      "第六段：有限阶系数与低阶导数",
      "路线选择",
      "本讲小结"
    ],
    "stats": {
      "independentQuestions": 27,
      "positions": 35,
      "choiceCount": 12,
      "blankCount": 11,
      "solutionCount": 12,
      "math1Score": 42,
      "math2Score": 88,
      "math3Score": 102,
      "math1Percent": "1.65%",
      "math2Percent": "3.45%",
      "math3Percent": "4.00%",
      "avgDifficulty": "★★★★☆"
    },
    "methodCards": [
      {
        "title": "泰勒展开极限攻略核心准则",
        "subtitle": "展开到几阶 · 上下齐阶 · 复合式展开",
        "content": "分母为 x^k 则分子所有加减项统一展开到 x^k+o(x^k)；遇复杂幂指型先化为 e^{g(x)ln f(x)} 后再展开；严禁加减项部分等价替换而部分展开。"
      }
    ],
    "pitfalls": [
      "未看清本讲在三卷中的具体分值权重与适用标签（重点讲、统考必考）。",
      "忽略定理适用的前提条件（如开闭区间、可导性、正交性或独立性前提）。"
    ],
    "mappedTopicIds": [
      "gaoshu-01-indeterminate-0-0",
      "gaoshu-10-cross-taylor-proofs"
    ]
  },
  {
    "id": "L14",
    "num": 14,
    "title": "导数的应用",
    "partNum": 1,
    "partTitle": "第 1 编 一元函数微积分",
    "page": 225,
    "pageEnd": 249,
    "isKey": true,
    "isCompressed": false,
    "isMath1Only": false,
    "isMath2Heavy": false,
    "isMath3Only": false,
    "isMethod": false,
    "tags": [
      "重点讲",
      "统考必考"
    ],
    "orientation": "微分学里题位最多的一讲：36 道独立题、51 个卷面题位。数二占5.98%（平均每年 9.0 分），数三2.37%（3.6 分），数一",
    "subsections": [
      "单调性与极值（解答题的产地）",
      "凹凸与拐点（选择题的产地）",
      "渐近线",
      "曲率",
      "全讲最后一道：曲率圆（综合）",
      "导数的经济语言（数三的铺垫）",
      "本讲小结"
    ],
    "stats": {
      "independentQuestions": 36,
      "positions": 51,
      "choiceCount": 31,
      "blankCount": 13,
      "solutionCount": 7,
      "math1Score": 48,
      "math2Score": 152,
      "math3Score": 60,
      "math1Percent": "1.88%",
      "math2Percent": "5.96%",
      "math3Percent": "2.35%",
      "avgDifficulty": "★★★★☆"
    },
    "methodCards": [
      {
        "title": "导数的应用 核心方法梳理",
        "subtitle": "涵盖 7 个进阶小节",
        "content": "本讲重点掌握 单调性与极值（解答题的产地）、凹凸与拐点（选择题的产地）、渐近线、曲率 等核心知识链路，严格对齐考研大纲要求与历年命题规律。"
      }
    ],
    "pitfalls": [
      "未看清本讲在三卷中的具体分值权重与适用标签（重点讲、统考必考）。",
      "忽略定理适用的前提条件（如开闭区间、可导性、正交性或独立性前提）。"
    ],
    "mappedTopicIds": [
      "gaoshu-02-inequality-and-roots"
    ]
  },
  {
    "id": "L15",
    "num": 15,
    "title": "不等式证明与方程根的个数",
    "partNum": 1,
    "partTitle": "第 1 编 一元函数微积分",
    "page": 249,
    "pageEnd": 269,
    "isKey": false,
    "isCompressed": false,
    "isMath1Only": false,
    "isMath2Heavy": false,
    "isMath3Only": false,
    "isMethod": false,
    "tags": [
      "统考必考"
    ],
    "orientation": "微分学部分的收尾讲，不引入新知识，而是把L07、L10–L14 的工具组织成两套决策 流程。17 年真题里9 道独立题、12 个卷面题位，12 个题位里8 个是解答题，平均难度3.44—— 分不算多（三卷占比最高只有",
    "subsections": [
      "方程的根：四级递进",
      "不等式证明：四条路线",
      "本讲小结"
    ],
    "stats": {
      "independentQuestions": 9,
      "positions": 12,
      "choiceCount": 4,
      "blankCount": 0,
      "solutionCount": 8,
      "math1Score": 21,
      "math2Score": 40,
      "math3Score": 40,
      "math1Percent": "0.82%",
      "math2Percent": "1.57%",
      "math3Percent": "1.57%",
      "avgDifficulty": "★★★★☆"
    },
    "methodCards": [
      {
        "title": "不等式证明与方程根的个数 核心方法梳理",
        "subtitle": "涵盖 3 个进阶小节",
        "content": "本讲重点掌握 方程的根：四级递进、不等式证明：四条路线、本讲小结 等核心知识链路，严格对齐考研大纲要求与历年命题规律。"
      }
    ],
    "pitfalls": [
      "未看清本讲在三卷中的具体分值权重与适用标签（统考必考）。",
      "忽略定理适用的前提条件（如开闭区间、可导性、正交性或独立性前提）。"
    ],
    "mappedTopicIds": [
      "gaoshu-02-inequality-and-roots"
    ]
  },
  {
    "id": "L16",
    "num": 16,
    "title": "不定积分：换元与分部的决策树",
    "partNum": 1,
    "partTitle": "第 1 编 一元函数微积分",
    "page": 269,
    "pageEnd": 287,
    "isKey": false,
    "isCompressed": false,
    "isMath1Only": false,
    "isMath2Heavy": false,
    "isMath3Only": false,
    "isMethod": false,
    "tags": [
      "统考必考"
    ],
    "orientation": "17 年真题里本讲名下只有6 道独立题、10 个卷面题位，数一18 分、数二23 分、数 三19 分——折算下来平均每年从这一讲直接拿走1 分出头。但这一讲不能按1 分来投入：L18 到 L22 的每一道积分题，最后都要落回这里的手上功夫，真题里它是“中间步骤”而不是“题目”。 真正值得注意的是这6 道题的构成。3 道计算题（2011 数三17、2018 数一／数二15、2018 数三10）是同一个模子：反三角函数（或对数）套在一个根式／指数外面，先换元把根号和指数 换干净，再分部。另外2 道考的是分段函数的原函数（2016 数一／数二2、2023 数二／数三2， 都跨两卷），这类题跟“怎么积”关系不大，考的是原函数必须连续。剩下1 道是“反着积”：由 f′ 的表达式积回f，再靠奇偶性定常数（2014 数一／数二10）。",
    "subsections": [
      "原函数与不定积分：先把两个词分清",
      "基本积分表（必须默写）",
      "决策树：先看结构，再动笔算",
      "第一类换元：凑微分",
      "第二类换元：设新变量",
      "分部积分",
      "分段函数的原函数（决策树第 1 步，真题占近三分之一）",
      "本讲小结"
    ],
    "stats": {
      "independentQuestions": 6,
      "positions": 10,
      "choiceCount": 4,
      "blankCount": 3,
      "solutionCount": 3,
      "math1Score": 18,
      "math2Score": 23,
      "math3Score": 19,
      "math1Percent": "0.71%",
      "math2Percent": "0.90%",
      "math3Percent": "0.75%",
      "avgDifficulty": "★★★☆☆"
    },
    "methodCards": [
      {
        "title": "不定积分换元与分部决策树",
        "subtitle": "动笔前先看结构",
        "content": "决策树四步：1. 分段函数找分界点；2. 凑微分（第一类换元）；3. 根式与三角代换（第二类换元）；4. 反对幂指三分部积分法。"
      }
    ],
    "pitfalls": [
      "未看清本讲在三卷中的具体分值权重与适用标签（统考必考）。",
      "忽略定理适用的前提条件（如开闭区间、可导性、正交性或独立性前提）。"
    ],
    "mappedTopicIds": [
      "gaoshu-03-variable-limit-integral"
    ]
  },
  {
    "id": "L17",
    "num": 17,
    "title": "三类特殊函数的积分",
    "partNum": 1,
    "partTitle": "第 1 编 一元函数微积分",
    "page": 287,
    "pageEnd": 293,
    "isKey": false,
    "isCompressed": true,
    "isMath1Only": false,
    "isMath2Heavy": false,
    "isMath3Only": false,
    "isMethod": false,
    "tags": [
      "压缩讲",
      "统考必考"
    ],
    "orientation": "全书最该压缩的一讲。2010–2026 年51 套卷、1155 个卷面题位里，本讲名下只有1 道题：2019 数二16（有理函数不定积分）。数一0 分、数三0 分、数二17 年合计10 分，占数二 卷面总分的0.41%——平均下来，数二每17 年才在这里出一道题，数一数三的考生17 年里一次 都没遇到过。 所以本讲只有一道完整例题（习题17.1），也只需要一道。但也不能整讲跳过，理由很具体： “部 分分式分解”这个动作在846 道真题的详解里出现了12 次，其中只有1 次是拿它本身命题（就 是本讲这道），另外11 次全是别的题的中间步骤——6 次在反常积分（L20），2 次在定积分计算 （L19），其余散在定积分应用、幂级数与随机变量函数的分布里。本讲的正确身份是一页工具：会 拆、拆得快即可，不要当成一个考点去攻。",
    "subsections": [
      "有理函数（本讲唯一要留的一节）",
      "两张方法卡",
      "本讲小结"
    ],
    "stats": {
      "independentQuestions": 1,
      "positions": 1,
      "choiceCount": 0,
      "blankCount": 0,
      "solutionCount": 1,
      "math1Score": 0,
      "math2Score": 10,
      "math3Score": 0,
      "math1Percent": "0.00%",
      "math2Percent": "0.39%",
      "math3Percent": "0.00%",
      "avgDifficulty": "★★☆☆☆"
    },
    "methodCards": [
      {
        "title": "三类特殊函数的积分 核心方法梳理",
        "subtitle": "涵盖 3 个进阶小节",
        "content": "本讲重点掌握 有理函数（本讲唯一要留的一节）、两张方法卡、本讲小结 等核心知识链路，严格对齐考研大纲要求与历年命题规律。"
      }
    ],
    "pitfalls": [
      "未看清本讲在三卷中的具体分值权重与适用标签（压缩讲、统考必考）。",
      "忽略定理适用的前提条件（如开闭区间、可导性、正交性或独立性前提）。"
    ],
    "mappedTopicIds": [
      "gaoshu-03-variable-limit-integral"
    ]
  },
  {
    "id": "L18",
    "num": 18,
    "title": "定积分：定义、性质与变限积分",
    "partNum": 1,
    "partTitle": "第 1 编 一元函数微积分",
    "page": 293,
    "pageEnd": 325,
    "isKey": true,
    "isCompressed": false,
    "isMath1Only": false,
    "isMath2Heavy": false,
    "isMath3Only": false,
    "isMethod": false,
    "tags": [
      "重点讲",
      "统考必考"
    ],
    "orientation": "全书体量最大的两讲之一。17 年真题里本讲名下有51 道独立题、81 个卷面题位—— 题位数排全书第一，独立题数仅次于L33 二重积分。数二占卷面总分的10.33%（264 分，平均 每年15.5 分）、数一5.70%（145 分，每年8.5 分）、数三5.59%（142 分，每年8.4 分）。三卷 都排在本编前列，数二更是仅次于L33 二重积分的第二大讲，这一讲没有任何取巧的余地。 本讲下挂三个考点，体量与题型都不一样，必须分开对待： 考点 独立／题位 题型 数一／二／三分 难度 18.1 定积分的概念与性质 16 ／29 选18 填4 解7 59 ／73 ／43 2.81 18.2 定积分",
    "subsections": [
      "（一）定积分的概念、性质与比较",
      "（二）奇偶性、周期性与平均值",
      "（三）黎曼和的识别：定积分定义求极限",
      "（四）变限积分的基本求导",
      "（五）复合上限与被积函数含参数：先把参数提出积分号",
      "（六）综合：变限积分接极限、极值、零点与证明",
      "本讲小结"
    ],
    "stats": {
      "independentQuestions": 51,
      "positions": 81,
      "choiceCount": 34,
      "blankCount": 17,
      "solutionCount": 30,
      "math1Score": 145,
      "math2Score": 264,
      "math3Score": 142,
      "math1Percent": "5.69%",
      "math2Percent": "10.35%",
      "math3Percent": "5.57%",
      "avgDifficulty": "★★★★☆"
    },
    "methodCards": [
      {
        "title": "定积分：定义、性质与变限积分 核心方法梳理",
        "subtitle": "涵盖 7 个进阶小节",
        "content": "本讲重点掌握 （一）定积分的概念、性质与比较、（二）奇偶性、周期性与平均值、（三）黎曼和的识别：定积分定义求极限、（四）变限积分的基本求导 等核心知识链路，严格对齐考研大纲要求与历年命题规律。"
      }
    ],
    "pitfalls": [
      "未看清本讲在三卷中的具体分值权重与适用标签（重点讲、统考必考）。",
      "忽略定理适用的前提条件（如开闭区间、可导性、正交性或独立性前提）。"
    ],
    "mappedTopicIds": [
      "gaoshu-03-variable-limit-integral",
      "gaoshu-03-definite-integral-symmetry"
    ]
  },
  {
    "id": "L19",
    "num": 19,
    "title": "定积分的计算技巧",
    "partNum": 1,
    "partTitle": "第 1 编 一元函数微积分",
    "page": 325,
    "pageEnd": 341,
    "isKey": false,
    "isCompressed": false,
    "isMath1Only": false,
    "isMath2Heavy": false,
    "isMath3Only": false,
    "isMethod": false,
    "tags": [
      "统考必考"
    ],
    "orientation": "填空题的主场。17 年真题里本讲名下15 道独立题、19 个卷面题位，其中12 个是填 空、1 个选择、6 个解答；数一44 分（",
    "subsections": [
      "方法选择表（动笔前先看这张表）",
      "基本计算：换元与分部",
      "区间变换：对称性、周期性与“直接读面积”",
      "二次三项式：配方后的两条路线",
      "函数方程 + 区间平移（基本计算之后的第一道综合）",
      "平均值与“由积分值定参数”",
      "区间再现与华里士公式",
      "全讲最后一道：积分递推数列（本讲唯一的四星）",
      "本讲小结"
    ],
    "stats": {
      "independentQuestions": 15,
      "positions": 19,
      "choiceCount": 1,
      "blankCount": 12,
      "solutionCount": 6,
      "math1Score": 44,
      "math2Score": 40,
      "math3Score": 40,
      "math1Percent": "1.73%",
      "math2Percent": "1.57%",
      "math3Percent": "1.57%",
      "avgDifficulty": "★★★★☆"
    },
    "methodCards": [
      {
        "title": "定积分方法选择表与华里士区间再现",
        "subtitle": "区间变换 · 对称性 · 直接读面积",
        "content": "对称区间奇零偶倍；对称区间再现公式 ∫_0^π x f(sin x)dx = (π/2)∫_0^π f(sin x)dx；华里士点火公式计算 sin^n x 定积分。"
      }
    ],
    "pitfalls": [
      "未看清本讲在三卷中的具体分值权重与适用标签（统考必考）。",
      "忽略定理适用的前提条件（如开闭区间、可导性、正交性或独立性前提）。"
    ],
    "mappedTopicIds": [
      "gaoshu-03-definite-integral-symmetry"
    ]
  },
  {
    "id": "L20",
    "num": 20,
    "title": "反常积分",
    "partNum": 1,
    "partTitle": "第 1 编 一元函数微积分",
    "page": 341,
    "pageEnd": 355,
    "isKey": false,
    "isCompressed": false,
    "isMath1Only": false,
    "isMath2Heavy": false,
    "isMath3Only": false,
    "isMethod": false,
    "tags": [
      "统考必考"
    ],
    "orientation": "几乎只在选择题和填空题里出现的考点。17 年真题里本讲名下22 道独立题、26 个卷 面题位，10 选、15 填，解答题只有1 个题位（2013 数一15）——2010–2026 年没有哪一卷把 “判敛散”单独出成大题。这个事实决定了本讲的学法：要的是一眼判对、算对，不需要写得漂亮。 三卷的差距在这一讲被拉到最大：数二66 分（2.59%，平均每年3.9 分），数一32 分（",
    "subsections": [
      "第一步：找出所有瑕点，把积分拆开",
      "基准积分：两种 p 积分",
      "比较判别法与它的极限形式",
      "含参数：每段各出一个不等式，答案取交集",
      "计算：13 道题只有两个模子",
      "命题辨析型（近年新增，本讲唯一的四星）",
      "本讲小结"
    ],
    "stats": {
      "independentQuestions": 22,
      "positions": 26,
      "choiceCount": 10,
      "blankCount": 15,
      "solutionCount": 1,
      "math1Score": 32,
      "math2Score": 66,
      "math3Score": 24,
      "math1Percent": "1.25%",
      "math2Percent": "2.59%",
      "math3Percent": "0.94%",
      "avgDifficulty": "★★★☆☆"
    },
    "methodCards": [
      {
        "title": "反常积分 核心方法梳理",
        "subtitle": "涵盖 7 个进阶小节",
        "content": "本讲重点掌握 第一步：找出所有瑕点，把积分拆开、基准积分：两种 p 积分、比较判别法与它的极限形式、含参数：每段各出一个不等式，答案取交集 等核心知识链路，严格对齐考研大纲要求与历年命题规律。"
      }
    ],
    "pitfalls": [
      "未看清本讲在三卷中的具体分值权重与适用标签（统考必考）。",
      "忽略定理适用的前提条件（如开闭区间、可导性、正交性或独立性前提）。"
    ],
    "mappedTopicIds": [
      "gaoshu-03-improper-integral-convergence"
    ]
  },
  {
    "id": "L21",
    "num": 21,
    "title": "定积分的几何应用",
    "partNum": 1,
    "partTitle": "第 1 编 一元函数微积分",
    "page": 355,
    "pageEnd": 375,
    "isKey": true,
    "isCompressed": false,
    "isMath1Only": false,
    "isMath2Heavy": false,
    "isMath3Only": false,
    "isMethod": false,
    "tags": [
      "重点讲",
      "统考必考"
    ],
    "orientation": "二重数二的大讲之一，也是全书分卷差距最悬殊的一讲。17 年真题里本讲名下有21 道独立题、24 个卷面题位，数二独占16 个题位、147 分，占数二卷面总分的5.77%——排在L33、 L18、L14 之后，平均每年8.7 分。数三7 个题位、",
    "subsections": [
      "微元法：先画微元，再写公式",
      "面积",
      "体积",
      "弧长",
      "旋转曲面面积",
      "本讲小结"
    ],
    "stats": {
      "independentQuestions": 21,
      "positions": 24,
      "choiceCount": 0,
      "blankCount": 9,
      "solutionCount": 15,
      "math1Score": 4,
      "math2Score": 147,
      "math3Score": 51,
      "math1Percent": "0.16%",
      "math2Percent": "5.76%",
      "math3Percent": "2.00%",
      "avgDifficulty": "★★★★☆"
    },
    "methodCards": [
      {
        "title": "定积分的几何应用 核心方法梳理",
        "subtitle": "涵盖 6 个进阶小节",
        "content": "本讲重点掌握 微元法：先画微元，再写公式、面积、体积、弧长 等核心知识链路，严格对齐考研大纲要求与历年命题规律。"
      }
    ],
    "pitfalls": [
      "未看清本讲在三卷中的具体分值权重与适用标签（重点讲、统考必考）。",
      "忽略定理适用的前提条件（如开闭区间、可导性、正交性或独立性前提）。"
    ],
    "mappedTopicIds": [
      "gaoshu-03-geometric-applications"
    ]
  },
  {
    "id": "L22",
    "num": 22,
    "title": "定积分的物理与经济应用",
    "partNum": 1,
    "partTitle": "第 1 编 一元函数微积分",
    "page": 375,
    "pageEnd": 391,
    "isKey": false,
    "isCompressed": false,
    "isMath1Only": false,
    "isMath2Heavy": false,
    "isMath3Only": false,
    "isMethod": false,
    "tags": [
      "统考必考"
    ],
    "orientation": "这一讲名义上是一讲，实际上是互不相干的两讲，而且各归各卷。17 年真题里本讲有 11 道独立题、11 个卷面题位，分属两个考点： 考点 内容 数一 数二 数三 题位（选/填/解） 22.1 物理应用：功、压力、引力（质心见L33）0 分 24 分 0 分 4（2/1/1） 22.2 经济应用：边际与弹性 0 分 0 分 42 分 7（1/4/2） 物理应用的4 道题全部出自数二，经济应用的7 道题全部出自数三，两边都没有一道交叉。合起 来数二0.96%（每年",
    "subsections": [
      "物理应用",
      "经济应用",
      "本讲小结"
    ],
    "stats": {
      "independentQuestions": 11,
      "positions": 11,
      "choiceCount": 3,
      "blankCount": 5,
      "solutionCount": 3,
      "math1Score": 0,
      "math2Score": 24,
      "math3Score": 42,
      "math1Percent": "0.00%",
      "math2Percent": "0.94%",
      "math3Percent": "1.65%",
      "avgDifficulty": "★★★☆☆"
    },
    "methodCards": [
      {
        "title": "定积分的物理与经济应用 核心方法梳理",
        "subtitle": "涵盖 3 个进阶小节",
        "content": "本讲重点掌握 物理应用、经济应用、本讲小结 等核心知识链路，严格对齐考研大纲要求与历年命题规律。"
      }
    ],
    "pitfalls": [
      "未看清本讲在三卷中的具体分值权重与适用标签（统考必考）。",
      "忽略定理适用的前提条件（如开闭区间、可导性、正交性或独立性前提）。"
    ],
    "mappedTopicIds": [
      "gaoshu-03-geometric-applications"
    ]
  },
  {
    "id": "L23",
    "num": 23,
    "title": "第一编串讲：积分等式与不等式的证明",
    "partNum": 1,
    "partTitle": "第 1 编 一元函数微积分",
    "page": 391,
    "pageEnd": 407,
    "isKey": false,
    "isCompressed": false,
    "isMath1Only": false,
    "isMath2Heavy": false,
    "isMath3Only": false,
    "isMethod": false,
    "tags": [
      "统考必考"
    ],
    "orientation": "本讲做两件事。第一件：讲一个考点——本讲名下只挂着23.1「积分等式与积分不等 式的证明」，它17 年只出过2 道独立题，但5 个卷面题位全部是解答题，平均难度4.0，是全书 118 个考点里唯一一个满4.0 的。第二件：给出第1 编21 讲的真题优先级表——按2010–2026 的实际分值排序，告诉你时间该往哪里投、哪几讲可以轻放。结论必须按卷分开给，因为三卷的 答案很不一样。 本讲不教新知识。两道真题用的每一件工具你都已经学过：被积函数的初等不等式在L15、构 造辅助函数在L10、变限积分求导在L18。这里做的是把它们串成两条固定路线。",
    "subsections": [
      "两条总路线",
      "第 1 编优先级表（按真题分值）",
      "复盘速查：做完题再回头看",
      "本讲小结"
    ],
    "stats": {
      "independentQuestions": 2,
      "positions": 5,
      "choiceCount": 0,
      "blankCount": 0,
      "solutionCount": 5,
      "math1Score": 10,
      "math2Score": 21,
      "math3Score": 21,
      "math1Percent": "0.39%",
      "math2Percent": "0.82%",
      "math3Percent": "0.82%",
      "avgDifficulty": "★★☆☆☆"
    },
    "methodCards": [
      {
        "title": "第一编串讲：积分等式与不等式的证明 核心方法梳理",
        "subtitle": "涵盖 4 个进阶小节",
        "content": "本讲重点掌握 两条总路线、第 1 编优先级表（按真题分值）、复盘速查：做完题再回头看、本讲小结 等核心知识链路，严格对齐考研大纲要求与历年命题规律。"
      }
    ],
    "pitfalls": [
      "未看清本讲在三卷中的具体分值权重与适用标签（统考必考）。",
      "忽略定理适用的前提条件（如开闭区间、可导性、正交性或独立性前提）。"
    ],
    "mappedTopicIds": [
      "gaoshu-03-variable-limit-integral",
      "gaoshu-03-definite-integral-symmetry"
    ]
  },
  {
    "id": "L24",
    "num": 24,
    "title": "一阶微分方程",
    "partNum": 2,
    "partTitle": "第 2 编 常微分方程与差分方程",
    "page": 407,
    "pageEnd": 435,
    "isKey": false,
    "isCompressed": false,
    "isMath1Only": false,
    "isMath2Heavy": false,
    "isMath3Only": false,
    "isMethod": false,
    "tags": [
      "统考必考"
    ],
    "orientation": "本编分值最均衡的一讲。17 年真题里本讲名下有19 道独立题、24 个卷面题位，三卷 分值都在",
    "subsections": [
      "基本概念",
      "类型识别：拿到方程先问哪一句",
      "直接求解：可分离与一阶线性",
      "初值问题：通解之后怎么定常数",
      "其余两类与“四步都不像”的两条出路",
      "积分方程：一阶方程最常见的包装",
      "由特解反求方程（解的结构在这里用）",
      "综合接口：解完之后的那一问",
      "本讲小结"
    ],
    "stats": {
      "independentQuestions": 19,
      "positions": 24,
      "choiceCount": 3,
      "blankCount": 10,
      "solutionCount": 11,
      "math1Score": 54,
      "math2Score": 76,
      "math3Score": 46,
      "math1Percent": "2.12%",
      "math2Percent": "2.98%",
      "math3Percent": "1.80%",
      "avgDifficulty": "★★★★☆"
    },
    "methodCards": [
      {
        "title": "一阶微分方程 核心方法梳理",
        "subtitle": "涵盖 9 个进阶小节",
        "content": "本讲重点掌握 基本概念、类型识别：拿到方程先问哪一句、直接求解：可分离与一阶线性、初值问题：通解之后怎么定常数 等核心知识链路，严格对齐考研大纲要求与历年命题规律。"
      }
    ],
    "pitfalls": [
      "未看清本讲在三卷中的具体分值权重与适用标签（统考必考）。",
      "忽略定理适用的前提条件（如开闭区间、可导性、正交性或独立性前提）。"
    ],
    "mappedTopicIds": [
      "gaoshu-04-first-order-ode"
    ]
  },
  {
    "id": "L25",
    "num": 25,
    "title": "可降阶方程与二阶常系数线性方程",
    "partNum": 2,
    "partTitle": "第 2 编 常微分方程与差分方程",
    "page": 435,
    "pageEnd": 459,
    "isKey": true,
    "isCompressed": false,
    "isMath1Only": false,
    "isMath2Heavy": false,
    "isMath3Only": false,
    "isMethod": false,
    "tags": [
      "重点讲",
      "统考必考"
    ],
    "orientation": "17 年真题里本讲名下有23 道独立题、28 个卷面题位——本编题位最多的一讲，数二 3.62%（本编第一）、数一",
    "subsections": [
      "特征方程与三种根：先把通解写顺",
      "非齐次：特解形式识别",
      "由解反求方程，与解的结构",
      "后半场：特征根决定解的整体行为",
      "可降阶的高阶方程（数一数二的考纲内容，数三不考）",
      "本讲小结"
    ],
    "stats": {
      "independentQuestions": 23,
      "positions": 28,
      "choiceCount": 10,
      "blankCount": 10,
      "solutionCount": 8,
      "math1Score": 46,
      "math2Score": 92,
      "math3Score": 32,
      "math1Percent": "1.80%",
      "math2Percent": "3.61%",
      "math3Percent": "1.25%",
      "avgDifficulty": "★★★★☆"
    },
    "methodCards": [
      {
        "title": "二阶常系数线性微分方程解法全表",
        "subtitle": "特征方程三种根 · 待定系数特解设法",
        "content": "特征根 r1!=r2、r1=r2 二重根、一对共轭复根 α±iβ 对应的三种齐次通解形式；非齐次项 Pm(x)e^{λx} 与 e^{λx}[Pl cos ωx + Qn sin ωx] 的设特解原则。"
      }
    ],
    "pitfalls": [
      "未看清本讲在三卷中的具体分值权重与适用标签（重点讲、统考必考）。",
      "忽略定理适用的前提条件（如开闭区间、可导性、正交性或独立性前提）。"
    ],
    "mappedTopicIds": [
      "gaoshu-04-second-order-constant-coeff",
      "gaoshu-04-reducible-ode"
    ]
  },
  {
    "id": "L26",
    "num": 26,
    "title": "高阶线性与欧拉方程／差分方程",
    "partNum": 2,
    "partTitle": "第 2 编 常微分方程与差分方程",
    "page": 459,
    "pageEnd": 469,
    "isKey": false,
    "isCompressed": false,
    "isMath1Only": false,
    "isMath2Heavy": false,
    "isMath3Only": false,
    "isMethod": false,
    "tags": [
      "统考必考"
    ],
    "orientation": "本编最该压缩的一讲。17 年真题里本讲名下只有8 道独立题、8 个卷面题位（数一 0.20%、数三0.51%、数二",
    "subsections": [
      "线性方程解的结构",
      "高阶常系数线性方程",
      "欧拉方程",
      "差分方程",
      "本讲小结"
    ],
    "stats": {
      "independentQuestions": 8,
      "positions": 8,
      "choiceCount": 0,
      "blankCount": 7,
      "solutionCount": 1,
      "math1Score": 5,
      "math2Score": 26,
      "math3Score": 13,
      "math1Percent": "0.20%",
      "math2Percent": "1.02%",
      "math3Percent": "0.51%",
      "avgDifficulty": "★★★☆☆"
    },
    "methodCards": [
      {
        "title": "高阶线性与欧拉方程／差分方程 核心方法梳理",
        "subtitle": "涵盖 5 个进阶小节",
        "content": "本讲重点掌握 线性方程解的结构、高阶常系数线性方程、欧拉方程、差分方程 等核心知识链路，严格对齐考研大纲要求与历年命题规律。"
      }
    ],
    "pitfalls": [
      "未看清本讲在三卷中的具体分值权重与适用标签（统考必考）。",
      "忽略定理适用的前提条件（如开闭区间、可导性、正交性或独立性前提）。"
    ],
    "mappedTopicIds": [
      "gaoshu-04-euler-equation"
    ]
  },
  {
    "id": "L27",
    "num": 27,
    "title": "微分方程应用题",
    "partNum": 2,
    "partTitle": "第 2 编 常微分方程与差分方程",
    "page": 469,
    "pageEnd": 491,
    "isKey": false,
    "isCompressed": false,
    "isMath1Only": false,
    "isMath2Heavy": false,
    "isMath3Only": false,
    "isMethod": false,
    "tags": [
      "统考必考"
    ],
    "orientation": "题最少、单题最贵的一讲。17 年真题只有10 道独立题、11 个卷面题位，但11 个题 位里9 个是解答题（10–12 分一道），平均难度3.1——本编四讲里最高。分值：数二",
    "subsections": [
      "通用建模四步",
      "几何应用（数一数二的全部分数）",
      "变限积分方程",
      "物理应用",
      "经济应用：把弹性式读成微分方程",
      "本讲小结"
    ],
    "stats": {
      "independentQuestions": 10,
      "positions": 11,
      "choiceCount": 0,
      "blankCount": 2,
      "solutionCount": 9,
      "math1Score": 33,
      "math2Score": 43,
      "math3Score": 30,
      "math1Percent": "1.29%",
      "math2Percent": "1.69%",
      "math3Percent": "1.18%",
      "avgDifficulty": "★★★★☆"
    },
    "methodCards": [
      {
        "title": "微分方程应用题 核心方法梳理",
        "subtitle": "涵盖 6 个进阶小节",
        "content": "本讲重点掌握 通用建模四步、几何应用（数一数二的全部分数）、变限积分方程、物理应用 等核心知识链路，严格对齐考研大纲要求与历年命题规律。"
      }
    ],
    "pitfalls": [
      "未看清本讲在三卷中的具体分值权重与适用标签（统考必考）。",
      "忽略定理适用的前提条件（如开闭区间、可导性、正交性或独立性前提）。"
    ],
    "mappedTopicIds": [
      "gaoshu-04-first-order-ode",
      "gaoshu-04-second-order-constant-coeff"
    ]
  },
  {
    "id": "L28",
    "num": 28,
    "title": "向量代数与空间解析几何",
    "partNum": 3,
    "partTitle": "第 3 编 多元函数微积分",
    "page": 491,
    "pageEnd": 495,
    "isKey": false,
    "isCompressed": false,
    "isMath1Only": true,
    "isMath2Heavy": false,
    "isMath3Only": false,
    "isMethod": true,
    "tags": [
      "方法课",
      "数一专属"
    ],
    "orientation": "本讲的卷面直接分值是零。向量运算、平面与直线、曲面与空间曲线及其投影，这三 个考点在2010–2026 十七年、51 套卷、1155 个卷面题位里，没有一道题以它们中任何一个为主 考点——全书唯一一讲。但它的先修中心性极高：后面的L31、L33、L34、L35、L36、L37 每一 讲都要用到这里的法向量、方向向量、叉积与“投影＝消元”，你在那些讲里每写一道大题，第一 步几乎都踩在本讲上。所以最低要求只有一条：会用就行，不必深挖。本讲不当“讲”学，当工 具卡记：两张卡加四道上手诊断，一页看完。",
    "subsections": [
      "工具卡"
    ],
    "stats": {
      "independentQuestions": 0,
      "positions": 0,
      "choiceCount": 0,
      "blankCount": 0,
      "solutionCount": 0,
      "math1Score": 0,
      "math2Score": 0,
      "math3Score": 0,
      "math1Percent": "0.00%",
      "math2Percent": "0.00%",
      "math3Percent": "0.00%",
      "avgDifficulty": "★★☆☆☆"
    },
    "methodCards": [
      {
        "title": "向量代数与空间解析几何 核心方法梳理",
        "subtitle": "涵盖 1 个进阶小节",
        "content": "本讲重点掌握 工具卡 等核心知识链路，严格对齐考研大纲要求与历年命题规律。"
      }
    ],
    "pitfalls": [
      "未看清本讲在三卷中的具体分值权重与适用标签（方法课、数一专属）。",
      "忽略定理适用的前提条件（如开闭区间、可导性、正交性或独立性前提）。"
    ],
    "mappedTopicIds": [
      "gaoshu-09-vectors-planes-lines",
      "gaoshu-09-surfaces-and-projections"
    ]
  },
  {
    "id": "L29",
    "num": 29,
    "title": "多元函数的极限、连续、偏导与全微分",
    "partNum": 3,
    "partTitle": "第 3 编 多元函数微积分",
    "page": 495,
    "pageEnd": 511,
    "isKey": false,
    "isCompressed": false,
    "isMath1Only": false,
    "isMath2Heavy": false,
    "isMath3Only": false,
    "isMethod": false,
    "tags": [
      "统考必考"
    ],
    "orientation": "本讲是全编的概念地基，从真题看它以选填为主：20 个卷面题位= 11 选+ 7 填+ 2 解答，17 年只出过两道解答题。分值上数一只占0.31%（17 年总共8 分，平均每年0.5 分），数 二、数三各",
    "subsections": [
      "二重极限",
      "偏导数与全微分",
      "四个概念的关系图（本讲核心）",
      "填空题的固定形态：由 df 反求 f",
      "应用题：经济与旋转体（本讲最后做）",
      "本讲小结"
    ],
    "stats": {
      "independentQuestions": 17,
      "positions": 20,
      "choiceCount": 11,
      "blankCount": 7,
      "solutionCount": 2,
      "math1Score": 8,
      "math2Score": 45,
      "math3Score": 45,
      "math1Percent": "0.31%",
      "math2Percent": "1.76%",
      "math3Percent": "1.76%",
      "avgDifficulty": "★★★☆☆"
    },
    "methodCards": [
      {
        "title": "多元函数的极限、连续、偏导与全微分 核心方法梳理",
        "subtitle": "涵盖 6 个进阶小节",
        "content": "本讲重点掌握 二重极限、偏导数与全微分、四个概念的关系图（本讲核心）、填空题的固定形态：由 df 反求 f 等核心知识链路，严格对齐考研大纲要求与历年命题规律。"
      }
    ],
    "pitfalls": [
      "未看清本讲在三卷中的具体分值权重与适用标签（统考必考）。",
      "忽略定理适用的前提条件（如开闭区间、可导性、正交性或独立性前提）。"
    ],
    "mappedTopicIds": [
      "gaoshu-05-differentiability-concept"
    ]
  },
  {
    "id": "L30",
    "num": 30,
    "title": "复合函数与隐函数求导",
    "partNum": 3,
    "partTitle": "第 3 编 多元函数微积分",
    "page": 511,
    "pageEnd": 535,
    "isKey": true,
    "isCompressed": false,
    "isMath1Only": false,
    "isMath2Heavy": false,
    "isMath3Only": false,
    "isMethod": false,
    "tags": [
      "重点讲",
      "统考必考"
    ],
    "orientation": "本编第二大讲（仅次于L33 二重积分），也是三卷共同的高频讲。17 年真题里本讲名 下39 道独立题、51 个卷面题位——按题位数在全书与L14 并列第四，前面只有L18（82）、L33 （70）、L59（60）。数一占4.44%（113 分）、数二5.50%（140 分，数二单讲第五，排在L33、L18、 L14、L21 之后）、数三3.36%（86 分）。折算下来数二平均每年从这一讲拿走8.2 分、数一6.6 分、数三5.1 分。 题位构成是12 选+ 21 填+ 18 解——填空和解答各占一头，两条线要分开练：填空线是隐 函数（21 个填空题位里12 个是“给一个方程求某点的偏导或全微分”），解答线不是课本上的链 式法则练习，而是换元化偏微分方程与由偏导方程反求f （18 个解答题位里占8 个）+ 由隐函 数定极值（3 个）。",
    "subsections": [
      "显式复合函数的一阶偏导：把三层树形图画出来",
      "显式复合函数的二阶偏导（本讲标志题型）",
      "隐函数的一阶偏导（填空主力）",
      "隐函数的二阶偏导",
      "变量代换：化简偏微分方程与反求 f"
    ],
    "stats": {
      "independentQuestions": 39,
      "positions": 51,
      "choiceCount": 12,
      "blankCount": 21,
      "solutionCount": 18,
      "math1Score": 113,
      "math2Score": 140,
      "math3Score": 86,
      "math1Percent": "4.43%",
      "math2Percent": "5.49%",
      "math3Percent": "3.37%",
      "avgDifficulty": "★★★★☆"
    },
    "methodCards": [
      {
        "title": "复合函数与隐函数求导 核心方法梳理",
        "subtitle": "涵盖 5 个进阶小节",
        "content": "本讲重点掌握 显式复合函数的一阶偏导：把三层树形图画出来、显式复合函数的二阶偏导（本讲标志题型）、隐函数的一阶偏导（填空主力）、隐函数的二阶偏导 等核心知识链路，严格对齐考研大纲要求与历年命题规律。"
      }
    ],
    "pitfalls": [
      "未看清本讲在三卷中的具体分值权重与适用标签（重点讲、统考必考）。",
      "忽略定理适用的前提条件（如开闭区间、可导性、正交性或独立性前提）。"
    ],
    "mappedTopicIds": [
      "gaoshu-05-chain-rule-composite",
      "gaoshu-05-implicit-function-differentiation"
    ]
  },
  {
    "id": "L31",
    "num": 31,
    "title": "方向导数、梯度与几何应用",
    "partNum": 3,
    "partTitle": "第 3 编 多元函数微积分",
    "page": 535,
    "pageEnd": 529,
    "isKey": false,
    "isCompressed": false,
    "isMath1Only": true,
    "isMath2Heavy": false,
    "isMath3Only": false,
    "isMethod": false,
    "tags": [
      "数一专属"
    ],
    "orientation": "本讲为《Maki考研数学一站式大串讲》核心讲次，全方位剖析 方向导数、梯度与几何应用 的考查主线与经典题型。",
    "subsections": [
      "方向导数：先单位化，再与梯度作点积",
      "最大方向导数：|f|",
      "曲面的切平面与法线",
      "空间曲线的切线与法平面",
      "本讲小结"
    ],
    "stats": {
      "independentQuestions": 0,
      "positions": 0,
      "choiceCount": 0,
      "blankCount": 0,
      "solutionCount": 0,
      "math1Score": 0,
      "math2Score": 0,
      "math3Score": 0,
      "math1Percent": "0.00%",
      "math2Percent": "0.00%",
      "math3Percent": "0.00%",
      "avgDifficulty": "★★☆☆☆"
    },
    "methodCards": [
      {
        "title": "方向导数、梯度与几何应用 核心方法梳理",
        "subtitle": "涵盖 5 个进阶小节",
        "content": "本讲重点掌握 方向导数：先单位化，再与梯度作点积、最大方向导数：|f|、曲面的切平面与法线、空间曲线的切线与法平面 等核心知识链路，严格对齐考研大纲要求与历年命题规律。"
      }
    ],
    "pitfalls": [
      "未看清本讲在三卷中的具体分值权重与适用标签（数一专属）。",
      "忽略定理适用的前提条件（如开闭区间、可导性、正交性或独立性前提）。"
    ],
    "mappedTopicIds": [
      "gaoshu-05-directional-derivative-gradient"
    ]
  },
  {
    "id": "L32",
    "num": 32,
    "title": "隐函数确定的函数求极值（本讲与 L32 的接口）",
    "partNum": 3,
    "partTitle": "第 3 编 多元函数微积分",
    "page": 529,
    "pageEnd": 563,
    "isKey": false,
    "isCompressed": false,
    "isMath1Only": false,
    "isMath2Heavy": false,
    "isMath3Only": false,
    "isMethod": false,
    "tags": [
      "统考必考"
    ],
    "orientation": "本讲为《Maki考研数学一站式大串讲》核心讲次，全方位剖析 隐函数确定的函数求极值（本讲与 L32 的接口） 的考查主线与经典题型。",
    "subsections": [
      "本讲小结"
    ],
    "stats": {
      "independentQuestions": 0,
      "positions": 0,
      "choiceCount": 0,
      "blankCount": 0,
      "solutionCount": 0,
      "math1Score": 0,
      "math2Score": 0,
      "math3Score": 0,
      "math1Percent": "0.00%",
      "math2Percent": "0.00%",
      "math3Percent": "0.00%",
      "avgDifficulty": "★★☆☆☆"
    },
    "methodCards": [
      {
        "title": "隐函数确定的函数求极值（本讲与 L32 的接口） 核心方法梳理",
        "subtitle": "涵盖 1 个进阶小节",
        "content": "本讲重点掌握 本讲小结 等核心知识链路，严格对齐考研大纲要求与历年命题规律。"
      }
    ],
    "pitfalls": [
      "未看清本讲在三卷中的具体分值权重与适用标签（统考必考）。",
      "忽略定理适用的前提条件（如开闭区间、可导性、正交性或独立性前提）。"
    ],
    "mappedTopicIds": [
      "gaoshu-05-lagrange-multipliers"
    ]
  },
  {
    "id": "L33",
    "num": 33,
    "title": "二重积分",
    "partNum": 3,
    "partTitle": "第 3 编 多元函数微积分",
    "page": 563,
    "pageEnd": 591,
    "isKey": true,
    "isCompressed": false,
    "isMath1Only": false,
    "isMath2Heavy": true,
    "isMath3Only": false,
    "isMethod": false,
    "tags": [
      "重点讲",
      "数二重点",
      "统考必考"
    ],
    "orientation": "全书独立题最多、解答题位也最多的一讲，而且是数二数三的单讲分值第一。17 年真 题里本讲名下有58 道独立题、70 个卷面题位（题位数仅次于L18 的82 个），解答题位38 个， 全书第一（第二是L18 的30 个）。数二占卷面总分的10.56%——全书单讲第一，超过L18 定积 分的10.33%；数三8.27%，仅次于L59 数字特征，排第二。折成分数是数二269 分、数三211 分，平均每年15.8 分与12.4 分。也就是说这一讲不是拿来“选对”的，是拿来完整写出十分的。 数一只有2.81%（72 分，每年4.2 分），因为数一的多元积分主战场在三重与曲线曲面积分。 本讲的功夫全在画区域、定次序上，计算本身是一元积分的活。",
    "subsections": [
      "概念与性质",
      "直角坐标：两种次序",
      "交换积分次序",
      "极坐标",
      "对称性与轮换对称性",
      "换元法（近年新增路线）",
      "形心与质心：静矩除以总量",
      "本讲小结"
    ],
    "stats": {
      "independentQuestions": 58,
      "positions": 70,
      "choiceCount": 20,
      "blankCount": 12,
      "solutionCount": 38,
      "math1Score": 72,
      "math2Score": 269,
      "math3Score": 211,
      "math1Percent": "2.82%",
      "math2Percent": "10.55%",
      "math3Percent": "8.27%",
      "avgDifficulty": "★★★★☆"
    },
    "methodCards": [
      {
        "title": "二重积分计算选择表（数二每年15.8分第一大讲）",
        "subtitle": "直角坐标切片 · 极坐标雅可比 · 轮换对称性",
        "content": "X型先y后x，Y型先x后y；圆域扇形或 x^2+y^2 果断转极坐标（面积微元 r dr dθ，切勿漏乘r）；轮换对称性 ∬_D f(x)dσ = ∬_D f(y)dσ 大幅消项。"
      }
    ],
    "pitfalls": [
      "未看清本讲在三卷中的具体分值权重与适用标签（重点讲、数二重点、统考必考）。",
      "忽略定理适用的前提条件（如开闭区间、可导性、正交性或独立性前提）。"
    ],
    "mappedTopicIds": [
      "gaoshu-06-double-integral-polar",
      "gaoshu-06-order-exchange-symmetry"
    ]
  },
  {
    "id": "L34",
    "num": 34,
    "title": "三重积分",
    "partNum": 3,
    "partTitle": "第 3 编 多元函数微积分",
    "page": 591,
    "pageEnd": 601,
    "isKey": false,
    "isCompressed": true,
    "isMath1Only": true,
    "isMath2Heavy": false,
    "isMath3Only": false,
    "isMethod": false,
    "tags": [
      "压缩讲",
      "数一专属"
    ],
    "orientation": "L34–L37 四讲导读。这四讲只有数一考，数二数三17 年真题里一道都没有——不是 “少考”，是0 分。但对数一，这四讲合起来是272 分、占数一卷面总分的10.7%，平均每年从 这里拿走16 分，是数一相对数二数三多出来的最大一块负担，也是数一最集中的一片分数。四 讲内部的权重极不平均： 讲 题位 数一占比 平均每年 落点 L34 三重积分 5",
    "subsections": [
      "三种坐标系：只需要会选，不需要苦练",
      "对称性与形心：真题的两个真正落点",
      "本讲小结"
    ],
    "stats": {
      "independentQuestions": 5,
      "positions": 5,
      "choiceCount": 1,
      "blankCount": 2,
      "solutionCount": 2,
      "math1Score": 34,
      "math2Score": 0,
      "math3Score": 0,
      "math1Percent": "1.33%",
      "math2Percent": "0.00%",
      "math3Percent": "0.00%",
      "avgDifficulty": "★★☆☆☆"
    },
    "methodCards": [
      {
        "title": "三重积分 核心方法梳理",
        "subtitle": "涵盖 3 个进阶小节",
        "content": "本讲重点掌握 三种坐标系：只需要会选，不需要苦练、对称性与形心：真题的两个真正落点、本讲小结 等核心知识链路，严格对齐考研大纲要求与历年命题规律。"
      }
    ],
    "pitfalls": [
      "未看清本讲在三卷中的具体分值权重与适用标签（压缩讲、数一专属）。",
      "忽略定理适用的前提条件（如开闭区间、可导性、正交性或独立性前提）。"
    ],
    "mappedTopicIds": [
      "gaoshu-06-triple-integral-coordinates"
    ]
  },
  {
    "id": "L35",
    "num": 35,
    "title": "曲线积分",
    "partNum": 3,
    "partTitle": "第 3 编 多元函数微积分",
    "page": 601,
    "pageEnd": 623,
    "isKey": true,
    "isCompressed": false,
    "isMath1Only": true,
    "isMath2Heavy": false,
    "isMath3Only": false,
    "isMethod": false,
    "tags": [
      "重点讲",
      "数一专属"
    ],
    "orientation": "数一的固定大题产地。17 年本讲名下12 道独立题、12 个卷面题位，其中6 道是解 答题——一半的题是要整道写出来的，这个比例在数一各讲里排在前列。数一占卷面总分3.53% （90 分），平均每年5.3 分，平均难度3.25。数二数三0 分。 但真正要记住的是本讲内部的悬殊：12 道题里11 道属于“第二类曲线积分与格林公式”（86 分），第一类曲线积分（对弧长）17 年只考过1 道——2018 数一12，一个填空，4 分。第一类曲 线积分十七年只有这1 个题位，记住一个ds 公式就够；本讲的重心是格林公式的四种变形（直 接用、补线、挖洞、路径无关）。你的时间也照这个比例分。",
    "subsections": [
      "向量场前置工具卡",
      "第一类曲线积分（对弧长）",
      "第二类曲线积分：直接计算",
      "格林公式",
      "路径无关与原函数",
      "奇点：挖洞",
      "空间曲线积分",
      "本讲小结"
    ],
    "stats": {
      "independentQuestions": 12,
      "positions": 12,
      "choiceCount": 2,
      "blankCount": 4,
      "solutionCount": 6,
      "math1Score": 90,
      "math2Score": 0,
      "math3Score": 0,
      "math1Percent": "3.53%",
      "math2Percent": "0.00%",
      "math3Percent": "0.00%",
      "avgDifficulty": "★★★★☆"
    },
    "methodCards": [
      {
        "title": "曲线积分 核心方法梳理",
        "subtitle": "涵盖 8 个进阶小节",
        "content": "本讲重点掌握 向量场前置工具卡、第一类曲线积分（对弧长）、第二类曲线积分：直接计算、格林公式 等核心知识链路，严格对齐考研大纲要求与历年命题规律。"
      }
    ],
    "pitfalls": [
      "未看清本讲在三卷中的具体分值权重与适用标签（重点讲、数一专属）。",
      "忽略定理适用的前提条件（如开闭区间、可导性、正交性或独立性前提）。"
    ],
    "mappedTopicIds": [
      "gaoshu-07-curvilinear-path-independent",
      "gaoshu-07-green-formula-hole-technique"
    ]
  },
  {
    "id": "L36",
    "num": 36,
    "title": "曲面积分",
    "partNum": 3,
    "partTitle": "第 3 编 多元函数微积分",
    "page": 623,
    "pageEnd": 645,
    "isKey": true,
    "isCompressed": false,
    "isMath1Only": true,
    "isMath2Heavy": false,
    "isMath3Only": false,
    "isMethod": false,
    "tags": [
      "重点讲",
      "数一专属"
    ],
    "orientation": "数一在整个第3 编的最大单讲，在数一全卷分值排行里排第五。17 年本讲名下16 道 独立题、16 个卷面题位，其中10 道是解答题，数一占卷面总分5.31%（135 分），平均每年7.9 分，平均难度3.50——是本编难度最高的一讲。数二数三0 分。 三个考点的权重差得很远，时间就照这个比例分： 考点 独立题 解答 数一分 难度 命题年份 第一类曲面积分 3 2 24.9 3.33 2010、2012、2017 第二类＋高斯公式 9 6 79.1 3.56 2014–2025 共9 年 斯托克斯公式 4 2 3",
    "subsections": [
      "第一类曲面积分（对面积）",
      "第二类曲面积分与高斯公式",
      "斯托克斯公式",
      "本讲小结"
    ],
    "stats": {
      "independentQuestions": 16,
      "positions": 16,
      "choiceCount": 1,
      "blankCount": 5,
      "solutionCount": 10,
      "math1Score": 135,
      "math2Score": 0,
      "math3Score": 0,
      "math1Percent": "5.29%",
      "math2Percent": "0.00%",
      "math3Percent": "0.00%",
      "avgDifficulty": "★★★★☆"
    },
    "methodCards": [
      {
        "title": "曲面积分 核心方法梳理",
        "subtitle": "涵盖 4 个进阶小节",
        "content": "本讲重点掌握 第一类曲面积分（对面积）、第二类曲面积分与高斯公式、斯托克斯公式、本讲小结 等核心知识链路，严格对齐考研大纲要求与历年命题规律。"
      }
    ],
    "pitfalls": [
      "未看清本讲在三卷中的具体分值权重与适用标签（重点讲、数一专属）。",
      "忽略定理适用的前提条件（如开闭区间、可导性、正交性或独立性前提）。"
    ],
    "mappedTopicIds": [
      "gaoshu-07-gauss-divergence-theorem"
    ]
  },
  {
    "id": "L37",
    "num": 37,
    "title": "场论初步",
    "partNum": 3,
    "partTitle": "第 3 编 多元函数微积分",
    "page": 645,
    "pageEnd": 655,
    "isKey": false,
    "isCompressed": true,
    "isMath1Only": true,
    "isMath2Heavy": false,
    "isMath3Only": false,
    "isMethod": false,
    "tags": [
      "压缩讲",
      "数一专属"
    ],
    "orientation": "数一全书最便宜的送分点，也是第3 编的收口。17 年本讲名下只有3 道题、3 个卷面 题位，数一占0.51%（13 分），数二数三0 分。但真正的关键数字是难度：平均难度",
    "subsections": [
      "场论统一总结：三个算子各归其位",
      "公式回看与验收清单",
      "两道快速复盘题",
      "本讲小结"
    ],
    "stats": {
      "independentQuestions": 3,
      "positions": 3,
      "choiceCount": 0,
      "blankCount": 3,
      "solutionCount": 0,
      "math1Score": 13,
      "math2Score": 0,
      "math3Score": 0,
      "math1Percent": "0.51%",
      "math2Percent": "0.00%",
      "math3Percent": "0.00%",
      "avgDifficulty": "★★☆☆☆"
    },
    "methodCards": [
      {
        "title": "场论初步 核心方法梳理",
        "subtitle": "涵盖 4 个进阶小节",
        "content": "本讲重点掌握 场论统一总结：三个算子各归其位、公式回看与验收清单、两道快速复盘题、本讲小结 等核心知识链路，严格对齐考研大纲要求与历年命题规律。"
      }
    ],
    "pitfalls": [
      "未看清本讲在三卷中的具体分值权重与适用标签（压缩讲、数一专属）。",
      "忽略定理适用的前提条件（如开闭区间、可导性、正交性或独立性前提）。"
    ],
    "mappedTopicIds": [
      "gaoshu-07-stokes-theorem-curl"
    ]
  },
  {
    "id": "L38",
    "num": 38,
    "title": "常数项级数与正项级数",
    "partNum": 4,
    "partTitle": "第 4 编 无穷级数",
    "page": 655,
    "pageEnd": 669,
    "isKey": false,
    "isCompressed": false,
    "isMath1Only": false,
    "isMath2Heavy": false,
    "isMath3Only": false,
    "isMethod": false,
    "tags": [
      "统考必考"
    ],
    "orientation": "判敛线的第一讲，体量不大，但它在数三卷上比在数一卷上重一倍。17 年真题里本讲 名下有6 道独立题、6 个卷面题位，数一0.56%、数三0.88%、数二0——平均每年数一0.8 分、 数三",
    "subsections": [
      "第一道关卡：通项是否趋于零",
      "两个基准级数",
      "比较判别法与它的极限形式",
      "比值判别法与根值判别法",
      "其他判别法，以及五条判别法的真题权重",
      "本讲小结"
    ],
    "stats": {
      "independentQuestions": 6,
      "positions": 6,
      "choiceCount": 4,
      "blankCount": 0,
      "solutionCount": 2,
      "math1Score": 14,
      "math2Score": 0,
      "math3Score": 22,
      "math1Percent": "0.55%",
      "math2Percent": "0.00%",
      "math3Percent": "0.86%",
      "avgDifficulty": "★★★☆☆"
    },
    "methodCards": [
      {
        "title": "常数项级数与正项级数 核心方法梳理",
        "subtitle": "涵盖 6 个进阶小节",
        "content": "本讲重点掌握 第一道关卡：通项是否趋于零、两个基准级数、比较判别法与它的极限形式、比值判别法与根值判别法 等核心知识链路，严格对齐考研大纲要求与历年命题规律。"
      }
    ],
    "pitfalls": [
      "未看清本讲在三卷中的具体分值权重与适用标签（统考必考）。",
      "忽略定理适用的前提条件（如开闭区间、可导性、正交性或独立性前提）。"
    ],
    "mappedTopicIds": [
      "gaoshu-08-series-convergence-tests"
    ]
  },
  {
    "id": "L39",
    "num": 39,
    "title": "交错级数与任意项级数",
    "partNum": 4,
    "partTitle": "第 4 编 无穷级数",
    "page": 669,
    "pageEnd": 681,
    "isKey": false,
    "isCompressed": false,
    "isMath1Only": false,
    "isMath2Heavy": false,
    "isMath3Only": false,
    "isMethod": false,
    "tags": [
      "统考必考"
    ],
    "orientation": "本编最“偏科”的一讲：9 个卷面题位里8 个是选择题，唯一的解答题（2016 数一19） 还是道数列题借了级数的壳。数一0.80%、数三",
    "subsections": [
      "决策顺序：四步，顺序不能换",
      "绝对收敛与条件收敛（流程的第 2、4 步）",
      "莱布尼茨判别法（流程的第 3 步）",
      "本讲小结"
    ],
    "stats": {
      "independentQuestions": 8,
      "positions": 9,
      "choiceCount": 8,
      "blankCount": 0,
      "solutionCount": 1,
      "math1Score": 20,
      "math2Score": 0,
      "math3Score": 26,
      "math1Percent": "0.78%",
      "math2Percent": "0.00%",
      "math3Percent": "1.02%",
      "avgDifficulty": "★★★☆☆"
    },
    "methodCards": [
      {
        "title": "交错级数与任意项级数 核心方法梳理",
        "subtitle": "涵盖 4 个进阶小节",
        "content": "本讲重点掌握 决策顺序：四步，顺序不能换、绝对收敛与条件收敛（流程的第 2、4 步）、莱布尼茨判别法（流程的第 3 步）、本讲小结 等核心知识链路，严格对齐考研大纲要求与历年命题规律。"
      }
    ],
    "pitfalls": [
      "未看清本讲在三卷中的具体分值权重与适用标签（统考必考）。",
      "忽略定理适用的前提条件（如开闭区间、可导性、正交性或独立性前提）。"
    ],
    "mappedTopicIds": [
      "gaoshu-08-series-convergence-tests"
    ]
  },
  {
    "id": "L40",
    "num": 40,
    "title": "幂级数",
    "partNum": 4,
    "partTitle": "第 4 编 无穷级数",
    "page": 681,
    "pageEnd": 699,
    "isKey": true,
    "isCompressed": false,
    "isMath1Only": false,
    "isMath2Heavy": false,
    "isMath3Only": false,
    "isMethod": false,
    "tags": [
      "重点讲",
      "统考必考"
    ],
    "orientation": "本编唯一的大讲，也是本编的全部重心。17 年真题里本讲名下有17 道独立题、17 个 卷面题位，数一3.11%、数三2.30%、数二0——一讲吃掉了本编数一分值的49%、数三的39%， 每年从数一卷拿走4.7 分、数三卷3.5 分。更关键的是题型：17 个题位里10 个是解答题，全编 18 个解答题位有10 个在这里。本讲不是拿来“选对”的，是拿来完整写出十分的。 而这17 道题的内部分布极不均匀，必须先说清楚： 考点 独立题 数一分 数三分 题型 40.1 收敛半径与收敛域 6 22.0 4.0 5 选1 填，0 解答 40.2 幂级数求和函数 11 57.4 54.7 1 填10 解答 “求和函数”一个考点占了本讲的11 道题、10 个解答题位，数一57.4 分、数三54.7 分，是整 个第4 编最大的单考点。而“收敛半径与收敛域”6 道题全是选填，且数三17 年只在这上面出过 4 分（一道2020 年的选择）。 本讲先把展开表摆出来当工具（下一节），然后按这两个考点分成两大块讲，中间不混：第一 块只谈“级数在哪些x 上收敛”，第二块只谈“收敛的地方它等于什么函数”。这两件事用的工具 完全不同，考场上也是分开给分的——第一块的结论是一个集合（收敛域），第二块的结论是一个 表达式（和函数加",
    "subsections": [
      "开工之前：把这张展开表放在手边",
      "第一块：收敛半径与收敛域",
      "第二块：和函数",
      "本讲小结"
    ],
    "stats": {
      "independentQuestions": 17,
      "positions": 17,
      "choiceCount": 5,
      "blankCount": 2,
      "solutionCount": 10,
      "math1Score": 79,
      "math2Score": 0,
      "math3Score": 59,
      "math1Percent": "3.10%",
      "math2Percent": "0.00%",
      "math3Percent": "2.31%",
      "avgDifficulty": "★★★★☆"
    },
    "methodCards": [
      {
        "title": "幂级数 核心方法梳理",
        "subtitle": "涵盖 4 个进阶小节",
        "content": "本讲重点掌握 开工之前：把这张展开表放在手边、第一块：收敛半径与收敛域、第二块：和函数、本讲小结 等核心知识链路，严格对齐考研大纲要求与历年命题规律。"
      }
    ],
    "pitfalls": [
      "未看清本讲在三卷中的具体分值权重与适用标签（重点讲、统考必考）。",
      "忽略定理适用的前提条件（如开闭区间、可导性、正交性或独立性前提）。"
    ],
    "mappedTopicIds": [
      "gaoshu-08-power-series-radius-interval"
    ]
  },
  {
    "id": "L41",
    "num": 41,
    "title": "函数展开与级数求和",
    "partNum": 4,
    "partTitle": "第 4 编 无穷级数",
    "page": 699,
    "pageEnd": 715,
    "isKey": false,
    "isCompressed": false,
    "isMath1Only": false,
    "isMath2Heavy": false,
    "isMath3Only": false,
    "isMethod": false,
    "tags": [
      "统考必考"
    ],
    "orientation": "题量不大、但解答题密度是本编第二高的一讲：17 年10 个卷面题位、7 道独立题，其 中5 个是解答题位——整整一半。分布在2018、2019、2023、2024、2026 五个年份，数一0.92% （23 分，每年",
    "subsections": [],
    "stats": {
      "independentQuestions": 7,
      "positions": 10,
      "choiceCount": 3,
      "blankCount": 2,
      "solutionCount": 5,
      "math1Score": 23,
      "math2Score": 10,
      "math3Score": 43,
      "math1Percent": "0.90%",
      "math2Percent": "0.39%",
      "math3Percent": "1.69%",
      "avgDifficulty": "★★★☆☆"
    },
    "methodCards": [
      {
        "title": "函数展开与级数求和 核心方法梳理",
        "subtitle": "涵盖 0 个进阶小节",
        "content": "本讲重点掌握  等核心知识链路，严格对齐考研大纲要求与历年命题规律。"
      }
    ],
    "pitfalls": [
      "未看清本讲在三卷中的具体分值权重与适用标签（统考必考）。",
      "忽略定理适用的前提条件（如开闭区间、可导性、正交性或独立性前提）。"
    ],
    "mappedTopicIds": [
      "gaoshu-08-power-series-summation"
    ]
  },
  {
    "id": "L42",
    "num": 42,
    "title": "傅里叶级数",
    "partNum": 4,
    "partTitle": "第 4 编 无穷级数",
    "page": 715,
    "pageEnd": 733,
    "isKey": false,
    "isCompressed": true,
    "isMath1Only": true,
    "isMath2Heavy": false,
    "isMath3Only": false,
    "isMethod": false,
    "tags": [
      "压缩讲",
      "数一专属"
    ],
    "orientation": "数一专属，且17 年零解答题。本讲名下5 个卷面题位、5 道独立题，全部落在数一 卷上：数一0.90%（17 年23 分，每年约",
    "subsections": [
      "这一讲在做什么：把一个周期函数拆成一堆正弦余弦",
      "第一步：认出延拓方式",
      "第二步：算系数 an 与 bn",
      "第三步：用狄利克雷收敛定理读值",
      "本讲小结"
    ],
    "stats": {
      "independentQuestions": 5,
      "positions": 5,
      "choiceCount": 2,
      "blankCount": 3,
      "solutionCount": 0,
      "math1Score": 23,
      "math2Score": 0,
      "math3Score": 0,
      "math1Percent": "0.90%",
      "math2Percent": "0.00%",
      "math3Percent": "0.00%",
      "avgDifficulty": "★★☆☆☆"
    },
    "methodCards": [
      {
        "title": "傅里叶级数 核心方法梳理",
        "subtitle": "涵盖 5 个进阶小节",
        "content": "本讲重点掌握 这一讲在做什么：把一个周期函数拆成一堆正弦余弦、第一步：认出延拓方式、第二步：算系数 an 与 bn、第三步：用狄利克雷收敛定理读值 等核心知识链路，严格对齐考研大纲要求与历年命题规律。"
      }
    ],
    "pitfalls": [
      "未看清本讲在三卷中的具体分值权重与适用标签（压缩讲、数一专属）。",
      "忽略定理适用的前提条件（如开闭区间、可导性、正交性或独立性前提）。"
    ],
    "mappedTopicIds": [
      "gaoshu-10-fourier-series-dirichlet"
    ]
  },
  {
    "id": "L43",
    "num": 43,
    "title": "行列式",
    "partNum": 5,
    "partTitle": "第 5 编 线性代数",
    "page": 733,
    "pageEnd": 745,
    "isKey": false,
    "isCompressed": false,
    "isMath1Only": false,
    "isMath2Heavy": false,
    "isMath3Only": false,
    "isMethod": false,
    "tags": [
      "统考必考"
    ],
    "orientation": "十七年真题里本讲名下只有8 道独立题、14 个卷面题位，分值占比数一0.63%、数二 0.67%、数三",
    "subsections": [
      "定义与本质",
      "性质与展开定理：本讲的真正主体",
      "代数余子式的线性组合",
      "特殊行列式",
      "本讲小结"
    ],
    "stats": {
      "independentQuestions": 8,
      "positions": 14,
      "choiceCount": 4,
      "blankCount": 10,
      "solutionCount": 0,
      "math1Score": 16,
      "math2Score": 17,
      "math3Score": 27,
      "math1Percent": "0.63%",
      "math2Percent": "0.67%",
      "math3Percent": "1.06%",
      "avgDifficulty": "★★★☆☆"
    },
    "methodCards": [
      {
        "title": "行列式 核心方法梳理",
        "subtitle": "涵盖 5 个进阶小节",
        "content": "本讲重点掌握 定义与本质、性质与展开定理：本讲的真正主体、代数余子式的线性组合、特殊行列式 等核心知识链路，严格对齐考研大纲要求与历年命题规律。"
      }
    ],
    "pitfalls": [
      "未看清本讲在三卷中的具体分值权重与适用标签（统考必考）。",
      "忽略定理适用的前提条件（如开闭区间、可导性、正交性或独立性前提）。"
    ],
    "mappedTopicIds": [
      "xiandai-01-determinant-properties-definition",
      "xiandai-01-determinant-calc-techniques"
    ]
  },
  {
    "id": "L44",
    "num": 44,
    "title": "矩阵运算与逆矩阵",
    "partNum": 5,
    "partTitle": "第 5 编 线性代数",
    "page": 745,
    "pageEnd": 759,
    "isKey": false,
    "isCompressed": false,
    "isMath1Only": false,
    "isMath2Heavy": false,
    "isMath3Only": false,
    "isMethod": false,
    "tags": [
      "统考必考"
    ],
    "orientation": "6 道独立题、12 个卷面题位，数一0.55%、数二0.86%、数三0.67%，每年0.8 ／",
    "subsections": [
      "矩阵是什么，怎么算",
      "运算律、可逆性与行列式",
      "伴随矩阵：本讲的主体",
      "求逆矩阵的四条路线",
      "矩阵高次幂：整块在 L50",
      "分块矩阵",
      "本讲小结"
    ],
    "stats": {
      "independentQuestions": 6,
      "positions": 12,
      "choiceCount": 4,
      "blankCount": 8,
      "solutionCount": 0,
      "math1Score": 14,
      "math2Score": 22,
      "math3Score": 17,
      "math1Percent": "0.55%",
      "math2Percent": "0.86%",
      "math3Percent": "0.67%",
      "avgDifficulty": "★★★☆☆"
    },
    "methodCards": [
      {
        "title": "矩阵运算与逆矩阵 核心方法梳理",
        "subtitle": "涵盖 7 个进阶小节",
        "content": "本讲重点掌握 矩阵是什么，怎么算、运算律、可逆性与行列式、伴随矩阵：本讲的主体、求逆矩阵的四条路线 等核心知识链路，严格对齐考研大纲要求与历年命题规律。"
      }
    ],
    "pitfalls": [
      "未看清本讲在三卷中的具体分值权重与适用标签（统考必考）。",
      "忽略定理适用的前提条件（如开闭区间、可导性、正交性或独立性前提）。"
    ],
    "mappedTopicIds": [
      "xiandai-02-matrix-multiplication-inverse",
      "xiandai-02-adjoint-matrix-properties"
    ]
  },
  {
    "id": "L45",
    "num": 45,
    "title": "初等变换、初等矩阵与秩",
    "partNum": 5,
    "partTitle": "第 5 编 线性代数",
    "page": 759,
    "pageEnd": 779,
    "isKey": false,
    "isCompressed": false,
    "isMath1Only": false,
    "isMath2Heavy": false,
    "isMath3Only": false,
    "isMethod": false,
    "tags": [
      "统考必考"
    ],
    "orientation": "“地基三讲”里体量最大的一讲，而且它基本是一讲选择题课。16 道独立题、22 个卷 面题位，数一",
    "subsections": [
      "初等矩阵：左行右列",
      "秩：选择题的战场",
      "矩阵方程：本讲的大题所在",
      "本讲小结"
    ],
    "stats": {
      "independentQuestions": 16,
      "positions": 22,
      "choiceCount": 15,
      "blankCount": 5,
      "solutionCount": 2,
      "math1Score": 36,
      "math2Score": 43,
      "math3Score": 34,
      "math1Percent": "1.41%",
      "math2Percent": "1.69%",
      "math3Percent": "1.33%",
      "avgDifficulty": "★★★☆☆"
    },
    "methodCards": [
      {
        "title": "初等变换、初等矩阵与秩 核心方法梳理",
        "subtitle": "涵盖 4 个进阶小节",
        "content": "本讲重点掌握 初等矩阵：左行右列、秩：选择题的战场、矩阵方程：本讲的大题所在、本讲小结 等核心知识链路，严格对齐考研大纲要求与历年命题规律。"
      }
    ],
    "pitfalls": [
      "未看清本讲在三卷中的具体分值权重与适用标签（统考必考）。",
      "忽略定理适用的前提条件（如开闭区间、可导性、正交性或独立性前提）。"
    ],
    "mappedTopicIds": [
      "xiandai-02-elementary-matrix-operations",
      "xiandai-02-matrix-rank-theorems"
    ]
  },
  {
    "id": "L46",
    "num": 46,
    "title": "向量组的线性相关性",
    "partNum": 5,
    "partTitle": "第 5 编 线性代数",
    "page": 779,
    "pageEnd": 793,
    "isKey": false,
    "isCompressed": false,
    "isMath1Only": false,
    "isMath2Heavy": false,
    "isMath3Only": false,
    "isMethod": false,
    "tags": [
      "统考必考"
    ],
    "orientation": "12 道独立题、22 个卷面题位，数一",
    "subsections": [
      "两个基本词：线性组合与张成",
      "线性相关与线性无关：定义与三种判定法",
      "必背结论",
      "从向量关系到行列式",
      "向量组的等价",
      "往哪里去：本讲结束时手上有什么",
      "本讲小结"
    ],
    "stats": {
      "independentQuestions": 12,
      "positions": 22,
      "choiceCount": 18,
      "blankCount": 2,
      "solutionCount": 2,
      "math1Score": 31,
      "math2Score": 41,
      "math3Score": 35,
      "math1Percent": "1.22%",
      "math2Percent": "1.61%",
      "math3Percent": "1.37%",
      "avgDifficulty": "★★★☆☆"
    },
    "methodCards": [
      {
        "title": "向量组的线性相关性 核心方法梳理",
        "subtitle": "涵盖 7 个进阶小节",
        "content": "本讲重点掌握 两个基本词：线性组合与张成、线性相关与线性无关：定义与三种判定法、必背结论、从向量关系到行列式 等核心知识链路，严格对齐考研大纲要求与历年命题规律。"
      }
    ],
    "pitfalls": [
      "未看清本讲在三卷中的具体分值权重与适用标签（统考必考）。",
      "忽略定理适用的前提条件（如开闭区间、可导性、正交性或独立性前提）。"
    ],
    "mappedTopicIds": [
      "xiandai-03-vector-linear-combination-dependence",
      "xiandai-03-maximal-linearly-independent-set"
    ]
  },
  {
    "id": "L47",
    "num": 47,
    "title": "线性方程组（一）：消元、判定与通解",
    "partNum": 5,
    "partTitle": "第 5 编 线性代数",
    "page": 793,
    "pageEnd": 817,
    "isKey": false,
    "isCompressed": false,
    "isMath1Only": false,
    "isMath2Heavy": false,
    "isMath3Only": false,
    "isMethod": false,
    "tags": [
      "统考必考"
    ],
    "orientation": "线代第一条主线的主干，也是整编动手量最大的一套动作。17 年真题里本讲名下有 19 道独立题、32 个卷面题位，数一",
    "subsections": [
      "第一节　高斯消元与行阶梯形：唯一真正要练的手上功夫",
      "第二节　解的判定：三个数字决定一切",
      "第三节　齐次方程组与基础解系",
      "第四节　非齐次通解：结构与几何",
      "第五节　含参数方程组的完整讨论：本讲的全部大题",
      "本讲小结"
    ],
    "stats": {
      "independentQuestions": 19,
      "positions": 32,
      "choiceCount": 19,
      "blankCount": 5,
      "solutionCount": 8,
      "math1Score": 47,
      "math2Score": 72,
      "math3Score": 71,
      "math1Percent": "1.84%",
      "math2Percent": "2.82%",
      "math3Percent": "2.78%",
      "avgDifficulty": "★★★★☆"
    },
    "methodCards": [
      {
        "title": "线性方程组（一）：消元、判定与通解 核心方法梳理",
        "subtitle": "涵盖 6 个进阶小节",
        "content": "本讲重点掌握 第一节　高斯消元与行阶梯形：唯一真正要练的手上功夫、第二节　解的判定：三个数字决定一切、第三节　齐次方程组与基础解系、第四节　非齐次通解：结构与几何 等核心知识链路，严格对齐考研大纲要求与历年命题规律。"
      }
    ],
    "pitfalls": [
      "未看清本讲在三卷中的具体分值权重与适用标签（统考必考）。",
      "忽略定理适用的前提条件（如开闭区间、可导性、正交性或独立性前提）。"
    ],
    "mappedTopicIds": [
      "xiandai-04-linear-system-solvability",
      "xiandai-04-homogeneous-fundamental-system"
    ]
  },
  {
    "id": "L48",
    "num": 48,
    "title": "线性方程组（二）：矩阵方程、同解与向量空间",
    "partNum": 5,
    "partTitle": "第 5 编 线性代数",
    "page": 817,
    "pageEnd": 837,
    "isKey": true,
    "isCompressed": false,
    "isMath1Only": false,
    "isMath2Heavy": false,
    "isMath3Only": false,
    "isMethod": false,
    "tags": [
      "重点讲",
      "统考必考"
    ],
    "orientation": "线代第一条主线的终点站，也是本编前半段的大题仓库。17 年真题里本讲名下有16 道独立题、31 个卷面题位，数一4.38%（本编第3）、数三3.52%、数二2.45%。折成分数：数 一11",
    "subsections": [
      "第一节　矩阵方程：一次解一批方程组",
      "第二节　公共解、同解与线性表出的反问题",
      "第三节　极大无关组、向量组的秩与满秩分解",
      "第四节　向量空间、基、坐标与过渡矩阵",
      "本讲小结"
    ],
    "stats": {
      "independentQuestions": 16,
      "positions": 31,
      "choiceCount": 7,
      "blankCount": 4,
      "solutionCount": 20,
      "math1Score": 112,
      "math2Score": 62,
      "math3Score": 90,
      "math1Percent": "4.39%",
      "math2Percent": "2.43%",
      "math3Percent": "3.53%",
      "avgDifficulty": "★★★★☆"
    },
    "methodCards": [
      {
        "title": "线性方程组（二）：矩阵方程、同解与向量空间 核心方法梳理",
        "subtitle": "涵盖 5 个进阶小节",
        "content": "本讲重点掌握 第一节　矩阵方程：一次解一批方程组、第二节　公共解、同解与线性表出的反问题、第三节　极大无关组、向量组的秩与满秩分解、第四节　向量空间、基、坐标与过渡矩阵 等核心知识链路，严格对齐考研大纲要求与历年命题规律。"
      }
    ],
    "pitfalls": [
      "未看清本讲在三卷中的具体分值权重与适用标签（重点讲、统考必考）。",
      "忽略定理适用的前提条件（如开闭区间、可导性、正交性或独立性前提）。"
    ],
    "mappedTopicIds": [
      "xiandai-04-non-homogeneous-general-solution",
      "xiandai-04-matrix-equation-and-common-solutions"
    ]
  },
  {
    "id": "L49",
    "num": 49,
    "title": "特征值与特征向量",
    "partNum": 5,
    "partTitle": "第 5 编 线性代数",
    "page": 837,
    "pageEnd": 853,
    "isKey": false,
    "isCompressed": false,
    "isMath1Only": false,
    "isMath2Heavy": false,
    "isMath3Only": false,
    "isMethod": false,
    "tags": [
      "统考必考"
    ],
    "orientation": "第二条主线的起点，是一个几乎全是选填的讲。17 年真题里本讲名下8 道独立题、10 个卷面题位，其中5 选4 填1 解——解答题位只有1 个（2025 数一21），十七年里本讲只撑起 过这一道大题。分值占比数一0.97%、数二0.55%、数三0.55%，折成分数是数一25 分、数二 14 分、数三14 分，平均每年",
    "subsections": [
      "定义、几何意义与求法",
      "性质表与派生矩阵",
      "几类特殊矩阵的特征值",
      "本讲唯一的一道解答题",
      "本讲小结"
    ],
    "stats": {
      "independentQuestions": 8,
      "positions": 10,
      "choiceCount": 5,
      "blankCount": 4,
      "solutionCount": 1,
      "math1Score": 25,
      "math2Score": 14,
      "math3Score": 14,
      "math1Percent": "0.98%",
      "math2Percent": "0.55%",
      "math3Percent": "0.55%",
      "avgDifficulty": "★★★☆☆"
    },
    "methodCards": [
      {
        "title": "特征值与特征向量 核心方法梳理",
        "subtitle": "涵盖 5 个进阶小节",
        "content": "本讲重点掌握 定义、几何意义与求法、性质表与派生矩阵、几类特殊矩阵的特征值、本讲唯一的一道解答题 等核心知识链路，严格对齐考研大纲要求与历年命题规律。"
      }
    ],
    "pitfalls": [
      "未看清本讲在三卷中的具体分值权重与适用标签（统考必考）。",
      "忽略定理适用的前提条件（如开闭区间、可导性、正交性或独立性前提）。"
    ],
    "mappedTopicIds": [
      "xiandai-05-eigenvalues-eigenvectors",
      "xiandai-05-eigen-properties-special-matrices"
    ]
  },
  {
    "id": "L50",
    "num": 50,
    "title": "相似对角化",
    "partNum": 5,
    "partTitle": "第 5 编 线性代数",
    "page": 853,
    "pageEnd": 879,
    "isKey": true,
    "isCompressed": false,
    "isMath1Only": false,
    "isMath2Heavy": false,
    "isMath3Only": false,
    "isMethod": false,
    "tags": [
      "重点讲",
      "统考必考"
    ],
    "orientation": "第二条主线的主力讲。17 年真题里本讲名下23 道独立题、48 个卷面题位，数二5.02%、 数三4.71%、数一4.13%——数二数三都排本编第一，数一仅次于L52。分数上是数一105 分、 数二128 分、数三120 分，平均每年6.2 ／7.5 ／7.1 分。本讲的题几乎全部挂在一个考点「相 似矩阵与相似对角化」下面，它单独就拿了数二128 分（数二单考点榜第5）、数三120 分（数 三单考点榜第2）、数一105 分（数一单考点榜第2）——全书一百一十八个考点里，能在两卷同 时进前二的只此一个。 本讲最值得注意的是它的题型结构：48 个题位里22 个选择、23 个解答、只有3 个填空。全 书很少有讲是这样两头都重的。它的含义很实在：选择题考“能不能对角化”和“两个矩阵相不 相似”（判定），解答题考“怎么对角化”（计算）。两套准备都得有，且都不能省。 易错/ 提醒 正文按四层走，顺序就是你在考场上的思考顺序：",
    "subsections": [
      "第一层：相似的定义与不变量",
      "第二层：可对角化的判定",
      "第三层：构造 P 与",
      "第四层：用对角化算高次幂、迹与递推",
      "由特征信息反求矩阵",
      "本讲小结"
    ],
    "stats": {
      "independentQuestions": 23,
      "positions": 48,
      "choiceCount": 22,
      "blankCount": 3,
      "solutionCount": 23,
      "math1Score": 105,
      "math2Score": 128,
      "math3Score": 120,
      "math1Percent": "4.12%",
      "math2Percent": "5.02%",
      "math3Percent": "4.71%",
      "avgDifficulty": "★★★★☆"
    },
    "methodCards": [
      {
        "title": "相似对角化 核心方法梳理",
        "subtitle": "涵盖 6 个进阶小节",
        "content": "本讲重点掌握 第一层：相似的定义与不变量、第二层：可对角化的判定、第三层：构造 P 与、第四层：用对角化算高次幂、迹与递推 等核心知识链路，严格对齐考研大纲要求与历年命题规律。"
      }
    ],
    "pitfalls": [
      "未看清本讲在三卷中的具体分值权重与适用标签（重点讲、统考必考）。",
      "忽略定理适用的前提条件（如开闭区间、可导性、正交性或独立性前提）。"
    ],
    "mappedTopicIds": [
      "xiandai-06-similarity-diagonalization-criterion",
      "xiandai-06-power-trace-applications"
    ]
  },
  {
    "id": "L51",
    "num": 51,
    "title": "实对称矩阵",
    "partNum": 5,
    "partTitle": "第 5 编 线性代数",
    "page": 879,
    "pageEnd": 899,
    "isKey": false,
    "isCompressed": false,
    "isMath1Only": false,
    "isMath2Heavy": false,
    "isMath3Only": false,
    "isMethod": false,
    "tags": [
      "统考必考"
    ],
    "orientation": "一讲题量不大、但解答题密度很高的讲。十七年7 道独立题、14 个卷面题位（8 个选 择题位、1 个填空题位、5 个解答题位），数三",
    "subsections": [
      "第一节　内积、正交与施密特：本讲的全部前置",
      "实对称矩阵的四条特有性质",
      "正交对角化的完整步骤",
      "由特征信息反求实对称矩阵",
      "本讲小结"
    ],
    "stats": {
      "independentQuestions": 7,
      "positions": 14,
      "choiceCount": 8,
      "blankCount": 1,
      "solutionCount": 5,
      "math1Score": 28,
      "math2Score": 29,
      "math3Score": 34,
      "math1Percent": "1.10%",
      "math2Percent": "1.14%",
      "math3Percent": "1.33%",
      "avgDifficulty": "★★★☆☆"
    },
    "methodCards": [
      {
        "title": "实对称矩阵 核心方法梳理",
        "subtitle": "涵盖 5 个进阶小节",
        "content": "本讲重点掌握 第一节　内积、正交与施密特：本讲的全部前置、实对称矩阵的四条特有性质、正交对角化的完整步骤、由特征信息反求实对称矩阵 等核心知识链路，严格对齐考研大纲要求与历年命题规律。"
      }
    ],
    "pitfalls": [
      "未看清本讲在三卷中的具体分值权重与适用标签（统考必考）。",
      "忽略定理适用的前提条件（如开闭区间、可导性、正交性或独立性前提）。"
    ],
    "mappedTopicIds": [
      "xiandai-06-real-symmetric-orthogonal-diag"
    ]
  },
  {
    "id": "L52",
    "num": 52,
    "title": "二次型",
    "partNum": 5,
    "partTitle": "第 5 编 线性代数",
    "page": 899,
    "pageEnd": 923,
    "isKey": true,
    "isCompressed": false,
    "isMath1Only": false,
    "isMath2Heavy": false,
    "isMath3Only": false,
    "isMethod": false,
    "tags": [
      "重点讲",
      "统考必考"
    ],
    "orientation": "第5 编题位最多的一讲，也是全书数一分值第三高的一讲。17 年真题里本讲名下29 道独立题、50 个卷面题位，数一5.4%、数二4.8%、数三4.27%——三卷全部进本编前二。折 成分数：数一137 分、数二123 分、数三109 分，平均每年8.1 ／7.2 ／6.4 分。50 个题位里 23 个是解答题位，与L50 并列本编最多。 内部权重极不均匀，这一点必须先说清楚，因为它决定了本讲的复习顺序： 考点 题位 题型 数一 数二 数三 52.1 化标准形（配方法／正交变换法） 24 6 选2 填16 解 82 分 59 分 66 分 52.2 合同、惯性指数与规范形 22 11 选6 填5 解 28 分 64 分 37 分 52.3 正定二次型与正定矩阵 4 1 选1 填2 解 27 分 0 分 5 分 「化标准形」单独就是数一单考点分值榜的第7 名（82 分），数三榜上也占一席（66 分）；数二则 是「合同与惯性指数」更强（64 分，进数二单考点榜）。而正定二次型十七年只出了4 道题、数 二一分没考过——数一那27 分还全部是大题第二问的附属结论，不是独立题型。",
    "subsections": [
      "矩阵表示与三种关系",
      "化标准形的两条路线",
      "标准形、规范形与惯性指数",
      "正定二次型",
      "进阶：半正定与矩阵的平方根",
      "本讲小结"
    ],
    "stats": {
      "independentQuestions": 29,
      "positions": 50,
      "choiceCount": 18,
      "blankCount": 9,
      "solutionCount": 23,
      "math1Score": 138,
      "math2Score": 122,
      "math3Score": 109,
      "math1Percent": "5.41%",
      "math2Percent": "4.78%",
      "math3Percent": "4.27%",
      "avgDifficulty": "★★★★☆"
    },
    "methodCards": [
      {
        "title": "二次型 核心方法梳理",
        "subtitle": "涵盖 6 个进阶小节",
        "content": "本讲重点掌握 矩阵表示与三种关系、化标准形的两条路线、标准形、规范形与惯性指数、正定二次型 等核心知识链路，严格对齐考研大纲要求与历年命题规律。"
      }
    ],
    "pitfalls": [
      "未看清本讲在三卷中的具体分值权重与适用标签（重点讲、统考必考）。",
      "忽略定理适用的前提条件（如开闭区间、可导性、正交性或独立性前提）。"
    ],
    "mappedTopicIds": [
      "xiandai-07-quadratic-form-matrix-representation",
      "xiandai-07-canonical-standard-form-methods",
      "xiandai-07-positive-definite-criteria"
    ]
  },
  {
    "id": "L53",
    "num": 53,
    "title": "大串讲：五条主线的语言互译",
    "partNum": 5,
    "partTitle": "第 5 编 线性代数",
    "page": 923,
    "pageEnd": 933,
    "isKey": false,
    "isCompressed": false,
    "isMath1Only": false,
    "isMath2Heavy": false,
    "isMath3Only": false,
    "isMethod": true,
    "tags": [
      "方法课",
      "统考必考"
    ],
    "orientation": "本讲名下没有一道真题——它不是考点，是把前十讲焊在一起的方法课。线代大题之所 以让人觉得“看不懂题在问什么”，是因为同一件事有好几套说法。本讲做两件事：把这些说法整 理成五条语言链；用2010–2026 的真实统计告诉你第5 编的钱在哪儿、按你的卷种该照什么顺序 补。 先给一个总量：第5 编（L43–L52）十七年占三卷的比重几乎完全相同——数一2",
    "subsections": [
      "五条语言链",
      "第 5 编的真题地形图",
      "翻译演练",
      "本编收官清单"
    ],
    "stats": {
      "independentQuestions": 0,
      "positions": 0,
      "choiceCount": 0,
      "blankCount": 0,
      "solutionCount": 0,
      "math1Score": 0,
      "math2Score": 0,
      "math3Score": 0,
      "math1Percent": "0.00%",
      "math2Percent": "0.00%",
      "math3Percent": "0.00%",
      "avgDifficulty": "★★☆☆☆"
    },
    "methodCards": [
      {
        "title": "大串讲：五条主线的语言互译总表",
        "subtitle": "几何 ⇄ 向量 ⇄ 方程 ⇄ 矩阵 ⇄ 二次型",
        "content": "几何共线垂直 ⇄ 向量线性相关正交 ⇄ 方程组有非零解与解的结构 ⇄ 矩阵秩与初等变换相似对角化 ⇄ 二次型正负惯性指数合同正定。五套语言一一等价翻译。"
      }
    ],
    "pitfalls": [
      "未看清本讲在三卷中的具体分值权重与适用标签（方法课、统考必考）。",
      "忽略定理适用的前提条件（如开闭区间、可导性、正交性或独立性前提）。"
    ],
    "mappedTopicIds": [
      "xiandai-08-cross-linear-algebra-mastery"
    ]
  },
  {
    "id": "L54",
    "num": 54,
    "title": "随机事件与概率",
    "partNum": 6,
    "partTitle": "第 6 编 概率论与数理统计",
    "page": 933,
    "pageEnd": 949,
    "isKey": false,
    "isCompressed": false,
    "isMath1Only": false,
    "isMath2Heavy": false,
    "isMath3Only": false,
    "isMethod": false,
    "tags": [
      "统考必考"
    ],
    "orientation": "本讲17 年有16 道独立题、24 个卷面题位，13 选11 填，解答题0 道——2010–2026 十七年，这一讲没有出过一道大题。数一占",
    "subsections": [
      "事件运算",
      "条件概率：本讲真正的主战场",
      "全概率公式与贝叶斯公式",
      "独立性的两个层次",
      "本讲小结"
    ],
    "stats": {
      "independentQuestions": 16,
      "positions": 24,
      "choiceCount": 13,
      "blankCount": 11,
      "solutionCount": 0,
      "math1Score": 48,
      "math2Score": 0,
      "math3Score": 56,
      "math1Percent": "1.88%",
      "math2Percent": "0.00%",
      "math3Percent": "2.20%",
      "avgDifficulty": "★★★☆☆"
    },
    "methodCards": [
      {
        "title": "随机事件与概率 核心方法梳理",
        "subtitle": "涵盖 5 个进阶小节",
        "content": "本讲重点掌握 事件运算、条件概率：本讲真正的主战场、全概率公式与贝叶斯公式、独立性的两个层次 等核心知识链路，严格对齐考研大纲要求与历年命题规律。"
      }
    ],
    "pitfalls": [
      "未看清本讲在三卷中的具体分值权重与适用标签（统考必考）。",
      "忽略定理适用的前提条件（如开闭区间、可导性、正交性或独立性前提）。"
    ],
    "mappedTopicIds": [
      "gailv-01-random-events-conditional-prob",
      "gailv-01-total-probability-bayes",
      "gailv-01-event-independence-bernoulli"
    ]
  },
  {
    "id": "L55",
    "num": 55,
    "title": "一维随机变量及其分布",
    "partNum": 6,
    "partTitle": "第 6 编 概率论与数理统计",
    "page": 949,
    "pageEnd": 963,
    "isKey": false,
    "isCompressed": false,
    "isMath1Only": false,
    "isMath2Heavy": false,
    "isMath3Only": false,
    "isMethod": false,
    "tags": [
      "统考必考"
    ],
    "orientation": "17 年9 道独立题、16 个卷面题位，其中15 个是选择题、1 个填空，解答题位是0。 数一占",
    "subsections": [
      "分布函数：两类随机变量共用的语言",
      "两条分支：离散型与连续型",
      "常见的离散分布：五个",
      "常见的连续分布：均匀、指数、正态",
      "本讲小结"
    ],
    "stats": {
      "independentQuestions": 9,
      "positions": 16,
      "choiceCount": 15,
      "blankCount": 1,
      "solutionCount": 0,
      "math1Score": 38,
      "math2Score": 0,
      "math3Score": 30,
      "math1Percent": "1.49%",
      "math2Percent": "0.00%",
      "math3Percent": "1.18%",
      "avgDifficulty": "★★★☆☆"
    },
    "methodCards": [
      {
        "title": "一维随机变量及其分布 核心方法梳理",
        "subtitle": "涵盖 5 个进阶小节",
        "content": "本讲重点掌握 分布函数：两类随机变量共用的语言、两条分支：离散型与连续型、常见的离散分布：五个、常见的连续分布：均匀、指数、正态 等核心知识链路，严格对齐考研大纲要求与历年命题规律。"
      }
    ],
    "pitfalls": [
      "未看清本讲在三卷中的具体分值权重与适用标签（统考必考）。",
      "忽略定理适用的前提条件（如开闭区间、可导性、正交性或独立性前提）。"
    ],
    "mappedTopicIds": [
      "gailv-02-cdf-properties",
      "gailv-02-common-discrete-distributions",
      "gailv-02-common-continuous-distributions"
    ]
  },
  {
    "id": "L56",
    "num": 56,
    "title": "随机变量函数的分布",
    "partNum": 6,
    "partTitle": "第 6 编 概率论与数理统计",
    "page": 963,
    "pageEnd": 971,
    "isKey": false,
    "isCompressed": true,
    "isMath1Only": false,
    "isMath2Heavy": false,
    "isMath3Only": false,
    "isMethod": false,
    "tags": [
      "压缩讲",
      "统考必考"
    ],
    "orientation": "全书题位最少的一讲：17 年只有1 道独立题、1 个卷面题位，就是2013 数一22 那 道解答题。数一累计10.4 分（每年0.6 分），数二数三0 分，难度3.0。 这个1 需要解释，否则会误导你：“求Y = g(X) 的分布”这个动作在真题里出现得很多， 但它极少是题目的落点。近年的大题几乎都把它放在第一问，第二问接着问E(Y )——按落点分类， 那些题整道记在L59 数字特征名下（2021 数一／数三22 的随机分点、2025 数一／数三22 的保 险赔付额、2023 数三22 的分布函数变换都是）。剩下真正“只问分布、不问期望”的，十七年就 这一道。 所以本讲的定位是：一套必须会写、但很少单独计分的手工动作。用半天练熟这套四步的分 布函数法，然后到L59 去用它。",
    "subsections": [
      "离散型",
      "分布函数法：真题的唯一路线",
      "三种延伸形态（落点都在 L59）",
      "公式法：只在严格单调的分支上才成立",
      "本讲小结"
    ],
    "stats": {
      "independentQuestions": 1,
      "positions": 1,
      "choiceCount": 0,
      "blankCount": 0,
      "solutionCount": 1,
      "math1Score": 10,
      "math2Score": 0,
      "math3Score": 0,
      "math1Percent": "0.39%",
      "math2Percent": "0.00%",
      "math3Percent": "0.00%",
      "avgDifficulty": "★★☆☆☆"
    },
    "methodCards": [
      {
        "title": "随机变量函数的分布 核心方法梳理",
        "subtitle": "涵盖 5 个进阶小节",
        "content": "本讲重点掌握 离散型、分布函数法：真题的唯一路线、三种延伸形态（落点都在 L59）、公式法：只在严格单调的分支上才成立 等核心知识链路，严格对齐考研大纲要求与历年命题规律。"
      }
    ],
    "pitfalls": [
      "未看清本讲在三卷中的具体分值权重与适用标签（压缩讲、统考必考）。",
      "忽略定理适用的前提条件（如开闭区间、可导性、正交性或独立性前提）。"
    ],
    "mappedTopicIds": [
      "gailv-02-distribution-function-method"
    ]
  },
  {
    "id": "L57",
    "num": 57,
    "title": "二维随机变量",
    "partNum": 6,
    "partTitle": "第 6 编 概率论与数理统计",
    "page": 971,
    "pageEnd": 987,
    "isKey": false,
    "isCompressed": false,
    "isMath1Only": false,
    "isMath2Heavy": false,
    "isMath3Only": false,
    "isMethod": false,
    "tags": [
      "统考必考"
    ],
    "orientation": "17 年7 道独立题、9 个卷面题位，其中4 个是解答题位。数三占",
    "subsections": [
      "联合分布",
      "边缘分布",
      "条件分布：真题的真正主线",
      "独立性",
      "两个重要的二维分布",
      "本讲小结"
    ],
    "stats": {
      "independentQuestions": 7,
      "positions": 9,
      "choiceCount": 2,
      "blankCount": 3,
      "solutionCount": 4,
      "math1Score": 23,
      "math2Score": 0,
      "math3Score": 39,
      "math1Percent": "0.90%",
      "math2Percent": "0.00%",
      "math3Percent": "1.53%",
      "avgDifficulty": "★★★☆☆"
    },
    "methodCards": [
      {
        "title": "二维随机变量 核心方法梳理",
        "subtitle": "涵盖 6 个进阶小节",
        "content": "本讲重点掌握 联合分布、边缘分布、条件分布：真题的真正主线、独立性 等核心知识链路，严格对齐考研大纲要求与历年命题规律。"
      }
    ],
    "pitfalls": [
      "未看清本讲在三卷中的具体分值权重与适用标签（统考必考）。",
      "忽略定理适用的前提条件（如开闭区间、可导性、正交性或独立性前提）。"
    ],
    "mappedTopicIds": [
      "gailv-03-joint-marginal-distributions",
      "gailv-03-conditional-distribution-independence"
    ]
  },
  {
    "id": "L58",
    "num": 58,
    "title": "二维随机变量函数的分布",
    "partNum": 6,
    "partTitle": "第 6 编 概率论与数理统计",
    "page": 987,
    "pageEnd": 999,
    "isKey": false,
    "isCompressed": false,
    "isMath1Only": false,
    "isMath2Heavy": false,
    "isMath3Only": false,
    "isMethod": false,
    "tags": [
      "统考必考"
    ],
    "orientation": "17 年8 道独立题、11 个卷面题位，3 个解答题位、8 个选择题位，平均难度3.25—— 本编最高。全讲数一占",
    "subsections": [
      "通法：分布函数法",
      "混合型（一离散一连续）：解答题的唯一形态",
      "Z=X+Y 的卷积公式",
      "独立正态的线性组合：卷积算完留下的现成结果",
      "其余的连续型：选择题的另一半",
      "与 ：零命题的一节",
      "本讲小结"
    ],
    "stats": {
      "independentQuestions": 8,
      "positions": 11,
      "choiceCount": 8,
      "blankCount": 0,
      "solutionCount": 3,
      "math1Score": 35,
      "math2Score": 0,
      "math3Score": 33,
      "math1Percent": "1.37%",
      "math2Percent": "0.00%",
      "math3Percent": "1.29%",
      "avgDifficulty": "★★★☆☆"
    },
    "methodCards": [
      {
        "title": "二维随机变量函数的分布 核心方法梳理",
        "subtitle": "涵盖 7 个进阶小节",
        "content": "本讲重点掌握 通法：分布函数法、混合型（一离散一连续）：解答题的唯一形态、Z=X+Y 的卷积公式、独立正态的线性组合：卷积算完留下的现成结果 等核心知识链路，严格对齐考研大纲要求与历年命题规律。"
      }
    ],
    "pitfalls": [
      "未看清本讲在三卷中的具体分值权重与适用标签（统考必考）。",
      "忽略定理适用的前提条件（如开闭区间、可导性、正交性或独立性前提）。"
    ],
    "mappedTopicIds": [
      "gailv-03-discrete-continuous-mixed-variables",
      "gailv-03-convolution-formula-sum"
    ]
  },
  {
    "id": "L59",
    "num": 59,
    "title": "数字特征",
    "partNum": 6,
    "partTitle": "第 6 编 概率论与数理统计",
    "page": 999,
    "pageEnd": 1027,
    "isKey": true,
    "isCompressed": false,
    "isMath1Only": false,
    "isMath2Heavy": false,
    "isMath3Only": false,
    "isMethod": false,
    "tags": [
      "重点讲",
      "统考必考"
    ],
    "orientation": "全书单讲分值第一的一讲。17 年真题里本讲名下有47 道独立题、60 个卷面题位，数 一占卷面总分7.76%（合计198 分，平均每年1",
    "subsections": [
      "59.1 期望与方差",
      "59.2 协方差、相关系数与不相关",
      "59.3 条件期望与全期望公式",
      "59.4 矩与切比雪夫不等式",
      "本讲小结"
    ],
    "stats": {
      "independentQuestions": 47,
      "positions": 60,
      "choiceCount": 21,
      "blankCount": 15,
      "solutionCount": 24,
      "math1Score": 198,
      "math2Score": 0,
      "math3Score": 223,
      "math1Percent": "7.76%",
      "math2Percent": "0.00%",
      "math3Percent": "8.75%",
      "avgDifficulty": "★★★★☆"
    },
    "methodCards": [
      {
        "title": "数字特征 核心方法梳理",
        "subtitle": "涵盖 5 个进阶小节",
        "content": "本讲重点掌握 59.1 期望与方差、59.2 协方差、相关系数与不相关、59.3 条件期望与全期望公式、59.4 矩与切比雪夫不等式 等核心知识链路，严格对齐考研大纲要求与历年命题规律。"
      }
    ],
    "pitfalls": [
      "未看清本讲在三卷中的具体分值权重与适用标签（重点讲、统考必考）。",
      "忽略定理适用的前提条件（如开闭区间、可导性、正交性或独立性前提）。"
    ],
    "mappedTopicIds": [
      "gailv-04-expectation-variance-properties",
      "gailv-04-covariance-correlation-coefficient",
      "gailv-04-chebyshev-inequality"
    ]
  },
  {
    "id": "L60",
    "num": 60,
    "title": "大数定律与中心极限定理",
    "partNum": 6,
    "partTitle": "第 6 编 概率论与数理统计",
    "page": 1027,
    "pageEnd": 1035,
    "isKey": false,
    "isCompressed": true,
    "isMath1Only": false,
    "isMath2Heavy": false,
    "isMath3Only": false,
    "isMethod": false,
    "tags": [
      "压缩讲",
      "统考必考"
    ],
    "orientation": "全书性价比最低的一讲，没有之一。2010–2026 年51 套卷、1155 个卷面题位里，本讲 名下只有2 道题，而且都是选择题：2022 数三9（大数定律求依概率极限，5 分）、2020 数一8 （中心极限定理近似，4 分）。三卷合计9 分。数一17 年占卷面总分的0.16%、数三0.2%、数二 不考本编。平均难度2.0，是本编最低的一档。 换成人话：数一考生17 年里在这一讲上一共遇到过1 道题，数三考生也是1 道，两道都是 套一个公式就能选出答案的送分题。 另外，切比雪夫不等式不在本讲：真题分类里它归在考点59.4「矩、切比雪夫不等式」下，也 就是L59，17 年在那里出过1 道（2022 数一9），需要时回L59 看。 所以本讲的正确用法是：把下面两道真题看完，就可以走。",
    "subsections": [
      "先分清：这道题该用哪一个",
      "大数定律：只需要一个动作",
      "中心极限定理：三步走",
      "本讲小结"
    ],
    "stats": {
      "independentQuestions": 2,
      "positions": 2,
      "choiceCount": 2,
      "blankCount": 0,
      "solutionCount": 0,
      "math1Score": 4,
      "math2Score": 0,
      "math3Score": 5,
      "math1Percent": "0.16%",
      "math2Percent": "0.00%",
      "math3Percent": "0.20%",
      "avgDifficulty": "★★☆☆☆"
    },
    "methodCards": [
      {
        "title": "大数定律与中心极限定理 核心方法梳理",
        "subtitle": "涵盖 4 个进阶小节",
        "content": "本讲重点掌握 先分清：这道题该用哪一个、大数定律：只需要一个动作、中心极限定理：三步走、本讲小结 等核心知识链路，严格对齐考研大纲要求与历年命题规律。"
      }
    ],
    "pitfalls": [
      "未看清本讲在三卷中的具体分值权重与适用标签（压缩讲、统考必考）。",
      "忽略定理适用的前提条件（如开闭区间、可导性、正交性或独立性前提）。"
    ],
    "mappedTopicIds": [
      "gailv-05-law-of-large-numbers",
      "gailv-05-central-limit-theorem"
    ]
  },
  {
    "id": "L61",
    "num": 61,
    "title": "数理统计基础",
    "partNum": 6,
    "partTitle": "第 6 编 概率论与数理统计",
    "page": 1035,
    "pageEnd": 1045,
    "isKey": false,
    "isCompressed": false,
    "isMath1Only": false,
    "isMath2Heavy": false,
    "isMath3Only": false,
    "isMethod": false,
    "tags": [
      "统考必考"
    ],
    "orientation": "从这一讲开始进入数理统计。17 年真题里本讲名下有9 道独立题、11 个卷面题位，数 一占卷面总分0.51%（合计13 分，平均每年0.76 分），数三",
    "subsections": [
      "总体、样本、统计量与样本矩",
      "三大抽样分布（本讲主力）",
      "正态总体的抽样分布总表",
      "本讲小结"
    ],
    "stats": {
      "independentQuestions": 9,
      "positions": 11,
      "choiceCount": 10,
      "blankCount": 1,
      "solutionCount": 0,
      "math1Score": 13,
      "math2Score": 0,
      "math3Score": 34,
      "math1Percent": "0.51%",
      "math2Percent": "0.00%",
      "math3Percent": "1.33%",
      "avgDifficulty": "★★★☆☆"
    },
    "methodCards": [
      {
        "title": "数理统计基础 核心方法梳理",
        "subtitle": "涵盖 4 个进阶小节",
        "content": "本讲重点掌握 总体、样本、统计量与样本矩、三大抽样分布（本讲主力）、正态总体的抽样分布总表、本讲小结 等核心知识链路，严格对齐考研大纲要求与历年命题规律。"
      }
    ],
    "pitfalls": [
      "未看清本讲在三卷中的具体分值权重与适用标签（统考必考）。",
      "忽略定理适用的前提条件（如开闭区间、可导性、正交性或独立性前提）。"
    ],
    "mappedTopicIds": [
      "gailv-06-population-sample-statistics",
      "gailv-06-three-sampling-distributions"
    ]
  },
  {
    "id": "L62",
    "num": 62,
    "title": "参数估计",
    "partNum": 6,
    "partTitle": "第 6 编 概率论与数理统计",
    "page": 1045,
    "pageEnd": 1067,
    "isKey": true,
    "isCompressed": false,
    "isMath1Only": false,
    "isMath2Heavy": false,
    "isMath3Only": false,
    "isMethod": false,
    "tags": [
      "重点讲",
      "统考必考"
    ],
    "orientation": "数一全书分值第二高的一讲（仅次于L59 数字特征）。17 年真题里本讲名下有19 道 独立题、32 个卷面题位，数一占卷面总分6.43%（合计164 分，平均每年9.6 分），数三5.14% （合计131 分，平均每年7.7 分，数三排行榜第四）。数二不考本编。 而且题型结构比分值本身更说明问题：32 个题位里解答题有24 个，占75%。这一讲不是 拿来“选对”的，是拿来完整写出十到十二分的。更直白一点：数一17 年里有14 年、数三有 10 年，全卷的最后一道大题就是本讲的题（旧卷第23 题、新卷第22 题，位置一次没变过）。它 和L59 数字特征两讲相加，数一14.2%、数三13.9%——本编近三分之二的分在这两讲。 本讲正文按三节走，顺序固定，不要跳读： 节 内容 独立题/ 题位 你要练到什么程度 62.1 矩估计 0 道/ 0 个 会写，两行收工 62.2 最大似然估计 9 道/ 16 个 四步默写，动笔写完整 62.3 估计量的评价 10 道/ 16 个 三条标准会判、会算 这个顺序不是随便排的：矩估计是最短的动作，先学它是为了让你看清“估计”到底在干什么；最 大似然是本讲的分值主体；估计量的评价则是回头审视“估出来的东西好不好”。考场上那道大题 往往就是按这个顺序分成三问的。",
    "subsections": [
      "62.1 矩估计",
      "62.2 最大似然估计",
      "62.3 估计量的评价：无偏性、有效性、一致性",
      "本讲小结"
    ],
    "stats": {
      "independentQuestions": 19,
      "positions": 32,
      "choiceCount": 6,
      "blankCount": 2,
      "solutionCount": 24,
      "math1Score": 164,
      "math2Score": 0,
      "math3Score": 131,
      "math1Percent": "6.43%",
      "math2Percent": "0.00%",
      "math3Percent": "5.14%",
      "avgDifficulty": "★★★★☆"
    },
    "methodCards": [
      {
        "title": "参数估计 核心方法梳理",
        "subtitle": "涵盖 4 个进阶小节",
        "content": "本讲重点掌握 62.1 矩估计、62.2 最大似然估计、62.3 估计量的评价：无偏性、有效性、一致性、本讲小结 等核心知识链路，严格对齐考研大纲要求与历年命题规律。"
      }
    ],
    "pitfalls": [
      "未看清本讲在三卷中的具体分值权重与适用标签（重点讲、统考必考）。",
      "忽略定理适用的前提条件（如开闭区间、可导性、正交性或独立性前提）。"
    ],
    "mappedTopicIds": [
      "gailv-07-moment-and-mle-estimation",
      "gailv-07-unbiasedness-eval-criteria"
    ]
  },
  {
    "id": "L63",
    "num": 63,
    "title": "区间估计与假设检验",
    "partNum": 6,
    "partTitle": "第 6 编 概率论与数理统计",
    "page": 1067,
    "pageEnd": 1079,
    "isKey": false,
    "isCompressed": true,
    "isMath1Only": true,
    "isMath2Heavy": false,
    "isMath3Only": false,
    "isMethod": false,
    "tags": [
      "压缩讲",
      "数一专属"
    ],
    "orientation": "本讲只有数一考，而且是全书最该被压缩的几讲之一。2010–2026 年51 套卷、1155 个卷面题位里，本讲名下只有4 道题、4 个卷面题位：区间估计1 道填空（2016 数一14），假设 检验3 道选择（2018 数一8、2021 数一10、2025 数一10）。17 年0 道解答题。数一合计18 分， 占卷面总分0.71%，平均每年",
    "subsections": [
      "一个枢轴量，两种读法",
      "区间估计：把枢轴量反解开",
      "假设检验：固定六步",
      "本讲小结"
    ],
    "stats": {
      "independentQuestions": 4,
      "positions": 4,
      "choiceCount": 3,
      "blankCount": 1,
      "solutionCount": 0,
      "math1Score": 18,
      "math2Score": 0,
      "math3Score": 0,
      "math1Percent": "0.71%",
      "math2Percent": "0.00%",
      "math3Percent": "0.00%",
      "avgDifficulty": "★★☆☆☆"
    },
    "methodCards": [
      {
        "title": "区间估计与假设检验 核心方法梳理",
        "subtitle": "涵盖 4 个进阶小节",
        "content": "本讲重点掌握 一个枢轴量，两种读法、区间估计：把枢轴量反解开、假设检验：固定六步、本讲小结 等核心知识链路，严格对齐考研大纲要求与历年命题规律。"
      }
    ],
    "pitfalls": [
      "未看清本讲在三卷中的具体分值权重与适用标签（压缩讲、数一专属）。",
      "忽略定理适用的前提条件（如开闭区间、可导性、正交性或独立性前提）。"
    ],
    "mappedTopicIds": [
      "gailv-08-confidence-interval-hypothesis-test"
    ]
  },
  {
    "id": "L64",
    "num": 64,
    "title": "卷面结构与时间分配",
    "partNum": 7,
    "partTitle": "第 7 编 应试工程",
    "page": 1079,
    "pageEnd": 1089,
    "isKey": false,
    "isCompressed": false,
    "isMath1Only": false,
    "isMath2Heavy": false,
    "isMath3Only": false,
    "isMethod": true,
    "tags": [
      "方法课",
      "统考必考"
    ],
    "orientation": "考前一个月听。本讲不教数学，教怎么在180 分钟里把会做的题全部变成分数。 数",
    "subsections": [
      "一、卷面结构：两种骨架与三卷的板块坐标",
      "二、三卷各自的难度地形",
      "三、时间分配：两个参数决定的方案",
      "四、每卷的解答题分数集中在哪里",
      "五、解答题的踩分书写",
      "六、本讲小结"
    ],
    "stats": {
      "independentQuestions": 0,
      "positions": 0,
      "choiceCount": 0,
      "blankCount": 0,
      "solutionCount": 0,
      "math1Score": 0,
      "math2Score": 0,
      "math3Score": 0,
      "math1Percent": "0.00%",
      "math2Percent": "0.00%",
      "math3Percent": "0.00%",
      "avgDifficulty": "★★☆☆☆"
    },
    "methodCards": [
      {
        "title": "180分钟卷面黄金时间分配与踩分规范",
        "subtitle": "选填65分钟 · 大题85分钟 · 检查30分钟",
        "content": "选择填空单题控制在3-4分钟，卡壳超5分钟立刻跳过；大题按踩分点书写，首句写定理依据与设元，中间写核心变形，末句写最终答案。"
      }
    ],
    "pitfalls": [
      "未看清本讲在三卷中的具体分值权重与适用标签（方法课、统考必考）。",
      "忽略定理适用的前提条件（如开闭区间、可导性、正交性或独立性前提）。"
    ],
    "mappedTopicIds": [
      "yingshi-64-exam-time-structure"
    ]
  },
  {
    "id": "L65",
    "num": 65,
    "title": "计算失误清单",
    "partNum": 7,
    "partTitle": "第 7 编 应试工程",
    "page": 1089,
    "pageEnd": 1097,
    "isKey": false,
    "isCompressed": false,
    "isMath1Only": false,
    "isMath2Heavy": false,
    "isMath3Only": false,
    "isMethod": true,
    "tags": [
      "方法课",
      "统考必考"
    ],
    "orientation": "投入产出比最高的一讲。考研数学丢分的最大来源不是不会，而是会了算错。 这一讲不是知识点罗列，是一份提交答案前的动作清单：每一条都写成你在考场上能真的做 出来的一个动作（重读、圈出、回代、验一眼），后面跟着这个动作挡住的那种失误，再跟着一道 可以回去复盘的题。 易错/ 提醒 怎么用这份清单。",
    "subsections": [
      "一、读题错误：交卷前先把题干再读一遍",
      "二、建模错误：把题目翻译成式子的那一步",
      "三、方法选择错误：选路之前停三秒",
      "四、计算错误：算完立刻做的三个动作",
      "五、书写失分：写完之后看一眼纸面",
      "六、两条不必画正字的"
    ],
    "stats": {
      "independentQuestions": 0,
      "positions": 0,
      "choiceCount": 0,
      "blankCount": 0,
      "solutionCount": 0,
      "math1Score": 0,
      "math2Score": 0,
      "math3Score": 0,
      "math1Percent": "0.00%",
      "math2Percent": "0.00%",
      "math3Percent": "0.00%",
      "avgDifficulty": "★★☆☆☆"
    },
    "methodCards": [
      {
        "title": "考场计算失误清单与交卷前动作表",
        "subtitle": "读题 · 建模 · 选方法 · 计算 · 书写 五步防漏",
        "content": "交卷前必做：1. 读题回头核对问极值还是极值点；2. 圈出二阶导与连续前置词；3. 极坐标检查r因子；4. 高斯公式核对曲面内外侧法向量定向；5. 矩阵初等变换左行右列。"
      }
    ],
    "pitfalls": [
      "未看清本讲在三卷中的具体分值权重与适用标签（方法课、统考必考）。",
      "忽略定理适用的前提条件（如开闭区间、可导性、正交性或独立性前提）。"
    ],
    "mappedTopicIds": [
      "yingshi-65-calculation-mistakes-checklist"
    ]
  },
  {
    "id": "L66",
    "num": 66,
    "title": "保命清单与进阶清单",
    "partNum": 7,
    "partTitle": "第 7 编 应试工程",
    "page": 1097,
    "pageEnd": 1105,
    "isKey": false,
    "isCompressed": false,
    "isMath1Only": false,
    "isMath2Heavy": false,
    "isMath3Only": false,
    "isMethod": true,
    "tags": [
      "方法课",
      "统考必考"
    ],
    "orientation": "最后一讲。给出两张清单，它们的分工不一样： • 保命清单只装一样东西：能稳定拿分的标准动作。每一条都是一个套路固定、见到就知道怎么 下笔的考点，每一条后面标着最低掌握层级——你至少要练到哪一档才算过关。清单里没有综 合迁移题，它们全部在第二张清单里。 • 进阶清单只装综合迁移题。它们的共同特征只有一个：跨讲拼装——一道题要同时调用两三讲 的东西，所以练单讲练不出来，必须按“拼装路线”练。 每一条后面都附了它在2010–2026 年真题里的题位数、解答题位数、该卷分值与平均难度，你 可以拿各讲的考频面板逐条核对。 易错/ 提醒 三档掌握层级（保命清单用）： • 会认：看到题面能立刻说出它考的是什么、该用哪个判据，选项能排除。适用于几乎只出 选择题的考点——练到这一档就够了，再往上是浪费。 • 会算：能在三四分钟内算出一个准确的数或式子。适用于选填为主的考点。 • 会写全过程：能把步骤、条件、结论按阅卷找得分点的方式写在答题纸上。只有解答题位 多的考点才需要练到这一档。 两张清单的划线规则：保命档= 分值可观、动作固定、平均难度≤3.0；进阶档= 分值可观、 必须跨讲拼装、平均难度多在3.2 以上。难度在3.0 与3.2 之间的考点里有三个必须点名：多 元函数的无条件极值（32.1，难3.06）与合同、惯性指数与规范形（52.2，难3.09）动作固定， 按保命档练；最大似然估计（62.2，难3.11）虽然动作也固定，但它每年都要和分布、期望拼 在一起出大题，所以列进进阶清单。 难度是真题库对每道题的1–5 评级按考点取的平均；全书118 个考点里有108 个挂着真题， 它们的难度中位数是2.87。 1081 Maki 的完美算术教室 L66 保命清单与进阶清单",
    "subsections": [
      "一、保命清单（目标 60–90 分）",
      "二、进阶清单（目标 120–140 分）",
      "三、两张清单各值多少分",
      "四、最后两周怎么安排"
    ],
    "stats": {
      "independentQuestions": 0,
      "positions": 0,
      "choiceCount": 0,
      "blankCount": 0,
      "solutionCount": 0,
      "math1Score": 0,
      "math2Score": 0,
      "math3Score": 0,
      "math1Percent": "0.00%",
      "math2Percent": "0.00%",
      "math3Percent": "0.00%",
      "avgDifficulty": "★★☆☆☆"
    },
    "methodCards": [
      {
        "title": "保命清单（60-90分）与进阶清单（120-140分）",
        "subtitle": "分档攻坚 · 冲刺收官",
        "content": "保命清单：等价无穷小、一元求导法则、基本积分表、齐次线性方程组基础解系、二次型配方法、数字特征期望方差速算；进阶清单：双中值证明、反常积分判敛、微分方程应用建模、空间曲线曲面积分。"
      }
    ],
    "pitfalls": [
      "未看清本讲在三卷中的具体分值权重与适用标签（方法课、统考必考）。",
      "忽略定理适用的前提条件（如开闭区间、可导性、正交性或独立性前提）。"
    ],
    "mappedTopicIds": [
      "yingshi-66-survival-and-advanced-checklist"
    ]
  }
];
