// QA against the BUILT site (../v2 served from ../): 2 languages × 3 themes × desktop/mobile.
// Fails on: page errors, console errors, failed requests, horizontal overflow, broken images,
// language switch not working, and SEO/GEO static checks on each language's raw HTML (what non-JS AI crawlers see).
// Usage: npm run qa            (screens -> qa-out/, add --shots=0 to skip screenshots)
import fs from "node:fs"
import path from "node:path"
import puppeteer from "puppeteer-core"
import { serve } from "./serve.mjs"

const OUT = path.resolve(import.meta.dirname, "qa-out"), ROOT = path.resolve(import.meta.dirname, "..")
const SHOTS = !process.argv.includes("--shots=0")
const CHROME = process.env.CHROME || "C:/Program Files/Google/Chrome/Application/chrome.exe"
const { srv, url: URL0 } = serve()
fs.mkdirSync(OUT, { recursive: true })

const LANGS = { zh: "", en: "en/" }
// CJK allowed on the English page: partner proper nouns only (no official English names)
const PROPER = /玻音先創|玩樂生活|(?<![㐀-鿿])中(?![㐀-鿿])/g // + the "中" language-switch label
const CJK = /[\u3400-\u9fff\uff00-\uffef\u3000-\u303f]/
const VIEWS = { d: { width: 1440, height: 900 }, m: { width: 390, height: 844, isMobile: true, hasTouch: true, deviceScaleFactor: 2 } }
const browser = await puppeteer.launch({ executablePath: CHROME, args: ["--autoplay-policy=no-user-gesture-required"] })
const fails = []
const wait = (ms) => new Promise((r) => setTimeout(r, ms))

for (const [lang, sub] of Object.entries(LANGS)) for (const theme of ["dark", "rytho", "light"]) for (const [vk, vp] of Object.entries(VIEWS)) {
  const tag = `${lang}/${theme}/${vk}`, pre = `${lang}_${theme}_${vk}`, page = await browser.newPage(); await page.setViewport(vp)
  await page.evaluateOnNewDocument((t) => localStorage.setItem("rh2-theme", t), theme)
  page.on("pageerror", (e) => fails.push(`${tag} pageerror: ${e.message}`))
  page.on("console", (m) => m.type() === "error" && fails.push(`${tag} console: ${m.text()}`))
  page.on("requestfailed", (r) => !r.url().includes("fonts.g") && !/\.mp4/.test(r.url()) && fails.push(`${tag} requestfailed: ${r.url()}`))
  page.on("response", (r) => r.status() >= 400 && fails.push(`${tag} HTTP ${r.status()}: ${r.url()}`))
  await page.goto(URL0 + sub, { waitUntil: "networkidle2", timeout: 60000 })
  // walk the page so whileInView reveals + lazy images fire
  const H = await page.evaluate(() => document.documentElement.scrollHeight)
  for (let y = 0; y < H; y += vp.height * .6) { await page.evaluate((y) => scrollTo(0, y), y); await wait(120) }
  await page.evaluate(() => scrollTo(0, 0)); await wait(600)
  const r = await page.evaluate(() => ({
    sw: document.documentElement.scrollWidth, iw: innerWidth, lang: document.documentElement.lang,
    text: document.querySelector("main").innerText,
    broken: [...document.images].filter((i) => i.complete && i.naturalWidth === 0 && i.getAttribute("src")).map((i) => i.getAttribute("src")),
    sections: [...document.querySelectorAll("main > section")].map((s) => [s.id, Math.round(s.getBoundingClientRect().height)]),
  }))
  if (r.sw > r.iw + 1) fails.push(`${tag} horizontal overflow: scrollWidth ${r.sw} > ${r.iw}`)
  r.broken.forEach((b) => fails.push(`${tag} broken image: ${b}`))
  if (lang === "en") {
    if (r.lang !== "en") fails.push(`${tag} <html lang> is "${r.lang}", expected en`)
    const left = r.text.replace(PROPER, "").split("\n").filter((l) => CJK.test(l))
    left.slice(0, 5).forEach((l) => fails.push(`${tag} untranslated: ${l.trim().slice(0, 80)}`))
  }
  console.log(tag.padEnd(14), r.sections.map(([id, h]) => `${id}:${h}`).join(" "))
  if (SHOTS) for (const [id] of r.sections) {
    await page.evaluate((id) => { document.documentElement.style.scrollBehavior = "auto"; document.getElementById(id).scrollIntoView() }, id)
    await wait(900)
    await page.screenshot({ path: path.join(OUT, `${pre}_${id}.jpg`), type: "jpeg", quality: 70 })
  }
  // interactions (desktop, dark only per language to keep the run short): explode, product 04 + Hi-Fi, language switch
  if (vk === "d" && (SHOTS ? true : theme === "dark")) {
    const click = (sel, text) => page.evaluate((sel, text) => { const b = [...document.querySelectorAll(sel)].find((e) => e.textContent.trim() === text || e.textContent.includes(text)); b?.scrollIntoView({ block: "center" }); b?.click(); return !!b }, sel, text)
    if (!(await click("#explode button", "Explode"))) fails.push(`${tag} interaction: Explode button missing`)
    await wait(2600); await page.evaluate(() => document.getElementById("explode").scrollIntoView()); await wait(500)
    if (SHOTS) await page.screenshot({ path: path.join(OUT, `${pre}_x_explode-open.jpg`), type: "jpeg", quality: 70 })
    await click("#products [role=radio]", "04"); await wait(900)
    await click("#products [role=radio]", "Hi-Fi"); await wait(1200)
    await page.evaluate(() => document.getElementById("products").scrollIntoView()); await wait(600)
    if (SHOTS) await page.screenshot({ path: path.join(OUT, `${pre}_x_p04-hifi.jpg`), type: "jpeg", quality: 70 })
    // switch language in place: URL, <html lang> and copy must all follow
    const to = lang === "zh" ? "en" : "zh"
    if (!(await click("header [role=radio]", to === "en" ? "EN" : "中"))) fails.push(`${tag} language switch missing`)
    await wait(900)
    const s = await page.evaluate(() => ({ path: location.pathname, lang: document.documentElement.lang, h: document.querySelector("#faq h2")?.textContent }))
    const okPath = to === "en" ? /\/v2\/en\/$/.test(s.path) : /\/v2\/$/.test(s.path)
    const okCopy = to === "en" ? s.h?.startsWith("FAQ") : s.h?.startsWith("常見問題")
    if (!okPath || !okCopy || !s.lang.startsWith(to === "en" ? "en" : "zh")) fails.push(`${tag} language switch → ${to} failed: ${JSON.stringify(s)}`)
  }
  await page.close()
}

