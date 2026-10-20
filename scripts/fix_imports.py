import sys

# 1. Update KnowledgeDetailView.tsx
with open('src/components/KnowledgeDetailView.tsx', 'r', encoding='utf-8') as f:
    k_content = f.read()

k_content = k_content.replace(
    "import React, { useState, useEffect } from 'react';",
    "import React, { useState, useEffect, useMemo } from 'react';"
)
k_content = k_content.replace(
    "import { LearningStatus, MistakeTag } from '../data/types';",
    "import { LearningStatus, MistakeTag, PastQuestion } from '../data/types';"
)
k_content = k_content.replace(
    "filteredPastQuestions.map((q) => {",
    "filteredPastQuestions.map((q: PastQuestion) => {"
)
k_content = k_content.replace(
    "q.options.map((opt, i) => (",
    "q.options.map((opt: string, i: number) => ("
)
k_content = k_content.replace(
    "q.solutionSteps.map((s, stepIdx) => (",
    "q.solutionSteps.map((s: string, stepIdx: number) => ("
)
with open('src/components/KnowledgeDetailView.tsx', 'w', encoding='utf-8') as f:
    f.write(k_content)

print("KnowledgeDetailView.tsx updated successfully.")

# 2. Update featureIndex.ts
with open('src/data/featureIndex.ts', 'r', encoding='utf-8') as f:
    f_content = f.read()

f_content = f_content.replace(
    "category: q.category,",
    "category: q.category as ('数一' | '数二' | '数三'),"
)
f_content = f_content.replace(
    "paperSet.add(q.category);",
    "paperSet.add(q.category as ('数一' | '数二' | '数三'));"
)
with open('src/data/featureIndex.ts', 'w', encoding='utf-8') as f:
    f.write(f_content)

print("featureIndex.ts updated successfully.")
