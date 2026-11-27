import * as React from "react"
import { motion } from "motion/react"
import { Menu } from "lucide-react"
import { Glass } from "@/lib/glass"
import { LANG_LABELS as LANGS, SECTIONS, UI } from "@/data"
import { useApp, useT, type Theme } from "@/app-state"
import { Switch } from "@/components/ui/switch"
import { Tooltip, TooltipContent, TooltipTrigger } from "@/components/ui/tooltip"
import { Sheet, SheetContent, SheetHeader, SheetTitle, SheetTrigger } from "@/components/ui/sheet"
import { cn } from "@/lib/utils"

export const SPRING = { type: "spring", stiffness: 420, damping: 34, mass: .7 } as const

function useScrollSpy(ids: readonly string[]) {
  const [active, setActive] = React.useState(ids[0])
  React.useEffect(() => {
    const io = new IntersectionObserver((es) => {
      for (const e of es) if (e.isIntersecting) setActive(e.target.id)
    }, { rootMargin: "-45% 0px -50% 0px" })
    ids.forEach((id) => { const el = document.getElementById(id); if (el) io.observe(el) })
    return () => io.disconnect()
  }, [ids])
  return active
}

/** One segmented-control spec for the whole site: 36px glass track, sliding pill (shared layout). */
export function Segmented<T extends string>({ value, onChange, items, id, size = "md", className }: {
  value: T; onChange: (v: T) => void; items: { v: T; label: React.ReactNode }[]; id: string; size?: "sm" | "md"; className?: string
}) {
  return (
    <Glass level={2} role="radiogroup" className={cn("inline-flex items-center rounded-full p-1", className)}>
      <div className="flex items-center">
        {items.map((it) => {
          const on = it.v === value
          return (
            <button key={it.v} role="radio" aria-checked={on} onClick={() => onChange(it.v)}
              className={cn("relative rounded-full font-medium tracking-wide transition-colors outline-none focus-visible:ring-2 focus-visible:ring-ring",
                size === "sm" ? "h-7 px-3 text-[11px]" : "h-8 px-4 text-xs",
                on ? "text-background" : "text-muted-foreground hover:text-foreground")}>
              {on && <motion.span layoutId={"seg-" + id} transition={SPRING} className="absolute inset-0 rounded-full bg-foreground shadow-sm" />}
              <span className="relative">{it.label}</span>
            </button>
          )
        })}
      </div>
    </Glass>
  )
}

const THEMES: { v: Theme; label: string }[] = [{ v: "dark", label: "DARK" }, { v: "rytho", label: "RYTHO" }, { v: "light", label: "LIGHT" }]

export function Nav() {
  const { theme, setTheme, lang, setLang, notes, setNotes } = useApp()
  const tr = useT()
  const active = useScrollSpy(SECTIONS.map((s) => s.id))
  const [open, setOpen] = React.useState(false)
  return (
    <header className="pointer-events-none fixed inset-x-0 top-4 z-50 flex justify-center px-4">
      <Glass level={1} as="nav" aria-label="Sections" className="pointer-events-auto flex h-12 w-full max-w-5xl items-center gap-2 rounded-full pr-1.5 pl-5 light:bg-background/70">
        <a href="#film" className="flex items-center gap-2 text-[13px] font-semibold tracking-[.14em]">
          <span className="size-1.5 rounded-full bg-key shadow-[0_0_10px_var(--key)]" />RYTHO HYPE
        </a>
        <ul className="mx-auto hidden items-center lg:flex">
          {SECTIONS.map((s) => (
            <li key={s.id}>
              <a href={"#" + s.id} className={cn("relative block rounded-full px-3 py-1.5 text-xs transition-colors", active === s.id ? "text-foreground" : "text-muted-foreground hover:text-foreground")}>
                {active === s.id && <motion.span layoutId="nav-pill" transition={SPRING} className="absolute inset-0 rounded-full bg-foreground/8 ring-1 ring-foreground/10" />}
                <span className="relative">{s.t}</span>
              </a>
            </li>
          ))}
        </ul>
        <div className="ml-auto hidden items-center gap-3 md:flex lg:ml-0">
          <Tooltip>
            <TooltipTrigger asChild>
              <label className="flex cursor-pointer items-center gap-2 text-[11px] text-muted-foreground">
                <Switch checked={notes} onCheckedChange={setNotes} aria-label={tr(UI.notesLong)} />{tr(UI.notes)}
              </label>
            </TooltipTrigger>
            <TooltipContent>{tr(UI.notesTip)}</TooltipContent>
          </Tooltip>
          <Segmented id="lang" size="sm" value={lang} onChange={setLang} items={LANGS} />
          <Segmented id="theme" size="sm" value={theme} onChange={setTheme} items={THEMES} />
        </div>
        <Sheet open={open} onOpenChange={setOpen}>
          <SheetTrigger asChild>
            <button aria-label="Menu" className="ml-auto grid size-9 place-items-center rounded-full text-foreground md:hidden"><Menu className="size-4" /></button>
          </SheetTrigger>
          <SheetContent side="bottom" className="rounded-t-3xl">
            <SheetHeader><SheetTitle className="tracking-[.14em]">RYTHO HYPE</SheetTitle></SheetHeader>
            <div className="grid gap-6 px-4 pb-8">
              <div className="grid grid-cols-2 gap-1">
                {SECTIONS.map((s) => <a key={s.id} href={"#" + s.id} onClick={() => setOpen(false)} className={cn("rounded-xl px-3 py-3 text-sm", active === s.id ? "bg-foreground/8 text-foreground" : "text-muted-foreground")}>{s.t}</a>)}
              </div>
              <div className="flex flex-wrap gap-2"><Segmented id="lang-m" value={lang} onChange={setLang} items={LANGS} /><Segmented id="theme-m" value={theme} onChange={setTheme} items={THEMES} /></div>
              <label className="flex items-center gap-3 text-sm text-muted-foreground"><Switch checked={notes} onCheckedChange={setNotes} />{tr(UI.notesLong)}</label>
            </div>
          </SheetContent>
        </Sheet>
      </Glass>
    </header>
  )
}
