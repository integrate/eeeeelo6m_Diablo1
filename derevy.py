import pygame,fullscreen,nospawn as modul_nospawn

class Derevo(modul_nospawn.Nospawn):
    def __init__(self,x,y,w,h,nospawn):
        modul_nospawn.Nospawn.__init__(self,x,y,w,h,nospawn)
        self.x=x
        self.y=y
        self.h=h
        self.w=w
        self.rect=pygame.Rect(self.x,self.y,self.w,self.h)
    def draw(self,screen,minimap=False):
        # super().draw(screen,minimap)
        derevo = pygame.Rect(fullscreen.fulscren(screen, self.rect.width, self.rect.height, self.rect.x, self.rect.y,minimap))
        pygame.draw.rect(screen, [97, 67, 9], derevo)