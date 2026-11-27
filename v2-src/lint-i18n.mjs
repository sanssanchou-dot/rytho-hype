// i18n guardrail: visible copy lives only in src/data.ts as { zh, en } pairs.
// Fails if any other source file contains CJK text outside comments (= untranslated hard-coded copy).
import fs from "node:fs"
import path from "node:path"
const SRC = path.resolve(import.meta.dirname, "src"), ALLOW = new Set(["data.ts"])
const CJK = /[㐀-鿿＀-￯　-〿]/
const hits = []
const walk = (d) => fs.readdirSync(d, { withFileTypes: true }).forEach((e) => {
  const f = path.join(d, e.name)
  if (e.isDirectory()) return walk(f)
  if (!/\.(tsx?|jsx?)$/.test(e.name) || ALLOW.has(e.name)) return
  fs.readFileSync(f, "utf8").replace(/\/\*[\s\S]*?\*\//g, (m) => m.replace(/[^\n]/g, " ")).split("\n").forEach((l, i) => {
    const code = l.replace(/\/\/.*$/, ""); if (CJK.test(code)) hits.push(`${path.relative(SRC, f)}:${i + 1}  ${code.trim().slice(0, 90)}`)
  })
})
walk(SRC)
if (hits.length) { console.error("i18n: hard-coded CJK copy outside src/data.ts — move it into a { zh, en } pair:\n" + hits.join("\n")); process.exit(1) }
console.log("i18n ok")
