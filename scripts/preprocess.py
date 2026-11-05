"""Clean the raw story text.

Usage: python scripts/preprocess.py corpus/sultanas_dream_raw.txt corpus/sultanas_dream.txt

What it does: strips Project Gutenberg / site headers if present, joins lines
that were hard-wrapped, collapses extra spaces and keeps one blank line between
paragraphs. Read the output once yourself; no script catches every scan error.
"""
import re
import sys
from pathlib import Path


def clean(text):
    text = text.replace("\r\n", "\n").replace("\r", "\n").replace("\ufeff", "")
    s = re.search(r"\*\*\* ?START OF (THE|THIS) PROJECT GUTENBERG.*?\*\*\*", text, re.S)
    if s:
        text = text[s.end():]
    e = re.search(r"\*\*\* ?END OF (THE|THIS) PROJECT GUTENBERG", text)
    if e:
        text = text[: e.start()]
    paras = re.split(r"\n\s*\n", text)
    paras = [re.sub(r"\s+", " ", p).strip() for p in paras]
    return "\n\n".join(p for p in paras if p) + "\n"


if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    out = clean(Path(sys.argv[1]).read_text(encoding="utf-8", errors="ignore"))
    Path(sys.argv[2]).write_text(out, encoding="utf-8")
    print(f"written {sys.argv[2]}: {len(out.split())} words, {out.count(chr(10)+chr(10))+1} paragraphs")
