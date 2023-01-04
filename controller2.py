import pygame,model2,view2,os
from pygame import event

def controller2():
    e=event.get()
    for r in e:
        print(r.type)
        if r.type==pygame.QUIT:
            exit()
        if r.type==pygame.MOUSEBUTTONDOWN:
            model2.dvogenie_igroc(r.pos[0],r.pos[1])
        if r.type==pygame.KEYUP and r.key==pygame.K_F11:
            a=pygame.display.get_surface()
            if a.get_width()==683:
                pygame.display.set_mode(flags=pygame.FULLSCREEN)
            else:

                pygame.display.set_mode([683, 384])

