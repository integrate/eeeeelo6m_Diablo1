import pygame,fullscreen,nospawn as modul_nospawn

import load_cartinki


class Real_world_object(modul_nospawn.Nospawn):
    def __init__(self,x,y,w,h,cartinka,nospawn={},base_nospawn=150):
        modul_nospawn.Nospawn.__init__(self,x,y,w,h,nospawn,base_nospawn)

        self.x=x
        self.y=y
        self.w=w
        self.h=h
        self.rect=pygame.Rect(self.x,self.y,self.w,self.h)
        self.cartinka=load_cartinki.do_picture(cartinka,w,h)

    def draw(self,screen:pygame.Surface,minimap=False):

        # super().draw(screen,minimap)
        mul='minimap' if minimap else 'map'
        a=fullscreen.fullscreen_surface(screen, self.cartinka, mul)
        derevo =fullscreen.fullscreen_rect(self.rect,screen,mul)
        # pygame.draw.rect(screen, [97, 67, 9], derevo)
        screen.blit(a,derevo)
