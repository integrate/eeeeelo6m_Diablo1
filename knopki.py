from pygame import font
import pygame,fullscreen,knopki_kartinki

class Knopka(knopki_kartinki.Knopka_kartinka):
    def __init__(self,txt,x,y,name_font,size_font,deystvie,background_color,txt_color=[0,0,0],border_width=2,border_color=[0,0,0]):
        fonti = font.SysFont(name_font,size_font,True)
        txt=fonti.render(txt,True,txt_color)
        knopki_kartinki.Knopka_kartinka.__init__(self,txt,x,y,deystvie,background_color,border_width,border_color)

