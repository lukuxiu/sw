import React, { useState, useRef, useEffect } from 'react';
import { 
  ZoomIn, ZoomOut, RotateCcw, ChevronRight, ChevronDown, 
  Minus, Plus, ArrowRight
} from 'lucide-react';
import { SUBJECTS, CHAPTERS } from '../data/subjects';
import { KNOWLEDGE_BASE } from '../data/knowledgeBase';
import { SubjectId, LearningStatus } from '../data/types';
import { getAllLearningStatuses } from '../data/storage';

interface MindmapViewProps {
  onSelectChapter: (chapterId: string) => void;
  onSelectTopic: (topicId: string) => void;
  highlightTopicId?: string;
}

export const MindmapView: React.FC<MindmapViewProps> = ({
  onSelectChapter,
  onSelectTopic,
  highlightTopicId,
}) => {
  const containerRef = useRef<HTMLDivElement>(null);

  const [scale, setScale] = useState<number>(0.85);
  const [position, setPosition] = useState<{ x: number; y: number }>({ x: 60, y: 260 });
  const [isDragging, setIsDragging] = useState<boolean>(false);
  const [dragStart, setDragStart] = useState<{ x: number; y: number }>({ x: 0, y: 0 });

  const [expandedSubjects, setExpandedSubjects] = useState<Record<string, boolean>>({
    gaoshu: true,
    xiandai: true,
    gailv: true,
  });

  const [expandedChapters, setExpandedChapters] = useState<Record<string, boolean>>({
    'gaoshu-ch01': true,
    'gaoshu-ch07': true,
    'xiandai-ch04': true,
    'gailv-ch04': true,
  });

  const [learningStatuses, setLearningStatuses] = useState<Record<string, LearningStatus>>({});

  useEffect(() => {
    setLearningStatuses(getAllLearningStatuses());
    const onStatusChange = () => setLearningStatuses(getAllLearningStatuses());
    window.addEventListener('learning-status-change', onStatusChange);
    return () => window.removeEventListener('learning-status-change', onStatusChange);
  }, []);

  const handleResetCenter = () => {
    setScale(0.85);
    setPosition({ x: 60, y: 260 });
  };

  const handleZoomIn = () => setScale((s) => Math.min(s + 0.15, 2.0));
  const handleZoomOut = () => setScale((s) => Math.max(s - 0.15, 0.4));

  const handleWheel = (e: React.WheelEvent) => {
    e.preventDefault();
    const zoomFactor = -e.deltaY * 0.001;
    setScale((prevScale) => Math.min(Math.max(prevScale + zoomFactor, 0.35), 2.2));
  };

  const handleMouseDown = (e: React.MouseEvent) => {
    if ((e.target as HTMLElement).closest('.interactive-node')) return;
    setIsDragging(true);
    setDragStart({ x: e.clientX - position.x, y: e.clientY - position.y });
  };

  const handleMouseMove = (e: React.MouseEvent) => {
    if (!isDragging) return;
    setPosition({
      x: e.clientX - dragStart.x,
      y: e.clientY - dragStart.y,
    });
  };

  const handleMouseUp = () => setIsDragging(false);

  const toggleSubject = (sid: string, e: React.MouseEvent) => {
    e.stopPropagation();
    setExpandedSubjects((prev) => ({ ...prev, [sid]: !prev[sid] }));
  };

  const toggleChapter = (cid: string, e: React.MouseEvent) => {
    e.stopPropagation();
    setExpandedChapters((prev) => ({ ...prev, [cid]: !prev[cid] }));
  };

  const handleToggleAll = (expand: boolean) => {
    setExpandedSubjects({
      gaoshu: expand,
      xiandai: expand,
      gailv: expand,
    });
    const allChs: Record<string, boolean> = {};
    Object.keys(CHAPTERS).forEach((cid) => {
      allChs[cid] = expand;
    });
    setExpandedChapters(allChs);
  };

  return (
    <div className="relative w-full h-[calc(100vh-56px)] overflow-hidden maki-grid-pattern select-none cursor-grab active:cursor-grabbing font-body">
      {/* Maki Style Toolbar */}
      <div className="absolute top-4 left-4 z-30 flex items-center gap-2 bg-[var(--sheet)] border border-[var(--line)] px-3 py-1.5 rounded-[9px] shadow-sm text-xs text-[var(--ink)]">
        <span className="font-mono text-[var(--muted)] mr-1 text-[11px]">
          [缩放: {Math.round(scale * 100)}%]
        </span>

        <button
          onClick={handleZoomIn}
          title="放大"
          className="p-1 hover:bg-[var(--well)] rounded-[6px] transition-colors text-[var(--muted)] hover:text-[var(--ink)]"
        >
          <ZoomIn className="w-3.5 h-3.5" />
        </button>

        <button
          onClick={handleZoomOut}
          title="缩小"
          className="p-1 hover:bg-[var(--well)] rounded-[6px] transition-colors text-[var(--muted)] hover:text-[var(--ink)]"
        >
          <ZoomOut className="w-3.5 h-3.5" />
        </button>

        <button
          onClick={handleResetCenter}
          title="重置居中"
          className="p-1 hover:bg-[var(--well)] rounded-[6px] transition-colors text-[var(--muted)] hover:text-[var(--ink)] flex items-center gap-1 font-mono text-[11px]"
        >
          <RotateCcw className="w-3.5 h-3.5" />
          <span>居中</span>
        </button>

        <div className="h-3.5 w-px bg-[var(--line)] mx-1" />

        <button
          onClick={() => handleToggleAll(true)}
          className="px-2 py-0.5 bg-[var(--well)] hover:bg-[var(--line)] rounded-[6px] text-[var(--ink)] text-[11px] font-mono transition-colors"
        >
          展开全部
        </button>

        <button
          onClick={() => handleToggleAll(false)}
          className="px-2 py-0.5 bg-[var(--well)] hover:bg-[var(--line)] rounded-[6px] text-[var(--ink)] text-[11px] font-mono transition-colors"
        >
          收起全部
        </button>
      </div>

      {/* Maki Style Bottom Legend */}
      <div className="absolute bottom-4 left-4 z-30 hidden md:flex items-center gap-4 bg-[var(--sheet)] border border-[var(--line)] px-3.5 py-1.5 rounded-[8px] text-xs text-[var(--muted)] font-mono shadow-sm">
        <span>画布交互: 拖拽平移 · 滚轮缩放 · 节点展开/折叠</span>
        <div className="h-3 w-px bg-[var(--line)]" />
        <span className="flex items-center gap-1 text-[var(--ink)]">
          三大板块: 高等数学 (56%) · 线性代数 (22%) · 概率论与数理统计 (22%)
        </span>
      </div>

      {/* Main Graph Canvas */}
      <div
        ref={containerRef}
        onWheel={handleWheel}
        onMouseDown={handleMouseDown}
        onMouseMove={handleMouseMove}
        onMouseUp={handleMouseUp}
        className="w-full h-full relative"
      >
        <div
          className="absolute origin-top-left transition-transform duration-75 ease-out"
          style={{
            transform: `translate(${position.x}px, ${position.y}px) scale(${scale})`,
          }}
        >
          <div className="flex items-center space-x-14">
            
            {/* Level 0: Central Node */}
            <div className="interactive-node relative z-20 flex-shrink-0">
              <div className="relative px-6 py-5 rounded-[14px] bg-[var(--sheet)] border border-[var(--line)] shadow-sm text-center w-56">
                <div className="text-[11px] font-mono text-[var(--muted)] uppercase tracking-wider mb-1">
                  Maki 考研数学一
                </div>
                <h1 className="text-xl font-display font-bold tracking-tight text-[var(--ink)]">
                  解题思路全景导图
                </h1>
                <div className="mt-3 pt-2.5 border-t border-[var(--line)] text-[11px] font-mono text-[var(--muted)]">
                  3 板块 · 26 章节 · 74 考点
                </div>
              </div>
            </div>

            {/* Level 1: Three Core Mathematical Subjects */}
            <div className="flex flex-col space-y-12">
              {(['gaoshu', 'xiandai', 'gailv'] as SubjectId[]).map((sid) => {
                const subj = SUBJECTS[sid];
                const isExpanded = !!expandedSubjects[sid];
                const chapters = subj.chapterIds.map((cid) => CHAPTERS[cid]);

                const subjectMeta = {
                  gaoshu: { code: '01', ratio: '56%', badge: '高等数学' },
                  xiandai: { code: '02', ratio: '22%', badge: '线性代数' },
                  gailv: { code: '03', ratio: '22%', badge: '概率统计' },
                }[sid];

                return (
                  <div key={sid} className="flex items-center space-x-12">
                    {/* Subject Card */}
                    <div className="interactive-node relative z-10 flex-shrink-0">
                      <div className="relative w-64 p-4 rounded-[14px] bg-[var(--sheet)] border border-[var(--line)] hover:border-[var(--blue)] transition-colors shadow-sm">
                        <div className="flex items-center justify-between">
                          <div className="flex items-center space-x-2">
                            <span className="font-mono text-xs font-bold text-[var(--muted)] bg-[var(--well)] px-1.5 py-0.5 rounded-[4px] border border-[var(--line)]">
                              {subjectMeta.code}
                            </span>
                            <h2 className="text-base font-display font-bold text-[var(--ink)] tracking-tight">
                              {subj.name}
                            </h2>
                          </div>

                          <button
                            onClick={(e) => toggleSubject(sid, e)}
                            className="p-1 rounded-[6px] bg-[var(--well)] hover:bg-[var(--line)] text-[var(--muted)] hover:text-[var(--ink)] border border-[var(--line)] transition-colors"
                            title={isExpanded ? '收起章节' : '展开章节'}
                          >
                            {isExpanded ? (
                              <Minus className="w-3.5 h-3.5" />
                            ) : (
                              <Plus className="w-3.5 h-3.5" />
                            )}
                          </button>
                        </div>

                        <p className="text-xs text-[var(--muted)] mt-2 line-clamp-2 leading-relaxed font-body">
                          {subj.description}
                        </p>

                        <div className="mt-3 flex items-center justify-between text-[11px] font-mono pt-2 border-t border-[var(--line)] text-[var(--muted)]">
                          <span>{subj.chapterIds.length} 个章节</span>
                          <span className="text-[var(--blue)]">分值约 {subjectMeta.ratio}</span>
                        </div>
                      </div>
                    </div>

                    {/* Level 2: Chapters Branch */}
                    {isExpanded && (
                      <div className="flex flex-col space-y-3 pl-3 border-l border-[var(--line)]">
                        {chapters.map((ch) => {
                          const isChExpanded = !!expandedChapters[ch.id];
                          const topics = ch.topicIds.map((tid) => KNOWLEDGE_BASE[tid]).filter(Boolean);

                          return (
                            <div key={ch.id} className="flex items-center space-x-8">
                              {/* Chapter Node Card */}
                              <div className="interactive-node relative flex-shrink-0">
                                <div
                                  onClick={() => onSelectChapter(ch.id)}
                                  className="w-72 p-3 rounded-[10px] bg-[var(--sheet)] hover:bg-[var(--well)] border border-[var(--line)] hover:border-[var(--blue)] transition-all cursor-pointer group"
                                >
                                  <div className="flex items-center justify-between">
                                    <div className="flex items-center space-x-2">
                                      <span className="text-[10px] font-mono font-bold text-[var(--muted)] px-1.5 py-0.5 bg-[var(--well)] rounded-[4px] border border-[var(--line)]">
                                        第 {ch.order} 讲
                                      </span>
                                      <h3 className="text-xs font-semibold text-[var(--ink)] group-hover:text-[var(--blue)] transition-colors">
                                        {ch.title}
                                      </h3>
                                    </div>

                                    <button
                                      onClick={(e) => toggleChapter(ch.id, e)}
                                      className="p-1 rounded-[4px] bg-[var(--well)] hover:bg-[var(--line)] text-[var(--muted)] hover:text-[var(--ink)] transition-colors"
                                      title={isChExpanded ? '收起考点' : '展开考点'}
                                    >
                                      {isChExpanded ? (
                                        <ChevronDown className="w-3.5 h-3.5" />
                                      ) : (
                                        <ChevronRight className="w-3.5 h-3.5" />
                                      )}
                                    </button>
                                  </div>

                                  <div className="mt-2 flex items-center justify-between text-[11px] font-mono text-[var(--muted)] pt-1.5 border-t border-[var(--line)]">
                                    <span>{topics.length} 个思路考点</span>
                                    <span className="flex items-center gap-1 text-[var(--blue)] group-hover:underline">
                                      进入章节
                                      <ArrowRight className="w-3 h-3" />
                                    </span>
                                  </div>
                                </div>
                              </div>

                              {/* Level 3: Topics Nodes */}
                              {isChExpanded && (
                                <div className="flex flex-col space-y-2 pl-3 border-l border-[var(--line)]">
                                  {topics.map((t) => {
                                    const status = learningStatuses[t.id] || 'unlearned';
                                    const isHighlighted = highlightTopicId === t.id;

                                    return (
                                      <div
                                        key={t.id}
                                        onClick={() => onSelectTopic(t.id)}
                                        className={`interactive-node w-80 p-3 rounded-[9px] border transition-all cursor-pointer ${
                                          isHighlighted
                                            ? 'bg-[var(--blue-bg)] border-[var(--blue)]'
                                            : 'bg-[var(--sheet)] hover:bg-[var(--well)] border-[var(--line)] hover:border-[var(--muted)]'
                                        }`}
                                      >
                                        <div className="flex items-start justify-between gap-2">
                                          <div className="flex-1">
                                            <div className="flex items-center gap-1.5 flex-wrap">
                                              <span className="text-xs font-semibold text-[var(--ink)] hover:text-[var(--blue)]">
                                                {t.title}
                                              </span>
                                              {t.isPending && (
                                                <span className="text-[10px] font-mono px-1 py-0.2 rounded bg-[var(--well)] text-[var(--muted)] border border-[var(--line)]">
                                                  待补充
                                                </span>
                                              )}
                                            </div>
                                            <p className="text-[11px] text-[var(--muted)] mt-1 line-clamp-1 leading-relaxed">
                                              {t.summary}
                                            </p>
                                          </div>

                                          {/* Status Indicator */}
                                          <div className="flex-shrink-0 pt-0.5">
                                            {status === 'mastered' ? (
                                              <span className="text-[10px] font-mono px-1.5 py-0.5 rounded bg-[var(--green-bg)] text-[var(--green)] border border-[var(--green)]">
                                                已掌握
                                              </span>
                                            ) : status === 'struggling' ? (
                                              <span className="text-[10px] font-mono px-1.5 py-0.5 rounded bg-[var(--amber-bg)] text-[var(--amber)] border border-[var(--amber)]">
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
                                          <div className="mt-2 pt-1.5 border-t border-[var(--line)] flex items-center gap-1 text-[10px] font-mono text-[var(--muted)]">
                                            <span className="text-[var(--blue)]">看到:</span>
                                            <span className="truncate">{t.triggers[0]}</span>
                                          </div>
                                        )}
                                      </div>
                                    );
                                  })}
                                </div>
                              )}
                            </div>
                          );
                        })}
                      </div>
                    )}
                  </div>
                );
              })}
            </div>

          </div>
        </div>
      </div>
    </div>
  );
};
