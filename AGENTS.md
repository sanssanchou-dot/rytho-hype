# RYTHO HYPE site

Two versions, one repo (GitHub Pages → https://sanssanchou-dot.github.io/rytho-hype/):
- `/` — v1, hand-written `index.html` + `lg.js`, edited by scripts in `_tools/`. Frozen; fix only on request.
- `/v2/` — built from `v2-src/` (Vite + React + shadcn/ui + motion). **Edit `v2-src/`, never `v2/`** (build output).

## Standard website workflow (every change)
1. Edit `v2-src/src/`. Colours/radius/shadows/fonts live only in `src/index.css` tokens (tweakcn format, `:root`/.dark/.rytho/.light) — no per-component colours, no `!important`.
   Copy and product data live only in `src/data.ts`; FAQ answers there are facts only (no acoustic performance claims — see ../../聲學設計強制規則.md §3).
2. `npm --prefix v2-src run build` — typecheck → vite build → `prerender.mjs` (bakes HTML for non-JS AI crawlers, JSON-LD, writes `/llms.txt` + `/sitemap.xml`).
3. `npm --prefix v2-src run qa` — 3 themes × desktop/mobile + interactions + SEO/GEO static checks; screenshots in `v2-src/qa-out/`. **Look at the screenshots**, not just PASS.
4. Commit with `-c user.name=sanssanchou-dot -c user.email=sanssanchou-dot@users.noreply.github.com`, push (pre-push hook re-runs QA).
5. After deploy: `/geo quick https://sanssanchou-dot.github.io/rytho-hype/v2/`; run `/geo audit` before any public launch.

## Gotchas
- Images are shared from `../img/` (referenced as `../img/x` from /v2/). Render sources: c01–04 ← family_shot/closeup_v4, arch_* ← scene_arch, hifi6_* ← bespoke_style_v2, explode/* ← explode_pair_v2 (all under RYTHO_HYPE_RENDER_PROOFS_20261123/).
- Dark-backdrop renders sit in `.stage` (dark card in LIGHT); white-background body cutouts (b_*, fin_*, hifi6_*) sit on a white card. Never feather dark renders into white.
- Project Pages can't own `robots.txt` (it's the domain root). AI crawler access is governed by github.io's robots; a custom domain would fix this.
- ffmpeg: `C:/Users/san/AppData/Local/Programs/Python/Python313/Lib/site-packages/imageio_ffmpeg/binaries/ffmpeg-win-x86_64-v7.1.exe`.
- Puppeteer `clip` uses page coordinates — screenshot the viewport, then crop.
