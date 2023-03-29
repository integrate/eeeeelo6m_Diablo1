import pygame, settings, fullscreen, knopki, draw_helper
from pygame import font

import igroc_war
import knopki_kartinki

font.init()
print(font.get_fonts())


class Panel():
    def __init__(self, damage, igroc: igroc_war.Igroc_war):
        self.igroc = igroc

        self.panel = pygame.Rect(1, 1, settings.PANEL_SIZE_W, 768)

        self.font = font.SysFont('segoeui', 25, True)

        # self.hp_bar = self.font.render(str(igroc.hp), True, [0, 0, 0])
        self.hp_bar_rect = pygame.Rect(self.panel.x + settings.PANEL_SIZE_W / 6, 25, settings.PANEL_SIZE_W / 3 * 2, 25)

        self.slot_rect = pygame.Rect(self.panel.x + settings.PANEL_SIZE_W / 3, 25, settings.PANEL_SIZE_W / 3,
                                     settings.PANEL_SIZE_W / 3)

        self.slot_rect_art = pygame.image.load('picture/топор.png')
        self.slot_rect_art = pygame.transform.scale(self.slot_rect_art, self.slot_rect.size)
        self.slot_rect_vibor = knopki_kartinki.Knopka_kartinka(self.slot_rect_art,
                                                               self.panel.x + settings.PANEL_SIZE_W / 3, 200,
                                                               self.on_button_click_vibor, [255, 255, 73])

        self.regim = 'normal'

        self.damage_weapon = self.font.render(str(damage[0]) + '-' + str(damage[1]), True, [255, 35, 50])
        self.damage_weapon_rect = pygame.Rect(self.slot_rect.x, self.slot_rect.bottom + 10,
                                              self.slot_rect.w, 50)

        self.kcopka = knopki.Knopka('использовать', 0, 0, 'segoeui', 25, self.on_button_click_hod, [124, 45, 1])
        self.kcopka.rect.centerx = settings.PANEL_SIZE_W / 2
        self.kcopka.rect.bottom = self.panel.bottom - 10

        self.exit = knopki.Knopka(' X ', self.slot_rect.x - 63, self.slot_rect.y, 'segoeui', 25,
                                  self.on_button_click_normal, [124, 45, 1])

        self.opisanie_orugiy = draw_helper.text('легендарный топор который претворяется молотом', self.font,
                                                settings.PANEL_SIZE_W)


        self.opisanie_orugiy_rect = pygame.Rect(5, self.damage_weapon_rect.bottom, 0, 100)

    def draw(self, screen: pygame.surface.Surface):
        if self.regim == 'normal' or self.regim == 'hod':
            self.draw_normal(screen)
        if self.regim == 'vibor':
            self.draw_wibor(screen)

    def draw_normal(self, screen):
        a = fullscreen.fullscreen_rect(self.panel, screen, 'war', False)
        pygame.draw.rect(screen, [134, 145, 221], a)

        self.slot_rect_vibor.draw(screen)
        hp_bar = self.font.render(str(self.igroc.hp), True, [0, 0, 0])
        draw_helper.draw_picture(screen, self.hp_bar_rect, hp_bar, [255, 255, 255])

    def draw_wibor(self, screen):
        a = fullscreen.fullscreen_rect(self.panel, screen, 'war', False)
        pygame.draw.rect(screen, [134, 145, 221], a)

        # рисования орудия
        draw_helper.draw_picture(screen, self.slot_rect, self.slot_rect_art, [255, 255, 73])

        draw_helper.draw_picture(screen, self.damage_weapon_rect, self.damage_weapon, None)

        draw_helper.draw_picture(screen, self.opisanie_orugiy_rect, self.opisanie_orugiy, None,'topleft','topleft')

        self.kcopka.draw(screen)

        self.exit.draw(screen)

    def on_button_click_hod(self):
        self.regim = 'hod'
        self.igroc.mona_hodit = True

    def on_button_click_normal(self):
        self.regim = 'normal'

    def on_button_click_vibor(self):
        if self.regim != 'hod':
            self.regim = 'vibor'

    def init_event(self, event):
        self.kcopka.nagatie(event)
        self.exit.nagatie(event)
        self.slot_rect_vibor.nagatie(event)
