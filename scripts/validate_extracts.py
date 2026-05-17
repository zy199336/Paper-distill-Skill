from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
COMBINED_DIR = ROOT / "data" / "extracts" / "combined"

REQUIRED_HEADINGS = [
    "## 0. Paper identity",
    "## 1. Corpus value",
    "## 2. One-sentence positioning",
    "## 3. Overall paper storyline",
    "## 4. Section-by-section outline extraction",
    "## 5. Problem formulation pattern",
    "## 6. Method section pattern",
    "## 7. Experiment design pattern",
    "## 8. Figure and table pattern",
    "## 9. Abstract writing pattern",
    "## 10. Introduction writing pattern",
    "## 11. Gap and contribution writing pattern",
    "## 12. Problem formulation writing pattern",
    "## 13. Methodology writing pattern",
    "## 14. Results and discussion writing pattern",
    "## 15. Transition and coherence rules",
    "## 16. Reviewer-risk signals",
    "## 17. Transferable rules for writing-paper-outline",
    "## 18. Transferable rules for writing-paper",
]


def main() -> int:
    if not COMBINED_DIR.exists():
        print(f"ERROR: combined extract directory not found: {COMBINED_DIR}")
        return 2

    files = sorted(COMBINED_DIR.glob("*.md"))
    if not files:
        print("No combined extract files found.")
        return 1

    failures = 0
    for path in files:
        text = path.read_text(encoding="utf-8", errors="ignore")
        missing = [heading for heading in REQUIRED_HEADINGS if heading not in text]
        if missing:
            failures += 1
            print(f"[MISSING] {path.name}")
            for heading in missing:
                print(f"  - {heading}")
        else:
            print(f"[OK] {path.name}")

    print("Validation complete.")
    print(f"- Files checked: {len(files)}")
    print(f"- Files with missing sections: {failures}")
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
