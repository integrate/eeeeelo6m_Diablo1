import pygame, settings, fullscreen, knopki, draw_helper
from pygame import font

import igroc_war
import knopki_kartinki

font.init()
print(font.get_fonts())


class Panel():
    def __init__(self, damage, igroc: igroc_war.Igroc_war,x=1,regim='bloc'):
        self.igroc = igroc

        self.panel = pygame.Rect(x, 1, settings.PANEL_SIZE_W, 768)

        self.font = font.SysFont('segoeui', 25, True)

        # self.hp_bar = self.font.render(str(igroc.hp), True, [0, 0, 0])
        self.hp_bar_rect = pygame.Rect(self.panel.x + settings.PANEL_SIZE_W / 6, 25, settings.PANEL_SIZE_W / 3 * 2, 25)

        self.slot_rect = pygame.Rect(self.panel.x + settings.PANEL_SIZE_W / 3, 25, settings.PANEL_SIZE_W / 3,
                                     settings.PANEL_SIZE_W / 3)


        self.slot_rect_vibor = knopki_kartinki.Knopka_kartinka.do_cnopca(igroc.orugie.cartinca,self.slot_rect.size,
                                                               self.panel.x + settings.PANEL_SIZE_W / 3, 200,
                                                               self.on_button_click_vibor, [255, 255, 73])
        self.slot_rect_vibor_2 = knopki_kartinki.Knopka_kartinka.do_cnopca(igroc.orugie_2.cartinca,self.slot_rect.size,
                                                               self.panel.x + settings.PANEL_SIZE_W / 3, 350,
                                                               self.on_button_click_vibor, [255, 255, 73])

        self.regim = regim

        self.damage_weapon = self.font.render(str(igroc.orugie.damage[0]) + '-' + str(igroc.orugie.damage[1]), True, [255, 35, 50])
        self.damage_weapon_rect = pygame.Rect(self.slot_rect.x, self.slot_rect.bottom + 10,
                                              self.slot_rect.w, 50)

        self.kcopka = knopki.Knopka('использовать', 0, 0, 'segoeui', 25, self.on_button_click_hod, [124, 45, 1])
        self.kcopka.rect.centerx = self.panel.right-settings.PANEL_SIZE_W / 2
        self.kcopka.rect.bottom = self.panel.bottom - 10

        self.exit = knopki.Knopka(' X ', self.slot_rect.x - 63, self.slot_rect.y, 'segoeui', 25,
                                  self.on_button_click_normal, [124, 45, 1])

        self.opisanie_orugiy = draw_helper.text(igroc.orugie.opisanie, self.font,
                                                settings.PANEL_SIZE_W)


        self.opisanie_orugiy_rect = pygame.Rect(self.panel.x+5, self.damage_weapon_rect.bottom, 0, 100)

    def draw(self, screen: pygame.surface.Surface):
        if self.regim in ['normal','hod','bloc']:
            self.draw_normal(screen)
        if self.regim == 'vibor':
            self.draw_wibor(screen)

    def draw_normal(self, screen):
        a = fullscreen.fullscreen_rect(self.panel, screen, 'war', False)
        pygame.draw.rect(screen, [134, 145, 221], a)

        self.slot_rect_vibor.draw(screen)
        self.slot_rect_vibor_2.draw(screen)

        hp_bar = self.font.render(str(self.igroc.hp), True, [0, 0, 0])
        draw_helper.draw_picture(screen, self.hp_bar_rect, hp_bar, [255, 255, 255])

    def draw_wibor(self, screen):
        a = fullscreen.fullscreen_rect(self.panel, screen, 'war', False)
        pygame.draw.rect(screen, [134, 145, 221], a)

        # рисования орудия
        draw_helper.draw_picture(screen, self.slot_rect, self.orugie, [255, 255, 73])

        draw_helper.draw_picture(screen, self.damage_weapon_rect, self.damage_weapon, None)

        draw_helper.draw_picture(screen, self.opisanie_orugiy_rect, self.opisanie_orugiy, None,'topleft','topleft')

        self.kcopka.draw(screen)

        self.exit.draw(screen)

    def on_button_click_hod(self):
        if self.regim == 'vibor' :
            self.regim = 'hod'
            self.igroc.mona_hodit = True

    def on_button_click_normal(self):
        if self.regim=='vibor':
            self.regim = 'normal'

    def on_button_click_vibor(self):
        if self.regim =='normal':
            self.regim = 'vibor'
            self.orugie=self.igroc.orugie


    def init_event(self, event):
        self.kcopka.nagatie(event)
        self.exit.nagatie(event)
        self.slot_rect_vibor.nagatie(event)
        self.slot_rect_vibor_2.nagatie(event)



