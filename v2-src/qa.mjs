// QA: 3 themes × desktop/mobile against the BUILT site (../v2 served from ../).
// Fails on: page errors, console errors, failed requests, horizontal overflow, broken images.
// Usage: npm run qa            (screens -> qa-out/, add --shots=0 to skip screenshots)
import http from "node:http"
import fs from "node:fs"
import path from "node:path"
import puppeteer from "puppeteer-core"

const ROOT = path.resolve(import.meta.dirname, "..")
const OUT = path.resolve(import.meta.dirname, "qa-out")
const SHOTS = !process.argv.includes("--shots=0")
const CHROME = process.env.CHROME || "C:/Program Files/Google/Chrome/Application/chrome.exe"
const TYPES = { ".html": "text/html", ".js": "text/javascript", ".css": "text/css", ".webp": "image/webp", ".jpg": "image/jpeg", ".png": "image/png", ".json": "application/json", ".mp4": "video/mp4", ".svg": "image/svg+xml" }

const srv = http.createServer((req, res) => {
  let p = decodeURIComponent(new URL(req.url, "http://x").pathname); if (p.endsWith("/")) p += "index.html"
  const f = path.join(ROOT, p); if (!f.startsWith(ROOT) || !fs.existsSync(f)) { res.writeHead(404); return res.end() }
  const st = fs.statSync(f), type = TYPES[path.extname(f)] || "application/octet-stream", range = req.headers.range
  if (range) { const [a, b] = range.replace("bytes=", "").split("-"); const s = +a, e = b ? +b : st.size - 1
    res.writeHead(206, { "Content-Type": type, "Content-Range": `bytes ${s}-${e}/${st.size}`, "Accept-Ranges": "bytes", "Content-Length": e - s + 1 }); return fs.createReadStream(f, { start: s, end: e }).pipe(res) }
  res.writeHead(200, { "Content-Type": type, "Content-Length": st.size, "Accept-Ranges": "bytes" }); fs.createReadStream(f).pipe(res)
}).listen(0)
const URL0 = `http://localhost:${srv.address().port}/v2/`
fs.mkdirSync(OUT, { recursive: true })

const VIEWS = { d: { width: 1440, height: 900 }, m: { width: 390, height: 844, isMobile: true, hasTouch: true, deviceScaleFactor: 2 } }
const browser = await puppeteer.launch({ executablePath: CHROME, args: ["--autoplay-policy=no-user-gesture-required"] })
const fails = []
for (const theme of ["dark", "rytho", "light"]) for (const [vk, vp] of Object.entries(VIEWS)) {
  const tag = `${theme}/${vk}`, page = await browser.newPage(); await page.setViewport(vp)
  await page.evaluateOnNewDocument((t) => localStorage.setItem("rh2-theme", t), theme)
  page.on("pageerror", (e) => fails.push(`${tag} pageerror: ${e.message}`))
  page.on("console", (m) => m.type() === "error" && fails.push(`${tag} console: ${m.text()}`))
  page.on("requestfailed", (r) => !r.url().includes("fonts.g") && !/\.mp4/.test(r.url()) && fails.push(`${tag} requestfailed: ${r.url()}`))
  page.on("response", (r) => r.status() >= 400 && fails.push(`${tag} HTTP ${r.status()}: ${r.url()}`))
  await page.goto(URL0, { waitUntil: "networkidle2", timeout: 60000 })
  // walk the page so whileInView reveals + lazy images fire
  const H = await page.evaluate(() => document.documentElement.scrollHeight)
  for (let y = 0; y < H; y += vp.height * .6) { await page.evaluate((y) => scrollTo(0, y), y); await new Promise((r) => setTimeout(r, 120)) }
  await page.evaluate(() => scrollTo(0, 0)); await new Promise((r) => setTimeout(r, 600))
  const r = await page.evaluate(() => ({
    sw: document.documentElement.scrollWidth, iw: innerWidth,
    broken: [...document.images].filter((i) => i.complete && i.naturalWidth === 0 && i.getAttribute("src")).map((i) => i.getAttribute("src")),
    sections: [...document.querySelectorAll("main > section")].map((s) => [s.id, Math.round(s.getBoundingClientRect().height)]),
  }))
  if (r.sw > r.iw + 1) fails.push(`${tag} horizontal overflow: scrollWidth ${r.sw} > ${r.iw}`)
  r.broken.forEach((b) => fails.push(`${tag} broken image: ${b}`))
  console.log(tag.padEnd(9), r.sections.map(([id, h]) => `${id}:${h}`).join(" "))
  if (SHOTS) for (const [id] of r.sections) {
    await page.evaluate((id) => { document.documentElement.style.scrollBehavior = "auto"; document.getElementById(id).scrollIntoView() }, id)
    await new Promise((res) => setTimeout(res, 900))
    await page.screenshot({ path: path.join(OUT, `${theme}_${vk}_${id}.jpg`), type: "jpeg", quality: 70 })
  }
  // interactions (desktop): explode open, product 04 + Hi-Fi body
  if (SHOTS && vk === "d") {
    const click = (sel, text) => page.evaluate((sel, text) => { const b = [...document.querySelectorAll(sel)].find((e) => e.textContent.includes(text)); b?.scrollIntoView({ block: "center" }); b?.click(); return !!b }, sel, text)
    if (!(await click("#explode button", "Explode"))) fails.push(`${tag} interaction: Explode button missing`)
    await new Promise((r) => setTimeout(r, 2600)); await page.evaluate(() => document.getElementById("explode").scrollIntoView())
    await new Promise((r) => setTimeout(r, 500)); await page.screenshot({ path: path.join(OUT, `${theme}_${vk}_x_explode-open.jpg`), type: "jpeg", quality: 70 })
    await click("#products [role=radio]", "04"); await new Promise((r) => setTimeout(r, 900))
    await click("#products [role=radio]", "Hi-Fi"); await new Promise((r) => setTimeout(r, 1200))
    await page.evaluate(() => document.getElementById("products").scrollIntoView()); await new Promise((r) => setTimeout(r, 600))
    await page.screenshot({ path: path.join(OUT, `${theme}_${vk}_x_p04-hifi.jpg`), type: "jpeg", quality: 70 })
  }
  await page.close()
}
await browser.close(); srv.close()
if (fails.length) { console.log("\nFAIL\n" + [...new Set(fails)].join("\n")); process.exit(1) }
console.log("\nPASS")
