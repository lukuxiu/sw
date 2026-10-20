import re, sys

sys.stdout.reconfigure(encoding='utf-8')

with open('src/components/KnowledgeDetailView.tsx', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace options rendering block
old_options_block = """                      {q.options && (
                        <div className="grid grid-cols-1 sm:grid-cols-2 gap-2 mt-3 pt-3 border-t border-[var(--line)]">
                          {q.options.map((opt: string, i: number) => (
                            <div key={i} className="text-xs text-[var(--ink)]">
                              <MathView content={opt} inline />
                            </div>
                          ))}
                        </div>
                      )}"""

new_options_block = """                      {q.options && q.options.length > 0 && (
                        <div className="grid grid-cols-1 sm:grid-cols-2 gap-2.5 mt-3.5 pt-3.5 border-t border-[var(--line)] font-mono text-xs">
                          {q.options.map((opt: string, i: number) => {
                            const optLabel = String.fromCharCode(65 + i);
                            const cleanOpt = opt.replace(new RegExp(`^\\\\s*\\\\(?${optLabel}\\\\)?[\\\\.、\\\\s]*`, 'i'), '').trim();
                            return (
                              <div
                                key={i}
                                className="flex items-start gap-2.5 p-2.5 rounded-[8px] bg-[var(--well)] hover:bg-[var(--sheet)] border border-[var(--line)] transition-colors group/opt"
                              >
                                <span className="w-5 h-5 rounded-[5px] bg-[var(--sheet)] text-[var(--blue)] group-hover/opt:bg-[var(--blue)] group-hover/opt:text-white font-bold text-[11px] flex items-center justify-center flex-shrink-0 border border-[var(--line)] shadow-2xs transition-colors">
                                  {optLabel}
                                </span>
                                <div className="flex-1 font-serif text-[var(--ink)] leading-relaxed pt-0.5">
                                  <MathView content={cleanOpt} inline />
                                </div>
                              </div>
                            );
                          })}
                        </div>
                      )}"""

if old_options_block in content:
    content = content.replace(old_options_block, new_options_block)
    print("Replaced options block successfully in KnowledgeDetailView.tsx")
else:
    print("Could not find exact old_options_block")

# Replace step rendering block
old_steps_block = """                        <div className="space-y-2 pt-1">
                          <span className="text-xs font-mono font-bold text-[var(--ink)]">分步解答过程：</span>
                          {q.solutionSteps.map((s: string, stepIdx: number) => (
                            <div
                              key={stepIdx}
                              className="text-xs text-[var(--ink)] bg-[var(--sheet)] p-3 rounded-[8px] border border-[var(--line)] leading-relaxed font-body"
                            >
                              <MathView content={s} inline />
                            </div>
                          ))}
                        </div>"""

new_steps_block = """                        <div className="space-y-2.5 pt-1">
                          <span className="text-xs font-mono font-bold text-[var(--ink)]">分步解答过程：</span>
                          {q.solutionSteps.map((s: string, stepIdx: number) => (
                            <div
                              key={stepIdx}
                              className="text-xs text-[var(--ink)] bg-[var(--sheet)] p-3 rounded-[8px] border border-[var(--line)] leading-relaxed font-body flex items-start gap-2.5"
                            >
                              <span className="px-1.5 py-0.5 rounded bg-[var(--well)] text-[var(--muted)] font-mono font-bold text-[10px] border border-[var(--line)] flex-shrink-0 mt-0.5">
                                步 {stepIdx + 1}
                              </span>
                              <div className="flex-1">
                                <MathView content={s} />
                              </div>
                            </div>
                          ))}
                        </div>"""

if old_steps_block in content:
    content = content.replace(old_steps_block, new_steps_block)
    print("Replaced steps block successfully in KnowledgeDetailView.tsx")

with open('src/components/KnowledgeDetailView.tsx', 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated KnowledgeDetailView.tsx.")
