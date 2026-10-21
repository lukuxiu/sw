import { KNOWLEDGE_BASE } from '../src/data/knowledgeBase';
import { EXTRACTED_PAST_QUESTIONS } from '../src/data/pastQuestionsData';

const qMap = new Map<string, any>();
for (const [nid, node] of Object.entries(KNOWLEDGE_BASE)) {
  for (const q of node.pastQuestions || []) qMap.set(q.id, q);
}
for (const [nid, qlist] of Object.entries(EXTRACTED_PAST_QUESTIONS)) {
  for (const q of qlist) if (!qMap.has(q.id)) qMap.set(q.id, q);
}

const makiYearDist: Record<string, number> = {};
for (const [id, q] of qMap.entries()) {
  if (/^q-\d{4}-\d+-\d+-\d+\.\d+$/.test(id)) {
    const y = q.year || 'unknown';
    makiYearDist[y] = (makiYearDist[y] || 0) + 1;
  }
}

console.log('Maki PDF extracted questions year distribution:');
Object.entries(makiYearDist).sort().forEach(([y, c]) => console.log(`  ${y}: ${c}`));
