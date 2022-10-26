import pygame,settings, stenaputi as osnovnay_stena, igroc as igroc_mod, derevy, random

obshie_nospawn = []
obshie = []
igroc = igroc_mod.Igroc(0, 1000, 100, 1, 1, 100, 100, obshie)


def add_stena_puti():
    stena = osnovnay_stena.Stenaputi(-275, 631, 100, 200, 200)
    obshie.append(stena)
    obshie_nospawn.append(stena.rect_nospawn)
    stena = osnovnay_stena.Stenaputi(-270, 10, 700, 4, 200)
    obshie.append(stena)
    obshie_nospawn.append(stena.rect_nospawn)



add_stena_puti()


def add_derevo():
    colder=1250
    colpowtor=50
    while colder>0 :
        if colpowtor==0:
            colpowtor=50
            colder-=1
        if colpowtor==50:
            derevo = derevy.Derevo(random.randint(-settings.MAP_SIZE/2, settings.MAP_SIZE/2-50), random.randint(-settings.MAP_SIZE/2, settings.MAP_SIZE/2), 50, 50, 100)
        if derevo.rect.collidelist(obshie_nospawn)!=-1 and colpowtor>0:
            derevo = derevy.Derevo(random.randint(-settings.MAP_SIZE/2, settings.MAP_SIZE/2-50), random.randint(-settings.MAP_SIZE/2, settings.MAP_SIZE/2), 50, 50, 100)
            colpowtor-=1
        if derevo.rect.collidelist(obshie_nospawn)==-1:
            obshie.append(derevo)
            obshie_nospawn.append(derevo.rect_nospawn)
            colder-=1
            colpowtor=50



def add_granici():
    granici_top = osnovnay_stena.Vid2(-settings.MAP_SIZE/2, -settings.MAP_SIZE/2-settings.MAP_FAT, settings.MAP_SIZE, settings.MAP_FAT)
    obshie.append(granici_top)
    granici_down = osnovnay_stena.Vid2(-settings.MAP_SIZE/2, settings.MAP_SIZE/2+200, settings.MAP_SIZE, settings.MAP_FAT)
    obshie.append(granici_down)
    granici_left = osnovnay_stena.Vid2(-settings.MAP_SIZE/2-settings.MAP_FAT, -settings.MAP_SIZE/2-settings.MAP_FAT, settings.MAP_FAT, settings.MAP_SIZE+settings.MAP_FAT)
    obshie.append(granici_left)
    granici_right = osnovnay_stena.Vid2(settings.MAP_SIZE/2, -settings.MAP_SIZE/2-settings.MAP_FAT, settings.MAP_FAT,settings.MAP_SIZE+settings.MAP_FAT)
    obshie.append(granici_right)


add_granici()

add_derevo()


def step():
    pass
