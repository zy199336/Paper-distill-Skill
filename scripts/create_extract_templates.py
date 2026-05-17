from __future__ import annotations

import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "data" / "paper_manifest.csv"
COMBINED_DIR = ROOT / "data" / "extracts" / "combined"
TEMPLATE = ROOT / ".agents" / "skills" / "paper-corpus-analyzer" / "references" / "combined_extraction_template.md"


def is_yes(value: str) -> bool:
    return (value or "").strip().lower() in {"yes", "y", "true", "1"}


def should_skip_existing(path: Path) -> bool:
    if not path.exists():
        return False
    text = path.read_text(encoding="utf-8", errors="ignore")
    status_markers = ["extraction_status: completed", "Extraction status: completed", "completed"]
    return any(marker in text for marker in status_markers)


def main() -> int:
    if not MANIFEST.exists():
        print(f"ERROR: manifest not found: {MANIFEST}")
        print("Run: python scripts/build_manifest.py")
        return 2
    if not TEMPLATE.exists():
        print(f"ERROR: template not found: {TEMPLATE}")
        return 2

    template = TEMPLATE.read_text(encoding="utf-8")
    COMBINED_DIR.mkdir(parents=True, exist_ok=True)
    created = 0
    skipped = 0

    with MANIFEST.open("r", encoding="utf-8-sig", newline="") as f:
        for row in csv.DictReader(f):
            include = is_yes(row.get("include_for_outline", "")) or is_yes(row.get("include_for_writing", ""))
            if not include:
                skipped += 1
                continue
            paper_id = (row.get("paper_id") or "").strip()
            if not paper_id:
                skipped += 1
                continue
            out = COMBINED_DIR / f"{paper_id}.md"
            if should_skip_existing(out):
                skipped += 1
                continue
            if out.exists():
                skipped += 1
                continue

            prefill = template
            replacements = {
                "- paper_id:": f"- paper_id: {paper_id}",
                "- title:": f"- title: {row.get('title', '')}",
                "- authors:": f"- authors: {row.get('authors', '')}",
                "- year:": f"- year: {row.get('year', '')}",
                "- journal_or_venue:": f"- journal_or_venue: {row.get('journal_or_venue', '')}",
                "- domain:": f"- domain: {row.get('domain', '')}",
                "- subdomain:": f"- subdomain: {row.get('subdomain', '')}",
                "- paper_type:": f"- paper_type: {row.get('paper_type', '')}",
                "- method_type:": f"- method_type: {row.get('method_type', '')}",
                "- data_type:": f"- data_type: {row.get('data_type', '')}",
                "- scenario_type:": f"- scenario_type: {row.get('scenario_type', '')}",
            }
            for old, new in replacements.items():
                prefill = prefill.replace(old, new, 1)
            out.write_text(prefill, encoding="utf-8")
            created += 1

    print("Extraction template creation complete.")
    print(f"- Created: {created}")
    print(f"- Skipped: {skipped}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
