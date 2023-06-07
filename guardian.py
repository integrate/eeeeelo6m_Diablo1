import igroc_war


class Guardian(igroc_war.Igroc_war):
    def __init__(self,*args,**kwargs):
        igroc_war.Igroc_war.__init__(self,*args,**kwargs)
        self.clas='Guardian'

