// Tiny static server for ../ (RYTHO_HYPE_WEB root) with Range support — shared by qa.mjs and prerender.mjs.
import http from "node:http"
import fs from "node:fs"
import path from "node:path"
export const ROOT = path.resolve(import.meta.dirname, "..")
const TYPES = { ".html": "text/html; charset=utf-8", ".js": "text/javascript", ".css": "text/css", ".webp": "image/webp", ".jpg": "image/jpeg", ".png": "image/png", ".json": "application/json", ".mp4": "video/mp4", ".svg": "image/svg+xml", ".txt": "text/plain; charset=utf-8", ".xml": "application/xml" }
export function serve() {
  const srv = http.createServer((req, res) => {
    let p = decodeURIComponent(new URL(req.url, "http://x").pathname); if (p.endsWith("/")) p += "index.html"
    const f = path.join(ROOT, p); if (!f.startsWith(ROOT) || !fs.existsSync(f)) { res.writeHead(404); return res.end() }
    const st = fs.statSync(f), type = TYPES[path.extname(f)] || "application/octet-stream", range = req.headers.range
    if (range) { const [a, b] = range.replace("bytes=", "").split("-"); const s = +a, e = b ? +b : st.size - 1
      res.writeHead(206, { "Content-Type": type, "Content-Range": `bytes ${s}-${e}/${st.size}`, "Accept-Ranges": "bytes", "Content-Length": e - s + 1 }); return fs.createReadStream(f, { start: s, end: e }).pipe(res) }
    res.writeHead(200, { "Content-Type": type, "Content-Length": st.size, "Accept-Ranges": "bytes" }); fs.createReadStream(f).pipe(res)
  }).listen(0)
  return { srv, url: `http://localhost:${srv.address().port}/v2/` }
}
