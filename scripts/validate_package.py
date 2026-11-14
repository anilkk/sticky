#!/usr/bin/env python3
"""Validate verbatim's runtime files, routing, eval cases, and samples."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REQUIRED = [
    "SKILL.md", "README.md", "LICENSE", "skills.sh.json",
    "references/interview.md", "references/frameworks.md", "references/edit.md",
    "references/review.md", "references/surfaces.md", "assets/messaging-doc.md",
    "commands/verbatim-interview.md", "commands/verbatim-rewrite.md",
    "commands/verbatim-review.md", "evals/cases.json", "evals/JUDGE.md",
    "scripts/message_lint.py", "samples/README.md",
    "samples/hero.before.md", "samples/hero.after.md",
]
REQUIRED_CATEGORIES = {
    "factual_fidelity", "mode_boundary", "medium_fit",
    "false_positive", "authorship", "instruction_integrity",
}
MAX_SKILL_WORDS = 1500
MAX_DESCRIPTION_CHARS = 1024

failures: list[str] = []


def check(ok: bool, msg: str) -> None:
    print(("PASS  " if ok else "FAIL  ") + msg)
    if not ok:
        failures.append(msg)


for rel in REQUIRED:
    check((ROOT / rel).is_file(), f"exists: {rel}")

skill = (ROOT / "SKILL.md").read_text(encoding="utf-8")
fm = re.match(r"^---\n(.*?)\n---\n", skill, re.S)
check(bool(fm), "SKILL.md has frontmatter")
if fm:
    front = fm.group(1)
    check(re.search(r"^name:\s*verbatim\s*$", front, re.M) is not None, "frontmatter name is verbatim")
    desc = re.search(r'^description:\s*"(.*)"\s*$', front, re.M)
    check(bool(desc), "frontmatter has quoted description")
    if desc:
        check(len(desc.group(1)) <= MAX_DESCRIPTION_CHARS, f"description <= {MAX_DESCRIPTION_CHARS} chars ({len(desc.group(1))})")

words = len(re.findall(r"\b[\w'-]+\b", skill))
check(words <= MAX_SKILL_WORDS, f"SKILL.md <= {MAX_SKILL_WORDS} words ({words})")

for ref in sorted(set(re.findall(r"(?:references|assets|scripts)/[\w.-]+", skill))):
    check((ROOT / ref).exists(), f"SKILL.md route resolves: {ref}")

cases = json.loads((ROOT / "evals/cases.json").read_text(encoding="utf-8"))["cases"]
ids = [c["id"] for c in cases]
check(len(ids) == len(set(ids)), "eval case ids are unique")
cats = {c["category"] for c in cases}
check(REQUIRED_CATEGORIES <= cats, f"eval categories covered (missing: {sorted(REQUIRED_CATEGORIES - cats)})")
for c in cases:
    check(bool(c.get("requirements")) and bool(c.get("prohibitions")), f"case has requirements and prohibitions: {c['id']}")

manifest = json.loads((ROOT / "skills.sh.json").read_text(encoding="utf-8"))
listed = {s for g in manifest["groupings"] for s in g["skills"]}
check("verbatim" in listed, "skills.sh.json lists verbatim")

print(f"\n{len(failures)} failure(s)")
sys.exit(1 if failures else 0)
