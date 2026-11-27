/* All copy + asset paths. Images live in ../img (shared with v1). */
export const IMG = (f: string) => `../img/${f}`

export type ProductId = "p01" | "p02" | "p03" | "p04"
export type Product = {
  id: ProductId; n: string; en: string; zh: string; line: string
  heightMm: number; heightLabel: string; ai: boolean
  closeup: string; scene: string
  facts: { k: string; v: string }[]
  missing?: string
}

export const PRODUCTS: Product[] = [
  { id: "p01", n: "01", en: "Portable", zh: "隨身", line: "螺旋全透明聲學腔，一手帶走。", heightMm: 180, heightLabel: "H 180 mm", ai: false,
    closeup: "c01.webp", scene: "arch_01.webp",
    facts: [{ k: "取自整塔", v: "透明中音模組的振膜與螺旋腔" }, { k: "連線", v: "Bluetooth" }, { k: "狀態", v: "概念階段" }],
    missing: "精修渲染（目前 AI 概念圖、無 CAD）" },
  { id: "p02", n: "02", en: "Home AI · Single", zh: "單顆＋底座", line: "一顆透明模組，中心加同軸高音。", heightMm: 261, heightLabel: "H 261 mm", ai: true,
    closeup: "c02.webp", scene: "arch_02.webp",
    facts: [{ k: "取自整塔", v: "透明中音模組 ×1＋新增同軸高音、底座" }, { k: "連線", v: "Wi-Fi · AI · Bluetooth" }, { k: "狀態", v: "原模組渲染" }],
    missing: "底座修薄、振膜透光特寫" },
  { id: "p03", n: "03", en: "Home AI · Upper Two", zh: "上半段兩節", line: "整塔上半段直接取下，自己就能站立。", heightMm: 1022, heightLabel: "H 1,022 mm ×2", ai: true,
    closeup: "c03.webp", scene: "arch_03.webp",
    facts: [{ k: "取自整塔", v: "小圓高音 ×2、方形單體、透明中音 ×1" }, { k: "連線", v: "Wi-Fi · AI · Bluetooth" }, { k: "狀態", v: "原模型渲染" }] },
  { id: "p04", n: "04", en: "Bespoke · Full Set", zh: "整組高訂", line: "單體與箱體不動，只換承載主體。", heightMm: 2693, heightLabel: "H 2,693 mm ×2", ai: true,
    closeup: "c04.webp", scene: "arch_04.webp",
    facts: [{ k: "取自整塔", v: "整組八個單體與箱體" }, { k: "連線", v: "Wi-Fi · AI" }, { k: "狀態", v: "原網格渲染" }],
    missing: "完整外殼版" },
]

export type BodyKey = "orig" | "fin" | "hifi"
export const BODIES: Record<BodyKey, { label: string; note: string; c: { name: string; sw: string; img: string }[] }> = {
  orig: { label: "Original", note: "原版主體 · 原模型渲染", c: [{ name: "原版", sw: "#2a2c30", img: "b_original.webp" }] },
  fin: { label: "Fin", note: "Fin 主體 · AI 概念圖，已對齊原版單體位置 · 待 CAD", c: [
    { name: "鋁本色", sw: "linear-gradient(135deg,#f2f3f5,#a9adb3)", img: "r3_style_02_aluminium_fins.webp" },
    { name: "黑色陽極", sw: "#16171a", img: "fin_black_anodized.webp" },
    { name: "香檳金", sw: "#d8c2a0", img: "fin_champagne.webp" },
    { name: "石墨灰", sw: "#7d8187", img: "fin_graphite.webp" },
    { name: "白陶瓷", sw: "#f7f7f4", img: "fin_white_ceramic.webp" },
    { name: "萊姆細線", sw: "conic-gradient(#C6F432 0 25%,#d9dbdf 0)", img: "fin_rytho_lime.webp" },
    { name: "古銅", sw: "#b06a3e", img: "fin_bronze.webp" }] },
  hifi: { label: "Hi-Fi", note: "Hi-Fi 主體 · 經典 Hi-Fi 設計語彙（Blender 渲染，已對齊原版單體位置）· 待 CAD", c: [
    { name: "70s 錄音室監聽", sw: "linear-gradient(135deg,#6b4429 50%,#d8653a 50%)", img: "hifi6_studio70s.webp" },
    { name: "英式傳統監聽", sw: "linear-gradient(135deg,#3a2618 50%,#c9a24a 50%)", img: "hifi6_heritage.webp" },
    { name: "北歐雕塑", sw: "linear-gradient(135deg,#d9dcdf 50%,#b9b2a6 50%)", img: "hifi6_scandi_sculpt.webp" }] },
}

