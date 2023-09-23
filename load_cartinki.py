import pygame.image

a={}
def get_picture(put):
    if put in a.keys(): return a[put]
    pic=pygame.image.load(put)
    print(put)
    a[put]=pic
    return pic






# 'picture/rock_stena.png': 'загруженая стена'