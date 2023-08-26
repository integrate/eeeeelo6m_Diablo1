import random
from effects import multi_effects

from Orugie import orugie


class Multi_orugie_effects(orugie.Orugie):
    def __init__(self, modification=None):
        orugie.Orugie.__init__(self, [1, 1], 'реликвия господина алхимика', 'picture/мульти_оружие_эфектов.png', 3)


    def do_attack(self,wrag):
        a=random.randint(self.damage[0],self.damage[1])
        wrag.hp-=a
        multi_effect=multi_effects.Multi_effects(wrag)
        wrag.effects.append(multi_effect)



