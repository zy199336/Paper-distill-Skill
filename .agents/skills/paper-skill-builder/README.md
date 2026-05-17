# paper-skill-builder

This skill orchestrates the full workflow for creating two installed Codex/Claude/OpenCode skills from a small local PDF corpus:

- `writing-paper-outline`
- `writing-paper`

The user should provide the folder containing reference PDFs. Codex/Claude/OpenCode then runs the project scripts, fills extraction files using the `paper-corpus-analyzer` workflow, synthesizes rules, syncs references, installs the generated skills, and reminds the user to restart Codex/Claude/OpenCode.
