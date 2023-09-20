import pygame,fullscreen,nospawn as modul_nospawn

class Real_world_object(modul_nospawn.Nospawn):
    def __init__(self,x,y,w,h,nospawn):
        modul_nospawn.Nospawn.__init__(self,x,y,w,h,nospawn)
        self.x=x
        self.y=y
        self.w=w
        self.h=h
        self.rect=pygame.Rect(self.x,self.y,self.w,self.h)
        self.derevo_art = pygame.image.load('picture/дерево.png')
        self.derevo_art = pygame.transform.scale(self.derevo_art, [w, h])
    def draw(self,screen:pygame.Surface,minimap=False):

        # super().draw(screen,minimap)
        mul='minimap' if minimap else 'map'
        a=fullscreen.fullscreen_surface(screen,self.derevo_art,mul)
        derevo =fullscreen.fullscreen_rect(self.rect,screen,mul)
        # pygame.draw.rect(screen, [97, 67, 9], derevo)
        screen.blit(a,derevo)
