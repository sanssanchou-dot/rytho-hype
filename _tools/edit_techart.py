p='index.html';t=open(p,encoding='utf-8').read()
# font: Doto dot-matrix
t=t.replace('family=Inter+Tight:wght@400;500;600;700&','family=Doto:wght@600;800;900&family=Inter+Tight:wght@400;500;600;700&')
css='''
/* ---- tech art layer ---- */
:root{--dot:'Doto',ui-monospace,monospace}
.num{font-family:var(--dot)!important;font-weight:900!important;color:var(--ice)!important;-webkit-text-stroke:0!important;letter-spacing:-.02em!important;opacity:.9}
.prop .num{background:linear-gradient(180deg,#fff,rgba(238,242,255,.35));-webkit-background-clip:text;background-clip:text;color:transparent!important}
#rail .ch span{font-family:var(--dot);font-weight:900;font-size:13px}
#chipTitle b{font-family:var(--dot);font-weight:900}
.slash{font:500 11px var(--mono);letter-spacing:.22em;color:var(--mute);text-transform:uppercase}
.slash::before{content:"/";margin-right:.3em;color:var(--lime)}
/* aura stage (concentric + grain) */
.stage,.stage.ai-glow{background:
 radial-gradient(circle at 50% 46%,rgba(238,242,255,.16) 0 14%,transparent 14.4%),
 radial-gradient(circle at 50% 46%,rgba(138,156,255,.18) 0 27%,transparent 27.5%),
 radial-gradient(circle at 50% 46%,rgba(61,46,188,.22) 0 41%,transparent 41.5%),
 radial-gradient(circle at 50% 46%,rgba(47,191,165,.10) 0 56%,transparent 56.5%),
 radial-gradient(70% 60% at 50% 46%,#1b1a33,#07070c 75%)!important}
.stage.ai-glow{background:
 radial-gradient(circle at 50% 46%,rgba(182,228,103,.14) 0 14%,transparent 14.4%),
 radial-gradient(circle at 50% 46%,rgba(138,125,255,.22) 0 27%,transparent 27.5%),
 radial-gradient(circle at 50% 46%,rgba(61,46,188,.30) 0 41%,transparent 41.5%),
 radial-gradient(circle at 50% 46%,rgba(61,46,188,.12) 0 56%,transparent 56.5%),
 radial-gradient(70% 60% at 50% 46%,#221a4a,#07070c 75%)!important}
.stage::after{content:"";position:absolute;inset:0;pointer-events:none;opacity:.35;mix-blend-mode:overlay;filter:blur(.6px);
 background-image:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='220' height='220'%3E%3Cfilter id='n'%3E%3CfeTurbulence baseFrequency='.9' numOctaves='3' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)'/%3E%3C/svg%3E")}
/* HUD brackets (ref: gallery presents) */
.hud{position:absolute;inset:0;pointer-events:none;z-index:3}
.hud i{position:absolute;width:22px;height:22px;border:1.2px solid rgba(238,242,255,.85);display:grid;place-items:center;font:italic 500 11px var(--mono);color:#fff;opacity:0;transition:opacity .25s}
.hud i.on{opacity:1}
.hud i.g{border-color:var(--lime);color:var(--lime)}
.hud .scan{position:absolute;left:6%;right:6%;height:1px;background:linear-gradient(90deg,transparent,var(--lime),transparent);box-shadow:0 0 12px var(--lime);opacity:.0;top:10%}
.stage:hover .hud .scan{opacity:.8;animation:scan 2.4s linear infinite}
@keyframes scan{from{top:8%}to{top:92%}}
/* explode: node-line diagram labels (ref: PlayerZero) */
.lab{background:none!important;box-shadow:none!important;backdrop-filter:none!important;padding:0!important;display:flex;align-items:center;gap:0;max-width:none}
.lab .tg{font:500 11px var(--mono);letter-spacing:.06em;padding:6px 12px;border-radius:999px;border:1px solid rgba(238,242,255,.35);background:rgba(10,10,18,.6);white-space:nowrap}
.lab .ln{height:1px;width:clamp(40px,8vw,140px);background:linear-gradient(90deg,rgba(238,242,255,.4),rgba(182,228,103,.9));position:relative}
.lab .ln::after{content:"";position:absolute;right:-4px;top:-3.5px;width:8px;height:8px;border-radius:50%;background:var(--ice)}
.ex-labels.r .lab .ln{background:linear-gradient(270deg,rgba(238,242,255,.4),rgba(182,228,103,.9))}
.ex-labels.r .lab .ln::after{right:auto;left:-4px}
.lab.on .tg{border-color:var(--lime);color:var(--lime);box-shadow:0 0 16px rgba(182,228,103,.25)}
.lab b,.lab span.d{display:none}
.lab .sub{display:block;font:400 11px var(--zh);color:var(--dim);margin-top:4px;white-space:nowrap}
.ex-labels{gap:30px}
/* halftone dot field behind explode */
#s-explode .pin::before{content:"";position:absolute;inset:8% 20%;pointer-events:none;opacity:.25;
 background-image:radial-gradient(circle,rgba(238,242,255,.9) 1px,transparent 1.6px);background-size:9px 9px;
 -webkit-mask:radial-gradient(45% 50% at 50% 50%,#000 20%,transparent 70%);mask:radial-gradient(45% 50% at 50% 50%,#000 20%,transparent 70%)}
'''
t=t.replace('</style>',css+'</style>',1)
# rebuild labels
import re
def lab(m):
    at,b,s=m.group(1),m.group(2),m.group(3)
    return f'<div class="lab" data-at="{at}"><div><span class="tg">{b}</span><span class="sub">{s}</span></div><span class="ln"></span></div>'
