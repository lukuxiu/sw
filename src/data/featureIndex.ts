import { KNOWLEDGE_BASE } from './knowledgeBase';
import { SubjectId } from './types';

export type FeatureCategory = 
  | 'all'
  | '极限与连续'
  | '微分与中值定理'
  | '积分与常微分方程'
  | '多元与多元微积分'
  | '级数与空间几何'
  | '行列式与矩阵'
  | '方程组与向量组'
  | '特征值与二次型'
  | '随机变量与分布'
  | '数理统计与参数估计'
  | '应试工程与备考策略';

export interface FeatureExample {
  id: string;
  year: string;
  category: string;
  questionNumber: string;
  source: string;
  prompt: string;
  options?: string[];
  keyReaction: string;
  answer: string;
  difficulty: string;
}

export interface FeatureItem {
  id: string;
  topicId: string;
  topicTitle: string;
  subjectId: SubjectId;
  subjectName: string;
  chapterTitle: string;
  category: FeatureCategory;
  trigger: string;
  firstReaction: string;
  primaryMethod: string;
  whyChoose: string;
  pitfalls?: string[];
  papers: ('数一' | '数二' | '数三')[];
  recentYears: string[];
  examples: FeatureExample[];
  metaMethodId?: string;
  metaMethodName?: string;
}

export const TOPIC_TO_META_METHOD: Record<string, { id: string; name: string }> = {
  'gaoshu-03-definite-integral-symmetry': { id: 'meta-symmetry', name: '对称性法则' },
  'gaoshu-06-order-exchange-symmetry': { id: 'meta-symmetry', name: '对称性法则' },
  'gaoshu-07-first-kind-curve-surface': { id: 'meta-symmetry', name: '对称性法则' },
  'xiandai-06-real-symmetric-orthogonal-diag': { id: 'meta-symmetry', name: '对称性法则' },
  'gailv-02-normal-distribution-symmetry': { id: 'meta-symmetry', name: '对称性法则' },

  'gaoshu-02-rolle-lagrange-cauchy': { id: 'meta-auxiliary', name: '构造辅助函数' },
  'gaoshu-02-inequality-and-roots': { id: 'meta-auxiliary', name: '构造辅助函数' },
  'gaoshu-03-variable-limit-integral': { id: 'meta-auxiliary', name: '构造辅助函数' },

  'gaoshu-06-polar-coordinates': { id: 'meta-substitution', name: '变量代换与解耦' },
  'gaoshu-04-second-order-linear-ode': { id: 'meta-substitution', name: '变量代换与解耦' },
  'xiandai-07-quadratic-form-canonical': { id: 'meta-substitution', name: '变量代换与解耦' },
  'gailv-03-random-variable-functions-2d': { id: 'meta-substitution', name: '变量代换与解耦' },

  'gaoshu-01-indeterminate-0-0': { id: 'meta-taylor', name: '泰勒展开局部逼近' },
  'gaoshu-08-series-convergence-tests': { id: 'meta-taylor', name: '泰勒展开局部逼近' },
  'gaoshu-02-taylor-formula-peano-lagrange': { id: 'meta-taylor', name: '泰勒展开局部逼近' },

  'xiandai-05-eigenvalues-eigenvectors': { id: 'meta-eigen', name: '特征分析与矩阵方幂' },
  'xiandai-06-matrix-diagonalization-criterion': { id: 'meta-eigen', name: '特征分析与矩阵方幂' },
  'xiandai-07-positive-definite-criteria': { id: 'meta-eigen', name: '特征分析与矩阵方幂' },

  'gaoshu-07-green-formula': { id: 'meta-complement', name: '反面法与挖洞补面' },
  'gaoshu-07-gauss-divergence-theorem': { id: 'meta-complement', name: '反面法与挖洞补面' },
  'gailv-01-total-probability-bayes': { id: 'meta-complement', name: '反面法与挖洞补面' },

  'gaoshu-05-conditional-extrema-lagrange': { id: 'meta-lagrange', name: '拉格朗日乘数与最值' },
  'gailv-06-maximum-likelihood-estimation': { id: 'meta-lagrange', name: '拉格朗日乘数与最值' },

  'gaoshu-04-first-order-ode': { id: 'meta-integrating-factor', name: '积分因子与反求导' },

  'gaoshu-03-integration-methods': { id: 'meta-parts-recurrence', name: '分部降次与递推' },
  'gaoshu-08-power-series-sum-function': { id: 'meta-parts-recurrence', name: '分部降次与递推' },
  'xiandai-01-determinant-properties-calc': { id: 'meta-parts-recurrence', name: '分部降次与递推' },
  'gailv-02-common-continuous-distributions': { id: 'meta-parts-recurrence', name: '分部降次与递推' },

  'gaoshu-01-sequence-monotone-bounded': { id: 'meta-squeeze', name: '夹逼与放缩法' },
  'gailv-05-chebyshev-inequality': { id: 'meta-squeeze', name: '夹逼与放缩法' },
};

