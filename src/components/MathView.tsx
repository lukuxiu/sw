import React, { useMemo } from 'react';
import katex from 'katex';

interface MathViewProps {
  content: string;
  className?: string;
  inline?: boolean;
}

export const MathView: React.FC<MathViewProps> = ({ content, className = '', inline = false }) => {
  const renderedHtml = useMemo(() => {
    if (!content) return '';

    // If pure formula passed without delimiters and inline=true or false
    if (!content.includes('$')) {
      try {
        return katex.renderToString(content, {
          displayMode: !inline,
          throwOnError: false,
        });
      } catch (e) {
        return content;
      }
    }

    // Split text by $$...$$ (display math) and $...$ (inline math)
    const parts = content.split(/(\$\$[\s\S]*?\$\$|\$[^$\n]+\$)/g);

    return parts
      .map((part) => {
        if (part.startsWith('$$') && part.endsWith('$$')) {
          const math = part.slice(2, -2).trim();
          try {
            return katex.renderToString(math, { displayMode: true, throwOnError: false });
          } catch (e) {
            return part;
          }
        } else if (part.startsWith('$') && part.endsWith('$')) {
          const math = part.slice(1, -1).trim();
          try {
            return katex.renderToString(math, { displayMode: false, throwOnError: false });
          } catch (e) {
            return part;
          }
        } else {
          // Plain text - convert newlines to <br/> or escape html
          const escaped = part
            .replace(/&/g, '&amp;')
            .replace(/</g, '&lt;')
            .replace(/>/g, '&gt;')
            .replace(/\n/g, '<br/>');
          return escaped;
        }
      })
      .join('');
  }, [content, inline]);

  return (
    <span
      className={`math-rendered leading-relaxed ${className}`}
      dangerouslySetInnerHTML={{ __html: renderedHtml }}
    />
  );
};
