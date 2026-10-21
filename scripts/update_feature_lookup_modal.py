import re, sys

sys.stdout.reconfigure(encoding='utf-8')

with open('src/components/FeatureLookupModal.tsx', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Add Eye, EyeOff to lucide-react import
text = text.replace(
    "import { \n  X, Search, Sparkles, Filter, ExternalLink, ArrowRight, \n  RotateCcw, CheckCircle2, AlertCircle, Shuffle, BookOpen, Layers,\n  ChevronDown, ChevronUp, FileText, Check\n} from 'lucide-react';",
    "import { \n  X, Search, Sparkles, Filter, ExternalLink, ArrowRight, \n  RotateCcw, CheckCircle2, AlertCircle, Shuffle, BookOpen, Layers,\n  ChevronDown, ChevronUp, FileText, Check, Eye, EyeOff\n} from 'lucide-react';"
)

# 2. Add maskMode state
state_target = "  // Expanded examples on matrix cards\n  const [expandedCardId, setExpandedCardId] = useState<string | null>(null);"
state_rep = """  // Expanded examples on matrix cards
  const [expandedCardId, setExpandedCardId] = useState<string | null>(null);

  // Mask recall mode (背诵遮盖模式)
  const [isMaskMode, setIsMaskMode] = useState<boolean>(false);
  const [revealedFeatures, setRevealedFeatures] = useState<Record<string, boolean>>({});"""

text = text.replace(state_target, state_rep)

# 3. Add mask toggle button in filter bar
filter_bar_target = """                <div className="flex items-center gap-1">
                  <span className="text-[var(--muted)] mr-1">年份:</span>"""

filter_bar_rep = """                <div className="flex items-center gap-2">
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
                  <span className="text-[var(--muted)] mr-1">年份:</span>"""

text = text.replace(filter_bar_target, filter_bar_rep)

# 4. Add meta method badge on card header
card_meta_target = """                          <div className="flex items-center gap-1">
                            {item.papers.map((p) => (
                              <span key={p} className="text-[9px] font-mono px-1 py-0.2 rounded bg-[var(--sheet)] text-[var(--blue)] border border-[var(--line)]">
                                {p}
                              </span>
                            ))}
                          </div>"""

card_meta_rep = """                          <div className="flex items-center gap-1">
                            {item.papers.map((p) => (
                              <span key={p} className="text-[9px] font-mono px-1 py-0.2 rounded bg-[var(--sheet)] text-[var(--blue)] border border-[var(--line)]">
                                {p}
                              </span>
                            ))}
                            {item.metaMethodName && (
                              <span className="text-[9px] font-mono px-1.5 py-0.2 rounded bg-[var(--purple-bg)]/30 text-[var(--purple)] border border-[var(--purple)]/40 font-bold flex items-center gap-0.5">
                                <Layers className="w-2.5 h-2.5 text-[var(--purple)]" />
                                通用方法: {item.metaMethodName}
                              </span>
                            )}
                          </div>"""

text = text.replace(card_meta_target, card_meta_rep)

# 5. Mask reaction and method in columns
cols_target = """                        {/* First reaction */}
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
                        </div>"""

cols_rep = """                        {/* First reaction & Primary method with Mask Mode support */}
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
                        )}"""

text = text.replace(cols_target, cols_rep)

# 6. Enhance options rendering in examples
examples_target = """                                <div className="text-[var(--ink)] font-serif leading-relaxed bg-[var(--well)] p-2.5 rounded-[6px]">
                                  <MathView content={ex.prompt} />
                                </div>

                                <div className="grid grid-cols-1 sm:grid-cols-2 gap-2 text-[11px] font-mono">"""

examples_rep = """                                <div className="text-[var(--ink)] font-serif leading-relaxed bg-[var(--well)] p-2.5 rounded-[6px]">
                                  <MathView content={ex.prompt} />
                                  {ex.options && ex.options.length > 0 && (
                                    <div className="grid grid-cols-1 sm:grid-cols-2 gap-2 mt-2 pt-2 border-t border-[var(--line)] font-mono text-[11px]">
                                      {ex.options.map((opt, oi) => {
                                        const optLabel = String.fromCharCode(65 + oi);
                                        const cleanOpt = opt.replace(new RegExp(`^\\\\s*\\\\(?${optLabel}\\\\)?[-.、\\\\s]*`, 'i'), '').trim();
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

                                <div className="grid grid-cols-1 sm:grid-cols-2 gap-2 text-[11px] font-mono">"""

text = text.replace(examples_target, examples_rep)

with open('src/components/FeatureLookupModal.tsx', 'w', encoding='utf-8') as f:
    f.write(text)

print("Updated src/components/FeatureLookupModal.tsx with mask mode, meta pills, and option cards!")
