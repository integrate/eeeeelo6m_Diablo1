import pygame,fullscreen

class Vrag():
    def __init__(self,x,y,hp):
        self.x=x
        self.y=y
        self.hp=hp
        self.vrag=pygame.Rect(x,y,100,100)


    def draw(self,screen):
        vrag_fullscreen=pygame.Rect()