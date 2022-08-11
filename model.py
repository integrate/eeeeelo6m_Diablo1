import pygame,stenaputi as osnovnay_stena
igroc=pygame.Rect(400,200,100,100)
derevo=pygame.Rect(525,175,50,50)
steniputi=[]
def add_stena_puti():
    stena=osnovnay_stena.Stenaputi(0,0,1366,768)
    steniputi.append(stena)
add_stena_puti()
def step():
    pass