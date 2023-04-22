import pygame, settings, stenaputi as osnovnay_stena, igroc as igroc_mod, derevy, random, \
    time,vrag,randomspawn,exit as exit_mod





def add_stena_puti():
    global vid, exit, spawn
    vid = random.randint(1, 3)

    stena(0, 0, 100, 2000, 400)
    stena(400, -400, 100, 2400, 400)
    stena(-2500, -400, 2900, 100, 400)
    stena(-2700, 0, 2700, 100, 400)
    exit = exit_mod.Exit(-2600, -275, 150, 150)
    spawn = [250, 3000]
    igroc.rect_igroc.x = spawn[0]
    igroc.rect_igroc.y = spawn[1]


def stena(x, y, w, h, nospawn=200):
    stena = osnovnay_stena.Stenaputi(x, y, w, h, nospawn)
    obshie.append(stena)
    obshie_nospawn.append(stena.rect_nospawn)


def add_vrag():
    def maker(x, y):
        derevo = vrag.Vrag(x, y)
        return derevo
    randomspawn.add_derevo(50,maker,obshie_nospawn,obshie,50)


def add_derevo():
    def maker(x,y):
        derevo = derevy.Derevo(x,y,75,75,100)
        return derevo

    randomspawn.add_derevo(500,maker,obshie_nospawn,obshie,50)



def add_granici():
    granici_top = osnovnay_stena.Vid2(-settings.MAP_SIZE / 2, -settings.MAP_SIZE / 2 - settings.MAP_FAT,
                                      settings.MAP_SIZE, settings.MAP_FAT)
    obshie.append(granici_top)
    granici_down = osnovnay_stena.Vid2(-settings.MAP_SIZE / 2, settings.MAP_SIZE / 2 + 200, settings.MAP_SIZE,
                                       settings.MAP_FAT)
    obshie.append(granici_down)
    granici_left = osnovnay_stena.Vid2(-settings.MAP_SIZE / 2 - settings.MAP_FAT,
                                       -settings.MAP_SIZE / 2 - settings.MAP_FAT, settings.MAP_FAT,
                                       settings.MAP_SIZE + settings.MAP_FAT)
    obshie.append(granici_left)
    granici_right = osnovnay_stena.Vid2(settings.MAP_SIZE / 2, -settings.MAP_SIZE / 2 - settings.MAP_FAT,
                                        settings.MAP_FAT, settings.MAP_SIZE + settings.MAP_FAT)
    obshie.append(granici_right)


def next_lvl():
    global lvl,  go_to_next_lvl, sostoynie

    if igroc.rect_igroc.colliderect(exit) and sostoynie==SOSTOYNIE_NORMAL:
        go_to_next_lvl = time.time()
        sostoynie = SOSTOYNIE_POTEMNENIE
        # if time.time() - go_to_next_lvl > 2:
            #     lvl -= 1


def go_right():
    global sostoynie,go_to_next_lvl
    if sostoynie == SOSTOYNIE_NORMAL:
        a=igroc.dvigenie_right()
        if type(a) is vrag.Vrag:
            sostoynie=SOSTOYNIE_POTEMNENIE_WAR
            go_to_next_lvl = time.time()


def go_left():
    global sostoynie,go_to_next_lvl
    if sostoynie == SOSTOYNIE_NORMAL:
        a=igroc.dvigenie_left()
        if type(a)is vrag.Vrag:
            sostoynie=SOSTOYNIE_POTEMNENIE_WAR
            go_to_next_lvl = time.time()


def go_down():
    global sostoynie,go_to_next_lvl
    if sostoynie == SOSTOYNIE_NORMAL:
        a=igroc.dvigenie_bottom()
        if type(a) is vrag.Vrag:
            sostoynie=SOSTOYNIE_POTEMNENIE_WAR
            go_to_next_lvl = time.time()


def go_top():
    global sostoynie,go_to_next_lvl
    if sostoynie == SOSTOYNIE_NORMAL:
        a=igroc.dvigenie_top()
        if type(a) is vrag.Vrag:
            sostoynie=SOSTOYNIE_POTEMNENIE_WAR
            go_to_next_lvl = time.time()



def step():
    global sostoynie,go_to_next_lvl
    if time.time() - go_to_next_lvl > 2.5 and sostoynie == SOSTOYNIE_POTEMNENIE_WAR:
        sostoynie=SOSTOYNIE_START_WAR
    if time.time()-go_to_next_lvl>2.5 and sostoynie==SOSTOYNIE_POTEMNENIE:
        sostoynie=SOSTOYNIE_PEREGENERACIY

    elif sostoynie==SOSTOYNIE_PEREGENERACIY :
        obshie.clear()
        obshie_nospawn.clear()
        add_stena_puti()
        add_granici()
        add_derevo()
        add_vrag()
        time.sleep(random.randint(100,200)/100)
        sostoynie=SOSTOYNIE_OSVETLENIE
        go_to_next_lvl=time.time()
    elif sostoynie==SOSTOYNIE_OSVETLENIE  and 2.5-(time.time()-go_to_next_lvl)<0:
        sostoynie=SOSTOYNIE_NORMAL



obshie_nospawn = []
obshie = []
igroc = igroc_mod.Igroc(0, 1000, 100, 10, 3, 100, 100, obshie)
lvl = 5
go_to_next_lvl = 0
SOSTOYNIE_NORMAL=1
SOSTOYNIE_POTEMNENIE=2
SOSTOYNIE_PEREGENERACIY=3
SOSTOYNIE_OSVETLENIE=4
SOSTOYNIE_POTEMNENIE_WAR=5
SOSTOYNIE_OSVETLENIE_WAR=6
SOSTOYNIE_START_WAR=7
exit=None
sostoynie = SOSTOYNIE_START_WAR # potemnenie,peregeneraciy,osvetlenie,
add_stena_puti()
add_granici()
add_derevo()
add_vrag()
