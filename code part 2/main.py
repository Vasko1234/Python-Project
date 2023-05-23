import pygame
import sys
from settings import *

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
FPS = 240

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.set_caption(f"FPS: {int(clock.get_fps())}")
    screen.fill((0, 0, 0))

    pygame.display.update()
    clock.tick(FPS)