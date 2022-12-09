import pygame
from pygame import event


def controller2():
    e=event.get()
    for r in e:
        print(r.type)
