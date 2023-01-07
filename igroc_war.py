import pygame,fullscreen

class Igroc_war():
    def __init__(self,x,y,w,h):
        self.x=x
        self.y=y
        self.w=w
        self.h=h
        self.rect=pygame.Rect(x,y,w,h)
        self.stamina=3

    def draw(self,screen):
        a=fullscreen.fullscreen_rect(self.rect,screen,'war',False)
        pygame.draw.rect(screen,[255,24,74],a)

    def sdvig(self,x,y):
        self.rect.x=x
        self.rect.y=y

