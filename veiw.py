# 1366,768
import pygame

screen = pygame.display.set_mode(flags=pygame.FULLSCREEN)
# screen = pygame.display.set_mode([683, 384])
# screen = pygame.display.set_mode([1366,768])
# print(screen.get_rect())
import model,stenaputi,fullscreen
from pygame import display, draw

print(1366/768)

minimap=pygame.Surface([250*1.7786458333333333,250])

def world(what,minimap):

    for stenaputi in model.obshie:
        stenaputi.draw(what,minimap)
    model.igroc.draw(what,minimap)

def veiw():
    screen.fill([30, 255, 30])
    world(screen,False)
    minimap.fill([73,97, 0])
    world(minimap,True)
    screen.blit(minimap,[1336-minimap.get_width(),30])





    display.flip()


