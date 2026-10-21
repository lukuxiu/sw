import katex from 'katex';
import { KNOWLEDGE_BASE } from '../src/data/knowledgeBase';
import { EXTRACTED_PAST_QUESTIONS } from '../src/data/pastQuestionsData';
import { MAKI_LECTURES, MAKI_WAR_MAP } from '../src/data/makiLectures';
import { UNIVERSAL_META_METHODS } from '../src/data/metaMethods';
import { getAllFeatures } from '../src/data/featureIndex';

interface AuditIssue {
  type: string;
  location: string;
  sample: string;
  message: string;
}

const issues: AuditIssue[] = [];

const COMMON_COMMANDS = new Set([
  'frac', 'lim', 'int', 'iint', 'iiint', 'oint', 'sum', 'prod',
  'alpha', 'beta', 'gamma', 'delta', 'epsilon', 'zeta', 'eta', 'theta',
  'iota', 'kappa', 'lambda', 'mu', 'nu', 'xi', 'pi', 'rho', 'sigma',
  'tau', 'upsilon', 'phi', 'chi', 'psi', 'omega',
  'Gamma', 'Delta', 'Theta', 'Lambda', 'Xi', 'Pi', 'Sigma', 'Phi', 'Psi', 'Omega',
  'partial', 'infty', 'nabla', 'sqrt', 'cdot', 'times', 'div', 'pm', 'mp',
  'le', 'ge', 'leq', 'geq', 'neq', 'approx', 'equiv', 'sim',
  'in', 'notin', 'subset', 'subseteq', 'cup', 'cap',
  'to', 'rightarrow', 'leftarrow', 'Rightarrow', 'Leftarrow', 'iff',
  'quad', 'qquad', 'text', 'mathrm', 'mathbf', 'mathit', 'bm',
  'sin', 'cos', 'tan', 'cot', 'sec', 'csc', 'arcsin', 'arccos', 'arctan',
  'ln', 'log', 'exp', 'det', 'tr', 'rank', 'dim', 'ker',
  'begin', 'end', 'pmatrix', 'bmatrix', 'vmatrix', 'matrix', 'cases', 'aligned'
]);

function removeDollarMath(text: string): string {
  const noDisplay = text.replace(/\$\$[\s\S]*?\$\$/g, ' ').replace(/\\\[[\s\S]*?\\\]/g, ' ');
  return noDisplay.replace(/\$[\s\S]*?\$|\\\([\s\S]*?\\\)/g, ' ');
}

function auditString(text: string | undefined, location: string) {
  if (!text || typeof text !== 'string') return;

  // 1. Check unmatched $
  const dollars = text.match(/(?<!\\)\$/g) || [];
  if (dollars.length % 2 !== 0) {
    issues.push({
      type: 'UNMATCHED_DOLLAR',
      location,
      sample: text.slice(0, 100),
      message: `Odd number of $ (${dollars.length})`,
    });
  }

  // 2. Check for \( \) \[ \]
  const outside = removeDollarMath(text);
  if (outside.includes('\\(') || outside.includes('\\)') || outside.includes('\\[') || outside.includes('\\]')) {
    issues.push({
      type: 'PAREN_BRACKET_DELIMITER',
      location,
      sample: text.slice(0, 100),
      message: 'Found \\( / \\) / \\[ / \\] outside of $...$',
    });
  }

  // 3. Check for raw LaTeX commands outside of $...$
  const leakedMatches = outside.match(/\\[a-zA-Z]+/g) || [];
  const leaked = leakedMatches.map((m) => m.slice(1)).filter((cmd) => COMMON_COMMANDS.has(cmd));
  if (leaked.length > 0) {
    // Exclude false positives like '\n' which is not in common commands
    issues.push({
      type: 'RAW_LATEX_LEAK',
      location,
      sample: text.slice(0, 120),
      message: `Commands without $: ${Array.from(new Set(leaked)).join(', ')}`,
    });
  }

  // 4. Test KaTeX rendering on every formula inside $...$ and $$...$$
  const formulaRegex = /(\$\$[\s\S]*?\$\$|\$[^\$]+?\$)/g;
  let match;
  while ((match = formulaRegex.exec(text)) !== null) {
    const raw = match[0];
    const isDisplay = raw.startsWith('$$');
    const math = isDisplay ? raw.slice(2, -2).trim() : raw.slice(1, -1).trim();

    try {
      katex.renderToString(math, { displayMode: isDisplay, throwOnError: true });
    } catch (e: any) {
      issues.push({
        type: 'KATEX_RENDER_ERROR',
        location,
        sample: raw,
        message: e.message,
      });
    }
  }

  // 5. Test if the entire string was supposed to be a formula without $
  // e.g. starts with \lim or \int or \frac and contains no Chinese
  const trimmed = text.trim();
  const hasChinese = /[\u4e00-\u9fa5]/.test(trimmed);
  if (!text.includes('$') && !hasChinese && (trimmed.startsWith('\\') || /\\[a-zA-Z]+/.test(trimmed))) {
    try {
      katex.renderToString(trimmed, { displayMode: false, throwOnError: true });
    } catch (e: any) {
      issues.push({
        type: 'UNWRAPPED_LATEX_ERROR',
        location,
        sample: trimmed.slice(0, 80),
        message: `Unwrapped LaTeX string failed: ${e.message}`,
      });
    }
  }
}

