import pygame,fullscreen

class Igroc_war():
    def __init__(self,x,y,w,h,hp,mona_hodit=False):

        self.hp=hp
        self.rect=pygame.Rect(x,y,w,h)
        self.stamina=3
        self.mona_hodit=mona_hodit

    def draw(self,screen):
        a=fullscreen.fullscreen_rect(self.rect,screen,'war',False)
        pygame.draw.rect(screen,[255,24,74],a)

    def sdvig(self,x,y):
        if self.mona_hodit==True:
            self.rect.x=x
            self.rect.y=y

