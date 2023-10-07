import pygame, fullscreen


class Nospawn:
    def __init__(self, x, y, w, h, nospawn={}, base_nospawn=150):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.nospawn = nospawn
        self.base_nospawn = base_nospawn

    def get_nospawn_rect(self, object_class):
        a = self.nospawn[object_class] if object_class in self.nospawn.keys() else self.base_nospawn
        return pygame.Rect(self.x-a, self.y-a, self.w+a*2, self.h+a*2)

    def draw(self, screen, mul):
        rect_nospawn_fullscreen = fullscreen.fullscreen_rect(self.rect_nospawn, screen, mul)
        pygame.draw.rect(screen, [0, 0, 0], rect_nospawn_fullscreen, 2)