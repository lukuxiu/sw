import React, { useState, useRef, useEffect, useMemo } from 'react';
import { 
  ZoomIn, ZoomOut, RotateCcw, ChevronRight, ChevronDown, 
  Minus, Plus, ArrowRight, LayoutGrid, Network, Compass
} from 'lucide-react';
import { SUBJECTS, CHAPTERS } from '../data/subjects';
import { KNOWLEDGE_BASE } from '../data/knowledgeBase';
import { SubjectId, LearningStatus } from '../data/types';
import { getAllLearningStatuses } from '../data/storage';
import { MathView } from './MathView';

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

  // View mode: canvas (interactive 2D graph) vs outline (vertical mobile-first tree)
  const [viewMode, setViewMode] = useState<'canvas' | 'outline'>('canvas');

  // Branch focus: 'all' | 'gaoshu' | 'xiandai' | 'gailv'
  const [focusSubject, setFocusSubject] = useState<'all' | SubjectId>('all');

  const [scale, setScale] = useState<number>(0.85);
  const [position, setPosition] = useState<{ x: number; y: number }>({ x: 40, y: 220 });
  const [isDragging, setIsDragging] = useState<boolean>(false);
  const [dragStart, setDragStart] = useState<{ x: number; y: number }>({ x: 0, y: 0 });

  // Touch pinch state
  const [initialPinchDist, setInitialPinchDist] = useState<number | null>(null);
  const [initialPinchScale, setInitialPinchScale] = useState<number>(0.85);

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

  // For outline mode: which subject is open
  const [outlineOpenSubjects, setOutlineOpenSubjects] = useState<Record<string, boolean>>({
    gaoshu: true,
    xiandai: true,
    gailv: true,
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
    setPosition({ x: 40, y: 220 });
  };

  const handleZoomIn = () => setScale((s) => Math.min(s + 0.15, 2.0));
  const handleZoomOut = () => setScale((s) => Math.max(s - 0.15, 0.4));

  const handleWheel = (e: React.WheelEvent) => {
    e.preventDefault();
    const zoomFactor = -e.deltaY * 0.001;
    setScale((prevScale) => Math.min(Math.max(prevScale + zoomFactor, 0.35), 2.2));
  };

  // Mouse handlers
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

  // Touch handlers (pan and pinch-to-zoom for mobile devices)
  const handleTouchStart = (e: React.TouchEvent) => {
    if ((e.target as HTMLElement).closest('.interactive-node')) return;
    if (e.touches.length === 1) {
      setIsDragging(true);
      setDragStart({
        x: e.touches[0].clientX - position.x,
        y: e.touches[0].clientY - position.y,
      });
      setInitialPinchDist(null);
    } else if (e.touches.length === 2) {
      setIsDragging(false);
      const dist = Math.hypot(
        e.touches[0].clientX - e.touches[1].clientX,
        e.touches[0].clientY - e.touches[1].clientY
      );
      setInitialPinchDist(dist);
      setInitialPinchScale(scale);
    }
  };

  const handleTouchMove = (e: React.TouchEvent) => {
    if (e.touches.length === 1 && isDragging) {
      setPosition({
        x: e.touches[0].clientX - dragStart.x,
        y: e.touches[0].clientY - dragStart.y,
      });
    } else if (e.touches.length === 2 && initialPinchDist !== null) {
      const currentDist = Math.hypot(
        e.touches[0].clientX - e.touches[1].clientX,
        e.touches[0].clientY - e.touches[1].clientY
      );
      const factor = currentDist / initialPinchDist;
      const nextScale = Math.min(Math.max(initialPinchScale * factor, 0.35), 2.2);
      setScale(nextScale);
    }
  };

  const handleTouchEnd = () => {
    setIsDragging(false);
    setInitialPinchDist(null);
  };

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

  const handleFocusSubject = (sid: 'all' | SubjectId) => {
    setFocusSubject(sid);
    if (sid !== 'all') {
      setExpandedSubjects((prev) => ({ ...prev, [sid]: true }));
      // Center on this branch
      setPosition({ x: 30, y: 160 });
      setScale(0.85);
    } else {
      handleResetCenter();
    }
  };

  const displayedSubjectIds: SubjectId[] = useMemo(() => {
    if (focusSubject === 'all') return ['gaoshu', 'xiandai', 'gailv'];
    return [focusSubject];
  }, [focusSubject]);

  return (
    <div className="relative w-full h-[calc(100vh-56px)] overflow-hidden font-body flex flex-col">
      {/* Top Floating Control Bar */}
      <div className="relative z-30 bg-[var(--sheet)] border-b border-[var(--line)] px-3 py-2 flex flex-wrap items-center justify-between gap-2 shadow-xs">
        {/* Left: View Mode Toggle & Subject Branch Focus */}
        <div className="flex items-center gap-1.5 flex-wrap">
          {/* View mode toggle */}
          <div className="flex items-center bg-[var(--well)] p-0.5 rounded-[8px] border border-[var(--line)] text-xs font-mono">
            <button
              onClick={() => setViewMode('canvas')}
              className={`flex items-center gap-1 px-2.5 py-1 rounded-[6px] transition-colors ${
                viewMode === 'canvas'
                  ? 'bg-[var(--sheet)] text-[var(--ink)] font-bold shadow-xs'
                  : 'text-[var(--muted)] hover:text-[var(--ink)]'
              }`}
            >
              <Network className="w-3.5 h-3.5" />
              <span>导图画布</span>
            </button>
            <button
              onClick={() => setViewMode('outline')}
              className={`flex items-center gap-1 px-2.5 py-1 rounded-[6px] transition-colors ${
                viewMode === 'outline'
                  ? 'bg-[var(--sheet)] text-[var(--ink)] font-bold shadow-xs'
                  : 'text-[var(--muted)] hover:text-[var(--ink)]'
              }`}
            >
              <LayoutGrid className="w-3.5 h-3.5" />
              <span>大纲列表</span>
            </button>
          </div>

          {/* Subject Focus Pills (Especially helpful on mobile) */}
          <div className="hidden sm:flex items-center gap-1 bg-[var(--well)] p-0.5 rounded-[8px] border border-[var(--line)] text-xs font-mono">
            <button
              onClick={() => handleFocusSubject('all')}
              className={`px-2 py-0.8 rounded-[6px] transition-colors ${
                focusSubject === 'all'
                  ? 'bg-[var(--sheet)] text-[var(--ink)] font-bold shadow-xs'
                  : 'text-[var(--muted)] hover:text-[var(--ink)]'
              }`}
            >
              全部板块
            </button>
            <button
              onClick={() => handleFocusSubject('gaoshu')}
              className={`px-2 py-0.8 rounded-[6px] transition-colors ${
                focusSubject === 'gaoshu'
                  ? 'bg-[var(--blue-bg)] text-[var(--blue)] font-bold border border-[var(--blue)]'
                  : 'text-[var(--muted)] hover:text-[var(--ink)]'
              }`}
            >
              高数 56%
            </button>
            <button
              onClick={() => handleFocusSubject('xiandai')}
              className={`px-2 py-0.8 rounded-[6px] transition-colors ${
                focusSubject === 'xiandai'
                  ? 'bg-[var(--blue-bg)] text-[var(--blue)] font-bold border border-[var(--blue)]'
                  : 'text-[var(--muted)] hover:text-[var(--ink)]'
              }`}
            >
              线代 22%
            </button>
            <button
              onClick={() => handleFocusSubject('gailv')}
              className={`px-2 py-0.8 rounded-[6px] transition-colors ${
                focusSubject === 'gailv'
                  ? 'bg-[var(--blue-bg)] text-[var(--blue)] font-bold border border-[var(--blue)]'
                  : 'text-[var(--muted)] hover:text-[var(--ink)]'
              }`}
            >
              概率 22%
            </button>
          </div>
        </div>

        {/* Right: Zoom Controls (Only in Canvas mode) */}
        {viewMode === 'canvas' && (
          <div className="flex items-center gap-1 text-xs">
            <span className="font-mono text-[var(--muted)] mr-1 text-[11px] hidden md:inline">
              [缩放: {Math.round(scale * 100)}%]
            </span>

            <button
              onClick={handleZoomIn}
              title="放大"
              className="p-1.5 hover:bg-[var(--well)] rounded-[6px] transition-colors text-[var(--muted)] hover:text-[var(--ink)] border border-[var(--line)]"
            >
              <ZoomIn className="w-3.5 h-3.5" />
            </button>

            <button
              onClick={handleZoomOut}
              title="缩小"
              className="p-1.5 hover:bg-[var(--well)] rounded-[6px] transition-colors text-[var(--muted)] hover:text-[var(--ink)] border border-[var(--line)]"
            >
              <ZoomOut className="w-3.5 h-3.5" />
            </button>

            <button
              onClick={handleResetCenter}
              title="重置居中"
              className="p-1.5 hover:bg-[var(--well)] rounded-[6px] transition-colors text-[var(--muted)] hover:text-[var(--ink)] border border-[var(--line)] flex items-center gap-1 font-mono text-[11px]"
            >
              <RotateCcw className="w-3.5 h-3.5" />
              <span className="hidden sm:inline">居中</span>
            </button>

            <div className="hidden sm:block h-3.5 w-px bg-[var(--line)] mx-1" />

            <button
              onClick={() => handleToggleAll(true)}
              className="hidden sm:inline-block px-2 py-1 bg-[var(--well)] hover:bg-[var(--line)] rounded-[6px] text-[var(--ink)] text-[11px] font-mono transition-colors"
            >
              展开全部
            </button>

            <button
              onClick={() => handleToggleAll(false)}
              className="hidden sm:inline-block px-2 py-1 bg-[var(--well)] hover:bg-[var(--line)] rounded-[6px] text-[var(--ink)] text-[11px] font-mono transition-colors"
            >
              收起全部
            </button>
          </div>
        )}
      </div>

      {/* Mobile Branch Focus Switcher Bar on small screens */}
      {viewMode === 'canvas' && (
        <div className="sm:hidden bg-[var(--well)] border-b border-[var(--line)] px-3 py-1.5 flex items-center justify-between text-xs font-mono overflow-x-auto gap-2">
          <span className="text-[var(--muted)] text-[11px] flex-shrink-0">聚焦分支:</span>
          <div className="flex items-center gap-1 flex-shrink-0">
            <button
              onClick={() => handleFocusSubject('all')}
              className={`px-2 py-0.5 rounded-[4px] text-[11px] ${
                focusSubject === 'all'
                  ? 'bg-[var(--ink)] text-[var(--paper)] font-bold'
                  : 'bg-[var(--sheet)] text-[var(--muted)]'
              }`}
            >
              全部
            </button>
            <button
              onClick={() => handleFocusSubject('gaoshu')}
              className={`px-2 py-0.5 rounded-[4px] text-[11px] ${
                focusSubject === 'gaoshu'
                  ? 'bg-[var(--blue)] text-white font-bold'
                  : 'bg-[var(--sheet)] text-[var(--muted)]'
              }`}
            >
              高数 56%
            </button>
            <button
              onClick={() => handleFocusSubject('xiandai')}
              className={`px-2 py-0.5 rounded-[4px] text-[11px] ${
                focusSubject === 'xiandai'
                  ? 'bg-[var(--blue)] text-white font-bold'
                  : 'bg-[var(--sheet)] text-[var(--muted)]'
              }`}
            >
              线代 22%
            </button>
            <button
              onClick={() => handleFocusSubject('gailv')}
              className={`px-2 py-0.5 rounded-[4px] text-[11px] ${
                focusSubject === 'gailv'
                  ? 'bg-[var(--blue)] text-white font-bold'
                  : 'bg-[var(--sheet)] text-[var(--muted)]'
              }`}
            >
              概率 22%
            </button>
          </div>
        </div>
      )}

      {/* MODE 1: Interactive Canvas Mode (with Touch Drag & Pinch-to-Zoom) */}
      {viewMode === 'canvas' && (
        <div className="flex-1 relative w-full overflow-hidden maki-grid-pattern select-none cursor-grab active:cursor-grabbing touch-canvas">
          {/* Main Graph Canvas */}
          <div
            ref={containerRef}
            onWheel={handleWheel}
            onMouseDown={handleMouseDown}
            onMouseMove={handleMouseMove}
            onMouseUp={handleMouseUp}
            onTouchStart={handleTouchStart}
            onTouchMove={handleTouchMove}
            onTouchEnd={handleTouchEnd}
            onTouchCancel={handleTouchEnd}
            className="w-full h-full relative"
          >
            <div
              className="absolute origin-top-left transition-transform duration-75 ease-out"
              style={{
                transform: `translate(${position.x}px, ${position.y}px) scale(${scale})`,
              }}
            >
              <div className="flex items-center space-x-12 sm:space-x-14">
                
                {/* Level 0: Central Node */}
                <div className="interactive-node relative z-20 flex-shrink-0">
                  <div className="relative px-5 py-4 sm:px-6 sm:py-5 rounded-[14px] bg-[var(--sheet)] border border-[var(--line)] shadow-sm text-center w-48 sm:w-56">
                    <div className="text-[10px] sm:text-[11px] font-mono text-[var(--muted)] uppercase tracking-wider mb-1">
                      Maki 考研数学一
                    </div>
                    <h1 className="text-lg sm:text-xl font-display font-bold tracking-tight text-[var(--ink)]">
                      解题思路全景导图
                    </h1>
                    <div className="mt-2.5 pt-2 border-t border-[var(--line)] text-[10px] sm:text-[11px] font-mono text-[var(--muted)]">
                      3 板块 · 26 章节 · 74 考点
                    </div>
                  </div>
                </div>

                {/* Level 1: Core Mathematical Subjects */}
                <div className="flex flex-col space-y-12">
                  {displayedSubjectIds.map((sid) => {
                    const subj = SUBJECTS[sid];
                    const isExpanded = !!expandedSubjects[sid];
                    const chapters = subj.chapterIds.map((cid) => CHAPTERS[cid]);

                    const subjectMeta = {
                      gaoshu: { code: '01', ratio: '56%', badge: '高等数学' },
                      xiandai: { code: '02', ratio: '22%', badge: '线性代数' },
                      gailv: { code: '03', ratio: '22%', badge: '概率统计' },
                    }[sid];

                    return (
                      <div key={sid} className="flex items-center space-x-10 sm:space-x-12">
                        {/* Subject Card */}
                        <div className="interactive-node relative z-10 flex-shrink-0">
                          <div className="relative w-60 sm:w-64 p-4 rounded-[14px] bg-[var(--sheet)] border border-[var(--line)] hover:border-[var(--blue)] transition-colors shadow-sm">
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
                                <div key={ch.id} className="flex items-center space-x-6 sm:space-x-8">
                                  {/* Chapter Node Card */}
                                  <div className="interactive-node relative flex-shrink-0">
                                    <div
                                      onClick={() => onSelectChapter(ch.id)}
                                      className="w-64 sm:w-72 p-3 rounded-[10px] bg-[var(--sheet)] hover:bg-[var(--well)] border border-[var(--line)] hover:border-[var(--blue)] transition-all cursor-pointer group"
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
                                            className={`interactive-node w-72 sm:w-80 p-3 rounded-[9px] border transition-all cursor-pointer ${
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
                                                <div className="text-[11px] text-[var(--muted)] mt-1 line-clamp-1 leading-relaxed">
                                                  <MathView content={t.summary} inline />
                                                </div>
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
                                                <span className="truncate"><MathView content={t.triggers[0]} inline /></span>
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
      )}

      {/* MODE 2: Mobile-First Outline List Mode (Vertical Tree View) */}
      {viewMode === 'outline' && (
        <div className="flex-1 overflow-y-auto p-4 sm:p-6 max-w-4xl mx-auto w-full space-y-4">
          <div className="bg-[var(--sheet)] border border-[var(--line)] rounded-[12px] p-4 text-xs font-mono text-[var(--muted)] flex items-center justify-between">
            <span className="text-[var(--ink)] font-bold">考研数学一三大板块大纲导航</span>
            <span>共 26 讲 · 74 个思路考点</span>
          </div>

          {(['gaoshu', 'xiandai', 'gailv'] as SubjectId[]).map((sid) => {
            const subj = SUBJECTS[sid];
            const isOpen = !!outlineOpenSubjects[sid];
            const chapters = subj.chapterIds.map((cid) => CHAPTERS[cid]);

            const subjectMeta = {
              gaoshu: { code: '01', ratio: '56%', badge: '高等数学' },
              xiandai: { code: '02', ratio: '22%', badge: '线性代数' },
              gailv: { code: '03', ratio: '22%', badge: '概率统计' },
            }[sid];

            return (
              <div
                key={sid}
                className="bg-[var(--sheet)] border border-[var(--line)] rounded-[14px] overflow-hidden shadow-xs"
              >
                {/* Subject Header */}
                <div
                  onClick={() =>
                    setOutlineOpenSubjects((prev) => ({ ...prev, [sid]: !prev[sid] }))
                  }
                  className="p-4 bg-[var(--well)] border-b border-[var(--line)] flex items-center justify-between cursor-pointer select-none"
                >
                  <div className="flex items-center gap-2.5">
                    <span className="font-mono text-xs font-bold text-[var(--muted)] bg-[var(--sheet)] px-1.5 py-0.5 rounded border border-[var(--line)]">
                      {subjectMeta.code}
                    </span>
                    <div>
                      <h2 className="text-base font-display font-bold text-[var(--ink)]">
                        {subj.name}
                      </h2>
                      <p className="text-[11px] text-[var(--muted)] font-mono">
                        {chapters.length} 讲 · 分值约 {subjectMeta.ratio}
                      </p>
                    </div>
                  </div>

                  <div className="flex items-center gap-2">
                    {isOpen ? (
                      <ChevronDown className="w-4 h-4 text-[var(--muted)]" />
                    ) : (
                      <ChevronRight className="w-4 h-4 text-[var(--muted)]" />
                    )}
                  </div>
                </div>

                {/* Chapter List inside Subject */}
                {isOpen && (
                  <div className="divide-y divide-[var(--line)]">
                    {chapters.map((ch) => {
                      const isChOpen = !!expandedChapters[ch.id];
                      const topics = ch.topicIds.map((tid) => KNOWLEDGE_BASE[tid]).filter(Boolean);

                      return (
                        <div key={ch.id} className="p-3.5 space-y-2">
                          <div className="flex items-center justify-between">
                            <div
                              onClick={() => toggleChapter(ch.id, { stopPropagation: () => {} } as any)}
                              className="flex items-center gap-2 cursor-pointer select-none"
                            >
                              <span className="text-[10px] font-mono px-1.5 py-0.2 rounded bg-[var(--well)] text-[var(--muted)] border border-[var(--line)]">
                                第 {ch.order} 讲
                              </span>
                              <h3 className="text-xs font-bold text-[var(--ink)] hover:text-[var(--blue)]">
                                {ch.title}
                              </h3>
                              <span className="text-[10px] font-mono text-[var(--muted)]">
                                ({topics.length} 考点)
                              </span>
                            </div>

                            <button
                              onClick={() => onSelectChapter(ch.id)}
                              className="flex items-center gap-1 text-[11px] font-mono text-[var(--blue)] hover:underline"
                            >
                              <span>进入章节</span>
                              <ArrowRight className="w-3 h-3" />
                            </button>
                          </div>

                          {/* Topics List under Chapter */}
                          <div className="grid grid-cols-1 sm:grid-cols-2 gap-2 pt-1 pl-2 border-l-2 border-[var(--line)]">
                            {topics.map((t) => {
                              const s = learningStatuses[t.id] || 'unlearned';

                              return (
                                <div
                                  key={t.id}
                                  onClick={() => onSelectTopic(t.id)}
                                  className="bg-[var(--well)] hover:bg-[var(--sheet)] border border-[var(--line)] hover:border-[var(--blue)] p-2.5 rounded-[8px] cursor-pointer transition-colors space-y-1"
                                >
                                  <div className="flex items-center justify-between gap-1">
                                    <span className="text-xs font-semibold text-[var(--ink)]">
                                      {t.title}
                                    </span>
                                    {s === 'mastered' ? (
                                      <span className="text-[10px] font-mono px-1 py-0.2 rounded bg-[var(--green-bg)] text-[var(--green)]">
                                        已掌握
                                      </span>
                                    ) : s === 'struggling' ? (
                                      <span className="text-[10px] font-mono px-1 py-0.2 rounded bg-[var(--amber-bg)] text-[var(--amber)]">
                                        困难
                                      </span>
                                    ) : null}
                                  </div>
                                  <p className="text-[11px] text-[var(--muted)] line-clamp-1">
                                    <MathView content={t.summary} inline />
                                  </p>
                                </div>
                              );
                            })}
                          </div>
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
};
