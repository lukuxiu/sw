import json

with open('src/data/knowledgeBase.ts', 'r', encoding='utf-8') as f:
    kb_full = f.read().replace('\r\n', '\n')

prefix_kb = 'import { KnowledgeNode } from \'./types\';\n\nexport const KNOWLEDGE_BASE: Record<string, KnowledgeNode> = '
kb_import = kb_full.find("import { EXTRACTED_PAST_QUESTIONS }")
kb_semi = kb_full.rfind('};', 0, kb_import)
kb_json_str = kb_full[len(prefix_kb):kb_semi + 1].strip()

kb_data = json.loads(kb_json_str)
print(f"KNOWLEDGE_BASE loaded: {len(kb_data)} topics.")

with open('src/data/pastQuestionsData.ts', 'r', encoding='utf-8') as f:
    pq_full = f.read().replace('\r\n', '\n')

var_decl = 'export const EXTRACTED_PAST_QUESTIONS: Record<string, PastQuestionItem[]> = '
pq_start = pq_full.find(var_decl) + len(var_decl)
pq_json_str = pq_full[pq_start:].strip().rstrip(';')

pq_data = json.loads(pq_json_str)
print(f"EXTRACTED_PAST_QUESTIONS loaded: {len(pq_data)} topics.")
