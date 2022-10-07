import pygame

class Granstage():
    def __init__(self,x,y,w,h):
        self.x=x
        self.y=y
        self.w=w
        self.h=h
        self.rect=pygame.Rect(self.x,self.y,self.w,self.h)
    def draw(self,screen):
        pygame.draw.rect(screen,[0,0,0],self.rect)
