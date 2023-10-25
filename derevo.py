import exit
import real_world_object
import wrag_skelet


class Derevo(real_world_object.Real_world_object):
    def __init__(self,x,y,w,h):
        real_world_object.Real_world_object.__init__(self,x,y,w,h,'picture/дерево.png',{wrag_skelet.Wrag_skelet:500,exit.Exit:100},1000)