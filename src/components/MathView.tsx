import React, { useMemo } from 'react';
import katex from 'katex';

interface MathViewProps {
  content: string;
  className?: string;
  inline?: boolean;
}

function escapeHtml(str: string): string {
  return str
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/\n/g, '<br/>');
}

export const MathView: React.FC<MathViewProps> = ({ content, className = '', inline = false }) => {
  const renderedHtml = useMemo(() => {
    if (!content) return '';

    // Pre-process and normalize delimiters and legacy artifacts
    let str = content
      .replace(/[\u0000-\u0008\u000b\u000c\u000e-\u001f]/g, '')
      .replace(/\(\\quad\)/g, '（　　）')
      .replace(/\\\[([\s\S]*?)\\\]/g, '$$$$1$$$')
      .replace(/\\\(([\s\S]*?)\\\)/g, '$$$1$');

    // Wrap unwrapped LaTeX environments like \begin{cases}...\end{cases} or \begin{pmatrix}...\end{pmatrix}
    if (!str.includes('$') && /\\begin\{(cases|pmatrix|bmatrix|vmatrix|aligned|matrix)\}/.test(str)) {
      str = `$$${str}$$`;
    }

    // 1. If content contains $ delimiters, parse segments
    if (str.includes('$')) {
      // Match display math $$...$$ or inline math $...$
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

    // If no Chinese characters, check if it's likely a pure LaTeX formula or math equation
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
      // If it contains Chinese and has LaTeX commands with \text{...}, attempt KaTeX rendering
      if (trimmed.includes('\\text{') && (trimmed.startsWith('\\') || trimmed.includes('='))) {
        try {
          return katex.renderToString(trimmed, {
            displayMode: !inline,
            throwOnError: false,
          });
        } catch (e) {
          // Fallback to plain text
        }
      }
    }

    // 3. Plain text
    return escapeHtml(str);
  }, [content, inline]);

  return (
    <span
      className={`math-rendered leading-relaxed ${className}`}
      dangerouslySetInnerHTML={{ __html: renderedHtml }}
    />
  );
};
