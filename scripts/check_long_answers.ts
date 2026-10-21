import { KNOWLEDGE_BASE } from '../src/data/knowledgeBase';
import { EXTRACTED_PAST_QUESTIONS } from '../src/data/pastQuestionsData';

const longAnswers: any[] = [];

function check(q: any, src: string, nid: string) {
  if (q.answer && q.answer.length > 50) {
    longAnswers.push({ qId: q.id, year: q.year, category: q.category, nid, ans: q.answer });
  }
}

for (const [nid, node] of Object.entries(KNOWLEDGE_BASE)) {
  for (const q of node.pastQuestions || []) check(q, 'KB', nid);
}
for (const [nid, qlist] of Object.entries(EXTRACTED_PAST_QUESTIONS)) {
  for (const q of qlist) check(q, 'EXT', nid);
}

console.log(`Total long answers (> 50 chars): ${longAnswers.length}`);
longAnswers.forEach((a, i) => {
  console.log(`\n[#${i + 1}] (${a.qId} in ${a.nid}) len=${a.ans.length}:`);
  console.log(a.ans.slice(0, 160));
});
