import pygame,help,fullscreen,math

class Stenaputi:
    def __init__(self,x,y,w,h,nospawn=None):
        self.cratinca=pygame.Surface([w,h])
        self.sten_cartinca=pygame.image.load('picture/стэнка.png')
        self.sten_cartinca=pygame.transform.scale(self.sten_cartinca,[self.sten_cartinca.get_width()/10,self.sten_cartinca.get_height()/10])
        cy=range(0,h,self.sten_cartinca.get_height())
        cx=range(0,w,self.sten_cartinca.get_width())
        for c1 in cx:
            for c2 in cy:
                self.cratinca.blit(self.sten_cartinca, [c1, c2])


        self.x=x
        self.y=y
        self.w=w
        self.h=h
        self.nospawn=nospawn
        self.stena=pygame.Rect(self.x,self.y,self.w,self.h)

    def draw(self,screen:pygame.Surface):
        stena_fullscreen=pygame.Rect(fullscreen.fulscren(screen,self.w,self.h,self.x,self.y))
        pygame.draw.rect(screen,[0,0,0],stena_fullscreen)
        screen.blit(self.cratinca,stena_fullscreen)
        # screen.blit(self.sten_cartinca,stena_fullscreen,[0,0,stena_fullscreen.w,stena_fullscreen.h])


# self.times_h=range(0,math.ceil(12/5))
# self.times_h=range(0,h//math.ceil(self.sten_cartinca.get_height()))
# self.times_h=range(0,h//math.ceil(self.sten_cartinca.get_height()))