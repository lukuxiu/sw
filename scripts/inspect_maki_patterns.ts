import { EXTRACTED_PAST_QUESTIONS } from '../src/data/pastQuestionsData';

let headerCruftCount = 0;
let choiceCount = 0;
let caretCount = 0;
let casesCount = 0;
let matrixCount = 0;

for (const [nid, qlist] of Object.entries(EXTRACTED_PAST_QUESTIONS)) {
  for (const q of qlist) {
    if (!/^q-\d{4}-\d+-\d+-\d+\.\d+$/.test(q.id)) continue;
    
    if (/（习题集\d+\.\d+）|★|L\d+\n/.test(q.content)) {
      headerCruftCount++;
    }
    if (/\(A\)[\s\S]*?\(B\)[\s\S]*?\(C\)[\s\S]*?\(D\)/.test(q.content)) {
      choiceCount++;
    }
    if (/ˆ/.test(q.content)) {
      caretCount++;
    }
    if (/[]/.test(q.content)) {
      casesCount++;
    }
    if (/[]/.test(q.content)) {
      matrixCount++;
    }
  }
}

console.log(`Out of 275 Maki PDF questions:`);
console.log(`  Questions with Maki book header/footer cruft: ${headerCruftCount}`);
console.log(`  Questions with (A)(B)(C)(D) in content: ${choiceCount}`);
console.log(`  Questions with ˆ (integral): ${caretCount}`);
console.log(`  Questions with unicode cases brace: ${casesCount}`);
console.log(`  Questions with unicode matrix paren: ${matrixCount}`);
