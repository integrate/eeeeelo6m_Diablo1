import fullscreen,pygame

def draw_picture(screen,rect,cartinka,color):
    rect=fullscreen.fullscreen_rect(rect,screen,'war',False)

    picture=fullscreen.fullscreen_surface(screen,cartinka)

    pygame.draw.rect(screen, color, rect)

    screen.blit(picture, rect)
    return rect