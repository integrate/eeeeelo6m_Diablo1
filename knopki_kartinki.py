import pygame,draw_helper




class Knopka_kartinka():
    def __init__(self,picture,x,y,deystvie,color,border_width=2,border_color=[0,0,0],w=None,h=None):
        self.picture=picture
        self.color=color
        self.x=x
        if w==None and h==None:
            self.rect=pygame.Rect(self.x,y,self.picture.get_width(),self.picture.get_height())
        else:
            self.rect = pygame.Rect(self.x, y, w, h)
        self.deystvie=deystvie
        self.fullscreen_rect=pygame.Rect(0,0,0,0)
        self.border_color=border_color
        self.border_width=border_width

    def draw(self,screen:pygame.Surface):
        self.fullscreen_rect=draw_helper.draw_picture(screen,self.rect,self.picture,self.color)
        pygame.draw.rect(screen,self.border_color,self.fullscreen_rect,self.border_width)


    def nagatie(self,event):
        if event.type==pygame.MOUSEBUTTONDOWN and self.fullscreen_rect.collidepoint(event.pos):
            self.deystvie()
    @staticmethod
    def do_cnopca(load_picture,cnopca_size,x,y,deystvie,color):
        picture = pygame.image.load(load_picture)
        picture = pygame.transform.scale(picture,cnopca_size)
        return Knopka_kartinka(picture,x,y,deystvie,color)




