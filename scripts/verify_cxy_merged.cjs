const fs = require('fs');
const katex = require('katex');

const data = JSON.parse(fs.readFileSync('scripts/merged_questions_test.json', 'utf8'));
console.log(`Checking KaTeX on ${data.length} questions...`);

let totalFormulas = 0;
let errors = [];
let unmatched = [];

function checkText(str, ctx) {
  if (!str || typeof str !== 'string') return;

  const dollarCount = (str.match(/(?<!\\)\$/g) || []).length;
  if (dollarCount % 2 !== 0) {
    unmatched.push({ ctx, str: str.slice(0, 100) });
  }

  const regex = /(\$\$[\s\S]*?\$\$|\$[^\$]+?\$)/g;
  let match;
  while ((match = regex.exec(str)) !== null) {
    totalFormulas++;
    const raw = match[0];
    const isDisplay = raw.startsWith('$$');
    const math = isDisplay ? raw.slice(2, -2).trim() : raw.slice(1, -1).trim();

    try {
      katex.renderToString(math, { displayMode: isDisplay, throwOnError: true });
    } catch (e) {
      errors.push({ ctx, math: math.slice(0, 100), err: e.message });
    }
  }
}

data.forEach((entry, idx) => {
  const it = entry.item;
  const ctx = `${it.id} (${it.year} ${it.category})`;
  checkText(it.content, `${ctx}.content`);
  (it.options || []).forEach((opt, oi) => {
    checkText(opt, `${ctx}.options[${oi}]`);
  });
  checkText(it.answer, `${ctx}.answer`);
  checkText(it.analysis, `${ctx}.analysis`);
  (it.solutionSteps || []).forEach((s, si) => {
    checkText(s, `${ctx}.solutionSteps[${si}]`);
  });
  checkText(it.pitfall, `${ctx}.pitfall`);
});

console.log(`Total formulas tested: ${totalFormulas}`);
console.log(`Unmatched dollars: ${unmatched.length}`);
console.log(`KaTeX errors: ${errors.length}`);

if (errors.length > 0) {
  console.log("Sample errors:");
  errors.slice(0, 10).forEach(e => {
    console.log(`  [${e.ctx}]: "${e.math}" -> ${e.err}`);
  });
}
if (unmatched.length > 0) {
  console.log("Sample unmatched:");
  unmatched.slice(0, 10).forEach(u => {
    console.log(`  [${u.ctx}]: "${u.str}"`);
  });
}
