p='index.html';t=open(p,encoding='utf-8').read()
# button inside the hero
t=t.replace('<video id="heroB" class="hv" src="img/hero_v3.mp4" muted playsinline preload="auto"></video></div>',
 '<video id="heroB" class="hv" src="img/hero_v3.mp4" muted playsinline preload="auto"></video></div><button id="sndBtn" type="button" aria-pressed="false" aria-label="Sound on"><span class="eq"><i></i><i></i><i></i><i></i></span><em>SOUND</em></button>',1)
# replace hero loop logic with audio-aware version
s=t.index('/* hero: one continuous film, seamless loop');e=t.index('requestAnimationFrame(tick)})();',s)+len('requestAnimationFrame(tick)})();')
t=t[:s]+'''/* hero: one continuous film, seamless loop by cross-fading two players (picture AND sound), sound opt-in */
(()=>{const A=document.getElementById('heroA'),B=document.getElementById('heroB'),btn=document.getElementById('sndBtn'),hero=document.getElementById('s-film');
let cur=A,nxt=B,xf=0,xfStart=0,sound=false;const XF=1.2;
function vis(){const r=hero.getBoundingClientRect();return Math.max(0,Math.min(1,(r.bottom-innerHeight*.15)/(innerHeight*.85)))}
function setVol(){const g=sound?vis():0;const k=xf?Math.min(1,(performance.now()-xfStart)/(XF*1000)):1;
 cur.volume=Math.max(0,Math.min(1,g*(xf?(1-k):1)));nxt.volume=Math.max(0,Math.min(1,g*(xf?k:0)))}
function tick(){if(!xf&&cur.duration&&cur.currentTime>cur.duration-XF){xf=1;xfStart=performance.now();nxt.currentTime=0;nxt.muted=!sound;nxt.volume=0;nxt.play().catch(()=>{});nxt.classList.add('on');cur.classList.remove('on');
  setTimeout(()=>{cur.pause();const t=cur;cur=nxt;nxt=t;xf=0},XF*1000+80)}
 setVol();requestAnimationFrame(tick)}
btn.addEventListener('click',()=>{sound=!sound;cur.muted=!sound;nxt.muted=!sound||!xf;if(sound&&cur.paused)cur.play().catch(()=>{});
 btn.classList.toggle('on',sound);btn.setAttribute('aria-pressed',sound);btn.setAttribute('aria-label',sound?'Sound off':'Sound on');btn.querySelector('em').textContent=sound?'SOUND ON':'SOUND'});
A.play().catch(()=>{});requestAnimationFrame(tick)})();'''+t[e:]
css='''
/* hero sound toggle (glass, green breathing light when on) */
#sndBtn{position:absolute;right:28px;bottom:28px;z-index:5;display:flex;align-items:center;gap:10px;height:43px;padding:0 18px 0 14px;border:0;border-radius:999px;cursor:pointer;isolation:isolate;
 font:600 12px var(--en);letter-spacing:.08em;color:var(--t2,rgba(242,243,245,.62));background:rgba(255,255,255,.04)}
#sndBtn em{font-style:normal}
#sndBtn .eq{display:flex;align-items:flex-end;gap:2px;height:14px}
#sndBtn .eq i{display:block;width:2px;height:3px;border-radius:2px;background:currentColor;transition:height .3s}
#sndBtn.on{color:var(--acc)}
#sndBtn.on .eq i{animation:eqb 1s ease-in-out infinite}
#sndBtn.on .eq i:nth-child(2){animation-delay:-.3s}#sndBtn.on .eq i:nth-child(3){animation-delay:-.6s}#sndBtn.on .eq i:nth-child(4){animation-delay:-.15s}
@keyframes eqb{0%,100%{height:3px}50%{height:14px}}
body.light #sndBtn.on{color:#6f9a00}
body.rytho #sndBtn{font-family:var(--ur)}
@media(max-width:600px){#sndBtn{right:16px;bottom:16px}}
'''
t=t.replace('</style>',css+'</style>',1)
open(p,'w',encoding='utf-8').write(t);print('ok')
