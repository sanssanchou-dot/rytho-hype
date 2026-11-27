import * as React from "react"
import { animate, motion, AnimatePresence } from "motion/react"
import { Plus, Minus } from "lucide-react"
import { Glass } from "@/lib/glass"
import { EXPLODE_LABELS, IMG, UI } from "@/data"
import { useT } from "@/app-state"
import { cn } from "@/lib/utils"

const FR = 72, LAB_X = .8
const frame = (i: number) => IMG(`explode/explode_${String(i + 1).padStart(4, "0")}.webp`)

/** Click to explode (no scroll binding). Standard: the mids separate; woofers move only slightly. */
export function Explode() {
  const cv = React.useRef<HTMLCanvasElement>(null)
  const frames = React.useRef<HTMLImageElement[]>([])
  const [open, setOpen] = React.useState(false)
  const [p, setP] = React.useState(0)
  const [ready, setReady] = React.useState(false)
  const tr = useT()

  const draw = React.useCallback((q: number) => {
    const c = cv.current; if (!c) return
    const im = frames.current[Math.round(q * (FR - 1))]
    if (!im?.complete || !im.naturalWidth) return
    const x = c.getContext("2d")!
    if (c.width !== im.naturalWidth) { c.width = im.naturalWidth; c.height = im.naturalHeight }
    x.clearRect(0, 0, c.width, c.height); x.drawImage(im, 0, 0)
  }, [])

  React.useEffect(() => {
    const first = new Image(); first.src = frame(0)
    first.onload = () => { frames.current[0] = first; draw(0); setReady(true) }
    // preload the rest once the section is near
    const io = new IntersectionObserver(([e]) => {
      if (!e.isIntersecting) return; io.disconnect()
      for (let i = 1; i < FR; i++) { const im = new Image(); im.src = frame(i); frames.current[i] = im }
    }, { rootMargin: "600px" })
    io.observe(cv.current!)
    return () => io.disconnect()
  }, [draw])

  const run = React.useRef<{ stop: () => void } | null>(null), cur = React.useRef(0)
  const toggle = () => {
    const to = open ? 0 : 1; setOpen(!open); run.current?.stop()
    run.current = animate(cur.current, to, { duration: 1.8 * Math.abs(to - cur.current), ease: [.65, 0, .35, 1], onUpdate: (v) => { cur.current = v; setP(v); draw(v) } })
  }

  const showLabs = p > .62
  return (
    <section id="explode" className="relative flex min-h-[100svh] flex-col justify-center py-24">
      <div className="mx-auto flex w-full max-w-6xl items-end justify-between gap-6 px-6">
        <div>
          <p className="font-mono text-[10px] tracking-[.24em] text-muted-foreground">02 / EXPLODED</p>
          <h2 className="mt-4 text-[clamp(28px,3.6vw,48px)] leading-tight font-light tracking-tight">{tr(UI.explodeH)}</h2>
        </div>
        <span className="font-mono text-xs text-muted-foreground tabular-nums">{String(Math.round(p * 100)).padStart(3, "0")}</span>
      </div>

      <div className="relative mx-auto mt-8 aspect-video w-full max-w-[min(1600px,calc(78svh*16/9))]">
        <canvas ref={cv} className={cn("absolute inset-0 size-full transition-opacity duration-700", ready ? "opacity-100" : "opacity-0")} />
        <div className="absolute inset-0 hidden md:block">
          <AnimatePresence>
            {showLabs && EXPLODE_LABELS.map((l, i) => (
              <motion.div key={l.t} className="absolute flex items-center gap-3" style={{ left: LAB_X * 100 + "%", top: l.y * 100 + "%" }}
                initial={{ opacity: 0, x: -8 }} animate={{ opacity: 1, x: 0 }} exit={{ opacity: 0, transition: { duration: .15 } }}
                transition={{ delay: i * .06, duration: .45, ease: [.22, 1, .36, 1] }}>
                <span className="h-px w-8 bg-gradient-to-r from-transparent to-foreground/40" />
                <span className="-translate-y-1/2 pt-[0.6em]">
                  <b className={cn("block font-mono text-[11px] font-medium tracking-[.16em]", l.hero ? "text-primary" : "text-foreground")}>{l.t}</b>
                  <span className="mt-1 block text-xs text-muted-foreground">{tr(l.s)}</span>
                </span>
              </motion.div>
            ))}
          </AnimatePresence>
        </div>
      </div>

      <div className="mt-8 flex justify-center">
        <Glass as="button" level={2} onClick={toggle} aria-pressed={open}
          className="lit flex h-11 items-center gap-3 rounded-full pr-1.5 pl-5 text-sm font-medium">
          {tr(open ? UI.assemble : UI.explode)}
          <span className="grid size-8 place-items-center rounded-full text-primary ring-1 ring-primary/70">
            {open ? <Minus className="size-3.5" /> : <Plus className="size-3.5" />}
          </span>
        </Glass>
      </div>

      <ul className="mx-auto mt-8 grid w-full max-w-md gap-3 px-6 md:hidden">
        {EXPLODE_LABELS.map((l) => (
          <li key={l.t} className="flex items-baseline justify-between gap-4 border-b border-border pb-3">
            <b className={cn("font-mono text-[11px] font-medium tracking-[.14em]", l.hero ? "text-primary" : "")}>{l.t}</b>
            <span className="text-right text-xs text-muted-foreground">{tr(l.s)}</span>
          </li>
        ))}
      </ul>
    </section>
  )
}
