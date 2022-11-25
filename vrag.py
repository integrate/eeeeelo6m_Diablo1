import pygame,fullscreen,nospawn as modul_nospawn

class Vrag(modul_nospawn.Nospawn):
    def __init__(self,x,y,hp=10):
        modul_nospawn.Nospawn.__init__(self,x,y,150,150,25)
        self.x=x
        self.y=y
        self.hp=hp
        self.rect=pygame.Rect(x,y,150,150)


    def draw(self,screen,minimap):
        vrag_fullscreen=fullscreen.fullscreen_rect(self.rect,screen,minimap)
        pygame.draw.rect(screen,[23,124,45],vrag_fullscreen)