from __future__ import annotations

import os
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE_ROOT = ROOT / ".agents" / "skills"
GENERATED_SKILLS = ["writing-paper-outline", "writing-paper"]
MARKER = ".paper_skill_builder_managed"


def codex_home() -> Path:
    env_home = os.environ.get("CODEX_HOME")
    if env_home:
        return Path(env_home).expanduser()
    return Path.home() / ".codex"


def install_skill(name: str, target_root: Path) -> tuple[bool, str]:
    source = SOURCE_ROOT / name
    target = target_root / name
    if not source.exists():
        return False, f"missing source skill: {source}"

    if target.exists() and not (target / MARKER).exists():
        return False, f"destination exists and is not marked as builder-managed: {target}"

    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copytree(source, target, dirs_exist_ok=True)
    (target / MARKER).write_text("Installed by paper-skill-builder.\n", encoding="utf-8")
    return True, f"installed {name} -> {target}"


def main() -> int:
    target_root = codex_home() / "skills"
    failures = 0
    print(f"Installing generated skills to: {target_root}")
    for name in GENERATED_SKILLS:
        ok, message = install_skill(name, target_root)
        print(f"[{'OK' if ok else 'SKIP'}] {message}")
        if not ok:
            failures += 1

    print("Install step complete.")
    if failures:
        print("Some skills were not installed. Resolve existing unmarked destination folders or install manually.")
        return 1
    print("Restart Codex after installation so the new skills are discovered.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
