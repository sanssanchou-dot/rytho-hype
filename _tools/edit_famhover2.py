p='index.html';t=open(p,encoding='utf-8').read()
s=t.index('/* family hover scene */');e=t.index('/* bespoke chooser',s)
t=t[:s]+'''/* family hover scene: card opens beside the hovered product */
(()=>{const box=$('#famScene'),img=box.querySelector('img'),fam=box.parentElement;
$$('#s-family .fam a').forEach((a,k)=>{a.addEventListener('mouseenter',()=>{fam.classList.add('hov');$$('#s-family .fam a').forEach(x=>x.classList.toggle('cur',x===a));const u=a.dataset.scene;if(!u){box.classList.remove('show');return}
 img.src=u;const fr=fam.getBoundingClientRect(),fg=a.querySelector('figure').getBoundingClientRect(),gi=a.querySelector('figure img').getBoundingClientRect();
 const W=box.offsetWidth,H=box.offsetHeight;const right=k<2;
 let x=right?(gi.right-fr.left+32):(gi.left-fr.left-W-32);x=Math.max(-fr.left+90,Math.min(x,innerWidth-fr.left-W-24));
 let y=fg.bottom-fr.top-H;box.style.left=x+'px';box.style.top=y+'px';box.classList.add('show')});
 a.addEventListener('mouseleave',()=>{box.classList.remove('show');fam.classList.remove('hov')})});})();
'''+t[e:]
t=t.replace('</style>','''
#s-family .fam a{transition:opacity .35s}
#s-family .fam.hov a:not(.cur){opacity:.28}
#s-family .fam em{white-space:nowrap}
'''+'</style>',1)
open(p,'w',encoding='utf-8').write(t);print('ok')
