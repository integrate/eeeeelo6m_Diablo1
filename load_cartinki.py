import pygame.image


a={}
def get_picture(put):
    if put in a.keys(): return a[put]
    pic=pygame.image.load(put)
    # print(put)
    a[put] = pic


    return pic


b=[]
def scale_picture(pic,w,h):
    for e in b:
        if pic is e['pic'] and w == e['w'] and h == e['h']: return e['done_pic']
    a={'pic':pic,'w':w,'h':h}
    cartinka = pygame.transform.scale(pic, [w, h])
    a['done_pic']=cartinka
    b.append(a)
    # print(pic,w,h,a['done_pic'])
    return a['done_pic']


def do_picture(pic,w,h):
    a=get_picture(pic)
    return scale_picture(a,w,h)







# 'picture/rock_stena.png': 'загруженая стена'