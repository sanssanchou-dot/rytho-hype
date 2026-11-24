p='index.html';t=open(p,encoding='utf-8').read()
t=t.replace('<canvas id="exCanvas" width="544" height="1367"></canvas>','<canvas id="exCanvas" width="1920" height="1080"></canvas>')
css='''
/* ---- full-screen explode ---- */
#s-explode{height:340vh}
#s-explode .pin{display:block;max-width:none;padding:0;position:sticky;top:0;height:100svh}
#s-explode .ex-stage{position:absolute;inset:0;display:block}
#exCanvas{position:absolute!important;inset:0;width:100%!important;height:100%!important;max-width:none!important}
#s-explode .ex-labels{position:absolute;top:50%;transform:translateY(-50%);z-index:2}
#s-explode #labL{left:28px}
#s-explode #labR{right:28px}
#s-explode .ex-head{top:28px;z-index:2}
#s-explode .ex-foot{z-index:2}
#s-explode .pin::before{inset:6% 10%}
@media(max-width:900px){#s-explode .ex-labels{top:auto;bottom:90px;transform:none}#s-explode #labL{left:12px;right:60px}}
'''
t=t.replace('</style>',css+'</style>',1)
old_fb=t[t.index('function drawFallback(p){'):t.index('}',t.index('function drawFallback(p){'))+1]
t=t.replace(old_fb,'''function fitDraw(im){const cw=exC.width=exC.clientWidth*Math.min(2,devicePixelRatio||1),ch=exC.height=exC.clientHeight*Math.min(2,devicePixelRatio||1);const s=Math.min(cw/im.naturalWidth,ch/im.naturalHeight)*.96;const w=im.naturalWidth*s,h=im.naturalHeight*s;ex.clearRect(0,0,cw,ch);ex.drawImage(im,(cw-w)/2,(ch-h)/2+ch*.02,w,h)}
function drawFallback(p){fitDraw(fallback)}''')
t=t.replace("if(im&&im.complete){ex.clearRect(0,0,544,1367);ex.drawImage(im,0,0,544,1367)}","if(im&&im.complete&&im.naturalWidth)fitDraw(im)")
open(p,'w',encoding='utf-8').write(t)
print('fitDraw' in t, old_fb[:60])
