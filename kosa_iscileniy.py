import orugie


class Kosa_iscileniy(orugie.Orugie):
    def __init__(self, modification=None):
        orugie.Orugie.__init__(self, [-5, 5], 'может как и убить так и добавить здоровье врагу',
                               'picture/коса_исцеления.png', 2)