def labR(m):
    at,b,s=m.group(1),m.group(2),m.group(3)
    return f'<div class="lab" data-at="{at}"><span class="ln"></span><div style="text-align:right"><span class="tg">{b}</span><span class="sub">{s}</span></div></div>'
L=t.index('id="labL"');R=t.index('id="labR"');E=t.index('class="ex-foot"')
pat=r'<div class="lab glass" data-at="([^"]+)"><b>([^<]+)</b><span>([^<]+)</span></div>'
t=t[:L]+re.sub(pat,lab,t[L:R])+t[R:]
R=t.index('id="labR"');E=t.index('class="ex-foot"')
t=t[:R]+re.sub(pat,labR,t[R:E])+t[E:]
# slash labels on proposals: replace runhead mono with slash
t=t.replace('<span class="mono">01 / Portable</span>','<span class="slash">01 Portable / Bluetooth</span>')
t=t.replace('<span class="mono">02 / Home AI · Upper Two</span>','<span class="slash">02 Home AI / Upper Two</span>')
t=t.replace('<span class="mono">03 / Home AI · Single</span>','<span class="slash">03 Home AI / Single</span>')
t=t.replace('<span class="mono">04 / Bespoke · Full Set</span>','<span class="slash">04 Bespoke / Full Set</span>')
# HUD into stages + JS
t=t.replace('<div class="stage ','<div class="stage hudded ')
js='''
/* HUD brackets */
const HC='!?2Hai9S~b;Z0x#+'.split('');
$$('.stage').forEach(st=>{const h=document.createElement('div');h.className='hud';h.innerHTML='<div class="scan"></div>';st.appendChild(h);
 const pts=[];for(let i=0;i<14;i++){const a=Math.random()*6.283,r=.30+Math.random()*.16;const e=document.createElement('i');e.style.left=(50+Math.cos(a)*r*100*.9)+'%';e.style.top=(46+Math.sin(a)*r*100)+'%';e.textContent=HC[i%HC.length];if(Math.random()<.18)e.classList.add('g');h.appendChild(e);pts.push(e)}
 let live=false;new IntersectionObserver(es=>es.forEach(en=>live=en.isIntersecting),{threshold:.3}).observe(st);
 setInterval(()=>{if(!live)return;pts.forEach(e=>{if(Math.random()<.22){e.classList.toggle('on');e.textContent=HC[Math.random()*HC.length|0]}})},260)});
'''
t=t.replace('/* bespoke chooser */',js+'/* bespoke chooser */')
open(p,'w',encoding='utf-8').write(t)
print(t.count('class="lab"'),t.count('class="stage hudded'))
