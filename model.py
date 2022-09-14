import pygame,stenaputi as osnovnay_stena,igroc as igroc_mod

derevo=pygame.Rect(525,175,50,50)
steniputi=[]
igroc=igroc_mod.Igroc(0,0,100,1,1,10,10,steniputi)
def add_stena_puti():
    stena=osnovnay_stena.Stenaputi(270,63,40,76)
    steniputi.append(stena)
    stena=osnovnay_stena.Stenaputi(-123,73,73,873)
    steniputi.append(stena)
add_stena_puti()


def step():
    pass