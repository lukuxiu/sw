import { KNOWLEDGE_BASE } from '../src/data/knowledgeBase';
import { EXTRACTED_PAST_QUESTIONS } from '../src/data/pastQuestionsData';

const dirtyAnswers: any[] = [];
const brokenFormulas: any[] = [];

function auditQ(q: any, src: string, nid: string) {
  // 1. Check answer starting with [A-D] followed by newline
  if (q.answer && /^[A-D]\s*\n/.test(q.answer)) {
    dirtyAnswers.push({
      qId: q.id,
      year: q.year,
      category: q.category,
      src,
      nid,
      type: 'CHOICE_ANSWER_TRAILING_TEXT',
      raw: q.answer,
    });
  }

  // 2. Check if answer contains raw PDF artifacts like √ followed by newline or 
  if (q.answer && (/√\s*\n/.test(q.answer) || /[]/.test(q.answer))) {
    dirtyAnswers.push({
      qId: q.id,
      year: q.year,
      category: q.category,
      src,
      nid,
      type: 'PDF_OCR_ARTIFACT_IN_ANSWER',
      raw: q.answer.slice(0, 100),
    });
  }

  // 3. Check content for PDF OCR artifacts
  if (q.content && (/[]/.test(q.content) || /√\s*\n/.test(q.content))) {
    brokenFormulas.push({
      qId: q.id,
      year: q.year,
      category: q.category,
      src,
      nid,
      type: 'PDF_OCR_ARTIFACT_IN_CONTENT',
      raw: q.content.slice(0, 100),
    });
  }
}

for (const [nid, node] of Object.entries(KNOWLEDGE_BASE)) {
  for (const q of node.pastQuestions || []) {
    auditQ(q, 'KB', nid);
  }
}

for (const [nid, qlist] of Object.entries(EXTRACTED_PAST_QUESTIONS)) {
  for (const q of qlist) {
    auditQ(q, 'EXT', nid);
  }
}

console.log(`Total dirty answers: ${dirtyAnswers.length}`);
dirtyAnswers.forEach((d, i) => {
  console.log(`[#${i + 1}] (${d.qId} in ${d.nid}) ${d.year} ${d.category} [${d.type}]:`);
  console.log(`     Raw: ${JSON.stringify(d.raw)}`);
});

console.log(`\nTotal broken content: ${brokenFormulas.length}`);
brokenFormulas.forEach((b, i) => {
  console.log(`[#${i + 1}] (${b.qId} in ${b.nid}) ${b.year} ${b.category} [${b.type}]:`);
  console.log(`     Raw: ${JSON.stringify(b.raw)}`);
});
