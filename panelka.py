import pygame, settings, fullscreen, knopki
from pygame import font

import igroc_war
import knopki_kartinki

font.init()
print(font.get_fonts())


class Panel():
    def __init__(self, damage, igroc:igroc_war.Igroc_war):
        self.igroc = igroc

        self.panel = pygame.Rect(1, 1, settings.PANEL_SIZE_W, 768)

        self.font = font.SysFont('segoeui', 25, True)

        self.hp_bar = self.font.render(str(igroc.hp), True, [0, 0, 0])
        self.hp_bar_rect = pygame.Rect(self.panel.x + settings.PANEL_SIZE_W / 6, 25, settings.PANEL_SIZE_W / 3 * 2, 25)

        self.slot_rect = pygame.Rect(self.panel.x + settings.PANEL_SIZE_W / 3, 200, settings.PANEL_SIZE_W / 3,
                                     settings.PANEL_SIZE_W / 3)

        self.slot_rect_art = pygame.image.load('picture/топор.png')
        self.slot_rect_art = pygame.transform.scale(self.slot_rect_art, self.slot_rect.size)
        self.slot_rect_vibor=knopki_kartinki.Knopka_kartinka(self.slot_rect_art,self.panel.x + settings.PANEL_SIZE_W / 3, 25,self.on_button_click_vibor)
        # self.slot_rect_vibor = pygame.Rect(self.panel.x + settings.PANEL_SIZE_W / 3, 25, settings.PANEL_SIZE_W / 3,
        #                                    settings.PANEL_SIZE_W / 3)

        self.regim = 'normal'

        self.damage_weapon = self.font.render(str(damage[0]) + '-' + str(damage[1]), True, [255, 35, 50])
        self.damage_weapon_rect = pygame.Rect(self.slot_rect_vibor.rect.x, self.slot_rect_vibor.rect.bottom + 10,
                                              self.slot_rect_vibor.rect.w, 50)

        self.kcopka = knopki.Knopka('использовать', 0, 0, 'segoeui', 25, self.on_button_click_hod)
        self.kcopka.rect.centerx= settings.PANEL_SIZE_W / 2
        self.kcopka.rect.bottom= self.panel.bottom - 10

        self.exit = knopki.Knopka(' X ',self.slot_rect_vibor.rect.x - 63, self.slot_rect_vibor.rect.y, 'segoeui', 25,self.on_button_click_normal)


    def draw(self, screen: pygame.surface.Surface):
        if self.regim == 'normal' or self.regim == 'hod':
            self.draw_normal(screen)
        if self.regim == 'vibor':
            self.draw_wibor(screen)

    def draw_normal(self, screen):
        a = fullscreen.fullscreen_rect(self.panel, screen, 'war', False)
        pygame.draw.rect(screen, [134, 145, 221], a)
        b = fullscreen.fullscreen_rect(self.hp_bar_rect, screen, 'war', False)
        pygame.draw.rect(screen, [255, 255, 255], b)
        # self.c = fullscreen.fullscreen_rect(self.slot_rect, screen, 'war', False)
        # pygame.draw.rect(screen, [255, 255, 73], self.c)
        # slor_art = fullscreen.fullscreen_surface(screen, self.slot_rect_art)
        # screen.blit(slor_art, self.c)
        self.slot_rect_vibor.draw(screen)
        self.hp_bar = self.font.render(str(self.igroc.hp), True, [0, 0, 0])

        hp_bar = fullscreen.fullscreen_surface(screen, self.hp_bar)
        screen.blit(hp_bar, [b.centerx - hp_bar.get_width() / 2, b.centery - hp_bar.get_height() / 2])

    def draw_wibor(self, screen):
        a = fullscreen.fullscreen_rect(self.panel, screen, 'war', False)
        pygame.draw.rect(screen, [134, 145, 221], a)
        # c = fullscreen.fullscreen_rect(self.slot_rect_vibor, screen, 'war', False)
        # pygame.draw.rect(screen, [255, 255, 73], c)
        # slor_art = fullscreen.fullscreen_surface(screen, self.slot_rect_art)
        # screen.blit(slor_art, c)

        b = fullscreen.fullscreen_rect(self.damage_weapon_rect, screen, 'war', False)
        damage_weapon = fullscreen.fullscreen_surface(screen, self.damage_weapon)
        screen.blit(damage_weapon, [b.centerx - damage_weapon.get_width() / 2, b.y])
        h = self.text('легендарный топор который претворяется молотом', self.font, settings.PANEL_SIZE_W)
        h = fullscreen.fullscreen_surface(screen, h)
        screen.blit(h, [0, b.bottom])


        self.kcopka.draw(screen)


        self.exit.draw(screen)




    def on_button_click_hod(self):
        self.regim='hod'
        self.igroc.mona_hodit=True


    def on_button_click_normal(self):
        self.regim='normal'

    def on_button_click_vibor(self):
        self.regim='vibor'




    def init_event(self,event):
        self.kcopka.nagatie(event)
        self.exit.nagatie(event)
        self.slot_rect_vibor.nagatie(event)

    @staticmethod
    def text(txt, font, w_panel):
        a = ''
        s = pygame.Surface([0, 0])
        j = []
        words = txt.split()

        for r in words:
            e = font.render(r, True, [0, 0, 0])
            if a == '':
                a = r
            elif e.get_width() + s.get_width() <= w_panel:
                a = a + ' ' + r
            else:
                j.append(s)
                a = r
            s = font.render(a, True, [0, 0, 0])
        j.append(s)
        o = 0
        for v in j:
            if v.get_width() > o:
                o = v.get_width()
        k = pygame.Surface([o, len(j) * font.get_height()], pygame.SRCALPHA)
        o = 0
        for e in j:
            k.blit(e, [0, o])
            o += font.get_height()

        return k
