# Paper distill Skill Builder

This project builds two reusable Codex/Claude/OpenCode writing skills from a focused set of high-quality academic paper PDFs:

- `writing-paper-outline`: generates manuscript outlines, section structures, figure/table plans, experiment plans, and reviewer-risk checks from a research topic, paper idea, method, data, or preliminary concept.
- `writing-paper`: generates, rewrites, polishes, or restructures manuscript prose from an outline, draft, bullet points, or a short description of what a section should cover.

This project is not a normal literature-review tool. Its purpose is to extract transferable structural rules, writing rules, section functions, problem-formulation patterns, method-organization patterns, experiment-design patterns, figure/table functions, claim-control rules, and reviewer-risk signals from selected papers.

## Automatic Build Workflow

### 1. Install `paper-skill-builder`

Tell Codex/Claude/OpenCode:

```text
Please install the paper-skill-builder skill from the current project folder.
```

After installation, restart Codex/Claude/OpenCode once so `paper-skill-builder` can be discovered.

### 2. Place Reference Papers

Put high-quality academic PDF papers in:

```text
input_papers/
```

PDF quantity should be selective, not large. Choose the papers that are most relevant to the manuscript you want to write and highest in quality. A focused set of around 30 or fewer papers is recommended, but this is a quality suggestion rather than a hard limit.

You can also use an absolute folder path. If you provide `input_papers`, the scripts will recursively scan it for PDFs when needed.

### 3. Ask Codex/Claude/OpenCode To Create The Two Key Skills

After restarting Codex/Claude/OpenCode and confirming that `paper-skill-builder` is available, use a prompt like:

```text
Please use @paper-skill-builder.
My reference papers are stored in the input_papers folder. Please use paper-skill-builder to create the two key skills.
```

Expected behavior:

- If no paper folder is provided, Codex/Claude/OpenCode asks for the paper folder first.
- Codex/Claude/OpenCode runs `python scripts/build_manifest.py --paper-dir "<paper-folder>"`.
- Codex/Claude/OpenCode runs `python scripts/create_extract_templates.py`.
- Codex/Claude/OpenCode uses the `paper-corpus-analyzer` workflow to fill `data/extracts/combined/PAPER_ID.md` for all included papers.
- Codex/Claude/OpenCode runs `python scripts/validate_extracts.py`; if extraction files are incomplete, it should fix them and rerun validation.
- Codex/Claude/OpenCode runs `python scripts/synthesize_rules.py`.
- Codex/Claude/OpenCode runs `python scripts/sync_skills_from_synthesis.py`.
- Codex/Claude/OpenCode runs `python scripts/install_generated_skills.py`.
- Codex/Claude/OpenCode runs `python scripts/run_basic_checks.py --paper-dir "<paper-folder>"`.
- Codex/Claude/OpenCode reports the manifest, extracts, synthesis files, installed skill names, and restart reminder.

After successful installation, Codex/Claude/OpenCode should report:

```text
Installed writing-paper-outline and writing-paper. Please restart Codex/Claude/OpenCode so the two newly installed skills can be discovered.
```

### 4. Restart Codex/Claude/OpenCode

After the two generated skills are installed, restart Codex/Claude/OpenCode. After restart, you can call:

```text
@writing-paper-outline
@writing-paper
```

## Example Calls After Restart

### 1. Use `@writing-paper-outline` To Structure A Manuscript

```text
Please use @writing-paper-outline to design a manuscript outline for my paper.

Topic: Dynamic risk management and trajectory planning for manned-unmanned collaborative operations in general aviation airspace.

Methods include risk-field modeling, TLS constraints, tactical conflict resolution, and simulation validation.

Please focus on Problem Formulation, Methodology, Experiment Design, and figure/table planning.
```

Expected output:

- paper positioning;
- narrative storyline;
- section / subsection structure;
- Problem Formulation design;
- Methodology design;
- Experiment Design;
- figure/table planning;
- main text vs appendix recommendations;
- reviewer-risk checks.

### 2. Use `@writing-paper` To Draft A Section

```text
Please use @writing-paper skill.

The following is one subsection from the manuscript outline:

Section 3.1 Operational scenario and problem description

This subsection should cover:
- the manned-unmanned collaborative operation scenario in controlled airspace around a general aviation airport;
- manned aircraft, including training aircraft, general aviation aircraft, and helicopters;
- unmanned aircraft, including medium-to-large UAV test flights, inspection missions, and logistics missions;
- heterogeneity in speed, maneuverability, communication links, surveillance capability, and operational intent;
- why existing methods based on fixed separation or single conflict-detection logic are insufficient for dynamic risk management;
- how this scenario should be abstracted as a spatiotemporally coupled trajectory-planning problem under risk constraints.

Please write this as English manuscript prose. Requirements:
1. Do not start directly with equations.
2. First describe the scenario and problem in clear but academic language.
3. Let the final paragraph naturally transition to the mathematical formulation.
4. Output revision notes and reviewer-risk reminders.
```

Expected output:

- English manuscript prose;
- revision notes;
- alignment with the outline;
- style adaptation notes;
- missing information;
- reviewer-risk reminders.

### 3. Use `@writing-paper` To Polish Or Rewrite A Draft

```text
Please use @writing-paper skill.

Target subsection: Methodology overview

Please rewrite the following draft into English manuscript prose and strengthen reproducibility, module clarity, and input-output logic.

Draft:
This paper proposes a trajectory-planning method for dynamic risk management in low-altitude airspace. First, a risk field is constructed based on UAVs, manned aircraft, and ground risk sources, and the risk field is then used to guide trajectory search. To avoid trajectories entering high-risk regions, TLS constraints are introduced. Meanwhile, to improve real-time performance, grid-based search and local replanning are adopted. When conflict risk occurs, the system selects resolution actions such as detouring, waiting, or altitude adjustment according to the risk level.

Please output:
1. English manuscript prose;
2. structural revision notes;
3. technical details that still need to be added;
4. reviewer-risk reminders.
```

Expected output:

- English manuscript prose;
- structural revision notes;
- technical details that still need to be added;
- reviewer-risk reminders;
- reproducibility reminders for inputs, outputs, module sequence, TLS constraints, risk field, local replanning, and conflict-resolution logic.

## Additional Note

You can adjust the weights and inclusion fields in `data/paper_manifest.xlsx` to control how strongly different papers influence the distillation process.
