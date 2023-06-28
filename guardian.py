import effect
import effect_ulta_guardian
import igroc_war


class Guardian(igroc_war.Igroc_war):
    def __init__(self, *args, **kwargs):
        igroc_war.Igroc_war.__init__(self, *args, **kwargs)
        self.clas = 'Guardian'

    def ulta(self):
        if self.point == self.need_point:
            ultimat = effect_ulta_guardian.Effect_ulta_guardian(self.orugie, self.orugie_2)
            self.point=0
            self.effects.append(ultimat)
