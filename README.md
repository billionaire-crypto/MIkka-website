# Mikka Chinbaatar Website

Personal website for Mikka Chinbaatar — piano instructor / collaborative pianist / yatga soloist (San Francisco, CA).

## Files

| File | Purpose |
| --- | --- |
| [`hero_page_clean.html`](hero_page_clean.html) | Hero section (production) |
| [`awards_page_clean.html`](awards_page_clean.html) | Awards & Distinctions section (production) |
| [`index.html`](index.html) | Local preview — stacks both pages in iframes |
| [`_prep.py`](_prep.py) | One-shot cleanup script: rewrites smart quotes, en-dashes, and stray glyphs from the source `.txt` files into clean `.html` |
| [`LOCKED V! CODE.txt`](LOCKED%20V%21%20CODE.txt) | Signed-off design spec — palette, typography, type scale, hero v2, awards v4 |

## Local preview

```bash
cd "Mikka website"
python -m http.server 8765
# open http://localhost:8765/
```

## Versioning workflow

- `main` is the baseline / "factory reset" point — always known-good.
- Each change goes on its own feature branch and merges into `main` via a PR.
- Every merged PR is a labeled snapshot in history.
- To revert any change: `git revert <commit-sha>` (safe — keeps history) or `git checkout <prior-commit>` (browse the old state without changing anything).
