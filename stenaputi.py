import pygame,help,fullscreen,math,nospawn as modul_nospawn

class Stenaputi(modul_nospawn.Nospawn):
    def __init__(self,x,y,w,h,nospawn,prohodimost=False):
        modul_nospawn.Nospawn.__init__(self,x,y,w,h,{},nospawn)
        self.prohodimost=prohodimost
        self.cratinca=pygame.Surface([w,h])
        self.sten_cartinca=pygame.image.load('picture/стэнка.png')
        self.sten_cartinca=pygame.transform.scale(self.sten_cartinca,[self.sten_cartinca.get_width()/10,self.sten_cartinca.get_height()/10])
        self.w=w
        self.h=h
        cy=range(0,h,self.sten_cartinca.get_height())
        cx=range(0,w,self.sten_cartinca.get_width())

        for c1 in cx:
            for c2 in cy:
                self.cratinca.blit(self.sten_cartinca, [c1, c2])



        self.x=x
        self.y=y
        self.rect=pygame.Rect(self.x, self.y, self.w, self.h)


    def draw(self,screen:pygame.Surface,minimap=False):
        # super().draw(screen,minimap)
        mul='minimap' if minimap else 'map'

        stena_fullscreen=fullscreen.fullscreen_rect(self.rect,screen,mul)
        pygame.draw.rect(screen,[0,0,0],stena_fullscreen)
        screen.blit(self.cratinca,stena_fullscreen,[0,0,stena_fullscreen.w,stena_fullscreen.h])


class Vid2(Stenaputi):
    def __init__(self,x,y,w,h):
        Stenaputi.__init__(self,x,y,w,h,0)
        self.cratinca.fill([0,0,0])


