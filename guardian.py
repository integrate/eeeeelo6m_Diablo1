from effects import effect_ulta_guardian
import igroc_war
import full_igroc


class Guardian(full_igroc.Full_igroc):
    def __init__(self, x,y,rects,orugie,orugie_2):
        full_igroc.Full_igroc.__init__(self,x,y,25,25,rects,15,15,4,0,7,orugie=orugie,orugie_2=orugie_2)

    def ulta(self):
        if self.point == self.need_point:
            ultimat = effect_ulta_guardian.Effect_ulta_guardian(self.orugie, self.orugie_2)
            self.point=0
            self.effects.append(ultimat)
