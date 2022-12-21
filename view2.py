import model2,pygame,cletca as cleta
from pygame import display
screen=pygame.display.get_surface()
def view2():
    screen.fill([10,90,100])
    for cletca in model2.cletcas:
        cletca.draw(screen)

    display.flip()
