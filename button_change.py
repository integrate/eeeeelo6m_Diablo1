import pygame,fullscreen
from pygame import font


class Button_change():
    def __init__(self, x, y, w, h, txt, fonta, color,deystvie):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.rect = pygame.Rect(x, y, w, h)
        self.deystvie=deystvie
        self.color = color
        self.fonta = fonta
        self.text=txt
        self.txt=self.wirawnivonie_txt(self.fonta,self.color,txt)

    def nagatie(self,event):
        if event.type==pygame.MOUSEBUTTONDOWN and self.fullscreen_rect.collidepoint(event.pos):
            self.deystvie()

    def draw(self, screen: pygame.Surface):
        self.fullscreen_rect=fullscreen.fullscreen_rect(self.rect,screen,'war',False)
        pygame.draw.rect(screen, [55, 155, 255], self.fullscreen_rect)
        fullscreen_txt=fullscreen.fullscreen_surface(screen,self.txt)
        screen.blit(fullscreen_txt,[self.fullscreen_rect.centerx-fullscreen_txt.get_width()/2, self.fullscreen_rect.centery-fullscreen_txt.get_height()/2])

    def smena_txt(self, txt=None, color=None, fonta=None):
        if txt is None: txt = self.text
        if color is None: color = self.color
        if fonta is None: fonta= self.fonta
        self.txt = self.wirawnivonie_txt(fonta, color, txt)
        self.text=txt

    def wirawnivonie_txt(self, fonta, color, txt):
        txt_size = 1
        fonti = font.SysFont(fonta, txt_size, True)
        text = fonti.render(txt, True, color)
        while text.get_height() < self.rect.h:
            txt_size += 1
            fonti = font.SysFont(fonta, txt_size, True)
            text = fonti.render(txt, True, color)
        if txt_size > 1: txt_size -= 1
        fonti = font.SysFont(fonta, txt_size, True)
        text = fonti.render(txt, True, color)
        if text.get_width() > self.rect.w:
            a = text.get_width() / self.rect.w
            text = pygame.transform.scale(text, [text.get_width() / a, text.get_height() / a])
        return text


