import { KNOWLEDGE_BASE } from '../src/data/knowledgeBase';
import { EXTRACTED_PAST_QUESTIONS } from '../src/data/pastQuestionsData';

// Print samples of:
// 1. integral_symbol_caret (ˆ)
// 2. piecewise_brace_unicode
// 3. matrix_paren_unicode
// 4. broken_sqrt_newline
// 5. null_control_chars
// 6. exercise_header_cruft

function findSamples(type: string, regex: RegExp, max = 5) {
  console.log(`\n================ SAMPLES FOR ${type} ================`);
  let count = 0;
  for (const [nid, node] of Object.entries(KNOWLEDGE_BASE)) {
    for (const q of node.pastQuestions || []) {
      if (regex.test(q.content) || regex.test(q.answer) || regex.test(q.analysis || '')) {
        count++;
        console.log(`[${count}] ${q.id} (${q.year} ${q.category}) in ${nid}:`);
        console.log('CONTENT:\n', q.content.slice(0, 200));
        if (q.answer && regex.test(q.answer)) {
          console.log('ANSWER:\n', q.answer.slice(0, 150));
        }
        if (count >= max) return;
      }
    }
  }
}

findSamples('caret (integral)', /ˆ/);
findSamples('piecewise brace', /[]/);
findSamples('matrix paren', /[]/);
findSamples('broken sqrt', /√\s*\n/);
findSamples('exercise header cruft', /（习题集\d+\.\d+）/);
