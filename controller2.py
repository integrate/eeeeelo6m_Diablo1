import pygame,model2,view2,os,controller
from pygame import event

def controller2():
    e=event.get()
    for r in e:
        if r.type==pygame.QUIT:
            exit()
        if r.type==pygame.MOUSEBUTTONDOWN:
            model2.dvogenie_igroc(r.pos[0],r.pos[1])
        model2.panel.init_event(r)
        model2.panel_wrag.init_event(r)

        controller.f11(r)

