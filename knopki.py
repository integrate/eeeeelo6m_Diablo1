from pygame import font
import pygame,fullscreen,knopki_kartinki

class Knopka(knopki_kartinki.Knopka_kartinka):
    def __init__(self,txt,x,y,name_font,size_font,deystvie,color):
        fonti = font.SysFont(name_font,size_font,True)
        txt=fonti.render(txt,True,[0,0,0])
        knopki_kartinki.Knopka_kartinka.__init__(self,txt,x,y,deystvie,color)

