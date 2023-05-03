import fullscreen,pygame

def draw_picture(screen,rect,cartinka:pygame.Surface,color,point_pic='center',point_rect='center'):
    rect=fullscreen.fullscreen_rect(rect,screen,'war',False)
    picture=fullscreen.fullscreen_surface(screen,cartinka)
    rect_2=pygame.Rect(0,0,picture.get_width(),picture.get_height())

    rect_2.__setattr__(point_pic,rect.__getattribute__(point_rect))
    if color!=None:
        pygame.draw.rect(screen, color, rect)
        # pygame.draw.rect(screen,color,rect_2)
    screen.blit(picture, rect_2)
    return rect


def text(txt, font, w_panel):
    a = ''
    s = pygame.Surface([0, 0])
    j = []
    words = txt.split()
    i= font.render(' ',True,[123,123,123])
    for r in words:
        e = font.render(r, True, [0, 0, 0])
        if a == '':
            a = r
        elif e.get_width() + s.get_width()+ i.get_width() <= w_panel:
            a = a + ' ' + r
        else:
            j.append(s)
            a = r
        s = font.render(a, True, [0, 0, 0])
    j.append(s)
    o = 0
    for v in j:
        if v.get_width() > o:
            o = v.get_width()
    k = pygame.Surface([o, len(j) * font.get_height()], pygame.SRCALPHA)
    o = 0
    for e in j:
        k.blit(e, [0, o])
        o += font.get_height()

    return k