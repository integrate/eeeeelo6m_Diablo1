import model2,pygame,cletca as cleta
from pygame import display
screen=pygame.display.get_surface()
def view2():
    screen.fill([10,90,100])
    model2.pole.draw(screen)

    display.flip()
