# Paper Writing Skill Test Prompts

## Test 1: Introduction gap paragraph from outline

Prompt:
根据这个大纲，帮我写 Introduction 里的 gap paragraph，英文。

Expected behavior:
- Use `writing-paper`.
- Produce manuscript prose in English.
- Notes may be in Chinese.
- Make the gap specific and avoid unsupported novelty claims.

## Test 2: Problem Formulation scenario paragraph from bullets

Prompt:
根据这些 bullet points 写 Problem Formulation 开头的场景说明段：系统中有多个服务节点、随机需求、容量约束和延迟成本。

Expected behavior:
- Use `writing-paper`.
- Write prose before equations.
- Mark missing assumptions and definitions.

## Test 3: Mathematical modeling explanation

Prompt:
已知变量 x_ij 表示任务 i 是否分配给节点 j，约束包括容量、唯一分配和时间窗，请写数学建模说明段。

Expected behavior:
- Use `writing-paper`.
- Explain variables and constraints in prose.
- Avoid inventing full equations unless requested.

## Test 4: Polish English draft

Prompt:
Please polish this English draft for the Methodology section and improve paragraph logic.

Expected behavior:
- Use `writing-paper`.
- Preserve technical meaning.
- Improve structure, transitions, precision, and claim control.

## Test 5: Chinese draft to English manuscript prose

Prompt:
把下面中文草稿改写成英文论文正文，目标是 Results and Discussion。

Expected behavior:
- Use `writing-paper`.
- Produce English manuscript text.
- Explain changes and missing evidence in Chinese unless requested otherwise.

## Test 6: Results paragraph from experiment results

Prompt:
根据这些实验结果写 Results paragraph：我们的模型在三个场景下比 baseline 平均降低 12% 成本，但高负载场景优势下降。

Expected behavior:
- Use `writing-paper`.
- Report finding, compare baseline, interpret boundary, avoid overgeneralization.

## Test 7: Reduce overclaiming

Prompt:
请把这句话改得更稳妥：This method completely solves the scalability problem for all real-world networks.

Expected behavior:
- Use `writing-paper`.
- Weaken unsupported universal claims and explain claim-control change.

## Test 8: Negative case, complete outline

Prompt:
请根据我的研究主题设计完整论文大纲，包括图表和实验。

Expected behavior:
- Do not use `writing-paper`.
- Route to `writing-paper-outline`.
