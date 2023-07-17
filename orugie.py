import random,observer


class Orugie(observer.Observer):
    EVENT_SMENA_DAMAGE=1
    def __init__(self, damage, opisanie, cartinca, range):
        observer.Observer.__init__(self)
        self.damage = damage.copy()
        self.damage_base = damage.copy()
        self.opisanie = opisanie
        self.cartinca = cartinca
        self.range = range
        self.range_base = range

    def do_damage(self):
        return random.randint(self.damage[0], self.damage[1])

    def find_avg_damage(self):
        return (self.damage[0] + self.damage[1]) / 2

    def smena_damage(self, min, max):
        self.damage[0] += min
        self.damage[1] += max
        self.notify(self.EVENT_SMENA_DAMAGE)

    def base_stat(self):
        self.damage=self.damage_base.copy()
        self.range=self.range_base
        self.notify(self.EVENT_SMENA_DAMAGE)
