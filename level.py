from tiles import Tile
import pygame

class Level:
    def __init__(self, level_map, surface):
        self.display_surface = surface
        self.level_map = level_map