p='index.html';t=open(p,encoding='utf-8').read()
# 1 stop particles entirely
t=t.replace("const a=(.18+.5*(1-Math.abs(p.v)*1.6)*(.5+.5*p.s))*(1-cur.spread*.4);","continue;const a=0;")
css='''
/* ---- product-first ---- */
#wave{display:none!important}
h2{font-size:clamp(34px,3.6vw,56px)!important;letter-spacing:-.03em!important}
h2 .zh{font-size:clamp(16px,1.3vw,20px)!important;font-weight:500!important}
.body{font-size:14px!important}
/* family: products own the screen */
#s-family{min-height:100svh;padding:9vh 0 6vh!important;display:flex;flex-direction:column;justify-content:center}
#s-family .slash{text-align:center}
#s-family h2{text-align:center;font:500 clamp(18px,1.6vw,24px) var(--zh)!important;letter-spacing:.02em!important;margin-top:10px}
#s-family h2 br,#s-family h2 .dot{display:none}
#s-family .body{display:none}
.fam{margin-top:4vh!important;gap:2vw!important;max-width:1500px;margin-left:auto;margin-right:auto}
.fam figure{height:62vh!important;border:0!important;padding-bottom:0!important;margin-bottom:22px!important}
.fam a:nth-child(1) figure img{max-height:42%!important}
.fam a:nth-child(2) figure img{max-height:52%!important}
.fam a:nth-child(3) figure img{max-height:82%!important}
.fam a:nth-child(4) figure img{max-height:100%!important}
.fam img{filter:drop-shadow(0 30px 34px rgba(0,0,0,.5))}
body.light .fam img{filter:drop-shadow(0 26px 28px rgba(30,30,60,.2))}
.fam a{text-align:center!important}
.fam b{font-size:14px!important;display:inline!important;margin-right:8px}
.fam span{display:inline!important;font:500 13px var(--zh)!important}
.fam em{font-size:10px!important}
/* product pages: image first, small type */
.pd{padding:7vh 0 6vh!important;display:flex;flex-direction:column;justify-content:center}
.pd-t{font-size:clamp(22px,2vw,30px)!important;font-weight:600!important;margin-top:8px!important}
.pd-line{font-size:13px!important;margin-top:6px!important}
.pd-fig{height:72vh!important;margin-top:3vh!important}
.pd-fig img{max-width:min(100%,1400px)!important}
#p01 .pd-fig{height:60vh!important}
.pd-facts{margin-top:3vh!important;max-width:760px}
.pd-facts dt{font-size:9.5px!important}.pd-facts dd{font-size:13px!important}
.pd-miss{font-size:10.5px!important;margin-top:14px!important}
@media(max-width:900px){.fam figure{height:34vh!important}.pd-fig{height:50vh!important}}
'''
t=t.replace('</style>',css+'</style>',1)
open(p,'w',encoding='utf-8').write(t);print('continue;const a=0;' in t)
