# paper-skill-builder

This skill orchestrates the full workflow for creating two installed Codex skills from a small local PDF corpus:

- `writing-paper-outline`
- `writing-paper`

The user should provide the folder containing reference PDFs. Codex then runs the project scripts, fills extraction files using the `paper-corpus-analyzer` workflow, synthesizes rules, syncs references, installs the generated skills, and reminds the user to restart Codex.
