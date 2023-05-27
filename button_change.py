import pygame
from pygame import font


class Button_change():
    def __init__(self, x, y, w, h, txt, fonta, color):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.rect = pygame.Rect(x, y, w, h)
        self.color = color
        self.fonta = fonta
        self.text=txt
        self.txt=self.wirawnivonie_txt(self.fonta,self.color,txt)

    def draw(self, screen: pygame.Surface):
        pygame.draw.rect(screen, [55, 155, 255], self.rect)
        screen.blit(self.txt, self.rect)

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

    def _smena_size_txt(self):
        pass
