import pygame,fullscreen

import activ_object


class Exit(activ_object.Activ_object):
    def __init__(self,x,y,w,h,activ):
        activ_object.Activ_object.__init__(self,activ,x,y,w,h,'picture/люк.png')



    # def draw(self,screen,minimap=False):
    #     mul='minimap' if minimap else 'map'
    #     a=fullscreen.fullscreen_surface(screen,self.exit_art,mul)
    #     exit_rect =fullscreen.fullscreen_rect(self.rect,screen,mul)
    #
    #     screen.blit(a,exit_rect)




