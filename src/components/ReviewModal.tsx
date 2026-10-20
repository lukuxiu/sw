import React, { useState, useMemo, useRef } from 'react';
import { 
  X, CheckCircle2, HelpCircle, ArrowRight, Award, Download, Upload, Copy, Check, Clock, AlertTriangle
} from 'lucide-react';
import { KNOWLEDGE_BASE } from '../data/knowledgeBase';
import { LearningStatus, TopicRecord } from '../data/types';
import { MathView } from './MathView';
import { 
  getAllTopicRecords, getOverallProgress, setLearningStatus, 
  exportLearningData, importLearningData 
} from '../data/storage';

interface ReviewModalProps {
  isOpen: boolean;
  onClose: () => void;
  onSelectTopic: (topicId: string) => void;
}

function formatTimeAgo(timestamp?: number): string {
  if (!timestamp) return '未复习';
  const diffSec = Math.floor((Date.now() - timestamp) / 1000);
  if (diffSec < 60) return '刚刚';
  const diffMin = Math.floor(diffSec / 60);
  if (diffMin < 60) return `${diffMin} 分钟前`;
  const diffHour = Math.floor(diffMin / 60);
  if (diffHour < 24) return `${diffHour} 小时前`;
  const diffDay = Math.floor(diffHour / 24);
  return `${diffDay} 天前`;
}

