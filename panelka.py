import pygame,settings,fullscreen

class Panel():
    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y
        self.w=settings.PANEL_SIZE_W
        self.h=pygame.display.get_surface().get_height()
        self.panel=pygame.Rect(self.x,self.y,self.w,self.h)
    def draw(self,screen):
        a=fullscreen.fullscreen_rect(self.panel,screen,'war',False)
        pygame.draw.rect(screen,[134,145,221],a)