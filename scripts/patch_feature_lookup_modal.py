with open('src/components/FeatureLookupModal.tsx', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Update Props
old_props = """interface FeatureLookupModalProps {
  isOpen: boolean;
  onClose: () => void;
  onSelectTopic: (topicId: string) => void;
}"""

new_props = """interface FeatureLookupModalProps {
  isOpen: boolean;
  onClose: () => void;
  onSelectTopic: (topicId: string) => void;
  onSelectMetaMethod?: (metaMethodId: string) => void;
}"""

text = text.replace(old_props, new_props)

# 2. Update Component Arguments
old_args = """export const FeatureLookupModal: React.FC<FeatureLookupModalProps> = ({
  isOpen,
  onClose,
  onSelectTopic,
}) => {"""

new_args = """export const FeatureLookupModal: React.FC<FeatureLookupModalProps> = ({
  isOpen,
  onClose,
  onSelectTopic,
  onSelectMetaMethod,
}) => {"""

text = text.replace(old_args, new_args)

# 3. Update Universal Method Badge in matrix card
old_badge = """                            {item.metaMethodName && (
                              <span className="text-[9px] font-mono px-1.5 py-0.2 rounded bg-[var(--purple-bg)]/30 text-[var(--purple)] border border-[var(--purple)]/40 font-bold flex items-center gap-0.5">
                                <Layers className="w-2.5 h-2.5 text-[var(--purple)]" />
                                通用方法: {item.metaMethodName}
                              </span>
                            )}"""

new_badge = """                            {item.metaMethodName && (
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
                            )}"""

text = text.replace(old_badge, new_badge)

# 4. MathView for keyReaction and answer in examples
old_ex_render = """                                  <div className="p-2 rounded bg-[var(--blue-bg)] text-[var(--blue)] border border-[var(--blue)]">
                                    <span className="font-bold">[特征突破口]: </span>
                                    <span>{ex.keyReaction}</span>
                                  </div>
                                  <div className="p-2 rounded bg-[var(--green-bg)] text-[var(--green)] border border-[var(--green)]">
                                    <span className="font-bold">[参考答案]: </span>
                                    <span>{ex.answer}</span>
                                  </div>"""

new_ex_render = """                                  <div className="p-2 rounded bg-[var(--blue-bg)] text-[var(--blue)] border border-[var(--blue)]">
                                    <span className="font-bold">[特征突破口]: </span>
                                    <span><MathView content={ex.keyReaction} inline /></span>
                                  </div>
                                  <div className="p-2 rounded bg-[var(--green-bg)] text-[var(--green)] border border-[var(--green)]">
                                    <span className="font-bold">[参考答案]: </span>
                                    <span><MathView content={ex.answer} inline /></span>
                                  </div>"""

text = text.replace(old_ex_render, new_ex_render)

# 5. Flashcard back: add Universal Method link if available
old_flashcard_topic = """                          <div className="mt-2 pt-2 border-t border-[var(--line)] flex items-center justify-between text-[11px] font-mono">
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
                          </div>"""

new_flashcard_topic = """                          <div className="mt-2 pt-2 border-t border-[var(--line)] flex items-center justify-between text-[11px] font-mono">
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
                          )}"""

text = text.replace(old_flashcard_topic, new_flashcard_topic)

with open('src/components/FeatureLookupModal.tsx', 'w', encoding='utf-8') as f:
    f.write(text)

print("Updated FeatureLookupModal.tsx successfully!")
