p='index.html';t=open(p,encoding='utf-8').read()
a=t.index('<div class="seg2 rv" id="chooser">');b=t.index('</p>',a)+4
t=t[:a]+'''<div class="seg2 rv" id="chooser"><button class="on" data-body="orig">Original</button><button data-body="fin">Fin</button><button data-body="hifi">Hi-Fi</button></div>
  <div id="swatch" class="rv"></div>
  <p class="pd-miss" id="bodyNote" style="color:var(--dim)">原版主體 · 原模型渲染</p>'''+t[b:]
s=t.index('/* bespoke chooser */');e=t.index('</script>',s)
t=t[:s]+'''/* bespoke chooser: body + colour */
(()=>{const B={orig:{note:'原版主體 · 原模型渲染',c:[['原版','#2a2c30','img/b_original.webp']]},
 fin:{note:'Fin 主體 · AI 概念圖，已對齊原版單體位置 · 待 CAD',c:[['鋁本色','linear-gradient(135deg,#f2f3f5,#a9adb3)','img/r3_style_02_aluminium_fins.webp'],['黑色陽極','#16171a','img/fin_black_anodized.webp'],['香檳金','#d8c2a0','img/fin_champagne.webp'],['石墨灰','#7d8187','img/fin_graphite.webp'],['白陶瓷','#f7f7f4','img/fin_white_ceramic.webp'],['萊姆細線','conic-gradient(#C6F432 0 25%,#d9dbdf 0)','img/fin_rytho_lime.webp'],['古銅','#b06a3e','img/fin_bronze.webp']]},
 hifi:{note:'Hi-Fi 主體 · AI 概念圖，已對齊原版單體位置 · 待 CAD',c:[['胡桃木＋緞黑','linear-gradient(135deg,#6b4429 50%,#1b1b1d 50%)','img/hifi_walnut.webp'],['柚木＋拉絲鋁','linear-gradient(135deg,#c8955c 50%,#c9ccd0 50%)','img/hifi_teak_alu.webp'],['鋼琴黑＋大理石','linear-gradient(135deg,#0b0b0d 50%,#e7e5e0 50%)','img/hifi_piano_marble.webp']]}};
const im=$('#bodyImg'),sw=$('#swatch');
function show(u){if(im.getAttribute('src')===u)return;im.style.opacity=0;setTimeout(()=>{im.src=u;im.style.opacity=1},200)}
function body(k){$$('#chooser button').forEach(x=>x.classList.toggle('on',x.dataset.body===k));const d=B[k];$('#bodyNote').textContent=d.note;
 sw.innerHTML=d.c.length>1?d.c.map((c,i)=>`<button class="${i?'':'on'}" data-u="${c[2]}" title="${c[0]}" style="--c:${c[1]}"><i></i><span>${c[0]}</span></button>`).join(''):'';
 $$('#swatch button').forEach(x=>x.onclick=()=>{$$('#swatch button').forEach(y=>y.classList.toggle('on',y===x));show(x.dataset.u)});show(d.c[0][2])}
Object.values(B).forEach(v=>v.c.forEach(c=>{const p=new Image();p.src=c[2]}));
$$('#chooser button').forEach(b=>b.onclick=()=>body(b.dataset.body));})();
'''+t[e:]
t=t.replace('<figure class="pd-fig rv"><img src="img/portable_cut.webp" alt="隨身"></figure>','<figure class="pd-fig rv p01fig"><img class="th-d" src="img/p01_dark.webp" alt="隨身"><img class="th-l" src="img/p01_light.webp" alt="隨身"></figure>')
i=t.index('id="p03"');j=t.index('</dl>',i)+5
t=t[:j]+'''
  <figure class="pd-scene rv"><img src="img/scene_03_wide.webp" alt="03 北歐客廳情境" loading="lazy"><img src="img/scene_03_detail.webp" alt="03 情境近景" loading="lazy"></figure>
  <p class="pd-miss" style="color:var(--dim)">情境：AI 生成空間＋原模型渲染產品合成</p>'''+t[j:]
css='''
/* bespoke colour swatches */
#swatch{display:flex;justify-content:center;gap:14px;margin-top:18px;min-height:30px;flex-wrap:wrap}
#swatch button{all:unset;cursor:pointer;display:flex;flex-direction:column;align-items:center;gap:6px}
#swatch i{width:22px;height:22px;border-radius:50%;background:var(--c);box-shadow:inset 0 0 0 1px rgba(255,255,255,.25);transition:.25s}
#swatch button.on i{box-shadow:inset 0 0 0 1px rgba(255,255,255,.25),0 0 0 2px #000,0 0 0 3px var(--acc)}
#swatch span{font:400 10.5px var(--zh);color:var(--dim);opacity:0;transition:.25s;white-space:nowrap}
#swatch button.on span,#swatch button:hover span{opacity:1;color:var(--acc)}
body.light #swatch button.on i{box-shadow:inset 0 0 0 1px rgba(0,0,0,.15),0 0 0 2px #fff,0 0 0 3px #8fc000}
body.light #swatch button.on span{color:#4a7410}
/* 01 studio shot per theme */
.p01fig .th-l{display:none}body.light .p01fig .th-l{display:block}body.light .p01fig .th-d{display:none}
.p01fig img{filter:none!important;border-radius:22px;max-height:100%;object-fit:contain}
/* 03 scene */
.pd-scene{display:grid;grid-template-columns:1.6fr 1fr;gap:14px;margin-top:5vh}
.pd-scene img{width:100%;height:100%;object-fit:cover;border-radius:22px}
@media(max-width:900px){.pd-scene{grid-template-columns:1fr}}
'''
t=t.replace('</style>',css+'</style>',1)
open(p,'w',encoding='utf-8').write(t);print('ok')
