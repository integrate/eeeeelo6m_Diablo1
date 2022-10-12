# 1366,768
import pygame

screen = pygame.display.set_mode(flags=pygame.FULLSCREEN)
# screen = pygame.display.set_mode([683, 384])
# screen = pygame.display.set_mode([1366,768])
# print(screen.get_rect())
import model,stenaputi,fullscreen
from pygame import display, draw

print(1366/768)

minimap=pygame.Surface([150*1.7786458333333333,150])

def world(what):
    for stenaputi in model.obshie:
        stenaputi.draw(what)
    model.igroc.draw(what)

def veiw():
    screen.fill([30, 255, 30])
    world(screen)
    minimap.fill([73,97, 0])
    world(minimap)
    screen.blit(minimap,[1336-minimap.get_width(),30])





    display.flip()


