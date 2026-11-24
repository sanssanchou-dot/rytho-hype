p='index.html';t=open(p,encoding='utf-8').read()
# 1 statement section
a=t.index('<section id="s-core">');b=t.index('</section>',a)+10
t=t[:a]+'''<section id="s-core"><div class="core-bg"></div><div class="wrap">
  <p class="say" id="say"></p>
</div></section>'''+t[b:]
t=t.replace("const sentence='玻音先創的透明振膜，讓聲音的源頭，第一次被看見。';","const sentence='玻璃振膜＋透明箱體，\\n讓聲音第一次被看見。';")
t=t.replace("[...sentence].forEach((c,i)=>{const s=document.createElement('span');s.textContent=c;if(i>=2&&i<=8)s.dataset.g=1;say.appendChild(s)});",
 "[...sentence].forEach((c,i)=>{if(c==='\\n'){say.appendChild(document.createElement('br'));return}const s=document.createElement('span');s.textContent=c;if(i===4)s.dataset.g=1;say.appendChild(s)});")
t=t.replace("const ss=[...say.children];","const ss=[...say.querySelectorAll('span')];")
css_core='''
#s-core{min-height:100svh;display:grid;align-items:center;padding:0;overflow:hidden}
.core-bg{position:absolute;inset:0;z-index:-1;background:
 radial-gradient(42% 60% at 78% 50%,rgba(61,46,188,.55),transparent 70%),
 radial-gradient(30% 40% at 70% 62%,rgba(47,191,165,.18),transparent 70%),
 radial-gradient(18% 22% at 76% 44%,rgba(238,242,255,.22),transparent 70%),#000}
.core-bg::after{content:"";position:absolute;inset:0;opacity:.18;mix-blend-mode:overlay;background-image:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='200' height='200'%3E%3Cfilter id='n'%3E%3CfeTurbulence baseFrequency='.85' numOctaves='3'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)'/%3E%3C/svg%3E")}
#s-core .say{font-size:clamp(40px,6.4vw,104px);line-height:1.18;letter-spacing:-.02em}
'''
t=t.replace('</style>',css_core+'</style>',1)
# 2 sidebar replaces header
a=t.index('<header class="glass" id="hdr">');b=t.index('</header>')+9
chap=[('s-film','00','Film'),('s-core','+','Diaphragm'),('s-explode','EX','Explode'),('p01','01','Portable'),('p02','02','Home AI · Upper'),('p03','03','Home AI · Single'),('p04','04','Bespoke'),('s-partner','→','Partner')]
items=''.join(f'<a class="ch{" ai" if c[1] in ("02","03","04") else ""}" href="#{c[0]}" data-id="{c[0]}" data-t="{c[2]}"><svg viewBox="0 0 40 40"><circle class="tr" cx="20" cy="20" r="17"/><circle class="pg" cx="20" cy="20" r="17"/></svg><span>{c[1]}</span></a>' for c in chap)
t=t[:a]+f'''<nav id="rail" class="glass"><a class="star" href="#s-film">✦</a>{items}<div class="rail-line"><i id="railDot"></i></div></nav>
<div id="dial" aria-hidden="true"><div class="arc"></div><div id="dialNums"></div><div class="cur"><b id="dialNum">00</b><span id="dialTitle">Film</span></div></div>'''+t[b:]
css_rail='''
#rail{position:fixed;left:16px;top:50%;transform:translateY(-50%);z-index:40;width:58px;padding:12px 0 14px;border-radius:999px;display:flex;flex-direction:column;align-items:center;gap:6px}
#rail .star{font-size:18px;color:var(--ice);padding:6px 0 10px;border-bottom:1px solid rgba(255,255,255,.12);width:70%;text-align:center;margin-bottom:4px}
#rail .ch{position:relative;width:40px;height:40px;display:grid;place-items:center;border-radius:50%;transition:.3s}
#rail .ch svg{position:absolute;inset:0;transform:rotate(-90deg)}
#rail .ch .tr{fill:none;stroke:rgba(255,255,255,.08);stroke-width:2}
#rail .ch .pg{fill:none;stroke:var(--lime);stroke-width:2;stroke-linecap:round;stroke-dasharray:106.8;stroke-dashoffset:106.8;transition:stroke-dashoffset .2s}
#rail .ch.ai .pg{stroke:#8a7dff}
#rail .ch span{font:600 11px var(--en);color:var(--dim);transition:.3s}
#rail .ch.on{background:rgba(255,255,255,.92);box-shadow:0 0 18px rgba(182,228,103,.35)}
#rail .ch.on span{color:#000}
#rail .ch.on .tr{stroke:transparent}
#rail .ch::after{content:attr(data-t);position:absolute;left:52px;white-space:nowrap;font:500 12px var(--en);color:var(--ice);padding:7px 12px;border-radius:999px;background:rgba(20,20,30,.75);backdrop-filter:blur(10px);opacity:0;transform:translateX(-6px);transition:.25s;pointer-events:none}
#rail .ch:hover::after{opacity:1;transform:none}
.rail-line{width:2px;height:54px;background:rgba(255,255,255,.14);border-radius:2px;margin-top:6px;position:relative}
.rail-line i{position:absolute;left:-3px;width:8px;height:8px;border-radius:50%;background:var(--lime);box-shadow:0 0 10px var(--lime);top:0}
#dial{position:fixed;left:-150px;top:50%;width:300px;height:300px;transform:translateY(-50%);z-index:30;pointer-events:none;opacity:0;transition:opacity .4s}
#dial.show{opacity:1}
#dial .arc{position:absolute;inset:0;border-radius:50%;border:1px solid rgba(238,242,255,.12)}
#dialNums span{position:absolute;left:50%;top:50%;font:600 26px var(--mono);color:rgba(238,242,255,.13);transition:transform .6s cubic-bezier(.2,.7,.1,1),opacity .6s}
#dial .cur{position:absolute;left:168px;top:50%;transform:translateY(-50%);display:flex;align-items:center;gap:14px;white-space:nowrap}
#dial .cur b{font:600 46px var(--mono);letter-spacing:-.04em;color:var(--ice)}
#dial .cur span{font:500 12px var(--en);color:var(--mute);letter-spacing:.06em;max-width:110px;line-height:1.3;white-space:normal}
main,footer{padding-left:84px}
@media(max-width:900px){#rail{left:auto;right:8px;width:46px;padding:8px 0}#rail .ch{width:32px;height:32px}#rail .ch span{font-size:9.5px}#rail .star,.rail-line{display:none}#dial{display:none}main,footer{padding-left:0}}
'''
t=t.replace('</style>',css_rail+'</style>',1)
t=t.replace("const filmFrame=$('#filmFrame'),labs=$$('.lab'),links=$$('header a.l');","const filmFrame=$('#filmFrame'),labs=$$('.lab'),chs=$$('#rail .ch');\nconst dialN=$('#dialNums');chs.forEach((c,i)=>{const s=document.createElement('span');s.textContent=c.querySelector('span').textContent;dialN.appendChild(s)});const dn=[...dialN.children];")
t=t.replace(" $('#prog').style.transform=`scaleX(${y/(document.body.scrollHeight-vh)})`;"," $('#railDot').style.top=(y/(document.body.scrollHeight-vh))*46+'px';")
t=t.replace(" let cur='';$$('main section[id]').forEach(s=>{if(s.getBoundingClientRect().top<vh*.45)cur=s.id});links.forEach(a=>a.classList.toggle('on',a.getAttribute('href')==='#'+cur));",
""" let ci=0;chs.forEach((c,i)=>{const s=document.getElementById(c.dataset.id).getBoundingClientRect();const pr=clamp((vh*.5-s.top)/s.height);c.querySelector('.pg').style.strokeDashoffset=106.8*(1-pr);if(s.top<vh*.5)ci=i});
 chs.forEach((c,i)=>c.classList.toggle('on',i===ci));
 dn.forEach((s,i)=>{const a=(i-ci)*24*Math.PI/180;s.style.transform=`translate(${Math.cos(a)*150-14}px,${Math.sin(a)*150-16}px) rotate(${(i-ci)*24}deg)`;s.style.opacity=i===ci?0:Math.max(0,1-Math.abs(i-ci)*.3)});
 $('#dialNum').textContent=chs[ci].querySelector('span').textContent;$('#dialTitle').textContent=chs[ci].dataset.t;$('#dial').classList.toggle('show',ci>0&&innerWidth>900);""")
open(p,'w',encoding='utf-8').write(t)
for k in ["header a.l","#prog')","links.forEach"]:print(k,k in t)
