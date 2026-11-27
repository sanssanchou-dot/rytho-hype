/* All copy + asset paths — ONE source for both languages. Every visible string is a T = { zh, en }.
   Images live in /rytho-hype/img (shared with v1); resolved from the bundle URL so /v2/ and /v2/en/ both work. */
export type Lang = "zh" | "en"
export type T = { zh: string; en: string }
const t = (zh: string, en: string): T => ({ zh, en })

const here = import.meta.url
const IMG_BASE = here.includes("/assets/") ? new URL(here.slice(0, here.lastIndexOf("/assets/")) + "/../img/").href : "/img/"
export const IMG = (f: string) => IMG_BASE + f

export const SITE_URL = "https://sanssanchou-dot.github.io/rytho-hype/v2/"
export const META = {
  title: t("RYTHO HYPE — 讓聲音第一次被看見", "RYTHO HYPE — Sound, seen for the first time"),
  description: t(
    "RYTHO HYPE：以玻音先創透明玻璃振膜與透明螺旋箱體為核心的喇叭產品概念。一對塔型喇叭拆成四個產品——隨身、單顆＋底座、上半段兩節、整組高訂。OPQ Studio × Rytho × 玩樂生活。",
    "RYTHO HYPE is a transparent loudspeaker concept built around a glass diaphragm by 玻音先創 and a clear spiral enclosure. One pair of towers splits into four products. OPQ Studio × Rytho × 玩樂生活."),
  ogDesc: t("透明玻璃振膜 × 透明箱體。一座塔，拆成四個產品。", "A transparent glass diaphragm in a clear enclosure. One tower, four products."),
  ogAlt: t("RYTHO HYPE 四個產品依實際比例並排", "The four RYTHO HYPE products side by side at true scale"),
}

/* ---------------- UI copy ---------------- */
export const UI = {
  notes: t("待補", "Notes"),
  notesTip: t("顯示／隱藏內部待補註記", "Show / hide internal to-do notes"),
  notesLong: t("顯示待補項", "Show to-do notes"),
  todo: t("待補：", "To do: "),
  heroEyebrow: t("TRANSPARENT GLASS DIAPHRAGM", "TRANSPARENT GLASS DIAPHRAGM"),
  heroH1: t("讓聲音\n第一次被看見", "Sound,\nseen for the first time"),
  coreLines: t("玻璃振膜＋透明箱體，\n讓聲音第一次被看見。", "A glass diaphragm in a clear enclosure —\nsound you can see."),
  coreCaption: t("中音模組側視：前方是透明振膜的直接輻射，後方背波沿螺旋葉片走完導音管，從尾端出氣口離開。",
    "Side view of the mid module: the transparent diaphragm radiates forward; the rear wave runs the full channel of the spiral vane and leaves through the outlet at the tail."),
  coreNote: t("粒子路徑取自 261027 模型的螺旋流道幾何；動畫為示意，非模擬結果。",
    "Particle paths are traced from the spiral channel geometry of the 261027 model; the animation is illustrative, not a simulation."),
  vizD: t("玻音先創 透明振膜", "Transparent diaphragm by 玻音先創"),
  vizS: t("螺旋葉片即導音管", "The spiral vane is the port"),
  vizP: t("出氣口", "Outlet"),
  explodeH: t("八個單體，一個可換的主體。", "Eight drivers, one changeable body."),
  explode: t("Explode", "Explode"), assemble: t("Assemble", "Assemble"),
  familyH: t("一座塔，拆成四個產品", "One tower, four products"),
  familyP: t("由小到大：從一顆透明模組的隨身音響，到整組可訂製的高訂。02 起內建 Wi-Fi 與 AI。",
    "From small to large: a portable speaker built from one transparent module, up to a fully bespoke pair. Wi‑Fi and AI from 02 up."),
  familyAlt: t("RYTHO HYPE 四個產品依實際比例並排", "The four RYTHO HYPE products side by side at true scale"),
  inSpace: t("情境", "In space"), view: t("查看", "View"),
  scaleOf: t("佔整塔高度", "of full tower height"),
  aiP: t("02—04 內建 Wi-Fi 晶片，開啟 AI。", "02–04 have a built-in Wi‑Fi chip that enables AI."),
  aiTry: t("對它說話試試看", "Try talking to it"),
  aiListening: t("正在聆聽…", "Listening…"),
  aiDenied: t("麥克風權限被拒絕", "Microphone permission was denied"),
  aiLive: t("光會隨你的聲音升起，聲音不會離開這台電腦。", "The light rises with your voice. Audio never leaves this computer."),
  aiIdle: t("按下麥克風，光會跟著你的聲音呼吸。", "Press the mic and the light breathes with your voice."),
  aiStart: t("開始聆聽", "Start listening"), aiStop: t("停止聆聽", "Stop listening"),
  aiMissing: t("AI 功能定義、麥克風／狀態燈位置", "AI feature definition; microphone and status-light placement"),
  partnerMissing: t("四方 logo（玻音先創、Rytho、OPQ、玩樂生活）；時程與預算刻意不寫，等雙方確認。",
    "Logos of all four partners. Schedule and budget are deliberately left out until both sides confirm."),
  faqH: t("常見問題", "FAQ"),
  cta: t("一起把透明振膜帶進產品", "Bring the transparent diaphragm into products with us"),
}

