import { LearningStatus } from './types';
import { KNOWLEDGE_BASE } from './knowledgeBase';

const STORAGE_KEY = 'kaoyan_math1_learning_status';

export function getAllLearningStatuses(): Record<string, LearningStatus> {
  try {
    const raw = localStorage.getItem(STORAGE_KEY);
    if (!raw) return {};
    return JSON.parse(raw);
  } catch (e) {
    console.error('Failed to read learning status from localStorage', e);
    return {};
  }
}

export function getLearningStatus(nodeId: string): LearningStatus {
  const all = getAllLearningStatuses();
  return all[nodeId] || 'unlearned';
}

export function setLearningStatus(nodeId: string, status: LearningStatus): void {
  try {
    const all = getAllLearningStatuses();
    all[nodeId] = status;
    localStorage.setItem(STORAGE_KEY, JSON.stringify(all));
    // Dispatch custom event so reactive components update immediately
    window.dispatchEvent(new Event('learning-status-change'));
  } catch (e) {
    console.error('Failed to save learning status', e);
  }
}

export function getChapterProgress(topicIds: string[]) {
  const all = getAllLearningStatuses();
  let mastered = 0;
  let struggling = 0;
  let unlearned = 0;

  for (const tid of topicIds) {
    const s = all[tid] || 'unlearned';
    if (s === 'mastered') mastered++;
    else if (s === 'struggling') struggling++;
    else unlearned++;
  }

  return {
    total: topicIds.length,
    mastered,
    struggling,
    unlearned,
    percentage: topicIds.length > 0 ? Math.round((mastered / topicIds.length) * 100) : 0,
  };
}

export function getOverallProgress() {
  const allIds = Object.keys(KNOWLEDGE_BASE);
  return getChapterProgress(allIds);
}
