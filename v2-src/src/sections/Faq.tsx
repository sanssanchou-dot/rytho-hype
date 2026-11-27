import { Plus } from "lucide-react"
import { FAQ } from "@/data"
import { Reveal } from "./Products"

/** Plain <details>: readable with no JS (crawlers), keyboard-accessible, no extra deps. */
export function Faq() {
  return (
    <section id="faq" className="py-24 md:py-32">
      <div className="mx-auto max-w-3xl px-6">
        <Reveal><p className="font-mono text-[10px] tracking-[.24em] text-muted-foreground">06 / FAQ</p></Reveal>
        <Reveal delay={.05}><h2 className="mt-4 text-[clamp(28px,3.6vw,48px)] leading-tight font-light tracking-tight">常見問題<span className="text-key">.</span></h2></Reveal>
        <div className="mt-10 border-t border-border">
          {FAQ.map((f) => (
            <details key={f.q} className="group border-b border-border">
              <summary className="flex cursor-pointer list-none items-center justify-between gap-6 py-5 text-[15px] outline-none focus-visible:text-primary [&::-webkit-details-marker]:hidden">
                <h3 className="font-normal">{f.q}</h3>
                <Plus className="size-4 shrink-0 text-muted-foreground transition-transform duration-300 group-open:rotate-45" />
              </summary>
              <p className="pb-6 text-sm leading-relaxed text-muted-foreground">{f.a}</p>
            </details>
          ))}
        </div>
      </div>
    </section>
  )
}