function categorizeChapter(chapterTitle: string): FeatureCategory {
  if (chapterTitle.includes('极限') || chapterTitle.includes('函数')) return '极限与连续';
  if (chapterTitle.includes('一元函数微分') || chapterTitle.includes('中值定理') || chapterTitle.includes('导数')) return '微分与中值定理';
  if (chapterTitle.includes('一元函数积分') || chapterTitle.includes('微分方程') || chapterTitle.includes('变限积分')) return '积分与常微分方程';
  if (chapterTitle.includes('多元') || chapterTitle.includes('重积分') || chapterTitle.includes('曲线') || chapterTitle.includes('曲面')) return '多元与多元微积分';
  if (chapterTitle.includes('级数') || chapterTitle.includes('空间') || chapterTitle.includes('向量代数')) return '级数与空间几何';
  if (chapterTitle.includes('行列式') || chapterTitle.includes('矩阵及其运算')) return '行列式与矩阵';
  if (chapterTitle.includes('向量组') || chapterTitle.includes('线性方程组')) return '方程组与向量组';
  if (chapterTitle.includes('特征值') || chapterTitle.includes('相似') || chapterTitle.includes('二次型')) return '特征值与二次型';
  if (chapterTitle.includes('随机事件') || chapterTitle.includes('一维随机') || chapterTitle.includes('多维') || chapterTitle.includes('数字特征') || chapterTitle.includes('大数')) return '随机变量与分布';
  if (chapterTitle.includes('统计') || chapterTitle.includes('估计')) return '数理统计与参数估计';
  if (chapterTitle.includes('应试工程') || chapterTitle.includes('失误清单') || chapterTitle.includes('时间分配') || chapterTitle.includes('保命')) return '应试工程与备考策略';
  return '极限与连续';
}

export function getAllFeatures(): FeatureItem[] {
  const items: FeatureItem[] = [];

  for (const [topicId, node] of Object.entries(KNOWLEDGE_BASE)) {
    const category = categorizeChapter(node.chapterTitle);
    const primaryMethod = node.candidateMethods[0]?.name || '标准推导法';
    const whyChoose = node.candidateMethods[0]?.whyChoose || '首选基准方法';
    const pitfalls = node.pitfalls || [];
    const metaInfo = TOPIC_TO_META_METHOD[topicId];

    // Collect papers and years from pastQuestions
    const paperSet = new Set<'数一' | '数二' | '数三'>();
    const yearSet = new Set<string>();

    const examples: FeatureExample[] = (node.pastQuestions || []).slice(0, 4).map((q) => {
      if (q.category.includes('数一')) paperSet.add('数一');
      if (q.category.includes('数二')) paperSet.add('数二');
      if (q.category.includes('数三')) paperSet.add('数三');
      yearSet.add(q.year);
      return {
        id: q.id,
        year: q.year,
        category: q.category,
        questionNumber: q.questionNumber,
        source: q.source,
        prompt: q.content,
        options: q.options,
        keyReaction: q.analysis,
        answer: q.answer || '详见解析',
        difficulty: q.difficulty,
      };
    });

    const papers = paperSet.size > 0 
      ? Array.from(paperSet) 
      : (['数一', '数二', '数三'] as ('数一' | '数二' | '数三')[]);
    const recentYears = Array.from(yearSet).sort().reverse();

    (node.triggers || []).forEach((trig, idx) => {
      items.push({
        id: `${topicId}-trig-${idx}`,
        topicId: node.id,
        topicTitle: node.title,
        subjectId: node.subject,
        subjectName: node.subjectName,
        chapterTitle: node.chapterTitle,
        category,
        trigger: trig,
        firstReaction: node.firstReaction,
        primaryMethod,
        whyChoose,
        pitfalls,
        papers,
        recentYears,
        examples,
        metaMethodId: metaInfo?.id,
        metaMethodName: metaInfo?.name,
      });
    });
  }

  return items;
}

export const ALL_FEATURES = getAllFeatures();

export function searchFeatures(
  query: string,
  category: FeatureCategory = 'all',
  paper: 'all' | '数一' | '数二' | '数三' = 'all',
  yearFilter: 'all' | 'recent' | 'classic' = 'all'
): FeatureItem[] {
  const q = query.trim().toLowerCase();

  return ALL_FEATURES.filter((item) => {
    // Category filter
    if (category !== 'all' && item.category !== category) return false;

    // Paper filter (数一 / 数二 / 数三)
    if (paper !== 'all' && !item.papers.includes(paper)) return false;

    // Year filter (recent: 2021~2026, classic: earlier)
    if (yearFilter === 'recent') {
      const hasRecent = item.recentYears.some((yr) => ['2021', '2022', '2023', '2024', '2025', '2026'].includes(yr));
      if (!hasRecent) return false;
    } else if (yearFilter === 'classic') {
      const hasClassic = item.recentYears.some((yr) => !['2021', '2022', '2023', '2024', '2025', '2026'].includes(yr));
      if (!hasClassic && item.recentYears.length > 0) return false;
    }

    // Search query
    if (!q) return true;
    return (
      item.trigger.toLowerCase().includes(q) ||
      item.firstReaction.toLowerCase().includes(q) ||
      item.primaryMethod.toLowerCase().includes(q) ||
      item.topicTitle.toLowerCase().includes(q) ||
      (item.metaMethodName && item.metaMethodName.toLowerCase().includes(q)) ||
      item.examples.some((ex) => 
        ex.prompt.toLowerCase().includes(q) || 
        ex.year.includes(q) ||
        ex.category.includes(q)
      )
    );
  });
}
