import pygame
import sys
from source import src, set

src.init()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.key == pygame.K_RETURN:
                src.graph()

        if event.type == pygame.WINDOWRESIZED:
            src.screen_resized()



    pygame.display.flip()