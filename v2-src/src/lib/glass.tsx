/* Liquid glass — edge-refraction displacement map (after rdev/liquid-glass-react).
   Vector distance transform of the shape -> outward normal × smoothstep bevel -> feDisplacementMap ×3 (RGB split).
   Chromium only (backdrop-filter:url()); others keep the plain blur from CSS. */
import * as React from "react"
import { cn } from "@/lib/utils"

const NS = "http://www.w3.org/2000/svg"
const chromium = typeof window !== "undefined" && !!(window as any).chrome && CSS.supports("backdrop-filter", "blur(1px)")
let host: SVGSVGElement | null = null
let uid = 0

function svgHost() {
  if (host) return host
  host = document.createElementNS(NS, "svg")
  host.setAttribute("width", "0"); host.setAttribute("height", "0")
  host.style.cssText = "position:absolute;width:0;height:0;pointer-events:none"
  document.body.appendChild(host)
  return host
}

function buildMap(W: number, H: number, r: number, B: number) {
  const w = W + 2, h = H + 2
  const c = document.createElement("canvas"); c.width = w; c.height = h
  const x = c.getContext("2d")!
  x.translate(1, 1); x.fillStyle = "#fff"; x.beginPath(); x.roundRect(0, 0, W, H, r); x.fill()
  const m = x.getImageData(0, 0, w, h).data, N = w * h
  const vx = new Float32Array(N), vy = new Float32Array(N), BIG = 1e6
  for (let i = 0; i < N; i++) if (m[i * 4 + 3] > 127) { vx[i] = BIG; vy[i] = BIG }
  const L = (i: number) => vx[i] * vx[i] + vy[i] * vy[i]
  const tr = (i: number, j: number, ox: number, oy: number) => { const ax = vx[j] + ox, ay = vy[j] + oy; if (ax * ax + ay * ay < L(i)) { vx[i] = ax; vy[i] = ay } }
  for (let y = 0; y < h; y++) {
    for (let X = 0; X < w; X++) { const i = y * w + X; if (X > 0) tr(i, i - 1, -1, 0); if (y > 0) { tr(i, i - w, 0, -1); if (X > 0) tr(i, i - w - 1, -1, -1); if (X < w - 1) tr(i, i - w + 1, 1, -1) } }
    for (let X = w - 2; X >= 0; X--) { const i = y * w + X; tr(i, i + 1, 1, 0) }
  }
  for (let y = h - 1; y >= 0; y--) {
    for (let X = w - 1; X >= 0; X--) { const i = y * w + X; if (X < w - 1) tr(i, i + 1, 1, 0); if (y < h - 1) { tr(i, i + w, 0, 1); if (X < w - 1) tr(i, i + w + 1, 1, 1); if (X > 0) tr(i, i + w - 1, -1, 1) } }
    for (let X = 1; X < w; X++) { const i = y * w + X; tr(i, i - 1, -1, 0) }
  }
  const o = document.createElement("canvas"); o.width = W; o.height = H
  const ox = o.getContext("2d")!, od = ox.createImageData(W, H), d = od.data
  for (let y = 0; y < H; y++) for (let X = 0; X < W; X++) {
    const i = (y + 1) * w + X + 1, p = (y * W + X) * 4; let rr = .5, g = .5
    if (m[i * 4 + 3] > 127) { const D = Math.sqrt(L(i)); if (D < B && D > 0) { const t = 1 - D / B, mag = t * t * (3 - 2 * t) * .5; rr = .5 + vx[i] / D * mag; g = .5 + vy[i] / D * mag } }
    d[p] = rr * 255; d[p + 1] = g * 255; d[p + 2] = 128; d[p + 3] = 255
  }
  ox.putImageData(od, 0, 0)
  const s = document.createElement("canvas"); s.width = W; s.height = H
  const sx = s.getContext("2d")!; sx.filter = "blur(1.2px)"; sx.drawImage(o, 0, 0)
  return s.toDataURL()
}

