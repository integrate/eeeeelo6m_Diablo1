import model2,pygame,cletca as cleta
from pygame import display
screen=pygame.display.get_surface()

def view2():
    screen.fill([10,90,100])
    for cletca in model2.cletcas:
        cletca.draw(screen)
    # pygame.draw.rect(screen,[3,123,47],model2.rect)
    if model2.igroc is not None:
        model2.igroc.draw(screen)
    model2.panel.draw(screen)


    display.flip()
