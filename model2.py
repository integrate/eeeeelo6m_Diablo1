import model,time,cletca,settings,igroc_war

cletcas = []
igroc=None

def add_pole(col_x,col_y):
    global igroc
    a=range(col_y)
    b=range(col_x)
    w=(1366-(settings.PANEL_SIZE_W+settings.PANEL_OTSTUP)*2)/col_x
    h=(768-settings.POLE_OTSTUP_Y*2)/col_y
    w=min(w,h)
    h=min(w,h)
    x=1366/2-w*col_x/2
    y=768/2-h*col_y/2
    for coly in a:
        for colx in b:
            # pole = cletca.Cletca(750, 250,1366/2, 768/2)
            pole = cletca.Cletca(x+w*colx, y+h*coly, w, h)
            cletcas.append(pole)
    a=col_y*col_x
    x=a-col_x

    igroc=igroc_war.Igroc_war(cletcas[x].x,cletcas[x].y,cletcas[0].w,cletcas[0].h)

add_pole(3,3)

def dvogenie_igroc(x,y):
    for c in cletcas:
        if c.cletca.collidepoint(x,y):
            igroc.sdvig(c.cletca.x,c.cletca.y)


def step():
    pass