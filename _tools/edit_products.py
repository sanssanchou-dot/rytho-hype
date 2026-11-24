p='index.html';t=open(p,encoding='utf-8').read()
lines=t.split('\n')
# find block from "<!-- 01 PORTABLE -->" to line before "<!-- PARTNER -->"
a=next(i for i,l in enumerate(lines) if l.strip()=='<!-- 01 PORTABLE -->')
b=next(i for i,l in enumerate(lines) if l.strip()=='<!-- PARTNER -->')

def prod(id,n,en,zh,line,img,parts,conn,ai,status,miss,extra=''):
    aicls=' ai' if ai else ''
    return f'''<section class="pd{aicls}" id="{id}"><div class="wrap">
  <div class="pd-head rv"><span class="pd-n">{n}</span><span class="pd-en">{en}</span></div>
  <h2 class="pd-t rv">{zh}</h2>
  <p class="pd-line rv">{line}</p>
  <figure class="pd-fig rv"><img src="{img}" alt="{zh}"{' style="mix-blend-mode:multiply"' if 'portable' in img else ''}></figure>
  {extra}
  <dl class="pd-facts rv">
    <div><dt>取自整塔</dt><dd>{parts}</dd></div>
    <div><dt>連線</dt><dd>{conn}</dd></div>
    <div><dt>狀態</dt><dd>{status}</dd></div>
  </dl>
  <p class="pd-miss">{miss}</p>
</div></section>'''

overview='''<section id="s-family"><div class="wrap">
  <p class="slash rv">One pair · four products</p>
  <h2 class="rv">一座塔，<br>拆成四個產品<span class="dot">.</span></h2>
  <p class="body rv" style="margin-top:22px">由小到大：從一顆透明模組的隨身音響，到整組可訂製的高訂。02 起內建 Wi-Fi 與 AI。</p>
  <div class="fam rv">
    <a href="#p01"><figure><img src="img/portable.webp" alt="" style="mix-blend-mode:multiply"></figure><b>01</b><span>隨身</span><em>Bluetooth</em></a>
    <a href="#p02"><figure><img src="img/homeBcoax.webp" alt=""></figure><b>02</b><span>單顆＋底座</span><em class="ai">Wi-Fi · AI</em></a>
    <a href="#p03"><figure><img src="img/homeA.webp" alt=""></figure><b>03</b><span>上半段兩節</span><em class="ai">Wi-Fi · AI</em></a>
    <a href="#p04"><figure><img src="img/ring.webp" alt=""></figure><b>04</b><span>整組高訂</span><em class="ai">Wi-Fi · AI</em></a>
  </div>
</div></section>'''

ai='''<section id="s-ai"><div class="wrap">
  <div class="orb rv"><i class="rim r1"></i><i class="rim r2"></i><i class="rim r3"></i><i class="caus"></i></div>
  <h2 class="rv">Now it<br>listens<span class="dot">.</span></h2>
  <p class="body rv" style="margin:18px auto 0;text-align:center">02—04 內建 Wi-Fi 晶片，開啟 AI。</p>
  <p class="pd-miss" style="text-align:center">缺：AI 功能定義、麥克風／狀態燈位置</p>
</div></section>'''

p01=prod('p01','01','Portable','隨身','螺旋全透明聲學腔，一手帶走。','img/portable.webp',
 '透明中音模組的振膜與螺旋腔','Bluetooth',False,'概念階段',
 '缺：精修渲染（目前 AI 概念圖、無 CAD）')
p02=prod('p02','02','Home AI · Single','單顆＋底座','一顆透明模組，中心加同軸高音。','img/homeBcoax.webp',
 '透明中音模組 ×1＋新增同軸高音、底座','Wi-Fi · AI · Bluetooth',True,'原模組渲染',
 '缺：底座修薄、振膜透光特寫')
p03=prod('p03','03','Home AI · Upper Two','上半段兩節','整塔上半段直接取下，加一座底座。','img/homeA.webp',
 '小圓高音 ×2、方形單體、透明中音 ×1','Wi-Fi · AI · Bluetooth',True,'原模型渲染',
 '缺：居家情境圖')
chooser='''<div class="seg2 rv" id="chooser">
    <button class="on" data-img="img/ring.webp">Ring</button><button data-img="img/branch.webp">Branch</button><button data-img="img/fold.webp">Fold</button>
  </div>'''
p04=prod('p04','04','Bespoke · Full Set','整組高訂','單體與箱體不動，只換承載主體。','img/ring.webp',
 '整組八個單體與箱體','Wi-Fi · AI',True,'原網格渲染',
 '缺：主體顏色版本、完整外殼版',chooser).replace('<img src="img/ring.webp" alt="整組高訂">','<img id="bodyImg" src="img/ring.webp" alt="整組高訂">')

new=['<!-- PRODUCTS -->',overview,p01,ai,p02,p03,p04,'']
lines=lines[:a]+new+lines[b:]
t='\n'.join(lines)

