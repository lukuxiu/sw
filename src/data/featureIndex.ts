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
  category: '数一' | '数二' | '数三';
  questionNumber: string;
  source: string;
  prompt: string;
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
}

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

    // Collect papers and years from pastQuestions
    const paperSet = new Set<'数一' | '数二' | '数三'>();
    const yearSet = new Set<string>();

    const examples: FeatureExample[] = (node.pastQuestions || []).slice(0, 4).map((q) => {
      paperSet.add(q.category as ('数一' | '数二' | '数三'));
      yearSet.add(q.year);
      return {
        id: q.id,
        year: q.year,
        category: q.category as ('数一' | '数二' | '数三'),
        questionNumber: q.questionNumber,
        source: q.source,
        prompt: q.content,
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
      item.examples.some((ex) => 
        ex.prompt.toLowerCase().includes(q) || 
        ex.year.includes(q) ||
        ex.category.includes(q)
      )
    );
  });
}