function makeFilter(W: number, H: number, url: string, S: number) {
  const id = "lgf" + (++uid)
  const f = document.createElementNS(NS, "filter")
  f.id = id
  for (const [k, v] of [["x", "0"], ["y", "0"], ["width", String(W)], ["height", String(H)], ["filterUnits", "userSpaceOnUse"], ["primitiveUnits", "userSpaceOnUse"], ["color-interpolation-filters", "sRGB"]]) f.setAttribute(k, v)
  const ch = (k: string, s: number, mat: string) => `<feDisplacementMap in="SourceGraphic" in2="map" scale="${s}" xChannelSelector="R" yChannelSelector="G" result="d${k}"/><feColorMatrix in="d${k}" type="matrix" values="${mat}" result="c${k}"/>`
  f.innerHTML = `<feImage href="${url}" x="0" y="0" width="${W}" height="${H}" preserveAspectRatio="none" result="map"/>` +
    ch("r", S, "1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0") + ch("g", S * .93, "0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 1 0") + ch("b", S * .86, "0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 1 0") +
    `<feBlend in="cr" in2="cg" mode="screen" result="rg"/><feBlend in="rg" in2="cb" mode="screen"/>`
  svgHost().appendChild(f)
  return f
}

/** Attach refraction to the .lg-b layer of a glass host; rebuilds on resize. */
function useRefraction(ref: React.RefObject<HTMLElement | null>, blur: number) {
  React.useEffect(() => {
    const el = ref.current; if (!el || !chromium) return
    const b = el.querySelector<HTMLElement>(":scope > .lg-b"); if (!b) return
    let f: SVGFilterElement | null = null, key = "", t = 0
    const run = () => {
      const W = Math.round(el.offsetWidth), H = Math.round(el.offsetHeight); if (W < 4 || H < 4) return
      const k = W + "x" + H; if (k === key) return; key = k
      const r = Math.min(parseFloat(getComputedStyle(el).borderTopRightRadius) || 0, W / 2, H / 2)
      const B = Math.min(18, Math.min(W, H) * .42)
      f?.remove(); f = makeFilter(W, H, buildMap(W, H, r, B), -B * 1.6)
      b.style.backdropFilter = `blur(${blur}px) url(#${f.id}) saturate(165%) brightness(1.04)`
    }
    const ro = new ResizeObserver(() => { clearTimeout(t); t = window.setTimeout(run, 60) })
    ro.observe(el); run()
    return () => { ro.disconnect(); clearTimeout(t); f?.remove() }
  }, [ref, blur])
}

const NO_REF: React.RefObject<HTMLElement | null> = { current: null }

type GlassProps =React.HTMLAttributes<HTMLElement> & {
  as?: React.ElementType
  level?: 1 | 2 | 3
  /** refraction is costly; cards (level 3) use plain frosted blur */
  refract?: boolean
}

export const Glass = React.forwardRef<HTMLElement, GlassProps>(function Glass(
  { as: Tag = "div", level = 2, refract, className, children, ...rest }, fwd) {
  const ref = React.useRef<HTMLElement | null>(null)
  React.useImperativeHandle(fwd, () => ref.current as HTMLElement)
  useRefraction((refract ?? level < 3) ? ref : NO_REF, level === 1 ? 3 : 2)
  return (
    <Tag ref={ref} data-level={level} className={cn("lg", className)} {...rest}>
      <span className="lg-b" aria-hidden />
      {children}
      <span className="lg-t" aria-hidden />
    </Tag>
  )
})

/** Breathing light: the key light circles on its own (never tied to scroll). */
export function useBreathingLight() {
  React.useEffect(() => {
    const st = document.documentElement.style
    if (matchMedia("(prefers-reduced-motion: reduce)").matches) { st.setProperty("--la", "-45deg"); return }
    let raf = 0; const t0 = performance.now()
    const f = (T: number) => {
      const s = (T - t0) / 1000
      st.setProperty("--la", (-45 + 80 * Math.sin(s * 2 * Math.PI / 9) + 25 * Math.sin(s * 2 * Math.PI / 23)).toFixed(2) + "deg")
      st.setProperty("--lb", (.5 + .5 * Math.sin(s * 2 * Math.PI / 6)).toFixed(3))
      raf = requestAnimationFrame(f)
    }
    raf = requestAnimationFrame(f)
    return () => cancelAnimationFrame(raf)
  }, [])
}
