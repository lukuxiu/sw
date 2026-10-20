import React, { useState } from 'react';
import { X, Network, ArrowRight, Lightbulb, Compass, AlertTriangle } from 'lucide-react';
import { UNIVERSAL_META_METHODS } from '../data/metaMethods';
import { UniversalMetaMethod } from '../data/types';
import { MathView } from './MathView';

interface MetaMethodModalProps {
  isOpen: boolean;
  onClose: () => void;
  onSelectTopic: (topicId: string) => void;
}

export const MetaMethodModal: React.FC<MetaMethodModalProps> = ({
  isOpen,
  onClose,
  onSelectTopic,
}) => {
  if (!isOpen) return null;

  const [activeMethodId, setActiveMethodId] = useState<string>(UNIVERSAL_META_METHODS[0].id);

  const activeMethod: UniversalMetaMethod =
    UNIVERSAL_META_METHODS.find((m) => m.id === activeMethodId) || UNIVERSAL_META_METHODS[0];

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center p-2 sm:p-4 bg-black/60 backdrop-blur-xs font-body">
      <div className="bg-[var(--sheet)] border border-[var(--line)] rounded-[14px] w-full max-w-4xl max-h-[92vh] sm:max-h-[88vh] flex flex-col shadow-2xl overflow-hidden">
        {/* Header */}
        <div className="px-4 sm:px-6 py-3.5 bg-[var(--well)] border-b border-[var(--line)] flex items-center justify-between">
          <div className="flex items-center gap-2.5">
            <div className="p-1.5 rounded-[6px] bg-[var(--sheet)] text-[var(--purple)] border border-[var(--line)]">
              <Network className="w-4 h-4" />
            </div>
            <div>
              <div className="flex items-center gap-2">
                <h2 className="text-base font-display font-bold text-[var(--ink)] tracking-tight">
                  跨章节通用方法论矩阵 (Meta-Methods)
                </h2>
                <span className="text-[10px] font-mono px-1.5 py-0.2 rounded bg-[var(--sheet)] text-[var(--muted)] border border-[var(--line)] hidden sm:inline">
                  数一综合提分核心
                </span>
              </div>
              <p className="text-[11px] text-[var(--muted)] font-mono">
                穿透章节壁垒：同样的数学思想，在不同板块中如何演化与迁移
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

        {/* Content area */}
        <div className="flex-1 flex flex-col md:flex-row overflow-hidden">
          {/* Method selector tabs (Left on desktop, Top on mobile) */}
          <div className="w-full md:w-64 bg-[var(--well)] border-b md:border-b-0 md:border-r border-[var(--line)] p-2 sm:p-3 overflow-x-auto md:overflow-y-auto flex md:flex-col gap-1.5 flex-shrink-0 no-scrollbar">
            {UNIVERSAL_META_METHODS.map((m) => {
              const isSelected = m.id === activeMethodId;
              return (
                <button
                  key={m.id}
                  onClick={() => setActiveMethodId(m.id)}
                  className={`text-left p-2.5 sm:p-3 rounded-[10px] border transition-all flex-shrink-0 md:w-full ${
                    isSelected
                      ? 'bg-[var(--sheet)] border-[var(--purple)] shadow-xs'
                      : 'border-transparent hover:bg-[var(--sheet)] hover:border-[var(--line)] text-[var(--muted)]'
                  }`}
                >
                  <div className="text-xs font-bold text-[var(--ink)] font-display flex items-center justify-between">
                    <span>{m.name}</span>
                    <span className="text-[10px] font-mono px-1 rounded bg-[var(--well)] text-[var(--muted)] border border-[var(--line)] hidden md:inline">
                      {m.manifestations.length} 场景
                    </span>
                  </div>
                  <div className="text-[11px] font-mono text-[var(--purple)] mt-0.5 truncate">
                    {m.subtitle}
                  </div>
                </button>
              );
            })}
          </div>

          {/* Method detail panel */}
          <div className="flex-1 overflow-y-auto p-4 sm:p-6 space-y-5">
            {/* Core Philosophy Banner */}
            <div className="bg-[var(--well)] p-4 rounded-[12px] border-l-3 border-[var(--purple)] space-y-1.5">
              <div className="flex items-center gap-1.5 text-xs font-mono font-bold text-[var(--purple)]">
                <Lightbulb className="w-3.5 h-3.5" />
                <span>思想精髓与统一原则</span>
              </div>
              <p className="text-xs sm:text-sm text-[var(--ink)] leading-relaxed font-body">
                {activeMethod.corePhilosophy}
              </p>
            </div>

            {/* Manifestations across chapters */}
            <div className="space-y-3">
              <div className="flex items-center justify-between text-xs font-mono text-[var(--muted)]">
                <span className="font-bold text-[var(--ink)]">在各章节中的具体表现形态与触发点：</span>
                <span>收录 {activeMethod.manifestations.length} 个跨板块应用</span>
              </div>

              <div className="space-y-3">
                {activeMethod.manifestations.map((item, idx) => (
                  <div
                    key={idx}
                    className="bg-[var(--well)] border border-[var(--line)] hover:border-[var(--blue)] p-3.5 sm:p-4 rounded-[10px] space-y-2 transition-colors"
                  >
                    <div className="flex items-center justify-between pb-1.5 border-b border-[var(--line)]">
                      <div className="flex items-center gap-2 flex-wrap">
                        <span className="text-[10px] font-mono px-1.5 py-0.2 rounded bg-[var(--sheet)] text-[var(--muted)] border border-[var(--line)]">
                          {item.subjectName} · {item.chapterTitle}
                        </span>
                        <h4 className="text-xs font-bold text-[var(--ink)] font-display">
                          {item.topicTitle}
                        </h4>
                      </div>

                      <button
                        onClick={() => {
                          onSelectTopic(item.topicId);
                          onClose();
                        }}
                        className="flex items-center gap-1 text-xs font-mono text-[var(--blue)] hover:underline"
                      >
                        <span>去考点推导</span>
                        <ArrowRight className="w-3 h-3" />
                      </button>
                    </div>

                    <div className="grid grid-cols-1 sm:grid-cols-2 gap-2 text-xs">
                      <div className="bg-[var(--sheet)] p-2.5 rounded-[8px] border border-[var(--line)]">
                        <span className="text-[10px] font-mono text-[var(--amber)] font-bold">[触发形态]</span>
                        <div className="text-[var(--ink)] mt-1 font-body leading-relaxed">
                          <MathView content={item.triggerForm} inline />
                        </div>
                      </div>

                      <div className="bg-[var(--sheet)] p-2.5 rounded-[8px] border border-[var(--line)]">
                        <span className="text-[10px] font-mono text-[var(--green)] font-bold">[具体数学操作]</span>
                        <div className="text-[var(--ink)] mt-1 font-body leading-relaxed">
                          <MathView content={item.coreAction} inline />
                        </div>
                      </div>
                    </div>
                  </div>
                ))}
              </div>
            </div>

            {/* Pitfalls */}
            {activeMethod.commonPitfalls && activeMethod.commonPitfalls.length > 0 && (
              <div className="bg-[var(--sheet)] border border-[var(--red)]/40 p-4 rounded-[12px] space-y-2">
                <div className="flex items-center gap-1.5 text-xs font-mono font-bold text-[var(--red)]">
                  <AlertTriangle className="w-3.5 h-3.5" />
                  <span>跨章节迁移常见误区与避雷清单</span>
                </div>
                <ul className="space-y-1.5 text-xs text-[var(--ink)] font-body">
                  {activeMethod.commonPitfalls.map((pf, i) => (
                    <li key={i} className="flex items-start gap-1.5">
                      <span className="text-[var(--red)] font-mono font-bold">•</span>
                      <span className="leading-relaxed"><MathView content={pf} inline /></span>
                    </li>
                  ))}
                </ul>
              </div>
            )}
          </div>
        </div>
      </div>
    </div>
  );
};
