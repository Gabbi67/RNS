import math

import pygame.display
from pygame.color import THECOLORS
from source import set, src


def angle(x, y, screen_size):
    rns1_pos = [screen_size[0] / 2 - set.start_d / 2, screen_size[1] / 2]
    rns2_pos = [screen_size[0] / 2 + set.start_d / 2, screen_size[1] / 2]
    AB = [0, 0]
    AB[0] = rns1_pos[0] - x
    AB[1] = rns1_pos[1] - y
    CD = [0, 0]
    CD[0] = rns2_pos[0] - x
    CD[1] = rns2_pos[1] - y
    ABCD = AB[0] * CD[0] + AB[1] * CD[1]
    modAB = math.sqrt(pow(AB[0], 2) + pow(AB[1], 2))
    modCD = math.sqrt(pow(CD[0], 2) + pow(CD[1], 2))
    if modAB * modCD != 0:
        cosa = ABCD / (modAB * modCD)
    else:
        cosa = 0
    a = math.acos(cosa) * 180 / math.pi
    return a


def signal(x, y, screen_size):
    rns1_pos = [screen_size[0] / 2 - set.start_d / 2, screen_size[1] / 2]
    rns2_pos = [screen_size[0] / 2 + set.start_d / 2, screen_size[1] / 2]
    l1 = math.sqrt(((rns1_pos[0] - x) ** 2) + ((rns1_pos[1] - y) ** 2))
    l2 = math.sqrt(((rns2_pos[0] - x) ** 2) + ((rns2_pos[1] - y) ** 2))

    if l1 and l2 != 0:
        P1 = set.p / (4 * 3.14 * (float(l1 * (10 ** 3)) ** 2))
        P2 = 2.24 / (4 * 3.14 * (float(l2 * (10 ** 3)) ** 2))
        p = min(P1, P2) * (0.0004 / set.N)
        return p
    else:
        p = 100000
        return p


def color(x, y, screen_size=set.screen_start_size):
    a = angle(x, y, screen_size)
    s = signal(x, y, screen_size)
    if x > 200 or not y > screen_size[1] - 120:
        if 89 < a < 91:
            return THECOLORS["yellow"]
        elif s > set.min_p and set.range_a[0] < a < set.range_a[1]:
            return THECOLORS["green"]
        elif s > set.min_p:
            return 150, 150, 150
        elif set.range_a[0] < a < set.range_a[1]:
            return 100, 100, 100
        else:
            return THECOLORS["darkslategrey"]
    else:
        return 0


def mouse_check(x, y, screen_size=set.screen_start_size):
    pygame.draw.rect(set.screen, THECOLORS["darkslategray"], (0, screen_size[1] - 114, 200, 114))
    src.static_bg(screen_size)
    a = angle(x, y, screen_size)
    s = signal(x, y, screen_size)

    if set.range_a[0] < a < set.range_a[1]:
        txt_surface = set.small_font.render("a = " + str(round(a, 2)), True, THECOLORS["chartreuse"])
        set.screen.blit(txt_surface, (15, screen_size[1] - 100))
    else:
        txt_surface = set.small_font.render("a = " + str(round(a, 2)), True, THECOLORS["firebrick1"])
        set.screen.blit(txt_surface, (15, screen_size[1] - 100))

    if s > set.min_p:
        txt_surface = set.small_font.render("S/N = " + str(round(s, 2)), True, THECOLORS["chartreuse"])
        set.screen.blit(txt_surface, (15, screen_size[1] - 50))
    else:
        txt_surface = set.small_font.render("S/N = " + str(round(s, 2)), True, THECOLORS["firebrick1"])
        set.screen.blit(txt_surface, (15, screen_size[1] - 50))

    pygame.display.flip()


