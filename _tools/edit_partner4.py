p='index.html';t=open(p,encoding='utf-8').read()
a=t.index('<div class="cols">');b=t.index('<div class="steps rv">')
new='''<div class="cols">
    <div class="col glass rv"><span class="mono">Driver</span><h3>玻音先創</h3><p>單體技術與製造：透明玻璃振膜、單體參數、良率與供應。</p></div>
    <div class="col glass rv"><span class="mono">Software</span><h3>Rytho</h3><p>軟體技術：AI 聆聽、App 與 Wi-Fi 連網體驗。</p></div>
    <div class="col glass rv"><span class="mono">Design</span><h3>OPQ Studio</h3><p>產品設計：透明結構、卡榫主體、樣機與視覺敘事。</p></div>
    <div class="col glass rv"><span class="mono">DSP</span><h3>玩樂生活</h3><p>聲學技術：DSP 調校、分頻與量測。</p></div>
  </div>
  '''
t=t[:a]+new+t[b:]
t=t.replace('<b>缺：合作方 logo</b>（玻音先創、研發方）','<b>缺：四方 logo</b>（玻音先創、Rytho、OPQ、玩樂生活）')
t=t.replace('一起把透明振膜帶進產品<i></i><span class="go">','一起把透明振膜帶進產品<span class="go">')
t=t.replace('OPQ STUDIO × 玻音先創 · RYTHO HYPE · 2026','玻音先創 × Rytho × OPQ STUDIO × 玩樂生活 · RYTHO HYPE · 2026')
t=t.replace('</style>','''
/* partner: 4 columns; caret rules must not hit glass-rim <i> */
.cols{grid-template-columns:repeat(4,1fr)!important}
@media(max-width:1100px){.cols{grid-template-columns:repeat(2,1fr)!important}}
@media(max-width:700px){.cols{grid-template-columns:1fr!important}}
'''+'</style>',1)
for s in ['.pill i{','body.light .pill i{','.pill i{background:#0B0B12!important}']:
    pass
t=t.replace('.pill i{width:2px','.pill i.caret{width:2px').replace('body.light .pill i{','body.light .pill i.caret{').replace('.pill i{background:#0B0B12!important}','.pill i.caret{background:#0B0B12!important}')
open(p,'w',encoding='utf-8').write(t)
print(t.count('class="col glass'), '.pill i{' in t)
