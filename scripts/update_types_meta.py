import re, sys

sys.stdout.reconfigure(encoding='utf-8')
with open('src/data/types.ts', 'r', encoding='utf-8') as f:
    text = f.read()

target = """  manifestations: {
    subjectId: SubjectId;
    subjectName: string;
    chapterTitle: string;
    topicId: string;
    topicTitle: string;
    triggerForm: string;
    coreAction: string;
  }[];
  commonPitfalls: string[];
}"""

replacement = """  manifestations: {
    subjectId: SubjectId;
    subjectName: string;
    chapterTitle: string;
    topicId: string;
    topicTitle: string;
    triggerForm: string;
    coreAction: string;
  }[];
  representativeQuestions?: {
    year: string;
    category: string;
    questionNumber: string;
    stem: string;
    methodUsage: string;
    topicId: string;
  }[];
  commonPitfalls: string[];
}"""

# Normalize CRLF
text_norm = text.replace('\r\n', '\n')
if target in text_norm:
    text_norm = text_norm.replace(target, replacement)
    with open('src/data/types.ts', 'w', encoding='utf-8') as f:
        f.write(text_norm)
    print("Updated src/data/types.ts successfully!")
else:
    print("Target not found in text_norm!")
