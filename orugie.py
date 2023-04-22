import random

class Orugie():
    def __init__(self,damage,opisanie,cartinca,range):
        self.damage=damage
        self.opisanie=opisanie
        self.cartinca=cartinca
        self.range=range
    def do_damage(self):
        return random.randint(self.damage[0],self.damage[1])
