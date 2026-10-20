import React, { useState, useMemo, useEffect } from 'react';
import { 
  X, Search, Sparkles, Filter, ExternalLink, ArrowRight, 
  RotateCcw, CheckCircle2, AlertCircle, Shuffle, BookOpen, Layers
} from 'lucide-react';
import { ALL_FEATURES, FeatureCategory, FeatureItem, searchFeatures } from '../data/featureIndex';
import { MathView } from './MathView';
import { setLearningStatus } from '../data/storage';

interface FeatureLookupModalProps {
  isOpen: boolean;
  onClose: () => void;
  onSelectTopic: (topicId: string) => void;
}

const CATEGORIES: { id: FeatureCategory; label: string }[] = [
  { id: 'all', label: '全部特征' },
  { id: '极限与连续', label: '极限与连续' },
  { id: '微分与中值定理', label: '一元微分/中值' },
  { id: '积分与常微分方程', label: '一元积分/方程' },
  { id: '多元与多元微积分', label: '多元微积分/线面积分' },
  { id: '级数与空间几何', label: '级数与空间几何' },
  { id: '行列式与矩阵', label: '行列式与矩阵' },
  { id: '方程组与向量组', label: '线性方程与向量' },
  { id: '特征值与二次型', label: '特征值与二次型' },
  { id: '随机变量与分布', label: '随机变量与分布' },
  { id: '数理统计与参数估计', label: '数理统计与估计' },
];

