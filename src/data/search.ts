import { SearchMatchItem } from './types';
import { KNOWLEDGE_BASE } from './knowledgeBase';
import { CHAPTERS, SUBJECTS } from './subjects';

export function searchKnowledgeBase(query: string): SearchMatchItem[] {
  const clean = query.trim().toLowerCase();
  if (!clean) return [];

  const results: SearchMatchItem[] = [];

  for (const [id, node] of Object.entries(KNOWLEDGE_BASE)) {
    // 1. Check title
    if (node.title.toLowerCase().includes(clean)) {
      results.push({
        nodeId: id,
        title: node.title,
        subjectName: node.subjectName,
        chapterTitle: node.chapterTitle,
        matchedField: 'title',
        snippet: node.title,
        subjectId: node.subject,
      });
      continue;
    }

    // 2. Check summary (一句话记忆)
    if (node.summary.toLowerCase().includes(clean)) {
      results.push({
        nodeId: id,
        title: node.title,
        subjectName: node.subjectName,
        chapterTitle: node.chapterTitle,
        matchedField: 'summary',
        snippet: node.summary,
        subjectId: node.subject,
      });
      continue;
    }

    // 3. Check triggers (触发信号)
    const matchedTrigger = node.triggers.find((t) => t.toLowerCase().includes(clean));
    if (matchedTrigger) {
      results.push({
        nodeId: id,
        title: node.title,
        subjectName: node.subjectName,
        chapterTitle: node.chapterTitle,
        matchedField: 'trigger',
        snippet: `触发信号: ${matchedTrigger}`,
        subjectId: node.subject,
      });
      continue;
    }

    // 4. Check candidate methods (解题方法)
    const matchedMethod = node.candidateMethods.find(
      (m) => m.name.toLowerCase().includes(clean) || m.condition.toLowerCase().includes(clean)
    );
    if (matchedMethod) {
      results.push({
        nodeId: id,
        title: node.title,
        subjectName: node.subjectName,
        chapterTitle: node.chapterTitle,
        matchedField: 'method',
        snippet: `方法: ${matchedMethod.name} (${matchedMethod.condition})`,
        subjectId: node.subject,
      });
      continue;
    }

    // 5. Check formulas (公式)
    const matchedFormula = node.formulas.find(
      (f) => f.title.toLowerCase().includes(clean) || f.latex.toLowerCase().includes(clean)
    );
    if (matchedFormula) {
      results.push({
        nodeId: id,
        title: node.title,
        subjectName: node.subjectName,
        chapterTitle: node.chapterTitle,
        matchedField: 'formula',
        snippet: `公式: ${matchedFormula.title}`,
        subjectId: node.subject,
      });
      continue;
    }

    // 6. Check past questions (年份、题号、内容)
    const matchedQuestion = node.pastQuestions.find(
      (q) =>
        q.year.includes(clean) ||
        q.questionNumber.includes(clean) ||
        q.content.toLowerCase().includes(clean) ||
        q.category.includes(clean)
    );
    if (matchedQuestion) {
      results.push({
        nodeId: id,
        title: node.title,
        subjectName: node.subjectName,
        chapterTitle: node.chapterTitle,
        matchedField: 'question',
        snippet: `真题: ${matchedQuestion.year} ${matchedQuestion.category} ${matchedQuestion.questionNumber}`,
        subjectId: node.subject,
      });
      continue;
    }

    // 7. Check tags
    const matchedTag = node.tags.find((t) => t.toLowerCase().includes(clean));
    if (matchedTag) {
      results.push({
        nodeId: id,
        title: node.title,
        subjectName: node.subjectName,
        chapterTitle: node.chapterTitle,
        matchedField: 'tag',
        snippet: `标签: #${matchedTag}`,
        subjectId: node.subject,
      });
      continue;
    }
  }

  return results;
}
