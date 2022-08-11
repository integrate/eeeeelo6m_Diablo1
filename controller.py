import pygame,model
from pygame import event

pygame.key.set_repeat(50, 50)
def control():
    e=event.get()
    for r in e:
        if r.type==pygame.QUIT:
            exit()
        if r.type==pygame.KEYDOWN and r.key==pygame.K_d:

            model.igroc.x+=10
        if r.type==pygame.KEYDOWN and r.key==pygame.K_a:
            model.igroc.x-=10
        if r.type==pygame.KEYDOWN and r.key==pygame.K_w:
            model.igroc.y-=10
        if r.type==pygame.KEYDOWN and r.key==pygame.K_s:
            model.igroc.y+=10
