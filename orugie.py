import random


class Orugie():
    def __init__(self, damage, opisanie, cartinca, range):
        self.damage = damage
        self.damage_base = damage
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
