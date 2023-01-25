import pygame,fullscreen

class Exit():
    def __init__(self,x,y,w,h):
        self.exit_art=pygame.image.load('picture/люк.png')
        self.exit_art=pygame.transform.scale(self.exit_art,[w,h])
        self.x=x
        self.y=y
        self.w=w
        self.h=h
        self.rect=pygame.Rect(x,y,h,w)


    def draw(self,screen,minimap=False):
        mul='minimap' if minimap else 'map'
        a=fullscreen.fullscreen_surface(screen,self.exit_art,mul)
        exit_rect =fullscreen.fullscreen_rect(self.rect,screen,mul)

        screen.blit(a,exit_rect)