css='''
/* ---- products v2: one template, one idea per screen ---- */
#s-family{padding:22vh 0 12vh}
.fam{display:grid;grid-template-columns:repeat(4,1fr);gap:28px;margin-top:70px;align-items:end}
.fam a{display:block;text-align:left}
.fam figure{height:min(34vh,320px);display:flex;align-items:flex-end;justify-content:center;border-bottom:1px solid rgba(238,242,255,.16);padding-bottom:18px;margin-bottom:16px}
.fam a:nth-child(1) figure img{max-height:40%}
.fam a:nth-child(2) figure img{max-height:55%}
.fam a:nth-child(3) figure img{max-height:80%}
.fam a:nth-child(4) figure img{max-height:100%}
.fam img{object-fit:contain;max-width:100%;transition:transform .5s cubic-bezier(.2,.7,.1,1)}
.fam a:hover img{transform:translateY(-8px)}
.fam b{font:900 22px var(--dot);display:block;color:var(--ice)}
.fam span{font:700 17px var(--zh);display:block;margin-top:4px}
.fam em{font:500 11px var(--mono);font-style:normal;letter-spacing:.12em;color:var(--mute);display:block;margin-top:6px}
.fam em.ai{color:#a89dff}
body.light .fam figure{border-color:rgba(11,11,18,.14)}
body.light .fam em.ai{color:#3D2EBC}
@media(max-width:900px){.fam{grid-template-columns:repeat(2,1fr)}}

.pd{min-height:100svh;padding:16vh 0 10vh;text-align:center}
.pd-head{display:flex;justify-content:center;gap:14px;align-items:baseline}
.pd-n{font:900 18px var(--dot);color:var(--lime)}
body.light .pd-n{color:#4a7410}
.pd.ai .pd-n{color:#a89dff}
body.light .pd.ai .pd-n{color:#3D2EBC}
.pd-en{font:500 12px var(--mono);letter-spacing:.2em;text-transform:uppercase;color:var(--mute)}
.pd-t{font-family:var(--zh)!important;font-weight:700!important;font-size:clamp(56px,8vw,120px)!important;letter-spacing:-.01em!important;line-height:1.05!important;margin-top:18px}
.pd-line{font:400 clamp(17px,1.5vw,22px)/1.6 var(--zh);color:var(--mute);margin-top:14px}
.pd-fig{margin:48px auto 0;height:min(62vh,640px);display:flex;align-items:center;justify-content:center}
.pd-fig img{max-height:100%;max-width:min(100%,980px);object-fit:contain;filter:drop-shadow(0 40px 50px rgba(0,0,0,.45));transition:opacity .35s}
body.light .pd-fig img{filter:drop-shadow(0 36px 40px rgba(30,30,60,.22))}
#p01 .pd-fig{height:min(46vh,480px)}
.pd-facts{display:grid;grid-template-columns:repeat(3,1fr);max-width:960px;margin:52px auto 0;border-top:1px solid rgba(238,242,255,.16);text-align:left}
.pd-facts div{padding:20px 24px 0 0}
.pd-facts dt{font:500 11px var(--mono);letter-spacing:.16em;color:var(--dim)}
.pd-facts dd{font:500 16px/1.5 var(--zh);margin-top:8px}
body.light .pd-facts{border-color:rgba(11,11,18,.14)}
.pd-miss{margin-top:28px;font:400 11.5px var(--zh);color:#ffb44d;opacity:.75}
body.light .pd-miss{color:#b06a00}
.seg2{display:inline-flex;gap:4px;padding:5px;border-radius:999px;margin-top:28px;background:rgba(255,255,255,.06);box-shadow:inset 0 0 0 1px rgba(255,255,255,.14)}
.seg2 button{all:unset;cursor:pointer;font:600 13px var(--en);padding:10px 20px;border-radius:999px;color:var(--mute)}
.seg2 button.on{background:var(--ice);color:#000}
body.light .seg2{background:rgba(0,0,0,.04);box-shadow:inset 0 0 0 1px rgba(0,0,0,.1)}
body.light .seg2 button.on{background:#0B0B12;color:#fff}
@media(max-width:900px){.pd-facts{grid-template-columns:1fr}.pd-fig{height:48vh}}
#s-ai{padding:22vh 0 12vh}
'''
t=t.replace('</style>',css+'</style>',1)
# chooser JS: update for new markup
t=t.replace("$$('#chooser .bev').forEach(b=>b.onclick=()=>{$$('#chooser .bev').forEach(x=>x.classList.toggle('on',x===b));const im=$('#bodyImg');im.style.opacity=0;setTimeout(()=>{im.src=b.dataset.img;im.style.opacity=1},220);$('#bodyTag').textContent=b.textContent.toUpperCase()});",
 "$$('#chooser button').forEach(b=>b.onclick=()=>{$$('#chooser button').forEach(x=>x.classList.toggle('on',x===b));const im=$('#bodyImg');im.style.opacity=0;setTimeout(()=>{im.src=b.dataset.img;im.style.opacity=1},220)});")
# rail: add family? keep; relabel chapters to new order
t=t.replace('data-id="p02" data-t="Home AI · Upper"','data-id="p02" data-t="Home AI · Single"',1)
t=t.replace('data-id="p03" data-t="Home AI · Single"','data-id="p03" data-t="Home AI · Upper Two"',1)
open(p,'w',encoding='utf-8').write(t)
print('ok', t.count('class="pd'), 'bodyTag' in t)
