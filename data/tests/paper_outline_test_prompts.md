# Paper Outline Skill Test Prompts

## Test 1: Full outline from topic

Prompt:
我想写一篇关于多智能体路径规划中冲突风险建模的论文，请帮我生成完整论文大纲。

Expected behavior:
- Use `writing-paper-outline`.
- Infer domain, paper type, method type, and validation assumptions.
- Output article positioning, storyline, section/subsection table, problem formulation plan, method plan, figures, experiments, appendix advice, and reviewer risks.

## Test 2: Outline from method and data

Prompt:
我有一个图神经网络方法和一组城市交通仿真数据，想写成论文，请帮我组织结构。

Expected behavior:
- Use `writing-paper-outline`.
- Treat method and data as inputs.
- Plan sections around problem, model, data, baselines, metrics, ablation, robustness, and limitations.

## Test 3: Problem Formulation focus

Prompt:
我的研究需要定义车辆调度优化问题，请重点帮我设计 Problem Formulation 部分。

Expected behavior:
- Use `writing-paper-outline`.
- Focus on scenario, assumptions, sets, parameters, variables, objectives, constraints, and mapping back to the real problem.

## Test 4: Experiment Design focus

Prompt:
请帮我规划实验设计，已有算法和仿真平台，但不知道 baselines、metrics、ablation 怎么组织。

Expected behavior:
- Use `writing-paper-outline`.
- Emphasize validation logic, baselines, metrics, ablation, sensitivity, robustness, runtime, and practical interpretation.

## Test 5: Negative case, polishing prose

Prompt:
请润色下面这段 Introduction 英文，使其更像论文正文。

Expected behavior:
- Do not use `writing-paper-outline`.
- Route to `writing-paper`.

## Test 6: Negative case, citation search

Prompt:
请帮我找 20 篇最新引用，用于 Related Work。

Expected behavior:
- Do not use `writing-paper-outline`.
- Use a citation/search workflow if available. Do not produce a manuscript outline unless the user asks for one.
