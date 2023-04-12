import pygame,fullscreen,random

class Cletca():
    def __init__(self,x,y,w,h,sostoynie='svobodna',color_hod=[255,100,100]):
        self.x=x
        self.y=y
        self.w=w
        self.h=h
        self.sostoynie=sostoynie
        self.cletca=pygame.Rect(self.x,self.y,self.w,self.h)
        self.prohod=False
        self.color=color_hod
    def draw(self,screen):
        self.cletca_fullscreen = fullscreen.fullscreen_rect(self.cletca, screen, 'war', False)
        if self.prohod==False:
            pygame.draw.rect(screen,[random.randint(0,255),random.randint(0,255),random.randint(0,255)],self.cletca_fullscreen)

        else:
            pygame.draw.rect(screen,self.color_hod,self.cletca_fullscreen)

        pygame.draw.rect(screen,[0,0,0],self.cletca_fullscreen,1)


