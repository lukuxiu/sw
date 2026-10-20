const fs = require('fs');

const text = fs.readFileSync('src/data/knowledgeBase.ts', 'utf8');
const jsonPart = text.split('export const KNOWLEDGE_BASE: Record<string, KnowledgeNode> = ')[1].trim().replace(/;$/, '');
const kb = JSON.parse(jsonPart);

console.log('Checking for unmatched $ and LaTeX anomalies in knowledgeBase.ts...');

let issues = [];

function checkString(str, context) {
  if (!str || typeof str !== 'string') return;

  // Check unmatched $$
  const doubleCount = (str.match(/\$\$/g) || []).length;
  if (doubleCount % 2 !== 0) {
    issues.push({ context, type: 'unmatched $$', str });
  }

  // Remove $$...$$ before checking single $
  const withoutDouble = str.replace(/\$\$[\s\S]*?\$\$/g, '');
  const singleCount = (withoutDouble.match(/\$/g) || []).length;
  if (singleCount % 2 !== 0) {
    issues.push({ context, type: 'unmatched $', str });
  }

  // Check for common LaTeX typos: e.g. \frac without braces or double backslashes in wrong place
  // Check for \left without \right
  const leftCount = (str.match(/\\left[\(\[\{\.\|]/g) || []).length;
  const rightCount = (str.match(/\\right[\)\]\}\.\|]/g) || []).length;
  if (leftCount !== rightCount) {
    issues.push({ context, type: `mismatched \\left (${leftCount}) vs \\right (${rightCount})`, str });
  }
}

for (const [tid, node] of Object.entries(kb)) {
  checkString(node.summary, `${tid} summary`);
  checkString(node.firstReaction, `${tid} firstReaction`);
  (node.triggers || []).forEach((t, i) => checkString(t, `${tid} trigger[${i}]`));
  (node.steps || []).forEach((s, i) => checkString(s, `${tid} step[${i}]`));
  (node.pitfalls || []).forEach((p, i) => checkString(p, `${tid} pitfall[${i}]`));
  for (const m of node.candidateMethods || []) {
    checkString(m.name, `${tid} method name`);
    checkString(m.condition, `${tid} method condition`);
    checkString(m.description, `${tid} method description`);
  }
  for (const f of node.formulas || []) {
    checkString(f.latex, `${tid} formula "${f.title}"`);
  }
  for (const q of node.pastQuestions || []) {
    checkString(q.content, `${tid} question ${q.id} content`);
    checkString(q.analysis, `${tid} question ${q.id} analysis`);
    (q.solutionSteps || []).forEach((s, i) => checkString(s, `${tid} question ${q.id} step[${i}]`));
    checkString(q.answer, `${tid} question ${q.id} answer`);
    checkString(q.pitfall, `${tid} question ${q.id} pitfall`);
  }
  for (const v of node.variants || []) {
    checkString(v.question, `${tid} variant ${v.id} question`);
    checkString(v.hint, `${tid} variant ${v.id} hint`);
    checkString(v.methodChoiceAnalysis, `${tid} variant ${v.id} analysis`);
    (v.fullSolution || []).forEach((s, i) => checkString(s, `${tid} variant ${v.id} step[${i}]`));
    checkString(v.keyTakeaway, `${tid} variant ${v.id} takeaway`);
  }
}

console.log(`Total anomalies found: ${issues.length}`);
issues.forEach((iss, i) => {
  console.log(`\n[${i+1}] ${iss.context} - ${iss.type}`);
  console.log(`String: ${iss.str.substring(0, 150)}...`);
});
