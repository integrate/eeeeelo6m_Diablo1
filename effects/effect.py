import pygame, draw_helper
from pygame import font

import fullscreen


class Effect():
    def __init__(self, deystvie, pic, long, statistic=None):
        self.deystvie = deystvie
        self.long = long
        self.pic = pygame.image.load(pic)
        self.effect_rect = pygame.Rect(50, 60, 50, 50)
        self.pic = pygame.transform.scale(self.pic, [self.effect_rect.w - 2, self.effect_rect.h - 2])
        self.statistic = statistic

    def draw(self, screen):
        self.fullscreen_rect = draw_helper.draw_picture(screen, self.effect_rect, self.pic, [0, 255, 16])

    def draw_statistic(self, screen: pygame.Surface):
        font_statistik = font.SysFont('segoeuihistoric', 20, True)
        txt_statistic = font_statistik.render(self.statistic, True, [255, 255, 255])
        txt_statistic=txt_statistic.convert_alpha()
        txt_statistic.set_alpha(200)
        rect_statistic = pygame.rect.Rect(self.effect_rect.bottomright, txt_statistic.get_size())
        pic_statistic = pygame.Surface(txt_statistic.get_size(), pygame.SRCALPHA)
        pic_statistic.fill([0, 0, 0, 150])

        draw_helper.draw_picture(screen, rect_statistic, pic_statistic, None)
        draw_helper.draw_picture(screen, rect_statistic, txt_statistic, None)


