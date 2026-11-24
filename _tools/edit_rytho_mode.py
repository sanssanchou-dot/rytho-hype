p='index.html';t=open(p,encoding='utf-8').read()
# font
t=t.replace('family=Doto:wght@600;800;900&','family=Doto:wght@600;800;900&family=Urbanist:wght@200;300;400;500;600;700&',1)
# toggle: DARK / RYTHO / LIGHT
t=t.replace('<div id="themeT" class="glass"><button data-th="dark" class="on">DARK</button><button data-th="light">LIGHT</button></div>',
            '<div id="themeT" class="glass"><button data-th="dark" class="on">DARK</button><button data-th="rytho">RYTHO</button><button data-th="light">LIGHT</button></div>',1)
old="function setTheme(th){document.body.classList.toggle('light',th==='light');"
assert old in t
t=t.replace(old,"function setTheme(th){document.body.classList.toggle('light',th==='light');document.body.classList.toggle('rytho',th==='rytho');",1)
css='''
/* =====================  RYTHO MODE  (flat solid cards · acid lime + brand purple · no glass) ===================== */
body.rytho{--rb:#0E0F12;--rc:#1B1C20;--rc2:#25262B;--rl:#D6FF65;--rp:#723CE8;--rt:#F4F5F7;--rm:#8B8E95;--rd:#4A4C52;--ur:'Urbanist','Noto Sans HK',sans-serif;
 --acc:#D6FF65;background:var(--rb)!important;color:var(--rt)}
body.rytho main,body.rytho section{background:transparent}
/* kill glass + light */
body.rytho .lg-b,body.rytho .lg-t,body.rytho .lgrim,body.rytho #rail .redge{display:none!important}
body.rytho .lgx{box-shadow:none!important}
/* type */
body.rytho h2,body.rytho .pd-t,body.rytho .say,body.rytho .fam span,body.rytho .col h3,body.rytho .steps h4{font-family:var(--ur)!important}
body.rytho h2{font-weight:300!important;letter-spacing:-.02em!important}
body.rytho .pd-t{font-weight:300!important;font-size:clamp(34px,3.4vw,54px)!important;letter-spacing:-.01em!important}
body.rytho .pd-n{font:200 clamp(40px,4vw,64px)/1 var(--ur)!important;color:var(--rl)!important;letter-spacing:-.03em}
body.rytho .pd-en,body.rytho .mono,body.rytho .slash{font-family:var(--ur)!important;letter-spacing:.06em!important;text-transform:none!important;color:var(--rm)!important;font-weight:500}
body.rytho .pd-line,body.rytho .body{color:var(--rm)!important}
body.rytho .dot{color:var(--rl)!important}
/* statement */
body.rytho .say{font-weight:300!important;letter-spacing:-.02em!important}
body.rytho .say span{color:#2A2C31}
body.rytho .say span.lit{color:var(--rt)}
body.rytho #s-core .say{text-shadow:0 0 40px var(--rb),0 0 80px var(--rb)}
body.rytho .midviz img{opacity:.38}
body.rytho .mvl{font-family:var(--ur);letter-spacing:.04em;font-weight:600;color:var(--rb);background:var(--rl);padding:5px 10px 6px;border-radius:999px}
body.rytho .mvl em{color:var(--rb);opacity:.7;font-size:10px}
/* rail: flat floating bar, white active pill */
body.rytho #rail .rshape{background:#16171A!important;-webkit-backdrop-filter:none!important;backdrop-filter:none!important}
body.rytho #rail .ch{background:transparent!important;box-shadow:inset 0 0 0 1px rgba(255,255,255,.07)!important}
body.rytho #rail .ch .pg,body.rytho #rail .ch .tr{stroke:transparent!important}
body.rytho #rail .ch span{font:500 11px var(--ur)!important;color:var(--rm)!important}
body.rytho #rail .ch.on{background:var(--rt)!important;box-shadow:none!important}
body.rytho #rail .ch.on span{color:#000!important;font-weight:700!important}
body.rytho .gdot{background:var(--rl)!important;box-shadow:none!important}
body.rytho .rail-line{background:#2A2C31!important}body.rytho .rail-line i{background:var(--rl)!important;box-shadow:none!important}
body.rytho #rail .star{border-color:rgba(255,255,255,.06)!important}
body.rytho #rail .ch::after{background:var(--rt)!important;color:#000!important;font-family:var(--ur);font-weight:600;box-shadow:none!important}
/* segmented controls + chip: solid, white selected pill */
body.rytho #themeT,body.rytho #chooser,body.rytho #chipTitle{background:var(--rc)!important;box-shadow:none!important;-webkit-backdrop-filter:none!important;backdrop-filter:none!important}
body.rytho #themeT button,body.rytho #chooser button{font-family:var(--ur)!important;font-weight:600!important;letter-spacing:.04em!important;color:var(--rm)!important}
body.rytho #themeT button.on,body.rytho #chooser button.on{background:var(--rt)!important;color:#000!important;box-shadow:none!important}
body.rytho #themeT button[data-th=rytho].on{background:var(--rl)!important}
body.rytho #chipTitle b{color:var(--rl)!important}body.rytho #chipTitle span{color:var(--rt)!important;font-family:var(--ur)}
/* explode: white pill button with lime action dot; labels as lime pins */
body.rytho #exBtn{background:var(--rt)!important;box-shadow:none!important;-webkit-backdrop-filter:none!important;backdrop-filter:none!important}
body.rytho #exBtn span{color:#000!important;font-family:var(--ur)!important;font-weight:700!important}
body.rytho #exBtn b{background:var(--rl)!important;color:#000!important}
body.rytho .xl b{display:inline-block!important;font:600 11px var(--ur)!important;letter-spacing:.06em!important;color:#000!important;background:var(--rt);padding:5px 11px 6px;border-radius:999px}
body.rytho .xl.c b{background:var(--rl)!important}
body.rytho .xl span{color:var(--rm)!important;margin-top:6px!important}
/* family lineup: solid cards, first one brand purple, scale bars */
body.rytho #s-family .fam a{background:var(--rc);border-radius:22px;padding:14px 14px 18px;text-align:left!important;transition:background .3s}
body.rytho #s-family .fam a:first-child{background:var(--rp)}
body.rytho #s-family .fam a:hover{background:var(--rc2)}body.rytho #s-family .fam a:first-child:hover{background:#7f4cf0}
body.rytho #s-family .fam a figure img{-webkit-mask:none!important;mask:none!important;border-radius:14px}
body.rytho #s-family .fam b{font:300 26px var(--ur)!important;color:var(--rt)!important;display:inline-block!important;width:34px;height:34px;line-height:32px;text-align:center;border-radius:50%;box-shadow:inset 0 0 0 1px rgba(255,255,255,.35);font-size:14px!important;font-weight:600!important;margin-right:10px!important}
body.rytho #s-family .fam span{font-weight:500!important;color:var(--rt)!important}
body.rytho #s-family .fam em{color:rgba(255,255,255,.55)!important;font-family:var(--ur)!important}
body.rytho #s-family .fam em::after{color:rgba(255,255,255,.75)!important}
.famBar{display:none}
body.rytho .famBar{display:block;height:6px;border-radius:6px;margin:14px 0 4px;background:repeating-linear-gradient(90deg,rgba(255,255,255,.22) 0 2px,transparent 2px 5px)}
body.rytho .famBar u{display:block;text-decoration:none;height:100%;border-radius:6px;background:var(--rt);width:var(--w)}
body.rytho .famBar+small{display:block;font:500 10px var(--ur);color:rgba(255,255,255,.5);letter-spacing:.04em}
.famBar+small{display:none}
body.rytho #s-family .famhero img{border-radius:28px}
/* product pages: stat tiles */
body.rytho .pd-fig.stage img,body.rytho .pd-arch img{-webkit-mask:none!important;mask:none!important;border-radius:28px!important}
body.rytho .pd-facts{gap:10px!important;border:0!important;padding:0!important;display:grid!important;grid-template-columns:repeat(3,1fr)!important}
body.rytho .pd-facts>div{background:var(--rc);border-radius:18px;padding:16px 18px 18px;border:0!important}
body.rytho .pd-facts dt{font:500 11px var(--ur)!important;letter-spacing:.04em!important;color:var(--rm)!important;text-transform:none!important}
body.rytho .pd-facts dd{font:400 17px var(--ur)!important;color:var(--rt)!important;margin-top:8px!important}
body.rytho .pd-facts>div:nth-child(2) dd{color:var(--rl)!important}
body.rytho .pd-miss,body.rytho .missing{color:var(--rm)!important}
body.rytho .pd-miss::before{content:"";display:inline-block;width:6px;height:6px;border-radius:50%;background:var(--rl);margin-right:8px;vertical-align:middle}
body.rytho .missing b{color:var(--rt)!important}
/* swatches */
body.rytho #swatch button.on i{box-shadow:0 0 0 2px var(--rb),0 0 0 3px var(--rt)!important}
body.rytho #swatch button.on span{color:var(--rt)!important}
body.rytho #p04 .pd-fig{border-radius:28px!important}
/* AI: purple + lime blur blobs (palette plate), lime waveform */
body.rytho #s-ai{position:relative;overflow:hidden}
body.rytho #s-ai::before{content:"";position:absolute;left:50%;top:44%;width:min(60vw,760px);aspect-ratio:1;transform:translate(-50%,-50%);border-radius:50%;
 background:radial-gradient(closest-side at 64% 34%,rgba(214,255,101,.95),rgba(214,255,101,0) 70%),radial-gradient(closest-side at 44% 58%,rgba(114,60,232,.95),rgba(114,60,232,0) 85%);filter:blur(40px);opacity:.75;z-index:0}
body.rytho #s-ai .wrap{position:relative;z-index:1}
body.rytho .orb{background:#0E0F12!important;box-shadow:none!important}
body.rytho .orb .wave i{background:var(--rl)!important}
/* partner: alternating solid + lime stage cards */
body.rytho #s-partner .col{background:var(--rc)!important;border-radius:22px!important;box-shadow:none!important;border:0!important}
body.rytho #s-partner .col:nth-child(even){background:var(--rl)!important}
body.rytho #s-partner .col:nth-child(even) h3,body.rytho #s-partner .col:nth-child(even) p,body.rytho #s-partner .col:nth-child(even) .mono{color:#0E0F12!important}
body.rytho #s-partner .col h3{font-weight:500!important;font-size:24px!important}
body.rytho #s-partner .col .mono{font:300 34px/1 var(--ur)!important;letter-spacing:-.02em!important;display:block;margin-bottom:14px}
body.rytho .steps b{display:inline-grid!important;place-items:center;width:30px;height:30px;border-radius:50%;background:var(--rt);color:#000!important;font:600 12px var(--ur)!important}
body.rytho .steps h4{font-weight:500!important}
body.rytho .runhead{border-color:rgba(255,255,255,.06)!important}
/* CTA: white pill, lime action dot */
body.rytho .pill{background:var(--rt)!important;color:#000!important;box-shadow:none!important;font-family:var(--ur)!important;font-weight:600!important}
body.rytho .pill .go{background:var(--rl)!important;color:#000!important}
body.rytho #famScene{box-shadow:0 30px 60px -30px rgba(0,0,0,.9)!important}body.rytho #famScene::after{display:none}
@media(max-width:900px){body.rytho .pd-facts{grid-template-columns:1fr!important}}
'''
t=t.replace('</style>',css+'</style>',1)
# scale bars in lineup (true height share vs 04 tower)
js='''
/* rytho mode: true-height scale bars in the family lineup */
(()=>{const H={p01:180,p02:261,p03:1022,p04:2693};document.querySelectorAll('#s-family .fam a').forEach(a=>{const k=(a.getAttribute('href')||'').slice(1);if(!H[k]||a.querySelector('.famBar'))return;
 const w=Math.max(3,H[k]/H.p04*100);a.insertAdjacentHTML('beforeend',`<div class="famBar"><u style="--w:${w.toFixed(1)}%"></u></div><small>${Math.round(w)}% of full tower height</small>`)})})();
'''
t=t.replace('/* bespoke chooser',js+'/* bespoke chooser',1)
open(p,'w',encoding='utf-8').write(t);print('ok')
