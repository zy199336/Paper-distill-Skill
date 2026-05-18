from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SYNTHESIS = ROOT / "data" / "synthesis"
COMBINED_EXTRACTS = ROOT / "data" / "extracts" / "combined"
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

SOURCE_ID_RE = re.compile(r"\b[A-Z][A-Z0-9]*_\d{3}\b")


def sort_paper_ids(ids: set[str]) -> list[str]:
    def key(value: str) -> tuple[str, int, str]:
        match = re.match(r"^([A-Za-z_]+)_(\d+)$", value)
        if match:
            return (match.group(1), int(match.group(2)), value)
        return (value, 0, value)

    return sorted(ids, key=key)


def collect_source_ids() -> list[str]:
    ids: set[str] = set()
    for root in (COMBINED_EXTRACTS, SYNTHESIS):
        if not root.exists():
            continue
        for path in root.rglob("*.md"):
            text = path.read_text(encoding="utf-8", errors="ignore")
            ids.update(SOURCE_ID_RE.findall(text))
    return sort_paper_ids(ids)


def ids_in_text(text: str, fallback: list[str]) -> list[str]:
    ids = set(SOURCE_ID_RE.findall(text))
    return sort_paper_ids(ids) if ids else fallback


def format_ids(ids: list[str]) -> str:
    return ", ".join(ids) if ids else "TODO"


def compact_for_reference(text: str) -> str:
    lines = []
    for line in text.splitlines():
        stripped = line.rstrip()
        if "Source paper_id" not in stripped and len(stripped) > 320:
            stripped = stripped[:317] + "..."
        lines.append(stripped)
    return "\n".join(lines).strip() + "\n"


def should_annotate_line(line: str) -> bool:
    stripped = line.strip()
    if not stripped:
        return False
    if "Source paper_id" in stripped or "source paper_id" in stripped:
        return False
    if SOURCE_ID_RE.search(stripped):
        return False
    if "TODO" in stripped:
        return False
    if stripped.startswith(("#", "|", "<!--")):
        return False
    if stripped.startswith("- "):
        return len(stripped) > 28
    if re.match(r"^\d+\.\s+\S", stripped):
        return len(stripped) > 28
    if len(stripped) > 45 and stripped.endswith("."):
        return True
    return False


def annotate_reference_lines(text: str, source_ids: list[str]) -> str:
    source_text = format_ids(source_ids)
    annotated = []
    for line in text.splitlines():
        clean = line.rstrip()
        if should_annotate_line(clean):
            suffix = "" if clean.endswith((".", ";", ":")) else "."
            annotated.append(f"{clean}{suffix} Source paper_id: {source_text}.")
        else:
            annotated.append(clean)
    return "\n".join(annotated).strip() + "\n"


def reference_banner(all_source_ids: list[str], source_ids: list[str]) -> str:
    return (
        "<!-- Synced from data/synthesis. Keep concise, executable, and source-grounded. -->\n\n"
        "## Corpus Source Coverage\n\n"
        f"- Completed source papers: {format_ids(all_source_ids)}.\n"
        f"- Source papers directly referenced in this file: {format_ids(source_ids)}.\n"
        "- Rules without narrower evidence should be treated as corpus-level patterns, not universal claims.\n\n"
    )


def main() -> int:
    synced = 0
    missing = 0
    all_source_ids = collect_source_ids()
    for source, target in MAPPINGS:
        target.parent.mkdir(parents=True, exist_ok=True)
        if not source.exists():
            missing += 1
            continue
        text = source.read_text(encoding="utf-8", errors="ignore")
        source_ids = ids_in_text(text, all_source_ids)
        body = annotate_reference_lines(compact_for_reference(text), source_ids)
        target.write_text(reference_banner(all_source_ids, source_ids) + body, encoding="utf-8")
        synced += 1
    print("Skill reference sync complete.")
    print(f"- Synced: {synced}")
    print(f"- Missing synthesis files: {missing}")
    print(f"- Completed source papers: {format_ids(all_source_ids)}")
    return 1 if missing else 0


if __name__ == "__main__":
    raise SystemExit(main())
