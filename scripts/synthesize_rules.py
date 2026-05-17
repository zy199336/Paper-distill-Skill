from __future__ import annotations

import re
from pathlib import Path
from typing import Dict, List

ROOT = Path(__file__).resolve().parents[1]
COMBINED_DIR = ROOT / "data" / "extracts" / "combined"
SYNTHESIS_DIR = ROOT / "data" / "synthesis"

SYNTHESIS_FILES = {
    "corpus_profile.md": "# Corpus Profile\n\n- corpus size: TODO\n- inferred domains: TODO\n- inferred venues: TODO\n- paper types: TODO\n- method types: TODO\n- common storyline: TODO\n- major limitations of this corpus: TODO\n- warning: rules are corpus-derived, not universal.\n",
    "paper_type_taxonomy.md": "# Paper Type Taxonomy\n\nTODO: synthesize paper types from completed extracts. Mark each rule with source paper_id.\n",
    "outline_patterns.md": "# Outline Patterns\n\nTODO: synthesize common storyline, section sequences, section variants, and main text vs appendix rules from completed extracts.\n",
    "section_function_matrix.md": "# Section Function Matrix\n\n| Section | Purpose | Must include | Optional include | Figures/Tables/Equations | Common mistakes | Reviewer risks | Source paper_id |\n|---|---|---|---|---|---|---|---|\n",
    "problem_formulation_patterns.md": "# Problem Formulation Patterns\n\nTODO: synthesize scenario, assumptions, sets, parameters, variables, objective, constraints, and mapping-back rules.\n",
    "method_section_patterns.md": "# Method Section Patterns\n\nTODO: synthesize method overview, module sequence, input-output relationships, formulas, algorithms, reproducibility, and method-problem alignment.\n",
    "experiment_design_patterns.md": "# Experiment Design Patterns\n\nTODO: synthesize dataset/scenario, baselines, metrics, parameters, ablation, sensitivity, robustness, runtime, case study, and practical interpretation rules.\n",
    "figure_table_patterns.md": "# Figure And Table Patterns\n\nTODO: synthesize recommended figure sequence, figure roles, table roles, section placement, and common mistakes.\n",
    "writing_patterns.md": "# Writing Patterns\n\nTODO: synthesize general writing stance, section-level logic, paragraph moves, drafting from outline, revising drafts, and claim control.\n",
    "abstract_intro_gap_contribution_patterns.md": "# Abstract Introduction Gap Contribution Patterns\n\nTODO: synthesize abstract structure, introduction paragraph moves, gap writing, contribution writing, and common mistakes.\n",
    "methodology_results_discussion_patterns.md": "# Methodology Results Discussion Patterns\n\nTODO: synthesize methodology writing, result interpretation, discussion, limitation, and future work patterns.\n",
    "transition_and_coherence_patterns.md": "# Transition And Coherence Patterns\n\nTODO: synthesize transitions for background to gap, gap to contribution, scenario to formulation, formulation to method, method to experiment, results to implication, and limitation to future work.\n",
    "reviewer_risk_checklist.md": "# Reviewer Risk Checklist\n\nTODO: synthesize outline, problem formulation, method, experiment, figure/table, writing, and claim risks.\n",
}


def extract_section(text: str, number: int) -> str:
    pattern = rf"^## {number}\. .*$([\s\S]*?)(?=^## \d+\. |\Z)"
    match = re.search(pattern, text, re.M)
    return match.group(0).strip() if match else ""


def paper_id_from_text(path: Path, text: str) -> str:
    match = re.search(r"paper_id:\s*(PAPER_\d{3})", text)
    return match.group(1) if match else path.stem


def collect_completed_extracts() -> Dict[str, str]:
    extracts = {}
    if not COMBINED_DIR.exists():
        return extracts
    for path in sorted(COMBINED_DIR.glob("*.md")):
        text = path.read_text(encoding="utf-8", errors="ignore")
        has_outline_rules = "## 17. Transferable rules for writing-paper-outline" in text
        has_writing_rules = "## 18. Transferable rules for writing-paper" in text
        still_empty = "TODO" in text.upper() and len(text) < 4000
        if has_outline_rules and has_writing_rules and not still_empty:
            extracts[paper_id_from_text(path, text)] = text
    return extracts


def main() -> int:
    SYNTHESIS_DIR.mkdir(parents=True, exist_ok=True)
    extracts = collect_completed_extracts()

    if not extracts:
        for name, content in SYNTHESIS_FILES.items():
            path = SYNTHESIS_DIR / name
            if not path.exists():
                path.write_text(content, encoding="utf-8")
        print("No completed combined extracts found. Initialized synthesis placeholders only.")
        return 0

    for name, fallback in SYNTHESIS_FILES.items():
        path = SYNTHESIS_DIR / name
        if path.exists() and "TODO" not in path.read_text(encoding="utf-8", errors="ignore"):
            continue
        parts: List[str] = [fallback.rstrip(), "\n\n## Source-Grounded Notes\n"]
        for paper_id, text in extracts.items():
            if "outline" in name or "section_function" in name:
                sections = [extract_section(text, n) for n in (4, 5, 6, 7, 8, 16, 17)]
            elif "writing" in name or "abstract" in name or "transition" in name or "methodology_results" in name:
                sections = [extract_section(text, n) for n in (9, 10, 11, 12, 13, 14, 15, 18)]
            else:
                sections = [extract_section(text, n) for n in range(1, 19)]
            parts.append(f"\n### {paper_id}\n")
            for section in sections:
                if section:
                    parts.append(section[:2500].strip())
                    parts.append("\n")
        parts.append("\n## Synthesis TODO\n\nConvert the notes above into concise transferable rules. Preserve source paper_id for each rule and do not add unsupported claims.\n")
        path.write_text("\n".join(parts), encoding="utf-8")

    print("Synthesis files updated from completed extracts.")
    print(f"- Completed extracts used: {len(extracts)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
