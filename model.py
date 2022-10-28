import pygame,settings, stenaputi as osnovnay_stena, igroc as igroc_mod, derevy, random

obshie_nospawn = []
obshie = []
igroc = igroc_mod.Igroc(0, 1000, 100, 1, 1, 25, 25, obshie)


def add_stena_puti():
    global vid
    vid=random.randint(1,3)

    stena(0, 0,100, 2000, 400)
    stena(400, -400, 100, 2400, 400)
    stena(-2500, -400, 2900, 100, 400)
    stena(-2700,0 , 2700, 100, 400)


def add_exit():
    global a
    a=pygame.Rect(-2600,-275,150,150)



add_exit()



def stena(x,y,w,h,nospawn=200):
    stena = osnovnay_stena.Stenaputi(x,y,w,h,nospawn)
    obshie.append(stena)
    obshie_nospawn.append(stena.rect_nospawn)




add_stena_puti()


def add_derevo():
    colder=500
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
