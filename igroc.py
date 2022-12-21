import pygame, fullscreen


class Igroc:
    def __init__(self, x, y, hp, dmg, deff, speedx, speedy, rects):
        self.x = x
        self.y = y
        self.hp = hp
        self.dmg = dmg
        self.deff = deff
        self.speedx = speedx
        self.speedy = speedy
        self.rects = rects
        self.rect_igroc = pygame.Rect(self.x, self.y, 100, 100)

    def draw(self, screen, minimap=False):
        # igroc = pygame.Rect(
        #     fullscreen.fulscren(screen, self.rect_igroc.width, self.rect_igroc.height, self.rect_igroc.x,
        #                         self.rect_igroc.y,minimap))
        mul='minimap' if minimap else 'map'

        igroc = fullscreen.fullscreen_rect(self.rect_igroc, screen, mul)
        pygame.draw.rect(screen, [255, 30, 30], igroc)

    def dvigenie_left(self):
        b=self.correct_wall_left()
        if b is not None:
            self.rect_igroc.x = b.rect.right
            return b
        else:
            self.rect_igroc.x -= self.speedx


    def correct_wall_left(self):
        b=None
        steni = []
        for stena in self.rects:
            crossx = stena.rect.right <= self.rect_igroc.x and stena.rect.right > self.rect_igroc.x - self.speedx
            crossy = stena.rect.y < self.rect_igroc.y < stena.rect.bottom or stena.rect.y < self.rect_igroc.bottom < stena.rect.bottom or self.rect_igroc.bottom > stena.rect.y > self.rect_igroc.y or self.rect_igroc.bottom > stena.rect.bottom > self.rect_igroc.y or (
                    self.rect_igroc.bottom == stena.rect.bottom and self.rect_igroc.y == stena.rect.y)

            if crossx and crossy:
                steni.append(stena)
        if len(steni) > 0:
            b = steni[0]
            for stena in steni:
                if stena.rect.right > b.rect.right:
                    b = stena
        return b


    def dvigenie_right(self):
        b=self.correct_wall_right()
        if b is not None:
            self.rect_igroc.right = b.rect.x
            return b
        else:
            self.rect_igroc.x += self.speedx


    def correct_wall_right(self):
        b=None
        steni=[]
        for stena in self.rects:
            crossx = stena.rect.x >= self.rect_igroc.right and stena.rect.x < self.rect_igroc.right + self.speedx
            crossy = stena.rect.y < self.rect_igroc.y < stena.rect.bottom or stena.rect.y < self.rect_igroc.bottom < stena.rect.bottom or self.rect_igroc.bottom > stena.rect.y > self.rect_igroc.y or self.rect_igroc.bottom > stena.rect.bottom > self.rect_igroc.y or (
                    self.rect_igroc.bottom == stena.rect.bottom and self.rect_igroc.y == stena.rect.y)

            if crossx and crossy:
                steni.append(stena)
        if len(steni) > 0:
            b = steni[0]
            for stena in steni:
                if stena.rect.x < b.rect.x:
                    b = stena
        return b

    # 1-17:10,2-17;11,3-17:15,4-17:16
    def dvigenie_bottom(self):
        b = self.correct_wall_bottom()
        if b is not None:
            self.rect_igroc.bottom = b.rect.y
            return b
        else:
            self.rect_igroc.y += self.speedy




    def correct_wall_bottom(self):
        b = None
        steni = []
        for stena in self.rects:
            crossy = stena.rect.y >= self.rect_igroc.bottom and stena.rect.y < self.rect_igroc.bottom + self.speedy
            crossx = stena.rect.x < self.rect_igroc.right < stena.rect.right or stena.rect.right > self.rect_igroc.x > stena.rect.x or self.rect_igroc.x < stena.rect.x < self.rect_igroc.right or self.rect_igroc.x < stena.rect.right < self.rect_igroc.right or (
                    self.rect_igroc.right == stena.rect.right and self.rect_igroc.x == stena.rect.x)

            if crossx and crossy:
                steni.append(stena)
        if len(steni) > 0:
            b = steni[0]
            for stena in steni:
                if stena.rect.y < b.rect.y:
                    b = stena

        return b


    def dvigenie_top(self):
        b=self.correct_wall_top()
        if b is not None:
            self.rect_igroc.y = b.rect.bottom
            return b
        else:
            self.rect_igroc.y -= self.speedy


    def correct_wall_top(self):
        steni=[]
        b=None
        for stena in self.rects:
            crossy = stena.rect.bottom <= self.rect_igroc.y and stena.rect.bottom > self.rect_igroc.y - self.speedy
            crossx = stena.rect.x < self.rect_igroc.right < stena.rect.right or stena.rect.right > self.rect_igroc.x > stena.rect.x or self.rect_igroc.x < stena.rect.x < self.rect_igroc.right or self.rect_igroc.x < stena.rect.right < self.rect_igroc.right or (
                    self.rect_igroc.right == stena.rect.right and self.rect_igroc.x == stena.rect.x)
            if crossx and crossy:
                steni.append(stena)
        if len(steni) > 0:
            b = steni[0]
            for stena in steni:
                if stena.rect.bottom > b.rect.bottom:
                    b=stena
        return b

