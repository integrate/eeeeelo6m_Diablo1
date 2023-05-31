import model2,pygame,cletca as cleta
from pygame import display
screen=pygame.display.get_surface()

def view2():
    screen.fill([10,90,100])
    for cletca in model2.cletcas:
        cletca.draw(screen)
    # pygame.draw.rect(screen,[3,123,47],model2.rect)

    model2.igroc.draw(screen)
    model2.panel.draw(screen)
    model2.wrag.draw(screen)
    model2.panel_wrag.draw(screen)




    display.flip()
