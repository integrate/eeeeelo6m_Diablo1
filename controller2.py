import pygame,model2
from pygame import event


def controller2():
    e=event.get()
    for r in e:
        print(r.type)
        if r.type==pygame.QUIT:
            exit()
        if r.type==pygame.MOUSEBUTTONDOWN:
            model2.dvogenie_igroc(r.pos[0],r.pos[1])
