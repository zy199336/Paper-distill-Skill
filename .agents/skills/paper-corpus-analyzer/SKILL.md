---
name: paper-corpus-analyzer
description: Analyze a folder of academic paper PDFs and extract reusable outline and writing patterns for building writing-paper-outline and writing-paper skills. Use when processing a focused paper corpus into structured extraction files, synthesis rules, section functions, problem-formulation patterns, writing patterns, figure/table patterns, experiment-design rules, and reviewer-risk checklists. This skill does not produce a generic literature review.
---

# Paper Corpus Analyzer

## Default stance

This skill does not produce a normal literature review or paper summary.

It extracts reusable rules for building two downstream skills:
- `writing-paper-outline`
- `writing-paper`

The analysis should focus on how high-quality papers are structured and written, not only what they study.

When called by `paper-skill-builder`, run as part of the automatic build workflow. Do not ask the user to manually run the project scripts unless a script fails and requires user intervention.

## Use when

Use this skill when:
- the user provides a folder of academic papers;
- the corpus is focused on papers most relevant to the target manuscript;
- the user wants to build reusable writing and outlining skills;
- the user wants automatic extraction without manually defining journal, writing_value, or outline_value.

## Do not use when

Do not use this skill when:
- the user only wants summaries of individual papers;
- the user asks for citation search only;
- the documents are not academic papers.

## Workflow

1. Read the manifest.
2. Process all papers with `include_for_outline=yes` or `include_for_writing=yes`, unless the user manually set both to `no`.
3. Infer journal, domain, paper_type, and method_type when possible.
4. For each paper, produce a combined extraction file.
5. Extract outline patterns:
   - paper storyline
   - section sequence
   - section function
   - problem formulation
   - methodology
   - experiment design
   - figure/table role
   - discussion and limitation
   - reviewer risks
6. Extract writing patterns:
   - abstract
   - introduction
   - gap
   - contribution
   - problem formulation writing
   - method writing
   - results writing
   - discussion writing
   - transitions
   - claim control
7. Convert observations into transferable rules.
8. Mark each rule with source paper_id.
9. Do not copy long passages from papers.
10. Do not invent unsupported rules.

## Output

For each paper, create:
- `data/extracts/combined/PAPER_ID.md`
- optionally `data/extracts/outline/PAPER_ID.md`
- optionally `data/extracts/writing/PAPER_ID.md`

Use the templates in references.

## Quality rules

- Prefer structural and rhetorical rules over content summaries.
- Keep rules source-grounded.
- Distinguish corpus-specific patterns from universal advice.
- Mark uncertainty.
- Do not infer a journal style if the journal cannot be identified.
- Do not copy long original text.
- Do not fabricate DOI, venue, experiments, figures, or conclusions.
