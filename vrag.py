import pygame,fullscreen,nospawn as modul_nospawn

import wrag_skelet


class Vrag(modul_nospawn.Nospawn,wrag_skelet.Wrag_skelet):
    def __init__(self,x,y,w,h):
        modul_nospawn.Nospawn.__init__(self,x,y,150,150,25)
        wrag_skelet.Wrag_skelet.__init__(self,x,y)
        self.rect=pygame.Rect(x,y,w,h)