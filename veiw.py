# 1366,768
import pygame,os



os.environ['SDL_VIDEO_WINDOW_POS'] = "341,192"

# screen = pygame.display.set_mode(flags=pygame.FULLSCREEN)
screen = pygame.display.set_mode([683, 384])
# screen = pygame.display.set_mode([1366,150])
# print(screen.get_rect())
import model, stenaputi, fullscreen, settings, time,model_view
from pygame import display, draw
import nospawn
import wrag_skelet

perehod = pygame.Surface([settings.BASE_W,settings.BASE_H], pygame.SRCALPHA)

perehod.fill([0, 0, 0, 0])


def world(what, minimap):
    mul = 'minimap' if minimap else 'map'
    model.exit.draw(what,minimap)
    for stenaputi in model.obshie:
        stenaputi.draw(what, minimap)
        # if wrag_skelet.Wrag_skelet is stenaputi.__class__:
        # nospawn.Nospawn.draw(stenaputi,what,mul)
    model.igroc.draw(what, minimap)



# def smena_minimap():


def veiw():

    screen.fill([30, 255, 30])
    world(screen, False)
    model_view.minimap.fill([73, 97, 0])
    world(model_view.minimap, True)
    screen.blit(model_view.minimap, model_view.rect_minimap)
    perehod_2=fullscreen.fullscreen_surface(screen,perehod,'1')



    if model.sostoynie == model.SOSTOYNIE_POTEMNENIE or model.sostoynie == model.SOSTOYNIE_POTEMNENIE_WAR  and time.time() - model.go_to_next_lvl < 2.5:
        perehod_2.fill([0, 0, 0, (time.time() - model.go_to_next_lvl) * 100])
        screen.blit(perehod_2, [0, 0])

    if model.sostoynie == model.SOSTOYNIE_OSVETLENIE and 2.5 - (time.time() - model.go_to_next_lvl) > 0:
        screen.blit(perehod_2, [0, 0])
        perehod_2.fill([0, 0, 0, 250 - (time.time() - model.go_to_next_lvl) * 100])

    if (model.sostoynie == model.SOSTOYNIE_POTEMNENIE or model.sostoynie == model.SOSTOYNIE_POTEMNENIE_WAR) and time.time() - model.go_to_next_lvl > 2.5:
        perehod_2.fill([0, 0, 0, 255])
        screen.blit(perehod_2, [0, 0])

    if model.sostoynie == model.SOSTOYNIE_PEREGENERACIY:
        perehod_2.fill([0, 0, 0, 255])
        screen.blit(perehod_2, [0, 0])
    if model.sostoynie == model.SOSTOYNIE_WIN_WAR:
        perehod_2.fill([0, 0, 0])

    display.flip()
