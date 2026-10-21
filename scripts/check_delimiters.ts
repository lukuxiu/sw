import { KNOWLEDGE_BASE } from '../src/data/knowledgeBase';
import { EXTRACTED_PAST_QUESTIONS } from '../src/data/pastQuestionsData';

let bracketCount = 0;
let parenCount = 0;

function check(str: string, loc: string) {
  if (!str) return;
  if (str.includes('\\[') || str.includes('\\]')) {
    bracketCount++;
    console.log(`Bracket in ${loc}:`, str.slice(0, 80));
  }
  if (str.includes('\\(') || str.includes('\\)')) {
    // Exclude choice bracket like (\quad)
    if (!str.includes('(\\quad)')) {
      parenCount++;
      console.log(`Paren in ${loc}:`, str.slice(0, 80));
    }
  }
}

for (const [nid, node] of Object.entries(KNOWLEDGE_BASE)) {
  for (const q of node.pastQuestions || []) {
    check(q.content, `KB.${nid}.${q.id}.content`);
    (q.options || []).forEach((o, i) => check(o, `KB.${nid}.${q.id}.options[${i}]`));
    check(q.analysis, `KB.${nid}.${q.id}.analysis`);
    check(q.answer, `KB.${nid}.${q.id}.answer`);
    check(q.pitfall, `KB.${nid}.${q.id}.pitfall`);
    (q.solutionSteps || []).forEach((s, i) => check(s, `KB.${nid}.${q.id}.step[${i}]`));
  }
}

for (const [nid, qlist] of Object.entries(EXTRACTED_PAST_QUESTIONS)) {
  for (const q of qlist) {
    check(q.content, `EXT.${nid}.${q.id}.content`);
    (q.options || []).forEach((o, i) => check(o, `EXT.${nid}.${q.id}.options[${i}]`));
    check(q.analysis, `EXT.${nid}.${q.id}.analysis`);
    check(q.answer, `EXT.${nid}.${q.id}.answer`);
    check(q.pitfall, `EXT.${nid}.${q.id}.pitfall`);
    (q.solutionSteps || []).forEach((s, i) => check(s, `EXT.${nid}.${q.id}.step[${i}]`));
  }
}

console.log(`Total \\[: ${bracketCount}, Total \\(: ${parenCount}`);
