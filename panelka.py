import pygame, settings, fullscreen, knopki, draw_helper
from pygame import font

import button_change
import igroc_war
import knopki_kartinki
import model2

font.init()
print(font.get_fonts())


class Panel():
    def __init__(self, damage, igroc: igroc_war.Igroc_war, x=1, regim='bloc'):
        if igroc == None:
            return
        self.igroc = igroc
        self.igroc.subscribe(self.smena_hp_igroc, igroc.EVENT_HP_CHANGE)
        self.igroc.subscribe(self.smena_ultimat_point, igroc.EVENT_POINT_CHANGE)
        self.igroc.orugie.subscribe(self.smena_damage, self.igroc.orugie.EVENT_SMENA_DAMAGE)
        self.igroc.orugie_2.subscribe(self.smena_damage, self.igroc.orugie_2.EVENT_SMENA_DAMAGE)

        self.panel = pygame.Rect(x, 1, settings.PANEL_SIZE_W, 768)

        self.font = font.SysFont('segoeui', 25, True)

        self.hp_bar_pic = self.font.render(str(igroc.hp), True, [0, 0, 0])
        self.hp_bar_rect = pygame.Rect(self.panel.x + settings.PANEL_SIZE_W / 6, 25, settings.PANEL_SIZE_W / 3 * 2, 25)

        self.slot_rect = pygame.Rect(self.panel.x + settings.PANEL_SIZE_W / 3, 25, settings.PANEL_SIZE_W / 3,
                                     settings.PANEL_SIZE_W / 3)

        self.slot_rect_vibor = knopki_kartinki.Knopka_kartinka.do_cnopca(igroc.orugie.cartinca, self.slot_rect.size,
                                                                         self.panel.x + settings.PANEL_SIZE_W / 3, 200,
                                                                         self.on_button_click_vibor, [255, 255, 73])
        self.slot_rect_vibor_2 = knopki_kartinki.Knopka_kartinka.do_cnopca(igroc.orugie_2.cartinca, self.slot_rect.size,
                                                                           self.panel.x + settings.PANEL_SIZE_W / 3,
                                                                           350,
                                                                           self.on_button_click_vibor_2, [255, 255, 73])

        self.orugie_art_1 = pygame.transform.scale(pygame.image.load(igroc.orugie.cartinca), self.slot_rect.size)
        self.orugie_art_2 = pygame.transform.scale(pygame.image.load(igroc.orugie_2.cartinca), self.slot_rect.size)

        self.regim = regim

        self.damage_weapon = self.font.render(str(igroc.orugie.damage[0]) + '-' + str(igroc.orugie.damage[1]), True,
                                              [255, 35, 50])
        self.damage_weapon_2 = self.font.render(str(igroc.orugie_2.damage[0]) + '-' + str(igroc.orugie_2.damage[1]),
                                                True, [255, 35, 50])
        self.damage_weapon_rect = pygame.Rect(self.slot_rect.x, self.slot_rect.bottom + 10,
                                              self.slot_rect.w, 50)

        self.kcopka = knopki.Knopka('использовать', 0, 0, 'segoeui', 25, self.on_button_click_hod, [124, 45, 1])
        self.kcopka.rect.centerx = self.panel.right - settings.PANEL_SIZE_W / 2
        self.kcopka.rect.bottom = self.panel.bottom - 10

        self.exit = knopki.Knopka(' X ', self.slot_rect.x - 63, self.slot_rect.y, 'segoeui', 25,
                                  self.on_button_click_normal, [124, 45, 1])

        self.opisanie_orugiy = draw_helper.text(igroc.orugie.opisanie, self.font,
                                                settings.PANEL_SIZE_W)
        self.opisanie_orugiy_2 = draw_helper.text(igroc.orugie_2.opisanie, self.font,
                                                  settings.PANEL_SIZE_W)

        self.opisanie_orugiy_rect = pygame.Rect(self.panel.x + 5, self.damage_weapon_rect.bottom, 0, 100)

        self.ultimat = button_change.Button_change(self.panel.centerx - settings.PANEL_SIZE_W / 3,
                                                   self.panel.bottom - 100, 200, 70,
                                                   str(igroc.point) + ' / ' + str(igroc.need_point),
                                                   'yugothicuiregular', [255, 86, 0], igroc.ulta)
        self.ultimat.rect.centerx = self.panel.centerx

    def draw(self, screen: pygame.surface.Surface):
        if self.regim in ['normal', 'hod', 'bloc']:
            self.draw_normal(screen)
        if self.regim == 'vibor':
            self.draw_wibor(screen)

    def draw_normal(self, screen):
        a = fullscreen.fullscreen_rect(self.panel, screen, 'war', False)
        pygame.draw.rect(screen, [134, 145, 221], a)

        self.slot_rect_vibor.draw(screen)
        self.slot_rect_vibor_2.draw(screen)

        draw_helper.draw_picture(screen, self.hp_bar_rect, self.hp_bar_pic, [255, 255, 255])

        self.ultimat.draw(screen)

    def draw_wibor(self, screen):
        a = fullscreen.fullscreen_rect(self.panel, screen, 'war', False)
        pygame.draw.rect(screen, [134, 145, 221], a)

        # рисования орудия
        a = self.orugie_art_1 if self.igroc.active_orugie is self.igroc.orugie else self.orugie_art_2
        draw_helper.draw_picture(screen, self.slot_rect, a, [255, 255, 73])

        b = 1
        a = 'one' if b == 1 else 'two'

        a = self.damage_weapon if self.igroc.active_orugie is self.igroc.orugie else self.damage_weapon_2
        draw_helper.draw_picture(screen, self.damage_weapon_rect, a, None)
        a = self.opisanie_orugiy if self.igroc.active_orugie is self.igroc.orugie else self.opisanie_orugiy_2
        draw_helper.draw_picture(screen, self.opisanie_orugiy_rect, a, None, 'topleft', 'topleft')
        # print(self.igroc.active_orugie.damage, self.igroc.active_orugie.damage_base)
        a = self.damage_weapon if self.igroc.active_orugie is self.igroc.orugie else self.damage_weapon_2
        draw_helper.draw_picture(screen, self.damage_weapon_rect, a, None)

        self.kcopka.draw(screen)

        self.exit.draw(screen)

    def on_button_click_hod(self):
        if self.regim == 'vibor':
            self.regim = 'hod'
            self.igroc.mona_hodit = True

    def on_button_click_normal(self):
        if self.regim == 'vibor':
            self.regim = 'normal'

    def on_button_click_vibor(self):
        if self.regim == 'normal':
            self.regim = 'vibor'
            self.igroc.active_orugie = self.igroc.orugie

    def on_button_click_vibor_2(self):
        if self.regim == 'normal':
            self.regim = 'vibor'
            self.igroc.active_orugie = self.igroc.orugie_2

    def smena_hp_igroc(self, observ, value, cod_event):
        self.hp_bar_pic = self.font.render(str(self.igroc.hp), True, [0, 0, 0])

    def smena_ultimat_point(self, observ, value, cod_event):
        if self.igroc.point == self.igroc.need_point:
            self.ultimat.smena_txt('ГОТОВО')
        else:
            self.ultimat.smena_txt(str(self.igroc.point) + ' / ' + str(self.igroc.need_point))

    def smena_damage(self, observ, value, cod_event):
        self.damage_weapon = self.font.render(
            str(self.igroc.orugie.damage[0]) + '-' + str(self.igroc.orugie.damage[1]), True,
            [255, 35, 50])
        self.damage_weapon_2 = self.font.render(
            str(self.igroc.orugie_2.damage[0]) + '-' + str(self.igroc.orugie_2.damage[1]),
            True, [255, 35, 50])

    def init_event(self, event):
        self.kcopka.nagatie(event)
        self.exit.nagatie(event)
        self.slot_rect_vibor.nagatie(event)
        self.slot_rect_vibor_2.nagatie(event)
        self.ultimat.nagatie(event)
