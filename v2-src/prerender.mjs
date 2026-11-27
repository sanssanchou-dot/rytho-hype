// After `vite build`: one prerendered page per language so crawlers that don't run JS
// (GPTBot, ClaudeBot, PerplexityBot…) read real content:  /v2/ = 中文,  /v2/en/ = English.
// Each page gets its own title/description/canonical/OG + hreflang alternates + JSON-LD in that language.
// Also writes /llms.txt + /sitemap.xml. All copy comes from src/data.ts (single source) via Vite's SSR loader.
import fs from "node:fs"
import path from "node:path"
import { createServer } from "vite"
import puppeteer from "puppeteer-core"
import { serve, ROOT } from "./serve.mjs"

const CHROME = process.env.CHROME || "C:/Program Files/Google/Chrome/Application/chrome.exe"
const vite = await createServer({ server: { middlewareMode: true }, appType: "custom", logLevel: "error" })
const D = await vite.ssrLoadModule("/src/data.ts"); await vite.close()
const SITE = D.SITE_URL, BASE = SITE.replace(/v2\/$/, ""), IMGU = (f) => BASE + "img/" + f
const LANGS = { zh: { url: SITE, dir: "", html: "zh-Hant", og: "zh_TW" }, en: { url: SITE + "en/", dir: "en", html: "en", og: "en_US" } }
const esc = (s) => s.replace(/&/g, "&amp;").replace(/"/g, "&quot;").replace(/</g, "&lt;")
const today = new Date().toISOString().slice(0, 10)

// the built shell; the English copy lives one level down, so its asset paths go up one level
const shell = fs.readFileSync(path.join(ROOT, "v2", "index.html"), "utf8")
fs.mkdirSync(path.join(ROOT, "v2", "en"), { recursive: true })
fs.writeFileSync(path.join(ROOT, "v2", "en", "index.html"), shell.replaceAll('"./assets/', '"../assets/'))

// ---------- 1. snapshots ----------
const { srv, url } = serve(), origin = new URL(url).origin
const browser = await puppeteer.launch({ executablePath: CHROME })
const snap = {}
for (const [lang, L] of Object.entries(LANGS)) {
  const page = await browser.newPage(); await page.setViewport({ width: 1440, height: 900 })
  await page.evaluateOnNewDocument(() => { localStorage.setItem("rh2-theme", "dark"); localStorage.setItem("rh2-notes", "0") })
  await page.goto(url + (L.dir ? L.dir + "/" : ""), { waitUntil: "networkidle2", timeout: 60000 })
  const H = await page.evaluate(() => document.documentElement.scrollHeight)
  for (let y = 0; y < H; y += 500) { await page.evaluate((y) => scrollTo(0, y), y); await new Promise((r) => setTimeout(r, 80)) }
  await new Promise((r) => setTimeout(r, 1200))
  snap[lang] = await page.evaluate(() => {
    const r = document.getElementById("root").cloneNode(true)
    r.querySelectorAll("canvas").forEach((c) => c.remove())
    r.querySelectorAll("[style]").forEach((e) => { e.style.opacity = ""; e.style.transform = ""; e.style.filter = ""; e.style.backdropFilter = ""; if (!e.getAttribute("style")) e.removeAttribute("style") })
    return r.innerHTML
  })
  await page.close()
}
await browser.close(); srv.close()

// ---------- 2. per-language head + JSON-LD ----------
function head(lang) {
  const L = LANGS[lang], M = D.META, tr = (x) => x[lang]
  const alt = Object.entries(LANGS).map(([k, v]) => `<link rel="alternate" hreflang="${v.html}" href="${v.url}" />`).join("\n    ")
  const ld = { "@context": "https://schema.org", "@graph": [
    { "@type": "WebSite", "@id": SITE + "#site", url: SITE, name: "RYTHO HYPE", inLanguage: ["zh-Hant", "en"], publisher: { "@id": SITE + "#opq" } },
    { "@type": "Organization", "@id": SITE + "#opq", name: "OPQ Studio", url: SITE },
    { "@type": "WebPage", "@id": L.url + "#page", url: L.url, name: tr(M.title), description: tr(M.description), isPartOf: { "@id": SITE + "#site" }, inLanguage: L.html,
      primaryImageOfPage: { "@type": "ImageObject", url: IMGU("og_v2.jpg"), width: 1200, height: 630 }, dateModified: today },
    { "@type": "ItemList", name: lang === "zh" ? "RYTHO HYPE 產品系列" : "RYTHO HYPE product family", itemListElement: D.PRODUCTS.map((p, i) => ({ "@type": "ListItem", position: i + 1, item: {
      "@type": "Product", name: `RYTHO HYPE ${p.n} ${tr(p.name)}`, alternateName: p.en, description: tr(p.line), image: IMGU(p.closeup), brand: { "@type": "Brand", name: "RYTHO HYPE" },
      additionalProperty: [{ "@type": "PropertyValue", name: lang === "zh" ? "高度" : "Height", value: p.heightLabel }, ...p.facts.map((f) => ({ "@type": "PropertyValue", name: tr(f.k), value: tr(f.v) }))] } })) },
    { "@type": "FAQPage", inLanguage: L.html, mainEntity: D.FAQ.map((f) => ({ "@type": "Question", name: tr(f.q), acceptedAnswer: { "@type": "Answer", text: tr(f.a) } })) },
  ] }
  const other = lang === "zh" ? "en_US" : "zh_TW"
  return `<meta name="description" content="${esc(tr(M.description))}" />
    <link rel="canonical" href="${L.url}" />
    ${alt}
    <link rel="alternate" hreflang="x-default" href="${SITE}" />
    <meta property="og:type" content="website" />
    <meta property="og:site_name" content="RYTHO HYPE" />
    <meta property="og:locale" content="${L.og}" />
    <meta property="og:locale:alternate" content="${other}" />
    <meta property="og:title" content="${esc(tr(M.title))}" />
    <meta property="og:description" content="${esc(tr(M.ogDesc))}" />
    <meta property="og:url" content="${L.url}" />
    <meta property="og:image" content="${IMGU("og_v2.jpg")}" />
    <meta property="og:image:width" content="1200" />
    <meta property="og:image:height" content="630" />
    <meta property="og:image:alt" content="${esc(tr(M.ogAlt))}" />
    <meta name="twitter:card" content="summary_large_image" />
    <script type="application/ld+json">${JSON.stringify(ld).replace(/</g, "\\u003c")}</script>`
}

// ---------- 3. write both pages ----------
for (const [lang, L] of Object.entries(LANGS)) {
  const f = path.join(ROOT, "v2", L.dir, "index.html")
  let t = fs.readFileSync(f, "utf8")
  t = t.replace(/<html lang="[^"]*"/, `<html lang="${L.html}"`)
  t = t.replace(/<title>[^<]*<\/title>/, `<title>${esc(D.META.title[lang])}</title>`)
  t = t.replace("<!--head-->", head(lang))
  if (/localhost:\d+/.test(snap[lang].replaceAll(origin + "/img/", ""))) throw new Error("prerender: localhost URL left in " + lang + " HTML")
  // runtime image URLs are absolute (from the bundle URL); in static HTML they must be relative to this page
  const rel = L.dir ? "../../img/" : "../img/"
  t = t.replace('<div id="root"></div>', `<div id="root">${snap[lang].replaceAll(origin + "/img/", rel)}</div>`)
  fs.writeFileSync(f, t)
}

// ---------- 4. llms.txt + sitemap.xml (repo root = /rytho-hype/) ----------
const block = (lang) => {
  const tr = (x) => x[lang], zh = lang === "zh"
  return `## ${zh ? "產品" : "Products"}
${D.PRODUCTS.map((p) => `- ${p.n} ${tr(p.name)} (${p.en}): ${tr(p.line)} ${p.heightLabel}; ${p.facts.map((f) => tr(f.k) + ": " + tr(f.v)).join("; ")}`).join("\n")}

## ${zh ? "常見問題" : "FAQ"}
${D.FAQ.map((f) => `### ${tr(f.q)}\n${tr(f.a)}`).join("\n\n")}`
}
fs.writeFileSync(path.join(ROOT, "llms.txt"), `# RYTHO HYPE

> ${D.META.description.en}

## Pages
- [RYTHO HYPE (中文)](${LANGS.zh.url}): 完整介紹——影片、透明振膜、爆炸圖、四個產品、AI、合作方、常見問題
- [RYTHO HYPE (English)](${LANGS.en.url}): the full page in English
- [RYTHO HYPE v1](${BASE}): earlier pitch page (Chinese)

${block("en")}

${block("zh")}

## Note
- The acoustic particle animation is traced from the spiral channel geometry of the 261027 model; it is illustrative, not a simulation or measurement. 動畫為示意，非模擬或量測結果。
`)
fs.writeFileSync(path.join(ROOT, "sitemap.xml"), `<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">
${Object.values(LANGS).map((L) => `  <url><loc>${L.url}</loc><lastmod>${today}</lastmod>
${Object.values(LANGS).map((A) => `    <xhtml:link rel="alternate" hreflang="${A.html}" href="${A.url}" />`).join("\n")}
  </url>`).join("\n")}
  <url><loc>${BASE}</loc><lastmod>${today}</lastmod></url>
</urlset>
`)
console.log(`prerender ok: zh ${(snap.zh.length / 1024).toFixed(0)} KB, en ${(snap.en.length / 1024).toFixed(0)} KB baked; hreflang + JSON-LD per language; llms.txt + sitemap.xml written`)