/* ---------------- products ---------------- */
export type ProductId = "p01" | "p02" | "p03" | "p04"
export type Product = {
  id: ProductId; n: string; en: string; name: T; line: T
  heightMm: number; heightLabel: string; ai: boolean
  closeup: string; scene: string
  facts: { k: T; v: T }[]
  missing?: T
}
const K = { from: t("取自整塔", "From the tower"), conn: t("連線", "Connectivity"), status: t("狀態", "Status") }

export const PRODUCTS: Product[] = [
  { id: "p01", n: "01", en: "Portable", name: t("隨身", "Portable"), line: t("螺旋全透明聲學腔，一手帶走。", "A fully transparent spiral acoustic chamber you carry in one hand."),
    heightMm: 180, heightLabel: "H 180 mm", ai: false, closeup: "c01.webp", scene: "arch_01.webp",
    facts: [{ k: K.from, v: t("透明中音模組的振膜與螺旋腔", "The transparent mid module’s diaphragm and spiral chamber") }, { k: K.conn, v: t("Bluetooth", "Bluetooth") }, { k: K.status, v: t("概念階段", "Concept stage") }],
    missing: t("精修渲染（目前 AI 概念圖、無 CAD）", "Final render (currently an AI concept image, no CAD)") },
  { id: "p02", n: "02", en: "Home AI · Single", name: t("單顆＋底座", "Single + Base"), line: t("一顆透明模組，中心加同軸高音。", "One transparent module with a coaxial tweeter at its centre."),
    heightMm: 261, heightLabel: "H 261 mm", ai: true, closeup: "c02.webp", scene: "arch_02.webp",
    facts: [{ k: K.from, v: t("透明中音模組 ×1＋新增同軸高音、底座", "Transparent mid module ×1 + new coaxial tweeter and base") }, { k: K.conn, v: t("Wi-Fi · AI · Bluetooth", "Wi‑Fi · AI · Bluetooth") }, { k: K.status, v: t("原模組渲染", "Rendered from the original module") }],
    missing: t("底座修薄、振膜透光特寫", "Slimmer base; close-up of light through the diaphragm") },
  { id: "p03", n: "03", en: "Home AI · Upper Two", name: t("上半段兩節", "Upper Two Sections"), line: t("整塔上半段直接取下，自己就能站立。", "The tower’s upper half lifts off and stands on its own."),
    heightMm: 1022, heightLabel: "H 1,022 mm ×2", ai: true, closeup: "c03.webp", scene: "arch_03.webp",
    facts: [{ k: K.from, v: t("小圓高音 ×2、方形單體、透明中音 ×1", "Small round tweeters ×2, square driver, transparent mid ×1") }, { k: K.conn, v: t("Wi-Fi · AI · Bluetooth", "Wi‑Fi · AI · Bluetooth") }, { k: K.status, v: t("原模型渲染", "Rendered from the original model") }] },
  { id: "p04", n: "04", en: "Bespoke · Full Set", name: t("整組高訂", "Bespoke Full Set"), line: t("單體與箱體不動，只換承載主體。", "Drivers and enclosures stay; only the carrying body changes."),
    heightMm: 2693, heightLabel: "H 2,693 mm ×2", ai: true, closeup: "c04.webp", scene: "arch_04.webp",
    facts: [{ k: K.from, v: t("整組八個單體與箱體", "All eight drivers and enclosures") }, { k: K.conn, v: t("Wi-Fi · AI", "Wi‑Fi · AI") }, { k: K.status, v: t("原網格渲染", "Rendered from the original mesh") }],
    missing: t("完整外殼版", "Full-shell version") },
]

