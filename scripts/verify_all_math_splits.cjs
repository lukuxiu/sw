const fs = require('fs');
const katex = require('katex');

const text = fs.readFileSync('src/data/knowledgeBase.ts', 'utf8');
const jsonPart = text.split('export const KNOWLEDGE_BASE: Record<string, KnowledgeNode> = ')[1].trim().replace(/;$/, '');
const kb = JSON.parse(jsonPart);

function escapeHtml(str) {
  return str
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/\n/g, '<br/>');
}

function renderMathContent(content, inline = false) {
  if (!content) return '';

  // 1. If content contains $ delimiters, parse segments
  if (content.includes('$')) {
    // Match display math $$...$$ or inline math $...$
    const parts = content.split(/(\$\$[\s\S]*?\$\$|\$[^$\n]+?\$)/g);

    return parts
      .map((part) => {
        if (part.startsWith('$$') && part.endsWith('$$')) {
          const math = part.slice(2, -2).trim();
          try {
            return katex.renderToString(math, { displayMode: true, throwOnError: false });
          } catch (e) {
            return escapeHtml(part);
          }
        } else if (part.startsWith('$') && part.endsWith('$')) {
          const math = part.slice(1, -1).trim();
          try {
            return katex.renderToString(math, { displayMode: false, throwOnError: false });
          } catch (e) {
            return escapeHtml(part);
          }
        } else {
          return escapeHtml(part);
        }
      })
      .join('');
  }

  // 2. If NO $ delimiters:
  const trimmed = content.trim();
  // Check if it's likely a pure LaTeX formula
  const hasChinese = /[\u4e00-\u9fa5]/.test(trimmed);
  const isLikelyLatex = !hasChinese && (
    trimmed.startsWith('\\') || 
    /\\[a-zA-Z]+/.test(trimmed) || 
    /^[a-zA-Z0-9\s\+\-\*\/\=\(\)\,\.\_\^]+$/.test(trimmed) && /[\^_\=]/.test(trimmed)
  );

  if (isLikelyLatex) {
    try {
      return katex.renderToString(trimmed, {
        displayMode: !inline,
        throwOnError: false,
      });
    } catch (e) {
      return escapeHtml(content);
    }
  }

  // 3. Plain text
  return escapeHtml(content);
}

let katexErrorCount = 0;
let rawDollarCount = 0;
let totalChecked = 0;

for (const [id, node] of Object.entries(kb)) {
  const allTexts = [
    node.summary,
    node.firstReaction,
    node.applicability,
    ...(node.triggers || []),
    ...(node.steps || []),
    ...(node.pitfalls || []),
    ...(node.candidateMethods || []).flatMap(m => [m.name, m.condition, m.description, m.whyChoose]),
    ...(node.formulas || []).map(f => `$$${f.latex}$$`),
    ...(node.pastQuestions || []).flatMap(q => [q.content, q.analysis, ...(q.solutionSteps || []), q.answer, q.pitfall]),
    ...(node.variants || []).flatMap(v => [v.question, v.hint, v.methodChoiceAnalysis, ...(v.fullSolution || []), v.keyTakeaway])
  ];

  for (const t of allTexts) {
    if (!t) continue;
    totalChecked++;
    const rendered = renderMathContent(t, true);
    if (rendered.includes('katex-error')) {
      katexErrorCount++;
      console.log(`[KaTeX Error] in node ${id}:`, t);
    }
    // Check if there are raw $ remaining outside of html tags or attributes
    // In our escapeHtml, $ is not escaped, but if KaTeX rendered it, there should be no $ in raw text unless intended
    const plainParts = t.split(/(\$\$[\s\S]*?\$\$|\$[^$\n]+?\$)/g);
    for (let i = 0; i < plainParts.length; i += 2) {
      if (plainParts[i] && plainParts[i].includes('$')) {
        rawDollarCount++;
        console.log(`[Unmatched $] in node ${id}:`, plainParts[i]);
      }
    }
  }
}

console.log('=== VERIFICATION SUMMARY ===');
console.log('Total text items checked:', totalChecked);
console.log('KaTeX errors found:', katexErrorCount);
console.log('Unmatched $ found:', rawDollarCount);
