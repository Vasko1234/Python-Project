import pygame
import sys
from settings import *
from overworld import Overworld

class Game:
    def __init__(self):
        self.max_level = 3
        self.overworld = Overworld(0, self.max_level, screen)

    def run(self):
        self.overworld.run()

pygame.init()

FPS = 240
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
game = Game()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.set_caption(f"FPS: {int(clock.get_fps())}")
    screen.fill((0, 0, 0))
    game.run()

    pygame.display.update()
    clock.tick(FPS)