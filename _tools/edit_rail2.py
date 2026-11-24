p='index.html';t=open(p,encoding='utf-8').read()
a=t.index('<div id="dial"');b=t.index('</div></div>',a)+12
t=t[:a]+'<div id="chipTitle" class="glass"><b id="ctN">00</b><span id="ctT">Film</span></div>'+t[b:]
t=t.replace('#dial{position:fixed;','#dialX{position:fixed;')
t=t.replace('main,footer{padding-left:84px}','''main,footer{padding-left:84px}
#chipTitle{position:fixed;left:84px;top:50%;z-index:39;display:flex;align-items:center;gap:10px;padding:8px 16px 8px 12px;border-radius:999px;opacity:0;transform:translateX(-8px);transition:opacity .35s,transform .35s,top .45s cubic-bezier(.2,.7,.1,1);pointer-events:none}
#chipTitle.show{opacity:1;transform:none}
#chipTitle b{font:600 18px var(--mono);color:var(--lime);letter-spacing:-.02em}
#chipTitle span{font:500 12px var(--en);color:var(--ice);letter-spacing:.06em;white-space:nowrap}''')
t=t.replace('#dial{display:none}main,footer{padding-left:0}}','#chipTitle{display:none}main,footer{padding-left:0}main .wrap{padding-right:62px}}')
t=t.replace("\nconst dialN=$('#dialNums');chs.forEach((c,i)=>{const s=document.createElement('span');s.textContent=c.querySelector('span').textContent;dialN.appendChild(s)});const dn=[...dialN.children];","\nlet lastCi=-1,chipT;")
old=t[t.index(" dn.forEach((s,i)=>"):t.index("innerWidth>900);")+len("innerWidth>900);")]
t=t.replace(old,""" if(ci!==lastCi){lastCi=ci;const r=chs[ci].getBoundingClientRect(),ct=$('#chipTitle');$('#ctN').textContent=chs[ci].querySelector('span').textContent;$('#ctT').textContent=chs[ci].dataset.t;ct.style.top=(r.top+r.height/2-18)+'px';ct.classList.add('show');clearTimeout(chipT);chipT=setTimeout(()=>ct.classList.remove('show'),1800)}""")
open(p,'w',encoding='utf-8').write(t)
print('dial' in t.replace('#dialX',''), 'chipTitle' in t)
