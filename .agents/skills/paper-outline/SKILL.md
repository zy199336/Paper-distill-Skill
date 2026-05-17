---
name: paper-outline
description: Draft source-grounded academic paper outlines from a research idea, topic, method, dataset, draft notes, or target venue. Use when the user wants section-by-section manuscript structure, subsection purposes, problem formulation design, methodology organization, figure/table planning, experiment planning, main-text vs appendix decisions, and reviewer-risk checks based on patterns extracted from a small local paper corpus.
---

# Paper Outline Skill

## Default stance

This skill drafts manuscript outlines, not full prose.

It uses source-grounded outline patterns extracted from the local paper corpus.

The outline should connect:
- research background
- specific problem
- gap
- problem formulation
- method or model
- validation
- results
- implication
- limitation

## Use when

Use this skill when the user asks to:
- design a paper outline;
- organize a manuscript;
- plan sections and subsections;
- decide what each section should contain;
- design Problem Formulation;
- plan figures and tables;
- plan experiments;
- check outline-level reviewer risks.

## Do not use when

Do not use this skill when:
- the user asks to write or polish final prose;
- the user asks for citation search only;
- the user asks for figure generation only;
- the task is unrelated to academic paper structuring.

## Inputs to infer

Try to identify:
- research topic;
- field/domain;
- target journal or venue if provided;
- paper type;
- method type;
- data or experiment setting;
- expected contribution;
- validation plan;
- existing notes or constraints.

If missing, make reasonable assumptions and mark them.

## Workflow

1. Identify paper type.
2. Identify likely corpus-derived style patterns.
3. Build the core storyline.
4. Select section sequence.
5. Design subsection functions.
6. Design Problem Formulation if relevant.
7. Plan Methodology / Model / Algorithm section.
8. Plan Experiment / Case Study / Validation.
9. Plan figures and tables.
10. Decide main text vs appendix.
11. Run reviewer-risk checklist.
12. Output a structured outline.

## References to consult

- references/outline_workflow.md
- references/section_templates.md
- references/problem_formulation_template.md
- references/method_section_template.md
- references/experiment_planning_template.md
- references/figure_table_planning.md
- references/reviewer_risk_checklist.md

## Output format

Always output in Chinese unless the user requests another language.

# 论文大纲建议

## 1. 文章定位
- 领域：
- 论文类型：
- 核心问题：
- 核心贡献：
- 主要方法：
- 验证方式：
- 推荐主线：

## 2. 推荐标题方向

Give 3-5 title directions.

## 3. 整体叙事链条

Background -> Gap -> Problem -> Formulation -> Method -> Validation -> Implication

## 4. Section-by-section outline

Use a table:
Section | Subsection | Purpose | What to write | Figures/Tables/Equations | Reviewer-risk notes

## 5. Problem Formulation 设计

If relevant, include:
- application scenario;
- assumptions;
- entities;
- sets and indices;
- parameters;
- variables;
- objective;
- constraints;
- mapping back to real problem.

## 6. Method / Model / Algorithm 设计

## 7. 图表规划

## 8. 实验与验证规划

## 9. Main text vs Appendix 建议

## 10. 审稿风险检查

## Quality checklist

Before final output, check:
- Is the research problem specific?
- Does the outline match the paper type?
- Is Problem Formulation readable before equations?
- Does Methodology follow from the formulation?
- Does validation test the stated contribution?
- Are figures/tables part of the argument?
- Are claims matched to evidence?
- Are assumptions marked?
