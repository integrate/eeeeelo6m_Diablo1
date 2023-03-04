from pygame import font
import pygame,fullscreen

class Knopka():
    def __init__(self,txt,x,y,name_font,size_font,deystvie):
        self.txt=txt
        self.font = font.SysFont(name_font,size_font,True)
        self.txt=self.font.render(txt,True,[0,0,0])
        self.rect=pygame.Rect(x,y,self.txt.get_width(),self.font.get_height())
        self.deystvie=deystvie
        self.fullscreen_rect=pygame.Rect(0,0,0,0)

    def draw(self,screen:pygame.Surface):
        self.fullscreen_rect=fullscreen.fullscreen_rect(self.rect, screen, 'war', False)
        pygame.draw.rect(screen, [124,45,1], self.fullscreen_rect)
        self.fullscreen_txt = fullscreen.fullscreen_surface(screen, self.txt)
        screen.blit(self.fullscreen_txt, self.fullscreen_rect)


    def nagatie(self,event):
        if event.type==pygame.MOUSEBUTTONDOWN and self.fullscreen_rect.collidepoint(event.pos):
            self.deystvie()

