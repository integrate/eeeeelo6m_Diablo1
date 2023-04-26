import pygame, panelka, random
import model, time, cletca, settings, igroc_war, orugie

cletcas = []
igroc = igroc_war.Igroc_war(0, 0, 0, 0, 0)
wrag = igroc_war.Igroc_war(0, 0, 0, 0, 0)
chey_hod = 'igroc'


def add_pole(col_x, col_y):
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
    orugie_igroc = orugie.Orugie([0, 100], 'легендарный топор который претворяется молотом', 'picture/топор.png', 2)
    orugie_igroc_2 = orugie.Orugie([-300, 300], 'может как и убить так и добавить здоровье врагу', 'picture/коса_исцеления.png', 2)
    igroc = igroc_war.Igroc_war(cletcas[x].x, cletcas[x].y, cletcas[0].w, cletcas[0].h, 100, deystvie_hod=deystvie_hod,
                                orugie=orugie_igroc,orugie_2=orugie_igroc_2)
    panel = panelka.Panel([0, 1000], igroc, regim='normal')
    x = col_x - 1
    orugie_wrag = orugie.Orugie([-300, 300], 'легендарный молотом', 'picture/коса_исцеления.png', 2)
    orugie_wrag_2 = orugie.Orugie([-300, 300], 'легендарный молотом', 'picture/коса_исцеления.png', 2)

    wrag = igroc_war.Igroc_war(cletcas[x].x, cletcas[x].y, cletcas[0].w, cletcas[0].h, 100, deystvie_hod=deystvie_hod,
                               color=[38, 242, 29],
                               cletca_color=[random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)],
                               orugie=orugie_wrag,orugie_2=orugie_wrag_2)
    panel_wrag = panelka.Panel([0, 10], wrag, 1366 - settings.PANEL_SIZE_W)


def deystvie_hod(hod, who):
    if hod:
        do_prohod(who)
    else:
        no_prohod()


def add_zona_deystviy(center, rang):
    wh = cletcas[0].w * (rang * 2 + 1) - 2
    rect = pygame.Rect([center[0] - wh / 2, center[1] - wh / 2, wh, wh])
    return rect


def do_prohod(who):
    zona_hod = add_zona_deystviy(who.rect.center, who.stamina)
    zona_attack = add_zona_deystviy(who.rect.center, who.orugie.range)

    for c in cletcas:
        c.color = who.cletca_color
        c.prohod = c.cletca.colliderect(zona_hod)
        c.attack = c.cletca.colliderect(zona_attack)


def no_prohod():
    for c in cletcas:
        c.prohod = False
        c.attack = False


# def dvogenie_igroc(realx, realy):
#     global chey_hod
#     for c in cletcas:
#         if c.prohod == True and c.cletca_fullscreen.collidepoint(realx, realy):
#             if chey_hod == 'igroc':
#                 igroc.sdvig(c.cletca.x, c.cletca.y)
#                 smena_hoda()
#             elif chey_hod == 'wrag':
#                 wrag.sdvig(c.cletca.x, c.cletca.y)
#                 smena_hoda()



def find_cletca(realx, realy):
    for c in cletcas:
        if c.cletca_fullscreen.collidepoint(realx, realy):
            return c
    return None

def who_is_who():
    if chey_hod=='igroc':
        hero=igroc
        bad_personag=wrag
    if chey_hod=='wrag':
        hero=wrag
        bad_personag=igroc
    return hero,bad_personag

def attack_igroc(realx, realy):
    c=find_cletca(realx,realy)
    if c==None: return

    hero,bad=who_is_who()
    if hero.rect.collidepoint(realx,realy): return
    if bad.rect.collidepoint(realx,realy) and c.attack:
        bad.hp -= hero.orugie.do_damage()
        smena_hoda()
    elif bad.rect.collidepoint(realx,realy)==False and c.prohod==True:
        hero.sdvig(c.cletca.x, c.cletca.y)
        smena_hoda()


def smena_hoda():
    global chey_hod
    if chey_hod=='igroc':
        chey_hod = 'wrag'
        panel.regim = 'bloc'
        panel_wrag.regim = 'normal'
        igroc.mona_hodit = False
    else:
        chey_hod = 'igroc'
        panel.regim = 'normal'
        panel_wrag.regim = 'bloc'
        wrag.mona_hodit = False


def step():
    pass


add_pole(10, 10)
