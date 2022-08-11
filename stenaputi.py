import pygame,help,fullscreen

class Stenaputi:
    def __init__(self,x,y,w,h,nospawn=None):
        self.cratinca=pygame.Surface([w,h])
        self.sten_cartinca=pygame.image.load('picture/стэнка.png')
        self.sten_cartinca=pygame.transform.scale(self.sten_cartinca,[self.sten_cartinca.get_width()/10,self.sten_cartinca.get_height()/10])
        times_w=w/self.sten_cartinca.get_width()
        times_h=h/self.sten_cartinca.get_height()

        cy=0
        cx=0
        while times_w>0 and times_h>0:
            self.cratinca.blit(self.sten_cartinca,[cx,cy])

            times_h-=1
            cy+=self.sten_cartinca.get_height()
            if times_h==0 and times_w!=0:
                cx+=self.sten_cartinca.get_width()
                times_h=h/self.sten_cartinca.get_height()
                times_w -= 1


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




