# 1366,768
import pygame

screen = pygame.display.set_mode(flags=pygame.FULLSCREEN)
# screen = pygame.display.set_mode([683, 384])
# screen = pygame.display.set_mode([1366,768])
# print(screen.get_rect())
import model,stenaputi,fullscreen
from pygame import display, draw





def veiw():
    screen.fill([30, 255, 30])

    derevo = pygame.Rect(fullscreen.fulscren(screen,model.derevo.width, model.derevo.height, model.derevo.x, model.derevo.y))
    for stenaputi in model.steniputi:
        stenaputi.draw(screen)


    model.igroc.draw(screen)
    draw.rect(screen,[150,100,150],derevo)
    display.flip()