export const ReviewModal: React.FC<ReviewModalProps> = ({
  isOpen,
  onClose,
  onSelectTopic,
}) => {
  if (!isOpen) return null;

  const [filter, setFilter] = useState<'all' | LearningStatus>('struggling');
  const [sortBy, setSortBy] = useState<'default' | 'oldest'>('default');
  const [records, setRecords] = useState(getAllTopicRecords());
  const [isBackupPanelOpen, setIsBackupPanelOpen] = useState(false);
  const [importJsonText, setImportJsonText] = useState('');
  const [backupMessage, setBackupMessage] = useState<{ type: 'success' | 'error'; text: string } | null>(null);
  const [isCopied, setIsCopied] = useState(false);

  const fileInputRef = useRef<HTMLInputElement>(null);

  const progress = useMemo(() => getOverallProgress(), [records]);

  const allTopics = useMemo(() => {
    return Object.values(KNOWLEDGE_BASE);
  }, []);

  const filteredTopics = useMemo(() => {
    let list = allTopics.filter((t) => {
      const s = records[t.id]?.status || 'unlearned';
      if (filter === 'all') return true;
      return s === filter;
    });

    if (sortBy === 'oldest') {
      // Sort by lastReviewedAt ascending (oldest or unreviewed first)
      list = [...list].sort((a, b) => {
        const timeA = records[a.id]?.lastReviewedAt || 0;
        const timeB = records[b.id]?.lastReviewedAt || 0;
        return timeA - timeB;
      });
    }

    return list;
  }, [allTopics, records, filter, sortBy]);

  const handleUpdateStatus = (nodeId: string, s: LearningStatus) => {
    setLearningStatus(nodeId, s);
    setRecords(getAllTopicRecords());
  };

  const handleExport = () => {
    const jsonStr = exportLearningData();
    // Copy to clipboard
    navigator.clipboard?.writeText(jsonStr).then(() => {
      setIsCopied(true);
      setTimeout(() => setIsCopied(false), 2000);
    });

    // Download file
    const blob = new Blob([jsonStr], { type: 'application/json' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = `kaoyan_math_progress_${new Date().toISOString().slice(0, 10)}.json`;
    a.click();
    URL.revokeObjectURL(url);
    setBackupMessage({ type: 'success', text: '备份文件已下载，同时已复制到剪贴板！' });
  };

  const handleImportText = () => {
    if (!importJsonText.trim()) {
      setBackupMessage({ type: 'error', text: '请输入或粘贴 JSON 备份数据' });
      return;
    }
    const res = importLearningData(importJsonText);
    if (res.success) {
      setRecords(getAllTopicRecords());
      setBackupMessage({ type: 'success', text: res.message });
      setImportJsonText('');
      setTimeout(() => setIsBackupPanelOpen(false), 1500);
    } else {
      setBackupMessage({ type: 'error', text: res.message });
    }
  };

  const handleFileUpload = (e: React.ChangeEvent<HTMLInputElement>) => {
    const file = e.target.files?.[0];
    if (!file) return;
    const reader = new FileReader();
    reader.onload = (event) => {
      const content = event.target?.result as string;
      if (content) {
        const res = importLearningData(content);
        if (res.success) {
          setRecords(getAllTopicRecords());
          setBackupMessage({ type: 'success', text: res.message });
          setTimeout(() => setIsBackupPanelOpen(false), 1500);
        } else {
          setBackupMessage({ type: 'error', text: res.message });
        }
      }
    };
    reader.readAsText(file);
  };

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center p-2 sm:p-4 bg-black/60 backdrop-blur-xs font-body">
      <div className="bg-[var(--sheet)] border border-[var(--line)] rounded-[14px] w-full max-w-3xl max-h-[90vh] sm:max-h-[85vh] flex flex-col shadow-2xl overflow-hidden">
        {/* Modal Header */}
        <div className="px-4 sm:px-6 py-3 sm:py-4 bg-[var(--well)] border-b border-[var(--line)] flex items-center justify-between">
          <div className="flex items-center gap-2.5">
            <div className="p-1.5 rounded-[6px] bg-[var(--sheet)] text-[var(--blue)] border border-[var(--line)]">
              <Award className="w-4 h-4" />
            </div>
            <div>
              <div className="flex items-center gap-2">
                <h2 className="text-base font-display font-bold text-[var(--ink)] tracking-tight">
                  复习与薄弱点清单 (Review Hub)
                </h2>
                <button
                  onClick={() => setIsBackupPanelOpen(!isBackupPanelOpen)}
                  className="text-[11px] font-mono px-2 py-0.5 rounded bg-[var(--sheet)] text-[var(--blue)] border border-[var(--line)] hover:border-[var(--blue)] transition-colors"
                >
                  {isBackupPanelOpen ? '返回清单' : '备份与同步'}
                </button>
              </div>
              <p className="text-[11px] text-[var(--muted)] font-mono">
                定位推导困难点，按图索骥攻克薄弱环节
              </p>
            </div>
          </div>
          <button
            onClick={onClose}
            className="p-1.5 rounded-[6px] text-[var(--muted)] hover:text-[var(--ink)] hover:bg-[var(--line)] transition-colors"
          >
            <X className="w-4 h-4" />
          </button>
        </div>

        {/* BACKUP & RESTORE PANEL */}
        {isBackupPanelOpen ? (
          <div className="flex-1 overflow-y-auto p-4 sm:p-6 space-y-4">
            <div className="bg-[var(--well)] p-4 rounded-[12px] border border-[var(--line)] space-y-2">
              <h3 className="text-xs font-bold text-[var(--ink)] font-mono flex items-center gap-1.5">
                <Download className="w-3.5 h-3.5 text-[var(--blue)]" />
                <span>导出当前学习进度 (跨设备备份)</span>
              </h3>
              <p className="text-xs text-[var(--muted)] font-body leading-relaxed">
                考研复习周期长，避免因清理浏览器缓存或在手机/电脑间切换丢失进度。一键下载 JSON 备份，也可直接通过微信/便签发送给自己。
              </p>
              <div className="pt-1 flex items-center gap-2">
                <button
                  onClick={handleExport}
                  className="flex items-center gap-1.5 px-3.5 py-1.5 rounded-[6px] bg-[var(--ink)] text-[var(--paper)] text-xs font-mono font-bold hover:opacity-90 transition-opacity"
                >
                  {isCopied ? <Check className="w-3.5 h-3.5 text-[var(--green)]" /> : <Download className="w-3.5 h-3.5" />}
                  <span>{isCopied ? '已复制并下载！' : '下载并复制进度 JSON'}</span>
                </button>
              </div>
            </div>

            <div className="bg-[var(--well)] p-4 rounded-[12px] border border-[var(--line)] space-y-3">
              <h3 className="text-xs font-bold text-[var(--ink)] font-mono flex items-center gap-1.5">
                <Upload className="w-3.5 h-3.5 text-[var(--green)]" />
                <span>恢复 / 导入备份数据</span>
              </h3>
              <p className="text-xs text-[var(--muted)] font-body leading-relaxed">
                上传之前下载的 `.json` 备份文件，或者直接在下方文本框中粘贴备份代码：
              </p>

              <div className="flex items-center gap-2">
                <button
                  onClick={() => fileInputRef.current?.click()}
                  className="flex items-center gap-1.5 px-3 py-1.5 rounded-[6px] bg-[var(--sheet)] hover:bg-[var(--line)] border border-[var(--line)] text-xs font-mono text-[var(--ink)] transition-colors"
                >
                  <Upload className="w-3.5 h-3.5 text-[var(--muted)]" />
                  <span>选择文件上传</span>
                </button>
                <input
                  ref={fileInputRef}
                  type="file"
                  accept=".json,application/json"
                  className="hidden"
                  onChange={handleFileUpload}
                />
              </div>

              <div className="space-y-1.5 pt-1">
                <textarea
                  rows={3}
                  placeholder="或者在此粘贴导出的 JSON 文本..."
                  value={importJsonText}
                  onChange={(e) => setImportJsonText(e.target.value)}
                  className="w-full bg-[var(--sheet)] border border-[var(--line)] rounded-[8px] p-2.5 text-xs font-mono text-[var(--ink)] placeholder-[var(--muted)] focus:outline-none"
                />
                <button
                  onClick={handleImportText}
                  className="px-4 py-1.5 rounded-[6px] bg-[var(--blue)] text-white text-xs font-mono font-bold hover:opacity-90 transition-opacity"
                >
                  解析并导入进度
                </button>
              </div>
            </div>

            {backupMessage && (
              <div
                className={`p-3 rounded-[8px] border text-xs font-mono flex items-center gap-2 ${
                  backupMessage.type === 'success'
                    ? 'bg-[var(--green-bg)] text-[var(--green)] border-[var(--green)]'
                    : 'bg-[var(--amber-bg)] text-[var(--amber)] border-[var(--amber)]'
                }`}
              >
                <span>{backupMessage.text}</span>
              </div>
            )}
          </div>
        ) : (
          /* REGULAR REVIEW HUB LIST */
          <>
            {/* Overview Stats Bar */}
            <div className="px-4 sm:px-6 py-2.5 sm:py-3 bg-[var(--sheet)] border-b border-[var(--line)] flex flex-wrap items-center justify-between gap-2 sm:gap-4 font-mono text-xs">
              <div className="flex items-center gap-3 sm:gap-4">
                <div>
                  <span className="text-[var(--muted)]">已掌握: </span>
                  <span className="font-bold text-[var(--ink)]">
                    {progress.mastered} / {progress.total}
                  </span>
                </div>
                <div className="h-4 w-px bg-[var(--line)]" />
                <div>
                  <span className="text-[var(--amber)]">推导困难: </span>
                  <span className="font-bold text-[var(--amber)]">
                    {progress.struggling}
                  </span>
                </div>
              </div>

              {/* Filter tabs & Sorting */}
              <div className="flex items-center gap-1.5 flex-wrap">
                <div className="flex items-center gap-1 bg-[var(--well)] p-0.5 rounded-[8px] border border-[var(--line)] text-[11px]">
                  <button
                    onClick={() => setFilter('struggling')}
                    className={`px-2 py-0.8 rounded-[6px] transition-colors ${
                      filter === 'struggling'
                        ? 'bg-[var(--amber-bg)] text-[var(--amber)] font-bold border border-[var(--amber)]'
                        : 'text-[var(--muted)] hover:text-[var(--ink)]'
                    }`}
                  >
                    <span className="hidden sm:inline">推导困难</span><span className="inline sm:hidden">困难</span> ({progress.struggling})
                  </button>
                  <button
                    onClick={() => setFilter('mastered')}
                    className={`px-2 py-0.8 rounded-[6px] transition-colors ${
                      filter === 'mastered'
                        ? 'bg-[var(--green-bg)] text-[var(--green)] font-bold border border-[var(--green)]'
                        : 'text-[var(--muted)] hover:text-[var(--ink)]'
                    }`}
                  >
                    <span className="hidden sm:inline">已完全掌握</span><span className="inline sm:hidden">已掌握</span> ({progress.mastered})
                  </button>
                  <button
                    onClick={() => setFilter('all')}
                    className={`px-2 py-0.8 rounded-[6px] transition-colors ${
                      filter === 'all'
                        ? 'bg-[var(--sheet)] text-[var(--ink)] font-bold shadow-sm'
                        : 'text-[var(--muted)] hover:text-[var(--ink)]'
                    }`}
                  >
                    全部 ({progress.total})
                  </button>
                </div>

                {/* Sort By time toggle */}
                <button
                  onClick={() => setSortBy(sortBy === 'default' ? 'oldest' : 'default')}
                  className={`flex items-center gap-1 px-2 py-1 rounded-[6px] border text-[11px] font-mono transition-colors ${
                    sortBy === 'oldest'
                      ? 'bg-[var(--sheet)] text-[var(--blue)] border-[var(--blue)] font-bold'
                      : 'bg-[var(--well)] text-[var(--muted)] border-[var(--line)]'
                  }`}
                  title="按艾宾浩斯记忆曲线：优先复习最久未看考点"
                >
                  <Clock className="w-3 h-3" />
                  <span>{sortBy === 'oldest' ? '遗忘优先' : '默认排序'}</span>
                </button>
              </div>
            </div>

            {/* Topic List */}
            <div className="flex-1 overflow-y-auto p-3 sm:p-6 space-y-2 sm:space-y-2.5">
              {filteredTopics.length === 0 ? (
                <div className="text-center py-12 text-[var(--muted)] font-mono text-xs space-y-1">
                  <p>暂无该状态下的考点</p>
                  <p className="text-[var(--muted)]">
                    做题或复习时可在考点详情页点击“推导困难”进行归集。
                  </p>
                </div>
              ) : (
                filteredTopics.map((topic) => {
                  const rec = records[topic.id] || { status: 'unlearned' };
                  const s = rec.status;

                  return (
                    <div
                      key={topic.id}
                      className="bg-[var(--well)] border border-[var(--line)] hover:border-[var(--blue)] p-3 sm:p-3.5 rounded-[10px] flex flex-col sm:flex-row sm:items-center justify-between gap-2.5 sm:gap-3 transition-colors"
                    >
                      <div className="flex-1">
                        <div className="flex items-center gap-2 flex-wrap">
                          <span 
                            className="text-xs font-semibold text-[var(--ink)] hover:text-[var(--blue)] cursor-pointer"
                            onClick={() => { onSelectTopic(topic.id); onClose(); }}
                          >
                            {topic.title}
                          </span>
                          <span className="text-[10px] font-mono px-1.5 py-0.2 rounded bg-[var(--sheet)] text-[var(--muted)] border border-[var(--line)]">
                            {topic.subjectName} · {topic.chapterTitle}
                          </span>
                          <span className="text-[10px] font-mono text-[var(--muted)]">
                            上次: {formatTimeAgo(rec.lastReviewedAt)}
                          </span>
                        </div>
                        <div className="text-xs text-[var(--muted)] mt-1 line-clamp-1 leading-relaxed font-body">
                          <MathView content={topic.summary} inline />
                        </div>
                        {rec.mistakeTags && rec.mistakeTags.length > 0 && (
                          <div className="flex items-center gap-1 mt-1.5 flex-wrap">
                            {rec.mistakeTags.map((mt, mi) => (
                              <span key={mi} className="text-[10px] font-mono px-1 py-0.2 rounded bg-[var(--amber-bg)] text-[var(--amber)] border border-[var(--amber)]">
                                {mt}
                              </span>
                            ))}
                          </div>
                        )}
                      </div>

                      {/* Actions */}
                      <div className="flex items-center justify-between sm:justify-end gap-2 flex-shrink-0 font-mono text-xs mt-2 sm:mt-0 pt-2 sm:pt-0 border-t sm:border-0 border-[var(--line)]">
                        <div className="flex items-center gap-1 bg-[var(--sheet)] p-0.5 rounded-[6px] border border-[var(--line)]">
                          <button
                            onClick={() => handleUpdateStatus(topic.id, 'struggling')}
                            className={`px-1.5 py-0.5 rounded-[4px] text-[11px] ${
                              s === 'struggling' ? 'bg-[var(--amber-bg)] text-[var(--amber)] font-bold border border-[var(--amber)]' : 'text-[var(--muted)] hover:text-[var(--ink)]'
                            }`}
                            title="标记为推导困难"
                          >
                            困难
                          </button>
                          <button
                            onClick={() => handleUpdateStatus(topic.id, 'mastered')}
                            className={`px-1.5 py-0.5 rounded-[4px] text-[11px] ${
                              s === 'mastered' ? 'bg-[var(--green-bg)] text-[var(--green)] font-bold border border-[var(--green)]' : 'text-[var(--muted)] hover:text-[var(--ink)]'
                            }`}
                            title="标记为能够独立完成"
                          >
                            已掌握
                          </button>
                        </div>

                        <button
                          onClick={() => {
                            onSelectTopic(topic.id);
                            onClose();
                          }}
                          className="flex items-center gap-1 px-3 py-1.5 rounded-[6px] bg-[var(--ink)] hover:opacity-90 text-[var(--paper)] text-xs font-bold transition-all"
                        >
                          <span>前往推导</span>
                          <ArrowRight className="w-3 h-3" />
                        </button>
                      </div>
                    </div>
                  );
                })
              )}
            </div>
          </>
        )}
      </div>
    </div>
  );
};
