import re

# 1. Update MindmapView.tsx
with open('src/components/MindmapView.tsx', 'r', encoding='utf-8') as f:
    mv = f.read().replace('\r\n', '\n')

mv = mv.replace(
    "EyeOff\n} from 'lucide-react';",
    "EyeOff, BookOpen\n} from 'lucide-react';"
)
mv = mv.replace(
    "import { getAllLearningStatuses } from '../data/storage';",
    "import { getAllLearningStatuses } from '../data/storage';\nimport { TOPIC_TO_LECTURE } from '../data/makiLectures';"
)
mv = mv.replace(
    "  highlightTopicId?: string;\n}",
    "  highlightTopicId?: string;\n  onOpenMakiLecture?: (lectureId?: string) => void;\n}"
)
mv = mv.replace(
    "  highlightTopicId,\n}) => {",
    "  highlightTopicId,\n  onOpenMakiLecture,\n}) => {"
)

# Canvas mode badge
old_canvas_t = """                                                  <span className="text-xs font-semibold text-[var(--ink)] hover:text-[var(--blue)]">
                                                    {t.title}
                                                  </span>"""
new_canvas_t = """                                                  <span className="text-xs font-semibold text-[var(--ink)] hover:text-[var(--blue)]">
                                                    {t.title}
                                                  </span>
                                                  {TOPIC_TO_LECTURE[t.id] && (
                                                    <button
                                                      type="button"
                                                      onClick={(e) => {
                                                        e.stopPropagation();
                                                        onOpenMakiLecture?.(TOPIC_TO_LECTURE[t.id].lectureId);
                                                      }}
                                                      className="inline-flex items-center gap-0.5 text-[9.5px] font-mono px-1 py-0.2 rounded bg-purple-50 text-purple-700 dark:bg-purple-950/40 dark:text-purple-300 border border-purple-200 dark:border-purple-800 hover:bg-purple-100 dark:hover:bg-purple-900 transition-colors"
                                                      title={`对应大串讲 ${TOPIC_TO_LECTURE[t.id].lectureId} ${TOPIC_TO_LECTURE[t.id].lectureTitle}`}
                                                    >
                                                      <span>{TOPIC_TO_LECTURE[t.id].lectureId}</span>
                                                      <span className="opacity-70 text-[8px]">↗</span>
                                                    </button>
                                                  )}"""
assert old_canvas_t in mv, "old_canvas_t not found in MindmapView"
mv = mv.replace(old_canvas_t, new_canvas_t)

# Outline mode badge
old_outline_t = """                                  <div className="flex items-center justify-between gap-1">
                                    <span className="text-xs font-semibold text-[var(--ink)]">
                                      {t.title}
                                    </span>"""
new_outline_t = """                                  <div className="flex items-center justify-between gap-1">
                                    <div className="flex items-center gap-1.5 flex-wrap">
                                      <span className="text-xs font-semibold text-[var(--ink)]">
                                        {t.title}
                                      </span>
                                      {TOPIC_TO_LECTURE[t.id] && (
                                        <button
                                          type="button"
                                          onClick={(e) => {
                                            e.stopPropagation();
                                            onOpenMakiLecture?.(TOPIC_TO_LECTURE[t.id].lectureId);
                                          }}
                                          className="inline-flex items-center gap-0.5 text-[9.5px] font-mono px-1 py-0.2 rounded bg-purple-50 text-purple-700 dark:bg-purple-950/40 dark:text-purple-300 border border-purple-200 dark:border-purple-800 hover:bg-purple-100 dark:hover:bg-purple-900 transition-colors"
                                          title={`大串讲 ${TOPIC_TO_LECTURE[t.id].lectureId} ${TOPIC_TO_LECTURE[t.id].lectureTitle}`}
                                        >
                                          <span>{TOPIC_TO_LECTURE[t.id].lectureId}</span>
                                          <span className="opacity-70 text-[8px]">↗</span>
                                        </button>
                                      )}
                                    </div>"""
assert old_outline_t in mv, "old_outline_t not found in MindmapView"
mv = mv.replace(old_outline_t, new_outline_t)

