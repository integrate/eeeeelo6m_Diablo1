import pygame,model2,view2,os,controller
from pygame import event




def controller2():
    e=event.get()
    for r in e:
        if r.type==pygame.QUIT:
            exit()
        if r.type==pygame.MOUSEBUTTONDOWN:
            model2.attack_igroc(r.pos[0],r.pos[1])
        model2.panel.init_event(r)
        # model2.panel_wrag.init_event(r)
        if r.type==model2.TIMER_DO_VIBOR:
            model2.do_vibor_vrag()
        if r.type==model2.TIMER_DO_ISPL:
            model2.ispl_orugie_vrag()
        if r.type==model2.TIMER_DO_HOD:
            model2.hod_wrag()
        if r.type== pygame.MOUSEBUTTONDOWN:
            model2.effect_statistik(r.pos[0],r.pos[1])


        controller.f11(r)

