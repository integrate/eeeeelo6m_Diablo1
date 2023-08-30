import pygame, panelka, random, math

from Orugie import axe_energi, orugie, multi_orugie_effects
import guardian
import cletca, settings, igroc_war
import knopki
import model

cletcas = []
# wrag = igroc_war.Igroc_war(0, 0, 0, 0, 0)
# igroc = igroc_war.Igroc_war(0, 0, 0, 0, 0)
# chey_hod = 'igroc'
# panel_wrag = panelka.Panel( None, 1366 - settings.PANEL_SIZE_W)
TIMER_DO_VIBOR = pygame.event.custom_type()
TIMER_DO_ISPL = pygame.event.custom_type()
TIMER_DO_HOD = pygame.event.custom_type()

# def deystvie_lose_win():
#     global win
#     if lose:
#         exit()
#     elif win:
#         model.sostoynie = model.SOSTOYNIE_WIN_WAR
#         win=False

knopka_lose = knopki.Knopka('ВЫХОД', settings.BASE_W / 2, settings.BASE_H / 1.5, 'leelawadeeuisemilight', 30,
                            'deystvie_lose', [255, 115, 0], [255, 190, 0], border_color=[255, 190, 0])
knopka_win = knopki.Knopka('NEXT', settings.BASE_W / 2, settings.BASE_H / 1.5, 'leelawadeeuisemilight', 100,
                           'deystvie_lose_win', [255, 115, 0], [255, 190, 0], border_color=[255, 190, 0])


def add_pole(col_x, col_y, base_igroc: igroc_war.Igroc_war, base_wrag):
    global igroc
    global panel
    global wrag
    global panel_wrag
    global lose
    global win
    global knopka_lose
    global knopka_win
    global win_rect
    global chey_hod

    # подготовка к созданию
    cletcas.clear()
    a = range(col_y)
    b = range(col_x)
    w = (1366 - (settings.PANEL_SIZE_W + settings.PANEL_OTSTUP) * 2) / col_x
    h = (768 - settings.POLE_OTSTUP_Y * 2) / col_y
    w = min(w, h)
    h = min(w, h)
    x = 1366 / 2 - w * col_x / 2
    y = 768 / 2 - h * col_y / 2
    chey_hod = 'igroc'
    igroc = base_igroc
    wrag = base_wrag

    # создание поля
    for coly in a:
        for colx in b:
            # pole = cletca.Cletca(750, 250,1366/2, 768/2)
            pole = cletca.Cletca(x + w * colx, y + h * coly, w, h)
            cletcas.append(pole)

    # активация игрока
    a = col_y * col_x
    x = a - col_x
    base_igroc.activate(cletcas[x].x, cletcas[x].y, cletcas[0].w, cletcas[0].h)

    # активация врага
    x = col_x - 1
    base_wrag.activate(cletcas[x].x, cletcas[x].y, cletcas[0].w, cletcas[0].h)

    # создание панелей
    panel = panelka.Panel(base_igroc, regim='normal')
    panel_wrag = panelka.Panel(wrag, 1366 - settings.PANEL_SIZE_W)

    # подписки
    igroc.subscribe(deystvie_hod, igroc.EVENT_SMENA_MONA_HODIT)
    wrag.subscribe(deystvie_hod, igroc.EVENT_SMENA_MONA_HODIT)

    # победа/поражение
    win = False
    lose = False
    knopka_lose = knopki.Knopka('EXIT', settings.BASE_W / 2, settings.BASE_H / 1.5, 'leelawadeeuisemilight', 100,
                                deystvie_lose_win, [255, 115, 0], [255, 190, 0], border_color=[255, 190, 0])
    knopka_win = knopki.Knopka('NEXT', settings.BASE_W / 2, settings.BASE_H / 1.5, 'leelawadeeuisemilight', 100,
                               deystvie_lose_win, [255, 115, 0], [255, 190, 0], border_color=[255, 190, 0])
    knopka_lose.rect.x -= knopka_lose.picture.get_width() / 2
    knopka_win.rect.x -= knopka_win.picture.get_width() / 2


def stop_war():
    pass


def deystvie_hod(who, hod, cod_event):
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
    zona_attack = add_zona_deystviy(who.rect.center, who.active_orugie.range)

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
    if chey_hod == 'igroc':
        hero = igroc
        bad_personag = wrag
    if chey_hod == 'wrag':
        hero = wrag
        bad_personag = igroc
    return hero, bad_personag


