export type SubjectId = 'gaoshu' | 'xiandai' | 'gailv';

export type LearningStatus = 'unlearned' | 'struggling' | 'mastered';

export interface SubjectInfo {
  id: SubjectId;
  name: string;
  shortName: string;
  description: string;
  color: {
    primary: string;
    light: string;
    border: string;
    text: string;
    badge: string;
  };
  chapterIds: string[];
}

export interface ChapterInfo {
  id: string;
  subjectId: SubjectId;
  title: string;
  order: number;
  description: string;
  goals: string[];
  topicIds: string[];
}

export interface CandidateMethod {
  name: string;
  priority?: number;
  condition?: string;
  applicability?: string;
  whyChoose: string;
  description?: string;
  limitations?: string;
}

export interface FormulaItem {
  title: string;
  latex: string;
  notes?: string;
}

export type PastQuestionItem = PastQuestion;
export interface PastQuestion {
  id: string;
  year: string;
  category: string; // e.g., '数一' | '数二' | '数三'
  questionNumber: string; // e.g., '(1)' | '(15)'
  content: string; // Problem statement (with LaTeX)
  options?: string[]; // Multiple choice options if applicable
  analysis: string; // First breakdown & core idea
  solutionSteps: string[]; // Detailed derivations
  answer?: string; // Correct option or final result
  pitfall: string; // Common errors & check technique
  difficulty: string; // e.g., '★★☆☆☆'
  verified: boolean; // Must be true, no fabricated questions
  source: string; // Provenance in Maki materials
}

export interface VariantTest {
  id: string;
  question: string;
  hint: string;
  methodChoiceAnalysis: string;
  fullSolution: string[];
  keyTakeaway: string;
}

export interface KnowledgeNode {
  id: string;
  title: string;
  subject: SubjectId;
  subjectName: string;
  chapterId: string;
  chapterTitle: string;
  parentId?: string;
  nodeType: 'subject' | 'chapter' | 'topic' | 'method';
  summary: string; // 一句话记忆
  triggers: string[]; // 触发信号：题目出现哪些形式、条件、关键词或结构
  firstReaction: string; // 第一反应：看到题目后首先应该检查什么、尝试什么
  candidateMethods: CandidateMethod[]; // 方法选择与优先级
  applicability?: string; // 适用条件与易忽略限制
  steps: string[]; // 从特征到具体数学操作的详细步骤
  pitfalls: string[]; // 易错点分析
  formulas: FormulaItem[]; // 核心公式与速记结论
  exampleIds?: string[];
  pastQuestions: PastQuestion[]; // 历年真题
  variants: VariantTest[]; // 自测与变式
  relatedKnowledgeIds: string[]; // 相关考点与跨章节方法
  tags: string[]; // 标签
  source: string; // 讲义来源
  whyChooseMethod?: string;
  selfCheckList?: string[];
  isPending?: boolean; // 是否待补充
}

export interface SearchMatchItem {
  nodeId: string;
  title: string;
  subjectName: string;
  chapterTitle: string;
  matchedField: 'title' | 'summary' | 'trigger' | 'method' | 'formula' | 'question' | 'tag';
  snippet: string;
  subjectId: SubjectId;
}

export interface MindmapTreeNode {
  id: string;
  name: string;
  type: 'root' | 'subject' | 'chapter' | 'topic';
  subjectId?: SubjectId;
  chapterId?: string;
  nodeId?: string;
  children?: MindmapTreeNode[];
  isPending?: boolean;
}


export type MistakeTag =
  | '公式记错'
  | '计算失误'
  | '定义域/限制遗漏'
  | '分类讨论不全'
  | '突破口未想到';

export interface TopicRecord {
  status: LearningStatus;
  lastReviewedAt?: number;
  reviewCount?: number;
  mistakeTags?: string[];
  notes?: string;
}

export interface UniversalMetaMethod {
  id: string;
  name: string;
  subtitle: string;
  corePhilosophy: string;
  manifestations: {
    subjectId: SubjectId;
    subjectName: string;
    chapterTitle: string;
    topicId: string;
    topicTitle: string;
    triggerForm: string;
    coreAction: string;
  }[];
  commonPitfalls: string[];
}
