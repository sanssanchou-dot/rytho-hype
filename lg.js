/* Liquid glass: edge-refraction displacement maps (after rdev/liquid-glass-react / shuding/liquid-glass),
   chromatic split, thickness rims, Rytho-green key light. Chromium uses backdrop-filter:url(); others fall back to blur. */
(()=>{
const NS='http://www.w3.org/2000/svg';
const host=document.createElementNS(NS,'svg');host.setAttribute('width','0');host.setAttribute('height','0');
host.style.cssText='position:absolute;width:0;height:0;pointer-events:none';document.body.appendChild(host);
const chromium=!!window.chrome&&CSS.supports('backdrop-filter','blur(1px)');
let uid=0;

/* displacement map from a shape mask: vector distance transform -> outward normal * bevel profile */
function buildMap(W,H,draw,B,openLeft){
  const w=W+2,h=H+2,c=document.createElement('canvas');c.width=w;c.height=h;const x=c.getContext('2d');
  x.translate(1,1);x.fillStyle='#fff';draw(x);if(openLeft){x.setTransform(1,0,0,1,0,0);
    const col=x.getImageData(1,0,1,h).data;const id=x.createImageData(1,h);id.data.set(col);x.putImageData(id,0,0)}
  const m=x.getImageData(0,0,w,h).data,N=w*h,vx=new Float32Array(N),vy=new Float32Array(N),BIG=1e6;
  for(let i=0;i<N;i++){if(m[i*4+3]>127){vx[i]=BIG;vy[i]=BIG}}
  const L=(i)=>vx[i]*vx[i]+vy[i]*vy[i];
  const tr=(i,j,ox,oy)=>{const ax=vx[j]+ox,ay=vy[j]+oy;if(ax*ax+ay*ay<L(i)){vx[i]=ax;vy[i]=ay}};
  for(let y=0;y<h;y++){for(let X=0;X<w;X++){const i=y*w+X;if(X>0)tr(i,i-1,-1,0);if(y>0){tr(i,i-w,0,-1);if(X>0)tr(i,i-w-1,-1,-1);if(X<w-1)tr(i,i-w+1,1,-1)}}
    for(let X=w-2;X>=0;X--){const i=y*w+X;tr(i,i+1,1,0)}}
  for(let y=h-1;y>=0;y--){for(let X=w-1;X>=0;X--){const i=y*w+X;if(X<w-1)tr(i,i+1,1,0);if(y<h-1){tr(i,i+w,0,1);if(X<w-1)tr(i,i+w+1,1,1);if(X>0)tr(i,i+w-1,-1,1)}}
    for(let X=1;X<w;X++){const i=y*w+X;tr(i,i-1,-1,0)}}
  const o=document.createElement('canvas');o.width=W;o.height=H;const ox=o.getContext('2d'),od=ox.createImageData(W,H),d=od.data;
  for(let y=0;y<H;y++)for(let X=0;X<W;X++){const i=(y+1)*w+X+1,p=(y*W+X)*4;let r=.5,g=.5;
    if(m[i*4+3]>127){const D=Math.sqrt(L(i));if(D<B&&D>0){const t=1-D/B,mag=t*t*(3-2*t)*.5;r=.5+vx[i]/D*mag;g=.5+vy[i]/D*mag}}
    d[p]=r*255;d[p+1]=g*255;d[p+2]=128;d[p+3]=255}
  ox.putImageData(od,0,0);const s2=document.createElement('canvas');s2.width=W;s2.height=H;const sx=s2.getContext('2d');sx.filter='blur(1.2px)';sx.drawImage(o,0,0);return s2.toDataURL();
}
function filterEl(id,W,H,url,S){
  const f=document.createElementNS(NS,'filter');f.id=id;
  f.setAttribute('x','0');f.setAttribute('y','0');f.setAttribute('width',W);f.setAttribute('height',H);
  f.setAttribute('filterUnits','userSpaceOnUse');f.setAttribute('primitiveUnits','userSpaceOnUse');f.setAttribute('color-interpolation-filters','sRGB');
  const ch=(k,s,mat)=>`<feDisplacementMap in="SourceGraphic" in2="map" scale="${s}" xChannelSelector="R" yChannelSelector="G" result="d${k}"/><feColorMatrix in="d${k}" type="matrix" values="${mat}" result="c${k}"/>`;
  f.innerHTML=`<feImage href="${url}" x="0" y="0" width="${W}" height="${H}" preserveAspectRatio="none" result="map"/>`+
   ch('r',S,'1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0')+ch('g',S*.93,'0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 1 0')+ch('b',S*.86,'0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 1 0')+
   `<feBlend in="cr" in2="cg" mode="screen" result="rg"/><feBlend in="rg" in2="cb" mode="screen"/>`;
  return f;
}
function apply(el,layer,W,H,draw,opt){
  if(W<4||H<4)return;const B=opt.bevel||Math.min(18,Math.min(W,H)*.42),S=-(opt.scale||B*1.6);
  const id='lgf'+(++uid);const url=buildMap(W,H,draw,B,opt.openLeft);
  if(layer.__lgf)layer.__lgf.remove();const f=filterEl(id,W,H,url,S);host.appendChild(f);layer.__lgf=f;
  const bl=opt.blur??3;
  layer.style.backdropFilter=layer.style.webkitBackdropFilter=chromium?`blur(${bl}px) url(#${id}) saturate(165%) brightness(1.04)`:`blur(${bl+10}px) saturate(165%)`;
}
function radius(el,W,H){const r=parseFloat(getComputedStyle(el).borderTopRightRadius)||0;return Math.min(r,H/2,W/2)}
function rrect(W,H,r){return x=>{x.beginPath();x.roundRect(0,0,W,H,r);x.fill()}}

/* generic rounded elements */
function glassify(el){
  if(el.__lg)return;el.__lg=1;el.classList.add('lgx');
  el.insertAdjacentHTML('afterbegin','<i class="lg-b"></i>');el.insertAdjacentHTML('beforeend','<i class="lg-t"></i>');
  const b=el.querySelector(':scope>.lg-b');
  const run=()=>{const W=Math.round(el.offsetWidth),H=Math.round(el.offsetHeight);if(!W||!H)return;if(b.__wh===W+'x'+H)return;b.__wh=W+'x'+H;apply(el,b,W,H,rrect(W,H,radius(el,W,H)),{})};
  new ResizeObserver(()=>{clearTimeout(el.__lgT);el.__lgT=setTimeout(run,60)}).observe(el);run();
}
/* rail: shape comes from the clip-path the rail script writes */
function rail(){
  const s=document.querySelector('#rail .rshape');if(!s)return;
  const go=()=>{const m=/path\(["']?([^"')]+)/.exec(s.style.clipPath||'');if(!m)return;const W=s.offsetWidth,H=s.offsetHeight;
    if(s.__d===m[1]+W+H)return;s.__d=m[1]+W+H;const P=new Path2D(m[1]);apply(s,s,W,H,x=>x.fill(P),{openLeft:true,bevel:16,scale:26,blur:3});
    /* thickness for the custom shape: blurred inner strokes clipped to the shape */
    const sv=document.querySelector('#rail .redge');if(!sv)return;let g=sv.querySelector('.lg-th');
    if(!g){sv.insertAdjacentHTML('afterbegin',`<defs><clipPath id="railClip"><path/></clipPath><filter id="railSoft" x="-20%" y="-20%" width="140%" height="140%"><feGaussianBlur stdDeviation="3"/></filter></defs><g class="lg-th" clip-path="url(#railClip)"><path class="t1" filter="url(#railSoft)"/><path class="t2" filter="url(#railSoft)"/><path class="t3"/></g>`);g=sv.querySelector('.lg-th')}
    const open=sv.querySelector(':scope>path').getAttribute('d');sv.querySelector('#railClip path').setAttribute('d',m[1]);
    g.querySelectorAll('path').forEach(p=>p.setAttribute('d',open));};
  new MutationObserver(go).observe(s,{attributes:true,attributeFilter:['style']});go();
}
const SEL=['#themeT','#chipTitle','.seg2','#exBtn','#s-partner .col.glass'];
function init(){document.querySelectorAll(SEL.join(',')).forEach(glassify);rail()}
if(document.readyState==='complete')init();else addEventListener('load',init);
})();
