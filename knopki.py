from pygame import font
import pygame,fullscreen

class Knopka():
    def __init__(self,txt,x,y,name_font,size_font):
        self.txt=txt
        self.font = font.SysFont(name_font,size_font,True)
        self.txt=self.font.render(txt,True,[0,0,0])
        self.rect=pygame.Rect(x,y,self.txt.get_width(),self.font.get_height())


    def draw(self,screen:pygame.Surface):
        self.rect=fullscreen.fullscreen_rect(self.rect,screen,'war',False)
        pygame.draw.rect(screen,[124,45,1],self.rect)
        self.txt = fullscreen.fullscreen_surface(screen, self.txt)
        screen.blit(self.txt, self.rect)
