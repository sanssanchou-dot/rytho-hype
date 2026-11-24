p='index.html';t=open(p,encoding='utf-8').read()
css='''
/* ---- theme toggle ---- */
#themeT{position:fixed;top:16px;right:16px;z-index:45;display:flex;padding:5px;border-radius:999px;gap:4px}
#themeT button{all:unset;cursor:pointer;font:600 12px var(--en);letter-spacing:.08em;padding:9px 16px;border-radius:999px;color:var(--mute);transition:.3s}
#themeT button.on{background:var(--ice);color:#000;box-shadow:inset 0 1px 0 #fff,0 6px 16px -8px rgba(0,0,0,.6)}
body,main,section{transition:background-color .5s,color .5s}
/* LIGHT */
body.light{--ice:#0B0B12;--mute:rgba(11,11,18,.62);--dim:rgba(11,11,18,.42);background:#F2F3ED;color:#0B0B12}
html:has(body.light){background:#F2F3ED}
body.light #flow{opacity:.45;mix-blend-mode:multiply}
body.light .glass{background:linear-gradient(180deg,rgba(255,255,255,.7),rgba(255,255,255,.35));box-shadow:inset 0 0 0 1px rgba(255,255,255,.9),inset 0 1px 0 #fff,inset 0 -1px 0 rgba(61,46,188,.08),0 24px 50px -28px rgba(30,30,60,.35)}
body.light #themeT button.on,body.light #rail .ch.on{background:#0B0B12;color:#fff}
body.light #rail .ch.on span{color:#fff}
body.light #rail .ch .tr{stroke:rgba(0,0,0,.08)}
body.light #rail .ch .pg{stroke:#6c9a1f}
body.light #rail .ch.ai .pg{stroke:#3D2EBC}
body.light .dot,body.light .say span.lit.g,body.light .slash::before,body.light #chipTitle b{color:#5e8f12}
body.light .say span{color:rgba(11,11,18,.12)}
body.light .say span.lit{color:#0B0B12}
body.light .core-bg{background:radial-gradient(42% 60% at 78% 50%,rgba(61,46,188,.22),transparent 70%),radial-gradient(30% 40% at 70% 62%,rgba(47,191,165,.16),transparent 70%),radial-gradient(18% 22% at 76% 44%,rgba(182,228,103,.25),transparent 70%),#F2F3ED}
body.light .stage,body.light .stage.ai-glow{background:
 radial-gradient(circle at 50% 46%,rgba(255,255,255,.9) 0 14%,transparent 14.4%),
 radial-gradient(circle at 50% 46%,rgba(214,220,240,.9) 0 27%,transparent 27.5%),
 radial-gradient(circle at 50% 46%,rgba(190,198,228,.6) 0 41%,transparent 41.5%),
 radial-gradient(circle at 50% 46%,rgba(172,219,184,.35) 0 56%,transparent 56.5%),
 radial-gradient(70% 60% at 50% 46%,#e9ebf1,#d6d9e1 75%)!important}
body.light .stage.ai-glow{background:
 radial-gradient(circle at 50% 46%,rgba(255,255,255,.9) 0 14%,transparent 14.4%),
 radial-gradient(circle at 50% 46%,rgba(206,200,255,.85) 0 27%,transparent 27.5%),
 radial-gradient(circle at 50% 46%,rgba(150,138,240,.45) 0 41%,transparent 41.5%),
 radial-gradient(circle at 50% 46%,rgba(182,228,103,.25) 0 56%,transparent 56.5%),
 radial-gradient(70% 60% at 50% 46%,#ecebf7,#d8d6ea 75%)!important}
body.light .stage img{filter:drop-shadow(0 36px 36px rgba(30,30,60,.3))}
body.light .hud i{border-color:rgba(11,11,18,.7);color:#0B0B12}
body.light .hud i.g{border-color:#5e8f12;color:#5e8f12}
body.light .prop .num{background:linear-gradient(180deg,#0B0B12,rgba(11,11,18,.25));-webkit-background-clip:text;background-clip:text}
body.light .film-frame{box-shadow:0 40px 80px -40px rgba(30,30,60,.5)}
body.light .lab .tg{background:rgba(255,255,255,.7);border-color:rgba(11,11,18,.25)}
body.light .lab.on .tg{border-color:#5e8f12;color:#4a7410}
body.light .lab .ln{background:linear-gradient(90deg,rgba(11,11,18,.3),#6c9a1f)}
body.light .ex-labels.r .lab .ln{background:linear-gradient(270deg,rgba(11,11,18,.3),#6c9a1f)}
body.light .lab .ln::after{background:#0B0B12}
body.light #s-explode .pin::before{background-image:radial-gradient(circle,rgba(11,11,18,.8) 1px,transparent 1.6px)}
body.light .badge.ai{color:#fff}
body.light .pill{color:#0B0B12;background:linear-gradient(90deg,rgba(61,46,188,.14),rgba(47,191,165,.14) 70%,rgba(182,228,103,.2));box-shadow:inset 0 0 0 1px rgba(61,46,188,.25),inset 0 1px 0 #fff,0 0 30px rgba(61,46,188,.18)}
body.light .pill i{background:#0B0B12}
body.light .bev{color:#0B0B12;background:linear-gradient(180deg,rgba(255,255,255,.9),rgba(255,255,255,.45));box-shadow:inset 0 0 0 1.2px rgba(11,11,18,.15),inset 0 2px 1px -1px #fff,inset 0 -5px 9px rgba(0,0,0,.06),0 12px 24px -14px rgba(30,30,60,.5)}
body.light .bev.on{box-shadow:inset 0 0 0 1.5px #6c9a1f,inset 0 2px 1px -1px #fff,0 0 18px rgba(108,154,31,.25)}
body.light .orb{background:radial-gradient(90% 120% at 50% 110%,rgba(255,255,255,.6),transparent 55%),radial-gradient(100% 100% at 50% 0%,#e8e9f2,#cfd2de 70%);box-shadow:inset 0 0 0 1.5px #fff,inset 0 2px 18px rgba(255,255,255,.8),0 0 60px rgba(61,46,188,.2)}
body.light .orb .st{mix-blend-mode:multiply}
body.light .runhead{border-color:rgba(11,11,18,.14)}
body.light footer .wrap,body.light .steps{border-color:rgba(11,11,18,.14)}
body.light .missing{color:rgba(11,11,18,.5)}
body.light .missing b{color:#b06a00}
body.light .spec div{border-color:rgba(11,11,18,.08)}
body.light #s-cta .pill .go,body.light .pill .go{color:#0B0B12}
'''
t=t.replace('</style>',css+'</style>',1)
t=t.replace('<div id="bg">','<div id="themeT" class="glass"><button data-th="dark" class="on">DARK</button><button data-th="light">LIGHT</button></div>\n<div id="bg">',1)
# canvas colours by theme
t=t.replace("let mode={spread:0,ai:0,thin:1};","let mode={spread:0,ai:0,thin:1};const isLight=()=>document.body.classList.contains('light');")
t=t.replace("const c=cur.ai>.5?[mix(236,61,g*cur.ai),mix(242,46,g*cur.ai),mix(255,188,g*cur.ai)]:[mix(236,61,g),mix(242,46,g),255];",
 "let c=cur.ai>.5?[mix(236,61,g*cur.ai),mix(242,46,g*cur.ai),mix(255,188,g*cur.ai)]:[mix(236,61,g),mix(242,46,g),255];if(isLight())c=[mix(20,61,g),mix(22,46,g),mix(40,188,g)];")
js='''
/* theme */
function setTheme(th){document.body.classList.toggle('light',th==='light');$$('#themeT button').forEach(b=>b.classList.toggle('on',b.dataset.th===th));try{localStorage.setItem('rh-theme',th)}catch(e){}}
$$('#themeT button').forEach(b=>b.onclick=()=>setTheme(b.dataset.th));
setTheme(new URLSearchParams(location.search).get('theme')||(()=>{try{return localStorage.getItem('rh-theme')}catch(e){}})()||'dark');
'''
t=t.replace('/* bespoke chooser */',js+'/* bespoke chooser */')
open(p,'w',encoding='utf-8').write(t)
print('ok')
