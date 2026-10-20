from PIL import Image, ImageDraw, ImageFont
import sys
BG=(13,13,13); ORANGE=(255,109,0); GREEN=(6,214,160)
FONT='/usr/share/fonts/truetype/google-fonts/Poppins-Bold.ttf'
def draw(size, scale=1.0, S=4):
    W=size*S; im=Image.new('RGB',(W,W),BG); d=ImageDraw.Draw(im)
    k=W/512*scale; cx=cy=W/2
    def X(v): return cx+(v-256)*k
    def Y(v): return cy+(v-256)*k
    def rr(x0,y0,x1,y1,r,fill): d.rounded_rectangle((X(x0),Y(y0),X(x1),Y(y1)),radius=r*k,fill=fill)
    # topes y barra
    rr(30,238,482,274,18,ORANGE)
    # discos exteriores
    rr(52,176,92,336,18,ORANGE); rr(420,176,460,336,18,ORANGE)
    # discos interiores
    rr(100,140,150,372,20,ORANGE); rr(362,140,412,372,20,ORANGE)
    # letras BG integradas al centro
    f=ImageFont.truetype(FONT, int(138*k))
    bb=d.textbbox((0,0),'BG',font=f)
    tw=bb[2]-bb[0]; th=bb[3]-bb[1]
    # fondo negro detrás de las letras para que "corten" la barra
    pad=14*k
    d.rectangle((X(156),Y(120),X(356),Y(392)),fill=BG)
    d.text((cx-tw/2-bb[0], cy-th/2-bb[1]), 'BG', font=f, fill=GREEN)
    return im.resize((size,size), Image.LANCZOS)
out=sys.argv[1]
for name,size,scale in [('icon-512.png',512,1.0),('icon-192.png',192,1.0),('icon-180.png',180,1.0),('favicon-32.png',32,1.0),('icon-maskable-512.png',512,0.74)]:
    draw(size,scale).save(f'{out}/{name}')
