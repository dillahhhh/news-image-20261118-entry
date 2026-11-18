# news-image-20261118 — The World Chronicle

Sum up 18 November 2026's world news in one image. make.fun bounty entry.

## How it works

- `stories.json` — the day's stories: lead, features, six desks, hot list,
  ticker, footer. Swapping the content means swapping this file.
- `tools/render.py` — build-time renderer. It builds a broadsheet page from
  `stories.json` (local fonts in `tools/fonts/`), screenshots it with
  Playwright + Chromium at 1600x2360, then shrinks it to fit the competition
  limits (1024x1024, 1 MiB) and writes `assets/entry.png`.
- `main.ts` — the submitted program. It only copies `assets/entry.png` to
  `$MAKEFUN_OUTPUT_DIR/entry.png` (or `/output/entry.png`). No network, and
  every run writes the same bytes.

## Rebuild the image

```bash
python3 tools/render.py
```

## Test the program

```bash
mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts
```

## Status

18 NOVEMBER 2026 content — 17 stories, all verified from primary sources
(see VERIFICATION.md). Built, rendered at 1024x1024, determinism checked
(two runs byte-identical). NO SUBMIT — build only, by the owner's order.
