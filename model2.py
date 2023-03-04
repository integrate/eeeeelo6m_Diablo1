import pygame,panelka
import model,time,cletca,settings,igroc_war

cletcas = []
igroc=None
def add_pole(col_x,col_y):
    global rect
    global igroc
    global panel
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


    igroc=igroc_war.Igroc_war(cletcas[x].x,cletcas[x].y,cletcas[0].w,cletcas[0].h,100)
    panel=panelka.Panel([0,1000],igroc)




def do_prohod():
    global rect
    w=cletcas[0].w*(igroc.stamina*2+1)-2
    rect=pygame.Rect([igroc.rect.centerx-w/2,igroc.rect.centery-w/2,w,w])
    for c in cletcas:
        if c.cletca.colliderect(rect):
            c.prohod=True
        else:
            c.prohod=False

def no_prohod():
    for c in cletcas:
        c.prohod=False

def vibor_orugiy(realx,realy):
    panel.pereponel(realx,realy)



def hod():
    if panel.regim=='hod':
        igroc.mona_hodit=True
        do_prohod()

    else:
        igroc.mona_hodit=False
        no_prohod()



def dvogenie_igroc(realx,realy):
    for c in cletcas:
        if c.prohod==True and c.cletca_fullscreen.collidepoint(realx,realy):
            igroc.sdvig(c.cletca.x,c.cletca.y)
            igroc.hp-=1
            panel.regim='normal'






def step():
    pass
add_pole(5,6)