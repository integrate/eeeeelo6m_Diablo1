import random,settings
def add_derevo(col,maker,obshie_nospawn,obshie,povtor=10,finalnospawn=150):
    colpowtor=povtor
    nospawn_here= obshie_nospawn.copy

    while col > 0:
        if colpowtor == 0:
            colpowtor = povtor
            col -= 1
        if colpowtor == povtor:
            derevo =maker(random.randint(-settings.MAP_SIZE / 2, settings.MAP_SIZE / 2 - 50),
                                   random.randint(-settings.MAP_SIZE / 2, settings.MAP_SIZE / 2))
                # derevy.Derevo(, 50, 50, 100)
        if derevo.rect.collidelist(obshie_nospawn) != -1 and colpowtor > 0:
            derevo =maker(random.randint(-settings.MAP_SIZE / 2, settings.MAP_SIZE / 2 - 50),
                                   random.randint(-settings.MAP_SIZE / 2, settings.MAP_SIZE / 2))
            colpowtor -= 1
        if derevo.rect.collidelist(obshie_nospawn) == -1:
            obshie.append(derevo)
            obshie_nospawn.append(derevo.rect_nospawn)
            col -= 1
            colpowtor = povtor