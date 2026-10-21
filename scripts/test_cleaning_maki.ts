import { EXTRACTED_PAST_QUESTIONS } from '../src/data/pastQuestionsData';
import { KNOWLEDGE_BASE } from '../src/data/knowledgeBase';

function cleanMakiQuestion(q: any): any {
  const cleaned = { ...q };

  // 1. Clean answer if it has trailing lecture headers
  if (cleaned.answer && /^[A-D]\s*\n/.test(cleaned.answer)) {
    cleaned.answer = cleaned.answer.match(/^([A-D])/)[1];
  }

  // 2. Specific question answer cleanups
  if (cleaned.id === 'q-2017-1-10-25.1') {
    cleaned.content = '微分方程 $y\'\' + 2y\' + 3y = 0$ 的通解为 $y = \\underline{\\hspace{4em}}$。';
    cleaned.answer = '$y = e^{-x}(C_1 \\cos\\sqrt{2}x + C_2 \\sin\\sqrt{2}x)$（$C_1, C_2$ 为任意常数）';
    cleaned.pitfall = '（1）把 $\\sqrt{-8}$ 化简成 $2\\sqrt{2}i$ 时算错，写成 $\\pm\\sqrt{2}$ 或 $-1 \\pm 2\\sqrt{2}i$；（2）忘记写任意常数 $C_1, C_2$，或只写一个常数。填空题问「通解」，必须含两个独立任意常数。';
  }

  let text = cleaned.content || '';

  // 3. Remove null / control chars
  text = text.replace(/[\u0000-\u0008\u000b\u000c\u000e-\u001f]/g, '');

  // 4. Strip header cruft like:
  // 与xk 同阶　（习题集11.5）★☆☆☆☆
  // L11
  // 极限计算总攻略（一）：洛必达与未定式
  text = text.replace(/^[^\n]*?（习题集\d+\.\d+）[★☆\s]*\n?/g, '');
  text = text.replace(/^L\d+\n[^\n]+\n?/g, '');

  // Strip footer cruft like:
  // \nL43\n行列式
  text = text.replace(/\nL\d+\n[^\n]+$/g, '');

  // 5. Replace (\quad) with （　　）
  text = text.replace(/\(\\quad\)/g, '（　　）');

  // 6. Extract options (A) ... (B) ... (C) ... (D) ... if present
  const optMatch = text.match(/[\n\s]*\(A\)\s*([\s\S]*?)\s*\(B\)\s*([\s\S]*?)\s*\(C\)\s*([\s\S]*?)\s*\(D\)\s*([\s\S]*)$/);
  if (optMatch) {
    const stem = text.slice(0, optMatch.index).trim();
    const optA = optMatch[1].trim();
    const optB = optMatch[2].trim();
    const optC = optMatch[3].trim();
    const optD = optMatch[4].trim();

    cleaned.content = stem;
    cleaned.options = [optA, optB, optC, optD];
  } else {
    cleaned.content = text.trim();
  }

  return cleaned;
}

// Test on first 10 questions
console.log('Testing cleaning on samples:');
let count = 0;
for (const [nid, qlist] of Object.entries(EXTRACTED_PAST_QUESTIONS)) {
  for (const q of qlist) {
    if (/^q-\d{4}-\d+-\d+-\d+\.\d+$/.test(q.id)) {
      count++;
      const res = cleanMakiQuestion(q);
      if (res.options && res.options.length > 0) {
        console.log(`\n[${count}] ${q.id} (STEM):`);
        console.log(res.content);
        console.log('OPTIONS:', res.options);
      }
      if (count >= 15) break;
    }
  }
}
