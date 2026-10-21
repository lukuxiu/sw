import { KNOWLEDGE_BASE } from '../src/data/knowledgeBase';
import { EXTRACTED_PAST_QUESTIONS } from '../src/data/pastQuestionsData';

interface ArtifactProblem {
  source: 'KB' | 'EXT';
  nodeId: string;
  qId: string;
  year: string;
  field: string;
  artifactType: string;
  sample: string;
}

const problems: ArtifactProblem[] = [];

const ARTIFACT_REGEXES: { name: string; regex: RegExp }[] = [
  { name: 'integral_symbol_caret', regex: /ˆ/ },
  { name: 'piecewise_brace_unicode', regex: /[]/ },
  { name: 'matrix_paren_unicode', regex: /[]/ },
  { name: 'broken_sqrt_newline', regex: /√\s*\n/ },
  { name: 'null_control_chars', regex: /[\u0000-\u0008\u000b\u000c\u000e-\u001f]/ },
  { name: 'leaked_quad', regex: /\(\\quad\)/ },
  { name: 'raw_latex_answer', regex: /^\s*\\[a-zA-Z]+/ },
  { name: 'dirty_choice_answer', regex: /^[A-D]\s*\n/ },
  { name: 'circled_numbers', regex: /[①②③④⑤⑥⑦⑧⑨⑩1⃝2⃝3⃝4⃝]/ },
  { name: 'exercise_header_cruft', regex: /（习题集\d+\.\d+）/ },
];

function scanText(text: string | undefined, source: 'KB' | 'EXT', nodeId: string, qId: string, year: string, field: string) {
  if (!text) return;
  for (const { name, regex } of ARTIFACT_REGEXES) {
    if (regex.test(text)) {
      problems.push({
        source,
        nodeId,
        qId,
        year,
        field,
        artifactType: name,
        sample: text.slice(0, 100).replace(/\n/g, '\\n'),
      });
    }
  }
}

for (const [nid, node] of Object.entries(KNOWLEDGE_BASE)) {
  for (const q of node.pastQuestions || []) {
    scanText(q.content, 'KB', nid, q.id, q.year, 'content');
    scanText(q.answer, 'KB', nid, q.id, q.year, 'answer');
    scanText(q.analysis, 'KB', nid, q.id, q.year, 'analysis');
    scanText(q.pitfall, 'KB', nid, q.id, q.year, 'pitfall');
    (q.options || []).forEach((o, i) => scanText(o, 'KB', nid, q.id, q.year, `options[${i}]`));
    (q.solutionSteps || []).forEach((s, i) => scanText(s, 'KB', nid, q.id, q.year, `steps[${i}]`));
  }
}

for (const [nid, qlist] of Object.entries(EXTRACTED_PAST_QUESTIONS)) {
  for (const q of qlist) {
    scanText(q.content, 'EXT', nid, q.id, q.year, 'content');
    scanText(q.answer, 'EXT', nid, q.id, q.year, 'answer');
    scanText(q.analysis, 'EXT', nid, q.id, q.year, 'analysis');
    scanText(q.pitfall, 'EXT', nid, q.id, q.year, 'pitfall');
    (q.options || []).forEach((o, i) => scanText(o, 'EXT', nid, q.id, q.year, `options[${i}]`));
    (q.solutionSteps || []).forEach((s, i) => scanText(s, 'EXT', nid, q.id, q.year, `steps[${i}]`));
  }
}

console.log(`Total artifact problems found: ${problems.length}`);
const byType: Record<string, number> = {};
for (const p of problems) {
  byType[p.artifactType] = (byType[p.artifactType] || 0) + 1;
}
for (const [t, c] of Object.entries(byType)) {
  console.log(`  ${t}: ${c}`);
}

// Check unique questions affected
const affectedQIds = new Set(problems.map((p) => p.qId));
console.log(`Total unique questions affected: ${affectedQIds.size}`);
