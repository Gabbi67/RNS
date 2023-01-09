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
    pygame.draw.circle(set.screen, THECOLORS["red"], rns1_pos, 5)
    pygame.draw.circle(set.screen, THECOLORS["red"], rns2_pos, 5)
    pygame.draw.rect(set.screen, THECOLORS["ivory4"], (0, screen_size[1] - 120, 200, 6))
    pygame.draw.rect(set.screen, THECOLORS["ivory4"], (200, screen_size[1] - 120, 6, 120))


def graph():
    screen_size = set.screen.get_size()
    pygame.draw.rect(set.screen, THECOLORS["darkslategrey"], (0, screen_size[1] - 114, 200, 114))
    for x in range(screen_size[0]):
        for y in range(screen_size[1]):
            color = cond.color(x, y, screen_size)
            if color != 0:
                set.screen.set_at((x, y), color)
        # Вкл/выкл плавного изменения экрана (2 строки)
        pygame.display.flip()
        static_bg(screen_size)
    static_bg(screen_size)


def left_click(x):
    cond.mouse_check(x[0], x[1], set.screen.get_size())