import sys
R = r'C:\Users\san\.001_OPQ_Design_Project\PROJECTS\_SOUND\20260714_speaker\output\RYTHO_HYPE_WEB\v2-src\src\sections\\'


def edit(name, pairs):
    p = R + name
    t = open(p, encoding='utf-8').read()
    for a, b in pairs:
        if a not in t:
            sys.exit(f'{name}: not found: {a[:70]!r}')
        t = t.replace(a, b)
    open(p, 'w', encoding='utf-8').write(t)
    print('ok', name)


# Hero: repair the split newline
edit('Hero.tsx', [('.split("\n")', '.split("\\n")')])

edit('Core.tsx', [
    ('import { IMG } from "@/data"', 'import { IMG, UI } from "@/data"'),
    ('import { useApp } from "@/app-state"', 'import { useApp, useT } from "@/app-state"'),
    ('  const { theme } = useApp()\n  const themeRef', '  const { theme } = useApp()\n  const tr = useT()\n  const themeRef'),
    ('<Lab at={labels.d} t="GLASS DIAPHRAGM" s="玻音先創 透明振膜" />', '<Lab at={labels.d} t="GLASS DIAPHRAGM" s={tr(UI.vizD)} />'),
    ('<Lab at={labels.s} t="SPIRAL = PORT LENGTH" s="螺旋葉片即導音管" />', '<Lab at={labels.s} t="SPIRAL = PORT LENGTH" s={tr(UI.vizS)} />'),
    ('<Lab at={labels.p} t="PORT" s="出氣口" />', '<Lab at={labels.p} t="PORT" s={tr(UI.vizP)} />'),
    ('const LINE1 = "玻璃振膜＋透明箱體，", LINE2 = "讓聲音第一次被看見。"\n\nexport function Core() {\n  const chars = [...LINE1, "\\n", ...LINE2]',
     'export function Core() {\n  const tr = useT()\n  const text = tr(UI.coreLines), en = /^[A-Za-z]/.test(text)\n  // CJK lights up per character, English per word\n  const chars = en ? text.split(/(\\s+)/).flatMap((w) => w.includes("\\n") ? ["\\n"] : [w]) : [...text]'),
    ('        <motion.h2 initial="h" whileInView="v"', '        <motion.h2 key={text} initial="h" whileInView="v"'),
    ('        中音模組側視：前方是透明振膜的直接輻射，後方背波沿螺旋葉片走完導音管，從尾端出氣口離開。\n        <span className="mt-2 block text-[11px] opacity-70">粒子路徑取自 261027 模型的螺旋流道幾何；動畫為示意，非模擬結果。</span>',
     '        {tr(UI.coreCaption)}\n        <span className="mt-2 block text-[11px] opacity-70">{tr(UI.coreNote)}</span>'),
])

edit('Explode.tsx', [
    ('import { EXPLODE_LABELS, IMG } from "@/data"', 'import { EXPLODE_LABELS, IMG, UI } from "@/data"\nimport { useT } from "@/app-state"'),
    ('  const [ready, setReady] = React.useState(false)', '  const [ready, setReady] = React.useState(false)\n  const tr = useT()'),
    ('tracking-tight">八個單體，一個可換的主體。</h2>', 'tracking-tight">{tr(UI.explodeH)}</h2>'),
    ('{open ? "Assemble" : "Explode"}', '{tr(open ? UI.assemble : UI.explode)}'),
    ('<span className="mt-1 block text-xs text-muted-foreground">{l.s}</span>', '<span className="mt-1 block text-xs text-muted-foreground">{tr(l.s)}</span>'),
    ('<span className="text-right text-xs text-muted-foreground">{l.s}</span>', '<span className="text-right text-xs text-muted-foreground">{tr(l.s)}</span>'),
])

