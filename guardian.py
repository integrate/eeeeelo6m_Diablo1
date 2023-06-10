import igroc_war


class Guardian(igroc_war.Igroc_war):
    def __init__(self,*args,**kwargs):
        igroc_war.Igroc_war.__init__(self,*args,**kwargs)
        self.clas='Guardian'

    def ulta(self):
        if self.point == self.need_point:
            self.orugie.smena_damage(1,1)
            self.orugie_2.smena_damage(1,1)
            self.orugie.range+=1
            self.orugie_2.range+=1
            self.point = 0

