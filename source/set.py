import pygame
import sys

screen_start_size = [1024, 768]
screen = pygame.display.set_mode(screen_start_size, pygame.RESIZABLE)

pygame.font.init()
small_font = pygame.font.SysFont("TimesNewRoman", 25)

start_d = 300
range_a = [30, 150]
p = 2.24
min_p = 800
N = 0.5e-18

