# 1366,768
import pygame

screen = pygame.display.set_mode(flags=pygame.FULLSCREEN)
# screen = pygame.display.set_mode([683, 384])
# screen = pygame.display.set_mode([1366,768])
# print(screen.get_rect())
import model,stenaputi,fullscreen,settings
from pygame import display, draw

print(1366/768)
minimap_size_h=screen.get_height()/settings.PERCENTMINIMAP
minimap_size_w=screen.get_width()/settings.PERCENTMINIMAP
rect_minimap=pygame.Rect(screen.get_width()-minimap_size_w-30,30,minimap_size_w,minimap_size_h)
minimap=pygame.Surface([rect_minimap.w,rect_minimap.h])

def world(what,minimap):

    for stenaputi in model.obshie:
        stenaputi.draw(what,minimap)
    model.igroc.draw(what,minimap)

def veiw():
    screen.fill([30, 255, 30])
    world(screen,False)
    minimap.fill([73,97, 0])
    world(minimap,True)
    screen.blit(minimap,rect_minimap)
    pygame.draw.rect(screen,[0,0,0],fullscreen.fulscren(screen,model.a.w,model.a.h,model.a.x,model.a.y,False))
    display.flip()


