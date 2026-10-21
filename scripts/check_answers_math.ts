import { KNOWLEDGE_BASE } from '../src/data/knowledgeBase';
import { EXTRACTED_PAST_QUESTIONS } from '../src/data/pastQuestionsData';

const nonLetterAnswers: any[] = [];

function checkAns(q: any, src: string, nid: string) {
  if (!q.answer) return;
  const ans = q.answer.trim();
  if (!/^[A-D]$/.test(ans)) {
    nonLetterAnswers.push({ qId: q.id, year: q.year, category: q.category, nid, ans });
  }
}

for (const [nid, node] of Object.entries(KNOWLEDGE_BASE)) {
  for (const q of node.pastQuestions || []) {
    checkAns(q, 'KB', nid);
  }
}

for (const [nid, qlist] of Object.entries(EXTRACTED_PAST_QUESTIONS)) {
  for (const q of qlist) {
    checkAns(q, 'EXT', nid);
  }
}

console.log(`Total non-letter answers: ${nonLetterAnswers.length}`);

// Group into: wrapped in $, or NOT wrapped in $
const unwrapped = nonLetterAnswers.filter((a) => !a.ans.includes('$'));
console.log(`Unwrapped non-letter answers: ${unwrapped.length}`);

unwrapped.forEach((a, i) => {
  console.log(`[#${i + 1}] (${a.qId} in ${a.nid}) ${a.year} ${a.category}: "${a.ans}"`);
});
