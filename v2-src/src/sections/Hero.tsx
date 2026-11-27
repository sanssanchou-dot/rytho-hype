import * as React from "react"
import { motion } from "motion/react"
import { Glass } from "@/lib/glass"
import { IMG, UI } from "@/data"
import { cn } from "@/lib/utils"
import { useApp, useT } from "@/app-state"

const XF = 1.2 // seconds of picture + sound cross-fade at the loop point

/** One continuous film: two players cross-fade at the loop (no seam). Sound is opt-in and fades with hero visibility. */
export function Hero() {
  const A = React.useRef<HTMLVideoElement>(null), B = React.useRef<HTMLVideoElement>(null), sec = React.useRef<HTMLElement>(null)
  const [onA, setOnA] = React.useState(true)
  const [sound, setSound] = React.useState(false)
  const { theme } = useApp()
  const tr = useT()
  const st = React.useRef({ cur: 0, xf: 0, t0: 0, sound: false })

  React.useEffect(() => {
    const v = [A.current!, B.current!]; let raf = 0
    v[0].play().catch(() => {})
    const vis = () => { const r = sec.current!.getBoundingClientRect(); return Math.max(0, Math.min(1, (r.bottom - innerHeight * .15) / (innerHeight * .85))) }
    const tick = () => {
      const s = st.current, cur = v[s.cur], nxt = v[1 - s.cur]
      if (!s.xf && cur.duration && cur.currentTime > cur.duration - XF) {
        s.xf = 1; s.t0 = performance.now(); nxt.currentTime = 0; nxt.muted = !s.sound; nxt.volume = 0; nxt.play().catch(() => {})
        setOnA(s.cur === 1)
        setTimeout(() => { cur.pause(); s.cur = 1 - s.cur; s.xf = 0 }, XF * 1000 + 80)
      }
      const g = s.sound ? vis() : 0, k = s.xf ? Math.min(1, (performance.now() - s.t0) / (XF * 1000)) : 1
      cur.volume = Math.max(0, Math.min(1, g * (s.xf ? 1 - k : 1))); nxt.volume = Math.max(0, Math.min(1, g * (s.xf ? k : 0)))
      raf = requestAnimationFrame(tick)
    }
    raf = requestAnimationFrame(tick)
    return () => cancelAnimationFrame(raf)
  }, [])

  const toggle = () => {
    const s = st.current; s.sound = !s.sound; setSound(s.sound)
    const v = [A.current!, B.current!]; v[s.cur].muted = !s.sound; v[1 - s.cur].muted = !s.sound || !s.xf
    if (s.sound && v[s.cur].paused) v[s.cur].play().catch(() => {})
  }

  return (
    <>
    <section id="film" ref={sec} className={cn("relative grid h-[100svh] min-h-[640px] place-items-center overflow-hidden", theme === "light" && "dark bg-[#08080a] text-foreground")}>
      <div className="fade-x relative h-full aspect-[9/16] max-w-full">
        <video ref={A} className={cn("absolute inset-0 size-full object-cover transition-opacity duration-[1200ms] ease-linear", onA ? "opacity-100" : "opacity-0")}
          src={IMG("hero_v3.mp4")} poster={IMG("hero_v3_poster.jpg")} autoPlay muted playsInline preload="auto" />
        <video ref={B} className={cn("absolute inset-0 size-full object-cover transition-opacity duration-[1200ms] ease-linear", onA ? "opacity-0" : "opacity-100")}
          src={IMG("hero_v3.mp4")} muted playsInline preload="auto" />
      </div>
      <div className="pointer-events-none absolute inset-0 bg-[linear-gradient(180deg,transparent_70%,var(--background))]" />

      <motion.div initial={{ opacity: 0, y: 14 }} animate={{ opacity: 1, y: 0 }} transition={{ delay: .4, duration: .9, ease: [.22, 1, .36, 1] }}
        className="absolute bottom-10 left-6 max-w-[17rem] md:bottom-16 md:left-12">
        <p className="font-mono text-[10px] tracking-[.24em] text-muted-foreground">{tr(UI.heroEyebrow)}</p>
        <h1 className="mt-3 text-[26px] leading-[1.15] font-light tracking-tight md:text-[32px]">{tr(UI.heroH1).split("\n").map((l, i) => <React.Fragment key={i}>{i > 0 && <br />}{l}</React.Fragment>)}<span className="text-key">.</span></h1>
      </motion.div>

      <Glass as="button" level={2} onClick={toggle} aria-pressed={sound} aria-label={sound ? "Sound off" : "Sound on"}
        className={cn("absolute right-6 bottom-10 flex h-10 items-center gap-2.5 rounded-full pr-4 pl-3.5 text-[11px] font-semibold tracking-[.12em] md:right-12 md:bottom-16", sound ? "text-primary" : "text-muted-foreground")}>
        <span className="flex h-3.5 items-end gap-[2px]">
          {[0, .3, .6, .15].map((d, i) => (
            <motion.i key={i} className="block w-[2px] rounded-full bg-current" style={{ height: 3 }}
              animate={sound ? { height: [3, 14, 3] } : { height: 3 }} transition={sound ? { repeat: Infinity, duration: 1, delay: d, ease: "easeInOut" } : { duration: .3 }} />
          ))}
        </span>
        {sound ? "SOUND ON" : "SOUND"}
      </Glass>
    </section>
    {theme === "light" && <div aria-hidden className="h-32 bg-[linear-gradient(180deg,#08080a,var(--background))]" />}
    </>
  )
}
