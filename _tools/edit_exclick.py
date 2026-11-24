p='index.html';t=open(p,encoding='utf-8').read()
old=""" const e=$('#s-explode'),er=e.getBoundingClientRect();const ep=clamp(-er.top/(er.height-vh));
 drawExplode(clamp((ep-.05)/.6));$('#exPct').textContent=String(Math.round(ep*100)).padStart(3,'0');
 $('#exLabs').classList.toggle('on',ep>.08);"""
assert old in t
t=t.replace(old," const e=$('#s-explode'),er=e.getBoundingClientRect();const ep=window.exP||0;")
# button
t=t.replace('<div class="ex-foot"><p class="missing" id="exMissing">','<button id="exBtn" type="button" aria-pressed="false"><span>Explode</span><b>+</b></button>\n    <div class="ex-foot"><p class="missing" id="exMissing">',1)
t=t.replace("['#themeT','#chooser','#chipTitle','.pill','#rail','.seg2']","['#themeT','#chooser','#chipTitle','.pill','#rail','.seg2','#exBtn']")
js='''
/* explode: click to open / close (no scroll scrub) */
(()=>{let p=0,target=0,from=0,t0=0;const D=1700,btn=$('#exBtn');window.exP=0;
const ease=x=>x<.5?4*x*x*x:1-Math.pow(-2*x+2,3)/2;
function tick(T){if(!t0)t0=T;const k=Math.min(1,(T-t0)/D);p=from+(target-from)*ease(k);window.exP=p;drawExplode(p);
 $('#exPct').textContent=String(Math.round(p*100)).padStart(3,'0');$('#exLabs').classList.toggle('on',p>.7);
 if(k<1)requestAnimationFrame(tick)}
btn.addEventListener('click',()=>{from=p;target=target?0:1;t0=0;btn.setAttribute('aria-pressed',target?'true':'false');
 btn.querySelector('span').textContent=target?'Assemble':'Explode';btn.classList.toggle('open',!!target);requestAnimationFrame(tick)});
addEventListener('resize',()=>drawExplode(p));
const f0=setInterval(()=>{if(frames[0]&&frames[0].complete&&frames[0].naturalWidth){drawExplode(p);clearInterval(f0)}},120)})();
'''
t=t.replace('/* bespoke chooser */',js+'/* bespoke chooser */',1)
css='''
/* explode = one screen, click to open */
#s-explode{height:100svh!important}
#s-explode .pin{position:relative!important}
#exBtn{position:absolute;left:50%;bottom:6.5vh;transform:translateX(-50%);z-index:5;display:flex;align-items:center;gap:14px;height:48px;padding:0 8px 0 24px;border-radius:999px;border:0;cursor:pointer;
 font:500 13px var(--mono);letter-spacing:.16em;text-transform:uppercase;color:var(--acc);isolation:isolate;
 background:linear-gradient(180deg,rgba(255,255,255,.07),rgba(255,255,255,.015) 60%,rgba(0,0,0,.25));-webkit-backdrop-filter:blur(26px) saturate(140%);backdrop-filter:blur(26px) saturate(140%);box-shadow:0 20px 40px -20px rgba(0,0,0,.8)}
#exBtn b{width:34px;height:34px;border-radius:50%;display:grid;place-items:center;font:300 20px var(--en);color:#0B0B12;background:var(--acc);transition:transform .5s cubic-bezier(.6,0,.2,1)}
#exBtn.open b{transform:rotate(45deg)}
#exBtn:hover b{box-shadow:0 0 16px rgba(198,244,50,.55)}
body.light #exBtn{background:linear-gradient(180deg,rgba(255,255,255,.95),rgba(240,242,236,.7));color:#4a7410}
/* rail edge in light theme */
body.light #rEdgeG stop:nth-child(3){stop-color:rgba(0,0,0,.10)}
body.light #rEdgeG stop:nth-child(4){stop-color:rgba(0,0,0,.16)}
body.light #rEdgeG stop:nth-child(5){stop-color:rgba(0,0,0,.08)}
body.light #rEdgeG stop:nth-child(1){stop-color:#8fc000}
'''
t=t.replace('</style>',css+'</style>',1)
open(p,'w',encoding='utf-8').write(t);print('ok')
