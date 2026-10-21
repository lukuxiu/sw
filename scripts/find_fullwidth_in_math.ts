import { KNOWLEDGE_BASE } from '../src/data/knowledgeBase';

for (const [nid, node] of Object.entries(KNOWLEDGE_BASE)) {
  for (const q of node.pastQuestions || []) {
    const text = q.content || '';
    const formulaRegex = /\$([^\$]+?)\$/g;
    let match;
    while ((match = formulaRegex.exec(text)) !== null) {
      if (match[1].includes('（') || match[1].includes('）')) {
        console.log(`Found in ${q.id} in ${nid}:`, match[1]);
      }
    }
  }
}
