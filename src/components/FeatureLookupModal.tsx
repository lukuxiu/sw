import React, { useState, useMemo, useEffect } from 'react';
import { 
  X, Search, Sparkles, Filter, ExternalLink, ArrowRight, 
  RotateCcw, CheckCircle2, AlertCircle, Shuffle, BookOpen, Layers,
  ChevronDown, ChevronUp, FileText, Check, Eye, EyeOff
} from 'lucide-react';
import { ALL_FEATURES, FeatureCategory, FeatureItem, FeatureExample, searchFeatures } from '../data/featureIndex';
import { MathView } from './MathView';
import { setLearningStatus } from '../data/storage';

interface FeatureLookupModalProps {
  isOpen: boolean;
  onClose: () => void;
  onSelectTopic: (topicId: string) => void;
  onSelectMetaMethod?: (metaMethodId: string) => void;
}

const CATEGORIES: { id: FeatureCategory; label: string }[] = [
  { id: 'all', label: '全部特征' },
  { id: '极限与连续', label: '极限与连续' },
  { id: '微分与中值定理', label: '一元微分/中值' },
  { id: '积分与常微分方程', label: '一元积分/方程' },
  { id: '多元与多元微积分', label: '多元微积分/线面' },
  { id: '级数与空间几何', label: '级数与空间几何' },
  { id: '行列式与矩阵', label: '行列式与矩阵' },
  { id: '方程组与向量组', label: '线性方程与向量' },
  { id: '特征值与二次型', label: '特征值与二次型' },
  { id: '随机变量与分布', label: '随机变量与分布' },
  { id: '数理统计与参数估计', label: '数理统计与估计' },
  { id: '应试工程与备考策略', label: '应试工程/失误/保命' },
];

