import { KNOWLEDGE_BASE } from '../src/data/knowledgeBase';
import { EXTRACTED_PAST_QUESTIONS } from '../src/data/pastQuestionsData';

const questions2021_2026: any[] = [];

function checkQ(q: any, source: string, topicId: string) {
  const y = parseInt(q.year);
  if (y >= 2021 && y <= 2026) {
    questions2021_2026.push({ q, source, topicId });
  }
}

for (const [nid, node] of Object.entries(KNOWLEDGE_BASE)) {
  for (const q of node.pastQuestions || []) {
    checkQ(q, 'KB', nid);
  }
}

for (const [nid, qlist] of Object.entries(EXTRACTED_PAST_QUESTIONS)) {
  for (const q of qlist) {
    checkQ(q, 'EXTRACTED', nid);
  }
}

console.log(`Total 2021-2026 questions: ${questions2021_2026.length}`);

// Breakdown by year and category
const byYearCat: Record<string, number> = {};
for (const item of questions2021_2026) {
  const key = `${item.q.year} ${item.q.category}`;
  byYearCat[key] = (byYearCat[key] || 0) + 1;
}

console.log('\nBreakdown:');
Object.entries(byYearCat).sort().forEach(([k, v]) => console.log(`  ${k}: ${v}`));