export const FeatureLookupModal: React.FC<FeatureLookupModalProps> = ({
  isOpen,
  onClose,
  onSelectTopic,
}) => {
  if (!isOpen) return null;

  const [activeTab, setActiveTab] = useState<'matrix' | 'flashcard'>('matrix');
  const [searchQuery, setSearchQuery] = useState('');
  const [selectedCategory, setSelectedCategory] = useState<FeatureCategory>('all');

  // Flashcard state
  const [currentCardIndex, setCurrentCardIndex] = useState(0);
  const [isFlipped, setIsFlipped] = useState(false);
  const [flashcardSubject, setFlashcardSubject] = useState<'all' | 'gaoshu' | 'xiandai' | 'gailv'>('all');

  const filteredFeatures = useMemo(() => {
    return searchFeatures(searchQuery, selectedCategory);
  }, [searchQuery, selectedCategory]);

  const flashcardPool = useMemo(() => {
    if (flashcardSubject === 'all') return ALL_FEATURES;
    return ALL_FEATURES.filter((f) => f.subjectId === flashcardSubject);
  }, [flashcardSubject]);

  const currentFlashcard: FeatureItem | undefined = useMemo(() => {
    if (flashcardPool.length === 0) return undefined;
    return flashcardPool[currentCardIndex % flashcardPool.length];
  }, [flashcardPool, currentCardIndex]);

  const handleNextFlashcard = () => {
    setIsFlipped(false);
    setCurrentCardIndex((prev) => (prev + 1) % flashcardPool.length);
  };

  const handleRandomFlashcard = () => {
    setIsFlipped(false);
    const rand = Math.floor(Math.random() * flashcardPool.length);
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
      <div className="bg-[var(--sheet)] border border-[var(--line)] rounded-[14px] w-full max-w-4xl max-h-[92vh] sm:max-h-[88vh] flex flex-col shadow-2xl overflow-hidden">
        {/* Header */}
        <div className="px-4 sm:px-6 py-3.5 bg-[var(--well)] border-b border-[var(--line)] flex items-center justify-between">
          <div className="flex items-center gap-2.5">
            <div className="p-1.5 rounded-[6px] bg-[var(--sheet)] text-[var(--amber)] border border-[var(--line)]">
              <Sparkles className="w-4 h-4" />
            </div>
            <div>
              <div className="flex items-center gap-2">
                <h2 className="text-base font-display font-bold text-[var(--ink)] tracking-tight">
                  特征 $\to$ 思路 逆向速查与刷题
                </h2>
                <span className="text-[10px] font-mono px-1.5 py-0.2 rounded bg-[var(--sheet)] text-[var(--muted)] border border-[var(--line)] hidden sm:inline">
                  看到什么 · 想到什么
                </span>
              </div>
              <p className="text-[11px] text-[var(--muted)] font-mono">
                从做题特征切入突破口，告别先翻目录再做题的被动模式
              </p>
            </div>
          </div>

          <div className="flex items-center gap-2">
            {/* Tab switch */}
            <div className="flex items-center bg-[var(--sheet)] p-0.5 rounded-[8px] border border-[var(--line)] text-xs font-mono">
              <button
                onClick={() => setActiveTab('matrix')}
                className={`flex items-center gap-1 px-2.5 py-1 rounded-[6px] transition-colors ${
                  activeTab === 'matrix'
                    ? 'bg-[var(--ink)] text-[var(--paper)] font-bold shadow-xs'
                    : 'text-[var(--muted)] hover:text-[var(--ink)]'
                }`}
              >
                <Layers className="w-3.5 h-3.5" />
                <span>特征速查表</span>
              </button>
              <button
                onClick={() => {
                  setActiveTab('flashcard');
                  setIsFlipped(false);
                }}
                className={`flex items-center gap-1 px-2.5 py-1 rounded-[6px] transition-colors ${
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
              className="p-1.5 rounded-[6px] text-[var(--muted)] hover:text-[var(--ink)] hover:bg-[var(--line)] transition-colors"
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
                    placeholder="输入题目中看到的特征（如：0/0型、路径无关、A^2=A、卡方分布、对称区间）..."
                    value={searchQuery}
                    onChange={(e) => setSearchQuery(e.target.value)}
                    className="w-full bg-[var(--well)] border border-transparent focus:border-[var(--line)] rounded-[8px] pl-9 pr-8 py-1.5 text-xs text-[var(--ink)] placeholder-[var(--muted)] focus:outline-none"
                  />
                  {searchQuery && (
                    <button
                      onClick={() => setSearchQuery('')}
                      className="absolute right-2.5 top-2 text-[var(--muted)] hover:text-[var(--ink)]"
                    >
                      <X className="w-3.5 h-3.5" />
                    </button>
                  )}
                </div>
                <span className="text-xs font-mono text-[var(--muted)] flex-shrink-0">
                  匹配到 {filteredFeatures.length} 条特征
                </span>
              </div>

              {/* Category Pills */}
              <div className="flex items-center gap-1 overflow-x-auto no-scrollbar py-0.5 text-[11px] font-mono">
                {CATEGORIES.map((c) => (
                  <button
                    key={c.id}
                    onClick={() => setSelectedCategory(c.id)}
                    className={`px-2 py-0.8 rounded-[6px] flex-shrink-0 transition-colors ${
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
                  未找到与 “{searchQuery}” 匹配的解题特征，请尝试更简练的关键词
                </div>
              ) : (
                filteredFeatures.map((item) => (
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
                      </div>

                      <button
                        onClick={() => {
                          onSelectTopic(item.topicId);
                          onClose();
                        }}
                        className="flex items-center gap-1 text-xs font-mono text-[var(--blue)] hover:underline self-end sm:self-auto"
                      >
                        <span>进入完整推导与例题</span>
                        <ArrowRight className="w-3 h-3" />
                      </button>
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

                      {/* First reaction */}
                      <div className="bg-[var(--sheet)] p-2.5 rounded-[8px] border border-[var(--line)]">
                        <div className="font-mono text-[10px] text-[var(--blue)] font-bold mb-1">
                          [应该想到什么 · 第一反应]
                        </div>
                        <div className="text-[var(--ink)] leading-relaxed font-body line-clamp-3">
                          <MathView content={item.firstReaction} inline />
                        </div>
                      </div>

                      {/* Primary method */}
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
                    </div>
                  </div>
                ))
              )}
            </div>
          </div>
        )}

        {/* TAB 2: FLASHCARD ACTIVE RECALL MODE */}
        {activeTab === 'flashcard' && (
          <div className="flex-1 flex flex-col p-4 sm:p-6 overflow-y-auto">
            {/* Subject filter & counter */}
            <div className="flex flex-wrap items-center justify-between gap-2 pb-3 border-b border-[var(--line)] font-mono text-xs">
              <div className="flex items-center gap-1 bg-[var(--well)] p-0.5 rounded-[8px] border border-[var(--line)] text-[11px]">
                <button
                  onClick={() => {
                    setFlashcardSubject('all');
                    setIsFlipped(false);
                  }}
                  className={`px-2 py-0.8 rounded-[6px] ${
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
                  className={`px-2 py-0.8 rounded-[6px] ${
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
                  className={`px-2 py-0.8 rounded-[6px] ${
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
                  className={`px-2 py-0.8 rounded-[6px] ${
                    flashcardSubject === 'gailv' ? 'bg-[var(--sheet)] font-bold text-[var(--blue)]' : 'text-[var(--muted)]'
                  }`}
                >
                  概率
                </button>
              </div>

              <div className="flex items-center gap-2">
                <span className="text-[var(--muted)]">
                  卡片 {currentCardIndex + 1} / {flashcardPool.length}
                </span>
                <button
                  onClick={handleRandomFlashcard}
                  className="flex items-center gap-1 px-2.5 py-1 rounded-[6px] bg-[var(--well)] hover:bg-[var(--sheet)] border border-[var(--line)] text-[var(--ink)]"
                  title="随机抽取"
                >
                  <Shuffle className="w-3 h-3 text-[var(--muted)]" />
                  <span>随机换题</span>
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
                    <span>主动提取训练</span>
                  </div>

                  {/* Card Front: Trigger Signal Prompt */}
                  <div className="space-y-3 py-2 text-center">
                    <div className="text-xs font-mono font-bold text-[var(--amber)] uppercase tracking-wider">
                      [ 看到题目特征 ]
                    </div>
                    <div className="text-base sm:text-xl font-display font-bold text-[var(--ink)] leading-relaxed bg-[var(--sheet)] p-4 sm:p-5 rounded-[12px] border border-[var(--line)] shadow-inner">
                      <MathView content={currentFlashcard.trigger} />
                    </div>
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
                        </div>
                      </div>

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
