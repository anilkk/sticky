#!/usr/bin/env python3
"""Locate common messaging habits. Prints a map of where to look; never a score.

Usage: python3 scripts/message_lint.py draft.md   (or - for stdin)
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

JARGON = [
    "leverage", "seamless", "seamlessly", "robust", "unlock", "unlocks", "empower",
    "empowers", "revolutionize", "revolutionizes", "revolutionary", "cutting-edge",
    "next-generation", "next-gen", "best-in-class", "world-class", "end-to-end", "holistic",
    "synergy", "game-changing", "game-changer", "supercharge", "streamline", "streamlines",
    "frictionless", "turnkey", "innovative", "solution", "solutions", "all-in-one",
    "mission-critical", "enterprise-grade", "paradigm", "disrupt", "disruptive",
    "state-of-the-art", "transform", "transforms", "elevate", "harness",
]
SUPERLATIVES = [
    "leading", "fastest", "best", "most reliable", "most powerful", "most advanced",
    "#1", "number one", "unmatched", "unparalleled", "trusted by", "industry-leading",
    "10x", "100x", "the only",
]
VAGUE_SOCIAL_PROOF = [
    "leading companies", "top companies", "teams everywhere", "thousands of companies",
    "fortune 500 companies", "innovative teams", "modern teams",
]
PROOF_SIGNAL = re.compile(r"\d|%|\[TK|\bbenchmark|\bcase study|\"|“", re.I)


def strip_markdown(text: str) -> str:
    text = re.sub(r"```.*?```", " ", text, flags=re.S)
    text = re.sub(r"`[^`]*`", " ", text)
    text = re.sub(r"^---\n.*?\n---\n", " ", text, flags=re.S)
    text = re.sub(r"!?\[([^\]]*)\]\([^)]*\)", r"\1", text)
    text = re.sub(r"^[#>\-\*\s]+", "", text, flags=re.M)
    return text


def blocks(src: str) -> list[str]:
    """Headings and list items stand alone; wrapped paragraph lines are joined."""
    out: list[str] = []
    para: list[str] = []
    for line in src.splitlines():
        stripped = line.strip()
        standalone = re.match(r"^(#{1,6}\s|[-*+]\s|\d+\.\s|\[)", stripped)
        if not stripped or standalone:
            if para:
                out.append(" ".join(para))
                para = []
            if standalone:
                out.append(stripped)
        else:
            para.append(stripped)
    if para:
        out.append(" ".join(para))
    return out


def sentences(src: str) -> list[str]:
    result: list[str] = []
    for block in blocks(src):
        clean = strip_markdown(block)
        result += [p.strip() for p in re.split(r"(?<=[.!?])\s+", clean) if p.strip()]
    return result


def find_terms(sentence: str, terms: list[str]) -> list[str]:
    low = sentence.lower()
    return [t for t in terms if re.search(r"(?<![\w-])" + re.escape(t) + r"(?![\w-])", low)]


def main() -> int:
    if len(sys.argv) != 2:
        print(__doc__.strip())
        return 2
    src = sys.stdin.read() if sys.argv[1] == "-" else Path(sys.argv[1]).read_text(encoding="utf-8")
    src = re.sub(r"```.*?```", " ", src, flags=re.S)
    src = re.sub(r"^---\n.*?\n---\n", " ", src, flags=re.S)
    text = strip_markdown(src)
    sents = sentences(src)

    print("verbatim lint: a map of where to look, not a grade\n")

    hits = 0
    for i, s in enumerate(sents, 1):
        notes = []
        j = find_terms(s, JARGON)
        if j:
            notes.append("jargon? " + ", ".join(j))
        sup = find_terms(s, SUPERLATIVES)
        if sup and not PROOF_SIGNAL.search(s):
            notes.append("claim without nearby proof: " + ", ".join(sup))
        vague = find_terms(s, VAGUE_SOCIAL_PROOF)
        if vague:
            notes.append("vague social proof: " + ", ".join(vague))
        if len(s.split()) > 30:
            notes.append(f"long sentence ({len(s.split())} words)")
        if notes:
            hits += 1
            short = s if len(s) <= 90 else s[:87] + "..."
            print(f"[{i}] {short}")
            for n in notes:
                print(f"     - {n}")

    words = re.findall(r"[A-Za-z']+", text.lower())
    we = sum(w in {"we", "our", "us", "we're", "we've"} for w in words)
    you = sum(w in {"you", "your", "you're", "you'll", "yours"} for w in words)
    tk = len(re.findall(r"\[TK", src))

    print("\nsummary")
    print(f"  sentences: {len(sents)}   sentences with notes: {hits}")
    print(f"  we/our/us: {we}   you/your: {you}" + ("   (company is the subject more than the reader)" if we > you else ""))
    print(f"  open [TK] markers: {tk}")
    print("\nEvery hit is a prompt to read the line in context. Precise buyer terms are not jargon.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
