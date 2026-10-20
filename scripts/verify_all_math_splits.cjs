const fs = require('fs');
const katex = require('katex');

// 1. Parse knowledgeBase JSON object
const text = fs.readFileSync('src/data/knowledgeBase.ts', 'utf8');
const startIdx = text.indexOf('export const KNOWLEDGE_BASE: Record<string, KnowledgeNode> = {') + 'export const KNOWLEDGE_BASE: Record<string, KnowledgeNode> = '.length;
const endIdx = text.indexOf('\n};\n\nimport { EXTRACTED_PAST_QUESTIONS }');
const jsonPart = text.slice(startIdx, endIdx + 2).trim();
const kb = JSON.parse(jsonPart);

// 2. Parse pastQuestionsData JSON object
const pqText = fs.readFileSync('src/data/pastQuestionsData.ts', 'utf8');
const pqStart = pqText.indexOf('export const EXTRACTED_PAST_QUESTIONS: Record<string, PastQuestionItem[]> = ') + 'export const EXTRACTED_PAST_QUESTIONS: Record<string, PastQuestionItem[]> = '.length;
const pqJson = pqText.slice(pqStart).trim().replace(/;$/, '');
const pqData = JSON.parse(pqJson);

// Merge pastQuestions into kb for full verification
for (const [nodeId, list] of Object.entries(pqData)) {
  if (kb[nodeId]) {
    kb[nodeId].pastQuestions = (kb[nodeId].pastQuestions || []).concat(list);
  }
}

let totalItemsChecked = 0;
let errorsFound = 0;
let unmatchedDollars = 0;

function checkString(str, context) {
  if (!str || typeof str !== 'string') return;
  totalItemsChecked++;

  // Check unmatched dollar signs
  const dollarCount = (str.match(/(?<!\\)\$/g) || []).length;
  if (dollarCount % 2 !== 0) {
    unmatchedDollars++;
    console.error(`[UNMATCHED $] Context: ${context} | Text: "${str.slice(0, 100)}..."`);
  }

  // Extract all math formulas $...$ and $$...$$
  const regex = /(\$\$[\s\S]*?\$\$|\$[^\$]+?\$)/g;
  let match;
  while ((match = regex.exec(str)) !== null) {
    const raw = match[0];
    const isDisplay = raw.startsWith('$$');
    const math = isDisplay ? raw.slice(2, -2).trim() : raw.slice(1, -1).trim();

    try {
      katex.renderToString(math, { displayMode: isDisplay, throwOnError: true });
    } catch (e) {
      errorsFound++;
      console.error(`[KATEX ERROR] in ${context}: "${math}" -> ${e.message}`);
    }
  }
}

// Traverse KB and check every string
for (const [nodeId, node] of Object.entries(kb)) {
  checkString(node.title, `${nodeId}.title`);
  checkString(node.firstReaction, `${nodeId}.firstReaction`);
  checkString(node.whyChooseMethod, `${nodeId}.whyChooseMethod`);
  (node.triggers || []).forEach((t, i) => checkString(t, `${nodeId}.triggers[${i}]`));
  (node.standardSteps || []).forEach((s, i) => checkString(s, `${nodeId}.standardSteps[${i}]`));
  (node.pitfalls || []).forEach((p, i) => checkString(p, `${nodeId}.pitfalls[${i}]`));

  (node.candidateMethods || []).forEach((m, i) => {
    checkString(m.name, `${nodeId}.candidateMethods[${i}].name`);
    checkString(m.applicability, `${nodeId}.candidateMethods[${i}].applicability`);
    checkString(m.whyChoose, `${nodeId}.candidateMethods[${i}].whyChoose`);
  });

  (node.coreFormulas || []).forEach((f, i) => {
    checkString(f.latex, `${nodeId}.coreFormulas[${i}].latex`);
  });

  (node.pastQuestions || []).forEach((q, i) => {
    checkString(q.content, `${nodeId}.pastQuestions[${i}].content (${q.id})`);
    checkString(q.analysis, `${nodeId}.pastQuestions[${i}].analysis (${q.id})`);
    checkString(q.answer, `${nodeId}.pastQuestions[${i}].answer (${q.id})`);
    checkString(q.pitfall, `${nodeId}.pastQuestions[${i}].pitfall (${q.id})`);
    (q.solutionSteps || []).forEach((s, si) => {
      checkString(s, `${nodeId}.pastQuestions[${i}].solutionSteps[${si}]`);
    });
  });
}

console.log("\n=== VERIFICATION SUMMARY ===");
console.log(`Total text items checked: ${totalItemsChecked}`);
console.log(`KaTeX errors found: ${errorsFound}`);
console.log(`Unmatched $ found: ${unmatchedDollars}`);

if (errorsFound === 0 && unmatchedDollars === 0) {
  process.exit(0);
} else {
  process.exit(1);
}
