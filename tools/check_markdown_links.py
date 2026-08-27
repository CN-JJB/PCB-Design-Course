#!/usr/bin/env python3
from pathlib import Path
from urllib.parse import unquote
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
LINK_RE = re.compile(r"!?[[^]]*](([^)]+))")

broken = []
for md in ROOT.rglob("*.md"):
    text = md.read_text(encoding="utf-8")
    for raw in LINK_RE.findall(text):
        target = raw.strip().split("#", 1)[0]
        if not target or target.startswith(("http://", "https://", "mailto:")):
            continue
        target = unquote(target)
        resolved = (md.parent / target).resolve()
        try:
            resolved.relative_to(ROOT)
        except ValueError:
            broken.append((md, raw, "escapes repository"))
            continue
        if not resolved.exists():
            broken.append((md, raw, str(resolved.relative_to(ROOT))))

if broken:
    print("Broken relative Markdown links:")
    for src, raw, resolved in broken:
        print(f"- {src.relative_to(ROOT)} -> {raw} ({resolved})")
    sys.exit(1)

print("Relative Markdown links: OK")
