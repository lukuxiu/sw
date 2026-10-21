const fs = require('fs');
const katex = require('katex');

const content = fs.readFileSync('src/data/makiLectures.ts', 'utf8');
const regex = /\$\$([\s\S]+?)\$\$|\$([^\$\n]+?)\$/g;
let match;
let count = 0;
let errors = 0;

while ((match = regex.exec(content)) !== null) {
  const formula = match[1] || match[2];
  count++;
  try {
    katex.renderToString(formula, { throwOnError: true, displayMode: !!match[1] });
  } catch (err) {
    console.error('KaTeX error in formula:', formula, err.message);
    errors++;
  }
}

console.log('Checked makiLectures.ts formulas:', count, 'Errors:', errors);
