with open('src/components/KnowledgeDetailView.tsx', 'r', encoding='utf-8') as f:
    k_text = f.read()

# 1. Import BookOpen and TOPIC_TO_LECTURE
k_text = k_text.replace(
    "import { TOPIC_TO_META_METHOD } from '../data/featureIndex';",
    "import { TOPIC_TO_META_METHOD } from '../data/featureIndex';\nimport { TOPIC_TO_LECTURE } from '../data/makiLectures';"
)

k_text = k_text.replace(
    "  ArrowLeft, ArrowRight, ChevronLeft, Compass, Eye, EyeOff, Tag, CheckCircle2, Bookmark, Layers\n} from 'lucide-react';",
    "  ArrowLeft, ArrowRight, ChevronLeft, Compass, Eye, EyeOff, Tag, CheckCircle2, Bookmark, Layers, BookOpen\n} from 'lucide-react';"
)

# 2. Props
old_props = """interface KnowledgeDetailViewProps {
  nodeId: string;
  onBackToChapter: (chapterId: string) => void;
  onBackToMindmap: () => void;
  onNavigateTopic: (nodeId: string) => void;
  onOpenMetaMethod?: (metaMethodId: string) => void;
}"""

new_props = """interface KnowledgeDetailViewProps {
  nodeId: string;
  onBackToChapter: (chapterId: string) => void;
  onBackToMindmap: () => void;
  onNavigateTopic: (nodeId: string) => void;
  onOpenMetaMethod?: (metaMethodId: string) => void;
  onOpenMakiLecture?: (lectureId: string) => void;
}"""

k_text = k_text.replace(old_props, new_props)

old_sig = """export const KnowledgeDetailView: React.FC<KnowledgeDetailViewProps> = ({
  nodeId,
  onBackToChapter,
  onBackToMindmap,
  onNavigateTopic,
  onOpenMetaMethod,
}) => {"""

new_sig = """export const KnowledgeDetailView: React.FC<KnowledgeDetailViewProps> = ({
  nodeId,
  onBackToChapter,
  onBackToMindmap,
  onNavigateTopic,
  onOpenMetaMethod,
  onOpenMakiLecture,
}) => {"""

k_text = k_text.replace(old_sig, new_sig)

# 3. Badge area
old_title_badge = """          <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-2">
            <h1 className="text-xl sm:text-2xl md:text-3xl font-display font-bold text-[var(--ink)] tracking-tight">
              {node.title}
            </h1>
            {TOPIC_TO_META_METHOD[node.id] && onOpenMetaMethod && (
              <button
                type="button"
                onClick={() => onOpenMetaMethod(TOPIC_TO_META_METHOD[node.id].id)}
                className="inline-flex items-center gap-1.5 px-3 py-1.5 rounded-[8px] bg-[var(--purple-bg)]/30 text-[var(--purple)] border border-[var(--purple)]/40 hover:bg-[var(--purple)] hover:text-white transition-colors cursor-pointer text-xs font-mono font-bold self-start sm:self-auto"
                title="查看该考点对应跨章节通用方法的完整矩阵与历年例题"
              >
                <Layers className="w-3.5 h-3.5" />
                <span>通用方法：{TOPIC_TO_META_METHOD[node.id].name} ↗</span>
              </button>
            )}
          </div>"""

new_title_badge = """          <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-2">
            <h1 className="text-xl sm:text-2xl md:text-3xl font-display font-bold text-[var(--ink)] tracking-tight">
              {node.title}
            </h1>
            <div className="flex items-center gap-1.5 flex-wrap self-start sm:self-auto">
              {TOPIC_TO_LECTURE[node.id] && onOpenMakiLecture && (
                <button
                  type="button"
                  onClick={() => onOpenMakiLecture(TOPIC_TO_LECTURE[node.id].lectureId)}
                  className="inline-flex items-center gap-1.5 px-2.5 py-1.5 rounded-[8px] bg-[var(--well)] hover:bg-[var(--sheet)] text-[var(--ink)] border border-[var(--purple)]/40 hover:border-[var(--purple)] transition-colors cursor-pointer text-xs font-mono font-bold shadow-xs"
                  title="查看 Maki 大串讲中本讲的完整定位、考频面板与方法卡"
                >
                  <BookOpen className="w-3.5 h-3.5 text-[var(--purple)]" />
                  <span>{TOPIC_TO_LECTURE[node.id].lectureId} {TOPIC_TO_LECTURE[node.id].lectureTitle} ↗</span>
                </button>
              )}
              {TOPIC_TO_META_METHOD[node.id] && onOpenMetaMethod && (
                <button
                  type="button"
                  onClick={() => onOpenMetaMethod(TOPIC_TO_META_METHOD[node.id].id)}
                  className="inline-flex items-center gap-1.5 px-2.5 py-1.5 rounded-[8px] bg-[var(--purple-bg)]/30 text-[var(--purple)] border border-[var(--purple)]/40 hover:bg-[var(--purple)] hover:text-white transition-colors cursor-pointer text-xs font-mono font-bold"
                  title="查看该考点对应跨章节通用方法的完整矩阵与历年例题"
                >
                  <Layers className="w-3.5 h-3.5" />
                  <span>通用方法：{TOPIC_TO_META_METHOD[node.id].name} ↗</span>
                </button>
              )}
            </div>
          </div>"""

k_text = k_text.replace(old_title_badge, new_title_badge)

with open('src/components/KnowledgeDetailView.tsx', 'w', encoding='utf-8') as f:
    f.write(k_text)

