p='index.html';t=open(p,encoding='utf-8').read()
# remove old label columns + group bar
a=t.index('<div class="ex-labels" id="labL">');b=t.index('</div>\n    <div class="ex-stage">')+6
t=t[:a]+t[b:]
a=t.index('<div class="ex-groups glass" id="exGroups"');b=t.index('</div>',t.index('04 整組</a>'))+6
t=t[:a]+t[b:]
a=t.index('<div class="ex-labels r" id="labR">');b=t.index('<div class="ex-foot">')
t=t[:a]+'''<div id="exLabs">
      <div class="xl" data-y=".09"><b>TWEETER ×2</b><span>小圓高音模組 · 原箱體</span></div>
      <div class="xl" data-y=".22"><b>HIGH</b><span>方形面單體 · 原箱體</span></div>
      <div class="xl" data-y=".42"><b>TRANSPARENT MID ×3</b><span>玻音先創透明振膜 · 螺旋腔</span></div>
      <div class="xl" data-y=".74"><b>WOOFER ×2</b><span>低音模組 · 原箱體</span></div>
      <div class="xl c" data-y=".56" data-side="body"><b>CHASSIS</b><span>帶卡榫的承載主體 · 唯一可變件</span></div>
    </div>
    '''+t[b:]
css='''
/* explode labels v3: one side, all at once, aligned to modules */
#exLabs{position:absolute;inset:0;z-index:2;pointer-events:none;opacity:0;transition:opacity .6s}
#exLabs.on{opacity:1}
.xl{position:absolute;left:0;top:0;transform:translateY(-50%);white-space:nowrap}
.xl b{display:block;font:500 12px var(--mono);letter-spacing:.12em;color:var(--ice)}
.xl span{display:block;font:400 12px var(--zh);color:var(--mute);margin-top:3px}
.xl.c b{color:var(--lime)}
body.light .xl.c b{color:#4a7410}
@media(max-width:900px){.xl span{display:none}.xl b{font-size:10px}}
'''
t=t.replace('</style>',css+'</style>',1)
# JS: replace label toggles and groups
t=t.replace(" labs.forEach(l=>l.classList.toggle('on',ep>=+l.dataset.at));$('#exGroups').classList.toggle('on',ep>.72);",
 " $('#exLabs').classList.toggle('on',ep>.08);")
# fitDraw stores rect, place labels
t=t.replace("ex.clearRect(0,0,cw,ch);ex.drawImage(im,(cw-w)/2,(ch-h)/2+ch*.02,w,h)}",
 "ex.clearRect(0,0,cw,ch);const X=(cw-w)/2,Y=(ch-h)/2+ch*.02;ex.drawImage(im,X,Y,w,h);placeLabs(X,Y,w,h,cw)}\nfunction placeLabs(X,Y,w,h,cw){const k=exC.clientWidth/cw;const right=(X+w*(window.LAB_RIGHT||.62))*k+24;$$('.xl').forEach(l=>{l.style.left=right+'px';l.style.top=((Y+h*+l.dataset.y)*k)+'px'})}")
open(p,'w',encoding='utf-8').write(t)
print(t.count('class="xl'), 'exGroups' in t, 'labL' in t)
