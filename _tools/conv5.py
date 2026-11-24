from PIL import Image
S='../RYTHO_HYPE_RENDER_PROOFS_20261123/'
m={'bespoke_style_v2/fin_r4_%s.png'%k:'img/fin_%s.webp'%k for k in ['black_anodized','champagne','graphite','white_ceramic','rytho_lime','bronze']}
m.update({'bespoke_style_v2/hifi_r5_%s.png'%k:'img/hifi_%s.webp'%k for k in ['walnut','teak_alu','piano_marble']})
m.update({'portable_dark/portable_dark_2048.png':'img/p01_dark.webp','portable_dark/portable_light_2048.png':'img/p01_light.webp','scene_03_nordic/scene_03_wide_2560.png':'img/scene_03_wide.webp','scene_03_nordic/scene_03_detail.png':'img/scene_03_detail.webp'})
for a,b in m.items():
    Image.open(S+a).convert('RGB').save(b,'WEBP',quality=88,method=6)
print(len(m))
