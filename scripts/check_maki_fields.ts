import { EXTRACTED_PAST_QUESTIONS } from '../src/data/pastQuestionsData';

let totalMaki = 0;
let withContent = 0;
let withOptions = 0;
let withAnalysis = 0;
let withAnswer = 0;
let withSteps = 0;

for (const [nid, qlist] of Object.entries(EXTRACTED_PAST_QUESTIONS)) {
  for (const q of qlist) {
    if (/^q-\d{4}-\d+-\d+-\d+\.\d+$/.test(q.id)) {
      totalMaki++;
      if (q.content) withContent++;
      if (q.options && q.options.length > 0) withOptions++;
      if (q.analysis) withAnalysis++;
      if (q.answer) withAnswer++;
      if (q.solutionSteps && q.solutionSteps.length > 0) withSteps++;
    }
  }
}

console.log(`Maki questions in EXTRACTED: ${totalMaki}`);
console.log(`  with content: ${withContent}`);
console.log(`  with options: ${withOptions}`);
console.log(`  with analysis: ${withAnalysis}`);
console.log(`  with answer: ${withAnswer}`);
console.log(`  with steps: ${withSteps}`);
