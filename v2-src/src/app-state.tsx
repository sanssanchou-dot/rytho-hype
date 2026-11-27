import * as React from "react"
import { META, UI, type Lang, type ProductId, type T } from "@/data"

export type Theme = "dark" | "rytho" | "light"
type S = {
  theme: Theme; setTheme: (t: Theme) => void
  lang: Lang; setLang: (l: Lang) => void
  notes: boolean; setNotes: (v: boolean) => void
  product: ProductId; setProduct: (p: ProductId) => void
}
const Ctx = React.createContext<S>(null!)
export const useApp = () => React.useContext(Ctx)
/** Translate a { zh, en } pair to the current language. */
export function useT() { const { lang } = useApp(); return React.useCallback((x: T) => x[lang], [lang]) }

/* Language lives in the URL: /v2/ = 中文, /v2/en/ = English (each prerendered for crawlers). */
const isEnPath = () => /\/en\/?$/.test(location.pathname)
const pathFor = (l: Lang) => { const p = location.pathname.replace(/en\/?$/, ""); return (l === "en" ? p + "en/" : p) + location.hash }

/** Fade-through for whole-page changes (theme, language) when View Transitions exist. */
function transition(fn: () => void) {
  const d = document as any
  if (d.startViewTransition && !matchMedia("(prefers-reduced-motion: reduce)").matches) d.startViewTransition(fn)
  else fn()
}

export function AppProvider({ children }: { children: React.ReactNode }) {
  const [theme, setThemeS] = React.useState<Theme>(() => (localStorage.getItem("rh2-theme") as Theme) || "dark")
  const [lang, setLangS] = React.useState<Lang>(() => isEnPath() ? "en" : "zh")
  const [notes, setNotes] = React.useState(() => localStorage.getItem("rh2-notes") !== "0")
  const [product, setProduct] = React.useState<ProductId>(() => {
    const h = location.hash.slice(1); return (["p01", "p02", "p03", "p04"].includes(h) ? h : "p01") as ProductId
  })
  React.useEffect(() => {
    const c = document.documentElement.classList
    c.remove("dark", "rytho", "light"); c.add(theme)
    document.documentElement.style.colorScheme = theme === "light" ? "light" : "dark"
    localStorage.setItem("rh2-theme", theme)
  }, [theme])
  React.useEffect(() => {
    document.documentElement.lang = lang === "en" ? "en" : "zh-Hant"
    document.title = META.title[lang]
    document.querySelector('meta[name="description"]')?.setAttribute("content", META.description[lang])
  }, [lang])
  React.useEffect(() => {
    const on = () => setLangS(isEnPath() ? "en" : "zh")
    addEventListener("popstate", on); return () => removeEventListener("popstate", on)
  }, [])
  React.useEffect(() => { localStorage.setItem("rh2-notes", notes ? "1" : "0") }, [notes])
  const setTheme = React.useCallback((t: Theme) => transition(() => setThemeS(t)), [])
  const setLang = React.useCallback((l: Lang) => transition(() => { history.replaceState(null, "", pathFor(l)); setLangS(l) }), [])
  return <Ctx.Provider value={{ theme, setTheme, lang, setLang, notes, setNotes, product, setProduct }}>{children}</Ctx.Provider>
}

/** Small to-do note — shown only when the notes switch is on. Neutral grey, hollow dot, no third hue. */
export function Missing({ children, className = "" }: { children: React.ReactNode; className?: string }) {
  const { notes } = useApp(); const tr = useT()
  if (!notes) return null
  return (
    <p className={"flex items-start gap-2 text-xs text-muted-foreground " + className}>
      <span className="mt-[5px] size-1.5 shrink-0 rounded-full ring-1 ring-muted-foreground/70" />
      <span>{tr(UI.todo)}{children}</span>
    </p>
  )
}
