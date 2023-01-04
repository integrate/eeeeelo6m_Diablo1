import pygame,fullscreen

class Cletca():
    def __init__(self,x,y,w,h,sostoynie='svobodna'):
        self.x=x
        self.y=y
        self.w=w
        self.h=h
        self.sostoynie=sostoynie
        self.cletca=pygame.Rect(self.x,self.y,self.w,self.h)
        self.prohod=False
    def draw(self,screen):
        self.cletca_fullscreen = fullscreen.fullscreen_rect(self.cletca, screen, 'war', False)
        if self.prohod==False:
            pygame.draw.rect(screen,[255,255,255],self.cletca_fullscreen)

        else:
            pygame.draw.rect(screen,[255,100,100],self.cletca_fullscreen)

        pygame.draw.rect(screen,[0,0,0],self.cletca_fullscreen,1)


