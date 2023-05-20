import pygame
from tiles import Tile
from settings import tile_size
from player import Player

class Level:
    def __init__(self, level_map, surface):
        self.display_surface = surface
        self.setup_level(level_map)
        self.world_shift = 0

    def setup_level(self, layout):
        self.tiles = pygame.sprite.Group()
        self.player = pygame.sprite.Group()

        for row_index, row in enumerate(layout):
            for col_index, cell in enumerate(row):
                x = col_index * tile_size
                y = row_index * tile_size

                if cell == "X":
                    tile = Tile((x, y), tile_size)
                    self.tiles.add(tile)
                if cell == "P":
                    player = Player((x, y))
                    self.player.add(player)

    def run(self):
        self.tiles.update(self.world_shift)
        self.tiles.draw(self.display_surface)

        self.player.update()
        self.player.draw(self.display_surface)