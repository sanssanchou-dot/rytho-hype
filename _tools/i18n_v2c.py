p = 'C:/Users/san/.001_OPQ_Design_Project/PROJECTS/_SOUND/20260714_speaker/output/RYTHO_HYPE_WEB/v2-src/src/data.ts'
t = open(p, encoding='utf-8').read()
a = 'const IMG_BASE = here.includes("/assets/") ? here.slice(0, here.lastIndexOf("/assets/")) + "/../img/" : "/img/"'
b = 'const IMG_BASE = here.includes("/assets/") ? new URL(here.slice(0, here.lastIndexOf("/assets/")) + "/../img/").href : "/img/"'
assert a in t; t = t.replace(a, b); open(p, 'w', encoding='utf-8').write(t); print('ok')
