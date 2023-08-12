import pygame,fullscreen,nospawn as modul_nospawn
derevo_art=pygame.image.load('picture/дерево.png')
derevo_art=pygame.transform.scale(derevo_art,[150,150])
class Derevo(modul_nospawn.Nospawn):
    def __init__(self,x,y,nospawn):
        modul_nospawn.Nospawn.__init__(self,x,y,150,150,nospawn)
        self.x=x
        self.y=y

        self.rect=pygame.Rect(self.x,self.y,150,150)
    def draw(self,screen:pygame.Surface,minimap=False):

        # super().draw(screen,minimap)
        mul='minimap' if minimap else 'map'
        a=fullscreen.fullscreen_surface(screen,derevo_art,mul)
        derevo =fullscreen.fullscreen_rect(self.rect,screen,mul)
        # pygame.draw.rect(screen, [97, 67, 9], derevo)
        screen.blit(a,derevo)
