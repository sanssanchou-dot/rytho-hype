p='index.html';t=open(p,encoding='utf-8').read()
css='''
/* ---- 65/35 ratio: base colour owns the top 65%, colour rises only from the bottom ---- */
#bg{-webkit-mask-image:linear-gradient(180deg,transparent 0%,transparent 58%,rgba(0,0,0,.55) 74%,#000 92%);mask-image:linear-gradient(180deg,transparent 0%,transparent 58%,rgba(0,0,0,.55) 74%,#000 92%)}
#glowFloor{position:fixed;left:0;right:0;bottom:0;height:42vh;z-index:0;pointer-events:none;
 background:
  radial-gradient(70% 90% at 50% 120%,rgba(182,228,103,.55) 0%,rgba(182,228,103,0) 38%),
  radial-gradient(90% 110% at 50% 125%,rgba(47,191,165,.55) 0%,rgba(47,191,165,0) 55%),
  radial-gradient(120% 140% at 50% 135%,rgba(61,46,188,.85) 0%,rgba(61,46,188,0) 70%);
 transition:opacity .6s}
#glowFloor::after{content:"";position:absolute;inset:0;opacity:.22;mix-blend-mode:overlay;background-image:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='200' height='200'%3E%3Cfilter id='n'%3E%3CfeTurbulence baseFrequency='.9' numOctaves='3'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)'/%3E%3C/svg%3E")}
body.ai-on #glowFloor{filter:hue-rotate(-18deg) saturate(1.15)}
body.light #glowFloor{opacity:.55}
body.light #bg{opacity:.8}
.core-bg{background:radial-gradient(80% 50% at 50% 118%,rgba(61,46,188,.6),transparent 70%),radial-gradient(50% 30% at 50% 112%,rgba(182,228,103,.35),transparent 70%),#000!important}
body.light .core-bg{background:radial-gradient(80% 50% at 50% 118%,rgba(61,46,188,.22),transparent 70%),radial-gradient(50% 30% at 50% 112%,rgba(182,228,103,.3),transparent 70%),#F2F3ED!important}
#flow{opacity:.5!important}
'''
t=t.replace('</style>',css+'</style>',1)
t=t.replace('<div id="bg">','<div id="glowFloor"></div><div id="bg">',1)
# move wave lower: centre line at 82% height, thinner envelope
t=t.replace("const cy=H*(.6-.2*Math.sin(p.u*2.6+.6+t*.25));","const cy=H*(.84-.08*Math.sin(p.u*2.6+.6+t*.25));")
t=t.replace("const Y=fh*(.55-.22*Math.sin(u*3+off+t*.3)-.07*Math.sin(u*9-t*.7+off));","const Y=fh*(.86-.08*Math.sin(u*3+off+t*.3)-.04*Math.sin(u*9-t*.7+off));")
t=t.replace("const env=(.16+.14*Math.sin(p.u*3.2+t*.4)+.05*Math.sin(p.u*11-t))*(1-cur.thin*.85);","const env=(.07+.05*Math.sin(p.u*3.2+t*.4)+.02*Math.sin(p.u*11-t))*(1-cur.thin*.85);")
t=t.replace("mode.thin=y<vh*.8?1:0;mode.spread=inEx?Math.sin(clamp(ep/.8)*Math.PI):0;mode.ai=ai?1:0;","mode.thin=y<vh*.8?1:0;mode.spread=inEx?Math.sin(clamp(ep/.8)*Math.PI)*.5:0;mode.ai=ai?1:0;document.body.classList.toggle('ai-on',ai);")
open(p,'w',encoding='utf-8').write(t)
print(t.count('glowFloor'))
