import fullscreen,pygame


class Knopka_kartinka():
    def __init__(self,picture,x,y,deystvie):
        self.picture=picture

        self.rect=pygame.Rect(x,y,self.picture.get_width(),self.picture.get_height())
        self.deystvie=deystvie
        self.fullscreen_rect=pygame.Rect(0,0,0,0)

    def draw(self,screen:pygame.Surface):
        self.fullscreen_rect=fullscreen.fullscreen_rect(self.rect,screen,'war',False)
        pygame.draw.rect(screen,[255, 255, 73],self.fullscreen_rect)
        self.fullscreen_picture=fullscreen.fullscreen_surface(screen,self.picture)
        screen.blit(self.fullscreen_picture,self.fullscreen_rect)


    def nagatie(self,event):
        if event.type==pygame.MOUSEBUTTONDOWN and self.fullscreen_rect.collidepoint(event.pos):
            self.deystvie()

