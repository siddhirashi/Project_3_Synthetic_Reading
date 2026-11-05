"""Steps 3-5: feed the whole story to the local LLM in order, segment by segment,
and write the extracted themes to Theme_JSON.py

Usage: python run_extraction.py
Needs: LM Studio local server running with a chat model loaded.
Edit MODEL, AUTHOR and AFFILIATION below.

Why segments? A 7B local model usually has a small context window. Cutting the
story into the same equal parts used for partial reading keeps every request
short, and it also tags each hit with its place in the story, which the
visualisation uses.
"""
import json
import pprint
import re
import sys
from pathlib import Path

import requests

sys.path.insert(0, str(Path(__file__).parent / "scripts"))
from partial_reading import equal_parts, split_units  # noqa: E402

BASE_URL = "http://localhost:1234/v1"
MODEL = "qwen2.5-7b-instruct"          # name as shown in LM Studio
STORY = "corpus/sultanas_dream.txt"
PARTS = 4                               # keep the same as in partial reading
AUTHOR = "[Enter Student Name(s)]"
AFFILIATION = "[Enter Department and Institution Name]"


def norm(s):
    return re.sub(r"\s+", " ", s).strip().lower()


SCHEMA = {
    "type": "json_schema",
    "json_schema": {
        "name": "theme_hits",
        "strict": True,
        "schema": {
            "type": "object",
            "properties": {"hits": {"type": "array", "items": {
                "type": "object",
                "properties": {
                    "theme": {"type": "string"},
                    "evidence": {"type": "string"},
                    "note": {"type": "string"},
                    "strength": {"type": "integer"}},
                "required": ["theme", "evidence", "note", "strength"]}}},
            "required": ["hits"]}}}


def call(prompt):
    payload = {"model": MODEL, "temperature": 0, "max_tokens": 3000,
               "messages": [{"role": "user", "content": prompt}]}
    # First ask LM Studio to force valid JSON; if the model/server refuses, retry plainly.
    r = requests.post(f"{BASE_URL}/chat/completions", timeout=900,
                      json={**payload, "response_format": SCHEMA})
    if r.status_code >= 400:
        r = requests.post(f"{BASE_URL}/chat/completions", timeout=900, json=payload)
    r.raise_for_status()
    return r.json()["choices"][0]["message"].get("content") or ""


def parse(reply):
    """Pull the list of hits out of a model reply, tolerating common mess."""
    text = re.sub(r"<think>.*?</think>", "", reply, flags=re.S)       # reasoning models
    text = re.sub(r"```(?:json)?", "", text)                          # markdown fences
    for open_c, close_c in (("{", "}"), ("[", "]")):
        a, b = text.find(open_c), text.rfind(close_c)
        if a == -1 or b <= a:
            continue
        chunk = text[a:b + 1]
        for candidate in (chunk, re.sub(r",\s*([}\]])", r"\1", chunk)):  # trailing commas
            try:
                obj = json.loads(candidate)
            except ValueError:
                continue
            if isinstance(obj, dict) and isinstance(obj.get("hits"), list):
                return obj["hits"]
            if isinstance(obj, list):
                return obj
    return None


def main():
    cfg = json.loads(Path("themes.json").read_text(encoding="utf-8"))
    template = Path("prompt.txt").read_text(encoding="utf-8")
    themes = cfg["themes"]
    paras = split_units(Path(STORY).read_text(encoding="utf-8"), "paragraph")
    segments = ["\n\n".join(p) for p in equal_parts(paras, PARTS)]

    data, dropped = [], []
    for no, seg in enumerate(segments, 1):
        prompt = (template.replace("{{RESEARCH_QUESTION}}", cfg["research_question"])
                  .replace("{{SEGMENT_NO}}", str(no)).replace("{{TOTAL}}", str(PARTS))
                  .replace("{{THEME_LIST}}", "\n".join(f"- {t}" for t in themes))
                  .replace("{{TEXT}}", seg))
        reply = call(prompt)
        hits = parse(reply)
        if hits is None:
            reply = call(prompt)                 # one retry
            hits = parse(reply)
        if hits is None:
            Path(f"debug_segment_{no}.txt").write_text(reply, encoding="utf-8")
            print(f"segment {no}: unreadable reply, skipped. Model said: {reply[:200]!r}")
            print(f"           full reply saved in debug_segment_{no}.txt")
            continue
        for h in hits:
            ok_theme = h.get("theme") in themes
            ok_quote = norm(str(h.get("evidence", ""))) in norm(seg)
            row = {"segment": no, "theme": h.get("theme"), "evidence": h.get("evidence"),
                   "note": h.get("note"), "strength": h.get("strength", 1),
                   "quote_verified": ok_quote}
            (data if ok_theme else dropped).append(row)
        print(f"segment {no}/{PARTS}: {len(hits)} hits")

    if not data:
        print("\nNo usable hits, so Theme_JSON.py was NOT written. Open debug_segment_1.txt "
              "to see what the model returned, then see the fixes in the README.")
        return

    bar = "=" * 59
    body = f'''"""
{bar}
Topic: Theme extraction for synthetic reading
{bar}
Author Name(s): {AUTHOR}
Short Description: Themes extracted by a local LLM ({MODEL}, LM Studio)
from {STORY}, read in {PARTS} ordered segments. Research question:
{cfg["research_question"]}
quote_verified is True when the quotation was found word for word in the
segment; check every False entry by hand before using it.
Semester: Monsoon Semester 2026
Affiliation: {AFFILIATION}
{bar}
"""

research_question = {cfg["research_question"]!r}

theme_vocabulary = {pprint.pformat(themes, width=88)}

theme_data = {pprint.pformat(data, width=88, sort_dicts=False)}
'''
    Path("Theme_JSON.py").write_text(body, encoding="utf-8")
    print(f"Theme_JSON.py written: {len(data)} hits, {sum(not d['quote_verified'] for d in data)} unverified quotes, {len(dropped)} dropped (label not in list)")


if __name__ == "__main__":
    main()