def attack_igroc(realx, realy):
    c = find_cletca(realx, realy)
    if c == None: return

    hero, bad = who_is_who()
    if hero is wrag: return
    if hero.rect_fullscren.collidepoint(realx, realy): return
    if bad.rect_fullscren.collidepoint(realx, realy) and c.attack:
        hero.active_orugie.do_attack(bad)
        igroc.point += 2
        smena_hoda()

    elif bad.rect_fullscren.collidepoint(realx, realy) == False and c.prohod == True:
        hero.sdvig(c.cletca.x, c.cletca.y)

        if add_zona_deystviy(hero.rect.center, hero.orugie.range).colliderect(bad.rect):
            hero.active_orugie.do_attack(bad)
        smena_hoda()
    win_or_lose(wrag, igroc)


def do_vibor_vrag():
    if wrag.hp <= wrag.max_hp * 0.2:
        if wrag.orugie_2.find_avg_damage() >= wrag.orugie.find_avg_damage():
            panel_wrag.on_button_click_vibor_2()

        else:
            panel_wrag.on_button_click_vibor()
        pygame.time.set_timer(TIMER_DO_ISPL, 1500, 1)
        return
    a = random.randint(1, 2)
    if a == 1:
        panel_wrag.on_button_click_vibor()
    else:
        panel_wrag.on_button_click_vibor_2()
    pygame.time.set_timer(TIMER_DO_ISPL, 1500, 1)


def ispl_orugie_vrag():
    panel_wrag.kcopka.deystvie()
    pygame.time.set_timer(TIMER_DO_HOD, 1500, 1)


def which_cletca(distant):
    """
    команда находит клетку, дальнейшую или ближайшую к игроку.
    если min, то ближайшая, на которую можно ходить. Или клетку с играком, если его можно атаковать
    если max, то дальнейшая, на которую можно пойти

    :param distant: min / max
    :return: сletca
    """
    best = None
    a = find_cletca(igroc.rect_fullscren.x, igroc.rect_fullscren.y)
    if a.attack and distant == 'min':
        return a
    for y in cletcas:
        now = math.dist(y.cletca_fullscreen.center, igroc.rect_fullscren.center)

        if now == 0:
            pass
        elif (best == None or now < best) and y.prohod and distant == 'min':
            best = now
            best_cletca = y
        elif (best == None or now > best) and y.prohod and distant == 'max':
            best = now
            best_cletca = y

    return best_cletca


def hod_wrag():
    if win is True or lose is True: return

    if wrag.hp <= wrag.max_hp * 0.2:

        if find_cletca(igroc.rect_fullscren.x,
                       igroc.rect_fullscren.y).attack == True and wrag.active_orugie.find_avg_damage() >= igroc.hp:
            wrag.active_orugie.do_attack(igroc)
            smena_hoda()
            wrag.point += 2
            return
        cletca = which_cletca('max')
        wrag.sdvig(cletca.cletca.x, cletca.cletca.y)
        wrag.point += 1

        smena_hoda()
        return

    cletca = which_cletca('min')
    if cletca.attack and igroc.rect_fullscren.collidepoint(cletca.cletca_fullscreen.topleft):
        wrag.active_orugie.do_attack(igroc)

        wrag.point += 2
        smena_hoda()
    elif igroc.rect_fullscren.collidepoint(cletca.cletca_fullscreen.topleft) == False and cletca.prohod == True:
        wrag.sdvig(cletca.cletca.x, cletca.cletca.y)
        wrag.point += 1
        smena_hoda()


def smena_hoda():
    global chey_hod
    if lose is not True and win is not True:
        if chey_hod == 'igroc':
            chey_hod = 'wrag'
            panel.bloc()
            panel_wrag.normal()
            pygame.time.set_timer(TIMER_DO_VIBOR, 1500, 1)
        else:
            chey_hod = 'igroc'
            panel.normal()
            panel_wrag.bloc()


def effect_statistik(realx, realy):
    for a in wrag.effects + igroc.effects:
        if a.fullscreen_rect.collidepoint(realx, realy):
            a.show_statistic = True
        else:
            a.show_statistic = False


def win_or_lose(wrag, igroc):
    global lose, win
    if igroc.hp <= 0:
        lose = True
    if wrag.hp <= 0:
        win = True
    if win or lose:
        panel_wrag.regim = 'bloc'
        panel.regim = 'bloc'


def deystvie_lose_win():
    global win
    if lose:
        exit()
    elif win:
        model.sostoynie = model.SOSTOYNIE_WIN_WAR
        win = False


def step():
    pass
