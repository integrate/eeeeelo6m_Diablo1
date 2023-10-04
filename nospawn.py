import pygame,fullscreen

class  Nospawn:
    def __init__(self,x,y,w,h,nospawn):
        self.rect_nospawn=pygame.Rect(x-nospawn, y-nospawn, w+nospawn*2, h+nospawn*2)
    def draw(self,screen,mul):
        rect_nospawn_fullscreen=fullscreen.fullscreen_rect(self.rect_nospawn,screen,mul)
        pygame.draw.rect(screen,[0,0,0],rect_nospawn_fullscreen,2)