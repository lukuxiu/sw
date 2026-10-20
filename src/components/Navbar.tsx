import React, { useState, useEffect, useRef } from 'react';
import { 
  Search, X, Compass, Award, Sun, Moon
} from 'lucide-react';
import { searchKnowledgeBase } from '../data/search';
import { MathView } from './MathView';
import { SearchMatchItem } from '../data/types';
import { getOverallProgress } from '../data/storage';

interface NavbarProps {
  onNavigateMindmap: () => void;
  onNavigateChapter: (chapterId: string) => void;
  onNavigateTopic: (topicId: string) => void;
  onOpenReviewModal: () => void;
}

export const Navbar: React.FC<NavbarProps> = ({
  onNavigateMindmap,
  onNavigateTopic,
  onOpenReviewModal,
}) => {
  const [searchQuery, setSearchQuery] = useState('');
  const [searchResults, setSearchResults] = useState<SearchMatchItem[]>([]);
  const [isSearchOpen, setIsSearchOpen] = useState(false);
  const [progress, setProgress] = useState(getOverallProgress());

  // Theme toggle: dark (default) vs light paper
  const [theme, setTheme] = useState<'dark' | 'light'>(() => {
    return (localStorage.getItem('maki_theme') as 'dark' | 'light') || 'dark';
  });

  const searchBoxRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    document.documentElement.setAttribute('data-theme', theme);
    localStorage.setItem('maki_theme', theme);
  }, [theme]);

  const toggleTheme = () => {
    setTheme((t) => (t === 'dark' ? 'light' : 'dark'));
  };

  useEffect(() => {
    const updateStats = () => setProgress(getOverallProgress());
    window.addEventListener('learning-status-change', updateStats);
    return () => window.removeEventListener('learning-status-change', updateStats);
  }, []);

  useEffect(() => {
    const handleClickOutside = (e: MouseEvent) => {
      if (searchBoxRef.current && !searchBoxRef.current.contains(e.target as Node)) {
        setIsSearchOpen(false);
      }
    };
    document.addEventListener('mousedown', handleClickOutside);
    return () => document.removeEventListener('mousedown', handleClickOutside);
  }, []);

  const handleSearchChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const q = e.target.value;
    setSearchQuery(q);
    if (q.trim().length > 0) {
      const res = searchKnowledgeBase(q);
      setSearchResults(res);
      setIsSearchOpen(true);
    } else {
      setSearchResults([]);
      setIsSearchOpen(false);
    }
  };

  const handleSelectSearchResult = (nodeId: string) => {
    onNavigateTopic(nodeId);
    setIsSearchOpen(false);
    setSearchQuery('');
  };

  return (
    <header className="sticky top-0 z-40 bg-[var(--sheet)] border-b border-[var(--line)] px-4 lg:px-8 h-14 flex items-center text-[var(--ink)]">
      <div className="max-w-7xl mx-auto w-full flex items-center justify-between gap-4">
        {/* Maki Style Brand Logo */}
        <div 
          onClick={onNavigateMindmap}
          className="flex items-center space-x-2.5 cursor-pointer group flex-shrink-0"
        >
          <div className="w-8 h-8 rounded-[7px] bg-[var(--ink)] text-[var(--paper)] flex items-center justify-center font-display font-bold text-base shadow-sm group-hover:scale-105 transition-transform">
            M
          </div>
          <div>
            <div className="flex items-center gap-1.5">
              <span className="font-display font-bold text-sm tracking-tight text-[var(--ink)]">
                Maki 考研数学
              </span>
              <span className="text-[11px] font-mono px-1.5 py-0.2 rounded bg-[var(--well)] text-[var(--muted)] border border-[var(--line)]">
                思路知识库
              </span>
            </div>
            <p className="text-[10px] text-[var(--muted)] hidden sm:block font-body">
              看到什么 · 想到什么 · 历年真题分类
            </p>
          </div>
        </div>

        {/* Maki Style Search Box */}
        <div ref={searchBoxRef} className="relative flex-1 max-w-md mx-2">
          <div className="relative">
            <Search className="w-3.5 h-3.5 absolute left-3 top-2.5 text-[var(--muted)]" />
            <input
              type="text"
              placeholder="搜索考点、方法、公式或真题（0/0、路径无关、2025、基础解系）..."
              value={searchQuery}
              onChange={handleSearchChange}
              onFocus={() => {
                if (searchQuery.trim().length > 0) setIsSearchOpen(true);
              }}
              className="w-full bg-[var(--well)] focus:bg-[var(--sheet)] border border-transparent focus:border-[var(--line)] rounded-[9px] pl-9 pr-8 py-1.5 text-xs text-[var(--ink)] placeholder-[var(--muted)] focus:outline-none transition-colors"
            />
            {searchQuery && (
              <button
                onClick={() => {
                  setSearchQuery('');
                  setIsSearchOpen(false);
                }}
                className="absolute right-2.5 top-2 text-[var(--muted)] hover:text-[var(--ink)]"
              >
                <X className="w-3.5 h-3.5" />
              </button>
            )}
          </div>

          {/* Search Results Dropdown */}
          {isSearchOpen && (
            <div className="absolute left-0 right-0 top-full mt-1.5 bg-[var(--sheet)] border border-[var(--line)] rounded-[12px] shadow-xl overflow-hidden z-50 max-h-96 overflow-y-auto">
              <div className="px-3 py-2 bg-[var(--well)] border-b border-[var(--line)] text-[11px] text-[var(--muted)] flex items-center justify-between font-mono">
                <span>匹配结果 ({searchResults.length})</span>
                <span className="text-[10px]">单击直达</span>
              </div>

              {searchResults.length === 0 ? (
                <div className="p-6 text-center text-xs text-[var(--muted)] font-mono">
                  未找到与 “{searchQuery}” 相关的考点或真题
                </div>
              ) : (
                <div className="divide-y divide-[var(--line)]">
                  {searchResults.map((item) => (
                    <div
                      key={item.nodeId}
                      onClick={() => handleSelectSearchResult(item.nodeId)}
                      className="p-3 hover:bg-[var(--well)] cursor-pointer transition-colors group"
                    >
                      <div className="flex items-center justify-between gap-2">
                        <span className="text-xs font-semibold text-[var(--ink)] group-hover:text-[var(--blue)] transition-colors">
                          {item.title}
                        </span>
                        <span className="text-[10px] font-mono px-1.5 py-0.5 rounded bg-[var(--well)] text-[var(--muted)] border border-[var(--line)]">
                          {item.subjectName} · {item.chapterTitle}
                        </span>
                      </div>
                      <div className="text-[11px] text-[var(--muted)] mt-1 line-clamp-1 font-mono">
                        <span className="text-[var(--blue)]">[{item.matchedField}]</span> <MathView content={item.snippet} inline />
                      </div>
                    </div>
                  ))}
                </div>
              )}
            </div>
          )}
        </div>

        {/* Right Navigation Actions */}
        <div className="flex items-center space-x-2">
          {/* Mindmap Nav Button */}
          <button
            onClick={onNavigateMindmap}
            className="flex items-center gap-1.5 px-3 py-1.5 rounded-[8px] bg-[var(--well)] hover:bg-[var(--sheet)] text-xs text-[var(--ink)] border border-[var(--line)] transition-colors"
          >
            <Compass className="w-3.5 h-3.5 text-[var(--muted)]" />
            <span className="hidden sm:inline font-medium">总思维导图</span>
          </button>

          {/* Review Hub Button */}
          <button
            onClick={onOpenReviewModal}
            className="flex items-center gap-1.5 px-3 py-1.5 rounded-[8px] bg-[var(--well)] hover:bg-[var(--sheet)] text-xs text-[var(--ink)] border border-[var(--line)] transition-colors"
          >
            <Award className="w-3.5 h-3.5 text-[var(--blue)]" />
            <span className="hidden sm:inline font-medium">复习薄弱点</span>
            <span className="font-mono text-[11px] text-[var(--muted)]">
              [{progress.mastered}/{progress.total}]
            </span>
          </button>

          {/* Theme Switcher Button */}
          <button
            onClick={toggleTheme}
            className="p-1.5 rounded-[8px] bg-[var(--well)] hover:bg-[var(--sheet)] text-[var(--muted)] hover:text-[var(--ink)] border border-[var(--line)] transition-colors"
            title={theme === 'dark' ? '切换为纸质明亮模式' : '切换为夜间深色模式'}
          >
            {theme === 'dark' ? (
              <Sun className="w-3.5 h-3.5 text-[var(--amber)]" />
            ) : (
              <Moon className="w-3.5 h-3.5 text-[var(--blue)]" />
            )}
          </button>
        </div>
      </div>
    </header>
  );
};