export const FeatureLookupModal: React.FC<FeatureLookupModalProps> = ({
  isOpen,
  onClose,
  onSelectTopic,
  onSelectMetaMethod,
}) => {
  if (!isOpen) return null;

  const [activeTab, setActiveTab] = useState<'matrix' | 'flashcard'>('matrix');
  const [searchQuery, setSearchQuery] = useState('');
  const [selectedCategory, setSelectedCategory] = useState<FeatureCategory>('all');
  const [selectedPaper, setSelectedPaper] = useState<'all' | '数一' | '数二' | '数三'>('all');
  const [selectedYearFilter, setSelectedYearFilter] = useState<'all' | 'recent' | 'classic'>('all');

  // Expanded examples on matrix cards
  const [expandedCardId, setExpandedCardId] = useState<string | null>(null);

  // Mask recall mode (背诵遮盖模式)
  const [isMaskMode, setIsMaskMode] = useState<boolean>(false);
  const [revealedFeatures, setRevealedFeatures] = useState<Record<string, boolean>>({});

  // Flashcard state
  const [currentCardIndex, setCurrentCardIndex] = useState(0);
  const [isFlipped, setIsFlipped] = useState(false);
  const [flashcardSubject, setFlashcardSubject] = useState<'all' | 'gaoshu' | 'xiandai' | 'gailv'>('all');
  const [flashcardPaper, setFlashcardPaper] = useState<'all' | '数一' | '数二' | '数三'>('all');
  const [showFlashcardExamplePrompt, setShowFlashcardExamplePrompt] = useState(false);

  const filteredFeatures = useMemo(() => {
    return searchFeatures(searchQuery, selectedCategory, selectedPaper, selectedYearFilter);
  }, [searchQuery, selectedCategory, selectedPaper, selectedYearFilter]);

  const flashcardPool = useMemo(() => {
    return ALL_FEATURES.filter((f) => {
      if (flashcardSubject !== 'all' && f.subjectId !== flashcardSubject) return false;
      if (flashcardPaper !== 'all' && !f.papers.includes(flashcardPaper)) return false;
      return true;
    });
  }, [flashcardSubject, flashcardPaper]);

  const currentFlashcard: FeatureItem | undefined = useMemo(() => {
    if (flashcardPool.length === 0) return undefined;
    return flashcardPool[currentCardIndex % flashcardPool.length];
  }, [flashcardPool, currentCardIndex]);

  const handleNextFlashcard = () => {
    setIsFlipped(false);
    setShowFlashcardExamplePrompt(false);
    setCurrentCardIndex((prev) => (prev + 1) % (flashcardPool.length || 1));
  };

  const handleRandomFlashcard = () => {
    setIsFlipped(false);
    setShowFlashcardExamplePrompt(false);
    const rand = Math.floor(Math.random() * (flashcardPool.length || 1));
    setCurrentCardIndex(rand);
  };

  const handleMarkFlashcardStatus = (status: 'struggling' | 'mastered') => {
    if (currentFlashcard) {
      setLearningStatus(currentFlashcard.topicId, status);
    }
    handleNextFlashcard();
  };

  // Keyboard navigation for active recall flashcards
  useEffect(() => {
    if (!isOpen || activeTab !== 'flashcard') return;

    const handleKeyDown = (e: KeyboardEvent) => {
      const activeTag = (document.activeElement?.tagName || '').toLowerCase();
      if (activeTag === 'input' || activeTag === 'textarea') return;

      if (e.code === 'Space' || e.key === 'Enter') {
        e.preventDefault();
        setIsFlipped((prev) => !prev);
      } else if (e.key === 'ArrowRight') {
        e.preventDefault();
        handleNextFlashcard();
      } else if (e.key === '1') {
        e.preventDefault();
        handleMarkFlashcardStatus('struggling');
      } else if (e.key === '2') {
        e.preventDefault();
        handleMarkFlashcardStatus('mastered');
      } else if (e.key.toLowerCase() === 'r') {
        e.preventDefault();
        handleRandomFlashcard();
      }
    };

    window.addEventListener('keydown', handleKeyDown);
    return () => window.removeEventListener('keydown', handleKeyDown);
  }, [isOpen, activeTab, flashcardPool.length, currentCardIndex, isFlipped, currentFlashcard]);

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center p-2 sm:p-4 bg-black/60 backdrop-blur-xs font-body">
      <div className="bg-[var(--sheet)] border border-[var(--line)] rounded-[14px] w-full max-w-5xl max-h-[92vh] sm:max-h-[88vh] flex flex-col shadow-2xl overflow-hidden">
        {/* Header */}
        <div className="px-4 sm:px-6 py-3.5 bg-[var(--well)] border-b border-[var(--line)] flex items-center justify-between">
          <div className="flex items-center gap-2.5">
            <div className="p-1.5 rounded-[6px] bg-[var(--sheet)] text-[var(--amber)] border border-[var(--line)]">
              <Sparkles className="w-4 h-4" />
            </div>
            <div>
              <div className="flex items-center gap-2">
                <h2 className="text-base font-display font-bold text-[var(--ink)] tracking-tight">
                  特征 $\to$ 思路 逆向速查与真题例题库
                </h2>
                <span className="text-[10px] font-mono px-1.5 py-0.2 rounded bg-[var(--sheet)] text-[var(--muted)] border border-[var(--line)] hidden sm:inline">
                  含 2021~2026 全部真题例题
                </span>
              </div>
              <p className="text-[11px] text-[var(--muted)] font-mono">
                从做题特征切入突破口，配套历年真题实战例题与主动回忆抽查
              </p>
            </div>
          </div>

          {/* Mode Switch Tabs */}
          <div className="flex items-center gap-2">
            <div className="bg-[var(--well)] p-0.5 rounded-[8px] border border-[var(--line)] flex items-center text-xs font-mono">
              <button
                onClick={() => setActiveTab('matrix')}
                className={`flex items-center gap-1 px-2.5 py-1 rounded-[6px] transition-colors cursor-pointer ${
                  activeTab === 'matrix'
                    ? 'bg-[var(--ink)] text-[var(--paper)] font-bold shadow-xs'
                    : 'text-[var(--muted)] hover:text-[var(--ink)]'
                }`}
              >
                <Layers className="w-3.5 h-3.5" />
                <span>特征与例题表</span>
              </button>
              <button
                onClick={() => {
                  setActiveTab('flashcard');
                  setIsFlipped(false);
                }}
                className={`flex items-center gap-1 px-2.5 py-1 rounded-[6px] transition-colors cursor-pointer ${
                  activeTab === 'flashcard'
                    ? 'bg-[var(--ink)] text-[var(--paper)] font-bold shadow-xs'
                    : 'text-[var(--muted)] hover:text-[var(--ink)]'
                }`}
              >
                <Shuffle className="w-3.5 h-3.5" />
                <span>特征闪卡抽查</span>
              </button>
            </div>

            <button
              onClick={onClose}
              className="p-1.5 rounded-[6px] text-[var(--muted)] hover:text-[var(--ink)] hover:bg-[var(--line)] transition-colors cursor-pointer"
            >
              <X className="w-4 h-4" />
            </button>
          </div>
        </div>

        {/* TAB 1: FEATURE MATRIX LIST */}
        {activeTab === 'matrix' && (
          <div className="flex-1 flex flex-col overflow-hidden">
            {/* Filter & Search Bar */}
            <div className="px-4 sm:px-6 py-2.5 bg-[var(--sheet)] border-b border-[var(--line)] space-y-2">
              <div className="flex items-center gap-2">
                <div className="relative flex-1">
                  <Search className="w-3.5 h-3.5 absolute left-3 top-2.5 text-[var(--muted)]" />
                  <input
                    type="text"
                    placeholder="输入题目中看到的特征（如：0/0型、路径无关、A^2=A、卡方分布、对称区间、2025、数二）..."
                    value={searchQuery}
                    onChange={(e) => setSearchQuery(e.target.value)}
                    className="w-full bg-[var(--well)] border border-transparent focus:border-[var(--line)] rounded-[8px] pl-9 pr-8 py-1.5 text-xs text-[var(--ink)] placeholder-[var(--muted)] focus:outline-none"
                  />
                  {searchQuery && (
                    <button
                      onClick={() => setSearchQuery('')}
                      className="absolute right-2.5 top-2 text-[var(--muted)] hover:text-[var(--ink)] cursor-pointer"
                    >
                      <X className="w-3.5 h-3.5" />
                    </button>
                  )}
                </div>
                <span className="text-xs font-mono text-[var(--muted)] flex-shrink-0">
                  匹配到 {filteredFeatures.length} 条特征
                </span>
              </div>

              {/* Sub-Filters: Paper & Year Filter Pills */}
              <div className="flex flex-wrap items-center justify-between gap-2 pt-1 border-t border-[var(--line)] text-[11px] font-mono">
                <div className="flex items-center gap-1">
                  <span className="text-[var(--muted)] mr-1">卷别:</span>
                  {(['all', '数一', '数二', '数三'] as const).map((p) => (
                    <button
                      key={p}
                      onClick={() => setSelectedPaper(p)}
                      className={`px-2 py-0.5 rounded-[5px] transition-colors cursor-pointer ${
                        selectedPaper === p
                          ? 'bg-[var(--ink)] text-[var(--paper)] font-bold'
                          : 'bg-[var(--well)] text-[var(--muted)] hover:text-[var(--ink)]'
                      }`}
                    >
                      {p === 'all' ? '全部卷别' : p}
                    </button>
                  ))}
                </div>

                <div className="flex items-center gap-2">
                  <button
                    onClick={() => {
                      setIsMaskMode(!isMaskMode);
                      setRevealedFeatures({});
                    }}
                    className={`flex items-center gap-1.5 px-2 py-0.5 rounded-[5px] transition-colors cursor-pointer text-[11px] font-mono ${
                      isMaskMode
                        ? 'bg-[var(--purple)] text-white font-bold shadow-xs'
                        : 'bg-[var(--well)] text-[var(--muted)] hover:text-[var(--ink)] border border-[var(--line)]'
                    }`}
                    title="遮盖第一反应与方法，主动回忆后再点击掀开"
                  >
                    {isMaskMode ? <EyeOff className="w-3 h-3" /> : <Eye className="w-3 h-3" />}
                    <span>{isMaskMode ? '遮盖自测中' : '开启背诵遮盖模式'}</span>
                  </button>
                  {isMaskMode && (
                    <button
                      onClick={() => {
                        const allRev = Object.keys(revealedFeatures).length === filteredFeatures.length;
                        if (allRev) {
                          setRevealedFeatures({});
                        } else {
                          const all: Record<string, boolean> = {};
                          filteredFeatures.forEach((f) => { all[f.id] = true; });
                          setRevealedFeatures(all);
                        }
                      }}
                      className="text-[10px] font-mono text-[var(--blue)] hover:underline cursor-pointer"
                    >
                      {Object.keys(revealedFeatures).length === filteredFeatures.length ? '全部遮盖' : '一键掀开全部'}
                    </button>
                  )}
                </div>

                <div className="flex items-center gap-1">
                  <span className="text-[var(--muted)] mr-1">年份:</span>
                  {[
                    { id: 'all', label: '全部年份' },
                    { id: 'recent', label: '2021~2026 近年真题' },
                    { id: 'classic', label: '往年经典' },
                  ].map((yf) => (
                    <button
                      key={yf.id}
                      onClick={() => setSelectedYearFilter(yf.id as any)}
                      className={`px-2 py-0.5 rounded-[5px] transition-colors cursor-pointer ${
                        selectedYearFilter === yf.id
                          ? 'bg-[var(--blue-bg)] text-[var(--blue)] font-bold border border-[var(--blue)]'
                          : 'bg-[var(--well)] text-[var(--muted)] hover:text-[var(--ink)]'
                      }`}
                    >
                      {yf.label}
                    </button>
                  ))}
                </div>
              </div>

              {/* Category Pills */}
              <div className="flex items-center gap-1 overflow-x-auto no-scrollbar py-0.5 text-[11px] font-mono">
                {CATEGORIES.map((c) => (
                  <button
                    key={c.id}
                    onClick={() => setSelectedCategory(c.id)}
                    className={`px-2 py-0.8 rounded-[6px] flex-shrink-0 transition-colors cursor-pointer ${
                      selectedCategory === c.id
                        ? 'bg-[var(--blue-bg)] text-[var(--blue)] font-bold border border-[var(--blue)]'
                        : 'bg-[var(--well)] text-[var(--muted)] hover:text-[var(--ink)]'
                    }`}
                  >
                    {c.label}
                  </button>
                ))}
              </div>
            </div>

            {/* Matrix Items Scroll List */}
            <div className="flex-1 overflow-y-auto p-3 sm:p-6 space-y-3">
              {filteredFeatures.length === 0 ? (
                <div className="text-center py-12 text-xs font-mono text-[var(--muted)]">
                  未找到与 “{searchQuery}” 匹配的解题特征，请尝试调整筛选或关键词
                </div>
              ) : (
                filteredFeatures.map((item) => {
                  const isExpanded = expandedCardId === item.id;

                  return (
                    <div
                      key={item.id}
                      className="bg-[var(--well)] border border-[var(--line)] hover:border-[var(--blue)] rounded-[12px] p-3.5 sm:p-4 space-y-2.5 transition-colors group"
                    >
                      <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-2 pb-2 border-b border-[var(--line)]">
                        <div className="flex items-center gap-2 flex-wrap">
                          <span className="text-[10px] font-mono px-1.5 py-0.5 rounded bg-[var(--sheet)] text-[var(--muted)] border border-[var(--line)]">
                            {item.subjectName} · {item.chapterTitle}
                          </span>
                          <span className="text-xs font-bold text-[var(--ink)] font-display">
                            {item.topicTitle}
                          </span>
                          <div className="flex items-center gap-1">
                            {item.papers.map((p) => (
                              <span key={p} className="text-[9px] font-mono px-1 py-0.2 rounded bg-[var(--sheet)] text-[var(--blue)] border border-[var(--line)]">
                                {p}
                              </span>
                            ))}
                            {item.metaMethodName && (
                              <button
                                type="button"
                                onClick={(e) => {
                                  e.stopPropagation();
                                  if (onSelectMetaMethod && item.metaMethodId) {
                                    onSelectMetaMethod(item.metaMethodId);
                                  }
                                }}
                                className="text-[9px] font-mono px-1.5 py-0.2 rounded bg-[var(--purple-bg)]/30 text-[var(--purple)] border border-[var(--purple)]/40 font-bold flex items-center gap-0.5 hover:bg-[var(--purple)] hover:text-white transition-colors cursor-pointer"
                                title="点击查看该通用方法的跨章节演化矩阵与实战例题"
                              >
                                <Layers className="w-2.5 h-2.5" />
                                <span>通用方法: {item.metaMethodName}</span>
                              </button>
                            )}
                          </div>
                        </div>

                        <div className="flex items-center gap-2 self-end sm:self-auto">
                          {item.examples.length > 0 && (
                            <button
                              onClick={() => setExpandedCardId(isExpanded ? null : item.id)}
                              className="flex items-center gap-1 text-[11px] font-mono px-2 py-0.5 rounded bg-[var(--sheet)] hover:bg-[var(--line)] text-[var(--ink)] border border-[var(--line)] transition-colors cursor-pointer"
                            >
                              <BookOpen className="w-3 h-3 text-[var(--amber)]" />
                              <span>{isExpanded ? '收起例题' : `配套真题例题 (${item.examples.length})`}</span>
                              {isExpanded ? <ChevronUp className="w-3 h-3" /> : <ChevronDown className="w-3 h-3" />}
                            </button>
                          )}

                          <button
                            onClick={() => {
                              onSelectTopic(item.topicId);
                              onClose();
                            }}
                            className="flex items-center gap-1 text-xs font-mono text-[var(--blue)] hover:underline cursor-pointer"
                          >
                            <span>完整考点推导</span>
                            <ArrowRight className="w-3 h-3" />
                          </button>
                        </div>
                      </div>

                      <div className="grid grid-cols-1 md:grid-cols-3 gap-2.5 text-xs">
                        {/* Trigger feature */}
                        <div className="bg-[var(--sheet)] p-2.5 rounded-[8px] border border-[var(--line)]">
                          <div className="font-mono text-[10px] text-[var(--amber)] font-bold mb-1">
                            [看到题目特征]
                          </div>
                          <div className="text-[var(--ink)] font-medium leading-relaxed font-body">
                            <MathView content={item.trigger} inline />
                          </div>
                        </div>

                        {/* First reaction & Primary method with Mask Mode support */}
                        {isMaskMode && !revealedFeatures[item.id] ? (
                          <div 
                            onClick={() => setRevealedFeatures(prev => ({ ...prev, [item.id]: true }))}
                            className="md:col-span-2 bg-[var(--sheet)] p-4 rounded-[8px] border border-dashed border-[var(--purple)]/50 hover:bg-[var(--purple-bg)]/10 flex flex-col items-center justify-center gap-1.5 text-center cursor-pointer transition-colors group/mask"
                          >
                            <div className="w-7 h-7 rounded-full bg-[var(--purple-bg)]/30 text-[var(--purple)] flex items-center justify-center group-hover/mask:scale-110 transition-transform">
                              <Eye className="w-4 h-4" />
                            </div>
                            <span className="text-xs font-mono font-bold text-[var(--purple)]">
                              点击掀开第一反应与解法
                            </span>
                            <span className="text-[10px] font-mono text-[var(--muted)]">
                              先在脑海中回忆“看到该特征应想到什么”，再点击翻面核对
                            </span>
                          </div>
                        ) : (
                          <>
                            <div className="bg-[var(--sheet)] p-2.5 rounded-[8px] border border-[var(--line)]">
                              <div className="font-mono text-[10px] text-[var(--blue)] font-bold mb-1 flex items-center justify-between">
                                <span>[应该想到什么 · 第一反应]</span>
                                {isMaskMode && (
                                  <span className="text-[9px] text-[var(--green)]">已揭晓</span>
                                )}
                              </div>
                              <div className="text-[var(--ink)] leading-relaxed font-body">
                                <MathView content={item.firstReaction} inline />
                              </div>
                            </div>

                            <div className="bg-[var(--sheet)] p-2.5 rounded-[8px] border border-[var(--line)]">
                              <div className="font-mono text-[10px] text-[var(--green)] font-bold mb-1">
                                [首选方法与理由]
                              </div>
                              <div className="text-[var(--ink)] font-semibold font-display">
                                {item.primaryMethod}
                              </div>
                              <p className="text-[11px] text-[var(--muted)] mt-1 font-body">
                                {item.whyChoose}
                              </p>
                            </div>
                          </>
                        )}
                      </div>

                      {/* Expandable Authentic Examples Section */}
                      {isExpanded && item.examples.length > 0 && (
                        <div className="mt-2 pt-2 border-t border-[var(--line)] space-y-2.5 animate-fadeIn">
                          <div className="flex items-center justify-between text-xs font-mono text-[var(--muted)]">
                            <span className="font-bold text-[var(--ink)]">
                              ★ 真实考卷配套例题演练（含 2021~2026 最新真题）
                            </span>
                            <span>共 {item.examples.length} 道精选真题</span>
                          </div>

                          <div className="grid grid-cols-1 gap-2.5">
                            {item.examples.map((ex) => (
                              <div
                                key={ex.id}
                                className="bg-[var(--sheet)] p-3 rounded-[8px] border border-[var(--line)] space-y-2 text-xs"
                              >
                                <div className="flex items-center justify-between font-mono text-[11px]">
                                  <div className="flex items-center gap-1.5">
                                    <span className="px-1.5 py-0.5 rounded bg-[var(--well)] text-[var(--ink)] font-bold border border-[var(--line)]">
                                      {ex.year} · {ex.category} · {ex.questionNumber}
                                    </span>
                                    <span className="text-[var(--amber)]">{ex.difficulty}</span>
                                  </div>
                                  <span className="text-[var(--muted)] text-[10px]">{ex.source}</span>
                                </div>

                                <div className="text-[var(--ink)] font-serif leading-relaxed bg-[var(--well)] p-2.5 rounded-[6px]">
                                  <MathView content={ex.prompt} />
                                  {ex.options && ex.options.length > 0 && (
                                    <div className="grid grid-cols-1 sm:grid-cols-2 gap-2 mt-2 pt-2 border-t border-[var(--line)] font-mono text-[11px]">
                                      {ex.options.map((opt, oi) => {
                                        const optLabel = String.fromCharCode(65 + oi);
                                        const cleanOpt = opt.replace(new RegExp(`^\\s*\\(?${optLabel}\\)?[-.、\\s]*`, 'i'), '').trim();
                                        return (
                                          <div key={oi} className="flex items-start gap-1.5 p-1.5 rounded bg-[var(--sheet)] border border-[var(--line)]">
                                            <span className="w-4 h-4 rounded bg-[var(--well)] text-[var(--blue)] font-bold text-[10px] flex items-center justify-center flex-shrink-0 border border-[var(--line)]">
                                              {optLabel}
                                            </span>
                                            <div className="flex-1 font-serif text-[var(--ink)]">
                                              <MathView content={cleanOpt} inline />
                                            </div>
                                          </div>
                                        );
                                      })}
                                    </div>
                                  )}
                                </div>

                                <div className="grid grid-cols-1 sm:grid-cols-2 gap-2 text-[11px] font-mono">
                                  <div className="p-2 rounded bg-[var(--blue-bg)] text-[var(--blue)] border border-[var(--blue)]">
                                    <span className="font-bold">[特征突破口]: </span>
                                    <span><MathView content={ex.keyReaction} inline /></span>
                                  </div>
                                  <div className="p-2 rounded bg-[var(--green-bg)] text-[var(--green)] border border-[var(--green)]">
                                    <span className="font-bold">[参考答案]: </span>
                                    <span><MathView content={ex.answer} inline /></span>
                                  </div>
                                </div>
                              </div>
                            ))}
                          </div>
                        </div>
                      )}
                    </div>
                  );
                })
              )}
            </div>
          </div>
        )}

        {/* TAB 2: FLASHCARD ACTIVE RECALL MODE */}
        {activeTab === 'flashcard' && (
          <div className="flex-1 flex flex-col p-4 sm:p-6 overflow-y-auto">
            {/* Subject filter & counter */}
            <div className="flex flex-wrap items-center justify-between gap-2 pb-3 border-b border-[var(--line)] font-mono text-xs">
              <div className="flex items-center gap-2">
                {/* Subject filter */}
                <div className="flex items-center gap-1 bg-[var(--well)] p-0.5 rounded-[8px] border border-[var(--line)] text-[11px]">
                  <button
                    onClick={() => {
                      setFlashcardSubject('all');
                      setIsFlipped(false);
                    }}
                    className={`px-2 py-0.8 rounded-[6px] cursor-pointer ${
                      flashcardSubject === 'all' ? 'bg-[var(--sheet)] font-bold text-[var(--ink)]' : 'text-[var(--muted)]'
                    }`}
                  >
                    全部 ({ALL_FEATURES.length})
                  </button>
                  <button
                    onClick={() => {
                      setFlashcardSubject('gaoshu');
                      setIsFlipped(false);
                    }}
                    className={`px-2 py-0.8 rounded-[6px] cursor-pointer ${
                      flashcardSubject === 'gaoshu' ? 'bg-[var(--sheet)] font-bold text-[var(--blue)]' : 'text-[var(--muted)]'
                    }`}
                  >
                    高数
                  </button>
                  <button
                    onClick={() => {
                      setFlashcardSubject('xiandai');
                      setIsFlipped(false);
                    }}
                    className={`px-2 py-0.8 rounded-[6px] cursor-pointer ${
                      flashcardSubject === 'xiandai' ? 'bg-[var(--sheet)] font-bold text-[var(--blue)]' : 'text-[var(--muted)]'
                    }`}
                  >
                    线代
                  </button>
                  <button
                    onClick={() => {
                      setFlashcardSubject('gailv');
                      setIsFlipped(false);
                    }}
                    className={`px-2 py-0.8 rounded-[6px] cursor-pointer ${
                      flashcardSubject === 'gailv' ? 'bg-[var(--sheet)] font-bold text-[var(--blue)]' : 'text-[var(--muted)]'
                    }`}
                  >
                    概率
                  </button>
                </div>

                {/* Paper filter */}
                <div className="flex items-center gap-1 bg-[var(--well)] p-0.5 rounded-[8px] border border-[var(--line)] text-[11px]">
                  {(['all', '数一', '数二', '数三'] as const).map((p) => (
                    <button
                      key={p}
                      onClick={() => {
                        setFlashcardPaper(p);
                        setIsFlipped(false);
                      }}
                      className={`px-1.5 py-0.8 rounded-[5px] cursor-pointer ${
                        flashcardPaper === p ? 'bg-[var(--sheet)] font-bold text-[var(--ink)]' : 'text-[var(--muted)]'
                      }`}
                    >
                      {p === 'all' ? '全部卷' : p}
                    </button>
                  ))}
                </div>
              </div>

              <div className="flex items-center gap-2">
                <span className="text-[var(--muted)]">
                  卡片 {currentCardIndex + 1} / {flashcardPool.length}
                </span>
                <button
                  onClick={handleRandomFlashcard}
                  className="flex items-center gap-1 px-2.5 py-1 rounded-[6px] bg-[var(--well)] hover:bg-[var(--sheet)] border border-[var(--line)] text-[var(--ink)] cursor-pointer"
                  title="随机抽取 [快捷键 R]"
                >
                  <Shuffle className="w-3 h-3 text-[var(--muted)]" />
                  <span>随机换题 [R]</span>
                </button>
              </div>
            </div>

            {/* Flashcard Area */}
            {currentFlashcard && (
              <div className="flex-1 flex flex-col items-center justify-center py-6 max-w-2xl mx-auto w-full">
                <div
                  className="w-full bg-[var(--well)] border border-[var(--line)] rounded-[16px] p-6 sm:p-8 space-y-6 shadow-md transition-all relative overflow-hidden"
                >
                  {/* Subject and Chapter banner */}
                  <div className="flex items-center justify-between text-xs font-mono text-[var(--muted)]">
                    <span className="px-2 py-0.5 rounded-[4px] bg-[var(--sheet)] border border-[var(--line)]">
                      {currentFlashcard.subjectName} · {currentFlashcard.chapterTitle}
                    </span>
                    <div className="flex items-center gap-1">
                      {currentFlashcard.papers.map((p) => (
                        <span key={p} className="text-[10px] px-1 py-0.2 rounded bg-[var(--sheet)] text-[var(--blue)] border border-[var(--line)]">
                          {p}
                        </span>
                      ))}
                    </div>
                  </div>

                  {/* Card Front: Trigger Signal Prompt */}
                  <div className="space-y-3 py-2 text-center">
                    <div className="text-xs font-mono font-bold text-[var(--amber)] uppercase tracking-wider">
                      [ 看到题目特征 ]
                    </div>
                    <div className="text-base sm:text-xl font-display font-bold text-[var(--ink)] leading-relaxed bg-[var(--sheet)] p-4 sm:p-5 rounded-[12px] border border-[var(--line)] shadow-inner">
                      <MathView content={currentFlashcard.trigger} />
                    </div>

                    {/* Optional Real Question In Front */}
                    {currentFlashcard.examples.length > 0 && (
                      <div className="pt-1">
                        <button
                          onClick={() => setShowFlashcardExamplePrompt((prev) => !prev)}
                          className="text-[11px] font-mono text-[var(--muted)] hover:text-[var(--ink)] flex items-center justify-center gap-1 mx-auto cursor-pointer"
                        >
                          <BookOpen className="w-3 h-3 text-[var(--amber)]" />
                          <span>{showFlashcardExamplePrompt ? '收起真题出题情境' : `查看在 ${currentFlashcard.examples[0].year} ${currentFlashcard.examples[0].category} 中的真实出题情境`}</span>
                          {showFlashcardExamplePrompt ? <ChevronUp className="w-3 h-3" /> : <ChevronDown className="w-3 h-3" />}
                        </button>

                        {showFlashcardExamplePrompt && (
                          <div className="mt-2 text-left bg-[var(--sheet)] p-3 rounded-[8px] border border-[var(--line)] font-serif text-xs text-[var(--ink)] animate-fadeIn">
                            <div className="font-mono text-[10px] text-[var(--muted)] mb-1">
                              真题背景：{currentFlashcard.examples[0].year} · {currentFlashcard.examples[0].category} · {currentFlashcard.examples[0].questionNumber}
                            </div>
                            <MathView content={currentFlashcard.examples[0].prompt} />
                          </div>
                        )}
                      </div>
                    )}

                    <p className="text-xs text-[var(--muted)] font-mono">
                      先在脑海中回忆：1. 第一反应检查什么？ 2. 首选方法是什么？ 3. 常见陷阱在哪？
                    </p>
                  </div>

                  {/* Flip Action Button */}
                  {!isFlipped ? (
                    <div className="pt-2 flex flex-col items-center gap-1.5">
                      <button
                        onClick={() => setIsFlipped(true)}
                        className="px-6 py-2.5 rounded-[8px] bg-[var(--ink)] text-[var(--paper)] font-bold text-xs sm:text-sm shadow-sm hover:opacity-90 transition-all flex items-center gap-2 cursor-pointer"
                      >
                        <RotateCcw className="w-4 h-4" />
                        <span>翻面揭晓：核对第一反应与首选方法</span>
                      </button>
                      <span className="text-[10px] text-[var(--muted)] font-mono hidden sm:inline">
                        按 <kbd className="px-1 py-0.5 rounded bg-[var(--sheet)] border border-[var(--line)]">空格</kbd> 或 <kbd className="px-1 py-0.5 rounded bg-[var(--sheet)] border border-[var(--line)]">Enter</kbd> 快速翻面
                      </span>
                    </div>
                  ) : (
                    /* Card Back: Answer and Methods Revealed */
                    <div className="space-y-4 pt-2 border-t border-[var(--line)] animate-fadeIn">
                      <div className="grid grid-cols-1 sm:grid-cols-2 gap-3 text-xs">
                        <div className="bg-[var(--sheet)] p-3 rounded-[8px] border border-[var(--line)]">
                          <span className="font-mono text-[10px] text-[var(--blue)] font-bold">
                            [应该想到什么 · 第一反应]
                          </span>
                          <div className="text-[var(--ink)] mt-1 leading-relaxed font-body">
                            <MathView content={currentFlashcard.firstReaction} inline />
                          </div>
                        </div>

                        <div className="bg-[var(--sheet)] p-3 rounded-[8px] border border-[var(--line)]">
                          <span className="font-mono text-[10px] text-[var(--green)] font-bold">
                            [首选方法与考点归属]
                          </span>
                          <div className="text-xs font-bold font-display text-[var(--ink)] mt-1">
                            {currentFlashcard.primaryMethod}
                          </div>
                          <p className="text-[11px] text-[var(--muted)] mt-0.5">
                            {currentFlashcard.whyChoose}
                          </p>
                          <div className="mt-2 pt-2 border-t border-[var(--line)] flex items-center justify-between text-[11px] font-mono">
                            <span className="text-[var(--muted)]">考点：{currentFlashcard.topicTitle}</span>
                            <button
                              onClick={() => {
                                onSelectTopic(currentFlashcard.topicId);
                                onClose();
                              }}
                              className="text-[var(--blue)] hover:underline flex items-center gap-0.5 cursor-pointer"
                            >
                              <span>去推导</span>
                              <ExternalLink className="w-3 h-3" />
                            </button>
                          </div>
                          {currentFlashcard.metaMethodId && currentFlashcard.metaMethodName && (
                            <div className="mt-1.5 pt-1.5 border-t border-dashed border-[var(--line)]">
                              <button
                                type="button"
                                onClick={() => {
                                  if (onSelectMetaMethod) {
                                    onSelectMetaMethod(currentFlashcard.metaMethodId!);
                                  }
                                }}
                                className="text-[11px] font-mono text-[var(--purple)] hover:underline flex items-center gap-1 cursor-pointer"
                              >
                                <Layers className="w-3 h-3 text-[var(--purple)]" />
                                <span>跨章节通用方法：{currentFlashcard.metaMethodName} ↗</span>
                              </button>
                            </div>
                          )}
                        </div>
                      </div>

                      {/* Example Result Highlight on Back */}
                      {currentFlashcard.examples.length > 0 && (
                        <div className="bg-[var(--sheet)] p-3 rounded-[8px] border border-[var(--line)] text-xs font-mono">
                          <div className="flex items-center justify-between text-[11px] text-[var(--amber)] font-bold mb-1">
                            <span>★ 配套真题例题答案核对：</span>
                            <span>{currentFlashcard.examples[0].year} · {currentFlashcard.examples[0].category} {currentFlashcard.examples[0].questionNumber}</span>
                          </div>
                          <div className="text-[var(--ink)] bg-[var(--well)] p-2 rounded text-[11px]">
                            {currentFlashcard.examples[0].answer}
                          </div>
                        </div>
                      )}

                      {/* Feedback buttons */}
                      <div className="pt-2 flex flex-col sm:flex-row items-center justify-between gap-2 font-mono text-xs">
                        <span className="text-[var(--muted)] text-[11px]">标记本次回忆状态：</span>
                        <div className="flex items-center gap-2 w-full sm:w-auto">
                          <button
                            onClick={() => handleMarkFlashcardStatus('struggling')}
                            className="flex-1 sm:flex-initial flex items-center justify-center gap-1 px-3 py-1.5 rounded-[6px] bg-[var(--amber-bg)] text-[var(--amber)] border border-[var(--amber)] font-bold hover:opacity-90 transition-opacity cursor-pointer text-xs"
                            title="按键盘 1 快捷标记"
                          >
                            <AlertCircle className="w-3.5 h-3.5" />
                            <span>卡壳了 [1]</span>
                          </button>
                          <button
                            onClick={() => handleMarkFlashcardStatus('mastered')}
                            className="flex-1 sm:flex-initial flex items-center justify-center gap-1 px-3 py-1.5 rounded-[6px] bg-[var(--green-bg)] text-[var(--green)] border border-[var(--green)] font-bold hover:opacity-90 transition-opacity cursor-pointer text-xs"
                            title="按键盘 2 快捷标记"
                          >
                            <CheckCircle2 className="w-3.5 h-3.5" />
                            <span>完全答对 [2]</span>
                          </button>
                          <button
                            onClick={handleNextFlashcard}
                            className="flex-1 sm:flex-initial px-3 py-1.5 rounded-[6px] bg-[var(--sheet)] text-[var(--ink)] border border-[var(--line)] hover:bg-[var(--well)] transition-colors cursor-pointer text-xs"
                            title="按键盘 → 快捷下一张"
                          >
                            下一张 [→]
                          </button>
                        </div>
                      </div>
                    </div>
                  )}
                </div>
              </div>
            )}
          </div>
        )}
      </div>
    </div>
  );
};
