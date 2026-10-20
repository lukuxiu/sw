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
    // Check if it's likely a pure LaTeX formula (no Chinese characters, and has LaTeX control sequence or math operators)
    const hasChinese = /[\u4e00-\u9fa5]/.test(trimmed);
    const isLikelyLatex =
      !hasChinese &&
      (trimmed.startsWith('\\') ||
        /\\[a-zA-Z]+/.test(trimmed) ||
        (/^[a-zA-Z0-9\s\+\-\*\/\=\(\)\,\.\_\^]+$/.test(trimmed) && /[\^_\=]/.test(trimmed)));

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
  }, [content, inline]);

  return (
    <span
      className={`math-rendered leading-relaxed ${className}`}
      dangerouslySetInnerHTML={{ __html: renderedHtml }}
    />
  );
};
