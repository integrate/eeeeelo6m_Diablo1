import effect


class Effect_ulta_guardian(effect.Effect):
    def __init__(self, orugie, orugie_2):
        effect.Effect.__init__(self, self.deystvie, 1)
        self.orugie = orugie
        self.orugie_2 = orugie_2

    def deystvie(self):
        self.orugie.smena_damage(1, 1)
        self.orugie_2.smena_damage(1, 1)
        self.orugie.range += 1
        self.orugie_2.range += 1
