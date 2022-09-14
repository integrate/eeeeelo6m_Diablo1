import pygame,fullscreen

class Igroc:
    def __init__(self,x,y,hp,dmg,deff,speedx,speedy,steni):
        self.x=x
        self.y=y
        self.hp=hp
        self.dmg=dmg
        self.deff=deff
        self.speedx=speedx
        self.speedy=speedy
        self.steni=steni
        self.rect_igroc=pygame.Rect(self.x,self.y,100,100)

    def draw(self,screen):
        igroc = pygame.Rect(fullscreen.fulscren(screen, self.rect_igroc.width, self.rect_igroc.height, self.rect_igroc.x, self.rect_igroc.y))
        pygame.draw.rect(screen, [255, 30, 30], igroc)
    def dvigenie_left(self):
        self.rect_igroc.x-=self.speedx
        # if self.rect_igroc.x < 0:
        #     self.rect_igroc.x = 0
        # for stena in self.steni:
            # if stena.x>

    def dvigenie_right(self):
        self.rect_igroc.x+=self.speedx
    def dvigenie_bottom(self):
        self.rect_igroc.y+=self.speedy

    def dvigenie_top(self):
        self.rect_igroc.y-=self.speedy


