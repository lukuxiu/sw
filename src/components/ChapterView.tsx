import React, { useState, useMemo } from 'react';
import { 
  ArrowLeft, ArrowRight, ExternalLink, Search, Target, Compass
} from 'lucide-react';
import { CHAPTERS, SUBJECTS } from '../data/subjects';
import { KNOWLEDGE_BASE } from '../data/knowledgeBase';
import { LearningStatus, KnowledgeNode } from '../data/types';
import { getChapterProgress, setLearningStatus } from '../data/storage';
import { MathView } from './MathView';

interface ChapterViewProps {
  chapterId: string;
  onBackToMindmap: () => void;
  onSelectTopic: (topicId: string) => void;
  initialTopicId?: string;
}

export const ChapterView: React.FC<ChapterViewProps> = ({
  chapterId,
  onBackToMindmap,
  onSelectTopic,
  initialTopicId,
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
      <div className="bg-[var(--sheet)] border-b border-[var(--line)] px-4 lg:px-8 py-5">
        <div className="max-w-7xl mx-auto">
          {/* Breadcrumbs */}
          <div className="flex items-center space-x-2 text-xs font-mono text-[var(--muted)] mb-3">
            <button
              onClick={onBackToMindmap}
              className="flex items-center gap-1 text-[var(--blue)] hover:underline transition-colors"
            >
              <Compass className="w-3.5 h-3.5" />
              总思维导图
            </button>
            <span>/</span>
            <span>{subject.name}</span>
            <span>/</span>
            <span className="text-[var(--ink)] font-semibold">{chapter.title}</span>
          </div>

          <div className="flex flex-col md:flex-row md:items-center justify-between gap-4">
            <div>
              <div className="flex items-center gap-3">
                <button
                  onClick={onBackToMindmap}
                  className="p-1.5 rounded-[7px] bg-[var(--well)] hover:bg-[var(--line)] text-[var(--ink)] border border-[var(--line)] transition-colors"
                  title="返回思维导图"
                >
                  <ArrowLeft className="w-4 h-4" />
                </button>
                <h1 className="text-xl sm:text-2xl font-display font-bold text-[var(--ink)] tracking-tight">
                  第 {chapter.order} 讲：{chapter.title}
                </h1>
                <span className="text-xs font-mono px-2 py-0.5 rounded-[999px] bg-[var(--well)] text-[var(--muted)] border border-[var(--line)]">
                  {subject.name}
                </span>
              </div>
              <p className="text-xs sm:text-sm text-[var(--muted)] mt-2 max-w-3xl leading-relaxed font-body">
                {chapter.description}
              </p>
            </div>

            {/* Chapter Progress Stats */}
            <div className="flex items-center gap-4 bg-[var(--well)] border border-[var(--line)] p-3.5 rounded-[12px] flex-shrink-0">
              <div className="text-center font-mono">
                <div className="text-base font-bold text-[var(--ink)]">
                  {progress.mastered} / {progress.total}
                </div>
                <div className="text-[10px] text-[var(--muted)]">已掌握考点</div>
              </div>

              <div className="h-7 w-px bg-[var(--line)]" />

              <div className="w-28 font-mono">
                <div className="flex justify-between text-[11px] mb-1">
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
            <div className="mt-4 pt-4 border-t border-[var(--line)]">
              <div className="flex items-center gap-1.5 text-xs font-semibold text-[var(--ink)] mb-2 font-mono">
                <Target className="w-3.5 h-3.5 text-[var(--blue)]" />
                本讲复习目标与考查定位：
              </div>
              <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-2">
                {chapter.goals.map((goal, idx) => (
                  <div
                    key={idx}
                    className="flex items-start gap-2 text-xs text-[var(--ink)] bg-[var(--well)] border border-[var(--line)] p-2.5 rounded-[8px]"
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

      {/* Main Two-Column Layout */}
      <div className="max-w-7xl mx-auto w-full flex-1 flex flex-col md:flex-row p-4 lg:p-8 gap-6">
        {/* Left Column: Topic List */}
        <div className="w-full md:w-80 lg:w-96 flex flex-col flex-shrink-0 space-y-3">
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
          <div className="space-y-2 overflow-y-auto max-h-[600px] pr-1">
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
                    onClick={() => setActiveTopicId(t.id)}
                    className={`p-3.5 rounded-[12px] border transition-all cursor-pointer ${
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
                          {t.isPending && (
                            <span className="text-[10px] font-mono px-1 py-0.2 rounded bg-[var(--well)] text-[var(--muted)] border border-[var(--line)]">
                              待补充
                            </span>
                          )}
                        </div>
                        <p className="text-[11px] text-[var(--muted)] mt-1 line-clamp-2 leading-relaxed font-body">
                          {t.summary}
                        </p>
                      </div>

                      <div className="flex-shrink-0 pt-0.5">
                        {nodeStatus === 'mastered' ? (
                          <span className="text-[10px] font-mono px-1.5 py-0.5 rounded-[4px] bg-[var(--green-bg)] text-[var(--green)] border border-[var(--green)]">
                            已掌握
                          </span>
                        ) : nodeStatus === 'struggling' ? (
                          <span className="text-[10px] font-mono px-1.5 py-0.5 rounded-[4px] bg-[var(--amber-bg)] text-[var(--amber)] border border-[var(--amber)]">
                            困难
                          </span>
                        ) : (
                          <span className="text-[10px] font-mono text-[var(--muted)]">
                            未练
                          </span>
                        )}
                      </div>
                    </div>

                    {t.triggers && t.triggers.length > 0 && (
                      <div className="mt-2 text-[10px] font-mono text-[var(--muted)] bg-[var(--well)] px-2 py-1 rounded-[6px] truncate border border-[var(--line)]">
                        看到: {t.triggers[0]}
                      </div>
                    )}
                  </div>
                );
              })
            )}
          </div>
        </div>

        {/* Right Column: Preview & Detailed Route */}
        <div className="flex-1">
          {activeTopic ? (
            <div className="bg-[var(--sheet)] border border-[var(--line)] rounded-[14px] p-6 shadow-sm space-y-6">
              {/* Header */}
              <div className="flex flex-col sm:flex-row sm:items-center justify-between pb-4 border-b border-[var(--line)] gap-3">
                <div>
                  <div className="flex items-center gap-2">
                    <span className="text-xs font-mono px-2 py-0.5 rounded-[999px] bg-[var(--blue-bg)] text-[var(--blue)]">
                      考点精讲
                    </span>
                    <h2 className="text-lg font-display font-bold text-[var(--ink)] tracking-tight">
                      {activeTopic.title}
                    </h2>
                  </div>
                  <p className="text-xs font-mono text-[var(--muted)] mt-1">
                    所属章节：{activeTopic.chapterTitle}
                  </p>
                </div>

                <button
                  onClick={() => onSelectTopic(activeTopic.id)}
                  className="flex items-center gap-1.5 px-3.5 py-2 bg-[var(--ink)] hover:opacity-90 text-[var(--paper)] rounded-[8px] text-xs font-bold transition-all"
                >
                  <span>进入完整思路推导页</span>
                  <ExternalLink className="w-3.5 h-3.5" />
                </button>
              </div>

              {/* 一句话记忆 */}
              <div className="p-4 rounded-[10px] bg-[var(--well)] border-l-2 border-[var(--blue)]">
                <div className="text-xs font-mono font-bold text-[var(--blue)] mb-1">
                  § 一句话记忆
                </div>
                <p className="text-sm text-[var(--ink)] font-medium leading-relaxed font-body">
                  <MathView content={activeTopic.summary} inline />
                </p>
              </div>

              {/* 触发信号 vs 第一反应 */}
              <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                <div className="bg-[var(--well)] border border-[var(--line)] p-4 rounded-[10px]">
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

                <div className="bg-[var(--well)] border border-[var(--line)] p-4 rounded-[10px]">
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
                <div className="bg-[var(--well)] border border-[var(--line)] p-4 rounded-[10px]">
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
              <div className="pt-4 border-t border-[var(--line)] flex flex-col sm:flex-row sm:items-center justify-between gap-3 font-mono text-xs">
                <span className="text-[var(--muted)]">标记我的掌握状态：</span>
                <div className="flex items-center gap-2">
                  <button
                    onClick={() => handleUpdateStatus(activeTopic.id, 'unlearned')}
                    className="px-3 py-1.5 rounded-[6px] bg-[var(--well)] hover:bg-[var(--line)] border border-[var(--line)] text-[var(--muted)]"
                  >
                    未掌握
                  </button>
                  <button
                    onClick={() => handleUpdateStatus(activeTopic.id, 'struggling')}
                    className="px-3 py-1.5 rounded-[6px] bg-[var(--amber-bg)] hover:opacity-90 border border-[var(--amber)] text-[var(--amber)] font-bold"
                  >
                    推导困难
                  </button>
                  <button
                    onClick={() => handleUpdateStatus(activeTopic.id, 'mastered')}
                    className="px-3 py-1.5 rounded-[6px] bg-[var(--green-bg)] hover:opacity-90 border border-[var(--green)] text-[var(--green)] font-bold"
                  >
                    能够独立完成
                  </button>
                </div>
              </div>
            </div>
          ) : (
            <div className="bg-[var(--sheet)] border border-[var(--line)] rounded-[14px] p-12 text-center text-[var(--muted)] font-mono">
              请从左侧选择考点查看思路
            </div>
          )}
        </div>
      </div>
    </div>
  );
};
