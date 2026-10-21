import { KNOWLEDGE_BASE } from '../src/data/knowledgeBase';
import { EXTRACTED_PAST_QUESTIONS } from '../src/data/pastQuestionsData';

// Merge all questions
const allQuestions: { q: any; src: string; nodeId: string }[] = [];

for (const [nodeId, node] of Object.entries(KNOWLEDGE_BASE)) {
  (node.pastQuestions || []).forEach((q) => {
    allQuestions.push({ q, src: 'KB', nodeId });
  });
}

for (const [nodeId, qlist] of Object.entries(EXTRACTED_PAST_QUESTIONS)) {
  qlist.forEach((q) => {
    allQuestions.push({ q, src: 'EXTRACTED', nodeId });
  });
}

console.log(`Total questions loaded: ${allQuestions.length}`);

// We want to detect ANY LaTeX syntax that appears outside of $...$ or $$...$$
function findLeakedLatex(str: string): string[] {
  if (!str) return [];
  // Remove all $$...$$ and $...$
  const withoutMath = str.replace(/\$\$[\s\S]*?\$\$/g, ' ').replace(/\$[^\$]+?\$/g, ' ');
  // Match any LaTeX command: \alpha, \frac, \sqrt, etc.
  const matches = withoutMath.match(/\\[a-zA-Z]+/g) || [];
  // Filter out non-math commands or formatting like \n or \t
  return matches.filter((m) => !['\\n', '\\t', '\\r'].includes(m));
}

let leakCount = 0;
const leakedItems: any[] = [];

for (const item of allQuestions) {
  const { q, src, nodeId } = item;
  const fields = [
    { name: 'content', val: q.content },
    { name: 'analysis', val: q.analysis },
    { name: 'answer', val: q.answer },
    { name: 'pitfall', val: q.pitfall },
  ];

  if (q.options) {
    q.options.forEach((opt: string, i: number) => fields.push({ name: `options[${i}]`, val: opt }));
  }
  if (q.solutionSteps) {
    q.solutionSteps.forEach((st: string, i: number) => fields.push({ name: `solutionSteps[${i}]`, val: st }));
  }

  for (const f of fields) {
    if (!f.val) continue;
    const leaks = findLeakedLatex(f.val);
    if (leaks.length > 0) {
      leakCount++;
      leakedItems.push({
        qId: q.id,
        year: q.year,
        category: q.category,
        nodeId,
        field: f.name,
        leaks: Array.from(new Set(leaks)),
        text: f.val,
      });
    }
  }
}

console.log(`Total fields with leaked LaTeX: ${leakCount}`);
console.log('\nTop 20 leaked items:');
leakedItems.slice(0, 20).forEach((item, i) => {
  console.log(`[#${i + 1}] (${item.qId} in ${item.nodeId}) ${item.field}: leaks: ${item.leaks.join(', ')}`);
  console.log(`     Text: ${item.text.slice(0, 140)}`);
});
