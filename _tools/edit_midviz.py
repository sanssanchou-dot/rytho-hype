p='index.html';t=open(p,encoding='utf-8').read()
old='<section id="s-core"><div class="core-bg"></div><div class="wrap">'
assert old in t
t=t.replace(old,'''<section id="s-core"><div class="core-bg"></div>
<div class="midviz" aria-hidden="true"><img src="img/mid_explode.webp" width="3200" height="1400" alt=""><canvas id="midCv"></canvas>
 <span class="mvl" id="mvlD">GLASS DIAPHRAGM<em>玻音先創 透明振膜</em></span>
 <span class="mvl" id="mvlS">SPIRAL = PORT LENGTH<em>螺旋葉片即導音管</em></span>
 <span class="mvl" id="mvlP">PORT<em>出氣口</em></span></div>
<div class="wrap">''',1)
css='''
/* ---- statement: mid module side explode + visible acoustics ---- */
#s-core{position:relative}
#s-core .wrap{position:relative;z-index:2}
#s-core .say{text-shadow:0 0 40px #000,0 0 80px #000}
body.light #s-core .say{text-shadow:0 0 40px var(--bgL,#F2F3ED),0 0 80px var(--bgL,#F2F3ED)}
.midviz{position:absolute;left:50%;top:50%;width:min(100vw - 100px,1900px);aspect-ratio:3200/1400;transform:translate(-50%,-50%);z-index:1;pointer-events:none}
.midviz img{position:absolute;inset:0;width:100%;height:100%;opacity:.42}
body.light .midviz img{opacity:.75;filter:invert(1) hue-rotate(180deg) contrast(.9)}
.midviz canvas{position:absolute;inset:0;width:100%;height:100%}
.mvl{position:absolute;font:500 10px var(--mono);letter-spacing:.14em;color:var(--acc);white-space:nowrap;transform:translateX(-50%)}
.mvl em{display:block;font:400 10.5px var(--zh);letter-spacing:.04em;color:var(--mute);font-style:normal;margin-top:3px}
body.light .mvl{color:#6f9a00}
@media(max-width:900px){.midviz{width:140vw}.mvl{display:none}}
'''
t=t.replace('</style>',css+'</style>',1)
js=r'''
/* mid module acoustics: front radiation from the glass diaphragm, back wave through the spiral, out the port */
(()=>{const box=document.querySelector('.midviz'),cv=document.getElementById('midCv');if(!box||!cv)return;const x=cv.getContext('2d');let D=null,W=0,H=0,dpr=1,P=[],L=[],tot=0,run=false;
fetch('img/mid_paths.json').then(r=>r.json()).then(d=>{D=d;prep();size();place();run=true;requestAnimationFrame(f)}).catch(()=>{});
function prep(){P=D.path;L=[0];for(let i=1;i<P.length;i++)L.push(L[i-1]+Math.hypot((P[i][0]-P[i-1][0])*3200,(P[i][1]-P[i-1][1])*1400));tot=L[L.length-1]}
function at(s){let i=1;while(i<L.length&&L[i]<s)i++;if(i>=L.length)return P[P.length-1];const a=P[i-1],b=P[i],k=(s-L[i-1])/(L[i]-L[i-1]||1);return [a[0]+(b[0]-a[0])*k,a[1]+(b[1]-a[1])*k,(a[2]==null||b[2]==null)?null:a[2]+(b[2]-a[2])*k,b[3]]}
function size(){const r=box.getBoundingClientRect();dpr=Math.min(2,devicePixelRatio||1);W=r.width;H=r.height;cv.width=W*dpr;cv.height=H*dpr;x.setTransform(dpr,0,0,dpr,0,0)}
function place(){const d=D.dia,p=D.port,s=D.path.filter(q=>q[3]==='sp');const mid=s[Math.floor(s.length*.45)];
 const set=(id,X,Y)=>{const e=document.getElementById(id);e.style.left=X*100+'%';e.style.top=Y*100+'%'};
 set('mvlD',d.x,d.bottom_y+.07);set('mvlS',mid[0],(p.y_outer_top_bottom[1])+.07);set('mvlP',p.x+.012,p.y_outer_top_bottom[0]-.12)}
addEventListener('resize',()=>{if(D){size()}});
const light=()=>document.body.classList.contains('light');
const col=a=>light()?`rgba(111,154,0,${a})`:`rgba(198,244,50,${a})`;
const vis=()=>{const r=box.getBoundingClientRect();return r.bottom>0&&r.top<innerHeight};
const reduce=matchMedia('(prefers-reduced-motion: reduce)').matches;
function f(T){if(!run)return;requestAnimationFrame(f);if(!vis())return;const t=reduce?2000:T;x.clearRect(0,0,W,H);
 const d=D.dia,cx=d.x_rim*W,cy=d.centre[1]*H,R=(d.bottom_y-d.top_y)/2*H;
 // diaphragm: thin lit edge breathing like a piston
 const pis=Math.sin(t/1000*2*Math.PI*1.25)*2.2;x.strokeStyle=col(.9);x.lineWidth=1.6;x.beginPath();x.moveTo(cx+pis,cy-R);x.lineTo(cx+pis,cy+R);x.stroke();
 // front radiation: wavefronts opening to the left
 for(let k=0;k<5;k++){const ph=((t/1000*1.25+k/5)%1);const r=R*.9+ph*cx*1.05;const a=(1-ph)*.55;x.strokeStyle=col(a);x.lineWidth=1.2;x.beginPath();x.arc(cx,cy,r,Math.PI-.62,Math.PI+.62);x.stroke()}
 // spiral channels: faint guide lines (far side dimmer)
 for(const ch of D.chs){for(let i=1;i<ch.length;i++){const a=ch[i-1],b=ch[i];const tc=b[2]==null?0:b[2];x.strokeStyle=col(tc>0?.22:.07);x.lineWidth=tc>0?1.1:.8;x.beginPath();x.moveTo(a[0]*W,a[1]*H);x.lineTo(b[0]*W,b[1]*H);x.stroke()}}
 // back wave particles along the measured path
 const N=34,sp=tot/5200;for(let k=0;k<N;k++){const s=((t*sp)+k*tot/N)%tot;for(let j=0;j<6;j++){const q=at(Math.max(0,s-j*7));if(!q)continue;const seg=q[3];let a=(1-j/6)*(seg==='ex'?.25:seg==='ou'?.5:.95);if(q[2]!=null&&q[2]<0)a*=.35;
   x.fillStyle=col(a);x.beginPath();x.arc(q[0]*W,q[1]*H,j?1.2:2.1,0,6.283);x.fill()}}
 // port: wavefronts leaving the outlet to the right
 const p=D.port,px=p.x_range[1]*W,py=.5*H,PR=(p.y_outer_top_bottom[1]-p.y_outer_top_bottom[0])/2*H;
 for(let k=0;k<4;k++){const ph=((t/1000*.8+k/4)%1);const r=PR*.6+ph*Math.min(W-px,PR*2.2);x.strokeStyle=col((1-ph)*.4);x.lineWidth=1;x.beginPath();x.arc(px-PR*.6,py,r,-.5,.5);x.stroke()}
}})();
'''
t=t.replace('/* bespoke chooser',js+'/* bespoke chooser',1)
open(p,'w',encoding='utf-8').write(t);print('ok')
