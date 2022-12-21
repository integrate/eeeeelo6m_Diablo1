import pygame,fullscreen

class Cletca():
    def __init__(self,x,y,w,h,sostoynie='svobodna'):
        self.x=x
        self.y=y
        self.w=w
        self.h=h
        self.sostoynie=sostoynie
        self.cletca=pygame.Rect(self.x,self.y,self.w,self.h)
    def draw(self,screen):

        cletca=fullscreen.fullscreen_rect(self.cletca,screen,'war',False)
        pygame.draw.rect(screen,[255,255,255],cletca)
        pygame.draw.rect(screen,[0,0,0],cletca,1)


