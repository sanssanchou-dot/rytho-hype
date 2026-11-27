import * as React from "react"
import { AnimatePresence, motion } from "motion/react"
import { ArrowRight, Wifi, Bluetooth, Sparkles } from "lucide-react"
import { Glass } from "@/lib/glass"
import { BODIES, IMG, PRODUCTS, type BodyKey, type ProductId } from "@/data"
import { Missing, useApp } from "@/app-state"
import { Segmented, SPRING } from "./Nav"
import { HoverCard, HoverCardContent, HoverCardTrigger } from "@/components/ui/hover-card"
import { Tooltip, TooltipContent, TooltipTrigger } from "@/components/ui/tooltip"
import { Badge } from "@/components/ui/badge"
import { cn } from "@/lib/utils"

const EASE = [.22, 1, .36, 1] as const
export const Reveal = ({ children, className, delay = 0 }: { children: React.ReactNode; className?: string; delay?: number }) => (
  <motion.div className={className} initial={{ opacity: 0, y: 18 }} whileInView={{ opacity: 1, y: 0 }} viewport={{ once: true, amount: .25 }} transition={{ duration: .8, delay, ease: EASE }}>{children}</motion.div>
)
const TALLEST = 2693

function goProduct(setProduct: (p: ProductId) => void, id: ProductId) {
  setProduct(id); history.replaceState(null, "", "#" + id)
  document.getElementById("products")?.scrollIntoView({ behavior: "smooth" })
}

/* ---------------- Family: the whole line-up at true scale; hover = scene, click = open in explorer ---------------- */
export function Family() {
  const { setProduct } = useApp()
  return (
    <section id="family" className="py-28 md:py-36">
      <div className="mx-auto max-w-6xl px-6">
        <Reveal><p className="font-mono text-[10px] tracking-[.24em] text-muted-foreground">03 / ONE PAIR · FOUR PRODUCTS</p></Reveal>
        <Reveal delay={.05}><h2 className="mt-4 text-[clamp(30px,4.4vw,60px)] leading-[1.1] font-light tracking-tight">一座塔，拆成四個產品<span className="text-key">.</span></h2></Reveal>
        <Reveal delay={.1}><p className="mt-5 max-w-lg text-sm leading-relaxed text-muted-foreground">由小到大：從一顆透明模組的隨身音響，到整組可訂製的高訂。02 起內建 Wi-Fi 與 AI。</p></Reveal>
      </div>
      <Reveal className="stage mx-auto mt-12 max-w-[1500px] light:mx-6 xl:light:mx-auto">
        <picture><source media="(max-width:900px)" srcSet={IMG("family_port.webp")} />
          <img src={IMG("family.webp")} width={2560} height={1440} alt="RYTHO HYPE family at true scale" className="soft-edge w-full" /></picture>
      </Reveal>
      <div className="mx-auto mt-10 grid max-w-6xl grid-cols-2 gap-3 px-6 md:grid-cols-4">
        {PRODUCTS.map((p, i) => (
          <HoverCard key={p.id} openDelay={120} closeDelay={60}>
            <HoverCardTrigger asChild>
              <motion.button onClick={() => goProduct(setProduct, p.id)} whileHover={{ y: -3 }} whileTap={{ scale: .98 }} transition={SPRING}
                initial={{ opacity: 0, y: 18 }} whileInView={{ opacity: 1, y: 0 }} viewport={{ once: true }}
                className="group text-left outline-none focus-visible:ring-2 focus-visible:ring-ring rounded-2xl" style={{ transitionDelay: i * 60 + "ms" }}>
                <Glass level={3} className="flex h-full flex-col rounded-2xl p-3">
                  <div className="aspect-[3/2] overflow-hidden rounded-xl"><img src={IMG(p.closeup)} alt="" loading="lazy" className="stage-img transition-transform duration-700 group-hover:scale-[1.03]" /></div>
                  <div className="mt-3 flex items-baseline gap-2 px-1"><span className="font-mono text-[11px] text-muted-foreground">{p.n}</span><span className="text-[15px] font-medium">{p.zh}</span></div>
                  <div className="mt-1 flex items-center justify-between px-1 text-[11px] text-muted-foreground">
                    <span>{p.ai ? "Wi-Fi · AI" : "Bluetooth"}</span><span className="font-mono">{p.heightLabel.replace(" ×2", "")}</span>
                  </div>
                  <ScaleBar mm={p.heightMm} className="mx-1 mt-3" />
                </Glass>
              </motion.button>
            </HoverCardTrigger>
            <HoverCardContent side="top" sideOffset={12} className="w-[380px] overflow-hidden rounded-2xl p-0">
              <img src={IMG(p.scene)} width={2560} height={1440} alt="" className="block w-full" />
              <div className="flex items-center justify-between px-4 py-3 text-xs"><span>{p.n} {p.zh} · 情境</span><span className="flex items-center gap-1 text-muted-foreground">查看 <ArrowRight className="size-3" /></span></div>
            </HoverCardContent>
          </HoverCard>
        ))}
      </div>
    </section>
  )
}

