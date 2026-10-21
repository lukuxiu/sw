import katex from 'katex';

const s1 = `f(x)=\\begin{cases}0,&0\\le x\\lt\\frac12,\\\\x^2,&\\frac12\\le x\\le1,\n\\end{cases}`;
try {
  const html = katex.renderToString(s1, { displayMode: false, throwOnError: true });
  console.log('s1 passed, len:', html.length);
} catch (e: any) {
  console.error('s1 failed:', e.message);
}

const s2 = `S\\left(-\\frac72\\right)=\\underline{\\hspace{3em}}`;
try {
  const html2 = katex.renderToString(s2, { displayMode: false, throwOnError: true });
  console.log('s2 passed, len:', html2.length);
} catch (e: any) {
  console.error('s2 failed:', e.message);
}
