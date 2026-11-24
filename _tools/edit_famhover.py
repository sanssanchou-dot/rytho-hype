p='index.html';t=open(p,encoding='utf-8').read()
t=t.replace('<a href="#p01"><figure>','<a href="#p01" data-scene="img/p01_dark.webp"><figure>',1)
t=t.replace('<a href="#p03"><figure>','<a href="#p03" data-scene="img/scene_03_wide.webp"><figure>',1)
i=t.index('<a href="#p04"><figure>');j=t.index('</a>',i)+4;t=t[:j]+'<div id="famScene"><img alt=""></div>'+t[j:]
css='''
/* family lineup: wider, bigger type, hover scene card */
#s-family .fam{max-width:min(94vw,2200px)!important;gap:5vw!important;position:relative}
#s-family .fam b{font-size:20px!important;margin-right:10px}
#s-family .fam span{font-size:19px!important;font-weight:600!important}
#s-family .fam em{font-size:12.5px!important;margin-top:10px!important;letter-spacing:.1em}
#famScene{position:absolute;z-index:6;width:min(40vw,720px);aspect-ratio:16/9;border-radius:22px;overflow:hidden;pointer-events:none;opacity:0;transform:translateY(12px) scale(.98);
 transition:opacity .35s,transform .45s cubic-bezier(.2,.7,.1,1);box-shadow:0 40px 80px -30px rgba(0,0,0,.9),inset 0 0 0 1px rgba(255,255,255,.14)}
#famScene.show{opacity:1;transform:none}
#famScene img{width:100%;height:100%;object-fit:cover;display:block}
#famScene::after{content:"";position:absolute;inset:0;border-radius:inherit;padding:1px;background:conic-gradient(from var(--la),#C6F432,rgba(198,244,50,.3) 30deg,rgba(255,255,255,.08) 90deg,rgba(255,255,255,.25) 190deg,rgba(255,255,255,.06) 260deg,rgba(198,244,50,.3) 330deg,#C6F432);
 -webkit-mask:linear-gradient(#000 0 0) content-box,linear-gradient(#000 0 0);-webkit-mask-composite:xor;mask-composite:exclude;opacity:var(--lb)}
@media(hover:none),(max-width:900px){#famScene{display:none}}
'''
t=t.replace('</style>',css+'</style>',1)
js='''
/* family hover scene */
(()=>{const box=$('#famScene'),img=box.querySelector('img'),fam=box.parentElement;
$$('#s-family .fam a').forEach(a=>{a.addEventListener('mouseenter',()=>{const u=a.dataset.scene;if(!u){box.classList.remove('show');return}
 img.src=u;const fr=fam.getBoundingClientRect(),fg=a.querySelector('figure img').getBoundingClientRect(),ar=a.getBoundingClientRect();
 const W=box.offsetWidth,H=box.offsetHeight;let x=ar.left+ar.width/2-fr.left-W/2;x=Math.max(-fr.left+90,Math.min(x,innerWidth-fr.left-W-24));
 let y=fg.top-fr.top-H-20;if(fg.top-H-20<70)y=Math.max(70-fr.top,y);box.style.left=x+'px';box.style.top=y+'px';box.classList.add('show')});
 a.addEventListener('mouseleave',()=>box.classList.remove('show'))});})();
'''
t=t.replace('/* bespoke chooser',js+'/* bespoke chooser',1)
open(p,'w',encoding='utf-8').write(t);print('ok')
