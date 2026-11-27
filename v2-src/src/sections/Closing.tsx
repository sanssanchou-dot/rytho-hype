import * as React from "react"
import { motion } from "motion/react"
import { ArrowRight, Mic, MicOff } from "lucide-react"
import { VoiceBeam, useMicrophone } from "voice-glow"
import { ThinkingOrb } from "thinking-orbs"
import { BorderBeam } from "border-beam"
import { Glass } from "@/lib/glass"
import { PARTNERS, PARTNER_LINE, STEPS, UI } from "@/data"
import { Missing, useApp, useT } from "@/app-state"
import { Reveal } from "./Products"
import { cn } from "@/lib/utils"

/* Light colours per theme: green is the key light; RYTHO adds the purple fill light. */
const GLOW: Record<string, string[]> = {
  dark: ["#C6F432", "#B8EE2A", "#E6FFA8", "#9ED61C", "#D8FF7A", "#7FB800", "#F2FFD6"],
  rytho: ["#D6FF65", "#8C5CFF", "#8C5CFF", "#B8F23A", "#A98BFF", "#723CE8", "#E9FFB0"],
  light: ["#6F9A00", "#8FC000", "#5E8500", "#A8D41E", "#4E7300", "#B7DE3C", "#76A300"],
}

/* ---------------- AI: the glow listens to YOUR voice (mic only after a click) ---------------- */
export function AI() {
  const { theme } = useApp()
  const mic = useMicrophone()
  const tr = useT()
  const live = mic.state === "live"
  return (
    <section id="ai" className="relative py-28 md:py-40">
      <div className="mx-auto max-w-3xl px-6 text-center">
        <Reveal><p className="font-mono text-[10px] tracking-[.24em] text-muted-foreground">04 / HOME AI</p></Reveal>
        <Reveal delay={.05}><h2 className="mt-4 text-[clamp(34px,5vw,72px)] leading-[1.05] font-light tracking-tight">Now it listens<span className="text-key">.</span></h2></Reveal>
        <Reveal delay={.1}><p className="mt-5 text-sm text-muted-foreground">{tr(UI.aiP)}</p></Reveal>
      </div>

      <Reveal delay={.15} className="mx-auto mt-14 max-w-xl px-6">
        <VoiceBeam stream={mic.stream} colors={GLOW[theme]} theme={theme === "light" ? "light" : "dark"} staticColors sensitivity={2}>
          <Glass level={2} refract={false} className="flex items-center gap-5 rounded-[28px] px-6 py-6">
            <ThinkingOrb state={live ? "listening" : "breathing"} size={64} theme={theme === "light" ? "light" : "dark"} />
            <div className="min-w-0 flex-1 text-left">
              <p className="text-[15px]">{tr(live ? UI.aiListening : UI.aiTry)}</p>
              <p className="mt-1 text-xs text-muted-foreground">
                {tr(mic.state === "denied" ? UI.aiDenied : live ? UI.aiLive : UI.aiIdle)}
              </p>
            </div>
            <button onClick={live ? mic.stop : mic.start} aria-pressed={live} aria-label={tr(live ? UI.aiStop : UI.aiStart)}
              className={cn("grid size-11 shrink-0 place-items-center rounded-full transition-colors focus-visible:ring-2 focus-visible:ring-ring outline-none",
                live ? "text-primary ring-1 ring-primary/70" : "text-foreground ring-1 ring-foreground/20 hover:ring-foreground/40")}>
              {live ? <MicOff className="size-4" /> : <Mic className="size-4" />}
            </button>
          </Glass>
        </VoiceBeam>
        <Missing className="mt-6 justify-center">{tr(UI.aiMissing)}</Missing>
      </Reveal>
    </section>
  )
}

/* ---------------- Partner: four roles, then the path ---------------- */
export function Partner() {
  const tr = useT()
  return (
    <section id="partner" className="py-28 md:py-36">
      <div className="mx-auto max-w-6xl px-6">
        <Reveal><p className="font-mono text-[10px] tracking-[.24em] text-muted-foreground">05 / PARTNERSHIP</p></Reveal>
        <Reveal delay={.05}><h2 className="mt-4 text-[clamp(30px,4.4vw,60px)] leading-[1.1] font-light tracking-tight">Build it together<span className="text-key">.</span></h2></Reveal>

        <div className="mt-14 grid gap-3 sm:grid-cols-2 lg:grid-cols-4">
          {PARTNERS.map((p, i) => (
            <Reveal key={p.name} delay={i * .06}>
              <Glass level={3} className="hatch flex h-full flex-col rounded-[22px] p-6">
                <span className="font-mono text-[10px] tracking-[.2em] text-muted-foreground uppercase">{p.role}</span>
                <h3 className="mt-10 text-2xl font-light tracking-tight">{p.name}</h3>
                <p className="mt-3 text-[13px] leading-relaxed text-muted-foreground">{tr(p.d)}</p>
              </Glass>
            </Reveal>
          ))}
        </div>

        <ol className="relative mt-20 grid gap-8 md:grid-cols-4 md:gap-4">
          <span aria-hidden className="absolute top-[15px] right-0 left-0 hidden border-t border-dashed border-foreground/15 md:block" />
          {STEPS.map((s, i) => (
            <Reveal key={s.n} delay={i * .08}>
              <li className="relative">
                <span className={cn("relative grid size-[30px] place-items-center rounded-full bg-background font-mono text-[11px] ring-1",
                  i === 0 ? "text-primary ring-primary/70" : "text-muted-foreground ring-foreground/15")}>{s.n}</span>
                <h4 className="mt-5 text-[15px] font-medium">{tr(s.t)}</h4>
                <p className="mt-1.5 text-[13px] text-muted-foreground">{tr(s.d)}</p>
              </li>
            </Reveal>
          ))}
        </ol>
        <Missing className="mt-10">{tr(UI.partnerMissing)}</Missing>
      </div>
    </section>
  )
}

/* ---------------- CTA: the one place a beam of light travels ---------------- */
export function CTA() {
  const { theme } = useApp()
  const tr = useT()
  return (
    <section id="cta" className="grid min-h-[80svh] place-items-center px-6 py-28 text-center">
      <div>
        <Reveal><h2 className="text-[clamp(38px,6vw,92px)] leading-[1.02] font-light tracking-tight">Sound takes<br />shape<span className="text-key">.</span></h2></Reveal>
        <Reveal delay={.12} className="mt-12 inline-block">
          <BorderBeam size="md" colorVariant="forest" theme={theme === "light" ? "light" : "dark"} strength={.85} duration={3.2} hueRange={8}>
            <motion.a href="mailto:OPQstudio.com@gmail.com" whileHover={{ scale: 1.02 }} whileTap={{ scale: .98 }}
              className="flex h-14 items-center gap-4 rounded-full bg-background pr-2 pl-7 text-[15px] ring-1 ring-foreground/12 outline-none focus-visible:ring-2 focus-visible:ring-ring">
              {tr(UI.cta)}
              <span className="grid size-10 place-items-center rounded-full text-primary ring-1 ring-primary/70"><ArrowRight className="size-4" /></span>
            </motion.a>
          </BorderBeam>
        </Reveal>
        <p className="mt-16 font-mono text-[10px] tracking-[.24em] text-muted-foreground">{PARTNER_LINE}</p>
      </div>
    </section>
  )
}