// ---------- SEO / GEO static checks per language: the raw HTML, no JS (GPTBot / ClaudeBot / PerplexityBot view) ----------
for (const [lang, sub] of Object.entries(LANGS)) {
  const raw = fs.readFileSync(path.join(ROOT, "v2", sub, "index.html"), "utf8")
  const need = (ok, msg) => ok || fails.push(`seo/${lang}: ` + msg)
  const meta = (k) => (raw.match(new RegExp(`<meta[^>]+(?:name|property)="${k}"[^>]+content="([^"]*)"`)) || [])[1]
  const title = (raw.match(/<title>([^<]*)<\/title>/) || [])[1] || ""
  need(new RegExp(`<html[^>]+lang="${lang === "en" ? "en" : "zh-Hant"}"`).test(raw), "<html lang> wrong or missing")
  need(title.length >= 10 && title.length <= 70, `title length ${title.length} (10–70)`)
  const desc = meta("description") || ""; need(desc.length >= 50 && desc.length <= 320, `meta description length ${desc.length} (50–320)`)
  need(/<link rel="canonical" href="https:\/\//.test(raw), "canonical missing")
  need(/hreflang="zh-Hant"/.test(raw) && /hreflang="en"/.test(raw) && /hreflang="x-default"/.test(raw), "hreflang alternates missing")
  for (const k of ["og:title", "og:description", "og:image", "og:url", "twitter:card"]) need(meta(k), k + " missing")
  const ogImg = meta("og:image"); if (ogImg) need(fs.existsSync(path.join(ROOT, ogImg.replace(/^https?:\/\/[^/]+\/rytho-hype\//, ""))), "og:image file not in repo: " + ogImg)
  const lds = [...raw.matchAll(/<script type="application\/ld\+json">([\s\S]*?)<\/script>/g)].map((m) => { try { return JSON.parse(m[1]) } catch { need(false, "JSON-LD does not parse"); return null } })
  const types = JSON.stringify(lds); for (const ty of ["WebSite", "Organization", "FAQPage", "ItemList"]) need(types.includes(`"@type":"${ty}"`), `JSON-LD ${ty} missing`)
  const root = (raw.match(/<div id="root">([\s\S]*)<\/div>\s*<\/body>/) || [])[1] || ""
  const text = root.replace(/<script[\s\S]*?<\/script>/g, "").replace(/<[^>]+>/g, " ").replace(/\s+/g, " ").trim()
  need(text.length > 1500, `prerendered text only ${text.length} chars — is prerender.mjs running?`)
  need((root.match(/<h1[\s>]/g) || []).length === 1, "exactly one <h1> expected in prerendered HTML")
  need((root.match(/<h2[\s>]/g) || []).length >= 6, "fewer than 6 <h2> in prerendered HTML")
  const noAlt = (root.match(/<img(?![^>]*alt=)[^>]*>/g) || []).length; need(!noAlt, `${noAlt} <img> without alt`)
  need(!/localhost:\d+/.test(root), "localhost URL baked into HTML")
  need(!/待補：|To do: /.test(text), "internal to-do notes leaked into prerendered HTML")
  if (lang === "en") { const left = text.replace(PROPER, "").match(/[\u3400-\u9fff]+/g) || []; need(!left.length, `untranslated CJK in English HTML: ${left.slice(0, 5).join(" ")}`) }
  console.log(`seo/${lang}`.padEnd(14), `title ${title.length} · desc ${desc.length} · text ${text.length} chars · JSON-LD ${lds.length}`)
}
for (const f of ["llms.txt", "sitemap.xml"]) if (!fs.existsSync(path.join(ROOT, f))) fails.push(`seo: ${f} missing`)

await browser.close(); srv.close()
if (fails.length) { console.log("\nFAIL\n" + [...new Set(fails)].join("\n")); process.exit(1) }
console.log("\nPASS")
