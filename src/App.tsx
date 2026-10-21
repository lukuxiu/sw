import React, { useState, useEffect } from 'react';
import { Navbar } from './components/Navbar';
import { MindmapView } from './components/MindmapView';
import { ChapterView } from './components/ChapterView';
import { KnowledgeDetailView } from './components/KnowledgeDetailView';
import { ReviewModal } from './components/ReviewModal';
import { FeatureLookupModal } from './components/FeatureLookupModal';
import { MetaMethodModal } from './components/MetaMethodModal';
import { CHAPTERS } from './data/subjects';
import { KNOWLEDGE_BASE } from './data/knowledgeBase';

type RouteState =
  | { type: 'mindmap'; highlightTopicId?: string }
  | { type: 'chapter'; chapterId: string; initialTopicId?: string }
  | { type: 'knowledge'; nodeId: string };

export function App() {
  const [route, setRoute] = useState<RouteState>({ type: 'mindmap' });
  const [isReviewOpen, setIsReviewOpen] = useState(false);
  const [isFeatureLookupOpen, setIsFeatureLookupOpen] = useState(false);
  const [isMetaMethodOpen, setIsMetaMethodOpen] = useState(false);
  const [selectedMetaMethodId, setSelectedMetaMethodId] = useState<string | undefined>(undefined);

  // Parse hash to route
  const parseHash = (): RouteState => {
    const hash = window.location.hash.slice(1); // remove '#'
    if (!hash || hash === '/') {
      return { type: 'mindmap' };
    }

    if (hash.startsWith('/chapter/')) {
      const chapterId = hash.replace('/chapter/', '');
      if (CHAPTERS[chapterId]) {
        return { type: 'chapter', chapterId };
      }
    }

    if (hash.startsWith('/knowledge/')) {
      const nodeId = hash.replace('/knowledge/', '');
      if (KNOWLEDGE_BASE[nodeId]) {
        return { type: 'knowledge', nodeId };
      }
    }

    return { type: 'mindmap' };
  };

  // Global keyboard shortcuts (Esc to close modals, / or Ctrl+K to search)
  useEffect(() => {
    const handleKeyDown = (e: KeyboardEvent) => {
      if (e.key === 'Escape') {
        if (isReviewOpen || isFeatureLookupOpen || isMetaMethodOpen) {
          setIsReviewOpen(false);
          setIsFeatureLookupOpen(false);
          setIsMetaMethodOpen(false);
        }
        return;
      }

      // Check if user is typing in an editable field
      const activeTag = (document.activeElement?.tagName || '').toLowerCase();
      const isInputFocused = activeTag === 'input' || activeTag === 'textarea';

      if (!isInputFocused) {
        if (e.key === '/' || ((e.ctrlKey || e.metaKey) && e.key.toLowerCase() === 'k')) {
          e.preventDefault();
          const searchInput = document.getElementById('global-search-input') as HTMLInputElement | null;
          if (searchInput) {
            searchInput.focus();
            searchInput.select();
          }
        }
      }
    };

    window.addEventListener('keydown', handleKeyDown);
    return () => window.removeEventListener('keydown', handleKeyDown);
  }, [isReviewOpen, isFeatureLookupOpen, isMetaMethodOpen]);

  // Sync hash on initial mount and hashchange event
  useEffect(() => {
    const initialRoute = parseHash();
    setRoute(initialRoute);

    const handleHashChange = () => {
      setRoute(parseHash());
    };

    window.addEventListener('hashchange', handleHashChange);
    return () => window.removeEventListener('hashchange', handleHashChange);
  }, []);

  // Navigation handlers
  const navigateToMindmap = (highlightTopicId?: string) => {
    window.location.hash = '#/';
    setRoute({ type: 'mindmap', highlightTopicId });
  };

  const navigateToChapter = (chapterId: string, initialTopicId?: string) => {
    window.location.hash = `#/chapter/${chapterId}`;
    setRoute({ type: 'chapter', chapterId, initialTopicId });
  };

  const navigateToTopic = (nodeId: string) => {
    window.location.hash = `#/knowledge/${nodeId}`;
    setRoute({ type: 'knowledge', nodeId });
  };

  return (
    <div className="min-h-screen bg-[var(--paper)] text-[var(--ink)] flex flex-col font-body">
      {/* Global Navbar */}
      <Navbar
        onNavigateMindmap={() => navigateToMindmap()}
        onNavigateChapter={(cid) => navigateToChapter(cid)}
        onNavigateTopic={(tid) => navigateToTopic(tid)}
        onOpenReviewModal={() => setIsReviewOpen(true)}
        onOpenFeatureLookup={() => setIsFeatureLookupOpen(true)}
        onOpenMetaMethods={() => { setSelectedMetaMethodId(undefined); setIsMetaMethodOpen(true); }}
      />

      {/* Main View Area */}
      <main className="flex-1 flex flex-col">
        {route.type === 'mindmap' && (
          <MindmapView
            onSelectChapter={(cid) => navigateToChapter(cid)}
            onSelectTopic={(tid) => navigateToTopic(tid)}
            highlightTopicId={route.highlightTopicId}
          />
        )}

        {route.type === 'chapter' && (
          <ChapterView
            chapterId={route.chapterId}
            onBackToMindmap={() => navigateToMindmap()}
            onSelectTopic={(tid) => navigateToTopic(tid)}
            initialTopicId={route.initialTopicId}
          />
        )}

        {route.type === 'knowledge' && (
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
        )}
      </main>

      {/* Review Hub Modal (With Export/Import & Ebbinghaus Time Sorting) */}
      <ReviewModal
        isOpen={isReviewOpen}
        onClose={() => setIsReviewOpen(false)}
        onSelectTopic={(tid) => navigateToTopic(tid)}
      />

      {/* Feature Matrix & Active Recall Flashcards Modal */}
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
      />
    </div>
  );
}

export default App;
