p='index.html';t=open(p,encoding='utf-8').read()
t=t.replace('<div class="orb rv"><i class="rim r1"></i><i class="rim r2"></i><i class="rim r3"></i><i class="caus"></i></div>',
 '<div class="orb rv"><span class="wave" aria-hidden="true"></span></div>',1)
css='''
/* ---- UX pass 1 ---- */
/* AI orb = listening waveform inside a glass pill */
.orb>.rim,.orb>.caus{display:none!important}
.orb{background:transparent!important}
.orb .wave{position:absolute;inset:0;display:flex;align-items:center;justify-content:center;gap:5px;z-index:2}
.orb .wave i{display:block;width:3px;border-radius:3px;height:8%;background:linear-gradient(180deg,#E6FF8A,var(--acc));opacity:.9;
 animation:lis 1.6s ease-in-out infinite;animation-delay:calc(var(--k) * -0.11s)}
@keyframes lis{0%,100%{height:var(--lo)}50%{height:var(--hi)}}
body.light .orb .wave i{background:linear-gradient(180deg,#a4d400,#6e9600)}
/* mobile */
@media(max-width:900px){
 #s-family .fam{grid-template-columns:repeat(2,minmax(0,1fr))!important;gap:14px 12px!important}
 #s-family .fam em{white-space:normal!important}
 #s-family .fam b{font-size:15px!important}#s-family .fam span{font-size:14px!important}
 .say{font-size:clamp(26px,7.4vw,40px)!important;text-wrap:balance}
 .pd-arch img{border-radius:16px}
 #exBtn{bottom:4vh}
}
.say{text-wrap:balance}
'''
t=t.replace('</style>',css+'</style>',1)
js='''
/* listening waveform bars */
(()=>{const w=document.querySelector('.orb .wave');if(!w)return;const N=29;let h='';for(let k=0;k<N;k++){const c=1-Math.abs(k-(N-1)/2)/((N-1)/2);const hi=Math.round(18+70*Math.pow(c,1.4)*(.6+.4*Math.abs(Math.sin(k*1.7))));h+=`<i style="--k:${k};--lo:${Math.max(6,Math.round(hi*.22))}%;--hi:${hi}%"></i>`}w.innerHTML=h})();
'''
t=t.replace('/* bespoke chooser',js+'/* bespoke chooser',1)
open(p,'w',encoding='utf-8').write(t);print('ok')
