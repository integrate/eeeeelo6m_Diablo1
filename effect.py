import pygame, draw_helper


class Effect():
    def __init__(self, deystvie, pic):
        self.deystvie = deystvie
        self.pic = pygame.image.load(pic)
        self.effect_rect = pygame.Rect(50, 100, 50, 50)
        self.pic=pygame.transform.scale(self.pic,[self.effect_rect.w-2,self.effect_rect.h-2])

    def draw(self, screen):


        fullscreen_rect = draw_helper.draw_picture(screen, self.effect_rect, self.pic, [0, 255, 16])
