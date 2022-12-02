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
        cletca=fullscreen.fullscreen_rect(self.cletca,screen,False)
        pygame.draw.rect(screen,[34,144,143],cletca)

