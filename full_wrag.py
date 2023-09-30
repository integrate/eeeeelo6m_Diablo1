import igroc_war
import real_world_object
from Orugie import orugie

class Full_wrag(real_world_object.Real_world_object,igroc_war.Igroc_war):
    def __init__(self, x, y,w,h,hp,max_hp,stamina,cartinka, point=None, need_point=None,
                 color=[255, 30, 30],
                 cletca_color=[255, 100, 100],orugie: orugie.Orugie = None, orugie_2: orugie.Orugie = None):
        igroc_war.Igroc_war.__init__(self, hp, max_hp, stamina, point, need_point, color,
                                     cletca_color, orugie, orugie_2,cartinka)
        real_world_object.Real_world_object.__init__(self,x,y,w,h,25,cartinka)