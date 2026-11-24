p='index.html';t=open(p,encoding='utf-8').read()
css='''
/* ===== RYTHO v2: black/white base + liquid glass lit by TWO lights (green key top-left, purple fill bottom-right) ===== */
body.rytho{--rb:#060608;background:#060608!important}
/* glass back on */
body.rytho .lg-b,body.rytho .lg-t,body.rytho #rail .redge{display:block!important}
body.rytho .lg-b{background:linear-gradient(180deg,rgba(255,255,255,.07),rgba(255,255,255,.02) 55%,rgba(255,255,255,.05))!important}
body.rytho .lg-t{box-shadow:
  inset 0 0 0 .5px rgba(255,255,255,.30),
  inset calc(var(--kx) * 1.2px) calc(var(--ky) * 1.2px) 0 -.2px rgba(214,255,101,.95),
  inset calc(var(--kx) * 7px) calc(var(--ky) * 7px) 14px -7px rgba(214,255,101,.40),
  inset calc(var(--kx) * -1.2px) calc(var(--ky) * -1.2px) 0 -.2px rgba(140,92,255,.95),
  inset calc(var(--kx) * -8px) calc(var(--ky) * -8px) 16px -8px rgba(114,60,232,.55),
  inset 0 1.5px 1px -.5px rgba(255,255,255,.5)!important}
body.rytho .lg-t::before{background:conic-gradient(from var(--la),#D6FF65,rgba(214,255,101,.25) 40deg,rgba(255,255,255,.08) 90deg,rgba(140,92,255,.35) 150deg,#8C5CFF 180deg,rgba(140,92,255,.3) 215deg,rgba(255,255,255,.08) 270deg,rgba(214,255,101,.25) 320deg,#D6FF65)!important;opacity:.95!important}
/* rail: glass, edge gradient green -> purple */
body.rytho #rail .rshape{background:linear-gradient(180deg,rgba(255,255,255,.06),rgba(255,255,255,.015) 55%,rgba(255,255,255,.04))!important;-webkit-backdrop-filter:blur(3px) saturate(165%)!important;backdrop-filter:blur(3px) saturate(165%)!important}
body.rytho #rEdgeG stop:nth-child(1){stop-color:#D6FF65}body.rytho #rEdgeG stop:nth-child(4){stop-color:rgba(140,92,255,.75)}body.rytho #rEdgeG stop:nth-child(5){stop-color:#8C5CFF}
body.rytho #rail .ch{box-shadow:inset 0 0 0 1px rgba(255,255,255,.10)!important}
/* controls: glass with white selected pill (black/white base) */
body.rytho #themeT,body.rytho #chooser,body.rytho #chipTitle,body.rytho #exBtn{background:transparent!important}
body.rytho #themeT button[data-th=rytho].on{background:var(--rt)!important}
body.rytho #exBtn span{color:var(--rt)!important}
body.rytho #exBtn b{background:var(--rl)!important;color:#000!important;box-shadow:0 0 18px rgba(214,255,101,.45)!important}
/* ambient light the glass refracts: green top-left, purple bottom-right (soft, fixed) */
body.rytho::before{content:"";position:fixed;inset:0;z-index:-1;pointer-events:none;
 background:radial-gradient(40vw 34vw at 6% 8%,rgba(214,255,101,.10),transparent 70%),radial-gradient(46vw 40vw at 96% 96%,rgba(114,60,232,.20),transparent 70%)}
/* family cards: glass panes; 01 = purple-tinted glass */
body.rytho #s-family .fam a{background:rgba(255,255,255,.035)!important;-webkit-backdrop-filter:blur(18px) saturate(160%);backdrop-filter:blur(18px) saturate(160%);
 box-shadow:inset 0 0 0 .5px rgba(255,255,255,.22),inset 1px 1px 0 rgba(214,255,101,.55),inset -1px -1px 0 rgba(140,92,255,.6),inset 0 1px 1px rgba(255,255,255,.25)}
body.rytho #s-family .fam a:first-child{background:linear-gradient(160deg,rgba(140,92,255,.42),rgba(114,60,232,.18))!important;box-shadow:inset 0 0 0 .5px rgba(255,255,255,.3),inset 1px 1px 0 rgba(214,255,101,.6),inset -1px -1px 0 #8C5CFF,0 20px 60px -20px rgba(114,60,232,.6)}
body.rytho #s-family .fam a:hover{background:rgba(255,255,255,.06)!important}
/* stat tiles: thin glass */
body.rytho .pd-facts>div{background:rgba(255,255,255,.035)!important;-webkit-backdrop-filter:blur(14px);backdrop-filter:blur(14px);
 box-shadow:inset 0 0 0 .5px rgba(255,255,255,.18),inset 1px 1px 0 rgba(214,255,101,.35),inset -1px -1px 0 rgba(140,92,255,.45)}
/* partner: glass cards alternating green / purple tint, text stays white */
body.rytho #s-partner .col{background:transparent!important}
body.rytho #s-partner .col:nth-child(even){background:transparent!important}
body.rytho #s-partner .col .lg-b{background:linear-gradient(160deg,rgba(140,92,255,.20),rgba(255,255,255,.02))!important}
body.rytho #s-partner .col:nth-child(even) .lg-b{background:linear-gradient(160deg,rgba(214,255,101,.16),rgba(255,255,255,.02))!important}
body.rytho #s-partner .col:nth-child(even) h3,body.rytho #s-partner .col:nth-child(even) p{color:var(--rt)!important}
body.rytho #s-partner .col:nth-child(even) .mono{color:var(--rl)!important}
body.rytho #s-partner .col:nth-child(odd) .mono{color:#A98BFF!important}
body.rytho #s-partner .col .lg-t::before{opacity:.7!important}
/* CTA: glass, dual light, lime action */
body.rytho .pill{background:rgba(255,255,255,.05)!important;color:var(--rt)!important;-webkit-backdrop-filter:blur(14px) saturate(160%);backdrop-filter:blur(14px) saturate(160%);
 box-shadow:inset 0 0 0 .5px rgba(255,255,255,.3),inset 1.2px 1.2px 0 #D6FF65,inset -1.2px -1.2px 0 #8C5CFF,inset 10px 10px 24px -14px rgba(214,255,101,.5),inset -12px -12px 26px -14px rgba(114,60,232,.7),0 0 50px -12px rgba(114,60,232,.6)!important}
body.rytho .pill .go{background:var(--rl)!important;color:#000!important;box-shadow:0 0 16px rgba(214,255,101,.5)!important}
/* orb: glass pill, waveform lime -> purple */
body.rytho .orb{background:transparent!important}
body.rytho .orb .wave i{background:linear-gradient(180deg,#D6FF65,#8C5CFF)!important}
/* explode labels: glass chips */
body.rytho .xl b{background:rgba(255,255,255,.06)!important;color:var(--rt)!important;box-shadow:inset 0 0 0 .5px rgba(255,255,255,.25),inset 1px 1px 0 rgba(214,255,101,.6),inset -1px -1px 0 rgba(140,92,255,.7)}
body.rytho .xl.c b{color:var(--rl)!important}
body.rytho .mvl{background:rgba(6,6,8,.55)!important;color:var(--rl)!important;box-shadow:inset 0 0 0 .5px rgba(255,255,255,.2),inset 1px 1px 0 rgba(214,255,101,.5),inset -1px -1px 0 rgba(140,92,255,.6)}
body.rytho .mvl em{color:var(--rm)!important;opacity:1}
'''
t=t.replace('</style>',css+'</style>',1)
open(p,'w',encoding='utf-8').write(t);print('ok')
