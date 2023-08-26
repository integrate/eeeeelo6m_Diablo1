import random
from Orugie import orugie


class Axe_energi(orugie.Orugie):
    def __init__(self, modification=None):
        orugie.Orugie.__init__(self, [0, 3], 'легендарный топор который претворяется молотом', 'picture/топор.png', 3)


    def do_attack(self,wrag):
        a=random.randint(self.damage[0],self.damage[1])
        if a>0:
            a+=1
            print(a)
        wrag.hp-=a


