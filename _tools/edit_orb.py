p='index.html';t=open(p,encoding='utf-8').read()
t=t.replace('<div class="orb rv"><div class="st"></div><div class="st b"></div></div>','<div class="orb rv"><i class="rim r1"></i><i class="rim r2"></i><i class="rim r3"></i><i class="caus"></i></div>')
css='''
/* ---- orb v2: gradient lives only as refraction around the glass edge ---- */
@property --a{syntax:'<angle>';inherits:false;initial-value:0deg}
.orb{width:min(380px,70vw)!important;background:radial-gradient(120% 140% at 50% -20%,#15151c,#050507 60%)!important;
 box-shadow:inset 0 0 0 1px rgba(255,255,255,.18),inset 0 18px 30px -22px rgba(238,242,255,.55),0 30px 60px -30px rgba(0,0,0,.9)!important;overflow:hidden}
.orb::before{display:none!important}
.orb .st{display:none}
.orb .rim{position:absolute;inset:0;border-radius:inherit;pointer-events:none;
 background:conic-gradient(from var(--a),#3D2EBC,#8a9cff 12%,#EEF2FF 20%,#2FBFA5 30%,#B6E467 38%,#3D2EBC 52%,#1b1550 62%,#8a9cff 76%,#EEF2FF 82%,#3D2EBC);
 -webkit-mask:linear-gradient(#000 0 0) content-box,linear-gradient(#000 0 0);-webkit-mask-composite:xor;mask-composite:exclude;animation:spinA 9s linear infinite}
.orb .r1{padding:1.6px;opacity:.95}
.orb .r2{padding:9px;filter:blur(7px);opacity:.75}
.orb .r3{padding:22px;filter:blur(18px);opacity:.35;animation-duration:13s;animation-direction:reverse}
.orb .caus{position:absolute;left:14%;right:14%;bottom:7%;height:22%;border-radius:50%;
 border-bottom:2px solid rgba(238,242,255,.85);filter:blur(1.2px);opacity:.8;
 -webkit-mask:linear-gradient(90deg,transparent,#000 30%,#000 70%,transparent);mask:linear-gradient(90deg,transparent,#000 30%,#000 70%,transparent)}
@keyframes spinA{to{--a:360deg}}
body.light .orb{background:radial-gradient(120% 140% at 50% -20%,#ffffff,#e4e6ee 65%)!important;box-shadow:inset 0 0 0 1px rgba(255,255,255,.95),inset 0 18px 30px -22px #fff,0 30px 60px -30px rgba(30,30,60,.35)!important}
body.light .orb .caus{border-bottom-color:rgba(61,46,188,.5)}
'''
t=t.replace('</style>',css+'</style>',1)
open(p,'w',encoding='utf-8').write(t)
print(t.count('class="rim'))
