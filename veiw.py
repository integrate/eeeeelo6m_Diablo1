# 1366,768
import pygame

screen = pygame.display.set_mode(flags=pygame.FULLSCREEN)
# screen = pygame.display.set_mode([683, 384])

import model,stenaputi,fullscreen
from pygame import display, draw





def veiw():
    screen.fill([30, 255, 30])
    igroc = pygame.Rect(fullscreen.fulscren(screen,model.igroc.width, model.igroc.height, model.igroc.x, model.igroc.y,))
    derevo = pygame.Rect(fullscreen.fulscren(screen,model.derevo.width, model.derevo.height, model.derevo.x, model.derevo.y))
    for stenaputi in model.steniputi:
        stenaputi.draw(screen)


    draw.rect(screen, [255, 30, 30], igroc)
    draw.rect(screen,[150,100,150],derevo)
    display.flip()