export type BodyKey = "orig" | "fin" | "hifi"
export const BODIES: Record<BodyKey, { label: string; note: T; c: { name: T; sw: string; img: string }[] }> = {
  orig: { label: "Original", note: t("原版主體 · 原模型渲染", "Original body · rendered from the original model"), c: [{ name: t("原版", "Original"), sw: "#2a2c30", img: "b_original.webp" }] },
  fin: { label: "Fin", note: t("Fin 主體 · AI 概念圖，已對齊原版單體位置 · 待 CAD", "Fin body · AI concept image aligned to the original driver positions · CAD pending"), c: [
    { name: t("鋁本色", "Natural aluminium"), sw: "linear-gradient(135deg,#f2f3f5,#a9adb3)", img: "r3_style_02_aluminium_fins.webp" },
    { name: t("黑色陽極", "Black anodised"), sw: "#16171a", img: "fin_black_anodized.webp" },
    { name: t("香檳金", "Champagne"), sw: "#d8c2a0", img: "fin_champagne.webp" },
    { name: t("石墨灰", "Graphite"), sw: "#7d8187", img: "fin_graphite.webp" },
    { name: t("白陶瓷", "White ceramic"), sw: "#f7f7f4", img: "fin_white_ceramic.webp" },
    { name: t("萊姆細線", "Lime pinstripe"), sw: "conic-gradient(#C6F432 0 25%,#d9dbdf 0)", img: "fin_rytho_lime.webp" },
    { name: t("古銅", "Bronze"), sw: "#b06a3e", img: "fin_bronze.webp" }] },
  hifi: { label: "Hi-Fi", note: t("Hi-Fi 主體 · 經典 Hi-Fi 設計語彙（Blender 渲染，已對齊原版單體位置）· 待 CAD", "Hi‑Fi body · classic hi‑fi design language (Blender render aligned to the original driver positions) · CAD pending"), c: [
    { name: t("70s 錄音室監聽", "70s studio monitor"), sw: "linear-gradient(135deg,#6b4429 50%,#d8653a 50%)", img: "hifi6_studio70s.webp" },
    { name: t("英式傳統監聽", "British heritage monitor"), sw: "linear-gradient(135deg,#3a2618 50%,#c9a24a 50%)", img: "hifi6_heritage.webp" },
    { name: t("北歐雕塑", "Scandinavian sculpture"), sw: "linear-gradient(135deg,#d9dcdf 50%,#b9b2a6 50%)", img: "hifi6_scandi_sculpt.webp" }] },
}

export const EXPLODE_LABELS: { y: number; t: string; s: T; key?: boolean; hero?: boolean }[] = [
  { y: .133, t: "CHASSIS", s: t("帶卡榫的承載主體 · 唯一可變件", "Carrying body with bayonet locks · the only variable part"), key: true },
  { y: .242, t: "TWEETER ×2", s: t("小圓高音模組 · 原箱體", "Small round tweeter modules · original enclosures") },
  { y: .337, t: "HIGH", s: t("方形面單體 · 原箱體", "Square-face driver · original enclosure") },
  { y: .507, t: "TRANSPARENT MID ×3", s: t("玻音先創透明振膜 · 螺旋腔", "Transparent diaphragm by 玻音先創 · spiral chamber"), hero: true },
  { y: .781, t: "WOOFER ×2", s: t("低音模組 · 原箱體", "Woofer modules · original enclosures") },
]

export const PARTNERS = [
  { role: "Driver", name: "玻音先創", d: t("單體技術與製造：透明玻璃振膜、單體參數、良率與供應。", "Driver technology and manufacturing: transparent glass diaphragm, driver parameters, yield and supply.") },
  { role: "Software", name: "Rytho", d: t("軟體技術：AI 聆聽、App 與 Wi-Fi 連網體驗。", "Software: AI listening, the app and the Wi‑Fi connected experience.") },
  { role: "Design", name: "OPQ Studio", d: t("產品設計：透明結構、卡榫主體、樣機與視覺敘事。", "Product design: transparent structure, bayonet body, prototypes and visual storytelling.") },
  { role: "DSP", name: "玩樂生活", d: t("聲學技術：DSP 調校、分頻與量測。", "Acoustics: DSP tuning, crossover and measurement.") },
]

