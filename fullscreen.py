import model
def fulscren(screen,w, h,x, y):
    wp=screen.get_width() * model.igroc.rect_igroc.width / 1366
    hp=screen.get_height() * model.igroc.rect_igroc.height / 768
    xp=screen.get_width() * model.igroc.rect_igroc.x / 1366
    yp=screen.get_height() * model.igroc.rect_igroc.y / 768

    w = screen.get_width() * w / 1366
    h = screen.get_height() * h / 768
    x = screen.get_width() * x / 1366
    y = screen.get_height() * y / 768


    sdvigx=+screen.get_width()/2-xp-wp/2
    sdvigy=screen.get_height()/2-yp-hp/2
    y+=sdvigy
    x+=sdvigx

    return x,y,w,h