print("Updated KnowledgeDetailView.tsx with Maki Lecture badge!")

# 4. Update App.tsx
with open('src/App.tsx', 'r', encoding='utf-8') as f:
    app_text = f.read()

# Import MakiLecturesModal
if 'MakiLecturesModal' not in app_text:
    app_text = app_text.replace(
        "import { MetaMethodModal } from './components/MetaMethodModal';",
        "import { MetaMethodModal } from './components/MetaMethodModal';\nimport { MakiLecturesModal } from './components/MakiLecturesModal';"
    )

# Add isMakiLecturesOpen state
old_app_states = """  const [isReviewOpen, setIsReviewOpen] = useState(false);
  const [isFeatureLookupOpen, setIsFeatureLookupOpen] = useState(false);
  const [isMetaMethodOpen, setIsMetaMethodOpen] = useState(false);
  const [selectedMetaMethodId, setSelectedMetaMethodId] = useState<string | undefined>(undefined);"""

new_app_states = """  const [isReviewOpen, setIsReviewOpen] = useState(false);
  const [isFeatureLookupOpen, setIsFeatureLookupOpen] = useState(false);
  const [isMetaMethodOpen, setIsMetaMethodOpen] = useState(false);
  const [selectedMetaMethodId, setSelectedMetaMethodId] = useState<string | undefined>(undefined);
  const [isMakiLecturesOpen, setIsMakiLecturesOpen] = useState(false);
  const [selectedLectureId, setSelectedLectureId] = useState<string | undefined>(undefined);"""

app_text = app_text.replace(old_app_states, new_app_states)

# Handle escape
app_text = app_text.replace(
    "if (isReviewOpen || isFeatureLookupOpen || isMetaMethodOpen) {",
    "if (isReviewOpen || isFeatureLookupOpen || isMetaMethodOpen || isMakiLecturesOpen) {\n          setIsMakiLecturesOpen(false);"
)
app_text = app_text.replace(
    "[isReviewOpen, isFeatureLookupOpen, isMetaMethodOpen]",
    "[isReviewOpen, isFeatureLookupOpen, isMetaMethodOpen, isMakiLecturesOpen]"
)

# Navbar props
app_text = app_text.replace(
    "onOpenMetaMethods={() => { setSelectedMetaMethodId(undefined); setIsMetaMethodOpen(true); }}\n      />",
    "onOpenMetaMethods={() => { setSelectedMetaMethodId(undefined); setIsMetaMethodOpen(true); }}\n        onOpenMakiLectures={() => { setSelectedLectureId(undefined); setIsMakiLecturesOpen(true); }}\n      />"
)

# KnowledgeDetailView onOpenMakiLecture
old_k_view = """        {route.type === 'knowledge' && (
          <KnowledgeDetailView
            nodeId={route.nodeId}
            onBackToChapter={(cid) => navigateToChapter(cid)}
            onBackToMindmap={() => navigateToMindmap()}
            onNavigateTopic={(tid) => navigateToTopic(tid)}
            onOpenMetaMethod={(mid) => {
              setSelectedMetaMethodId(mid);
              setIsMetaMethodOpen(true);
            }}
          />
        )}"""

new_k_view = """        {route.type === 'knowledge' && (
          <KnowledgeDetailView
            nodeId={route.nodeId}
            onBackToChapter={(cid) => navigateToChapter(cid)}
            onBackToMindmap={() => navigateToMindmap()}
            onNavigateTopic={(tid) => navigateToTopic(tid)}
            onOpenMetaMethod={(mid) => {
              setSelectedMetaMethodId(mid);
              setIsMetaMethodOpen(true);
            }}
            onOpenMakiLecture={(lid) => {
              setSelectedLectureId(lid);
              setIsMakiLecturesOpen(true);
            }}
          />
        )}"""

app_text = app_text.replace(old_k_view, new_k_view)

# Render MakiLecturesModal
old_modals_end = """      {/* Universal Cross-Chapter Meta-Methods Matrix Modal */}
      <MetaMethodModal
        isOpen={isMetaMethodOpen}
        onClose={() => setIsMetaMethodOpen(false)}
        onSelectTopic={(tid) => navigateToTopic(tid)}
        initialMethodId={selectedMetaMethodId}
        onOpenFeatureLookup={() => {
          setIsMetaMethodOpen(false);
          setIsFeatureLookupOpen(true);
        }}
      />
    </div>"""

new_modals_end = """      {/* Universal Cross-Chapter Meta-Methods Matrix Modal */}
      <MetaMethodModal
        isOpen={isMetaMethodOpen}
        onClose={() => setIsMetaMethodOpen(false)}
        onSelectTopic={(tid) => navigateToTopic(tid)}
        initialMethodId={selectedMetaMethodId}
        onOpenFeatureLookup={() => {
          setIsMetaMethodOpen(false);
          setIsFeatureLookupOpen(true);
        }}
      />

      {/* Maki 66 Lectures Directory & War Map Modal */}
      <MakiLecturesModal
        isOpen={isMakiLecturesOpen}
        onClose={() => setIsMakiLecturesOpen(false)}
        onSelectTopic={(tid) => navigateToTopic(tid)}
        initialLectureId={selectedLectureId}
      />
    </div>"""

app_text = app_text.replace(old_modals_end, new_modals_end)

with open('src/App.tsx', 'w', encoding='utf-8') as f:
    f.write(app_text)

print("Updated App.tsx with MakiLecturesModal successfully!")
