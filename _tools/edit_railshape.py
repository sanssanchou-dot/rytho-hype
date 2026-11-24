p='index.html';t=open(p,encoding='utf-8').read()
css='''
/* ---- rail as ONE shape: body + concave fillets in a single path ---- */
#rail{background:none!important;box-shadow:none!important;-webkit-backdrop-filter:none!important;backdrop-filter:none!important;border-radius:0!important;
 gap:16px!important;padding:30px 0 32px!important;width:60px!important;overflow:visible!important}
#rail::before,#rail::after,#rail>.lgrim{display:none!important}
#rail .rshape{position:absolute;left:0;top:-28px;bottom:-28px;width:100%;z-index:-1;pointer-events:none;
 background:radial-gradient(120% 60% at 0% 0%,rgba(198,244,50,.10),transparent 45%),linear-gradient(180deg,rgba(255,255,255,.07),rgba(255,255,255,.015) 60%,rgba(0,0,0,.25));
 -webkit-backdrop-filter:blur(26px) saturate(140%);backdrop-filter:blur(26px) saturate(140%)}
body.light #rail .rshape{background:radial-gradient(120% 60% at 0% 0%,rgba(198,244,50,.22),transparent 45%),linear-gradient(180deg,rgba(255,255,255,.95),rgba(240,242,236,.7))}
#rail .redge{position:absolute;left:0;top:-28px;width:100%;overflow:visible;pointer-events:none;z-index:4}
#rail .redge path{fill:none;stroke:url(#rEdgeG);stroke-width:1}
#rail .rail-line{height:70px!important}
@media(max-width:900px){#rail .rshape,#rail .redge{display:none}#rail{background:rgba(20,20,24,.8)!important;border-radius:22px 0 0 22px!important;gap:8px!important;padding:10px 0!important}}
'''
t=t.replace('</style>',css+'</style>',1)
js='''
/* rail single-shape path */
(()=>{const r=document.getElementById('rail');if(!r)return;const R=28,c=28;
r.insertAdjacentHTML('afterbegin','<div class="rshape"></div><svg class="redge"><defs><linearGradient id="rEdgeG" gradientUnits="userSpaceOnUse"><stop offset="0" stop-color="#C6F432"/><stop offset=".22" stop-color="rgba(198,244,50,.35)"/><stop offset=".5" stop-color="rgba(255,255,255,.10)"/><stop offset=".78" stop-color="rgba(255,255,255,.22)"/><stop offset="1" stop-color="rgba(255,255,255,.06)"/></linearGradient></defs><path/></svg>');
const sh=r.querySelector('.rshape'),sv=r.querySelector('.redge'),pa=sv.querySelector('path'),g=sv.querySelector('#rEdgeG');
let W=0,H=0;
function build(){W=r.offsetWidth;H=r.offsetHeight;const T=H+2*R;
 const d=`M0,0 A${R},${R} 0 0 0 ${R},${R} L${W-c},${R} A${c},${c} 0 0 1 ${W},${R+c} L${W},${R+H-c} A${c},${c} 0 0 1 ${W-c},${R+H} L${R},${R+H} A${R},${R} 0 0 0 0,${T}`;
 sh.style.clipPath=`path('${d} Z')`;sv.setAttribute('width',W);sv.setAttribute('height',T);sv.setAttribute('viewBox',`0 0 ${W} ${T}`);
 pa.setAttribute('d',d.replace(/^M0,0/,'M0.5,0').replace(/ 0,(\d+)$/,' 0.5,$1'));spin()}
function spin(){const T=H+2*R,a=(-45+scrollY*.12)*Math.PI/180,cx=W/2,cy=T/2,L=T/2;
 g.setAttribute('x1',cx-Math.cos(a)*L);g.setAttribute('y1',cy-Math.sin(a)*L);g.setAttribute('x2',cx+Math.cos(a)*L);g.setAttribute('y2',cy+Math.sin(a)*L)}
addEventListener('resize',build);addEventListener('scroll',spin,{passive:true});
if(document.fonts)document.fonts.ready.then(build);build()})();
'''
t=t.replace('/* bespoke chooser */',js+'/* bespoke chooser */',1)
open(p,'w',encoding='utf-8').write(t);print('rEdgeG' in t)
