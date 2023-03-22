import pygame,draw_helper




class Knopka_kartinka():
    def __init__(self,picture,x,y,deystvie,color):
        self.picture=picture
        self.color=color
        self.rect=pygame.Rect(x,y,self.picture.get_width(),self.picture.get_height())
        self.deystvie=deystvie
        self.fullscreen_rect=pygame.Rect(0,0,0,0)

    def draw(self,screen:pygame.Surface):
        self.fullscreen_rect=draw_helper.draw_picture(screen,self.rect,self.picture,self.color)


    def nagatie(self,event):
        if event.type==pygame.MOUSEBUTTONDOWN and self.fullscreen_rect.collidepoint(event.pos):
            self.deystvie()



