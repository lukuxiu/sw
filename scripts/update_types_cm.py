with open('src/data/types.ts', 'r', encoding='utf-8') as f:
    text = f.read()

old_cm = """export interface CandidateMethod {
  name: string;
  priority: number;
  condition: string;
  whyChoose: string;
  description: string;
}"""

new_cm = """export interface CandidateMethod {
  name: string;
  priority?: number;
  condition?: string;
  applicability?: string;
  whyChoose: string;
  description?: string;
  limitations?: string;
}"""

text = text.replace(old_cm, new_cm)

with open('src/data/types.ts', 'w', encoding='utf-8') as f:
    f.write(text)

print("Updated CandidateMethod in types.ts")