/** true-height share vs the full tower (data, so it may use the primary) */
function ScaleBar({ mm, className }: { mm: number; className?: string }) {
  const w = Math.max(3, mm / TALLEST * 100)
  return (
    <div className={cn("relative h-1 rounded-full bg-foreground/8", className)} title={`${Math.round(w)}% of full tower height`}>
      <motion.span className="absolute inset-y-0 left-0 rounded-full bg-primary/80" initial={{ width: 0 }} whileInView={{ width: w + "%" }} viewport={{ once: true }} transition={{ duration: 1.1, ease: EASE, delay: .2 }} />
    </div>
  )
}

/* ---------------- Products: one explorer instead of four long pages ---------------- */
export function Products() {
  const { product, setProduct } = useApp()
  const p = PRODUCTS.find((x) => x.id === product)!
  const [body, setBody] = React.useState<BodyKey>("orig")
  const [sw, setSw] = React.useState(0)
  const b = BODIES[body]
  const hero = p.id === "p04" ? b.c[Math.min(sw, b.c.length - 1)].img : p.closeup
  React.useEffect(() => {
    const on = () => { const h = location.hash.slice(1); if (PRODUCTS.some((x) => x.id === h)) setProduct(h as ProductId) }
    addEventListener("hashchange", on); return () => removeEventListener("hashchange", on)
  }, [setProduct])

  return (
    <section id="products" className="relative py-16 md:py-20">
      <div className="sticky top-20 z-30 flex justify-center px-4">
        <Segmented id="prod" value={product} onChange={(v) => { setProduct(v); history.replaceState(null, "", "#" + v) }}
          items={PRODUCTS.map((x) => ({ v: x.id, label: <span className="flex items-center gap-1.5"><span className="font-mono opacity-60">{x.n}</span><span className="hidden sm:inline">{x.zh}</span></span> }))} />
      </div>

      <div className="mx-auto mt-10 grid max-w-7xl items-center gap-10 px-6 lg:grid-cols-[1.35fr_1fr] lg:gap-16">
        <div className={cn("relative grid place-items-center", p.id === "p04"
          ? "mx-auto aspect-[3/4] h-[min(78svh,820px)] max-w-full overflow-hidden rounded-[28px] bg-white shadow-lg"
          : "stage aspect-[3/2] lg:aspect-auto lg:h-[min(70svh,720px)]")}>
          <AnimatePresence mode="popLayout" initial={false}>
            <motion.img key={hero} src={IMG(hero)} alt={p.zh} className={cn("stage-img absolute inset-0", p.id !== "p04" && "soft-edge")}
              initial={{ opacity: 0, scale: .985, filter: "blur(6px)" }} animate={{ opacity: 1, scale: 1, filter: "blur(0px)" }} exit={{ opacity: 0, filter: "blur(6px)" }}
              transition={{ duration: .6, ease: EASE }} />
          </AnimatePresence>
        </div>

        <AnimatePresence mode="wait" initial={false}>
          <motion.div key={p.id} initial={{ opacity: 0, y: 10 }} animate={{ opacity: 1, y: 0 }} exit={{ opacity: 0, y: -6 }} transition={{ duration: .4, ease: EASE }}>
            <div className="flex items-baseline gap-3"><span className="font-mono text-sm text-muted-foreground">{p.n}</span><span className="font-mono text-[10px] tracking-[.22em] text-muted-foreground uppercase">{p.en}</span></div>
            <h3 className="mt-3 text-[clamp(36px,4vw,56px)] leading-none font-light tracking-tight">{p.zh}</h3>
            <p className="mt-4 text-[15px] text-muted-foreground">{p.line}</p>
            <div className="mt-5 flex flex-wrap gap-1.5">
              {p.ai && <Badge variant="outline" className="gap-1 rounded-full"><Wifi className="size-3" />Wi-Fi</Badge>}
              {p.ai && <Badge variant="outline" className="gap-1 rounded-full"><Sparkles className="size-3" />AI</Badge>}
              {p.id !== "p04" && <Badge variant="outline" className="gap-1 rounded-full"><Bluetooth className="size-3" />Bluetooth</Badge>}
              <Badge variant="outline" className="rounded-full font-mono">{p.heightLabel}</Badge>
            </div>

            {p.id === "p04" && (
              <div className="mt-8">
                <p className="mb-3 text-[11px] tracking-[.18em] text-muted-foreground">BODY</p>
                <Segmented id="body" value={body} onChange={(v) => { setBody(v); setSw(0) }} items={(Object.keys(BODIES) as BodyKey[]).map((k) => ({ v: k, label: BODIES[k].label }))} />
                {b.c.length > 1 && (
                  <div className="mt-4 flex flex-wrap gap-2">
                    {b.c.map((c, i) => (
                      <Tooltip key={c.img}>
                        <TooltipTrigger asChild>
                          <button onClick={() => setSw(i)} aria-label={c.name} aria-pressed={sw === i}
                            className={cn("size-8 rounded-full ring-offset-2 ring-offset-background transition-shadow", sw === i ? "ring-2 ring-foreground" : "ring-1 ring-foreground/15 hover:ring-foreground/40")}
                            style={{ background: c.sw }} />
                        </TooltipTrigger>
                        <TooltipContent>{c.name}</TooltipContent>
                      </Tooltip>
                    ))}
                  </div>
                )}
                <p className="mt-3 text-xs text-muted-foreground">{b.note}</p>
              </div>
            )}

            <dl className="mt-8 grid grid-cols-1 gap-2 sm:grid-cols-3 lg:grid-cols-1 xl:grid-cols-3">
              {p.facts.map((f) => (
                <Glass key={f.k} level={3} className="rounded-xl px-4 py-3">
                  <dt className="text-[11px] text-muted-foreground">{f.k}</dt>
                  <dd className="mt-1.5 text-[13px] leading-snug">{f.v}</dd>
                </Glass>
              ))}
            </dl>
            {p.missing && <Missing className="mt-5">{p.missing}</Missing>}
          </motion.div>
        </AnimatePresence>
      </div>

      <div className="mx-auto mt-16 max-w-7xl px-6">
        <div className="stage relative aspect-video bg-[#0b0b0e]">
          <AnimatePresence initial={false}>
            <motion.img key={p.scene} src={IMG(p.scene)} width={2560} height={1440} alt="" loading="lazy" className="absolute inset-0 size-full object-cover"
              initial={{ opacity: 0 }} animate={{ opacity: 1 }} exit={{ opacity: 0 }} transition={{ duration: .7 }} />
          </AnimatePresence>
          <span className="absolute bottom-4 left-5 font-mono text-[10px] tracking-[.22em] text-white/70">{p.n} · IN SPACE</span>
        </div>
      </div>
    </section>
  )
}
