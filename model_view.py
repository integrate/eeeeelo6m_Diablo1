import pygame,settings

def smena_minimap():
    global minimap,rect_minimap
    screen=pygame.display.get_surface()
    minimap_size_h = screen.get_height() / settings.PERCENTMINIMAP
    minimap_size_w = screen.get_width() / settings.PERCENTMINIMAP
    rect_minimap = pygame.Rect(screen.get_width() - minimap_size_w - 30, 30, minimap_size_w, minimap_size_h)
    minimap = pygame.Surface([rect_minimap.w, rect_minimap.h])
smena_minimap()