import draw_helper
import model2,pygame,cletca as cleta
import time
from pygame import display
screen=pygame.display.get_surface()
a=time.time()
def view2():



    if model2.lose==False:
        fight()
    if model2.lose==True:
        lose()



    display.flip()


def fight():
    screen.fill([10, 90, 100])
    for cletca in model2.cletcas:
        cletca.draw(screen)
    model2.igroc.draw(screen)
    model2.panel.draw(screen)
    model2.wrag.draw(screen)
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