from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SYNTHESIS = ROOT / "data" / "synthesis"
OUTLINE_REF = ROOT / ".agents" / "skills" / "writing-paper-outline" / "references"
WRITING_REF = ROOT / ".agents" / "skills" / "writing-paper" / "references"

MAPPINGS = [
    (SYNTHESIS / "outline_patterns.md", OUTLINE_REF / "outline_workflow.md"),
    (SYNTHESIS / "section_function_matrix.md", OUTLINE_REF / "section_templates.md"),
    (SYNTHESIS / "problem_formulation_patterns.md", OUTLINE_REF / "problem_formulation_template.md"),
    (SYNTHESIS / "method_section_patterns.md", OUTLINE_REF / "method_section_template.md"),
    (SYNTHESIS / "experiment_design_patterns.md", OUTLINE_REF / "experiment_planning_template.md"),
    (SYNTHESIS / "figure_table_patterns.md", OUTLINE_REF / "figure_table_planning.md"),
    (SYNTHESIS / "reviewer_risk_checklist.md", OUTLINE_REF / "reviewer_risk_checklist.md"),
    (SYNTHESIS / "writing_patterns.md", WRITING_REF / "writing_workflow.md"),
    (SYNTHESIS / "writing_patterns.md", WRITING_REF / "section_writing_templates.md"),
    (SYNTHESIS / "abstract_intro_gap_contribution_patterns.md", WRITING_REF / "abstract_intro_gap_contribution_template.md"),
    (SYNTHESIS / "problem_formulation_patterns.md", WRITING_REF / "problem_formulation_writing_template.md"),
    (SYNTHESIS / "method_section_patterns.md", WRITING_REF / "methodology_writing_template.md"),
    (SYNTHESIS / "methodology_results_discussion_patterns.md", WRITING_REF / "results_discussion_writing_template.md"),
    (SYNTHESIS / "transition_and_coherence_patterns.md", WRITING_REF / "transition_and_coherence_rules.md"),
    (SYNTHESIS / "reviewer_risk_checklist.md", WRITING_REF / "overclaim_and_language_risk_checklist.md"),
]


def compact_for_reference(text: str) -> str:
    lines = []
    for line in text.splitlines():
        stripped = line.rstrip()
        if len(stripped) > 220:
            stripped = stripped[:217] + "..."
        lines.append(stripped)
    return "\n".join(lines).strip() + "\n"


def main() -> int:
    synced = 0
    missing = 0
    for source, target in MAPPINGS:
        target.parent.mkdir(parents=True, exist_ok=True)
        if not source.exists():
            missing += 1
            continue
        text = source.read_text(encoding="utf-8", errors="ignore")
        banner = "<!-- Synced from data/synthesis. Keep concise and executable. -->\n\n"
        target.write_text(banner + compact_for_reference(text), encoding="utf-8")
        synced += 1
    print("Skill reference sync complete.")
    print(f"- Synced: {synced}")
    print(f"- Missing synthesis files: {missing}")
    return 1 if missing else 0


if __name__ == "__main__":
    raise SystemExit(main())
