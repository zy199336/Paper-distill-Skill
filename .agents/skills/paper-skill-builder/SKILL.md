---
name: paper-skill-builder
description: Build and install two corpus-derived academic writing skills, writing-paper-outline and writing-paper, from a user-specified folder containing academic paper PDFs. Use when the user says their reference papers are in a folder and asks Codex/Claude/OpenCode to create paper skills, build writing-paper-outline/writing-paper skills, or run the paper-skill-builder workflow. Prefer a focused set of highly relevant, high-quality papers rather than a large loose corpus.
---

# Paper Skill Builder

## Default stance

This is an orchestration skill. It should run the project scripts automatically and use Codex/Claude/OpenCode to perform the paper reading and rule extraction steps.

The user must provide the folder where the reference papers are stored. If the folder is missing, ask for it before running the workflow.

PDF quantity is not a hard limit. If the folder contains many PDFs, warn the user that skill quality is usually better with a focused set of the most relevant, highest-quality papers, then continue unless the user asks to stop.

The final installed skills are:
- `writing-paper-outline`
- `writing-paper`

After installation, tell the user to restart Codex/Claude/OpenCode so the new skills can be discovered.

## Use when

Use this skill when the user says something like:
- "My reference papers are stored in input_papers. Build the two key paper skills."
- "Build paper skills from these PDFs."
- "Create outline and writing skills from this paper folder."
- "Run the paper-skill-builder workflow."

## Do not use when

Do not use this skill when:
- the user only wants a normal literature review;
- the user only wants summaries of papers;
- the documents are not academic papers;
- the user wants to directly draft or polish manuscript text after the final skills are already installed.

## Required input

Identify the paper folder from the user message. Examples:
- `input_papers`
- `input_papers/pdfs`
- an absolute local path

If the user gives `input_papers`, scan that folder recursively. If PDFs are directly under the folder, use them. If PDFs are under a nested `pdfs` folder, use those.

## Automatic workflow

Run these steps without asking the user to run scripts manually:

1. Verify the paper folder exists. If the folder contains many PDFs, warn that skill quality is usually better with a focused set of the most relevant, highest-quality papers.
2. Run:

   ```powershell
   python scripts/build_manifest.py --paper-dir "<paper-folder>"
   ```

3. Run:

   ```powershell
   python scripts/create_extract_templates.py
   ```

4. Use the `paper-corpus-analyzer` workflow to read every included PDF and fill:

   ```text
   data/extracts/combined/PAPER_ID.md
   ```

   Process all papers where `include_for_outline=yes` or `include_for_writing=yes`. Respect manual `no` values in the manifest.

5. Run:

   ```powershell
   python scripts/validate_extracts.py
   ```

   If validation fails because model-generated extracts are incomplete, fix the missing sections and rerun validation.

6. Run:

   ```powershell
   python scripts/synthesize_rules.py
   ```

7. Run:

   ```powershell
   python scripts/sync_skills_from_synthesis.py
   ```

8. Run:

   ```powershell
   python scripts/install_generated_skills.py
   ```

9. Run:

   ```powershell
   python scripts/run_basic_checks.py --paper-dir "<paper-folder>"
   ```

10. Report:
    - papers found and processed;
    - any recommendation to reduce or focus the corpus;
    - manifest path;
    - extraction and synthesis status;
    - installed skill names;
    - restart reminder.

## Extraction rules

- Do not produce a normal literature review.
- Do not copy long passages from papers.
- Extract only reusable outline rules, writing rules, section functions, problem-formulation patterns, method-section patterns, experiment-design patterns, figure/table patterns, claim-control patterns, and reviewer risks.
- Infer journal, venue, domain, paper type, method type, and data type when possible.
- If uncertain, write `unknown` or mark uncertainty. Do not fabricate.
- Every synthesized rule should keep source `paper_id` where possible.

## Installation behavior

The installation script copies only:
- `.agents/skills/writing-paper-outline`
- `.agents/skills/writing-paper`

to:

```text
$CODEX_HOME/skills
```

or, if `CODEX_HOME` is unset:

```text
~/.codex/skills
```

If an existing destination skill is not marked as builder-managed, the script skips it instead of overwriting user content.

## Final user-facing reminder

Always end successful builds with:

```text
Installed writing-paper-outline and writing-paper. Please restart Codex/Claude/OpenCode so the two newly installed skills can be discovered.
```

After restart, the user can call:
- `@writing-paper-outline`
- `@writing-paper`
