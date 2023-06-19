import pygame, fullscreen

import observer
import orugie


class Igroc_war():
    def __init__(self, x, y, w, h, hp, point=None, need_point=None, mona_hodit=False, deystvie_hod=None,
                 color=[255, 24, 74],
                 cletca_color=[255, 100, 100], orugie: orugie.Orugie = None, orugie_2: orugie.Orugie = None):
        self._hp = hp
        self.max_hp = 10
        self._point = point
        self.need_point = need_point
        if self._hp > self.max_hp:
            self._hp = self.max_hp
        self.rect = pygame.Rect(x, y, w, h)
        self.stamina = 4
        self._mona_hodit = mona_hodit
        self._deystvie_hod = deystvie_hod
        self.color = color
        self.cletca_color = cletca_color
        self.orugie = orugie
        self.orugie_2 = orugie_2
        self.active_orugie = None
        self.clas = 'none'
        self.observ=observer.Observer()

    @property
    def mona_hodit(self):
        return self._mona_hodit

    @mona_hodit.setter
    def mona_hodit(self, hod):
        self._mona_hodit = hod
        if callable(self._deystvie_hod):
            self._deystvie_hod(hod, self)

    @property
    def hp(self):
        return self._hp

    @hp.setter
    def hp(self, hp_now):
        if hp_now > self.max_hp:
            self._hp = self.max_hp
        else:
            self._hp = hp_now

    @property
    def point(self):
        return self._point

    @point.setter
    def point(self, new_point):
        self._point = new_point
        if self._point >= self.need_point:
            self._point = self.need_point

    def draw(self, screen):
        self.rect_fullscren = fullscreen.fullscreen_rect(self.rect, screen, 'war', False)
        pygame.draw.rect(screen, self.color, self.rect_fullscren)

    def sdvig(self, x, y):
        if self._mona_hodit == True:
            self.point += 1
            self.rect.x = x
            self.rect.y = y

    def ulta(self):
        raise Exception('нельзя создавать играков с этим классом')
