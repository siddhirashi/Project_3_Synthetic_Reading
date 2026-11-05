"""Step 1 of synthetic reading: split the text into equal parts and sample 20% of each.

Usage:
  python scripts/partial_reading.py corpus/sultanas_dream.txt
  python scripts/partial_reading.py corpus/sultanas_dream.txt --parts 4 --mode random --seed 7

--mode  first | middle | last | random  (which 20% of each part you read)
--unit  paragraph | sentence            (what counts as a "line"; use sentence
                                         if the story has very few paragraphs)
The chosen lines are written to partial_reading.txt with the part number and
position of each line, so you can say exactly what you did and did not read.
"""
import argparse
import math
import random
import re
from pathlib import Path


def split_units(text, unit):
    if unit == "sentence":
        flat = re.sub(r"\s+", " ", text).strip()
        return [s for s in re.split(r"(?<=[.!?])\s+", flat) if s]
    return [p.strip() for p in re.split(r"\n\s*\n", text) if p.strip()]


def equal_parts(items, n):
    size = len(items) / n
    return [items[round(i * size): round((i + 1) * size)] for i in range(n)]


def pick(part, share, mode, rng):
    k = max(1, math.ceil(len(part) * share))
    idx = list(range(len(part)))
    if mode == "first":
        chosen = idx[:k]
    elif mode == "last":
        chosen = idx[-k:]
    elif mode == "middle":
        start = max(0, (len(idx) - k) // 2)
        chosen = idx[start:start + k]
    else:
        chosen = sorted(rng.sample(idx, k))
    return chosen


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("file")
    ap.add_argument("--parts", type=int, default=4)
    ap.add_argument("--share", type=float, default=0.20)
    ap.add_argument("--mode", default="random", choices=["first", "middle", "last", "random"])
    ap.add_argument("--unit", default="paragraph", choices=["paragraph", "sentence"])
    ap.add_argument("--seed", type=int, default=2026)
    ap.add_argument("--out", default="partial_reading.txt")
    a = ap.parse_args()

    text = Path(a.file).read_text(encoding="utf-8")
    units = split_units(text, a.unit)
    parts = equal_parts(units, a.parts)
    rng = random.Random(a.seed)

    lines = [f"Source: {a.file}",
             f"Total {a.unit}s: {len(units)} | parts: {a.parts} | share per part: {a.share:.0%} | mode: {a.mode} | seed: {a.seed}",
             ""]
    read = 0
    for p_no, part in enumerate(parts, 1):
        chosen = pick(part, a.share, a.mode, rng)
        lines.append(f"--- PART {p_no} of {a.parts} ({len(part)} {a.unit}s, reading {len(chosen)}) ---")
        for i in chosen:
            lines.append(f"[{p_no}.{i + 1}] {part[i]}")
            read += 1
        lines.append("")
    Path(a.out).write_text("\n".join(lines), encoding="utf-8")
    print(f"{read} of {len(units)} {a.unit}s selected ({read / len(units):.0%}) -> {a.out}")


if __name__ == "__main__":
    main()
