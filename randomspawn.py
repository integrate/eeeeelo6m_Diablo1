import random,settings
def add_derevo(col,maker,obshie,povtor=10):
    object_class=type(maker(0,0))
    colpowtor=povtor
    obshie_nospawn=[]
    for a in obshie:
        obshie_nospawn.append(a.get_nospawn_rect(object_class))
    while col > 0:
        if colpowtor == 0:
            colpowtor = povtor
            col -= 1
        if colpowtor == povtor:
            #TODO не правильный отступ с правой стороны краты у объекта
            derevo =maker(random.randint(-settings.MAP_SIZE / 2, settings.MAP_SIZE / 2 - 50),
                                   random.randint(-settings.MAP_SIZE / 2, settings.MAP_SIZE / 2))
                # derevy.Derevo(, 50, 50, 100)
        if derevo.rect.collidelist(obshie_nospawn) != -1 and colpowtor > 0:
            derevo =maker(random.randint(-settings.MAP_SIZE / 2, settings.MAP_SIZE / 2 - 50),
                                   random.randint(-settings.MAP_SIZE / 2, settings.MAP_SIZE / 2))
            colpowtor -= 1
        if derevo.rect.collidelist(obshie_nospawn) == -1:
            obshie.append(derevo)
            obshie_nospawn.append(derevo.get_nospawn_rect(derevo.__class__))
            col -= 1
            colpowtor = povtor