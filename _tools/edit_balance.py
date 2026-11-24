p='index.html';t=open(p,encoding='utf-8').read()
css='''
/* ================= colour balance (DARK + LIGHT): black 70 / white-grey 25 / green 5 =================
   green only = light source on glass, the one primary action, the selected state, acoustic data */
body:not(.rytho){--t1:#F2F3F5;--t2:rgba(242,243,245,.62);--t3:rgba(242,243,245,.38);--t4:rgba(242,243,245,.18)}
body.light{--t1:#0B0B12;--t2:rgba(11,11,18,.62);--t3:rgba(11,11,18,.42);--t4:rgba(11,11,18,.14)}
/* numbers + labels back to neutral */
body:not(.rytho) .pd-n,body:not(.rytho) #s-family .fam b{color:var(--t1)!important}
body:not(.rytho) .pd-en,body:not(.rytho) .slash,body:not(.rytho) .runhead .mono,body:not(.rytho) .ex-head .mono{color:var(--t3)!important}
body:not(.rytho) .steps b{color:var(--t2)!important}
body:not(.rytho) .xl b{color:var(--t1)!important}body:not(.rytho) .xl span{color:var(--t3)!important}
body:not(.rytho) #s-partner .col .mono{color:var(--t3)!important}
body:not(.rytho) .pd-facts dt{color:var(--t3)!important}body:not(.rytho) .pd-facts dd{color:var(--t1)!important}
body:not(.rytho) .pd-line,body:not(.rytho) #s-family .fam em,body:not(.rytho) #s-family .fam em::after{color:var(--t2)!important}
/* no third hue: missing notes go neutral with a hollow dot */
body:not(.rytho) .pd-miss,body:not(.rytho) .missing{color:var(--t3)!important;opacity:1!important}
body:not(.rytho) .missing b{color:var(--t2)!important}
body:not(.rytho) .missing::before{background:transparent!important;box-shadow:inset 0 0 0 1px var(--t3)!important}
body:not(.rytho) .pd-miss::before{content:"";display:inline-block;width:6px;height:6px;border-radius:50%;box-shadow:inset 0 0 0 1px var(--t3);margin-right:8px;vertical-align:middle}
/* green as light, not paint: CTA + explode action become lit glass */
body:not(.rytho) .pill{background:rgba(255,255,255,.04)!important;color:var(--t1)!important;font-weight:500!important;
 box-shadow:inset 0 0 0 1px rgba(198,244,50,.55),inset 0 0 22px rgba(198,244,50,.16),0 0 40px -8px rgba(198,244,50,.35)!important;-webkit-backdrop-filter:blur(14px) saturate(150%);backdrop-filter:blur(14px) saturate(150%)}
body:not(.rytho) .pill .go{background:transparent!important;color:var(--acc)!important;box-shadow:inset 0 0 0 1px var(--acc),0 0 14px rgba(198,244,50,.45)!important}
body.light .pill{background:rgba(255,255,255,.55)!important;box-shadow:inset 0 0 0 1px #6f9a00,inset 0 0 20px rgba(143,192,0,.18),0 14px 30px -16px rgba(80,110,0,.45)!important}
body.light .pill .go{color:#6f9a00!important;box-shadow:inset 0 0 0 1px #6f9a00!important}
body:not(.rytho) #exBtn b{background:transparent!important;color:var(--acc)!important;box-shadow:inset 0 0 0 1px var(--acc),0 0 12px rgba(198,244,50,.4)}
body.light #exBtn b{color:#6f9a00!important;box-shadow:inset 0 0 0 1px #6f9a00}
/* second accent = cool-white glass highlight opposite the green key */
body:not(.rytho):not(.light) .lg-t::after{background:linear-gradient(180deg,rgba(225,236,255,.16),transparent)!important}
/* glass levels: nav thickest, controls mid, cards thin */
body:not(.rytho) #s-partner .col .lg-t{opacity:.55!important}
body:not(.rytho) #s-partner .col .lg-b{background:linear-gradient(180deg,rgba(255,255,255,.04),rgba(255,255,255,.012))}
body.light #s-partner .col .lg-b{background:rgba(255,255,255,.45)}
'''
t=t.replace('</style>',css+'</style>',1)
open(p,'w',encoding='utf-8').write(t);print('ok')