export const STEPS = [
  { n: "01", t: t("單體與視覺樣機", "Driver & visual prototype"), d: t("確認透明振膜單體資料", "Confirm the transparent diaphragm driver data") },
  { n: "02", t: t("家用 AI 樣機", "Home AI prototype"), d: t("02／03 比較、Wi-Fi 與 AI 整合", "Compare 02 / 03; Wi‑Fi and AI integration") },
  { n: "03", t: t("隨身可行性", "Portable feasibility"), d: t("電池、體積、耐用與成本", "Battery, size, durability and cost") },
  { n: "04", t: t("高訂主體系列", "Bespoke body series"), d: t("主體與顏色訂製流程", "Body and colour customisation process") },
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

/* FAQ — self-contained answers (AI-citable). Facts only: no performance claims (聲學設計強制規則 §3). Emitted as FAQPage JSON-LD per language. */
export const FAQ: { q: T; a: T }[] = [
  { q: t("RYTHO HYPE 是什麼？", "What is RYTHO HYPE?"),
    a: t("RYTHO HYPE 是一套透明喇叭產品概念：以玻音先創的透明玻璃振膜為核心，搭配透明箱體與螺旋葉片內構，讓發聲的結構被看見。由 OPQ Studio 設計，Rytho、玻音先創、玩樂生活共同開發。",
      "RYTHO HYPE is a transparent loudspeaker concept built around a transparent glass diaphragm from 玻音先創, a clear enclosure and an internal spiral vane, so the structure that makes the sound stays visible. OPQ Studio leads the design; Rytho, 玻音先創 and 玩樂生活 co-develop it.") },
  { q: t("RYTHO HYPE 有哪幾個產品？", "Which products are in the RYTHO HYPE family?"),
    a: t("一對完整的塔型喇叭可以拆成四個產品：01 隨身（Bluetooth，高 180 mm）、02 單顆＋底座（Wi‑Fi／AI，高 261 mm）、03 上半段兩節（Wi‑Fi／AI，高 1,022 mm，一對）、04 整組高訂（Wi‑Fi／AI，高 2,693 mm，一對）。",
      "One pair of tower speakers splits into four products: 01 Portable (Bluetooth, 180 mm tall), 02 Single + Base (Wi‑Fi and AI, 261 mm), 03 Upper Two Sections (Wi‑Fi and AI, 1,022 mm, a pair) and 04 Bespoke Full Set (Wi‑Fi and AI, 2,693 mm, a pair).") },
  { q: t("透明振膜和螺旋葉片在結構上扮演什麼角色？", "What do the glass diaphragm and the spiral vane do?"),
    a: t("中音模組正面是玻音先創的透明玻璃振膜；箱體內的螺旋葉片同時是導音管，背波沿螺旋流道前進，從尾端出氣口離開。網站上的粒子動畫取自 261027 模型的流道幾何，屬示意，不是模擬或量測結果。",
      "The mid-range module radiates through the transparent glass diaphragm at the front. Inside the enclosure the spiral vane doubles as the port: the rear wave follows the spiral channel and leaves through the outlet at the tail. The particle animation on this site is traced from the channel geometry of the 261027 model; it is an illustration, not a simulation or measurement.") },
  { q: t("04 整組高訂可以訂製什麼？", "What can be customised on the 04 Bespoke set?"),
    a: t("八個單體與箱體維持不變，只更換承載它們的主體。目前提供 Original、Fin（七種表面）與 Hi‑Fi（70s 錄音室監聽、英式傳統監聽、北歐雕塑）三種主體方向，皆待 CAD。",
      "The eight drivers and their enclosures stay the same; only the body that carries them changes. Current body directions are Original, Fin (seven finishes) and Hi‑Fi (70s studio monitor, British heritage monitor, Scandinavian sculpture), all pending CAD.") },
  { q: t("各合作方負責什麼？", "Who does what?"),
    a: t("玻音先創負責單體技術與製造（透明玻璃振膜）；Rytho 負責軟體技術（AI 聆聽、App、Wi‑Fi 連網）；OPQ Studio 負責產品設計；玩樂生活負責 DSP 聲學技術（調校、分頻與量測）。",
      "玻音先創: driver technology and manufacturing (transparent glass diaphragm). Rytho: software (AI listening, app, Wi‑Fi). OPQ Studio: product design. 玩樂生活: DSP acoustics (tuning, crossover and measurement).") },
  { q: t("RYTHO HYPE 現在可以購買嗎？", "Can I buy RYTHO HYPE?"),
    a: t("還不行。RYTHO HYPE 目前在概念與樣機階段，下一步是單體與視覺樣機、家用 AI 樣機、隨身可行性評估，以及高訂主體系列。",
      "Not yet. RYTHO HYPE is at concept and prototype stage. Next steps are driver and visual prototypes, a home AI prototype, a portable feasibility study and the bespoke body series.") },
]

/* Same in both languages (proper nouns / language names) */
export const PARTNER_LINE = "玻音先創 · RYTHO · OPQ STUDIO · 玩樂生活"
export const LANG_LABELS: { v: Lang; label: string }[] = [{ v: "zh", label: "中" }, { v: "en", label: "EN" }]
