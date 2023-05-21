import pygame
import sys
from settings import *
from level import Level

pygame.init()

FPS = 240
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
level = Level(level_map, screen)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.set_caption(f"FPS: {int(clock.get_fps())}")

    screen.fill((0, 0, 0))
    level.run()

    pygame.display.update()
    clock.tick(FPS)