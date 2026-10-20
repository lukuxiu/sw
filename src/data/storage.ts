import { LearningStatus, TopicRecord, MistakeTag } from './types';
import { KNOWLEDGE_BASE } from './knowledgeBase';

const STATUS_STORAGE_KEY = 'kaoyan_math1_learning_status';
const RECORDS_STORAGE_KEY = 'kaoyan_math1_learning_records_v2';

export function getAllTopicRecords(): Record<string, TopicRecord> {
  try {
    const raw = localStorage.getItem(RECORDS_STORAGE_KEY);
    if (raw) {
      return JSON.parse(raw);
    }
  } catch (e) {
    console.error('Failed to read learning records', e);
  }

  // Fallback to legacy statuses if v2 records don't exist yet
  try {
    const legacyRaw = localStorage.getItem(STATUS_STORAGE_KEY);
    if (legacyRaw) {
      const legacyMap: Record<string, LearningStatus> = JSON.parse(legacyRaw);
      const migrated: Record<string, TopicRecord> = {};
      for (const [id, s] of Object.entries(legacyMap)) {
        migrated[id] = { status: s, reviewCount: 1, lastReviewedAt: Date.now() };
      }
      return migrated;
    }
  } catch (e) {
    console.error('Failed to migrate legacy learning status', e);
  }

  return {};
}

export function getAllLearningStatuses(): Record<string, LearningStatus> {
  const records = getAllTopicRecords();
  const statuses: Record<string, LearningStatus> = {};
  for (const [id, rec] of Object.entries(records)) {
    statuses[id] = rec.status;
  }
  return statuses;
}

export function getLearningStatus(nodeId: string): LearningStatus {
  const records = getAllTopicRecords();
  return records[nodeId]?.status || 'unlearned';
}

export function getTopicRecord(nodeId: string): TopicRecord {
  const records = getAllTopicRecords();
  return records[nodeId] || { status: 'unlearned', reviewCount: 0 };
}

export function setLearningStatus(
  nodeId: string,
  status: LearningStatus,
  mistakeTags?: MistakeTag[]
): void {
  try {
    const records = getAllTopicRecords();
    const current = records[nodeId] || { status: 'unlearned', reviewCount: 0 };

    records[nodeId] = {
      ...current,
      status,
      lastReviewedAt: Date.now(),
      reviewCount: (current.reviewCount || 0) + 1,
      mistakeTags: mistakeTags !== undefined ? mistakeTags : current.mistakeTags || [],
    };

    localStorage.setItem(RECORDS_STORAGE_KEY, JSON.stringify(records));

    // Also mirror to legacy key for backward compatibility
    const legacyStatuses: Record<string, LearningStatus> = {};
    for (const [id, rec] of Object.entries(records)) {
      legacyStatuses[id] = rec.status;
    }
    localStorage.setItem(STATUS_STORAGE_KEY, JSON.stringify(legacyStatuses));

    // Dispatch event for UI reactivity
    window.dispatchEvent(new Event('learning-status-change'));
  } catch (e) {
    console.error('Failed to save learning status', e);
  }
}

export function setTopicMistakeTags(nodeId: string, tags: MistakeTag[]): void {
  try {
    const records = getAllTopicRecords();
    const current = records[nodeId] || { status: 'unlearned', reviewCount: 0 };
    records[nodeId] = {
      ...current,
      mistakeTags: tags,
      lastReviewedAt: Date.now(),
    };
    localStorage.setItem(RECORDS_STORAGE_KEY, JSON.stringify(records));
    window.dispatchEvent(new Event('learning-status-change'));
  } catch (e) {
    console.error('Failed to update mistake tags', e);
  }
}

export function getChapterProgress(topicIds: string[]) {
  const records = getAllTopicRecords();
  let mastered = 0;
  let struggling = 0;
  let unlearned = 0;

  for (const tid of topicIds) {
    const s = records[tid]?.status || 'unlearned';
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

// === EXPORT & IMPORT BACKUP ===
export interface ExportPayload {
  app: string;
  version: string;
  exportedAt: string;
  stats: {
    total: number;
    mastered: number;
    struggling: number;
  };
  records: Record<string, TopicRecord>;
}

export function exportLearningData(): string {
  const records = getAllTopicRecords();
  const progress = getOverallProgress();

  const payload: ExportPayload = {
    app: 'Maki-Kaoyan-Math1',
    version: '2.0.0',
    exportedAt: new Date().toISOString(),
    stats: {
      total: progress.total,
      mastered: progress.mastered,
      struggling: progress.struggling,
    },
    records,
  };

  return JSON.stringify(payload, null, 2);
}

export function importLearningData(jsonString: string): {
  success: boolean;
  count: number;
  message: string;
} {
  try {
    const data = JSON.parse(jsonString);
    if (!data || typeof data !== 'object') {
      return { success: false, count: 0, message: '无效的 JSON 数据格式' };
    }

    // Support either direct { [nodeId]: 'mastered' } or full ExportPayload { records: { ... } }
    let targetRecords: Record<string, TopicRecord> = {};

    if (data.records && typeof data.records === 'object') {
      targetRecords = data.records;
    } else {
      // Direct key-value map
      for (const [k, v] of Object.entries(data)) {
        if (typeof v === 'string') {
          targetRecords[k] = {
            status: v as LearningStatus,
            lastReviewedAt: Date.now(),
            reviewCount: 1,
          };
        } else if (v && typeof v === 'object' && 'status' in v) {
          targetRecords[k] = v as TopicRecord;
        }
      }
    }

    const count = Object.keys(targetRecords).length;
    if (count === 0) {
      return { success: false, count: 0, message: '备份数据为空，未找到考点记录' };
    }

    // Save to storage
    localStorage.setItem(RECORDS_STORAGE_KEY, JSON.stringify(targetRecords));

    const legacyStatuses: Record<string, LearningStatus> = {};
    for (const [id, rec] of Object.entries(targetRecords)) {
      legacyStatuses[id] = rec.status;
    }
    localStorage.setItem(STATUS_STORAGE_KEY, JSON.stringify(legacyStatuses));

    window.dispatchEvent(new Event('learning-status-change'));
    return { success: true, count, message: `成功导入 ${count} 条考点学习进度！` };
  } catch (err: any) {
    return { success: false, count: 0, message: `解析失败：${err.message || '格式错误'}` };
  }
}
