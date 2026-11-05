# Corpus

The story is Rokeya Sakhawat Hossain's "Sultana's Dream", first published in 1905 in *The Indian Ladies' Magazine* (Madras), in English. It is in the public domain, so the full text can sit in this repository.

| File | What it is |
|---|---|
| `sultanas_dream_raw.txt` | The text as I copied it from a public-domain online copy, with its original line breaks |
| `sultanas_dream.txt` | The cleaned version that every script uses (about 4,000 words, 140 paragraphs) |

The clean file was made with:

```bash
python scripts/preprocess.py corpus/sultanas_dream_raw.txt corpus/sultanas_dream.txt
```

`preprocess.py` removes any Project Gutenberg header and footer, joins lines that were hard-wrapped, collapses extra spaces and keeps one blank line between paragraphs. I read the result once for broken words.

Note that the first two "paragraphs" of the clean file are the title line and the publication note, not story text. They are counted in the 140.
