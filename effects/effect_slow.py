from effects import effect


class Effect_slow(effect.Effect):
    def __init__(self,igroc,strong,long=2):
        statistic = 'stamina' + '-' + str(strong)
        effect.Effect.__init__(self, self.deystvie, 'picture/эфект_slow.png', long,statistic)

        self.igroc=igroc
        self.strong=strong
        self.deystvie()


    def deystvie(self):
        self.igroc.stamina-=self.strong


