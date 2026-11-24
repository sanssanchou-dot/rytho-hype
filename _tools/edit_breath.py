p='index.html';t=open(p,encoding='utf-8').read()
old="addEventListener('scroll',()=>document.documentElement.style.setProperty('--la',(-45+scrollY*.12)%360+'deg'),{passive:true});document.documentElement.style.setProperty('--la','-45deg');"
assert old in t; t=t.replace(old,'')
t=t.replace("addEventListener('resize',build);addEventListener('scroll',spin,{passive:true});","addEventListener('resize',build);")
t=t.replace("function spin(){const T=H+2*R,a=(-45+scrollY*.12)*Math.PI/180,","function spin(){const T=H+2*R,a=(window.__la||-45)*Math.PI/180,")
js='''
/* breathing key light: slow loop, independent of scroll */
(()=>{const st=document.documentElement.style;function f(T){const s=T/1000;
 const a=-45+80*Math.sin(s*2*Math.PI/9)+25*Math.sin(s*2*Math.PI/23);window.__la=a;st.setProperty('--la',a+'deg');
 st.setProperty('--lb',(.72+.28*(.5+.5*Math.sin(s*2*Math.PI/4.5))).toFixed(3));
 const r=document.querySelector('#rail .redge');if(r&&r.__spin)r.__spin();requestAnimationFrame(f)}requestAnimationFrame(f)})();
'''
t=t.replace("if(document.fonts)document.fonts.ready.then(build);build()})();","sv.__spin=spin;if(document.fonts)document.fonts.ready.then(build);build()})();"+js,1)
t=t.replace('</style>','''
:root{--lb:1}.lgrim.a{opacity:var(--lb)!important}#rail .redge{opacity:var(--lb)}
'''+'</style>',1)
open(p,'w',encoding='utf-8').write(t);print('__la' in t)
