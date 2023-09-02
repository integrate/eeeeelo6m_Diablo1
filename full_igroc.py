import igroc
import igroc_war
from Orugie import orugie


class Full_igroc(igroc.Igroc, igroc_war.Igroc_war):
    def __init__(self, x, y, speedx, speedy, rects, hp,max_hp,stamina, point=None, need_point=None,
                 color=[255, 30, 30],
                 cletca_color=[255, 100, 100], orugie: orugie.Orugie = None, orugie_2: orugie.Orugie = None,w=100,h=100):
        igroc.Igroc.__init__(self, x, y, speedx, speedy, rects,w,h,color)
        igroc_war.Igroc_war.__init__(self, hp,max_hp,stamina,point, need_point, color,
                                     cletca_color, orugie, orugie_2)
