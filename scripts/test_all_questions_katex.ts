import katex from 'katex';
import { KNOWLEDGE_BASE } from '../src/data/knowledgeBase';
import { EXTRACTED_PAST_QUESTIONS } from '../src/data/pastQuestionsData';

const errors: any[] = [];
let formulaCount = 0;

function testString(str: string, loc: string) {
  if (!str) return;

  // Extract display formulas $$...$$
  const displayRegex = /\$\$([\s\S]*?)\$\$/g;
  let match;
  while ((match = displayRegex.exec(str)) !== null) {
    formulaCount++;
    const math = match[1].trim();
    try {
      katex.renderToString(math, { displayMode: true, throwOnError: true });
    } catch (e: any) {
      errors.push({ loc, type: 'display', math, error: e.message });
    }
  }

  // Extract inline formulas $...$ (remove $$ first)
  const noDisplay = str.replace(/\$\$[\s\S]*?\$\$/g, ' ');
  const inlineRegex = /\$([^\$]+?)\$/g;
  while ((match = inlineRegex.exec(noDisplay)) !== null) {
    formulaCount++;
    const math = match[1].trim();
    try {
      katex.renderToString(math, { displayMode: false, throwOnError: true });
    } catch (e: any) {
      errors.push({ loc, type: 'inline', math, error: e.message });
    }
  }
}

for (const [nid, node] of Object.entries(KNOWLEDGE_BASE)) {
  for (const q of node.pastQuestions || []) {
    testString(q.content, `KB.${nid}.${q.id}.content`);
    (q.options || []).forEach((o, i) => testString(o, `KB.${nid}.${q.id}.options[${i}]`));
    testString(q.analysis, `KB.${nid}.${q.id}.analysis`);
    testString(q.answer, `KB.${nid}.${q.id}.answer`);
    testString(q.pitfall, `KB.${nid}.${q.id}.pitfall`);
    (q.solutionSteps || []).forEach((s, i) => testString(s, `KB.${nid}.${q.id}.step[${i}]`));
  }
}

for (const [nid, qlist] of Object.entries(EXTRACTED_PAST_QUESTIONS)) {
  for (const q of qlist) {
    testString(q.content, `EXT.${nid}.${q.id}.content`);
    (q.options || []).forEach((o, i) => testString(o, `EXT.${nid}.${q.id}.options[${i}]`));
    testString(q.analysis, `EXT.${nid}.${q.id}.analysis`);
    testString(q.answer, `EXT.${nid}.${q.id}.answer`);
    testString(q.pitfall, `EXT.${nid}.${q.id}.pitfall`);
    (q.solutionSteps || []).forEach((s, i) => testString(s, `EXT.${nid}.${q.id}.step[${i}]`));
  }
}

console.log(`Total formulas tested: ${formulaCount}`);
console.log(`Total KaTeX errors found: ${errors.length}`);
errors.forEach((err, i) => {
  console.log(`[#${i + 1}] at ${err.loc} (${err.type}):`);
  console.log(`    Math : ${err.math}`);
  console.log(`    Error: ${err.error}`);
});
