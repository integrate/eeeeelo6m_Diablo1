import pygame, panelka, random
import model, time, cletca, settings, igroc_war, orugie

cletcas = []
igroc = igroc_war.Igroc_war(0, 0, 0, 0, 0)
wrag = igroc_war.Igroc_war(0, 0, 0, 0, 0)
chey_hod = 'igroc'


def add_pole(col_x, col_y):
    global rect
    global igroc
    global panel
    global wrag
    global panel_wrag

    a = range(col_y)
    b = range(col_x)
    w = (1366 - (settings.PANEL_SIZE_W + settings.PANEL_OTSTUP) * 2) / col_x
    h = (768 - settings.POLE_OTSTUP_Y * 2) / col_y
    w = min(w, h)
    h = min(w, h)
    x = 1366 / 2 - w * col_x / 2
    y = 768 / 2 - h * col_y / 2

    for coly in a:
        for colx in b:
            # pole = cletca.Cletca(750, 250,1366/2, 768/2)
            pole = cletca.Cletca(x + w * colx, y + h * coly, w, h)
            cletcas.append(pole)
    a = col_y * col_x
    x = a - col_x
    orugie_igroc = orugie.Orugie([0, 100], 'легендарный топор который претворяется молотом', 'picture/топор.png', 0)
    igroc = igroc_war.Igroc_war(cletcas[x].x, cletcas[x].y, cletcas[0].w, cletcas[0].h, 100, deystvie_hod=deystvie_hod,
                                orugie=orugie_igroc)
    panel = panelka.Panel([0, 1000], igroc, regim='normal')
    x = col_x - 1
    orugie_wrag = orugie.Orugie([25, 250], 'легендарный молотом', 'picture/топор.png', 0)

    wrag = igroc_war.Igroc_war(cletcas[x].x, cletcas[x].y, cletcas[0].w, cletcas[0].h, 100, deystvie_hod=deystvie_hod,
                               color=[38, 242, 29],
                               cletca_color=[random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)],
                               orugie=orugie_wrag)
    panel_wrag = panelka.Panel([0, 10], wrag, 1366 - settings.PANEL_SIZE_W)


def deystvie_hod(hod, who):
    if hod:
        do_prohod(who)
    else:
        no_prohod()


def do_prohod(who):
    global rect
    w = cletcas[0].w * (igroc.stamina * 2 + 1) - 2
    rect = pygame.Rect([who.rect.centerx - w / 2, who.rect.centery - w / 2, w, w])
    for c in cletcas:
        c.color = who.cletca_color
        if c.cletca.colliderect(rect):
            c.prohod = True
        else:
            c.prohod = False


def no_prohod():
    for c in cletcas:
        c.prohod = False


def dvogenie_igroc(realx, realy):
    global chey_hod
    for c in cletcas:
        if c.prohod == True and c.cletca_fullscreen.collidepoint(realx, realy):
            if chey_hod == 'igroc':
                igroc.sdvig(c.cletca.x, c.cletca.y)

                panel.regim = 'bloc'
                igroc.mona_hodit = False
                chey_hod = 'wrag'
                panel_wrag.regim = 'normal'
                if igroc.rect.colliderect(wrag):
                    wrag.hp -= 10
            elif chey_hod == 'wrag':
                wrag.sdvig(c.cletca.x, c.cletca.y)

                panel_wrag.regim = 'bloc'
                wrag.mona_hodit = False
                chey_hod = 'igroc'
                panel.regim = 'normal'


def step():
    # if panel_wrag.regim in ['hod','vibor'] and panel.regim=='vibor':
    #     panel.regim='normal'
    pass


add_pole(10, 10)
