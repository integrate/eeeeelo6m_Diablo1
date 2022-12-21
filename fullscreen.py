import model,settings,pygame

def fulscren(screen,w, h,x, y,mul,sdvig=True):
    base_w = 1366*settings.MUL[mul]
    base_h = 768*settings.MUL[mul]

    wp=screen.get_width() * model.igroc.rect_igroc.width / base_w
    hp=screen.get_height() * model.igroc.rect_igroc.height / base_h
    xp=screen.get_width() * model.igroc.rect_igroc.x / base_w
    yp=screen.get_height() * model.igroc.rect_igroc.y / base_h

    w = screen.get_width() * w / base_w
    h = screen.get_height() * h / base_h
    x = screen.get_width() * x / base_w
    y = screen.get_height() * y / base_h

    if sdvig==True:
        sdvigx=+screen.get_width()/2-xp-wp/2
        sdvigy=screen.get_height()/2-yp-hp/2
        y+=sdvigy
        x+=sdvigx

    return x,y,w,h

def fullscreen_rect(rect,screen,mul,sdvig=True):

    a=pygame.Rect(fulscren(screen,rect.w,rect.h,rect.x,rect.y,mul,sdvig))
    return a
