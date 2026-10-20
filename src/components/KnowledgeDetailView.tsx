import React, { useState, useEffect } from 'react';
import { 
  ArrowLeft, ArrowRight, ChevronLeft, Compass, Eye, EyeOff
} from 'lucide-react';
import { KNOWLEDGE_BASE } from '../data/knowledgeBase';
import { CHAPTERS, SUBJECTS } from '../data/subjects';
import { LearningStatus } from '../data/types';
import { getLearningStatus, setLearningStatus } from '../data/storage';
import { MathView } from './MathView';

interface KnowledgeDetailViewProps {
  nodeId: string;
  onBackToChapter: (chapterId: string) => void;
  onBackToMindmap: () => void;
  onNavigateTopic: (nodeId: string) => void;
}

export const KnowledgeDetailView: React.FC<KnowledgeDetailViewProps> = ({
  nodeId,
  onBackToChapter,
  onBackToMindmap,
  onNavigateTopic,
}) => {
  const node = KNOWLEDGE_BASE[nodeId] || KNOWLEDGE_BASE['gaoshu-01-indeterminate-0-0'];
  const chapter = CHAPTERS[node.chapterId] || CHAPTERS['gaoshu-ch01'];
  const subject = SUBJECTS[node.subject] || SUBJECTS['gaoshu'];

  const [status, setStatus] = useState<LearningStatus>(getLearningStatus(node.id));
  const [revealedVariants, setRevealedVariants] = useState<Record<string, boolean>>({});

  useEffect(() => {
    setStatus(getLearningStatus(node.id));
    window.scrollTo({ top: 0, behavior: 'smooth' });
  }, [node.id]);

  const handleStatusChange = (newStatus: LearningStatus) => {
    setStatus(newStatus);
    setLearningStatus(node.id, newStatus);
  };

  const toggleVariantReveal = (varId: string) => {
    setRevealedVariants((prev) => ({ ...prev, [varId]: !prev[varId] }));
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
      {/* Top Breadcrumb & Control Bar */}
      <div className="sticky top-0 z-20 bg-[var(--sheet)] border-b border-[var(--line)] px-4 lg:px-8 py-3 shadow-sm">
        <div className="max-w-4xl mx-auto flex flex-wrap items-center justify-between gap-3 font-mono text-xs">
          {/* Breadcrumbs */}
          <div className="flex items-center space-x-2 text-[var(--muted)] overflow-x-auto py-0.5">
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
            <span className="text-[var(--ink)] font-bold truncate max-w-[160px] sm:max-w-none">
              {node.title}
            </span>
          </div>

          {/* Quick Learning Status Switcher */}
          <div className="flex items-center gap-1.5 bg-[var(--well)] p-1 rounded-[8px] border border-[var(--line)]">
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
              推导困难
            </button>
            <button
              onClick={() => handleStatusChange('mastered')}
              className={`px-2.5 py-1 rounded-[6px] transition-colors ${
                status === 'mastered'
                  ? 'bg-[var(--green-bg)] text-[var(--green)] font-bold border border-[var(--green)]'
                  : 'text-[var(--muted)] hover:text-[var(--green)]'
              }`}
            >
              能够独立完成
            </button>
          </div>
        </div>
      </div>

      {/* Main Content Article Body */}
      <div className="max-w-4xl mx-auto px-4 lg:px-8 mt-6 space-y-8">
        
        {/* Title Header Card */}
        <div className="bg-[var(--sheet)] border border-[var(--line)] rounded-[14px] p-6 lg:p-8 space-y-4 shadow-sm">
          <div className="flex flex-wrap items-center gap-2 text-xs font-mono text-[var(--muted)]">
            <span className="px-2 py-0.5 rounded-[999px] bg-[var(--well)] border border-[var(--line)] text-[var(--ink)]">
              {subject.name} · 第 {chapter.order} 讲
            </span>
            {node.isPending && (
              <span className="px-2 py-0.5 rounded-[999px] bg-[var(--well)] border border-[var(--line)] text-[var(--muted)]">
                讲义待补充（后续同步）
              </span>
            )}
            <span className="ml-auto">
              出处: {node.source}
            </span>
          </div>

          <h1 className="text-2xl sm:text-3xl font-display font-bold text-[var(--ink)] tracking-tight">
            {node.title}
          </h1>

          {/* 一句话记忆 (Summary banner) */}
          <div className="p-4 rounded-[10px] bg-[var(--well)] border-l-2 border-[var(--blue)]">
            <div className="text-xs font-mono font-bold text-[var(--blue)] mb-1">
              § 1. 一句话记忆 (Core Takeaway)
            </div>
            <p className="text-sm text-[var(--ink)] font-medium leading-relaxed font-body">
              {node.summary}
            </p>
          </div>
        </div>

        {/* 触发信号 vs 第一反应 */}
        <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
          {/* 触发信号 */}
          <div className="bg-[var(--sheet)] border border-[var(--line)] rounded-[14px] p-5 space-y-2 shadow-sm">
            <div className="text-xs font-mono font-bold text-[var(--amber)]">
              § 2. 触发信号 (看到什么)
            </div>
            <p className="text-xs text-[var(--muted)]">
              题目中出现以下形式、关键词或结构时，立即想到该方法：
            </p>
            <ul className="space-y-2 text-xs text-[var(--ink)] pt-1">
              {node.triggers.map((trig, idx) => (
                <li key={idx} className="flex items-start gap-2 bg-[var(--well)] p-2.5 rounded-[8px] border border-[var(--line)]">
                  <span className="font-mono text-[var(--amber)] font-bold">0{idx + 1}.</span>
                  <span className="leading-relaxed">{trig}</span>
                </li>
              ))}
            </ul>
          </div>

          {/* 第一反应 */}
          <div className="bg-[var(--sheet)] border border-[var(--line)] rounded-[14px] p-5 space-y-2 shadow-sm">
            <div className="text-xs font-mono font-bold text-[var(--blue)]">
              § 3. 第一反应 (应该想到什么)
            </div>
            <p className="text-xs text-[var(--muted)]">
              读完题后大脑首要执行的自检动作与初步化简思路：
            </p>
            <div className="bg-[var(--well)] border border-[var(--line)] p-3.5 rounded-[8px] text-xs leading-relaxed text-[var(--ink)] font-body">
              {node.firstReaction}
            </div>
          </div>
        </div>

        {/* 候选解题方法与优先级 */}
        <div className="bg-[var(--sheet)] border border-[var(--line)] rounded-[14px] p-6 space-y-4 shadow-sm">
          <div className="flex items-center justify-between pb-2 border-b border-[var(--line)]">
            <h2 className="text-sm font-display font-bold text-[var(--ink)]">
              § 4. 候选方法与优先级判断 (Candidate Methods)
            </h2>
            <span className="text-xs font-mono text-[var(--muted)]">优先选用算力最小、不易出错的方法</span>
          </div>

          <div className="space-y-3">
            {node.candidateMethods.map((m, idx) => (
              <div
                key={idx}
                className="bg-[var(--well)] border border-[var(--line)] p-4 rounded-[10px] space-y-2.5"
              >
                <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-2 pb-2 border-b border-[var(--line)]">
                  <div className="flex items-center gap-2">
                    <span className="font-mono text-xs px-2 py-0.5 rounded-[999px] bg-[var(--sheet)] text-[var(--ink)] border border-[var(--line)] font-bold">
                      优先级 {m.priority}
                    </span>
                    <h3 className="text-xs font-bold text-[var(--ink)] font-display">{m.name}</h3>
                  </div>
                  <span className="text-xs font-mono text-[var(--blue)]">
                    理由: {m.whyChoose}
                  </span>
                </div>

                <div className="grid grid-cols-1 md:grid-cols-2 gap-3 text-xs">
                  <div>
                    <span className="text-[var(--muted)] font-mono">适用特征：</span>
                    <p className="text-[var(--ink)] mt-0.5 leading-relaxed font-body">{m.condition}</p>
                  </div>
                  <div>
                    <span className="text-[var(--muted)] font-mono">核心操作：</span>
                    <p className="text-[var(--ink)] mt-0.5 leading-relaxed font-body">{m.description}</p>
                  </div>
                </div>
              </div>
            ))}
          </div>
        </div>

        {/* 适用条件与具体解题步骤 */}
        <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
          {/* 适用条件 */}
          <div className="md:col-span-1 bg-[var(--sheet)] border border-[var(--line)] rounded-[14px] p-5 space-y-2 shadow-sm">
            <div className="text-xs font-mono font-bold text-[var(--red)]">
              § 5. 适用条件与前置限制
            </div>
            <p className="text-xs text-[var(--ink)] leading-relaxed bg-[var(--well)] p-3.5 rounded-[8px] border border-[var(--line)] font-body">
              {node.applicability}
            </p>
          </div>

          {/* 解题步骤 */}
          <div className="md:col-span-2 bg-[var(--sheet)] border border-[var(--line)] rounded-[14px] p-5 space-y-3 shadow-sm">
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
          <div className="bg-[var(--sheet)] border border-[var(--line)] rounded-[14px] p-6 space-y-4 shadow-sm">
            <h2 className="text-sm font-display font-bold text-[var(--ink)] pb-2 border-b border-[var(--line)]">
              § 7. 核心公式与速记结论 (Core Formulas)
            </h2>
            <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
              {node.formulas.map((f, idx) => (
                <div key={idx} className="bg-[var(--well)] p-4 rounded-[10px] border border-[var(--line)] space-y-2">
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

        {/* 易错点分析 */}
        {node.pitfalls && node.pitfalls.length > 0 && (
          <div className="bg-[var(--sheet)] border border-[var(--red)]/40 rounded-[14px] p-6 space-y-3 shadow-sm">
            <h2 className="text-xs font-mono font-bold text-[var(--red)]">
              § 8. 高频失分点与自查清单 (Pitfalls & Common Errors)
            </h2>
            <div className="grid grid-cols-1 sm:grid-cols-2 gap-3">
              {node.pitfalls.map((pitfall, idx) => (
                <div key={idx} className="bg-[var(--well)] p-3 rounded-[8px] border border-[var(--line)] flex items-start gap-2 text-xs text-[var(--ink)] leading-relaxed font-body">
                  <span className="text-[var(--red)] font-mono font-bold">[!]</span>
                  <span>{pitfall}</span>
                </div>
              ))}
            </div>
          </div>
        )}

        {/* 历年真题实战检验 (Maki PDF 真题分类精解样式) */}
        <div className="bg-[var(--sheet)] border border-[var(--line)] rounded-[14px] p-6 space-y-6 shadow-sm">
          <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-2 pb-3 border-b border-[var(--line)]">
            <div>
              <h2 className="text-base font-display font-bold text-[var(--ink)]">
                § 9. 历年真题实战检验 (Authentic Past Questions)
              </h2>
              <p className="text-xs font-mono text-[var(--muted)] mt-0.5">
                严格取材自《Maki 考研数学真题分类精解》，真实年份、题号与分步推导
              </p>
            </div>
            <span className="text-xs font-mono px-2 py-0.5 rounded-[999px] bg-[var(--well)] text-[var(--muted)] border border-[var(--line)]">
              收录 {node.pastQuestions.length} 道真题
            </span>
          </div>

          {node.pastQuestions.length === 0 ? (
            <div className="text-center py-8 text-xs font-mono text-[var(--muted)] bg-[var(--well)] rounded-[10px] border border-[var(--line)]">
              真题分类解析整理中，后续持续更新同步。
            </div>
          ) : (
            <div className="space-y-6">
              {node.pastQuestions.map((q) => (
                <div
                  key={q.id}
                  className="bg-[var(--well)] rounded-[12px] border border-[var(--line)] p-5 space-y-4"
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
                  <div className="text-sm text-[var(--ink)] font-serif leading-relaxed bg-[var(--sheet)] p-4 rounded-[10px] border border-[var(--line)]">
                    <MathView content={q.content} />
                    {q.options && (
                      <div className="grid grid-cols-1 sm:grid-cols-2 gap-2 mt-3 pt-3 border-t border-[var(--line)]">
                        {q.options.map((opt, i) => (
                          <div key={i} className="text-xs text-[var(--ink)]">
                            <MathView content={opt} inline />
                          </div>
                        ))}
                      </div>
                    )}
                  </div>

                  {/* Analysis */}
                  <div className="text-xs text-[var(--ink)] bg-[var(--sheet)] border border-[var(--line)] p-3 rounded-[8px]">
                    <span className="font-bold text-[var(--blue)] font-mono">考点分析：</span>
                    <span className="ml-1 leading-relaxed font-body"><MathView content={q.analysis} inline /></span>
                  </div>

                  {/* Solution Steps */}
                  <div className="space-y-2 pt-1">
                    <span className="text-xs font-mono font-bold text-[var(--ink)]">分步解答过程：</span>
                    {q.solutionSteps.map((s, stepIdx) => (
                      <div
                        key={stepIdx}
                        className="text-xs text-[var(--ink)] bg-[var(--sheet)] p-3 rounded-[8px] border border-[var(--line)] leading-relaxed font-body"
                      >
                        <MathView content={s} inline />
                      </div>
                    ))}
                  </div>

                  {/* Final Answer & Pitfall */}
                  <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-3 pt-3 border-t border-[var(--line)] text-xs font-mono">
                    {q.answer && (
                      <div className="flex items-center gap-2">
                        <span className="text-[var(--muted)] font-mono">答案：</span>
                        <span className="font-bold text-[var(--green)] bg-[var(--sheet)] px-2 py-0.5 rounded border border-[var(--line)]">
                          {q.answer}
                        </span>
                      </div>
                    )}
                    {q.pitfall && (
                      <div className="text-[var(--muted)] text-xs flex items-center gap-1 font-mono">
                        <span className="text-[var(--red)] font-bold">易错：</span>
                        <span>{q.pitfall}</span>
                      </div>
                    )}
                  </div>
                </div>
              ))}
            </div>
          )}
        </div>

        {/* 自测与变式训练 (Variants) */}
        <div className="bg-[var(--sheet)] border border-[var(--line)] rounded-[14px] p-6 space-y-4 shadow-sm">
          <div className="flex items-center justify-between pb-2 border-b border-[var(--line)]">
            <h2 className="text-base font-display font-bold text-[var(--ink)]">
              § 10. 自测与变式训练 (Self-Test Variants)
            </h2>
            <span className="text-xs font-mono text-[var(--muted)]">先自行思考判断方法，再展开校验</span>
          </div>

          {node.variants.length === 0 ? (
            <div className="text-center py-8 text-xs font-mono text-[var(--muted)] bg-[var(--well)] rounded-[10px] border border-[var(--line)]">
              变式训练题目整理中，建议结合上述真题自测。
            </div>
          ) : (
            <div className="space-y-4">
              {node.variants.map((v) => {
                const isRevealed = !!revealedVariants[v.id];

                return (
                  <div
                    key={v.id}
                    className="bg-[var(--well)] rounded-[12px] border border-[var(--line)] p-5 space-y-3"
                  >
                    <div className="text-sm text-[var(--ink)] font-serif leading-relaxed bg-[var(--sheet)] p-4 rounded-[10px] border border-[var(--line)]">
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
                        className={`flex items-center gap-1.5 px-3 py-1.5 rounded-[6px] text-xs font-mono font-medium transition-colors ${
                          isRevealed
                            ? 'bg-[var(--sheet)] text-[var(--muted)] border border-[var(--line)]'
                            : 'bg-[var(--ink)] text-[var(--paper)] font-bold hover:opacity-90'
                        }`}
                      >
                        {isRevealed ? (
                          <>
                            <EyeOff className="w-3.5 h-3.5" />
                            收起解析
                          </>
                        ) : (
                          <>
                            <Eye className="w-3.5 h-3.5" />
                            查看解题思路与解析
                          </>
                        )}
                      </button>
                    </div>

                    {isRevealed && (
                      <div className="mt-4 pt-4 border-t border-[var(--line)] space-y-3">
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
                            结论提炼：{v.keyTakeaway}
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

        {/* 关联考点 */}
        {node.relatedKnowledgeIds && node.relatedKnowledgeIds.length > 0 && (
          <div className="bg-[var(--sheet)] border border-[var(--line)] rounded-[14px] p-6 space-y-3 shadow-sm">
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
        <div className="flex flex-col sm:flex-row items-center justify-between gap-4 pt-6 border-t border-[var(--line)] font-mono text-xs">
          <div>
            {prevTopicId ? (
              <button
                onClick={() => onNavigateTopic(prevTopicId)}
                className="flex items-center gap-2 px-3.5 py-2 rounded-[8px] bg-[var(--sheet)] hover:bg-[var(--well)] border border-[var(--line)] text-[var(--ink)] transition-colors"
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
            className="px-4 py-2 rounded-[8px] bg-[var(--sheet)] hover:bg-[var(--well)] text-[var(--muted)] hover:text-[var(--ink)] border border-[var(--line)] transition-colors"
          >
            返回章节目录
          </button>

          <div>
            {nextTopicId ? (
              <button
                onClick={() => onNavigateTopic(nextTopicId)}
                className="flex items-center gap-2 px-3.5 py-2 rounded-[8px] bg-[var(--ink)] text-[var(--paper)] font-bold transition-all hover:opacity-90"
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
