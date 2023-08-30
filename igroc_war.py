import pygame, fullscreen

import observer
from Orugie import orugie


class Igroc_war(observer.Observer):
    EVENT_HP_CHANGE = 1
    EVENT_POINT_CHANGE = 2
    EVENT_SMENA_MONA_HODIT = 3

    def __init__(self, hp,max_hp , stamina, point=None, need_point=None,
                 color=[255, 24, 74],
                 cletca_color=[255, 100, 100], orugie: orugie.Orugie = None, orugie_2: orugie.Orugie = None):
        observer.Observer.__init__(self)
        self._hp = hp
        self._max_hp = max_hp

        self._point = point
        self.need_point = need_point
        if self._hp > self.max_hp:
            self._hp = self.max_hp
        self.stamina = stamina

        self.orugie = orugie
        self.orugie_2 = orugie_2

        self.stamina_orig = stamina
        self.max_hp_orig = max_hp


        self.effects = []
        self.active_orugie = None

        self._mona_hodit = False
        self.color = color
        self.cletca_color = cletca_color
        self._activ = False

    @property
    def activ(self):
        return self._activ

    def activate(self, x, y, w, h):
        self.rect = pygame.Rect(x, y, w, h)
        self.stamina_orig = self.stamina
        self.max_hp_orig = self.max_hp

    @property
    def mona_hodit(self):
        return self._mona_hodit

    @mona_hodit.setter
    def mona_hodit(self, hod):
        self._mona_hodit = hod
        self.notify(self.EVENT_SMENA_MONA_HODIT, self._mona_hodit)

    @property
    def hp(self):
        return self._hp

    @hp.setter
    def hp(self, hp_now):
        if hp_now > self._max_hp:
            self._hp = self._max_hp
        else:
            self._hp = hp_now
        self.notify(self.EVENT_HP_CHANGE, self._hp)

    @property
    def max_hp(self):
        return self._max_hp

    @max_hp.setter
    def max_hp(self, max_hp_now):
        if max_hp_now < self._hp:
            self._hp = max_hp_now
            self.notify(self.EVENT_HP_CHANGE, self._hp)
        self._max_hp = max_hp_now

    @property
    def point(self):
        return self._point

    @point.setter
    def point(self, new_point):
        self._point = new_point
        if self._point >= self.need_point:
            self._point = self.need_point
        self.notify(self.EVENT_POINT_CHANGE)

    def draw(self, screen):

        self.rect_fullscren = fullscreen.fullscreen_rect(self.rect, screen, 'war', False)
        pygame.draw.rect(screen, self.color, self.rect_fullscren)

    def sdvig(self, x, y):
        if self._mona_hodit == True:
            if self.point is not None:
                self.point += 1
            self.rect.x = x
            self.rect.y = y

    def sort(self):
        self.stamina = self.stamina_orig
        self._max_hp = self.max_hp_orig
        self.orugie.base_stat()
        self.orugie_2.base_stat()
        for a in self.effects.copy():
            a.long -= 1
            if a.long <= 0:
                self.effects.remove(a)
            else:
                a.deystvie()

    def ulta(self):
        raise Exception('нельзя создавать игроков с этим классом')
