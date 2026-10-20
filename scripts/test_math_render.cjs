const katex = require('katex');
const fs = require('fs');

// Read knowledgeBase.ts
const text = fs.readFileSync('src/data/knowledgeBase.ts', 'utf8');
const jsonPart = text.split('export const KNOWLEDGE_BASE: Record<string, KnowledgeNode> = ')[1].trim().replace(/;$/, '');
const kb = JSON.parse(jsonPart);

console.log('Testing KaTeX rendering for all 74 topics...');

let totalMathStrings = 0;
let errors = [];

function testRender(str, context) {
  if (!str || typeof str !== 'string') return;
  
  // Find all $$...$$
  const displayMatches = [...str.matchAll(/\$\$([\s\S]*?)\$\$/g)];
  for (const m of displayMatches) {
    totalMathStrings++;
    try {
      katex.renderToString(m[1].trim(), { displayMode: true, throwOnError: true });
    } catch (e) {
      errors.push({ type: 'display', math: m[1], err: e.message, context });
    }
  }

  // Find all $...$ (not $$)
  // Replace $$ first to avoid false matching
  const noDisplay = str.replace(/\$\$[\s\S]*?\$\$/g, '');
  const inlineMatches = [...noDisplay.matchAll(/\$([^$\n]+)\$/g)];
  for (const m of inlineMatches) {
    totalMathStrings++;
    try {
      katex.renderToString(m[1].trim(), { displayMode: false, throwOnError: true });
    } catch (e) {
      errors.push({ type: 'inline', math: m[1], err: e.message, context });
    }
  }
}

// Test formulas in knowledge base
for (const [tid, node] of Object.entries(kb)) {
  // 1. node.formulas
  for (const f of node.formulas || []) {
    totalMathStrings++;
    try {
      katex.renderToString(f.latex, { displayMode: true, throwOnError: true });
    } catch (e) {
      errors.push({ type: 'formula', math: f.latex, err: e.message, context: `${tid} -> formula "${f.title}"` });
    }
  }

  // 2. node.summary
  testRender(node.summary, `${tid} -> summary`);

  // 3. node.firstReaction
  testRender(node.firstReaction, `${tid} -> firstReaction`);

  // 4. candidateMethods
  for (const m of node.candidateMethods || []) {
    testRender(m.name, `${tid} -> method name`);
    testRender(m.condition, `${tid} -> method condition`);
    testRender(m.description, `${tid} -> method description`);
  }

  // 5. steps
  for (const s of node.steps || []) {
    testRender(s, `${tid} -> step`);
  }

  // 6. pitfalls
  for (const p of node.pitfalls || []) {
    testRender(p, `${tid} -> pitfall`);
  }

  // 7. pastQuestions
  for (const q of node.pastQuestions || []) {
    testRender(q.content, `${tid} -> question content`);
    testRender(q.analysis, `${tid} -> question analysis`);
    for (const s of q.solutionSteps || []) {
      testRender(s, `${tid} -> question step`);
    }
    testRender(q.answer, `${tid} -> question answer`);
    testRender(q.pitfall, `${tid} -> question pitfall`);
  }

  // 8. variants
  for (const v of node.variants || []) {
    testRender(v.question, `${tid} -> variant question`);
    testRender(v.hint, `${tid} -> variant hint`);
    testRender(v.methodChoiceAnalysis, `${tid} -> variant analysis`);
    for (const s of v.fullSolution || []) {
      testRender(s, `${tid} -> variant step`);
    }
    testRender(v.keyTakeaway, `${tid} -> variant takeaway`);
  }
}

console.log(`Total math expressions tested: ${totalMathStrings}`);
console.log(`Total errors found: ${errors.length}`);

if (errors.length > 0) {
  console.log('\nTop 20 errors:');
  errors.slice(0, 20).forEach((err, idx) => {
    console.log(`\n--- [${idx + 1}] in ${err.context} (${err.type}) ---`);
    console.log(`Math: "${err.math}"`);
    console.log(`Error: ${err.err}`);
  });
}
