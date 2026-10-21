import re, sys

sys.stdout.reconfigure(encoding='utf-8')
with open('src/components/MetaMethodModal.tsx', 'r', encoding='utf-8') as f:
    text = f.read()

target = """            {/* Pitfalls */}
            {activeMethod.commonPitfalls && activeMethod.commonPitfalls.length > 0 && ("""

rep = """            {/* Representative Exam Questions */}
            {activeMethod.representativeQuestions && activeMethod.representativeQuestions.length > 0 && (
              <div className="space-y-3">
                <div className="flex items-center justify-between text-xs font-mono text-[var(--muted)]">
                  <span className="font-bold text-[var(--ink)]">历年真题实战考查（典型考研真题与实战切入点）：</span>
                  <span className="text-[var(--purple)] font-bold">{activeMethod.representativeQuestions.length} 道精选真题</span>
                </div>

                <div className="space-y-2.5">
                  {activeMethod.representativeQuestions.map((q, qi) => (
                    <div
                      key={qi}
                      className="bg-[var(--sheet)] border border-[var(--line)] hover:border-[var(--purple)]/50 p-3.5 rounded-[10px] space-y-2 transition-colors"
                    >
                      <div className="flex items-center justify-between">
                        <div className="flex items-center gap-2">
                          <span className="px-2 py-0.5 rounded-[5px] bg-[var(--well)] text-[var(--ink)] font-mono text-[11px] font-bold border border-[var(--line)]">
                            {q.year} · {q.category} · {q.questionNumber}
                          </span>
                        </div>
                        <button
                          onClick={() => {
                            onSelectTopic(q.topicId);
                            onClose();
                          }}
                          className="flex items-center gap-1 text-xs font-mono text-[var(--blue)] hover:underline cursor-pointer"
                        >
                          <span>进入对应考点</span>
                          <ArrowRight className="w-3 h-3" />
                        </button>
                      </div>

                      <div className="text-xs text-[var(--ink)] font-serif leading-relaxed bg-[var(--well)] p-2.5 rounded-[8px] border border-[var(--line)]">
                        <MathView content={q.stem} />
                      </div>

                      <div className="text-xs font-mono text-[var(--purple)] bg-[var(--purple-bg)]/20 p-2 rounded-[6px] border border-[var(--purple)]/30 flex items-start gap-1.5">
                        <span className="font-bold flex-shrink-0">方法切入点：</span>
                        <span className="font-body text-[var(--ink)] leading-relaxed"><MathView content={q.methodUsage} inline /></span>
                      </div>
                    </div>
                  ))}
                </div>
              </div>
            )}

            {/* Pitfalls */}
            {activeMethod.commonPitfalls && activeMethod.commonPitfalls.length > 0 && ("""

text_norm = text.replace('\r\n', '\n')
if target in text_norm:
    text_norm = text_norm.replace(target, rep)
    with open('src/components/MetaMethodModal.tsx', 'w', encoding='utf-8') as f:
        f.write(text_norm)
    print("Updated MetaMethodModal.tsx successfully!")
else:
    print("Target not found in MetaMethodModal.tsx")
