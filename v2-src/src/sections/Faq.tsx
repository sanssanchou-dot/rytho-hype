import { Plus } from "lucide-react"
import { FAQ, FAQ_EN, SUMMARY_EN } from "@/data"
import { Reveal } from "./Products"

/** Plain <details>: readable with no JS (crawlers), keyboard-accessible, no extra deps. */
function List({ items }: { items: { q: string; a: string }[] }) {
  return (
    <div className="mt-8 border-t border-border">
      {items.map((f) => (
        <details key={f.q} className="group border-b border-border">
          <summary className="flex cursor-pointer list-none items-center justify-between gap-6 py-5 text-[15px] outline-none focus-visible:text-primary [&::-webkit-details-marker]:hidden">
            <h3 className="font-normal">{f.q}</h3>
            <Plus className="size-4 shrink-0 text-muted-foreground transition-transform duration-300 group-open:rotate-45" />
          </summary>
          <p className="pb-6 text-sm leading-relaxed text-muted-foreground">{f.a}</p>
        </details>
      ))}
    </div>
  )
}

export function Faq() {
  return (
    <section id="faq" className="py-24 md:py-32">
      <div className="mx-auto max-w-3xl px-6">
        <Reveal><p className="font-mono text-[10px] tracking-[.24em] text-muted-foreground">06 / FAQ</p></Reveal>
        <Reveal delay={.05}><h2 className="mt-4 text-[clamp(28px,3.6vw,48px)] leading-tight font-light tracking-tight">常見問題<span className="text-key">.</span></h2></Reveal>
        <List items={FAQ} />
        <div lang="en" className="mt-20">
          <h2 className="text-[clamp(22px,2.6vw,32px)] font-light tracking-tight">In English<span className="text-key">.</span></h2>
          <p className="mt-4 text-sm leading-relaxed text-muted-foreground">{SUMMARY_EN}</p>
          <List items={FAQ_EN} />
        </div>
      </div>
    </section>
  )
}
