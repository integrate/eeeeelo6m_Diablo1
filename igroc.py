import pygame, fullscreen


class Igroc:
    def __init__(self, x, y, hp, dmg, deff, speedx, speedy, steni):
        self.x = x
        self.y = y
        self.hp = hp
        self.dmg = dmg
        self.deff = deff
        self.speedx = speedx
        self.speedy = speedy
        self.steni = steni
        self.rect_igroc = pygame.Rect(self.x, self.y, 100, 100)

    def draw(self, screen):
        igroc = pygame.Rect(
            fullscreen.fulscren(screen, self.rect_igroc.width, self.rect_igroc.height, self.rect_igroc.x,
                                self.rect_igroc.y))
        pygame.draw.rect(screen, [255, 30, 30], igroc)

    def dvigenie_left(self):

        steni = []
        # if self.rect_igroc.x < 0:
        #     self.rect_igroc.x = 0
        for stena in self.steni:
            crossx = stena.stena.right <= self.rect_igroc.x and stena.stena.right > self.rect_igroc.x - self.speedx
            crossy = stena.y <= self.rect_igroc.y <= stena.stena.bottom or stena.y <= self.rect_igroc.bottom <= stena.stena.bottom or stena.y <= self.rect_igroc.y <= stena.stena.bottom or self.rect_igroc.bottom > stena.y > self.rect_igroc.y

            if crossx and crossy:
                steni.append(stena)
        if len(steni)>0:
            b=steni[0].stena.right
            for stena in steni:
                if stena.stena.right>b:
                    b=stena.stena.right
            print(b)
            self.rect_igroc.x=b
        else:
            self.rect_igroc.x -= self.speedx


    def dvigenie_right(self):
        steni = []
        for stena in self.steni:
            crossx = stena.stena.x >= self.rect_igroc.right and stena.stena.x < self.rect_igroc.right + self.speedx
            crossy = stena.y <= self.rect_igroc.y <= stena.stena.bottom or stena.y <= self.rect_igroc.bottom <= stena.stena.bottom or stena.y <= self.rect_igroc.y <= stena.stena.bottom or self.rect_igroc.bottom > stena.y > self.rect_igroc.y
            if crossx and crossy:
                steni.append(stena)
        if len(steni)>0:
            b=steni[0].stena.x
            for stena in steni:
                if stena.stena.x<b:
                    b=stena.stena.x
            print(b)
            self.rect_igroc.right=b
        else:
            self.rect_igroc.x += self.speedx

    def dvigenie_bottom(self):
        self.rect_igroc.y += self.speedy

    def dvigenie_top(self):
        self.rect_igroc.y -= self.speedy
