import pygame,fullscreen

class  Nospawn:
    def __init__(self,x,y,w,h,nospawn):
        self.rect_nospawn=pygame.Rect(x-nospawn, y-nospawn, w+nospawn*2, h+nospawn*2)
    def draw(self,screen,minimap):
        rect_nospawn_fullscreen=pygame.Rect(fullscreen.fulscren(screen,self.rect_nospawn.w,self.rect_nospawn.h,self.rect_nospawn.x,self.rect_nospawn.y,minimap))
        pygame.draw.rect(screen,[0,0,0],rect_nospawn_fullscreen)