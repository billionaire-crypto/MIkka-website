# Mikka Chinbaatar Website

Personal website for Mikka Chinbaatar — piano instructor / collaborative pianist / yatga soloist (San Francisco, CA).

## Files

| File | Purpose |
| --- | --- |
| [`index.html`](index.html) | The site — hero + Awards & Distinctions sections in one page |
| [`IMG_3282.jpeg`](IMG_3282.jpeg) | Hero portrait (Naru Photography) |
| [`vercel.json`](vercel.json) | Vercel static-hosting config (clean URLs, image caching) |

> **Note:** the Awards section currently contains `[placeholder]` entries —
> replace them with the real awards before sharing the live site.

## Local preview

```bash
python -m http.server 8765
# open http://localhost:8765/
```

## Deploying on Vercel

The repo is a plain static site — no build step.

1. Go to [vercel.com/new](https://vercel.com/new) and import
   `billionaire-crypto/MIkka-website` from GitHub.
2. Leave **Framework Preset** as **Other**; no build command, no output
   directory — the defaults are correct.
3. Deploy. Every push to `main` redeploys production automatically;
   every branch push gets a preview URL.

## Versioning workflow

- `main` is the baseline / "factory reset" point — always known-good.
- Each change goes on its own feature branch and merges into `main` via a PR.
- Every merged PR is a labeled snapshot in history.
- To revert any change: `git revert <commit-sha>` (safe — keeps history) or `git checkout <prior-commit>` (browse the old state without changing anything).
