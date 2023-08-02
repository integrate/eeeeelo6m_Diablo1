import fullscreen,pygame
import settings
from pygame import font


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


def text(txt, font, w_panel,color=(0,0,0)):
    a = ''
    s = pygame.Surface([0, 0])
    j = []
    words = txt.split()
    i= font.render(' ',True,color)
    for r in words:
        e = font.render(r, True, color)
        if a == '':
            a = r
        elif e.get_width() + s.get_width()+ i.get_width() <= w_panel:
            a = a + ' ' + r
        else:
            j.append(s)
            a = r
        s = font.render(a, True,color)
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

def draw_txt(screen:pygame.surface.Surface,txt,font_name,size,color):
    font=pygame.font.SysFont(font_name,size,True)
    a=font.render(txt,True,color)
    rect=pygame.rect.Rect(0,0,settings.BASE_W,settings.BASE_H)
    draw_picture(screen,rect,a,None)


def wirawnivonie_txt(fonta, color, txt,rect):
    txt_size = 1
    fonti = font.SysFont(fonta, txt_size, True)
    text = fonti.render(txt, True, color)
    while text.get_height() < rect.h:
        txt_size += 1
        fonti = font.SysFont(fonta, txt_size, True)
        text = fonti.render(txt, True, color)
    if txt_size > 1: txt_size -= 1
    fonti = font.SysFont(fonta, txt_size, True)
    text = fonti.render(txt, True, color)
    if text.get_width() > rect.w:
        a = text.get_width() / rect.w
        text = pygame.transform.scale(text, [text.get_width() / a, text.get_height() / a])
    return text