with open('src/components/MindmapView.tsx', 'w', encoding='utf-8', newline='\n') as f:
    f.write(mv)
print("MindmapView updated successfully!")

# 2. Update ChapterView.tsx
with open('src/components/ChapterView.tsx', 'r', encoding='utf-8') as f:
    cv = f.read().replace('\r\n', '\n')

cv = cv.replace(
    "ChevronDown, ChevronUp\n} from 'lucide-react';",
    "ChevronDown, ChevronUp, BookOpen\n} from 'lucide-react';"
)
cv = cv.replace(
    "import { getChapterProgress, setLearningStatus } from '../data/storage';",
    "import { getChapterProgress, setLearningStatus } from '../data/storage';\nimport { TOPIC_TO_LECTURE } from '../data/makiLectures';"
)
cv = cv.replace(
    "  initialTopicId?: string;\n}",
    "  initialTopicId?: string;\n  onOpenMakiLecture?: (lectureId: string) => void;\n}"
)
cv = cv.replace(
    "  initialTopicId,\n}) => {",
    "  initialTopicId,\n  onOpenMakiLecture,\n}) => {"
)

# Left list badge
old_list_t = """                        <div className="flex items-center gap-1.5 flex-wrap">
                          <h4 className={`text-xs font-semibold ${isSelected ? 'text-[var(--blue)]' : 'text-[var(--ink)]'}`}>
                            {t.title}
                          </h4>"""
new_list_t = """                        <div className="flex items-center gap-1.5 flex-wrap">
                          <h4 className={`text-xs font-semibold ${isSelected ? 'text-[var(--blue)]' : 'text-[var(--ink)]'}`}>
                            {t.title}
                          </h4>
                          {TOPIC_TO_LECTURE[t.id] && (
                            <button
                              type="button"
                              onClick={(e) => {
                                e.stopPropagation();
                                onOpenMakiLecture?.(TOPIC_TO_LECTURE[t.id].lectureId);
                              }}
                              className="inline-flex items-center gap-0.5 text-[9.5px] font-mono px-1 py-0.2 rounded bg-purple-50 text-purple-700 dark:bg-purple-950/40 dark:text-purple-300 border border-purple-200 dark:border-purple-800 hover:bg-purple-100 dark:hover:bg-purple-900 transition-colors"
                              title={`大串讲 ${TOPIC_TO_LECTURE[t.id].lectureId} ${TOPIC_TO_LECTURE[t.id].lectureTitle}`}
                            >
                              <span>{TOPIC_TO_LECTURE[t.id].lectureId}</span>
                              <span className="opacity-70 text-[8px]">↗</span>
                            </button>
                          )}"""
assert old_list_t in cv, "old_list_t not found in ChapterView"
cv = cv.replace(old_list_t, new_list_t)

# Right header lecture link
old_right_hdr = """                  <p className="text-xs font-mono text-[var(--muted)] mt-1">
                    所属章节：{activeTopic.chapterTitle}
                  </p>"""
new_right_hdr = """                  <div className="flex items-center gap-2 mt-1 flex-wrap text-xs font-mono text-[var(--muted)]">
                    <span>所属章节：{activeTopic.chapterTitle}</span>
                    {TOPIC_TO_LECTURE[activeTopic.id] && (
                      <>
                        <span>•</span>
                        <button
                          type="button"
                          onClick={() => onOpenMakiLecture?.(TOPIC_TO_LECTURE[activeTopic.id].lectureId)}
                          className="inline-flex items-center gap-1 text-purple-700 dark:text-purple-300 hover:underline"
                        >
                          <BookOpen className="w-3 h-3" />
                          <span>对应大串讲：{TOPIC_TO_LECTURE[activeTopic.id].lectureId} {TOPIC_TO_LECTURE[activeTopic.id].lectureTitle} ↗</span>
                        </button>
                      </>
                    )}
                  </div>"""
assert old_right_hdr in cv, "old_right_hdr not found in ChapterView"
cv = cv.replace(old_right_hdr, new_right_hdr)

with open('src/components/ChapterView.tsx', 'w', encoding='utf-8', newline='\n') as f:
    f.write(cv)
print("ChapterView updated successfully!")
