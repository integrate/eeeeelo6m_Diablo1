import pygame,fullscreen

class Derevo:
    def __init__(self,x,y,w,h):
        self.x=x
        self.y=y
        self.h=h
        self.w=w
        self.rect=pygame.Rect(self.x,self.y,self.w,self.h)

    def draw(self,screen):
        derevo = pygame.Rect(fullscreen.fulscren(screen, self.rect.width, self.rect.height, self.rect.x, self.rect.y))
        pygame.draw.rect(screen, [0, 0, 0], derevo)