export const EXPLODE_LABELS = [
  { y: .133, t: "CHASSIS", s: "帶卡榫的承載主體 · 唯一可變件", key: true },
  { y: .242, t: "TWEETER ×2", s: "小圓高音模組 · 原箱體" },
  { y: .337, t: "HIGH", s: "方形面單體 · 原箱體" },
  { y: .507, t: "TRANSPARENT MID ×3", s: "玻音先創透明振膜 · 螺旋腔", hero: true },
  { y: .781, t: "WOOFER ×2", s: "低音模組 · 原箱體" },
]

export const PARTNERS = [
  { role: "Driver", name: "玻音先創", d: "單體技術與製造：透明玻璃振膜、單體參數、良率與供應。" },
  { role: "Software", name: "Rytho", d: "軟體技術：AI 聆聽、App 與 Wi-Fi 連網體驗。" },
  { role: "Design", name: "OPQ Studio", d: "產品設計：透明結構、卡榫主體、樣機與視覺敘事。" },
  { role: "DSP", name: "玩樂生活", d: "聲學技術：DSP 調校、分頻與量測。" },
]

export const STEPS = [
  { n: "01", t: "單體與視覺樣機", d: "確認透明振膜單體資料" },
  { n: "02", t: "家用 AI 樣機", d: "02／03 比較、Wi-Fi 與 AI 整合" },
  { n: "03", t: "隨身可行性", d: "電池、體積、耐用與成本" },
  { n: "04", t: "高訂主體系列", d: "主體與顏色訂製流程" },
]

export const SECTIONS = [
  { id: "film", t: "Film" },
  { id: "core", t: "Diaphragm" },
  { id: "explode", t: "Explode" },
  { id: "family", t: "Family" },
  { id: "products", t: "Products" },
  { id: "ai", t: "AI" },
  { id: "partner", t: "Partner" },
  { id: "faq", t: "FAQ" },
] as const

/* FAQ — self-contained answers (AI-citable). Facts only: no performance claims (聲學設計強制規則 §3). Also emitted as FAQPage JSON-LD by prerender.mjs. */
export const SITE_URL = "https://sanssanchou-dot.github.io/rytho-hype/v2/"
export const FAQ = [
  { q: "RYTHO HYPE 是什麼？", a: "RYTHO HYPE 是一套透明喇叭產品概念：以玻音先創的透明玻璃振膜為核心，搭配透明箱體與螺旋葉片內構，讓發聲的結構被看見。由 OPQ Studio 設計，Rytho、玻音先創、玩樂生活共同開發。" },
  { q: "RYTHO HYPE 有哪幾個產品？", a: "一對完整的塔型喇叭可以拆成四個產品：01 隨身（Bluetooth，高 180 mm）、02 單顆＋底座（Wi‑Fi／AI，高 261 mm）、03 上半段兩節（Wi‑Fi／AI，高 1,022 mm，一對）、04 整組高訂（Wi‑Fi／AI，高 2,693 mm，一對）。" },
  { q: "透明振膜和螺旋葉片在結構上扮演什麼角色？", a: "中音模組正面是玻音先創的透明玻璃振膜；箱體內的螺旋葉片同時是導音管，背波沿螺旋流道前進，從尾端出氣口離開。網站上的粒子動畫取自 261027 模型的流道幾何，屬示意，不是模擬或量測結果。" },
  { q: "04 整組高訂可以訂製什麼？", a: "八個單體與箱體維持不變，只更換承載它們的主體。目前提供 Original、Fin（七種表面）與 Hi‑Fi（70s 錄音室監聽、英式傳統監聽、北歐雕塑）三種主體方向，皆待 CAD。" },
  { q: "各合作方負責什麼？", a: "玻音先創負責單體技術與製造（透明玻璃振膜）；Rytho 負責軟體技術（AI 聆聽、App、Wi‑Fi 連網）；OPQ Studio 負責產品設計；玩樂生活負責 DSP 聲學技術（調校、分頻與量測）。" },
  { q: "RYTHO HYPE 現在可以購買嗎？", a: "還不行。RYTHO HYPE 目前在概念與樣機階段，下一步是單體與視覺樣機、家用 AI 樣機、隨身可行性評估，以及高訂主體系列。" },
]
