import * as React from "react"
import type { ProductId } from "@/data"

export type Theme = "dark" | "rytho" | "light"
type S = {
  theme: Theme; setTheme: (t: Theme) => void
  notes: boolean; setNotes: (v: boolean) => void
  product: ProductId; setProduct: (p: ProductId) => void
}
const Ctx = React.createContext<S>(null!)
export const useApp = () => React.useContext(Ctx)

export function AppProvider({ children }: { children: React.ReactNode }) {
  const [theme, setThemeS] = React.useState<Theme>(() => (localStorage.getItem("rh2-theme") as Theme) || "dark")
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
  React.useEffect(() => { localStorage.setItem("rh2-notes", notes ? "1" : "0") }, [notes])
  const setTheme = React.useCallback((t: Theme) => {
    // cross-fade the whole page between themes when supported
    const d = document as any
    if (d.startViewTransition && !matchMedia("(prefers-reduced-motion: reduce)").matches) d.startViewTransition(() => setThemeS(t))
    else setThemeS(t)
  }, [])
  return <Ctx.Provider value={{ theme, setTheme, notes, setNotes, product, setProduct }}>{children}</Ctx.Provider>
}

/** Small "待補" note — shown only when the notes switch is on. Neutral grey, hollow dot, no third hue. */
export function Missing({ children, className = "" }: { children: React.ReactNode; className?: string }) {
  const { notes } = useApp()
  if (!notes) return null
  return (
    <p className={"flex items-start gap-2 text-xs text-muted-foreground " + className}>
      <span className="mt-[5px] size-1.5 shrink-0 rounded-full ring-1 ring-muted-foreground/70" />
      <span>待補：{children}</span>
    </p>
  )
}
