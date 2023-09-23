import draw_helper
import full_igroc
import igroc_war
import model2,pygame,cletca as cleta
import time
from pygame import display
import igroc
import nospawn
import real_world_object
import settings
import wrag_skelet

screen=pygame.display.get_surface()
a=time.time()
def view2():



    if model2.lose==False and model2.win==False:
        fight()
    if model2.lose==True:
        lose()
    if model2.win == True:
        win()



    display.flip()


def fight():
    screen.fill([10, 90, 100])
    for cletca in model2.cletcas:
        cletca.draw(screen)
    import guardian
    print("MRO:", [x.__name__ for x in wrag_skelet.Wrag_skelet.__mro__])
    super(igroc.Igroc,model2.igroc).draw(screen)
    super(nospawn.Nospawn,model2.wrag).draw(screen)

    # model2.igroc.draw(screen)

    model2.panel.draw(screen)
    # model2.wrag.draw(screen)
    model2.panel_wrag.draw(screen)

def lose():
    global a
    if a>time.time()-0.15:
        screen.fill([10,10,10])
        draw_helper.draw_txt(screen, 'GAME OVER', 'arial', 100, [250, 70, 70])
    elif a>time.time()-0.3:
        screen.fill([0,0,0])
        draw_helper.draw_txt(screen, 'GAME OVER', 'arial', 100, [190, 0, 0])
    else:
        a = time.time()
    model2.knopka_lose.draw(screen)


def win():
    model2.knopka_win.draw(screen)
    # pygame.draw.rect(screen,[0,0,0],model2.win_rect)