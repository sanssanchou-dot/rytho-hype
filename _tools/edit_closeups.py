p='index.html';t=open(p,encoding='utf-8').read()
t=t.replace('<figure><img src="img/portable_cut.webp" alt=""></figure>','<figure><img src="img/c01.webp" alt=""></figure>',1)
t=t.replace('<a href="#p02"><figure><img src="img/u02.webp" alt="">','<a href="#p02"><figure><img src="img/c02.webp" alt="">',1)
t=t.replace('<figure><img src="img/u03.webp" alt=""></figure>','<figure><img src="img/c03.webp" alt=""></figure>',1)
t=t.replace('<figure><img src="img/u04.webp" alt=""></figure>','<figure><img src="img/c04.webp" alt=""></figure>',1)
t=t.replace('<img class="th-d" src="img/p01_dark.webp" alt="隨身"><img class="th-l" src="img/p01_light.webp" alt="隨身">','<img src="img/c01.webp" alt="隨身">')
t=t.replace('<figure class="pd-fig rv"><img src="img/u02.webp" alt="單顆＋底座"></figure>','<figure class="pd-fig rv stage"><img src="img/c02.webp" alt="單顆＋底座"></figure>')
t=t.replace('<figure class="pd-fig rv"><img src="img/u03.webp" alt="上半段兩節"></figure>','<figure class="pd-fig rv stage"><img src="img/c03.webp" alt="上半段兩節"></figure>')
t=t.replace('pd-fig rv p01fig','pd-fig rv stage p01fig')
t=t.replace('?v=','?v=')
css='''
/* on-stage close-ups (opaque near-black renders): melt edges into the page */
#s-family .fam{grid-template-columns:1.5fr 1.5fr 1.6fr 1.6fr!important;gap:1.6vw!important;align-items:start!important}
#s-family .fam figure{height:auto!important;aspect-ratio:auto;display:block!important;margin-bottom:14px!important}
#s-family .fam a figure img{max-height:none!important;width:100%!important;height:auto!important;filter:none!important;transform:none!important;border-radius:18px;
 -webkit-mask:radial-gradient(120% 120% at 50% 45%,#000 55%,transparent 100%);mask:radial-gradient(120% 120% at 50% 45%,#000 55%,transparent 100%);transition:transform .6s cubic-bezier(.2,.7,.1,1)}
#s-family .fam a:hover figure img{transform:scale(1.03)!important}
.pd-fig.stage img{filter:none!important;width:auto;max-width:100%;max-height:100%;object-fit:contain;
 -webkit-mask:radial-gradient(75% 75% at 50% 48%,#000 60%,transparent 100%);mask:radial-gradient(75% 75% at 50% 48%,#000 60%,transparent 100%)}
body.light #s-family .fam a figure img,body.light .pd-fig.stage img{-webkit-mask:none;mask:none;border-radius:22px;box-shadow:0 30px 60px -30px rgba(0,0,0,.45)}
#p01 .pd-fig{height:72vh!important}
@media(max-width:900px){#s-family .fam{grid-template-columns:1fr 1fr!important}}
'''
t=t.replace('</style>',css+'</style>',1)
open(p,'w',encoding='utf-8').write(t);print(t.count('img/c0'))
