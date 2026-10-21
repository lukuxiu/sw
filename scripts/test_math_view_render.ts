import katex from 'katex';

function escapeHtml(str: string): string {
  return str
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/\n/g, '<br/>');
}

function renderMath(content: string, inline = false): string {
  if (!content) return '';

  let str = content
    .replace(/[\u0000-\u0008\u000b\u000c\u000e-\u001f]/g, '')
    .replace(/\(\\quad\)/g, '（　　）')
    .replace(/\\\[([\s\S]*?)\\\]/g, '$$$$1$$$')
    .replace(/\\\(([\s\S]*?)\\\)/g, '$$$1$');

  // If there's an unwrapped LaTeX environment
  if (!str.includes('$') && /\\begin\{(cases|pmatrix|bmatrix|vmatrix|aligned|matrix)\}/.test(str)) {
    str = `$$${str}$$`;
  }

  // 1. If content contains $ delimiters, parse segments
  if (str.includes('$')) {
    const parts = str.split(/(\$\$[\s\S]*?\$\$|\$[^\$]+?\$)/g);
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
  const trimmed = str.trim();
  const hasChinese = /[\u4e00-\u9fa5]/.test(trimmed);

  // If no Chinese, check if likely pure LaTeX formula
  if (!hasChinese) {
    const isLikelyLatex =
      trimmed.startsWith('\\') ||
      /\\[a-zA-Z]+/.test(trimmed) ||
      (/^[a-zA-Z0-9\s\+\-\*\/\=\(\)\,\.\_\^\:\;]+$/.test(trimmed) && /[\^_\=\+\-\*\/]/.test(trimmed));

    if (isLikelyLatex) {
      try {
        return katex.renderToString(trimmed, {
          displayMode: !inline,
          throwOnError: false,
        });
      } catch (e) {
        return escapeHtml(str);
      }
    }
  } else {
    // If has Chinese, but contains \text{...} and LaTeX math commands, attempt KaTeX directly
    if (trimmed.includes('\\text{') && (trimmed.startsWith('\\') || trimmed.includes('='))) {
      try {
        return katex.renderToString(trimmed, {
          displayMode: !inline,
          throwOnError: true,
        });
      } catch (e) {
        // Fallback
      }
    }
  }

  return escapeHtml(str);
}

// Test cases
console.log('Test 1 (\\[...\\]):', renderMath('\\[ x^2 + y^2 = 1 \\]').includes('katex'));
console.log('Test 2 (\\(...\\)):', renderMath('已知 \\( f(x) = x^2 \\)，求导数').includes('katex'));
console.log('Test 3 (\\pi / 2):', renderMath('\\pi / 2', true).includes('katex'));
console.log('Test 4 (\\begin{cases}):', renderMath('\\begin{cases} x, & x>0 \\\\ 0, & x \\le 0 \\end{cases}').includes('katex'));
console.log('Test 5 ((\\quad)):', renderMath('选项则为 (\\quad)').includes('（　　）'));
