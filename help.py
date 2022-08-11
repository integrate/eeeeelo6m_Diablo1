import pygame
def izmeni_kartinku(kartinka: pygame.Surface, shirina, visota, uberi_cvet, porog, replace_color=[0, 0, 0, 0]):
    # change pic size
    kartinka = pygame.transform.scale(kartinka, [shirina, visota])

    # convert to picture with transparency data
    kartinka = kartinka.convert_alpha()

    # get mask of pixels with ignored colors
    m1 = pygame.mask.from_threshold(kartinka, uberi_cvet, [porog, porog, porog])

    # make square filled with one of ignored colors
    q2 = kartinka.copy()

    # set pixels should be transparent, unset pixels should be taken from original picture
    m1.to_surface(q2, setcolor=replace_color, unsetsurface=kartinka)
    return q2