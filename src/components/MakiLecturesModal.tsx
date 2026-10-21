import React, { useState, useMemo } from 'react';
import { 
  X, Search, BookOpen, Map, Award, Star, Filter, 
  ArrowRight, Layers, Flame, Zap, ChevronDown, ChevronUp,
  AlertTriangle, FileText, Compass, ExternalLink, ShieldAlert
} from 'lucide-react';
import { MAKI_LECTURES, MAKI_WAR_MAP, MakiLecture } from '../data/makiLectures';
import { MathView } from './MathView';

interface MakiLecturesModalProps {
  isOpen: boolean;
  onClose: () => void;
  onSelectTopic: (topicId: string) => void;
  initialLectureId?: string;
}

export const MakiLecturesModal: React.FC<MakiLecturesModalProps> = ({
  isOpen,
  onClose,
  onSelectTopic,
  initialLectureId,
}) => {
  if (!isOpen) return null;

  const [activeTab, setActiveTab] = useState<'lectures' | 'warmap'>('lectures');
  const [searchQuery, setSearchQuery] = useState('');
  const [selectedPaper, setSelectedPaper] = useState<'all' | '数一' | '数二' | '数三'>('all');
  const [selectedTag, setSelectedTag] = useState<string>('all');
  const [selectedPart, setSelectedPart] = useState<number | 'all'>('all');
  const [expandedLecId, setExpandedLecId] = useState<string | null>(initialLectureId || 'L10');
  const [warMapPaper, setWarMapPaper] = useState<'数一' | '数二' | '数三'>('数一');

  // Filter lectures
  const filteredLectures = useMemo(() => {
    return MAKI_LECTURES.filter((lec) => {
      // Paper filter
      if (selectedPaper === '数一' && lec.isMath3Only) return false;
      if (selectedPaper === '数二' && (lec.isMath1Only || lec.isMath3Only || lec.partNum === 4 || lec.partNum === 6)) return false;
      if (selectedPaper === '数三' && (lec.isMath1Only || (lec.partNum === 3 && [28, 31, 34, 35, 36, 37].includes(lec.num)))) return false;

      // Tag filter
      if (selectedTag === 'key' && !lec.isKey) return false;
      if (selectedTag === 'compressed' && !lec.isCompressed) return false;
      if (selectedTag === 'method' && !lec.isMethod) return false;
      if (selectedTag === 'math1' && !lec.isMath1Only) return false;
      if (selectedTag === 'math2' && !lec.isMath2Heavy) return false;

      // Part filter
      if (selectedPart !== 'all' && lec.partNum !== selectedPart) return false;

      // Query search
      if (searchQuery.trim()) {
        const q = searchQuery.toLowerCase().trim();
        const matchesTitle = lec.title.toLowerCase().includes(q) || lec.id.toLowerCase().includes(q);
        const matchesOrientation = lec.orientation.toLowerCase().includes(q);
        const matchesSubs = lec.subsections.some((s) => s.toLowerCase().includes(q));
        const matchesCards = lec.methodCards.some((c) => c.title.toLowerCase().includes(q) || c.content.toLowerCase().includes(q));
        if (!matchesTitle && !matchesOrientation && !matchesSubs && !matchesCards) return false;
      }

      return true;
    });
  }, [selectedPaper, selectedTag, selectedPart, searchQuery]);

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center p-2 sm:p-4 bg-black/60 backdrop-blur-xs font-body">
      <div className="bg-[var(--sheet)] border border-[var(--line)] rounded-[14px] w-full max-w-5xl max-h-[94vh] flex flex-col shadow-2xl overflow-hidden animate-fadeIn">
        
        {/* Header */}
        <div className="px-4 sm:px-6 py-3.5 bg-[var(--well)] border-b border-[var(--line)] flex items-center justify-between">
          <div className="flex items-center gap-2.5">
            <div className="w-8 h-8 rounded-[8px] bg-[var(--ink)] text-[var(--paper)] flex items-center justify-center font-display font-bold text-sm shadow-sm flex-shrink-0">
              66
            </div>
            <div>
              <div className="flex items-center gap-2">
                <h2 className="text-base font-display font-bold text-[var(--ink)] tracking-tight">
                  Maki 考研数学一站式大串讲 (66讲全景)
                </h2>
                <span className="text-[10px] font-mono px-1.5 py-0.2 rounded bg-[var(--sheet)] text-[var(--purple)] border border-[var(--purple)]/40 font-bold hidden sm:inline">
                  原书 1105 页完全同步
                </span>
              </div>
              <p className="text-[11px] text-[var(--muted)] font-mono">
                考频面板 · 重点/压缩分级 · 独家决策树方法卡 · 作战地图
              </p>
            </div>
          </div>

          <div className="flex items-center gap-2">
            {/* View switcher tabs */}
            <div className="bg-[var(--sheet)] p-0.5 rounded-[8px] border border-[var(--line)] flex items-center text-xs font-mono">
              <button
                onClick={() => setActiveTab('lectures')}
                className={`flex items-center gap-1 px-2.5 py-1 rounded-[6px] transition-colors cursor-pointer ${
                  activeTab === 'lectures'
                    ? 'bg-[var(--ink)] text-[var(--paper)] font-bold shadow-xs'
                    : 'text-[var(--muted)] hover:text-[var(--ink)]'
                }`}
              >
                <BookOpen className="w-3.5 h-3.5" />
                <span>66讲全目录</span>
              </button>
              <button
                onClick={() => setActiveTab('warmap')}
                className={`flex items-center gap-1 px-2.5 py-1 rounded-[6px] transition-colors cursor-pointer ${
                  activeTab === 'warmap'
                    ? 'bg-[var(--ink)] text-[var(--paper)] font-bold shadow-xs'
                    : 'text-[var(--muted)] hover:text-[var(--ink)]'
                }`}
              >
                <Map className="w-3.5 h-3.5" />
                <span>全课程作战地图</span>
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

        {/* TAB 1: 66 LECTURES DIRECTORY */}
        {activeTab === 'lectures' && (
          <div className="flex-1 flex flex-col overflow-hidden">
            {/* Filter Toolbar */}
            <div className="px-4 sm:px-6 py-2.5 bg-[var(--sheet)] border-b border-[var(--line)] space-y-2">
              <div className="flex items-center gap-2">
                <div className="relative flex-1">
                  <Search className="w-3.5 h-3.5 absolute left-3 top-2.5 text-[var(--muted)]" />
                  <input
                    type="text"
                    placeholder="搜索讲次编号（如 L10、L33）、标题、决策树、中值定理、语言互译..."
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
                  筛选出 {filteredLectures.length} / 66 讲
                </span>
              </div>

              {/* Sub-Filters: Paper + Tags + Parts */}
              <div className="flex flex-wrap items-center justify-between gap-2 pt-1 border-t border-[var(--line)] text-[11px] font-mono">
                {/* Paper filter */}
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

                {/* Tag filter */}
                <div className="flex items-center gap-1 overflow-x-auto no-scrollbar">
                  <span className="text-[var(--muted)] mr-1">讲次性质:</span>
                  {[
                    { id: 'all', label: '全部' },
                    { id: 'key', label: '重点讲 (18讲)' },
                    { id: 'compressed', label: '压缩讲 (11讲)' },
                    { id: 'method', label: '方法讲 (7讲)' },
                    { id: 'math1', label: '数一专属' },
                    { id: 'math2', label: '数二重点' },
                  ].map((tg) => (
                    <button
                      key={tg.id}
                      onClick={() => setSelectedTag(tg.id)}
                      className={`px-2 py-0.5 rounded-[5px] transition-colors cursor-pointer ${
                        selectedTag === tg.id
                          ? 'bg-[var(--blue-bg)] text-[var(--blue)] font-bold border border-[var(--blue)]'
                          : 'bg-[var(--well)] text-[var(--muted)] hover:text-[var(--ink)]'
                      }`}
                    >
                      {tg.label}
                    </button>
                  ))}
                </div>
              </div>

              {/* Parts Pills */}
              <div className="flex items-center gap-1 overflow-x-auto no-scrollbar py-0.5 text-[11px] font-mono">
                {[
                  { id: 'all', label: '全部编次' },
                  { id: 0, label: '第0编 预备' },
                  { id: 1, label: '第1编 一元微积分' },
                  { id: 2, label: '第2编 微分方程' },
                  { id: 3, label: '第3编 多元微积分' },
                  { id: 4, label: '第4编 无穷级数' },
                  { id: 5, label: '第5编 线性代数' },
                  { id: 6, label: '第6编 概率统计' },
                  { id: 7, label: '第7编 应试工程' },
                ].map((pt) => (
                  <button
                    key={pt.id}
                    onClick={() => setSelectedPart(pt.id as any)}
                    className={`px-2 py-0.6 rounded-[5px] flex-shrink-0 transition-colors cursor-pointer ${
                      selectedPart === pt.id
                        ? 'bg-[var(--ink)] text-[var(--paper)] font-bold'
                        : 'bg-[var(--well)] text-[var(--muted)] hover:text-[var(--ink)]'
                    }`}
                  >
                    {pt.label}
                  </button>
                ))}
              </div>
            </div>

            {/* Lectures List */}
            <div className="flex-1 overflow-y-auto p-3 sm:p-6 space-y-3">
              {filteredLectures.map((lec) => {
                const isExpanded = expandedLecId === lec.id;

                return (
                  <div
                    key={lec.id}
                    className={`bg-[var(--well)] border rounded-[12px] p-3.5 sm:p-4.5 transition-all space-y-3 ${
                      isExpanded 
                        ? 'border-[var(--blue)] shadow-md' 
                        : 'border-[var(--line)] hover:border-[var(--line-strong)]'
                    }`}
                  >
                    {/* Header line */}
                    <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-2 pb-2 border-b border-[var(--line)]">
                      <div className="flex items-center gap-2 flex-wrap">
                        <span className="w-9 h-7 rounded-[6px] bg-[var(--sheet)] text-[var(--ink)] font-mono font-bold text-xs flex items-center justify-center border border-[var(--line)]">
                          {lec.id}
                        </span>
                        <h3 className="text-sm font-bold font-display text-[var(--ink)]">
                          {lec.title}
                        </h3>
                        <span className="text-[10px] font-mono px-1.5 py-0.2 rounded bg-[var(--sheet)] text-[var(--muted)] border border-[var(--line)]">
                          {lec.partTitle} · p.{lec.page}~{lec.pageEnd}
                        </span>

                        {/* Badges */}
                        <div className="flex items-center gap-1">
                          {lec.isKey && (
                            <span className="text-[9px] font-mono px-1.5 py-0.2 rounded bg-[var(--red-bg)] text-[var(--red)] border border-[var(--red)]/40 font-bold flex items-center gap-0.5">
                              <Flame className="w-2.5 h-2.5" />
                              重点讲
                            </span>
                          )}
                          {lec.isCompressed && (
                            <span className="text-[9px] font-mono px-1.5 py-0.2 rounded bg-[var(--well)] text-[var(--muted)] border border-[var(--line)]">
                              压缩讲
                            </span>
                          )}
                          {lec.isMethod && (
                            <span className="text-[9px] font-mono px-1.5 py-0.2 rounded bg-[var(--purple-bg)]/30 text-[var(--purple)] border border-[var(--purple)]/40 font-bold">
                              方法课
                            </span>
                          )}
                          {lec.isMath1Only && (
                            <span className="text-[9px] font-mono px-1.5 py-0.2 rounded bg-[var(--blue-bg)] text-[var(--blue)] border border-[var(--blue)]/40 font-bold">
                              仅数一
                            </span>
                          )}
                          {lec.isMath2Heavy && (
                            <span className="text-[9px] font-mono px-1.5 py-0.2 rounded bg-[var(--amber-bg)] text-[var(--amber)] border border-[var(--amber)]/40 font-bold">
                              数二重点
                            </span>
                          )}
                          {lec.isMath3Only && (
                            <span className="text-[9px] font-mono px-1.5 py-0.2 rounded bg-[var(--green-bg)] text-[var(--green)] border border-[var(--green)]/40 font-bold">
                              仅数三
                            </span>
                          )}
                        </div>
                      </div>

                      <div className="flex items-center gap-2 self-end sm:self-auto">
                        {lec.mappedTopicIds.length > 0 && (
                          <button
                            onClick={() => {
                              onSelectTopic(lec.mappedTopicIds[0]);
                              onClose();
                            }}
                            className="flex items-center gap-1 text-xs font-mono text-[var(--blue)] hover:underline cursor-pointer"
                          >
                            <span>去考点做题</span>
                            <ArrowRight className="w-3 h-3" />
                          </button>
                        )}
                        <button
                          onClick={() => setExpandedLecId(isExpanded ? null : lec.id)}
                          className="p-1 rounded text-[var(--muted)] hover:text-[var(--ink)] cursor-pointer"
                        >
                          {isExpanded ? <ChevronUp className="w-4 h-4" /> : <ChevronDown className="w-4 h-4" />}
                        </button>
                      </div>
                    </div>

                    {/* Orientation Quote */}
                    <div className="text-xs text-[var(--ink)] leading-relaxed font-body bg-[var(--sheet)] p-3 rounded-[8px] border border-[var(--line)]">
                      <div className="text-[10px] font-mono font-bold text-[var(--amber)] mb-1 flex items-center gap-1">
                        <Zap className="w-3 h-3" />
                        <span>Maki 讲义实战定位：</span>
                      </div>
                      <p className="line-clamp-2 md:line-clamp-none">
                        {lec.orientation}
                      </p>
                    </div>

                    {/* Exam Frequency Stats Panel */}
                    <div className="grid grid-cols-2 sm:grid-cols-4 md:grid-cols-6 gap-2 text-[11px] font-mono">
                      <div className="bg-[var(--sheet)] p-2 rounded-[6px] border border-[var(--line)]">
                        <span className="text-[var(--muted)] block text-[10px]">17年真题题量</span>
                        <span className="font-bold text-[var(--ink)]">{lec.stats.positions > 0 ? `${lec.stats.independentQuestions}题 (${lec.stats.positions}题位)` : '方法/无真题'}</span>
                      </div>
                      <div className="bg-[var(--sheet)] p-2 rounded-[6px] border border-[var(--line)]">
                        <span className="text-[var(--muted)] block text-[10px]">题型分布</span>
                        <span className="text-[var(--ink)] font-bold">
                          {lec.stats.positions > 0 ? `${lec.stats.choiceCount}选·${lec.stats.blankCount}填·${lec.stats.solutionCount}解` : '应试与思维'}
                        </span>
                      </div>
                      <div className="bg-[var(--sheet)] p-2 rounded-[6px] border border-[var(--line)]">
                        <span className="text-[var(--muted)] block text-[10px]">数一分值占比</span>
                        <span className="text-[var(--blue)] font-bold">{lec.stats.math1Score > 0 ? `${lec.stats.math1Percent} (${lec.stats.math1Score}分)` : '0%'}</span>
                      </div>
                      <div className="bg-[var(--sheet)] p-2 rounded-[6px] border border-[var(--line)]">
                        <span className="text-[var(--muted)] block text-[10px]">数二分值占比</span>
                        <span className="text-[var(--amber)] font-bold">{lec.stats.math2Score > 0 ? `${lec.stats.math2Percent} (${lec.stats.math2Score}分)` : '0%'}</span>
                      </div>
                      <div className="bg-[var(--sheet)] p-2 rounded-[6px] border border-[var(--line)]">
                        <span className="text-[var(--muted)] block text-[10px]">数三分值占比</span>
                        <span className="text-[var(--green)] font-bold">{lec.stats.math3Score > 0 ? `${lec.stats.math3Percent} (${lec.stats.math3Score}分)` : '0%'}</span>
                      </div>
                      <div className="bg-[var(--sheet)] p-2 rounded-[6px] border border-[var(--line)]">
                        <span className="text-[var(--muted)] block text-[10px]">平均难度</span>
                        <span className="text-[var(--amber)] font-bold">{lec.stats.avgDifficulty}</span>
                      </div>
                    </div>

                    {/* Expanded Content: Subsections + Method Cards */}
                    {isExpanded && (
                      <div className="space-y-3 pt-2 border-t border-[var(--line)] animate-fadeIn">
                        {/* Subsections list */}
                        {lec.subsections.length > 0 && (
                          <div className="space-y-1.5">
                            <span className="text-xs font-mono font-bold text-[var(--ink)] block">
                              ★ 本讲细分知识小节 ({lec.subsections.length} 节)：
                            </span>
                            <div className="flex flex-wrap gap-1.5">
                              {lec.subsections.map((sub, si) => (
                                <span
                                  key={si}
                                  className="text-[11px] font-mono px-2 py-0.5 rounded-[5px] bg-[var(--sheet)] text-[var(--ink)] border border-[var(--line)]"
                                >
                                  {sub}
                                </span>
                              ))}
                            </div>
                          </div>
                        )}

                        {/* Method Cards */}
                        {lec.methodCards.length > 0 && (
                          <div className="space-y-2">
                            <span className="text-xs font-mono font-bold text-[var(--purple)] flex items-center gap-1">
                              <Layers className="w-3.5 h-3.5" />
                              <span>Maki 独家解题思维决策树与方法卡：</span>
                            </span>
                            <div className="grid grid-cols-1 gap-2">
                              {lec.methodCards.map((mc, mci) => (
                                <div
                                  key={mci}
                                  className="bg-[var(--sheet)] p-3 rounded-[8px] border border-[var(--line)] space-y-1 text-xs"
                                >
                                  <div className="flex items-center justify-between font-mono">
                                    <span className="font-bold text-[var(--ink)] text-xs">{mc.title}</span>
                                    {mc.subtitle && (
                                      <span className="text-[10px] text-[var(--purple)] px-1.5 py-0.2 rounded bg-[var(--purple-bg)]/20 border border-[var(--purple)]/30">
                                        {mc.subtitle}
                                      </span>
                                    )}
                                  </div>
                                  <p className="text-[var(--ink)] leading-relaxed font-body">
                                    {mc.content}
                                  </p>
                                </div>
                              ))}
                            </div>
                          </div>
                        )}
                      </div>
                    )}
                  </div>
                );
              })}
            </div>
          </div>
        )}

        {/* TAB 2: WAR MAP (全课程作战地图) */}
        {activeTab === 'warmap' && (
          <div className="flex-1 overflow-y-auto p-4 sm:p-6 space-y-6">
            
            {/* Top Banner: Strategy intro */}
            <div className="bg-[var(--well)] p-4 rounded-[12px] border-l-3 border-[var(--purple)] space-y-1.5">
              <div className="flex items-center gap-1.5 text-xs font-mono font-bold text-[var(--purple)]">
                <Map className="w-4 h-4" />
                <span>Maki 考研数学全课程作战地图（51套真题实测）</span>
              </div>
              <p className="text-xs sm:text-sm text-[var(--ink)] leading-relaxed font-body">
                这一章不是目录，是作战地图。每一讲后面的数字，不是简介，而是这一讲在真题里值多少分。
                数二复习是“打歼灭战”（前8讲吃掉52.8%分值），数一数三是“扫大片”（前10讲才占51%）。
              </p>
            </div>

            {/* Section 1: Top 10 Lectures Rankings by Paper */}
            <div className="space-y-3">
              <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-2 pb-1 border-b border-[var(--line)]">
                <div className="flex items-center gap-2">
                  <Flame className="w-4 h-4 text-[var(--red)]" />
                  <h3 className="text-sm font-bold font-display text-[var(--ink)]">
                    三卷各自的十大讲（按 17 年分值占比排行榜）
                  </h3>
                </div>

                {/* Paper Switcher for Top 10 */}
                <div className="flex items-center gap-1 bg-[var(--well)] p-0.5 rounded-[8px] border border-[var(--line)] text-xs font-mono">
                  {(['数一', '数二', '数三'] as const).map((p) => (
                    <button
                      key={p}
                      onClick={() => setWarMapPaper(p)}
                      className={`px-3 py-1 rounded-[6px] transition-colors cursor-pointer ${
                        warMapPaper === p
                          ? 'bg-[var(--ink)] text-[var(--paper)] font-bold'
                          : 'text-[var(--muted)] hover:text-[var(--ink)]'
                      }`}
                    >
                      {p}
                    </button>
                  ))}
                </div>
              </div>

              {/* Top 10 List Display */}
              {(() => {
                const mapData = MAKI_WAR_MAP.topLectures.find((t) => t.paper === warMapPaper)!;
                return (
                  <div className="space-y-2">
                    <div className="flex items-center justify-between text-xs font-mono text-[var(--muted)] bg-[var(--well)] p-2 rounded-[6px]">
                      <span>{warMapPaper} 前十大讲总分占比：<strong className="text-[var(--red)]">{mapData.totalScorePercent}</strong></span>
                      <span>平均每年卷面贡献：<strong className="text-[var(--ink)]">{mapData.annualAvgPoints}</strong></span>
                    </div>

                    <div className="grid grid-cols-1 sm:grid-cols-2 gap-2">
                      {mapData.list.map((item) => (
                        <div
                          key={item.rank}
                          className="bg-[var(--sheet)] border border-[var(--line)] hover:border-[var(--blue)] p-3 rounded-[8px] flex items-center justify-between transition-colors"
                        >
                          <div className="flex items-center gap-2">
                            <span className={`w-5 h-5 rounded-[4px] font-mono text-xs font-bold flex items-center justify-center ${
                              item.rank <= 3 ? 'bg-[var(--amber-bg)] text-[var(--amber)]' : 'bg-[var(--well)] text-[var(--muted)]'
                            }`}>
                              {item.rank}
                            </span>
                            <span className="font-mono text-xs font-bold text-[var(--blue)]">{item.lectureId}</span>
                            <span className="text-xs font-display font-semibold text-[var(--ink)]">{item.lectureTitle}</span>
                          </div>

                          <div className="text-right font-mono text-xs">
                            <span className="font-bold text-[var(--ink)]">{item.scorePercent}</span>
                            <span className="text-[10px] text-[var(--muted)] block">每年约 {item.annualPoints}</span>
                          </div>
                        </div>
                      ))}
                    </div>
                  </div>
                );
              })()}
            </div>

            {/* Section 2: Zero Exam Topics List */}
            <div className="space-y-3">
              <div className="flex items-center gap-2 pb-1 border-b border-[var(--line)]">
                <ShieldAlert className="w-4 h-4 text-[var(--amber)]" />
                <h3 className="text-sm font-bold font-display text-[var(--ink)]">
                  零命题清单：十个 17 年没单独考过的考点与应对策略
                </h3>
              </div>
              <p className="text-xs text-[var(--muted)] font-mono">
                未单独命题不等于没被考到，它们大多是别的题里的某一步。只看结论，不做题型训练，杜绝浪费两周时间！
              </p>

              <div className="grid grid-cols-1 md:grid-cols-2 gap-2.5">
                {MAKI_WAR_MAP.zeroExamTopics.map((zt) => (
                  <div
                    key={zt.code}
                    className="bg-[var(--sheet)] border border-[var(--line)] p-3 rounded-[8px] space-y-1.5 text-xs"
                  >
                    <div className="flex items-center justify-between font-mono">
                      <div className="flex items-center gap-1.5">
                        <span className="px-1.5 py-0.2 rounded bg-[var(--well)] text-[var(--muted)] text-[10px] font-bold">
                          考点 {zt.code} · {zt.lectureId}
                        </span>
                        <span className="font-bold text-[var(--ink)]">{zt.title}</span>
                      </div>
                      <span className="text-[10px] text-[var(--red)] font-bold">{zt.fact}</span>
                    </div>

                    <div className="text-[11px] font-body text-[var(--muted)] bg-[var(--well)] p-2 rounded leading-relaxed">
                      <strong className="text-[var(--ink)]">应对方案：</strong>
                      {zt.strategy}
                    </div>
                  </div>
                ))}
              </div>
            </div>

            {/* Section 3: Shortest Paths by Paper */}
            <div className="space-y-3">
              <div className="flex items-center gap-2 pb-1 border-b border-[var(--line)]">
                <Compass className="w-4 h-4 text-[var(--green)]" />
                <h3 className="text-sm font-bold font-display text-[var(--ink)]">
                  三卷最短听课与复习路径规划
                </h3>
              </div>

              <div className="grid grid-cols-1 md:grid-cols-3 gap-3">
                {MAKI_WAR_MAP.shortestPaths.map((sp) => (
                  <div
                    key={sp.paper}
                    className="bg-[var(--sheet)] border border-[var(--line)] p-4 rounded-[10px] space-y-2 text-xs"
                  >
                    <div className="flex items-center justify-between pb-1.5 border-b border-[var(--line)]">
                      <span className="font-bold font-display text-sm text-[var(--ink)]">{sp.paper} 路径</span>
                      <span className="text-xs font-mono text-[var(--purple)] font-bold">{sp.estimatedHours}</span>
                    </div>

                    <div className="font-mono text-[11px] text-[var(--muted)] space-y-0.5">
                      <div>需听讲次：<strong className="text-[var(--ink)]">{sp.lecturesCount} 讲</strong></div>
                      <div>其中重点讲：<strong className="text-[var(--red)]">{sp.keyLecturesCount} 讲</strong></div>
                    </div>

                    <p className="text-[11px] text-[var(--ink)] font-body leading-relaxed pt-1">
                      {sp.strategySummary}
                    </p>
                  </div>
                ))}
              </div>
            </div>

          </div>
        )}

      </div>
    </div>
  );
};
