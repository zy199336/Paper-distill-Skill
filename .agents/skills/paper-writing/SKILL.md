---
name: paper-writing
description: Write, rewrite, polish, expand, or structurally improve academic manuscript text from an outline, section purpose, rough idea, bullet points, Chinese draft, or English draft. Use when the user wants source-grounded paper-style prose for Abstract, Introduction, Gap, Contributions, Problem Formulation, Methodology, Experiments, Results, Discussion, Conclusion, transitions, claim control, or reviewer-risk reduction based on patterns extracted from a small local paper corpus.
---

# Paper Writing Skill

## Default stance

This skill writes or revises manuscript text according to an existing or inferred outline.

It is not a generic grammar-polishing skill.

It uses writing patterns extracted from the local paper corpus.

The writing should connect:
- research context
- specific problem
- gap
- contribution
- formulation
- method
- evidence
- implication
- limitation

## Relationship with paper-outline

Use paper-outline when the user needs:
- full manuscript structure;
- section sequence;
- subsection planning;
- figure/table planning;
- experiment planning.

Use paper-writing when the user needs:
- paragraph writing;
- section drafting;
- polishing;
- restructuring;
- expansion from rough ideas;
- alignment with an existing outline;
- claim control;
- transition improvement.

If no outline is provided, infer a minimal local outline and mark assumptions.

## Use when

Use this skill when the user asks to:
- write a section from an outline;
- expand bullet points into manuscript prose;
- polish a draft;
- restructure paragraphs;
- write gap or contribution paragraphs;
- write Problem Formulation prose;
- write Methodology;
- interpret results;
- write Discussion or Limitations;
- reduce overclaiming;
- improve academic style.

## Do not use when

Do not use this skill when:
- the user asks only for a paper outline;
- the user asks for citation search only;
- the user asks for figure generation only;
- the text is not intended for academic manuscript writing.

## Inputs to infer

Try to identify:
- target section;
- target language;
- target venue if provided;
- outline context;
- paragraph purpose;
- field/domain;
- method;
- evidence or results;
- claim boundary.

If missing, make reasonable assumptions and mark them.

## Workflow

1. Identify task type:
   - write from outline;
   - write from rough idea;
   - polish draft;
   - restructure;
   - translate and polish;
   - reduce overclaiming;
   - improve transitions.
2. Identify target section.
3. Identify paper type and corpus-derived style.
4. Diagnose the input.
5. Select section writing template.
6. Generate or revise text.
7. Check claim strength.
8. Add revision notes.
9. Flag missing information.

## References to consult

- references/writing_workflow.md
- references/section_writing_templates.md
- references/abstract_intro_gap_contribution_template.md
- references/problem_formulation_writing_template.md
- references/methodology_writing_template.md
- references/results_discussion_writing_template.md
- references/transition_and_coherence_rules.md
- references/overclaim_and_language_risk_checklist.md

## Output format

If the user requests English manuscript text, write the manuscript text in English. Keep notes in Chinese unless requested otherwise.

# 修改/生成结果

## 1. 正文版本

Provide generated or revised manuscript text.

## 2. 修改说明

Explain:
- structure changes;
- logic changes;
- style changes;
- claim-control changes.

## 3. 与大纲的对应关系

Explain which outline section/subsection this text fits.

## 4. 风格适配说明

Explain how the text follows corpus-derived writing patterns.

## 5. 仍需补充的信息

List missing data, assumptions, metrics, citations, definitions, or experimental details.

## 6. 审稿风险提醒

List risks:
- vague gap;
- unsupported novelty;
- weak formulation;
- missing constraints;
- method not tied to problem;
- insufficient validation;
- overclaiming;
- weak limitation.

## Section-specific rules

### Abstract

Should usually include:
- context;
- problem;
- gap;
- method;
- validation;
- findings;
- implication.

### Introduction

Should usually include:
- background;
- challenge;
- prior work grouping;
- specific gap;
- proposed work;
- contributions;
- organization.

### Problem Formulation

Do not start directly with equations.
Usually write:
1. scenario/problem paragraph;
2. assumptions;
3. notation;
4. variables/objectives/constraints;
5. mapping back to real problem.

### Methodology

Usually write:
- method overview;
- input-output relation;
- modules;
- equations/algorithms;
- implementation details;
- connection to formulation.

### Results and Discussion

Usually write:
- setup;
- baselines;
- metrics;
- main findings;
- ablation/sensitivity;
- interpretation;
- limitation.

## Quality checklist

Before final output, check:
- Does the text serve the section function?
- Does it align with the outline?
- Are claims supported?
- Are assumptions marked?
- Is the writing precise?
- Are missing details flagged instead of invented?
- Is overclaiming avoided?
