import React, { useState, useMemo } from 'react';
import { 
  X, CheckCircle2, HelpCircle, ArrowRight, Award
} from 'lucide-react';
import { KNOWLEDGE_BASE } from '../data/knowledgeBase';
import { LearningStatus } from '../data/types';
import { MathView } from './MathView';
import { getAllLearningStatuses, getOverallProgress, setLearningStatus } from '../data/storage';

interface ReviewModalProps {
  isOpen: boolean;
  onClose: () => void;
  onSelectTopic: (topicId: string) => void;
}

export const ReviewModal: React.FC<ReviewModalProps> = ({
  isOpen,
  onClose,
  onSelectTopic,
}) => {
  if (!isOpen) return null;

  const [filter, setFilter] = useState<'all' | LearningStatus>('struggling');
  const [statuses, setStatuses] = useState(getAllLearningStatuses());
  const progress = useMemo(() => getOverallProgress(), [statuses]);

  const allTopics = useMemo(() => {
    return Object.values(KNOWLEDGE_BASE);
  }, []);

  const filteredTopics = useMemo(() => {
    return allTopics.filter((t) => {
      const s = statuses[t.id] || 'unlearned';
      if (filter === 'all') return true;
      return s === filter;
    });
  }, [allTopics, statuses, filter]);

  const handleUpdateStatus = (nodeId: string, s: LearningStatus) => {
    setLearningStatus(nodeId, s);
    setStatuses(getAllLearningStatuses());
  };

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center p-2 sm:p-4 bg-black/60 backdrop-blur-xs font-body">
      <div className="bg-[var(--sheet)] border border-[var(--line)] rounded-[14px] w-full max-w-3xl max-h-[85vh] flex flex-col shadow-2xl overflow-hidden">
        {/* Modal Header */}
        <div className="px-4 sm:px-6 py-3 sm:py-4 bg-[var(--well)] border-b border-[var(--line)] flex items-center justify-between">
          <div className="flex items-center gap-2.5">
            <div className="p-1.5 rounded-[6px] bg-[var(--sheet)] text-[var(--blue)] border border-[var(--line)]">
              <Award className="w-4 h-4" />
            </div>
            <div>
              <h2 className="text-base font-display font-bold text-[var(--ink)] tracking-tight">
                复习与薄弱点清单 (Review Hub)
              </h2>
              <p className="text-[11px] text-[var(--muted)] font-mono">
                定位推导困难点，按图索骥攻克薄弱环节
              </p>
            </div>
          </div>
          <button
            onClick={onClose}
            className="p-1.5 rounded-[6px] text-[var(--muted)] hover:text-[var(--ink)] hover:bg-[var(--line)] transition-colors"
          >
            <X className="w-4 h-4" />
          </button>
        </div>

        {/* Overview Stats Bar */}
        <div className="px-4 sm:px-6 py-2.5 sm:py-3 bg-[var(--sheet)] border-b border-[var(--line)] flex flex-wrap items-center justify-between gap-2 sm:gap-4 font-mono text-xs">
          <div className="flex items-center gap-4">
            <div>
              <span className="text-[var(--muted)]">已掌握: </span>
              <span className="font-bold text-[var(--ink)]">
                {progress.mastered} / {progress.total}
              </span>
            </div>
            <div className="h-4 w-px bg-[var(--line)]" />
            <div>
              <span className="text-[var(--amber)]">推导困难: </span>
              <span className="font-bold text-[var(--amber)]">
                {progress.struggling}
              </span>
            </div>
          </div>

          {/* Filter tabs */}
          <div className="flex items-center gap-1 bg-[var(--well)] p-0.5 rounded-[8px] border border-[var(--line)] text-[11px]">
            <button
              onClick={() => setFilter('struggling')}
              className={`px-2.5 py-1 rounded-[6px] transition-colors ${
                filter === 'struggling'
                  ? 'bg-[var(--amber-bg)] text-[var(--amber)] font-bold border border-[var(--amber)]'
                  : 'text-[var(--muted)] hover:text-[var(--ink)]'
              }`}
            >
              <span className="hidden sm:inline">推导困难</span><span className="inline sm:hidden">困难</span> ({progress.struggling})
            </button>
            <button
              onClick={() => setFilter('mastered')}
              className={`px-2.5 py-1 rounded-[6px] transition-colors ${
                filter === 'mastered'
                  ? 'bg-[var(--green-bg)] text-[var(--green)] font-bold border border-[var(--green)]'
                  : 'text-[var(--muted)] hover:text-[var(--ink)]'
              }`}
            >
              <span className="hidden sm:inline">已完全掌握</span><span className="inline sm:hidden">已掌握</span> ({progress.mastered})
            </button>
            <button
              onClick={() => setFilter('all')}
              className={`px-2.5 py-1 rounded-[6px] transition-colors ${
                filter === 'all'
                  ? 'bg-[var(--sheet)] text-[var(--ink)] font-bold shadow-sm'
                  : 'text-[var(--muted)] hover:text-[var(--ink)]'
              }`}
            >
              全部 ({progress.total})
            </button>
          </div>
        </div>

        {/* Topic List */}
        <div className="flex-1 overflow-y-auto p-3 sm:p-6 space-y-2 sm:space-y-2.5">
          {filteredTopics.length === 0 ? (
            <div className="text-center py-12 text-[var(--muted)] font-mono text-xs space-y-1">
              <p>暂无该状态下的考点</p>
              <p className="text-[var(--muted)]">
                做题或复习时可在考点详情页点击“推导困难”进行归集。
              </p>
            </div>
          ) : (
            filteredTopics.map((topic) => {
              const s = statuses[topic.id] || 'unlearned';

              return (
                <div
                  key={topic.id}
                  className="bg-[var(--well)] border border-[var(--line)] hover:border-[var(--blue)] p-3.5 rounded-[10px] flex flex-col sm:flex-row sm:items-center justify-between gap-3 transition-colors"
                >
                  <div className="flex-1">
                    <div className="flex items-center gap-2 flex-wrap">
                      <span 
                        className="text-xs font-semibold text-[var(--ink)] hover:text-[var(--blue)] cursor-pointer"
                        onClick={() => { onSelectTopic(topic.id); onClose(); }}
                      >
                        {topic.title}
                      </span>
                      <span className="text-[10px] font-mono px-1.5 py-0.2 rounded bg-[var(--sheet)] text-[var(--muted)] border border-[var(--line)]">
                        {topic.subjectName} · {topic.chapterTitle}
                      </span>
                    </div>
                    <div className="text-xs text-[var(--muted)] mt-1 line-clamp-1 leading-relaxed font-body">
                      <MathView content={topic.summary} inline />
                    </div>
                  </div>

                  {/* Actions */}
                  <div className="flex items-center justify-between sm:justify-end gap-2 flex-shrink-0 font-mono text-xs mt-2 sm:mt-0 pt-2 sm:pt-0 border-t sm:border-0 border-[var(--line)]">
                    <div className="flex items-center gap-1 bg-[var(--sheet)] p-0.5 rounded-[6px] border border-[var(--line)]">
                      <button
                        onClick={() => handleUpdateStatus(topic.id, 'struggling')}
                        className={`px-1.5 py-0.5 rounded-[4px] text-[11px] ${
                          s === 'struggling' ? 'bg-[var(--amber-bg)] text-[var(--amber)] font-bold border border-[var(--amber)]' : 'text-[var(--muted)] hover:text-[var(--ink)]'
                        }`}
                        title="标记为推导困难"
                      >
                        困难
                      </button>
                      <button
                        onClick={() => handleUpdateStatus(topic.id, 'mastered')}
                        className={`px-1.5 py-0.5 rounded-[4px] text-[11px] ${
                          s === 'mastered' ? 'bg-[var(--green-bg)] text-[var(--green)] font-bold border border-[var(--green)]' : 'text-[var(--muted)] hover:text-[var(--ink)]'
                        }`}
                        title="标记为能够独立完成"
                      >
                        已掌握
                      </button>
                    </div>

                    <button
                      onClick={() => {
                        onSelectTopic(topic.id);
                        onClose();
                      }}
                      className="flex items-center gap-1 px-3 py-1.5 rounded-[6px] bg-[var(--ink)] hover:opacity-90 text-[var(--paper)] text-xs font-bold transition-all"
                    >
                      <span>前往推导</span>
                      <ArrowRight className="w-3 h-3" />
                    </button>
                  </div>
                </div>
              );
            })
          )}
        </div>
      </div>
    </div>
  );
};
