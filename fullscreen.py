import model, settings, pygame

now_screen = None
pictures = []


def fulscren(screen, w, h, x, y, mul, sdvig=True):
    base_w = settings.BASE_W * settings.MUL[mul]
    base_h = settings.BASE_H * settings.MUL[mul]

    wp = screen.get_width() * model.igroc.rect_igroc.width / base_w
    hp = screen.get_height() * model.igroc.rect_igroc.height / base_h
    xp = screen.get_width() * model.igroc.rect_igroc.x / base_w
    yp = screen.get_height() * model.igroc.rect_igroc.y / base_h

    w = screen.get_width() * w / base_w
    h = screen.get_height() * h / base_h
    x = screen.get_width() * x / base_w
    y = screen.get_height() * y / base_h

    if sdvig == True:
        sdvigx = +screen.get_width() / 2 - xp - wp / 2
        sdvigy = screen.get_height() / 2 - yp - hp / 2
        y += sdvigy
        x += sdvigx

    return x, y, w, h


def fullscreen_rect(rect, screen, mul, sdvig=True):
    a = pygame.Rect(fulscren(screen, rect.w, rect.h, rect.x, rect.y, mul, sdvig))
    return a


def fullscreen_surface(screen, cartinka: pygame.Surface, mul='war'):
    for a in pictures:
        if a['cartinka'] is cartinka and a['mul'] == mul and a['screen']== screen.get_size(): return a['object']
    a = fulscren(screen, cartinka.get_width(), cartinka.get_height(), 0, 0, mul, False)
    a = pygame.transform.scale(cartinka, [a[2], a[3]])
    cartinca = {'cartinka': cartinka, 'mul': mul, 'screen': screen.get_size(), 'object': a}
    pictures.append(cartinca)
    return a
