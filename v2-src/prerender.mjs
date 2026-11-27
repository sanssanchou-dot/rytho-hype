// After `vite build`: bake the rendered page into ../v2/index.html so crawlers that don't run JS
// (GPTBot, ClaudeBot, PerplexityBot…) read real content; add JSON-LD; write llms.txt + sitemap.xml.
// Data comes from src/data.ts (single source) via Vite's SSR loader.
import fs from "node:fs"
import path from "node:path"
import { createServer } from "vite"
import puppeteer from "puppeteer-core"
import { serve, ROOT } from "./serve.mjs"

const CHROME = process.env.CHROME || "C:/Program Files/Google/Chrome/Application/chrome.exe"
const vite = await createServer({ server: { middlewareMode: true }, appType: "custom", logLevel: "error" })
const D = await vite.ssrLoadModule("/src/data.ts"); await vite.close()
const SITE = D.SITE_URL, BASE = SITE.replace(/v2\/$/, ""), IMGU = (f) => BASE + "img/" + f

// ---------- 1. snapshot ----------
const { srv, url } = serve()
const browser = await puppeteer.launch({ executablePath: CHROME })
const page = await browser.newPage(); await page.setViewport({ width: 1440, height: 900 })
await page.evaluateOnNewDocument(() => { localStorage.setItem("rh2-theme", "dark"); localStorage.setItem("rh2-notes", "0") })
await page.goto(url, { waitUntil: "networkidle2", timeout: 60000 })
const H = await page.evaluate(() => document.documentElement.scrollHeight)
for (let y = 0; y < H; y += 500) { await page.evaluate((y) => scrollTo(0, y), y); await new Promise((r) => setTimeout(r, 80)) }
await new Promise((r) => setTimeout(r, 1200))
const html = await page.evaluate(() => {
  const r = document.getElementById("root").cloneNode(true)
  r.querySelectorAll("canvas").forEach((c) => c.remove())
  r.querySelectorAll("[style]").forEach((e) => { e.style.opacity = ""; e.style.transform = ""; e.style.filter = ""; e.style.backdropFilter = ""; if (!e.getAttribute("style")) e.removeAttribute("style") })
  return r.innerHTML
})
await browser.close(); srv.close()

// ---------- 2. JSON-LD ----------
const org = { "@type": "Organization", "@id": SITE + "#opq", name: "OPQ Studio", url: SITE }
const ld = { "@context": "https://schema.org", "@graph": [
  { "@type": "WebSite", "@id": SITE + "#site", url: SITE, name: "RYTHO HYPE", inLanguage: ["zh-Hant", "en"], description: D.SUMMARY_EN, publisher: { "@id": SITE + "#opq" } },
  org,
  { "@type": "WebPage", "@id": SITE + "#page", url: SITE, name: "RYTHO HYPE — 讓聲音第一次被看見", isPartOf: { "@id": SITE + "#site" }, inLanguage: "zh-Hant",
    primaryImageOfPage: { "@type": "ImageObject", url: IMGU("og_v2.jpg"), width: 1200, height: 630 }, dateModified: new Date().toISOString().slice(0, 10) },
  { "@type": "ItemList", name: "RYTHO HYPE 產品系列", itemListElement: D.PRODUCTS.map((p, i) => ({ "@type": "ListItem", position: i + 1, item: {
    "@type": "Product", name: `RYTHO HYPE ${p.n} ${p.zh}`, alternateName: p.en, description: p.line, image: IMGU(p.closeup), brand: { "@type": "Brand", name: "RYTHO HYPE" },
    additionalProperty: [{ "@type": "PropertyValue", name: "高度", value: p.heightLabel }, ...p.facts.map((f) => ({ "@type": "PropertyValue", name: f.k, value: f.v }))] } })) },
  { "@type": "FAQPage", inLanguage: "zh-Hant", mainEntity: D.FAQ.map((f) => ({ "@type": "Question", name: f.q, acceptedAnswer: { "@type": "Answer", text: f.a } })) },
  { "@type": "FAQPage", inLanguage: "en", mainEntity: D.FAQ_EN.map((f) => ({ "@type": "Question", name: f.q, acceptedAnswer: { "@type": "Answer", text: f.a } })) },
] }

// ---------- 3. write index.html ----------
const out = path.join(ROOT, "v2", "index.html")
let t = fs.readFileSync(out, "utf8")
t = t.replace("<!--jsonld-->", `<script type="application/ld+json">${JSON.stringify(ld).replace(/</g, "\u003c")}</script>`)
t = t.replace('<div id="root"></div>', `<div id="root">${html}</div>`)
fs.writeFileSync(out, t)

// ---------- 4. llms.txt + sitemap.xml (repo root = /rytho-hype/) ----------
const llms = `# RYTHO HYPE

> 透明喇叭產品概念：以玻音先創的透明玻璃振膜為核心，搭配透明箱體與螺旋葉片內構，讓發聲結構被看見。OPQ Studio（設計）× Rytho（軟體）× 玻音先創（單體）× 玩樂生活（DSP）。目前為概念與樣機階段，尚未販售。

## 主要頁面
- [RYTHO HYPE v2](${SITE}): 完整介紹——影片、透明振膜、爆炸圖、四個產品、AI、合作方、常見問題
- [RYTHO HYPE v1](${BASE}): 前一版提案頁

## 產品
${D.PRODUCTS.map((p) => `- ${p.n} ${p.zh}（${p.en}）：${p.line} ${p.heightLabel}；${p.facts.map((f) => f.k + "：" + f.v).join("；")}`).join("\n")}

## 常見問題
${D.FAQ.map((f) => `### ${f.q}\n${f.a}`).join("\n\n")}

## 注意
- 網站上的聲學粒子動畫取自 261027 模型的螺旋流道幾何，屬示意，非模擬或量測結果。

## English
${D.SUMMARY_EN}

${D.FAQ_EN.map((f) => `### ${f.q}\n${f.a}`).join("\n\n")}
`
fs.writeFileSync(path.join(ROOT, "llms.txt"), llms)
const today = new Date().toISOString().slice(0, 10)
fs.writeFileSync(path.join(ROOT, "sitemap.xml"), `<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url><loc>${SITE}</loc><lastmod>${today}</lastmod></url>
  <url><loc>${BASE}</loc><lastmod>${today}</lastmod></url>
</urlset>
`)
console.log(`prerender ok: ${(html.length / 1024).toFixed(0)} KB of HTML baked, JSON-LD ${ld["@graph"].length} nodes, llms.txt + sitemap.xml written`)
