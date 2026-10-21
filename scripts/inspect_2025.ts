import { KNOWLEDGE_BASE } from '../src/data/knowledgeBase';

for (const [nid, node] of Object.entries(KNOWLEDGE_BASE)) {
  for (const q of node.pastQuestions || []) {
    if (q.id === 'q-2025-1-12' || q.id === 'q-2025-1-22') {
      console.log('--- ' + q.id + ' in ' + nid + ' ---');
      console.log('CONTENT:\n', q.content);
    }
  }
}
