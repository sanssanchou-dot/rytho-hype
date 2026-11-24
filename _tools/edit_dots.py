p='index.html';t=open(p,encoding='utf-8').read()
t=t.replace('img/homeA.webp','img/homeA_nobase.webp')
t=t.replace('整塔上半段直接取下，加一座底座。','整塔上半段直接取下，自己就能站立。')
t=t.replace('<div id="glowFloor"></div>','<div id="glowFloor"></div><canvas id="dots"></canvas>',1)
css='''
/* ---- dot field: everything coloured is a dot ---- */
#glowFloor,#s-explode .pin::before{display:none!important}
#dots{position:fixed;inset:0;width:100%;height:100%;z-index:0;pointer-events:none}
'''
t=t.replace('</style>',css+'</style>',1)
js='''
/* dot field */
(()=>{const c=document.getElementById('dots'),x=c.getContext('2d');let W,H,D=[];const dpr=Math.min(2,devicePixelRatio||1);const G=14;
const h=(a,b)=>{const s=Math.sin(a*127.1+b*311.7)*43758.5453;return s-Math.floor(s)};
function init(){W=innerWidth;H=innerHeight;c.width=W*dpr;c.height=H*dpr;x.setTransform(dpr,0,0,dpr,0,0);D=[];
 for(let j=0;j<=H/G+1;j++)for(let i=0;i<=W/G+1;i++){const X=i*G+(j%2)*G/2,Y=j*G;const u=X/W,v=Y/H;
  // base white field: denser toward lower half, fading upward
  let base=Math.pow(Math.max(0,v-.15)/.85,1.6)*.55+.05;
  // coloured clusters
  const dg=Math.hypot(u-.06,v-.08), di=Math.hypot(u-.94,v-.92), dt=Math.hypot(u-.9,v-.15);
  const g=Math.max(0,1-dg/.32), ind=Math.max(0,1-di/.42), te=Math.max(0,1-dt/.22);
  let col=[238,242,255],cw=0;
  if(g>ind&&g>te&&g>0){col=[182,228,103];cw=g}else if(ind>te&&ind>0){col=[124,110,255];cw=ind}else if(te>0){col=[47,191,165];cw=te}
  const a=Math.min(.9,base*.6+cw*.75);if(a<.03)continue;
  D.push({X,Y,a,col,ph:h(i,j)*6.28,sp:.4+h(j,i)*1.4,r:.6+cw*.7+h(i+3,j)*.5})}}
function light(){return document.body.classList.contains('light')}
function draw(T){const t=T*.001;x.clearRect(0,0,W,H);const L=light();
 for(const d of D){const f=.35+.65*Math.max(0,Math.sin(t*d.sp+d.ph));const a=d.a*f;if(a<.02)continue;
  const col=(L&&d.col[0]===238)?[30,32,48]:d.col;x.fillStyle=`rgba(${col[0]},${col[1]},${col[2]},${L?a*.7:a})`;x.beginPath();x.arc(d.X,d.Y,d.r,0,6.283);x.fill()}
 requestAnimationFrame(draw)}
addEventListener('resize',init);init();requestAnimationFrame(draw)})();
'''
t=t.replace('/* bespoke chooser */',js+'/* bespoke chooser */')
open(p,'w',encoding='utf-8').write(t)
print(t.count('homeA_nobase'))
