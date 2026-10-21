import React, { useState, useEffect, useMemo } from 'react';
import { 
  ArrowLeft, ArrowRight, ChevronLeft, Compass, Eye, EyeOff, Tag, CheckCircle2, Bookmark, Layers
} from 'lucide-react';
import { KNOWLEDGE_BASE } from '../data/knowledgeBase';
import { TOPIC_TO_META_METHOD } from '../data/featureIndex';
import { CHAPTERS, SUBJECTS } from '../data/subjects';
import { LearningStatus, MistakeTag, PastQuestion } from '../data/types';
import { getLearningStatus, setLearningStatus, getTopicRecord, setTopicMistakeTags } from '../data/storage';
import { MathView } from './MathView';

interface KnowledgeDetailViewProps {
  nodeId: string;
  onBackToChapter: (chapterId: string) => void;
  onBackToMindmap: () => void;
  onNavigateTopic: (nodeId: string) => void;
  onOpenMetaMethod?: (metaMethodId: string) => void;
}

const AVAILABLE_MISTAKE_TAGS: MistakeTag[] = [
  '公式记错',
  '计算失误',
  '定义域/限制遗漏',
  '分类讨论不全',
  '突破口未想到',
];

export const KnowledgeDetailView: React.FC<KnowledgeDetailViewProps> = ({
  nodeId,
  onBackToChapter,
  onBackToMindmap,
  onNavigateTopic,
  onOpenMetaMethod,
}) => {
  const node = KNOWLEDGE_BASE[nodeId] || KNOWLEDGE_BASE['gaoshu-01-indeterminate-0-0'];
  const chapter = CHAPTERS[node.chapterId] || CHAPTERS['gaoshu-ch01'];
  const subject = SUBJECTS[node.subject] || SUBJECTS['gaoshu'];

  const [status, setStatus] = useState<LearningStatus>(getLearningStatus(node.id));
  const [record, setRecord] = useState(getTopicRecord(node.id));
  const [revealedVariants, setRevealedVariants] = useState<Record<string, boolean>>({});
  const [revealedPastSolutions, setRevealedPastSolutions] = useState<Record<string, boolean>>({});
  const [pastPaperFilter, setPastPaperFilter] = useState<'all' | '数一' | '数二' | '数三'>('all');
  const [pastYearFilter, setPastYearFilter] = useState<'all' | 'recent' | 'classic'>('all');

  useEffect(() => {
    setStatus(getLearningStatus(node.id));
    setRecord(getTopicRecord(node.id));
    setRevealedVariants({});
    setRevealedPastSolutions({});
    setPastPaperFilter('all');
    setPastYearFilter('all');
    window.scrollTo({ top: 0, behavior: 'smooth' });
  }, [node.id]);

  const filteredPastQuestions = useMemo(() => {
    return (node.pastQuestions || []).filter((q) => {
      if (pastPaperFilter !== 'all' && !q.category.includes(pastPaperFilter)) return false;
      const yr = parseInt(q.year, 10) || 0;
      if (pastYearFilter === 'recent' && yr < 2021) return false;
      if (pastYearFilter === 'classic' && yr >= 2021) return false;
      return true;
    });
  }, [node.pastQuestions, pastPaperFilter, pastYearFilter]);

  const handleStatusChange = (newStatus: LearningStatus) => {
    setStatus(newStatus);
    setLearningStatus(node.id, newStatus);
    setRecord(getTopicRecord(node.id));
  };

  const scrollToSection = (id: string) => {
    const el = document.getElementById(id);
    if (el) {
      el.scrollIntoView({ behavior: 'smooth' });
    }
  };

  const handleToggleMistakeTag = (tag: MistakeTag) => {
    const currentTags = record.mistakeTags || [];
    const exists = currentTags.includes(tag);
    const newTags = exists
      ? currentTags.filter((t) => t !== tag)
      : [...currentTags, tag];
    setTopicMistakeTags(node.id, newTags as MistakeTag[]);
    setRecord(getTopicRecord(node.id));
  };

  const toggleVariantReveal = (varId: string) => {
    setRevealedVariants((prev) => ({ ...prev, [varId]: !prev[varId] }));
  };

  const togglePastSolutionReveal = (qid: string) => {
    setRevealedPastSolutions((prev) => ({ ...prev, [qid]: !prev[qid] }));
  };

  const currentChapterTopics = chapter.topicIds;
  const currentIndex = currentChapterTopics.indexOf(node.id);
  const prevTopicId = currentIndex > 0 ? currentChapterTopics[currentIndex - 1] : null;
  const nextTopicId =
    currentIndex >= 0 && currentIndex < currentChapterTopics.length - 1
      ? currentChapterTopics[currentIndex + 1]
      : null;

  return (
    <div className="min-h-[calc(100vh-56px)] bg-[var(--paper)] text-[var(--ink)] pb-20 font-body">
      {/* Top Breadcrumb & Status Bar */}
      <div className="sticky top-0 z-30 bg-[var(--sheet)] border-b border-[var(--line)] px-3 sm:px-6 lg:px-8 py-2 sm:py-2.5 shadow-xs">
        <div className="max-w-4xl mx-auto flex flex-wrap items-center justify-between gap-2.5 font-mono text-xs">
          {/* Breadcrumbs */}
          <div className="flex items-center space-x-1.5 sm:space-x-2 text-[var(--muted)] overflow-x-auto py-0.5">
            <button
              onClick={onBackToMindmap}
              className="flex items-center gap-1 text-[var(--blue)] hover:underline transition-colors flex-shrink-0"
            >
              <Compass className="w-3.5 h-3.5" />
              总导图
            </button>
            <span>/</span>
            <span className="flex-shrink-0">{subject.name}</span>
            <span>/</span>
            <button
              onClick={() => onBackToChapter(chapter.id)}
              className="text-[var(--muted)] hover:text-[var(--ink)] transition-colors flex-shrink-0"
            >
              {chapter.title}
            </button>
            <span>/</span>
            <span className="text-[var(--ink)] font-bold truncate max-w-[150px] sm:max-w-none">
              {node.title}
            </span>
          </div>

          {/* Quick Learning Status Switcher */}
          <div className="flex items-center gap-1.5 bg-[var(--well)] p-0.5 sm:p-1 rounded-[8px] border border-[var(--line)]">
            <span className="text-[11px] text-[var(--muted)] px-1 hidden sm:inline">掌握度:</span>
            <button
              onClick={() => handleStatusChange('unlearned')}
              className={`px-2.5 py-1 rounded-[6px] transition-colors ${
                status === 'unlearned'
                  ? 'bg-[var(--line)] text-[var(--ink)] font-bold'
                  : 'text-[var(--muted)] hover:text-[var(--ink)]'
              }`}
            >
              未掌握
            </button>
            <button
              onClick={() => handleStatusChange('struggling')}
              className={`px-2.5 py-1 rounded-[6px] transition-colors ${
                status === 'struggling'
                  ? 'bg-[var(--amber-bg)] text-[var(--amber)] font-bold border border-[var(--amber)]'
                  : 'text-[var(--muted)] hover:text-[var(--amber)]'
              }`}
            >
              <span className="hidden sm:inline">推导困难</span><span className="inline sm:hidden">困难</span>
            </button>
            <button
              onClick={() => handleStatusChange('mastered')}
              className={`px-2.5 py-1 rounded-[6px] transition-colors ${
                status === 'mastered'
                  ? 'bg-[var(--green-bg)] text-[var(--green)] font-bold border border-[var(--green)]'
                  : 'text-[var(--muted)] hover:text-[var(--green)]'
              }`}
            >
              <span className="hidden sm:inline">能够独立完成</span><span className="inline sm:hidden">已掌握</span>
            </button>
          </div>
        </div>
      </div>

      {/* Main Content Body */}
      <div className="max-w-4xl mx-auto px-3 sm:px-6 lg:px-8 mt-4 sm:mt-6 space-y-5 sm:space-y-7">
        
        {/* Title Header Card & First-Fold Anchor Quick Bar */}
        <div className="bg-[var(--sheet)] border border-[var(--line)] rounded-[14px] p-4 sm:p-6 lg:p-7 space-y-3 sm:space-y-4 shadow-xs">
          <div className="flex flex-wrap items-center gap-2 text-xs font-mono text-[var(--muted)]">
            <span className="px-2 py-0.5 rounded-[999px] bg-[var(--well)] border border-[var(--line)] text-[var(--ink)]">
              {subject.name} · 第 {chapter.order} 讲
            </span>
            {node.isPending && (
              <span className="px-2 py-0.5 rounded-[999px] bg-[var(--well)] border border-[var(--line)] text-[var(--muted)]">
                讲义待补充
              </span>
            )}
            <span className="ml-auto">
              出处: {node.source}
            </span>
          </div>

          <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-2">
            <h1 className="text-xl sm:text-2xl md:text-3xl font-display font-bold text-[var(--ink)] tracking-tight">
              {node.title}
            </h1>
            {TOPIC_TO_META_METHOD[node.id] && onOpenMetaMethod && (
              <button
                type="button"
                onClick={() => onOpenMetaMethod(TOPIC_TO_META_METHOD[node.id].id)}
                className="inline-flex items-center gap-1.5 px-3 py-1.5 rounded-[8px] bg-[var(--purple-bg)]/30 text-[var(--purple)] border border-[var(--purple)]/40 hover:bg-[var(--purple)] hover:text-white transition-colors cursor-pointer text-xs font-mono font-bold self-start sm:self-auto"
                title="查看该考点对应跨章节通用方法的完整矩阵与历年例题"
              >
                <Layers className="w-3.5 h-3.5" />
                <span>通用方法：{TOPIC_TO_META_METHOD[node.id].name} ↗</span>
              </button>
            )}
          </div>

          {/* § 1. 一句话记忆 (Summary banner) */}
          <div className="p-3.5 sm:p-4 rounded-[10px] bg-[var(--well)] border-l-2 border-[var(--blue)]">
            <div className="text-xs font-mono font-bold text-[var(--blue)] mb-1">
              § 1. 一句话记忆 (Core Takeaway)
            </div>
            <div className="text-xs sm:text-sm text-[var(--ink)] font-medium leading-relaxed font-body">
              <MathView content={node.summary} inline />
            </div>
          </div>

          {/* Quick Anchor Jump Bar */}
          <div className="pt-2 border-t border-[var(--line)] flex items-center gap-1.5 overflow-x-auto no-scrollbar font-mono text-[11px] text-[var(--muted)]">
            <span className="flex-shrink-0 text-[10px]">跳转:</span>
            <button onClick={() => scrollToSection('sec-breakthrough')} className="px-2 py-1 rounded bg-[var(--well)] hover:bg-[var(--line)] text-[var(--ink)] flex-shrink-0 cursor-pointer">
              突破口与反应
            </button>
            <button onClick={() => scrollToSection('sec-methods')} className="px-2 py-1 rounded bg-[var(--well)] hover:bg-[var(--line)] text-[var(--ink)] flex-shrink-0 cursor-pointer">
              候选方法
            </button>
            <button onClick={() => scrollToSection('sec-steps')} className="px-2 py-1 rounded bg-[var(--well)] hover:bg-[var(--line)] text-[var(--ink)] flex-shrink-0 cursor-pointer">
              标准步骤
            </button>
            <button onClick={() => scrollToSection('sec-formulas')} className="px-2 py-1 rounded bg-[var(--well)] hover:bg-[var(--line)] text-[var(--ink)] flex-shrink-0 cursor-pointer">
              核心公式
            </button>
            <button onClick={() => scrollToSection('sec-variants')} className="px-2 py-1 rounded bg-[var(--blue-bg)] text-[var(--blue)] font-bold flex-shrink-0 cursor-pointer">
              自测挑战(先练)
            </button>
            <button onClick={() => scrollToSection('sec-past')} className="px-2 py-1 rounded bg-[var(--well)] hover:bg-[var(--line)] text-[var(--ink)] flex-shrink-0 cursor-pointer">
              历年真题
            </button>
            <button onClick={() => scrollToSection('sec-pitfalls')} className="px-2 py-1 rounded bg-[var(--well)] hover:bg-[var(--line)] text-[var(--ink)] flex-shrink-0 cursor-pointer">
              易错自查
            </button>
          </div>
        </div>

        {/* 做题首屏：触发信号 vs 第一反应 */}
        <div id="sec-breakthrough" className="grid grid-cols-1 md:grid-cols-2 gap-3 sm:gap-4 scroll-mt-16">
          {/* 触发信号 */}
          <div className="bg-[var(--sheet)] border border-[var(--line)] rounded-[14px] p-4 sm:p-5 space-y-2 shadow-xs">
            <div className="text-xs font-mono font-bold text-[var(--amber)]">
              § 2. 触发信号 (看到什么)
            </div>
            <p className="text-xs text-[var(--muted)]">
              题目中出现以下形式、关键词或结构时，立即想到该考点：
            </p>
            <ul className="space-y-2 text-xs text-[var(--ink)] pt-1">
              {node.triggers.map((trig, idx) => (
                <li key={idx} className="flex items-start gap-2 bg-[var(--well)] p-2.5 rounded-[8px] border border-[var(--line)]">
                  <span className="font-mono text-[var(--amber)] font-bold">0{idx + 1}.</span>
                  <span className="leading-relaxed"><MathView content={trig} inline /></span>
                </li>
              ))}
            </ul>
          </div>

          {/* 第一反应 */}
          <div className="bg-[var(--sheet)] border border-[var(--line)] rounded-[14px] p-4 sm:p-5 space-y-2 shadow-xs">
            <div className="text-xs font-mono font-bold text-[var(--blue)]">
              § 3. 第一反应 (应该想到什么)
            </div>
            <p className="text-xs text-[var(--muted)]">
              读完题后大脑首要执行的自检动作与初步化简突破口：
            </p>
            <div className="bg-[var(--well)] border border-[var(--line)] p-3 sm:p-3.5 rounded-[8px] text-xs leading-relaxed text-[var(--ink)] font-body">
              <MathView content={node.firstReaction} inline />
            </div>
          </div>
        </div>

        {/* 候选解题方法与优先级判断 */}
        <div id="sec-methods" className="bg-[var(--sheet)] border border-[var(--line)] rounded-[14px] p-4 sm:p-6 space-y-3 sm:space-y-4 shadow-xs scroll-mt-16">
          <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-1 pb-2 border-b border-[var(--line)]">
            <h2 className="text-sm font-display font-bold text-[var(--ink)]">
              § 4. 候选方法与优先级判断 (Candidate Methods)
            </h2>
            <span className="text-xs font-mono text-[var(--muted)]">优先选用算力最小、不易出错的方法</span>
          </div>

          <div className="space-y-3">
            {node.candidateMethods.map((m, idx) => (
              <div
                key={idx}
                className="bg-[var(--well)] border border-[var(--line)] p-3.5 sm:p-4 rounded-[10px] space-y-2"
              >
                <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-1.5 pb-2 border-b border-[var(--line)]">
                  <div className="flex items-center gap-2">
                    <span className="font-mono text-xs px-2 py-0.5 rounded-[999px] bg-[var(--sheet)] text-[var(--ink)] border border-[var(--line)] font-bold">
                      优先级 {m.priority}
                    </span>
                    <h3 className="text-xs font-bold text-[var(--ink)] font-display">{m.name}</h3>
                  </div>
                  <span className="text-xs font-mono text-[var(--blue)]">
                    理由: <MathView content={m.whyChoose} inline />
                  </span>
                </div>

                <div className="grid grid-cols-1 md:grid-cols-2 gap-3 text-xs">
                  <div>
                    <span className="text-[var(--muted)] font-mono">适用特征：</span>
                    <div className="text-[var(--ink)] mt-0.5 leading-relaxed font-body">
                      <MathView content={m.condition || m.applicability || ""} inline />
                    </div>
                  </div>
                  <div>
                    <span className="text-[var(--muted)] font-mono">核心操作：</span>
                    <div className="text-[var(--ink)] mt-0.5 leading-relaxed font-body">
                      <MathView content={m.description || m.limitations || ""} inline />
                    </div>
                  </div>
                </div>
              </div>
            ))}
          </div>
        </div>

        {/* 适用条件与具体解题步骤 */}
        <div id="sec-steps" className="grid grid-cols-1 md:grid-cols-3 gap-3 sm:gap-4 scroll-mt-16">
          {/* 适用条件 */}
          <div className="md:col-span-1 bg-[var(--sheet)] border border-[var(--line)] rounded-[14px] p-4 sm:p-5 space-y-2 shadow-xs">
            <div className="text-xs font-mono font-bold text-[var(--red)]">
              § 5. 适用条件与前置限制
            </div>
            <div className="text-xs text-[var(--ink)] leading-relaxed bg-[var(--well)] p-3 sm:p-3.5 rounded-[8px] border border-[var(--line)] font-body">
              <MathView content={node.applicability || "适用于考研数学相关考点题型"} inline />
            </div>
          </div>

          {/* 解题步骤 */}
          <div className="md:col-span-2 bg-[var(--sheet)] border border-[var(--line)] rounded-[14px] p-4 sm:p-5 space-y-3 shadow-xs">
            <h2 className="text-xs font-mono font-bold text-[var(--ink)]">
              § 6. 标准化操作推导步骤 (Derivation Steps)
            </h2>
            <div className="space-y-2">
              {node.steps.map((step, idx) => (
                <div key={idx} className="flex items-start gap-2.5 bg-[var(--well)] p-2.5 rounded-[8px] border border-[var(--line)] text-xs">
                  <span className="font-mono text-[var(--blue)] font-bold">0{idx + 1}.</span>
                  <div className="text-[var(--ink)] leading-relaxed font-body">
                    <MathView content={step} inline />
                  </div>
                </div>
              ))}
            </div>
          </div>
        </div>

        {/* 核心公式与速记结论 */}
        {node.formulas && node.formulas.length > 0 && (
          <div id="sec-formulas" className="bg-[var(--sheet)] border border-[var(--line)] rounded-[14px] p-4 sm:p-6 space-y-3 sm:space-y-4 shadow-xs scroll-mt-16">
            <h2 className="text-sm font-display font-bold text-[var(--ink)] pb-2 border-b border-[var(--line)]">
              § 7. 核心公式与速记结论 (Core Formulas)
            </h2>
            <div className="grid grid-cols-1 sm:grid-cols-2 gap-3 sm:gap-4">
              {node.formulas.map((f, idx) => (
                <div key={idx} className="bg-[var(--well)] p-3.5 sm:p-4 rounded-[10px] border border-[var(--line)] space-y-2">
                  <div className="flex items-center justify-between text-xs font-mono">
                    <span className="font-bold text-[var(--ink)]">{f.title}</span>
                    {f.notes && (
                      <span className="text-[10px] text-[var(--purple)] bg-[var(--sheet)] px-1.5 py-0.5 rounded border border-[var(--line)]">
                        {f.notes}
                      </span>
                    )}
                  </div>
                  <div className="py-1 text-[var(--ink)] overflow-x-auto text-sm">
                    <MathView content={`$$${f.latex}$$`} />
                  </div>
                </div>
              ))}
            </div>
          </div>
        )}

        {/* § 8. 自测挑战与变式思维 (MOVED BEFORE PAST QUESTIONS!) */}
        <div id="sec-variants" className="bg-[var(--sheet)] border border-[var(--blue)]/50 rounded-[14px] p-4 sm:p-6 space-y-4 shadow-xs scroll-mt-16">
          <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-1 pb-2 border-b border-[var(--line)]">
            <div>
              <h2 className="text-base font-display font-bold text-[var(--ink)] flex items-center gap-2">
                <span>§ 8. 自测与变式训练 (Self-Test Variants)</span>
                <span className="text-[10px] font-mono px-2 py-0.5 rounded bg-[var(--blue-bg)] text-[var(--blue)] border border-[var(--blue)]">
                  先做题，后看真题解析
                </span>
              </h2>
              <p className="text-xs font-mono text-[var(--muted)] mt-0.5">
                先自行思考突破口与推导方案，展开核对提示与解析，检验独立做题能力
              </p>
            </div>
          </div>

          {node.variants.length === 0 ? (
            <div className="text-center py-8 text-xs font-mono text-[var(--muted)] bg-[var(--well)] rounded-[10px] border border-[var(--line)]">
              变式训练题目整理中，建议结合下方真题自测。
            </div>
          ) : (
            <div className="space-y-4">
              {node.variants.map((v) => {
                const isRevealed = !!revealedVariants[v.id];

                return (
                  <div
                    key={v.id}
                    className="bg-[var(--well)] rounded-[12px] border border-[var(--line)] p-4 sm:p-5 space-y-3"
                  >
                    <div className="text-sm text-[var(--ink)] font-serif leading-relaxed bg-[var(--sheet)] p-3.5 sm:p-4 rounded-[10px] border border-[var(--line)]">
                      <div className="text-xs font-bold font-mono text-[var(--muted)] mb-2">
                        [ 自测问题 ]
                      </div>
                      <MathView content={v.question} />
                    </div>

                    <div className="text-xs text-[var(--muted)] bg-[var(--sheet)] p-2.5 rounded-[8px] border border-[var(--line)] flex items-center gap-2 font-mono">
                      <span className="text-[var(--blue)] font-bold">提示:</span>
                      <MathView content={v.hint} inline />
                    </div>

                    <div className="flex justify-end pt-1">
                      <button
                        onClick={() => toggleVariantReveal(v.id)}
                        className={`flex items-center gap-1.5 px-3.5 py-1.5 rounded-[6px] text-xs font-mono font-medium transition-colors ${
                          isRevealed
                            ? 'bg-[var(--sheet)] text-[var(--muted)] border border-[var(--line)]'
                            : 'bg-[var(--ink)] text-[var(--paper)] font-bold hover:opacity-90'
                        }`}
                      >
                        {isRevealed ? (
                          <>
                            <EyeOff className="w-3.5 h-3.5" />
                            收起变式解析
                          </>
                        ) : (
                          <>
                            <Eye className="w-3.5 h-3.5" />
                            查看变式解题思路与解析
                          </>
                        )}
                      </button>
                    </div>

                    {isRevealed && (
                      <div className="mt-3 pt-3 border-t border-[var(--line)] space-y-3">
                        <div className="text-xs text-[var(--ink)] bg-[var(--sheet)] p-3 rounded-[8px] border border-[var(--line)]">
                          <span className="font-bold font-mono text-[var(--blue)]">方法选择思路：</span>
                          <span className="ml-1 font-body"><MathView content={v.methodChoiceAnalysis} inline /></span>
                        </div>

                        <div className="space-y-1.5">
                          <span className="text-xs font-mono font-bold text-[var(--ink)]">完整推导：</span>
                          {v.fullSolution.map((st, i) => (
                            <div
                              key={i}
                              className="text-xs text-[var(--ink)] bg-[var(--sheet)] p-3 rounded-[8px] border border-[var(--line)] font-body"
                            >
                              <MathView content={st} inline />
                            </div>
                          ))}
                        </div>

                        {v.keyTakeaway && (
                          <div className="text-xs font-mono text-[var(--green)] bg-[var(--green-bg)] p-2.5 rounded-[8px] border border-[var(--green)]">
                            结论提炼：<MathView content={v.keyTakeaway} inline />
                          </div>
                        )}
                      </div>
                    )}
                  </div>
                );
              })}
            </div>
          )}
        </div>

        {/* § 9. 历年真题实战检验 (AUTHENTIC PAST QUESTIONS - WITH COLLAPSIBLE SOLUTIONS & MISTAKE TAGS) */}
        <div id="sec-past" className="bg-[var(--sheet)] border border-[var(--line)] rounded-[14px] p-4 sm:p-6 space-y-4 sm:space-y-6 shadow-xs scroll-mt-16">
          <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-2 pb-3 border-b border-[var(--line)]">
            <div>
              <h2 className="text-base font-display font-bold text-[var(--ink)]">
                § 9. 历年真题实战检验 (Authentic Past Questions)
              </h2>
              <p className="text-xs font-mono text-[var(--muted)] mt-0.5">
                取材自《Maki 考研数学真题分类精解》，真实年份题号。建议先自己演算再展开解答。
              </p>
            </div>
            <span className="text-xs font-mono px-2 py-0.5 rounded-[999px] bg-[var(--well)] text-[var(--muted)] border border-[var(--line)] self-start sm:self-auto">
              收录 {node.pastQuestions.length} 道真题
            </span>
          </div>

          {/* Quick Paper & Year filter pills */}
          <div className="flex flex-wrap items-center justify-between gap-2 p-2 rounded-[8px] bg-[var(--well)] text-[11px] font-mono">
            <div className="flex items-center gap-1">
              <span className="text-[var(--muted)] mr-1">卷别:</span>
              {(['all', '数一', '数二', '数三'] as const).map((p) => (
                <button
                  key={p}
                  onClick={() => setPastPaperFilter(p)}
                  className={`px-2 py-0.5 rounded-[5px] transition-colors cursor-pointer ${
                    pastPaperFilter === p
                      ? 'bg-[var(--ink)] text-[var(--paper)] font-bold'
                      : 'bg-[var(--sheet)] text-[var(--muted)] hover:text-[var(--ink)]'
                  }`}
                >
                  {p === 'all' ? '全部' : p}
                </button>
              ))}
            </div>

            <div className="flex items-center gap-1">
              <span className="text-[var(--muted)] mr-1">年份:</span>
              {[
                { id: 'all', label: '全部年份' },
                { id: 'recent', label: '2021~2026 (重点)' },
                { id: 'classic', label: '往年真题' }
              ].map((yf) => (
                <button
                  key={yf.id}
                  onClick={() => setPastYearFilter(yf.id as any)}
                  className={`px-2 py-0.5 rounded-[5px] transition-colors cursor-pointer ${
                    pastYearFilter === yf.id
                      ? 'bg-[var(--blue-bg)] text-[var(--blue)] font-bold border border-[var(--blue)]'
                      : 'bg-[var(--sheet)] text-[var(--muted)] hover:text-[var(--ink)]'
                  }`}
                >
                  {yf.label}
                </button>
              ))}
            </div>
          </div>

          {filteredPastQuestions.length === 0 ? (
            <div className="text-center py-8 text-xs font-mono text-[var(--muted)] bg-[var(--well)] rounded-[10px] border border-[var(--line)]">
              当前筛选条件下暂无真题，请切换卷别或年份筛选。
            </div>
          ) : (
            <div className="space-y-5">
              {filteredPastQuestions.map((q: PastQuestion) => {
                const isSolutionOpen = !!revealedPastSolutions[q.id];

                return (
                  <div
                    key={q.id}
                    className="bg-[var(--well)] rounded-[12px] border border-[var(--line)] p-4 sm:p-5 space-y-3.5"
                  >
                    {/* Question header badge */}
                    <div className="flex flex-wrap items-center justify-between gap-2 font-mono text-xs">
                      <div className="flex items-center gap-2">
                        <span className="px-2 py-0.5 rounded-[6px] bg-[var(--sheet)] text-[var(--ink)] font-bold border border-[var(--line)]">
                          {q.year} · {q.category} · {q.questionNumber}
                        </span>
                        <span className="text-[var(--amber)] font-bold">
                          难度: {q.difficulty}
                        </span>
                      </div>
                      <span className="text-[11px] text-[var(--muted)]">
                        出处: {q.source}
                      </span>
                    </div>

                    {/* Problem statement */}
                    <div className="text-sm text-[var(--ink)] font-serif leading-relaxed bg-[var(--sheet)] p-3.5 sm:p-4 rounded-[10px] border border-[var(--line)]">
                      <MathView content={q.content} />
                      {q.options && q.options.length > 0 && (
                        <div className="grid grid-cols-1 sm:grid-cols-2 gap-2.5 mt-3.5 pt-3.5 border-t border-[var(--line)] font-mono text-xs">
                          {q.options.map((opt: string, i: number) => {
                            const optLabel = String.fromCharCode(65 + i);
                            const cleanOpt = opt.replace(new RegExp(`^\\s*\\(?${optLabel}\\)?[\\.、\\s]*`, 'i'), '').trim();
                            return (
                              <div
                                key={i}
                                className="flex items-start gap-2.5 p-2.5 rounded-[8px] bg-[var(--well)] hover:bg-[var(--sheet)] border border-[var(--line)] transition-colors group/opt"
                              >
                                <span className="w-5 h-5 rounded-[5px] bg-[var(--sheet)] text-[var(--blue)] group-hover/opt:bg-[var(--blue)] group-hover/opt:text-white font-bold text-[11px] flex items-center justify-center flex-shrink-0 border border-[var(--line)] shadow-2xs transition-colors">
                                  {optLabel}
                                </span>
                                <div className="flex-1 font-serif text-[var(--ink)] leading-relaxed pt-0.5">
                                  <MathView content={cleanOpt} inline />
                                </div>
                              </div>
                            );
                          })}
                        </div>
                      )}
                    </div>

                    {/* Toggle Solution Button (Protects against spoilers!) */}
                    <div className="flex items-center justify-between pt-1">
                      <span className="text-xs font-mono text-[var(--muted)]">
                        {isSolutionOpen ? '分步解答已展开' : '做完后核对答案：'}
                      </span>
                      <button
                        onClick={() => togglePastSolutionReveal(q.id)}
                        className={`flex items-center gap-1.5 px-3 py-1.5 rounded-[6px] text-xs font-mono font-medium transition-colors ${
                          isSolutionOpen
                            ? 'bg-[var(--sheet)] text-[var(--muted)] border border-[var(--line)]'
                            : 'bg-[var(--ink)] text-[var(--paper)] font-bold hover:opacity-90'
                        }`}
                      >
                        {isSolutionOpen ? (
                          <>
                            <EyeOff className="w-3.5 h-3.5" />
                            收起真题解析
                          </>
                        ) : (
                          <>
                            <Eye className="w-3.5 h-3.5" />
                            展开完整解析与答案
                          </>
                        )}
                      </button>
                    </div>

                    {/* Collapsible Solution Content */}
                    {isSolutionOpen && (
                      <div className="space-y-3 pt-2 border-t border-[var(--line)] animate-fadeIn">
                        {/* Analysis */}
                        <div className="text-xs text-[var(--ink)] bg-[var(--sheet)] border border-[var(--line)] p-3 rounded-[8px]">
                          <span className="font-bold text-[var(--blue)] font-mono">考点分析：</span>
                          <span className="ml-1 leading-relaxed font-body"><MathView content={q.analysis} inline /></span>
                        </div>

                        {/* Solution Steps */}
                        <div className="space-y-2.5 pt-1">
                          <span className="text-xs font-mono font-bold text-[var(--ink)]">分步解答过程：</span>
                          {q.solutionSteps.map((s: string, stepIdx: number) => (
                            <div
                              key={stepIdx}
                              className="text-xs text-[var(--ink)] bg-[var(--sheet)] p-3 rounded-[8px] border border-[var(--line)] leading-relaxed font-body flex items-start gap-2.5"
                            >
                              <span className="px-1.5 py-0.5 rounded bg-[var(--well)] text-[var(--muted)] font-mono font-bold text-[10px] border border-[var(--line)] flex-shrink-0 mt-0.5">
                                步 {stepIdx + 1}
                              </span>
                              <div className="flex-1">
                                <MathView content={s} />
                              </div>
                            </div>
                          ))}
                        </div>

                        {/* Final Answer & Pitfall */}
                        <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-2.5 pt-2 border-t border-[var(--line)] text-xs font-mono">
                          {q.answer && (
                            <div className="flex items-center gap-2">
                              <span className="text-[var(--muted)] font-mono">答案：</span>
                              <span className="font-bold text-[var(--green)] bg-[var(--sheet)] px-2 py-0.5 rounded border border-[var(--line)]">
                                <MathView content={q.answer} inline />
                              </span>
                            </div>
                          )}
                          {q.pitfall && (
                            <div className="text-[var(--muted)] text-xs flex items-center gap-1 font-mono">
                              <span className="text-[var(--red)] font-bold">易错：</span>
                              <MathView content={q.pitfall} inline />
                            </div>
                          )}
                        </div>
                      </div>
                    )}

                    {/* Mistake Tagging Bar */}
                    <div className="pt-2 border-t border-[var(--line)] flex flex-wrap items-center gap-1.5 text-[11px] font-mono">
                      <span className="text-[var(--muted)] flex items-center gap-1">
                        <Tag className="w-3 h-3 text-[var(--muted)]" />
                        若做错，记录错因:
                      </span>
                      {AVAILABLE_MISTAKE_TAGS.map((tag) => {
                        const isSelected = (record.mistakeTags || []).includes(tag);
                        return (
                          <button
                            key={tag}
                            onClick={() => handleToggleMistakeTag(tag)}
                            className={`px-2 py-0.5 rounded-[4px] border transition-colors ${
                              isSelected
                                ? 'bg-[var(--amber-bg)] text-[var(--amber)] border-[var(--amber)] font-bold'
                                : 'bg-[var(--sheet)] text-[var(--muted)] border-[var(--line)] hover:text-[var(--ink)]'
                            }`}
                          >
                            {tag}
                          </button>
                        );
                      })}
                    </div>
                  </div>
                );
              })}
            </div>
          )}
        </div>

        {/* § 10. 高频失分点与自查清单 */}
        {node.pitfalls && node.pitfalls.length > 0 && (
          <div id="sec-pitfalls" className="bg-[var(--sheet)] border border-[var(--red)]/40 rounded-[14px] p-4 sm:p-6 space-y-3 shadow-xs scroll-mt-16">
            <h2 className="text-xs font-mono font-bold text-[var(--red)]">
              § 10. 高频失分点与自查清单 (Pitfalls & Common Errors)
            </h2>
            <div className="grid grid-cols-1 sm:grid-cols-2 gap-3">
              {node.pitfalls.map((pitfall, idx) => (
                <div key={idx} className="bg-[var(--well)] p-3 rounded-[8px] border border-[var(--line)] flex items-start gap-2 text-xs text-[var(--ink)] leading-relaxed font-body">
                  <span className="text-[var(--red)] font-mono font-bold">[!]</span>
                  <div className="flex-1 leading-relaxed"><MathView content={pitfall} inline /></div>
                </div>
              ))}
            </div>
          </div>
        )}

        {/* § 11. 关联考点 */}
        {node.relatedKnowledgeIds && node.relatedKnowledgeIds.length > 0 && (
          <div className="bg-[var(--sheet)] border border-[var(--line)] rounded-[14px] p-4 sm:p-6 space-y-3 shadow-xs">
            <h2 className="text-xs font-mono font-bold text-[var(--ink)]">
              § 11. 关联考点 (Related Topics)
            </h2>
            <div className="flex flex-wrap gap-2 pt-1 font-mono text-xs">
              {node.relatedKnowledgeIds.map((relId) => {
                const relNode = KNOWLEDGE_BASE[relId];
                if (!relNode) return null;

                return (
                  <button
                    key={relId}
                    onClick={() => onNavigateTopic(relId)}
                    className="flex items-center gap-1.5 px-3 py-1.5 rounded-[6px] bg-[var(--well)] hover:bg-[var(--sheet)] border border-[var(--line)] hover:border-[var(--blue)] text-[var(--ink)] transition-colors"
                  >
                    <span>{relNode.title}</span>
                    <ArrowRight className="w-3 h-3 text-[var(--muted)]" />
                  </button>
                );
              })}
            </div>
          </div>
        )}

        {/* Bottom Navigation Buttons */}
        <div className="flex flex-col sm:flex-row items-stretch sm:items-center justify-between gap-3 sm:gap-4 pt-5 sm:pt-6 border-t border-[var(--line)] font-mono text-xs">
          <div>
            {prevTopicId ? (
              <button
                onClick={() => onNavigateTopic(prevTopicId)}
                className="w-full sm:w-auto flex items-center justify-center gap-2 px-3.5 py-2.5 sm:py-2 rounded-[8px] bg-[var(--sheet)] hover:bg-[var(--well)] border border-[var(--line)] text-[var(--ink)] transition-colors"
              >
                <ChevronLeft className="w-4 h-4" />
                <span>上一考点：{KNOWLEDGE_BASE[prevTopicId]?.title}</span>
              </button>
            ) : (
              <div />
            )}
          </div>

          <button
            onClick={() => onBackToChapter(chapter.id)}
            className="w-full sm:w-auto text-center px-4 py-2.5 sm:py-2 rounded-[8px] bg-[var(--sheet)] hover:bg-[var(--well)] text-[var(--muted)] hover:text-[var(--ink)] border border-[var(--line)] transition-colors"
          >
            返回章节目录
          </button>

          <div>
            {nextTopicId ? (
              <button
                onClick={() => onNavigateTopic(nextTopicId)}
                className="w-full sm:w-auto flex items-center justify-center gap-2 px-3.5 py-2.5 sm:py-2 rounded-[8px] bg-[var(--ink)] text-[var(--paper)] font-bold transition-all hover:opacity-90"
              >
                <span>下一考点：{KNOWLEDGE_BASE[nextTopicId]?.title}</span>
                <ArrowRight className="w-4 h-4" />
              </button>
            ) : (
              <div />
            )}
          </div>
        </div>

      </div>
    </div>
  );
};
