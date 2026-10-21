import React, { useState, useMemo } from 'react';
import { 
  ArrowLeft, ArrowRight, ExternalLink, Search, Target, Compass, Filter, ChevronDown, ChevronUp, BookOpen
} from 'lucide-react';
import { CHAPTERS, SUBJECTS } from '../data/subjects';
import { KNOWLEDGE_BASE } from '../data/knowledgeBase';
import { LearningStatus, KnowledgeNode } from '../data/types';
import { getChapterProgress, setLearningStatus } from '../data/storage';
import { TOPIC_TO_LECTURE } from '../data/makiLectures';
import { MathView } from './MathView';

interface ChapterViewProps {
  chapterId: string;
  onBackToMindmap: () => void;
  onSelectTopic: (topicId: string) => void;
  initialTopicId?: string;
  onOpenMakiLecture?: (lectureId: string) => void;
}

export const ChapterView: React.FC<ChapterViewProps> = ({
  chapterId,
  onBackToMindmap,
  onSelectTopic,
  initialTopicId,
  onOpenMakiLecture,
}) => {
  const chapter = CHAPTERS[chapterId] || CHAPTERS['gaoshu-ch01'];
  const subject = SUBJECTS[chapter.subjectId];

  const topics = useMemo(() => {
    return chapter.topicIds.map((tid) => KNOWLEDGE_BASE[tid]).filter(Boolean);
  }, [chapter]);

  const [activeTopicId, setActiveTopicId] = useState<string>(
    initialTopicId || (topics[0]?.id || '')
  );

  const [searchQuery, setSearchQuery] = useState<string>('');
  const [statusFilter, setStatusFilter] = useState<'all' | LearningStatus>('all');
  const [refreshKey, setRefreshKey] = useState<number>(0);
  const [isMobileListOpen, setIsMobileListOpen] = useState<boolean>(false);

  const progress = useMemo(() => {
    return getChapterProgress(chapter.topicIds);
  }, [chapter, refreshKey]);

  const filteredTopics = useMemo(() => {
    return topics.filter((t) => {
      if (statusFilter !== 'all') {
        const s = localStorage.getItem('kaoyan_math1_learning_status');
        const map = s ? JSON.parse(s) : {};
        const nodeStatus = map[t.id] || 'unlearned';
        if (nodeStatus !== statusFilter) return false;
      }
      if (!searchQuery.trim()) return true;
      const q = searchQuery.toLowerCase();
      return (
        t.title.toLowerCase().includes(q) ||
        t.summary.toLowerCase().includes(q) ||
        t.triggers.some((tr) => tr.toLowerCase().includes(q))
      );
    });
  }, [topics, statusFilter, searchQuery, refreshKey]);

  const activeTopic: KnowledgeNode | undefined = useMemo(() => {
    return KNOWLEDGE_BASE[activeTopicId] || filteredTopics[0] || topics[0];
  }, [activeTopicId, filteredTopics, topics]);

  const handleUpdateStatus = (nodeId: string, newStatus: LearningStatus) => {
    setLearningStatus(nodeId, newStatus);
    setRefreshKey((k) => k + 1);
  };

  return (
    <div className="min-h-[calc(100vh-56px)] bg-[var(--paper)] text-[var(--ink)] flex flex-col font-body">
      {/* Top Banner / Breadcrumb & Chapter Header */}
      <div className="bg-[var(--sheet)] border-b border-[var(--line)] px-3 sm:px-6 lg:px-8 py-4 sm:py-5">
        <div className="max-w-7xl mx-auto">
          {/* Breadcrumbs */}
          <div className="flex items-center space-x-1.5 sm:space-x-2 text-xs font-mono text-[var(--muted)] mb-2.5 overflow-x-auto">
            <button
              onClick={onBackToMindmap}
              className="flex items-center gap-1 text-[var(--blue)] hover:underline transition-colors flex-shrink-0"
            >
              <Compass className="w-3.5 h-3.5" />
              总思维导图
            </button>
            <span>/</span>
            <span className="flex-shrink-0">{subject.name}</span>
            <span>/</span>
            <span className="text-[var(--ink)] font-semibold flex-shrink-0 truncate max-w-[180px] sm:max-w-none">
              {chapter.title}
            </span>
          </div>

          <div className="flex flex-col md:flex-row md:items-center justify-between gap-3 sm:gap-4">
            <div>
              <div className="flex items-center gap-2 sm:gap-3">
                <button
                  onClick={onBackToMindmap}
                  className="p-1.5 rounded-[7px] bg-[var(--well)] hover:bg-[var(--line)] text-[var(--ink)] border border-[var(--line)] transition-colors"
                  title="返回思维导图"
                >
                  <ArrowLeft className="w-4 h-4" />
                </button>
                <h1 className="text-lg sm:text-2xl font-display font-bold text-[var(--ink)] tracking-tight">
                  第 {chapter.order} 讲 · {chapter.title}
                </h1>
              </div>
              <p className="text-xs text-[var(--muted)] mt-1 font-body">
                {chapter.description}
              </p>
            </div>

            {/* Quick Stats Badge & Progress Bar */}
            <div className="flex items-center gap-3 sm:gap-4 bg-[var(--well)] p-2 sm:p-2.5 rounded-[10px] border border-[var(--line)] self-start md:self-auto">
              <div className="text-left font-mono">
                <div className="text-[10px] sm:text-[11px] text-[var(--muted)]">考点总计</div>
                <div className="text-xs sm:text-sm font-bold text-[var(--ink)]">
                  {progress.mastered} / {progress.total}
                </div>
              </div>

              <div className="h-6 sm:h-7 w-px bg-[var(--line)]" />

              <div className="w-24 sm:w-28 font-mono">
                <div className="flex justify-between text-[10px] sm:text-[11px] mb-1">
                  <span className="text-[var(--muted)]">掌握进度</span>
                  <span className="text-[var(--blue)] font-bold">{progress.percentage}%</span>
                </div>
                <div className="w-full bg-[var(--line)] rounded-full h-1.5 overflow-hidden">
                  <div
                    className="bg-[var(--blue)] h-1.5 rounded-full transition-all duration-300"
                    style={{ width: `${progress.percentage}%` }}
                  />
                </div>
              </div>
            </div>
          </div>

          {/* Chapter Goals */}
          {chapter.goals && chapter.goals.length > 0 && (
            <div className="mt-3 sm:mt-4 pt-3 sm:pt-4 border-t border-[var(--line)]">
              <div className="flex items-center gap-1.5 text-xs font-semibold text-[var(--ink)] mb-2 font-mono">
                <Target className="w-3.5 h-3.5 text-[var(--blue)]" />
                本讲复习目标与考查定位：
              </div>
              <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-2">
                {chapter.goals.map((goal, idx) => (
                  <div
                    key={idx}
                    className="flex items-start gap-2 text-xs text-[var(--ink)] bg-[var(--well)] border border-[var(--line)] p-2 sm:p-2.5 rounded-[8px]"
                  >
                    <span className="text-[var(--blue)] font-mono font-bold">0{idx + 1}.</span>
                    <span className="leading-relaxed">{goal}</span>
                  </div>
                ))}
              </div>
            </div>
          )}
        </div>
      </div>

      {/* Main Layout */}
      <div className="max-w-7xl mx-auto w-full flex-1 flex flex-col md:flex-row p-3 sm:p-6 lg:p-8 gap-4 sm:gap-6">
        
        {/* Mobile Topic Horizontal Switcher Bar (Appears on < md) */}
        <div className="md:hidden flex flex-col gap-2">
          <div className="flex items-center justify-between gap-2 bg-[var(--sheet)] border border-[var(--line)] p-2 rounded-[10px]">
            <div className="flex-1 overflow-x-auto flex items-center gap-1.5 py-0.5 no-scrollbar">
              {topics.map((t, idx) => {
                const isSelected = activeTopic?.id === t.id;
                return (
                  <button
                    key={t.id}
                    onClick={() => setActiveTopicId(t.id)}
                    className={`flex items-center gap-1 px-2.5 py-1 rounded-[6px] text-xs font-mono flex-shrink-0 transition-colors ${
                      isSelected
                        ? 'bg-[var(--ink)] text-[var(--paper)] font-bold shadow-xs'
                        : 'bg-[var(--well)] text-[var(--muted)] hover:text-[var(--ink)]'
                    }`}
                  >
                    <span>0{idx + 1}</span>
                    <span className="truncate max-w-[110px]">{t.title}</span>
                  </button>
                );
              })}
            </div>

            <button
              onClick={() => setIsMobileListOpen(!isMobileListOpen)}
              className="flex items-center gap-1 px-2 py-1 rounded-[6px] bg-[var(--well)] text-[var(--muted)] text-xs font-mono flex-shrink-0 border border-[var(--line)]"
            >
              <Filter className="w-3 h-3" />
              <span>{isMobileListOpen ? '收起' : '筛选'}</span>
            </button>
          </div>
        </div>

        {/* Sidebar: Topic List (Always on desktop, Collapsible on mobile) */}
        <div
          className={`${
            isMobileListOpen ? 'flex' : 'hidden md:flex'
          } w-full md:w-80 lg:w-96 flex-col flex-shrink-0 space-y-3`}
        >
          {/* Search & Filter */}
          <div className="bg-[var(--sheet)] border border-[var(--line)] p-3 rounded-[12px] space-y-2.5 shadow-sm">
            <div className="relative">
              <Search className="w-3.5 h-3.5 absolute left-3 top-2.5 text-[var(--muted)]" />
              <input
                type="text"
                placeholder="筛选本讲思路考点..."
                value={searchQuery}
                onChange={(e) => setSearchQuery(e.target.value)}
                className="w-full bg-[var(--well)] border border-transparent focus:border-[var(--line)] rounded-[8px] pl-8 pr-3 py-1.5 text-xs text-[var(--ink)] placeholder-[var(--muted)] focus:outline-none"
              />
            </div>

            <div className="flex items-center justify-between gap-1 text-[11px] font-mono">
              <button
                onClick={() => setStatusFilter('all')}
                className={`px-2 py-1 rounded-[6px] transition-colors ${
                  statusFilter === 'all'
                    ? 'bg-[var(--ink)] text-[var(--paper)] font-semibold'
                    : 'bg-[var(--well)] text-[var(--muted)] hover:text-[var(--ink)]'
                }`}
              >
                全部 ({topics.length})
              </button>
              <button
                onClick={() => setStatusFilter('mastered')}
                className={`px-2 py-1 rounded-[6px] transition-colors ${
                  statusFilter === 'mastered'
                    ? 'bg-[var(--green-bg)] text-[var(--green)] font-semibold border border-[var(--green)]'
                    : 'bg-[var(--well)] text-[var(--muted)] hover:text-[var(--ink)]'
                }`}
              >
                已掌握
              </button>
              <button
                onClick={() => setStatusFilter('struggling')}
                className={`px-2 py-1 rounded-[6px] transition-colors ${
                  statusFilter === 'struggling'
                    ? 'bg-[var(--amber-bg)] text-[var(--amber)] font-semibold border border-[var(--amber)]'
                    : 'bg-[var(--well)] text-[var(--muted)] hover:text-[var(--ink)]'
                }`}
              >
                推导困难
              </button>
            </div>
          </div>

          {/* Topics List Container */}
          <div className="space-y-2 overflow-y-auto max-h-[420px] md:max-h-[600px] pr-1">
            {filteredTopics.length === 0 ? (
              <div className="text-center py-8 text-xs font-mono text-[var(--muted)] bg-[var(--sheet)] border border-[var(--line)] rounded-[12px]">
                无匹配考点
              </div>
            ) : (
              filteredTopics.map((t) => {
                const isSelected = activeTopic?.id === t.id;
                const status = localStorage.getItem('kaoyan_math1_learning_status');
                const map = status ? JSON.parse(status) : {};
                const nodeStatus: LearningStatus = map[t.id] || 'unlearned';

                return (
                  <div
                    key={t.id}
                    onClick={() => {
                      setActiveTopicId(t.id);
                      setIsMobileListOpen(false);
                    }}
                    className={`p-3 sm:p-3.5 rounded-[12px] border transition-all cursor-pointer ${
                      isSelected
                        ? 'bg-[var(--sheet)] border-[var(--blue)] shadow-sm'
                        : 'bg-[var(--sheet)] hover:bg-[var(--well)] border-[var(--line)]'
                    }`}
                  >
                    <div className="flex items-start justify-between gap-2">
                      <div className="flex-1">
                        <div className="flex items-center gap-1.5 flex-wrap">
                          <h4 className={`text-xs font-semibold ${isSelected ? 'text-[var(--blue)]' : 'text-[var(--ink)]'}`}>
                            {t.title}
                          </h4>
                          {TOPIC_TO_LECTURE[t.id] && (
                            <button
                              type="button"
                              onClick={(e) => {
                                e.stopPropagation();
                                onOpenMakiLecture?.(TOPIC_TO_LECTURE[t.id].lectureId);
                              }}
                              className="inline-flex items-center gap-0.5 text-[9.5px] font-mono px-1 py-0.2 rounded bg-purple-50 text-purple-700 dark:bg-purple-950/40 dark:text-purple-300 border border-purple-200 dark:border-purple-800 hover:bg-purple-100 dark:hover:bg-purple-900 transition-colors"
                              title={`大串讲 ${TOPIC_TO_LECTURE[t.id].lectureId} ${TOPIC_TO_LECTURE[t.id].lectureTitle}`}
                            >
                              <span>{TOPIC_TO_LECTURE[t.id].lectureId}</span>
                              <span className="opacity-70 text-[8px]">↗</span>
                            </button>
                          )}
                          {t.isPending && (
                            <span className="text-[10px] font-mono px-1 py-0.2 rounded bg-[var(--well)] text-[var(--muted)] border border-[var(--line)]">
                              待补充
                            </span>
                          )}
                        </div>
                        <p className="text-[11px] text-[var(--muted)] mt-1 line-clamp-1">
                          <MathView content={t.summary} inline />
                        </p>
                      </div>

                      <div className="flex-shrink-0 pt-0.5">
                        {nodeStatus === 'mastered' ? (
                          <span className="text-[10px] font-mono px-1.5 py-0.5 rounded bg-[var(--green-bg)] text-[var(--green)]">
                            已掌握
                          </span>
                        ) : nodeStatus === 'struggling' ? (
                          <span className="text-[10px] font-mono px-1.5 py-0.5 rounded bg-[var(--amber-bg)] text-[var(--amber)]">
                            困难
                          </span>
                        ) : (
                          <span className="text-[10px] font-mono text-[var(--muted)]">未练</span>
                        )}
                      </div>
                    </div>
                  </div>
                );
              })
            )}
          </div>
        </div>

        {/* Right Column: Active Topic Content Panel */}
        <div className="flex-1 min-w-0">
          {activeTopic ? (
            <div className="bg-[var(--sheet)] border border-[var(--line)] rounded-[14px] p-4 sm:p-6 lg:p-7 space-y-4 sm:space-y-5 shadow-sm">
              {/* Header */}
              <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-3 pb-3 sm:pb-4 border-b border-[var(--line)]">
                <div>
                  <div className="flex items-center gap-2">
                    <span className="font-mono text-xs px-2 py-0.5 rounded-[4px] bg-[var(--well)] text-[var(--blue)] font-bold">
                      考点精讲
                    </span>
                    <h2 className="text-base sm:text-lg font-display font-bold text-[var(--ink)] tracking-tight">
                      {activeTopic.title}
                    </h2>
                  </div>
                  <div className="flex items-center gap-2 mt-1 flex-wrap text-xs font-mono text-[var(--muted)]">
                    <span>所属章节：{activeTopic.chapterTitle}</span>
                    {TOPIC_TO_LECTURE[activeTopic.id] && (
                      <>
                        <span>•</span>
                        <button
                          type="button"
                          onClick={() => onOpenMakiLecture?.(TOPIC_TO_LECTURE[activeTopic.id].lectureId)}
                          className="inline-flex items-center gap-1 text-purple-700 dark:text-purple-300 hover:underline"
                        >
                          <BookOpen className="w-3 h-3" />
                          <span>对应大串讲：{TOPIC_TO_LECTURE[activeTopic.id].lectureId} {TOPIC_TO_LECTURE[activeTopic.id].lectureTitle} ↗</span>
                        </button>
                      </>
                    )}
                  </div>
                </div>

                <button
                  onClick={() => onSelectTopic(activeTopic.id)}
                  className="w-full sm:w-auto flex items-center justify-center gap-1.5 px-3.5 py-2 bg-[var(--ink)] hover:opacity-90 text-[var(--paper)] rounded-[8px] text-xs font-bold transition-all shadow-xs"
                >
                  <span>进入完整思路推导页</span>
                  <ExternalLink className="w-3.5 h-3.5" />
                </button>
              </div>

              {/* 一句话记忆 */}
              <div className="p-3.5 sm:p-4 rounded-[10px] bg-[var(--well)] border-l-2 border-[var(--blue)]">
                <div className="text-xs font-mono font-bold text-[var(--blue)] mb-1">
                  § 一句话记忆
                </div>
                <div className="text-xs sm:text-sm text-[var(--ink)] font-medium leading-relaxed font-body">
                  <MathView content={activeTopic.summary} inline />
                </div>
              </div>

              {/* 触发信号 vs 第一反应 */}
              <div className="grid grid-cols-1 md:grid-cols-2 gap-3 sm:gap-4">
                <div className="bg-[var(--well)] border border-[var(--line)] p-3.5 sm:p-4 rounded-[10px]">
                  <h3 className="text-xs font-mono font-bold text-[var(--amber)] mb-2">
                    [触发信号] 题目中看到什么？
                  </h3>
                  <ul className="space-y-1.5 text-xs text-[var(--ink)]">
                    {activeTopic.triggers.map((trig, idx) => (
                      <li key={idx} className="flex items-start gap-1.5">
                        <span className="text-[var(--muted)] font-mono">•</span>
                        <span className="leading-relaxed"><MathView content={trig} inline /></span>
                      </li>
                    ))}
                  </ul>
                </div>

                <div className="bg-[var(--well)] border border-[var(--line)] p-3.5 sm:p-4 rounded-[10px]">
                  <h3 className="text-xs font-mono font-bold text-[var(--blue)] mb-2">
                    [第一反应] 应该想到什么？
                  </h3>
                  <div className="text-xs text-[var(--ink)] leading-relaxed font-body">
                    <MathView content={activeTopic.firstReaction} inline />
                  </div>
                </div>
              </div>

              {/* Formulas */}
              {activeTopic.formulas && activeTopic.formulas.length > 0 && (
                <div className="bg-[var(--well)] border border-[var(--line)] p-3.5 sm:p-4 rounded-[10px]">
                  <h3 className="text-xs font-mono font-bold text-[var(--purple)] mb-2">
                    [核心公式]
                  </h3>
                  <div className="space-y-2">
                    {activeTopic.formulas.map((f, idx) => (
                      <div key={idx} className="bg-[var(--sheet)] p-3 rounded-[8px] border border-[var(--line)] text-xs">
                        <div className="font-semibold text-[var(--ink)] mb-1">{f.title}:</div>
                        <div className="text-[var(--ink)] overflow-x-auto py-1">
                          <MathView content={`$$${f.latex}$$`} />
                        </div>
                      </div>
                    ))}
                  </div>
                </div>
              )}

              {/* Status Switcher */}
              <div className="pt-3 sm:pt-4 border-t border-[var(--line)] flex flex-col sm:flex-row sm:items-center justify-between gap-2.5 sm:gap-3 font-mono text-xs">
                <span className="text-[var(--muted)]">标记我的掌握状态：</span>
                <div className="flex items-center gap-1.5 sm:gap-2">
                  <button
                    onClick={() => handleUpdateStatus(activeTopic.id, 'unlearned')}
                    className="flex-1 sm:flex-initial px-2.5 sm:px-3 py-1.5 rounded-[6px] bg-[var(--well)] hover:bg-[var(--line)] border border-[var(--line)] text-[var(--muted)] text-center text-xs"
                  >
                    未掌握
                  </button>
                  <button
                    onClick={() => handleUpdateStatus(activeTopic.id, 'struggling')}
                    className="flex-1 sm:flex-initial px-2.5 sm:px-3 py-1.5 rounded-[6px] bg-[var(--amber-bg)] hover:opacity-90 border border-[var(--amber)] text-[var(--amber)] font-bold text-center text-xs"
                  >
                    推导困难
                  </button>
                  <button
                    onClick={() => handleUpdateStatus(activeTopic.id, 'mastered')}
                    className="flex-1 sm:flex-initial px-2.5 sm:px-3 py-1.5 rounded-[6px] bg-[var(--green-bg)] hover:opacity-90 border border-[var(--green)] text-[var(--green)] font-bold text-center text-xs"
                  >
                    已掌握
                  </button>
                </div>
              </div>
            </div>
          ) : (
            <div className="bg-[var(--sheet)] border border-[var(--line)] rounded-[14px] p-12 text-center text-[var(--muted)] font-mono">
              请选择考点查看思路
            </div>
          )}
        </div>
      </div>
    </div>
  );
};
