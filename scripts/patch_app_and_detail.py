# 1. Update KnowledgeDetailView.tsx
with open('src/components/KnowledgeDetailView.tsx', 'r', encoding='utf-8') as f:
    text = f.read()

# Add Layers to lucide-react import
text = text.replace(
    "import { \n  ArrowLeft, ArrowRight, ChevronLeft, Compass, Eye, EyeOff, Tag, CheckCircle2, Bookmark\n} from 'lucide-react';",
    "import { \n  ArrowLeft, ArrowRight, ChevronLeft, Compass, Eye, EyeOff, Tag, CheckCircle2, Bookmark, Layers\n} from 'lucide-react';"
)
# In case it has single line import
text = text.replace(
    "import { ArrowLeft, ArrowRight, ChevronLeft, Compass, Eye, EyeOff, Tag, CheckCircle2, Bookmark } from 'lucide-react';",
    "import { ArrowLeft, ArrowRight, ChevronLeft, Compass, Eye, EyeOff, Tag, CheckCircle2, Bookmark, Layers } from 'lucide-react';"
)

# Import TOPIC_TO_META_METHOD
if 'TOPIC_TO_META_METHOD' not in text:
    text = text.replace(
        "import { KNOWLEDGE_BASE } from '../data/knowledgeBase';",
        "import { KNOWLEDGE_BASE } from '../data/knowledgeBase';\nimport { TOPIC_TO_META_METHOD } from '../data/featureIndex';"
    )

# Add onOpenMetaMethod to KnowledgeDetailViewProps
old_props = """interface KnowledgeDetailViewProps {
  nodeId: string;
  onBackToChapter: (chapterId: string) => void;
  onBackToMindmap: () => void;
  onNavigateTopic: (nodeId: string) => void;
}"""

new_props = """interface KnowledgeDetailViewProps {
  nodeId: string;
  onBackToChapter: (chapterId: string) => void;
  onBackToMindmap: () => void;
  onNavigateTopic: (nodeId: string) => void;
  onOpenMetaMethod?: (metaMethodId: string) => void;
}"""

text = text.replace(old_props, new_props)

# Update component signature
old_sig = """export const KnowledgeDetailView: React.FC<KnowledgeDetailViewProps> = ({
  nodeId,
  onBackToChapter,
  onBackToMindmap,
  onNavigateTopic,
}) => {"""

new_sig = """export const KnowledgeDetailView: React.FC<KnowledgeDetailViewProps> = ({
  nodeId,
  onBackToChapter,
  onBackToMindmap,
  onNavigateTopic,
  onOpenMetaMethod,
}) => {"""

text = text.replace(old_sig, new_sig)

# Add Universal Meta-Method banner in title card
old_title_area = """          <h1 className="text-xl sm:text-2xl md:text-3xl font-display font-bold text-[var(--ink)] tracking-tight">
            {node.title}
          </h1>"""

new_title_area = """          <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-2">
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

text = text.replace(old_title_area, new_title_area)

with open('src/components/KnowledgeDetailView.tsx', 'w', encoding='utf-8') as f:
    f.write(text)

print("Updated KnowledgeDetailView.tsx successfully!")

# 2. Update App.tsx
with open('src/App.tsx', 'r', encoding='utf-8') as f:
    app_text = f.read()

# Add selectedMetaMethodId state
old_app_states = """  const [isReviewOpen, setIsReviewOpen] = useState(false);
  const [isFeatureLookupOpen, setIsFeatureLookupOpen] = useState(false);
  const [isMetaMethodOpen, setIsMetaMethodOpen] = useState(false);"""

new_app_states = """  const [isReviewOpen, setIsReviewOpen] = useState(false);
  const [isFeatureLookupOpen, setIsFeatureLookupOpen] = useState(false);
  const [isMetaMethodOpen, setIsMetaMethodOpen] = useState(false);
  const [selectedMetaMethodId, setSelectedMetaMethodId] = useState<string | undefined>(undefined);"""

app_text = app_text.replace(old_app_states, new_app_states)

# Navbar onOpenMetaMethods
app_text = app_text.replace(
    "onOpenMetaMethods={() => setIsMetaMethodOpen(true)}",
    "onOpenMetaMethods={() => { setSelectedMetaMethodId(undefined); setIsMetaMethodOpen(true); }}"
)

# KnowledgeDetailView onOpenMetaMethod
old_k_view = """        {route.type === 'knowledge' && (
          <KnowledgeDetailView
            nodeId={route.nodeId}
            onBackToChapter={(cid) => navigateToChapter(cid)}
            onBackToMindmap={() => navigateToMindmap()}
            onNavigateTopic={(tid) => navigateToTopic(tid)}
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
          />
        )}"""

app_text = app_text.replace(old_k_view, new_k_view)

# FeatureLookupModal & MetaMethodModal wiring
old_modals = """      {/* Feature Matrix & Active Recall Flashcards Modal */}
      <FeatureLookupModal
        isOpen={isFeatureLookupOpen}
        onClose={() => setIsFeatureLookupOpen(false)}
        onSelectTopic={(tid) => navigateToTopic(tid)}
      />

      {/* Universal Cross-Chapter Meta-Methods Matrix Modal */}
      <MetaMethodModal
        isOpen={isMetaMethodOpen}
        onClose={() => setIsMetaMethodOpen(false)}
        onSelectTopic={(tid) => navigateToTopic(tid)}
      />"""

new_modals = """      {/* Feature Matrix & Active Recall Flashcards Modal */}
      <FeatureLookupModal
        isOpen={isFeatureLookupOpen}
        onClose={() => setIsFeatureLookupOpen(false)}
        onSelectTopic={(tid) => navigateToTopic(tid)}
        onSelectMetaMethod={(mid) => {
          setIsFeatureLookupOpen(false);
          setSelectedMetaMethodId(mid);
          setIsMetaMethodOpen(true);
        }}
      />

      {/* Universal Cross-Chapter Meta-Methods Matrix Modal */}
      <MetaMethodModal
        isOpen={isMetaMethodOpen}
        onClose={() => setIsMetaMethodOpen(false)}
        onSelectTopic={(tid) => navigateToTopic(tid)}
        initialMethodId={selectedMetaMethodId}
        onOpenFeatureLookup={() => {
          setIsMetaMethodOpen(false);
          setIsFeatureLookupOpen(true);
        }}
      />"""

app_text = app_text.replace(old_modals, new_modals)

with open('src/App.tsx', 'w', encoding='utf-8') as f:
    f.write(app_text)

print("Updated App.tsx successfully!")
