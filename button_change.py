import pygame,fullscreen,knopki_kartinki,draw_helper
from pygame import font


class Button_change(knopki_kartinki.Knopka_kartinka):
    def __init__(self, x, y, w, h, txt, fonta, color,deystvie):
        self.fonta = fonta
        self.color = color
        self.text = txt
        self.true_rect = pygame.Rect(x, y, w, h)
        self.txt = draw_helper.wirawnivonie_txt(self.fonta, self.color, txt, self.true_rect)
        knopki_kartinki.Knopka_kartinka.__init__(self, self.txt, x, y, deystvie, [55, 155, 255],w=w,h=h)


    def smena_txt(self, txt=None, color=None, fonta=None):
        if txt is None: txt = self.text
        if color is None: color = self.color
        if fonta is None: fonta= self.fonta
        self.txt = draw_helper.wirawnivonie_txt(fonta, color, txt,self.rect)
        self.text=txt




