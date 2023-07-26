import pygame, draw_helper
from pygame import font

import fullscreen


class Effect():
    def __init__(self, deystvie, pic, long, statistic=None):
        self.font_statistik = font.SysFont('segoeuihistoric', 20, True)
        self.show_statistic=False
        self.deystvie = deystvie
        self.long = long
        self.pic = pygame.image.load(pic)
        self.effect_rect = pygame.Rect(50, 60, 50, 50)
        self.pic = pygame.transform.scale(self.pic, [self.effect_rect.w - 2, self.effect_rect.h - 2])
        self._statistic=' '
        self.statistic = statistic
        self.fullscreen_rect=pygame.rect.Rect(0,0,0,0)


    @property
    def statistic(self):
        return self._statistic
    @statistic.setter
    def statistic(self,new):

        self._statistic=new
        if new is not None:
            self.txt_statistic = self.font_statistik.render(self._statistic, True, [255, 255, 255])
            self.txt_statistic = self.txt_statistic.convert_alpha()
            self.txt_statistic.set_alpha(200)
            self.rect_statistic = pygame.rect.Rect(self.effect_rect.bottomright, self.txt_statistic.get_size())
            self.pic_statistic = pygame.Surface(self.txt_statistic.get_size(), pygame.SRCALPHA)
            self.pic_statistic.fill([0, 0, 0, 150])




    def draw(self, screen):
        self.fullscreen_rect = draw_helper.draw_picture(screen, self.effect_rect, self.pic, [0, 255, 16])

        if self.show_statistic==True and self._statistic is not None:



            draw_helper.draw_picture(screen, self.rect_statistic, self.pic_statistic, None)
            draw_helper.draw_picture(screen, self.rect_statistic, self.txt_statistic, None)


