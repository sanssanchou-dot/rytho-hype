p='index.html';t=open(p,encoding='utf-8').read()
if 'src="lg.js"' not in t:
    t=t.replace('</body>','<script src="lg.js"></script>\n</body>',1)
css='''
/* ================= liquid glass v2: refraction + thickness + green key ================= */
:root{--kx:calc(cos(var(--la)) * 1);--ky:calc(sin(var(--la)) * 1)}
.lgx{background:transparent!important;-webkit-backdrop-filter:none!important;backdrop-filter:none!important;isolation:isolate;
 box-shadow:0 18px 40px -18px rgba(0,0,0,.85),0 2px 6px -2px rgba(0,0,0,.5)!important}
.lgx>.lgrim{display:none!important}
.lg-b{position:absolute;inset:0;border-radius:inherit;z-index:-1;pointer-events:none;
 background:linear-gradient(180deg,rgba(255,255,255,.075),rgba(255,255,255,.02) 55%,rgba(255,255,255,.045))}
.lg-t{position:absolute;inset:0;border-radius:inherit;z-index:3;pointer-events:none;
 box-shadow:
  inset 0 0 0 .5px rgba(255,255,255,.32),
  inset calc(var(--kx) * 1.2px) calc(var(--ky) * 1.2px) 0 -.2px rgba(198,244,50,.95),
  inset calc(var(--kx) * 6px) calc(var(--ky) * 6px) 12px -6px rgba(198,244,50,.42),
  inset 0 1.5px 1px -.5px rgba(255,255,255,.55),
  inset 0 -1.5px 1.5px -.5px rgba(255,255,255,.16),
  inset calc(var(--kx) * -10px) calc(var(--ky) * -10px) 18px -10px rgba(0,0,0,.65),
  inset 0 0 22px rgba(255,255,255,.035);opacity:calc(.75 + var(--lb) * .25)}
.lg-t::before{content:"";position:absolute;inset:0;border-radius:inherit;padding:1px;opacity:.9;
 background:conic-gradient(from var(--la),rgba(198,244,50,.95),rgba(198,244,50,.25) 35deg,rgba(255,255,255,.08) 90deg,rgba(255,255,255,.04) 150deg,rgba(255,255,255,.35) 185deg,rgba(255,255,255,.05) 230deg,rgba(198,244,50,.25) 325deg,rgba(198,244,50,.95));
 -webkit-mask:linear-gradient(#000 0 0) content-box,linear-gradient(#000 0 0);-webkit-mask-composite:xor;mask:linear-gradient(#000 0 0) content-box exclude,linear-gradient(#000 0 0)}
.lg-t::after{content:"";position:absolute;left:8%;right:8%;top:1px;height:40%;border-radius:inherit;
 background:linear-gradient(180deg,rgba(255,255,255,.10),transparent);filter:blur(1px)}
/* light theme: bright clear glass */
body.light .lgx{box-shadow:0 16px 36px -18px rgba(20,24,40,.35),0 1px 3px rgba(20,24,40,.12)!important}
body.light .lg-b{background:linear-gradient(180deg,rgba(255,255,255,.55),rgba(255,255,255,.22) 55%,rgba(255,255,255,.38))}
body.light .lg-t{box-shadow:
  inset 0 0 0 .5px rgba(255,255,255,.9),
  inset calc(var(--kx) * 1.2px) calc(var(--ky) * 1.2px) 0 -.2px rgba(143,192,0,.9),
  inset calc(var(--kx) * 6px) calc(var(--ky) * 6px) 12px -6px rgba(170,220,40,.45),
  inset 0 1.5px 1px -.5px #fff,
  inset calc(var(--kx) * -10px) calc(var(--ky) * -10px) 18px -10px rgba(30,40,60,.18)}
body.light .lg-t::before{background:conic-gradient(from var(--la),#8fc000,rgba(143,192,0,.25) 35deg,rgba(255,255,255,.9) 90deg,rgba(0,0,0,.06) 150deg,#fff 185deg,rgba(0,0,0,.05) 230deg,rgba(143,192,0,.25) 325deg,#8fc000)}
/* keep the selected states readable above the glass */
.lgx>*:not(.lg-b):not(.lg-t){position:relative;z-index:1}
#exBtn.lgx{position:absolute}
/* rail glass */
#rail .rshape{background:linear-gradient(180deg,rgba(255,255,255,.07),rgba(255,255,255,.02) 55%,rgba(255,255,255,.05))!important}
body.light #rail .rshape{background:linear-gradient(180deg,rgba(255,255,255,.55),rgba(255,255,255,.22) 55%,rgba(255,255,255,.38))!important}
#rail .lg-th .t1{fill:none;stroke:rgba(255,255,255,.22);stroke-width:5}
#rail .lg-th .t2{fill:none;stroke:url(#rEdgeG);stroke-width:12;opacity:.45}
#rail .lg-th .t3{fill:none;stroke:rgba(255,255,255,.35);stroke-width:2;transform:translate(-1px,1px);opacity:.5}
body.light #rail .lg-th .t1{stroke:rgba(255,255,255,.95)}
#rail .redge>path{stroke-width:1.2}
'''
t=t.replace('</style>',css+'</style>',1)
open(p,'w',encoding='utf-8').write(t);print('ok')
