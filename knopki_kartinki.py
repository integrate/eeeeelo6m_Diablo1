import fullscreen,pygame


def draw_picture(screen,rect,cartinka,color):
    rect=fullscreen.fullscreen_rect(rect,screen,'war',False)
    picture=fullscreen.fullscreen_surface(screen,cartinka)
    pygame.draw.rect(screen, color, rect)

    screen.blit(picture, rect)
    return rect


class Knopka_kartinka():
    def __init__(self,picture,x,y,deystvie,color):
        self.picture=picture
        self.color=color
        self.rect=pygame.Rect(x,y,self.picture.get_width(),self.picture.get_height())
        self.deystvie=deystvie
        self.fullscreen_rect=pygame.Rect(0,0,0,0)

    def draw(self,screen:pygame.Surface):
        self.fullscreen_rect=draw_picture(screen,self.rect,self.picture,self.color)


    def nagatie(self,event):
        if event.type==pygame.MOUSEBUTTONDOWN and self.fullscreen_rect.collidepoint(event.pos):
            self.deystvie()



