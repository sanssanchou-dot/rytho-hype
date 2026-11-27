import * as React from "react"
import { motion } from "motion/react"
import { IMG, UI } from "@/data"
import { useApp, useT } from "@/app-state"

type Paths = { path: [number, number, number | null, string][]; chs: [number, number][][]; dia: any; port: any }

/** Side-view mid-module explode + acoustic particles driven by the measured spiral path (mid_paths.json). */
function MidViz() {
  const box = React.useRef<HTMLDivElement>(null), cv = React.useRef<HTMLCanvasElement>(null)
  const { theme } = useApp()
  const tr = useT()
  const themeRef = React.useRef(theme); themeRef.current = theme
  const [labels, setLabels] = React.useState<{ d: [number, number]; s: [number, number]; p: [number, number] } | null>(null)

  React.useEffect(() => {
    let D: Paths | null = null, W = 0, H = 0, P: Paths["path"] = [], L: number[] = [], tot = 0, raf = 0, alive = true
    const x = cv.current!.getContext("2d")!
    const reduce = matchMedia("(prefers-reduced-motion: reduce)").matches
    const size = () => { const r = box.current!.getBoundingClientRect(), dpr = Math.min(2, devicePixelRatio || 1); W = r.width; H = r.height; cv.current!.width = W * dpr; cv.current!.height = H * dpr; x.setTransform(dpr, 0, 0, dpr, 0, 0) }
    const at = (s: number) => { let i = 1; while (i < L.length && L[i] < s) i++; if (i >= L.length) return P[P.length - 1]; const a = P[i - 1], b = P[i], k = (s - L[i - 1]) / (L[i] - L[i - 1] || 1); return [a[0] + (b[0] - a[0]) * k, a[1] + (b[1] - a[1]) * k, a[2] == null || b[2] == null ? null : a[2] + (b[2] - a[2]) * k, b[3]] as const }
    const rgb = () => themeRef.current === "light" ? "111,154,0" : themeRef.current === "rytho" ? "214,255,101" : "198,244,50"
    const hs = (a: number, b: number) => { const v = Math.sin(a * 127.1 + b * 311.7) * 43758.5453; return v - Math.floor(v) }
    const vis = () => { const r = box.current!.getBoundingClientRect(); return r.bottom > 0 && r.top < innerHeight }
    const f = (T: number) => {
      if (!alive) return; raf = requestAnimationFrame(f); if (!D || !vis()) return
      const t = reduce ? 2000 : T, c = rgb(), col = (a: number) => `rgba(${c},${a})`
      x.clearRect(0, 0, W, H)
      const d = D.dia, cx = d.x_rim * W, cy = d.centre[1] * H, R = (d.bottom_y - d.top_y) / 2 * H
      const pis = Math.sin(t / 1000 * 2 * Math.PI * 1.25) * 2.2
      x.strokeStyle = col(.55); x.lineWidth = .8; x.beginPath(); x.moveTo(cx + pis, cy - R); x.lineTo(cx + pis, cy + R); x.stroke()
      for (let k = 0; k < 6; k++) { const ph = (t / 1000 * .9 + k / 6) % 1, r = R * .9 + ph * cx * 1.05, A = (1 - ph) ** 2, n = Math.round(40 + r * .9)
        for (let i = 0; i < n; i++) { const u = i / (n - 1), ang = Math.PI - .7 + 1.4 * u, edge = Math.sin(u * Math.PI), rr = r + (hs(i, k) - .5) * 5 * (.4 + ph), a = A * edge * (.35 + .65 * hs(k, i)) * .85
          if (a < .02) continue; x.fillStyle = col(a); x.fillRect(cx + Math.cos(ang) * rr, cy + Math.sin(ang) * rr, 1.3, 1.3) } }
      for (const ch of D.chs) { x.beginPath(); ch.forEach((q, i) => i ? x.lineTo(q[0] * W, q[1] * H) : x.moveTo(q[0] * W, q[1] * H)); x.strokeStyle = col(.1); x.lineWidth = .6; x.stroke() }
      x.shadowColor = themeRef.current === "light" ? "transparent" : `rgba(${c},.8)`; x.shadowBlur = 5
      const N = 46, sp = tot / 5200
      for (let k = 0; k < N; k++) { const s = (t * sp + k * tot / N) % tot
        for (let j = 0; j < 10; j++) { const q = at(Math.max(0, s - j * 6)); if (!q) continue; let a = (1 - j / 10) * (q[3] === "ex" ? .25 : q[3] === "ou" ? .5 : .95); if (q[2] != null && q[2] < 0) a *= .35
          x.fillStyle = col(a); x.beginPath(); x.arc(q[0] * W, q[1] * H, j ? .9 : 1.8, 0, 6.283); x.fill() } }
      x.shadowBlur = 0
      const p = D.port, px = p.x_range[1] * W, py = .5 * H, PR = (p.y_outer_top_bottom[1] - p.y_outer_top_bottom[0]) / 2 * H
      for (let k = 0; k < 5; k++) { const ph = (t / 1000 * .6 + k / 5) % 1, r = PR * .6 + ph * Math.min(W - px, PR * 2.2), A = (1 - ph) ** 2, n = Math.round(30 + r * .7)
        for (let i = 0; i < n; i++) { const u = i / (n - 1), ang = -.55 + 1.1 * u, edge = Math.sin(u * Math.PI), rr = r + (hs(i, k + 9) - .5) * 5 * (.4 + ph), a = A * edge * (.35 + .65 * hs(k + 9, i)) * .75
          if (a < .02) continue; x.fillStyle = col(a); x.fillRect(px - PR * .6 + Math.cos(ang) * rr, py + Math.sin(ang) * rr, 1.3, 1.3) } }
    }
    fetch(IMG("mid_paths.json")).then((r) => r.json()).then((d: Paths) => {
      D = d; P = d.path; L = [0]
      for (let i = 1; i < P.length; i++) L.push(L[i - 1] + Math.hypot((P[i][0] - P[i - 1][0]) * 3200, (P[i][1] - P[i - 1][1]) * 1400))
      tot = L[L.length - 1]; size()
      const s = d.path.filter((q) => q[3] === "sp"), mid = s[Math.floor(s.length * .45)]
      setLabels({ d: [d.dia.x, d.dia.bottom_y + .07], s: [mid[0], d.port.y_outer_top_bottom[1] + .07], p: [d.port.x + .012, d.port.y_outer_top_bottom[0] - .12] })
      raf = requestAnimationFrame(f)
    }).catch(() => {})
    const ro = new ResizeObserver(() => D && size()); ro.observe(box.current!)
    return () => { alive = false; cancelAnimationFrame(raf); ro.disconnect() }
  }, [])

  const Lab = ({ at, t, s }: { at: [number, number]; t: string; s: string }) => (
    <span className="absolute -translate-x-1/2 text-center whitespace-nowrap" style={{ left: at[0] * 100 + "%", top: at[1] * 100 + "%" }}>
      <b className="block font-mono text-[10px] font-medium tracking-[.18em] text-primary">{t}</b>
      <em className="mt-1 block text-[11px] text-muted-foreground not-italic">{s}</em>
    </span>
  )
  return (
    <div ref={box} aria-hidden className="relative mx-auto aspect-[3200/1400] w-full max-w-[1500px]">
      <img src={IMG("mid_explode.webp")} width={3200} height={1400} alt="" className="absolute inset-0 size-full opacity-55 light:opacity-80 rytho:opacity-45" />
      <canvas ref={cv} className="absolute inset-0 size-full" />
      {labels && <div className="hidden md:block">
        <Lab at={labels.d} t="GLASS DIAPHRAGM" s={tr(UI.vizD)} />
        <Lab at={labels.s} t="SPIRAL = PORT LENGTH" s={tr(UI.vizS)} />
        <Lab at={labels.p} t="PORT" s={tr(UI.vizP)} />
      </div>}
    </div>
  )
}

