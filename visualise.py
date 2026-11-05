"""Step 6: charts from Theme_JSON.py

Usage: python visualise.py      (needs matplotlib: pip install matplotlib)

Chart 1 - heatmap: how strongly each theme is present in each part of the story.
Chart 2 - bars: total strength of each theme over the whole story.
Only quotes that were verified against the text are counted.
"""
import textwrap
from collections import defaultdict
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

import Theme_JSON as T

Path("figures").mkdir(exist_ok=True)
rows = [r for r in T.theme_data if r["quote_verified"]]
themes = T.theme_vocabulary
if not rows:
    raise SystemExit("No verified quotations in Theme_JSON.py, nothing to plot. "
                     "Check the quote_verified values or rerun run_extraction.py.")
segments = sorted({r["segment"] for r in T.theme_data})

grid = defaultdict(int)
for r in rows:
    grid[(r["theme"], r["segment"])] += int(r.get("strength", 1))
matrix = [[grid[(t, s)] for s in segments] for t in themes]
totals = [sum(row) for row in matrix]
labels = ["\n".join(textwrap.wrap(t, 28)) for t in themes]
title = "\n".join(textwrap.wrap(T.research_question, 90))

fig, ax = plt.subplots(figsize=(9, 5.5))
im = ax.imshow(matrix, cmap="Purples", aspect="auto")
ax.set_xticks(range(len(segments)), [f"Part {s}" for s in segments])
ax.set_yticks(range(len(themes)), labels, fontsize=8)
for i, row in enumerate(matrix):
    for j, v in enumerate(row):
        if v:
            ax.text(j, i, v, ha="center", va="center", fontsize=9,
                    color="white" if v > max(map(max, matrix)) / 2 else "black")
ax.set_title(title, fontsize=9)
fig.colorbar(im, ax=ax, label="summed strength of evidence")
fig.tight_layout()
fig.savefig("figures/theme_heatmap.png", dpi=200)

order = sorted(range(len(themes)), key=lambda i: totals[i])
fig, ax = plt.subplots(figsize=(9, 5))
ax.barh([labels[i] for i in order], [totals[i] for i in order], color="#5b4b8a")
ax.set_xlabel("summed strength of evidence")
ax.set_title("Which themes carry the story?", fontsize=10)
ax.tick_params(axis="y", labelsize=8)
fig.tight_layout()
fig.savefig("figures/theme_totals.png", dpi=200)
print("saved figures/theme_heatmap.png and figures/theme_totals.png")
