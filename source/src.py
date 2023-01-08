import pygame
from pygame.color import THECOLORS
from source import set, cond


def init():
    pygame.init()
    set.screen.fill(THECOLORS["darkslategrey"])
    static_bg(set.screen_start_size)


def screen_resized():
    global screen_dyn_size
    screen_dyn_size = set.screen.get_size()
    set.screen.fill(THECOLORS["darkslategrey"])
    static_bg(screen_dyn_size)


def static_bg(screen_size = set.screen_start_size):
    rns1_pos = [screen_size[0] / 2 - set.start_d / 2, screen_size[1] / 2]
    rns2_pos = [screen_size[0] / 2 + set.start_d / 2, screen_size[1] / 2]
    pygame.draw.circle(set.screen, (255, 255, 255), rns1_pos, 5, 3)
    pygame.draw.circle(set.screen, (255, 255, 255), rns2_pos, 5, 3)


def graph():
    screen_size = set.screen.get_size()
    for x in range(screen_size[0]):
        for y in range(screen_size[1]):
            set.screen.set_at((x, y), cond.color(x, y, screen_size))
        # Добавить для плавного изменения экрана
        pygame.display.flip()
        static_bg(screen_size)
    static_bg(screen_size)
