p='index.html';t=open(p,encoding='utf-8').read()
# star -> green dot
t=t.replace('<a class="star" href="#s-film">✦</a>','<a class="star" href="#s-film"><i class="gdot"></i></a>')
# plus not green in statement
t=t.replace("if(i===4)s.dataset.g=1;","")
# bespoke chooser: add Codex styles
old=t[t.index('<div class="seg2 rv" id="chooser">'):t.index('</div>',t.index('<div class="seg2 rv" id="chooser">'))+6]
opts=[('Ring','img/ring.webp'),('Branch','img/branch.webp'),('Fold','img/fold.webp'),('Panel','img/b_style_01_carpanel.webp'),('Fin','img/b_style_02_aluminium_fins.webp'),('Blade','img/b_style_03_brutalist_blades.webp'),('Pore','img/b_style_04_metabolist_tubes.webp'),('Panel×Fin','img/b_mix_12_panel_fins.webp'),('Fin×Blade','img/b_mix_23_fins_blades.webp'),('Blade×Pore','img/b_mix_34_blades_tubes.webp'),('Panel×Pore','img/b_mix_14_panel_tubes.webp')]
new='<div class="seg2 rv" id="chooser">'+''.join(f'<button{" class=\"on\"" if i==0 else ""} data-img="{u}" data-ai="{1 if i>2 else 0}">{n}</button>' for i,(n,u) in enumerate(opts))+'</div><p class="pd-miss" id="bodyNote" style="color:var(--dim)">Ring／Branch／Fold：原網格渲染</p>'
t=t.replace(old,new)
t=t.replace("const im=$('#bodyImg');im.style.opacity=0;setTimeout(()=>{im.src=b.dataset.img;im.style.opacity=1},220)});",
 "const im=$('#bodyImg');im.style.opacity=0;setTimeout(()=>{im.src=b.dataset.img;im.style.opacity=1},220);$('#bodyNote').textContent=b.dataset.ai==='1'?'AI 概念圖（Codex）· 單體與箱體依原配置，主體待 CAD':'Ring／Branch／Fold：原網格渲染'});")
css='''
/* ---- rail v3: black glass tab growing from the left edge ---- */
#rail{left:0!important;width:64px!important;padding:16px 0 18px!important;border-radius:0 26px 26px 0!important;
 background:linear-gradient(180deg,rgba(18,18,22,.86),rgba(6,6,9,.92))!important;-webkit-backdrop-filter:blur(24px) saturate(160%);backdrop-filter:blur(24px) saturate(160%);
 box-shadow:inset -1px 0 0 rgba(255,255,255,.10),inset 0 1px 0 rgba(255,255,255,.14),inset 0 -1px 0 rgba(255,255,255,.05),12px 0 40px -16px rgba(0,0,0,.8)!important}
#rail::before,#rail::after{content:"";position:absolute;left:0;width:26px;height:26px;pointer-events:none;background:radial-gradient(circle at 100% 0,transparent 25px,rgba(10,10,14,.9) 26px)}
#rail::before{top:-26px;background:radial-gradient(circle at 100% 0,transparent 25.5px,rgba(16,16,20,.88) 26px);transform:scaleY(-1)}
#rail::after{bottom:-26px;background:radial-gradient(circle at 100% 100%,transparent 25.5px,rgba(8,8,11,.92) 26px);transform:scaleY(-1)}
#rail .star{border-bottom:1px solid rgba(255,255,255,.08)!important;padding:4px 0 14px!important}
.gdot{display:block;width:9px;height:9px;border-radius:50%;margin:0 auto;background:#B6E467;box-shadow:0 0 10px rgba(182,228,103,.8)}
#rail .ch .pg{stroke:rgba(238,242,255,.75)!important}
#rail .ch.ai .pg{stroke:#8a7dff!important}
#rail .ch.on{background:#EEF2FF!important;box-shadow:none!important}
#rail .ch.on span{color:#000!important}
#rail .ch span{color:rgba(238,242,255,.45)!important}
.rail-line i{background:#EEF2FF!important;box-shadow:none!important}
body.light #rail{background:linear-gradient(180deg,rgba(18,18,22,.9),rgba(6,6,9,.94))!important}
body.light #rail .ch.on{background:#EEF2FF!important}
body.light #rail .ch.on span{color:#000!important}
main,footer{padding-left:76px!important}
#chipTitle{left:74px!important}
@media(max-width:900px){#rail{left:auto!important;right:0!important;border-radius:22px 0 0 22px!important;width:48px!important}#rail::before,#rail::after{display:none}main,footer{padding-left:0!important}}
/* ---- background: scattered glows (green top-left, indigo bottom-right, teal mid) ---- */
#flow{display:none!important}
#glowFloor{inset:0!important;height:auto!important;-webkit-mask-image:none!important;mask-image:none!important;
 background:
  radial-gradient(34vw 30vw at 4% 2%,rgba(182,228,103,.20),transparent 70%),
  radial-gradient(46vw 40vw at 100% 104%,rgba(61,46,188,.55),transparent 70%),
  radial-gradient(28vw 24vw at 92% 18%,rgba(47,191,165,.10),transparent 70%),
  radial-gradient(30vw 26vw at 8% 92%,rgba(61,46,188,.22),transparent 70%)!important;
 animation:drift2 26s ease-in-out infinite alternate}
@keyframes drift2{to{background-position:3vw 2vw,-3vw -2vw,-2vw 3vw,2vw -2vw}}
body.light #glowFloor{opacity:.7!important}
.say span.lit.g{color:inherit!important}
'''
t=t.replace('</style>',css+'</style>',1)
open(p,'w',encoding='utf-8').write(t)
print(t.count('data-ai='),'gdot' in t)
