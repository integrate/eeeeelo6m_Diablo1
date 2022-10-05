import pygame,stenaputi as osnovnay_stena,igroc as igroc_mod,derevy

obshie=[]
igroc=igroc_mod.Igroc(0,0,100,1,1,10,10,obshie)
def add_stena_puti():
    stena=osnovnay_stena.Stenaputi(-275,631,500,76)
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