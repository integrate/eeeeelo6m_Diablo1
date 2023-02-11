import pygame, settings, fullscreen
from pygame import font

font.init()
print(font.get_fonts())


class Panel():
    def __init__(self,damage, x=1, y=1, hp=110):
        self.x = x
        self.y = y
        self.w = settings.PANEL_SIZE_W
        self.h = pygame.display.get_surface().get_height()
        self.panel = pygame.Rect(self.x, self.y, self.w, self.h)

        self.font = font.SysFont('segoeui', 25, True)

        self.hp_bar = self.font.render(str(hp), True, [0, 0, 0])
        self.hp_bar_rect = pygame.Rect(self.panel.x + settings.PANEL_SIZE_W / 6, 25, settings.PANEL_SIZE_W / 3 * 2, 25)

        self.slot_rect = pygame.Rect(self.panel.x + settings.PANEL_SIZE_W / 3, 200, settings.PANEL_SIZE_W / 3,
                                     settings.PANEL_SIZE_W / 3)
        self.slot_rect_art=pygame.image.load('picture/топор.png')
        self.slot_rect_art=pygame.transform.scale(self.slot_rect_art,self.slot_rect.size)
        self.slot_rect_vibor = pygame.Rect(self.panel.x + settings.PANEL_SIZE_W / 3, 25, settings.PANEL_SIZE_W / 3,
                                     settings.PANEL_SIZE_W / 3)

        self.regim='normal'


        self.damage_weapon=self.font.render(str(damage[0]) + '-' + str(damage[1]),True,[255,35,50])
        self.damage_weapon_rect=pygame.Rect(self.slot_rect_vibor.x,self.slot_rect_vibor.bottom+10,self.slot_rect_vibor.w,50)

    def draw(self, screen: pygame.surface.Surface):
        if self.regim=='normal':
            self.draw_normal(screen)
        if self.regim=='vibor':
            self.draw_wibor(screen)


    def draw_normal(self,screen):
        a = fullscreen.fullscreen_rect(self.panel, screen, 'war', False)
        pygame.draw.rect(screen, [134, 145, 221], a)
        b = fullscreen.fullscreen_rect(self.hp_bar_rect, screen, 'war', False)
        pygame.draw.rect(screen, [255, 255, 255], b)
        self.c = fullscreen.fullscreen_rect(self.slot_rect, screen, 'war', False)
        pygame.draw.rect(screen, [255, 255, 73], self.c)
        slor_art = fullscreen.fullscreen_surface(screen, self.slot_rect_art)
        screen.blit(slor_art, self.c)
        hp_bar = fullscreen.fullscreen_surface(screen, self.hp_bar)
        screen.blit(hp_bar, [b.centerx - hp_bar.get_width() / 2, b.y])

    def draw_wibor(self,screen):
        a = fullscreen.fullscreen_rect(self.panel, screen, 'war', False)
        pygame.draw.rect(screen, [134, 145, 221], a)
        c = fullscreen.fullscreen_rect(self.slot_rect_vibor, screen, 'war', False)
        pygame.draw.rect(screen, [255, 255, 73], c)
        slor_art = fullscreen.fullscreen_surface(screen, self.slot_rect_art)
        screen.blit(slor_art, c)

        b=fullscreen.fullscreen_rect(self.damage_weapon_rect,screen,'war',False)
        damage_weapon=fullscreen.fullscreen_surface(screen,self.damage_weapon)
        screen.blit(damage_weapon,[b.centerx - damage_weapon.get_width() / 2, b.y])


        # screen.blit(self.text('легендарный топор который претворяется молотом',self.font,settings.PANEL_SIZE_W),[b.centerx - damage_weapon.get_width() / 2, b.y+100])




    def pereponel(self,x,y):
        if self.c.collidepoint(x,y):
            self.regim='vibor'
            self.slot_rect.y=25


    # @staticmethod
    # def text(txt,font,w_panel):
    #     a=''
    #     s=pygame.Surface([0,0])
    #     j=[]
    #     words=txt.split()
    #
    #     for r in words:
    #         e=font.render(r,True,[0,0,0])
    #         if e.get_width()+s.get_width()>w_panel!=True:
    #             a=a+' '+r
    #             s=font.render(a,True,[0,0,0])
    #         else:
    #             j.append(s)
    #             a=r
    #             s=font.render(a,True,[0,0,0])