edit('Products.tsx', [
    ('import { Missing, useApp } from "@/app-state"', 'import { Missing, useApp, useT } from "@/app-state"'),
    ('import { BODIES, IMG, PRODUCTS, type BodyKey, type ProductId } from "@/data"', 'import { BODIES, IMG, PRODUCTS, UI, type BodyKey, type ProductId } from "@/data"'),
    # Family
    ('export function Family() {\n  const { setProduct } = useApp()', 'export function Family() {\n  const { setProduct } = useApp()\n  const tr = useT()'),
    ('tracking-tight">一座塔，拆成四個產品<span className="text-key">.</span></h2>', 'tracking-tight">{tr(UI.familyH)}<span className="text-key">.</span></h2>'),
    ('text-muted-foreground">由小到大：從一顆透明模組的隨身音響，到整組可訂製的高訂。02 起內建 Wi-Fi 與 AI。</p>', 'text-muted-foreground">{tr(UI.familyP)}</p>'),
    ('alt="RYTHO HYPE family at true scale"', 'alt={tr(UI.familyAlt)}'),
    ('<span className="text-[15px] font-medium">{p.zh}</span>', '<span className="text-[15px] font-medium">{tr(p.name)}</span>'),
    ('<ScaleBar mm={p.heightMm} className="mx-1 mt-3" />', '<ScaleBar mm={p.heightMm} label={tr(UI.scaleOf)} className="mx-1 mt-3" />'),
    ('<span>{p.n} {p.zh} · 情境</span><span className="flex items-center gap-1 text-muted-foreground">查看 <ArrowRight className="size-3" /></span>',
     '<span>{p.n} {tr(p.name)} · {tr(UI.inSpace)}</span><span className="flex items-center gap-1 text-muted-foreground">{tr(UI.view)} <ArrowRight className="size-3" /></span>'),
    ('function ScaleBar({ mm, className }: { mm: number; className?: string }) {', 'function ScaleBar({ mm, label, className }: { mm: number; label: string; className?: string }) {'),
    ('title={`${Math.round(w)}% of full tower height`}', 'title={`${Math.round(w)}% ${label}`}'),
    # Products
    ('  const { product, setProduct } = useApp()', '  const { product, setProduct } = useApp()\n  const tr = useT()'),
    ('<span className="hidden sm:inline">{x.zh}</span>', '<span className="hidden sm:inline">{tr(x.name)}</span>'),
    ('<motion.img key={hero} src={IMG(hero)} alt={p.zh}', '<motion.img key={hero} src={IMG(hero)} alt={tr(p.name)}'),
    ('<span className="font-mono text-[10px] tracking-[.22em] text-muted-foreground uppercase">{p.en}</span>',
     '{p.en !== tr(p.name) && <span className="font-mono text-[10px] tracking-[.22em] text-muted-foreground uppercase">{p.en}</span>}'),
    ('font-light tracking-tight">{p.zh}</h3>', 'font-light tracking-tight">{tr(p.name)}</h3>'),
    ('<p className="mt-4 text-[15px] text-muted-foreground">{p.line}</p>', '<p className="mt-4 text-[15px] text-muted-foreground">{tr(p.line)}</p>'),
    ('<button onClick={() => setSw(i)} aria-label={c.name}', '<button onClick={() => setSw(i)} aria-label={tr(c.name)}'),
    ('<TooltipContent>{c.name}</TooltipContent>', '<TooltipContent>{tr(c.name)}</TooltipContent>'),
    ('<p className="mt-3 text-xs text-muted-foreground">{b.note}</p>', '<p className="mt-3 text-xs text-muted-foreground">{tr(b.note)}</p>'),
    ('<Glass key={f.k} level={3}', '<Glass key={f.k.en} level={3}'),
    ('<dt className="text-[11px] text-muted-foreground">{f.k}</dt>', '<dt className="text-[11px] text-muted-foreground">{tr(f.k)}</dt>'),
    ('<dd className="mt-1.5 text-[13px] leading-snug">{f.v}</dd>', '<dd className="mt-1.5 text-[13px] leading-snug">{tr(f.v)}</dd>'),
    ('{p.missing && <Missing className="mt-5">{p.missing}</Missing>}', '{p.missing && <Missing className="mt-5">{tr(p.missing)}</Missing>}'),
])

edit('Closing.tsx', [
    ('import { PARTNERS, STEPS } from "@/data"', 'import { PARTNERS, STEPS, UI } from "@/data"'),
    ('import { Missing, useApp } from "@/app-state"', 'import { Missing, useApp, useT } from "@/app-state"'),
    ('  const mic = useMicrophone()', '  const mic = useMicrophone()\n  const tr = useT()'),
    ('text-muted-foreground">02—04 內建 Wi-Fi 晶片，開啟 AI。</p>', 'text-muted-foreground">{tr(UI.aiP)}</p>'),
    ('<p className="text-[15px]">{live ? "正在聆聽…" : "對它說話試試看"}</p>', '<p className="text-[15px]">{tr(live ? UI.aiListening : UI.aiTry)}</p>'),
    ('{mic.state === "denied" ? "麥克風權限被拒絕" : live ? "光會隨你的聲音升起，聲音不會離開這台電腦。" : "按下麥克風，光會跟著你的聲音呼吸。"}',
     '{tr(mic.state === "denied" ? UI.aiDenied : live ? UI.aiLive : UI.aiIdle)}'),
    ('aria-label={live ? "停止聆聽" : "開始聆聽"}', 'aria-label={tr(live ? UI.aiStop : UI.aiStart)}'),
    ('<Missing className="mt-6 justify-center">AI 功能定義、麥克風／狀態燈位置</Missing>', '<Missing className="mt-6 justify-center">{tr(UI.aiMissing)}</Missing>'),
    ('export function Partner() {\n  return (', 'export function Partner() {\n  const tr = useT()\n  return ('),
    ('<p className="mt-3 text-[13px] leading-relaxed text-muted-foreground">{p.d}</p>', '<p className="mt-3 text-[13px] leading-relaxed text-muted-foreground">{tr(p.d)}</p>'),
    ('<h4 className="mt-5 text-[15px] font-medium">{s.t}</h4>', '<h4 className="mt-5 text-[15px] font-medium">{tr(s.t)}</h4>'),
    ('<p className="mt-1.5 text-[13px] text-muted-foreground">{s.d}</p>', '<p className="mt-1.5 text-[13px] text-muted-foreground">{tr(s.d)}</p>'),
    ('<Missing className="mt-10">四方 logo（玻音先創、Rytho、OPQ、玩樂生活）；時程與預算刻意不寫，等雙方確認。</Missing>', '<Missing className="mt-10">{tr(UI.partnerMissing)}</Missing>'),
    ('export function CTA() {\n  const { theme } = useApp()', 'export function CTA() {\n  const { theme } = useApp()\n  const tr = useT()'),
    ('              一起把透明振膜帶進產品\n', '              {tr(UI.cta)}\n'),
])
