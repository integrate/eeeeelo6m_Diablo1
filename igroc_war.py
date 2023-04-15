import pygame, fullscreen


class Igroc_war():
    def __init__(self, x, y, w, h, hp, mona_hodit=False, deystvie_hod=None, color=[255, 24, 74],
                 cletca_color=[255, 100, 100], orugie=None):
        self.hp = hp
        self.rect = pygame.Rect(x, y, w, h)
        self.stamina = 20
        self._mona_hodit = mona_hodit
        self._deystvie_hod = deystvie_hod
        self.color = color
        self.cletca_color = cletca_color
        self.orugie=orugie

    @property
    def mona_hodit(self):
        return self._mona_hodit

    @mona_hodit.setter
    def mona_hodit(self, hod):
        self._mona_hodit = hod
        if callable(self._deystvie_hod):
            self._deystvie_hod(hod, self)

    def draw(self, screen):
        a = fullscreen.fullscreen_rect(self.rect, screen, 'war', False)
        pygame.draw.rect(screen, self.color, a)

    def sdvig(self, x, y):
        if self._mona_hodit == True:
            self.rect.x = x
            self.rect.y = y
