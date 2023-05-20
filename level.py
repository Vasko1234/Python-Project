from tiles import Tile
import pygame

class Level:
    def __init__(self, level_map, surface):
        self.display_surface = surface
        self.setup_level(level_map)

    def setup_level(self, layout):
        self.tiles = pygame.sprite.Group()

    def run(self):
        self.tiles.draw(self.display_surface)