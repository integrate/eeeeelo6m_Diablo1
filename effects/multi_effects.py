from effects import effect
import random,igroc_war

class Multi_effects(effect.Effect):
    def __init__(self,igroc:igroc_war.Igroc_war):
        effect.Effect.__init__(self,self.deystvie,"picture/img.png",2)
        self.igroc=igroc


    def deystvie(self):
        a=random.randint(29,29)
        if 1<=a<=4:
            self.igroc.stamina-=2
        elif 5<=a<=8:
            self.igroc.max_hp-=5
        elif 9<=a<=12:
            self.igroc.orugie.range-=1
            self.igroc.orugie_2.range-=1
        elif 13<=a<=16:
            self.igroc.orugie.smena_damage(-2,-2)
            self.igroc.orugie_2.smena_damage(-2,-2)
        elif 17<=a<=19:
            self.igroc.max_hp -= 5
            self.igroc.stamina -= 2
        elif 20<=a<=22:
            self.igroc.orugie.smena_damage(-2, -2)
            self.igroc.orugie_2.smena_damage(-2, -2)
            self.igroc.orugie.range -= 1
            self.igroc.orugie_2.range -= 1
        elif 23<=a<=25:
            self.igroc.orugie.range -= 1
            self.igroc.orugie_2.range -= 1
            self.igroc.stamina -= 2
        elif 26<=a<=28:
            self.igroc.max_hp -= 5
            self.igroc.orugie.smena_damage(-2, -2)
            self.igroc.orugie_2.smena_damage(-2, -2)
        elif a==29:
            self.igroc.max_hp -= 5
            self.igroc.orugie.smena_damage(-2, -2)
            self.igroc.orugie_2.smena_damage(-2, -2)
            self.igroc.orugie.range -= 1
            self.igroc.orugie_2.range -= 1
            self.igroc.stamina -= 2
        elif a==30:
            self.igroc.hp+=1000





