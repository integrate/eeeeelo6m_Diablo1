import pygame

class Exit():
    def __init__(self,x,y,w,h):
        self.x=x
        self.y=y
        self.w=w
        self.h=h
        self.rect=pygame.Rect(x,y,h,w)


