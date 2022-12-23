import model2,pygame,cletca as cleta
from pygame import display
# screen=pygame.display.get_surface()
screen=display.set_mode([683, 384])
clet=cleta.Cletca(100,100,100,100)
def view2():
    screen.fill([10,90,100])
    for cletca in model2.cletcas:
        cletca.draw(screen)
    if model2.igroc is not None:
        model2.igroc.draw(screen)
        pygame.draw.rect(screen,[2,143,231],[100,100,100,100])
        clet.draw(screen)
    display.flip()