export function Core() {
  const tr = useT()
  const text = tr(UI.coreLines), en = /^[A-Za-z]/.test(text)
  // CJK lights up per character, English per word
  const chars = en ? text.split(/(\s+)/).flatMap((w) => w.includes("\n") ? ["\n"] : [w]) : [...text]
  return (
    <section id="core" className="relative overflow-hidden py-28 md:py-40">
      <div className="mx-auto max-w-6xl px-6">
        <p className="font-mono text-[10px] tracking-[.24em] text-muted-foreground">01 / THE IDEA</p>
        <motion.h2 key={text} initial="h" whileInView="v" viewport={{ once: true, amount: .6 }} transition={{ staggerChildren: .045 }}
          className="mt-5 text-[clamp(30px,5vw,68px)] leading-[1.12] font-light tracking-tight">
          {chars.map((c, i) => c === "\n" ? <br key={i} /> : (
            <motion.span key={i} variants={{ h: { opacity: .12 }, v: { opacity: 1 } }} transition={{ duration: .5 }}>{c}</motion.span>
          ))}
        </motion.h2>
      </div>
      <div className="mt-16 px-4 md:mt-24"><MidViz /></div>
      <p className="mx-auto mt-10 max-w-md px-6 text-center text-sm text-muted-foreground">
        {tr(UI.coreCaption)}
        <span className="mt-2 block text-[11px] opacity-70">{tr(UI.coreNote)}</span>
      </p>
    </section>
  )
}
