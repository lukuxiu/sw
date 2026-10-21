import { KNOWLEDGE_BASE } from '../src/data/knowledgeBase';
import { EXTRACTED_PAST_QUESTIONS } from '../src/data/pastQuestionsData';

// Classify question IDs into types
const qMap = new Map<string, any>();

for (const [nid, node] of Object.entries(KNOWLEDGE_BASE)) {
  for (const q of node.pastQuestions || []) {
    qMap.set(q.id, { q, source: 'KB', nid });
  }
}

for (const [nid, qlist] of Object.entries(EXTRACTED_PAST_QUESTIONS)) {
  for (const q of qlist) {
    if (!qMap.has(q.id)) {
      qMap.set(q.id, { q, source: 'EXTRACTED', nid });
    }
  }
}

console.log(`Total unique questions: ${qMap.size}`);

let makiPdfStyleCount = 0; // like q-2018-2-15-16.2
let standardKaoyanCount = 0; // like gaoshu-q-2021-1-1 or q-2021-1-1

const makiPdfQuestions: any[] = [];
const standardQuestions: any[] = [];

for (const [id, data] of qMap.entries()) {
  // If id matches q-\d{4}-\d+-\d+-\d+\.\d+
  if (/^q-\d{4}-\d+-\d+-\d+\.\d+$/.test(id)) {
    makiPdfStyleCount++;
    makiPdfQuestions.push(data);
  } else {
    standardKaoyanCount++;
    standardQuestions.push(data);
  }
}

console.log(`Maki PDF extracted style questions (q-YYYY-P-Q-LEC.X): ${makiPdfStyleCount}`);
console.log(`Standard / clean style questions: ${standardKaoyanCount}`);
