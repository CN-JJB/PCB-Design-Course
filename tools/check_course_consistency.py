#!/usr/bin/env python3
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
formal_prefixes = tuple(f"{n:02d}_" for n in range(10, 20))

violations = []
for md in ROOT.rglob("*.md"):
    rel = md.relative_to(ROOT).as_posix()
    if not rel.startswith(formal_prefixes):
        continue
    text = md.read_text(encoding="utf-8")
    for bad in (
        "KiCad 9",
        "KiCad9",
        "05_KiCad9多层必备复习.md",
        "14_Part4_EMI_EMC/09_参考资料与数据纪律.md",
    ):
        if bad in text:
            violations.append((rel, bad))

if violations:
    print("Formal-course consistency violations:")
    for rel, bad in violations:
        print(f"- {rel}: contains {bad!r}")
    sys.exit(1)

print("Formal-course consistency: OK")