// 1. Audit KNOWLEDGE_BASE pastQuestions
console.log('Auditing KNOWLEDGE_BASE pastQuestions...');
for (const [nid, node] of Object.entries(KNOWLEDGE_BASE)) {
  (node.pastQuestions || []).forEach((q, i) => {
    const loc = `KB.${nid}.pastQuestions[${i}](${q.id})`;
    auditString(q.content, `${loc}.content`);
    (q.options || []).forEach((opt, oi) => auditString(opt, `${loc}.options[${oi}]`));
    auditString(q.analysis, `${loc}.analysis`);
    auditString(q.answer, `${loc}.answer`);
    auditString(q.pitfall, `${loc}.pitfall`);
    (q.solutionSteps || []).forEach((st, si) => auditString(st, `${loc}.solutionSteps[${si}]`));
  });
}

// 2. Audit EXTRACTED_PAST_QUESTIONS
console.log('Auditing EXTRACTED_PAST_QUESTIONS...');
for (const [nid, qlist] of Object.entries(EXTRACTED_PAST_QUESTIONS)) {
  qlist.forEach((q, i) => {
    const loc = `EXTRACTED.${nid}[${i}](${q.id})`;
    auditString(q.content, `${loc}.content`);
    (q.options || []).forEach((opt, oi) => auditString(opt, `${loc}.options[${oi}]`));
    auditString(q.analysis, `${loc}.analysis`);
    auditString(q.answer, `${loc}.answer`);
    auditString(q.pitfall, `${loc}.pitfall`);
    (q.solutionSteps || []).forEach((st, si) => auditString(st, `${loc}.solutionSteps[${si}]`));
  });
}

// 3. Audit MAKI_LECTURES
console.log('Auditing MAKI_LECTURES...');
for (const lec of MAKI_LECTURES) {
  const loc = `MAKI.${lec.id}`;
  auditString(lec.title, `${loc}.title`);
  auditString(lec.orientation, `${loc}.orientation`);
  lec.subsections.forEach((sub, si) => auditString(sub, `${loc}.subsections[${si}]`));
  lec.methodCards.forEach((c, ci) => {
    auditString(c.title, `${loc}.methodCards[${ci}].title`);
    auditString(c.content, `${loc}.methodCards[${ci}].content`);
    (c.keySteps || []).forEach((ks, ksi) => auditString(ks, `${loc}.methodCards[${ci}].keySteps[${ksi}]`));
    auditString(c.formulaLatex, `${loc}.methodCards[${ci}].formulaLatex`);
  });
}

// 4. Audit UNIVERSAL_META_METHODS pastQuestions
console.log('Auditing UNIVERSAL_META_METHODS...');
for (const m of UNIVERSAL_META_METHODS) {
  const loc = `META.${m.id}`;
  (m.pastQuestions || []).forEach((q, qi) => {
    auditString(q.stem, `${loc}.pastQuestions[${qi}].stem`);
    auditString(q.methodUsage, `${loc}.pastQuestions[${qi}].methodUsage`);
    auditString(q.solutionKey, `${loc}.pastQuestions[${qi}].solutionKey`);
  });
}

// 5. Audit FEATURE_MATRIX
console.log('Auditing FEATURE_MATRIX...');
const features = getAllFeatures();
for (const feat of features) {
  const loc = `FEATURE.${feat.id}`;
  auditString(feat.trigger, `${loc}.trigger`);
  auditString(feat.firstReaction, `${loc}.firstReaction`);
  (feat.examples || []).forEach((ex, ei) => {
    auditString(ex.prompt, `${loc}.examples[${ei}].prompt`);
    (ex.options || []).forEach((opt, oi) => auditString(opt, `${loc}.examples[${ei}].options[${oi}]`));
    auditString(ex.keyReaction, `${loc}.examples[${ei}].keyReaction`);
  });
}

// Print results
console.log('\n================ AUDIT SUMMARY ================');
console.log(`Total issues found: ${issues.length}`);

const countByType: Record<string, number> = {};
for (const iss of issues) {
  countByType[iss.type] = (countByType[iss.type] || 0) + 1;
}

for (const [t, c] of Object.entries(countByType)) {
  console.log(`  ${t}: ${c}`);
}

console.log('\n================ ALL ISSUES LIST ================');
issues.forEach((iss, idx) => {
  console.log(`[#${idx + 1}] [${iss.type}] at ${iss.location}`);
  console.log(`    Message: ${iss.message}`);
  console.log(`    Sample : ${iss.sample}`);
});
