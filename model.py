import pygame,stenaputi as osnovnay_stena,igroc as igroc_mod,derevy,granstage

obshie=[]
igroc=igroc_mod.Igroc(0 ,1000,100,1,1,10,10,obshie)
granci=pygame.Rect(-2500,-2500,5000,5000)
def add_stena_puti():
    stena=osnovnay_stena.Stenaputi(-275,631,100,200)
    obshie.append(stena)
    stena=osnovnay_stena.Stenaputi(-270,10,700,4)
    obshie.append(stena)
add_stena_puti()
def add_derevo():
    derevo=derevy.Derevo(525,175,50,50)
    obshie.append(derevo)




add_derevo()

def step():
    pass