import re
p='index.html';t=open(p,encoding='utf-8').read()
# hover scenes for all four
t=t.replace(' data-scene="img/p01_dark.webp"','')
for n in ['01','02','03','04']:
    t=t.replace(f'<a href="#p{n}"><figure>',f'<a href="#p{n}" data-scene="img/arch_{n}.webp"><figure>',1)
# scene figure under each product page's facts
for n in ['01','02','03','04']:
    i=t.index(f'id="p{n}"');j=t.index('</dl>',i)+5
    if 'class="pd-arch' in t[i:t.index('</section>',i)]:continue
    t=t[:j]+f'\n  <figure class="pd-arch rv"><img src="img/arch_{n}.webp" alt="" loading="lazy"></figure>'+t[j:]
css='''
/* architectural scene per product */
.pd-arch{margin:6vh auto 0;max-width:1500px;width:100%}
.pd-arch img{display:block;width:100%;height:auto;border-radius:24px;box-shadow:0 40px 80px -40px rgba(0,0,0,.9)}
'''
t=t.replace('</style>',css+'</style>',1)
open(p,'w',encoding='utf-8').write(t);print(t.count('arch_'))
