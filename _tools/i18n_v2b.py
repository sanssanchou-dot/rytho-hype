R = 'C:/Users/san/.001_OPQ_Design_Project/PROJECTS/_SOUND/20260714_speaker/output/RYTHO_HYPE_WEB/v2-src/src/sections/'
def edit(n, pairs):
    t = open(R + n, encoding='utf-8').read()
    for a, b in pairs:
        assert a in t, (n, a[:60]); t = t.replace(a, b)
    open(R + n, 'w', encoding='utf-8').write(t); print('ok', n)
edit('Closing.tsx', [('import { PARTNERS, STEPS, UI } from "@/data"', 'import { PARTNERS, PARTNER_LINE, STEPS, UI } from "@/data"'),
                     ('text-muted-foreground">玻音先創 · RYTHO · OPQ STUDIO · 玩樂生活</p>', 'text-muted-foreground">{PARTNER_LINE}</p>')])
edit('Nav.tsx', [('import { SECTIONS, UI, type Lang } from "@/data"', 'import { LANG_LABELS as LANGS, SECTIONS, UI } from "@/data"'),
                 ('const LANGS: { v: Lang; label: string }[] = [{ v: "zh", label: "中" }, { v: "en", label: "EN" }]\n', '')])
