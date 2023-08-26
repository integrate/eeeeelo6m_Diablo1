import random
from Orugie import axe_energi, multi_orugie_effects
import full_igroc


class Wrag_skelet(full_igroc.Full_igroc):
    def __init__(self, x, y):
        hp = random.randint(7, 10)
        stamina = random.randint(3, 4)

        orugie_igroc = axe_energi.Axe_energi()
        orugie_igroc_2 = multi_orugie_effects.Multi_orugie_effects()
        full_igroc.Full_igroc.__init__(self, x, y, 0, 0, [], hp,hp,stamina, color=[220, 160, 255], cletca_color=[255, 92, 75],
                                       orugie=orugie_igroc_2, orugie_2=orugie_igroc)
