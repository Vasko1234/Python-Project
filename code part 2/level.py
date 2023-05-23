import pygame
from support import import_csv_layout, import_cut_graphics
from settings import tile_size
from tiles import Tile, StaticTile, Crate, AnimatedTile, Coin, Palm

class Level:
    def __init__(self, level_data, surface):
        self.display_surface = surface
        self.world_shift = 0

        terrain_layout = import_csv_layout(level_data["terrain"])
        self.terrain_sprites = self.create_tile_group(terrain_layout, "terrain")

        grass_layout = import_csv_layout(level_data["grass"])
        self.grass_sprites = self.create_tile_group(grass_layout, "grass")

        crates_layout = import_csv_layout(level_data["crates"])
        self.crates_sprites = self.create_tile_group(crates_layout, "crates")

        coins_layout = import_csv_layout(level_data["coins"])
        self.coins_sprites = self.create_tile_group(coins_layout, "coins")

        fg_palms_layout = import_csv_layout(level_data["fg_palms"])
        self.fg_palms_sprites = self.create_tile_group(fg_palms_layout, "fg_palms")

    def create_tile_group(self, layout, type):
        sprite_group = pygame.sprite.Group()

        for row_index, row in enumerate(layout):
            for col_index, value in enumerate(row):
                if value != "-1":
                    x = col_index * tile_size
                    y = row_index * tile_size

                    if type == "terrain":
                        terrain_tile_list = import_cut_graphics("Python-Project/graphics/terrain/terrain_tiles.png")
                        tile_surface = terrain_tile_list[int(value)]
                        sprite = StaticTile(tile_size, x, y, tile_surface)

                    if type == "grass":
                        grass_tile_list = import_cut_graphics("Python-Project/graphics/decoration/grass/grass.png")
                        tile_surface = grass_tile_list[int(value)]
                        sprite = StaticTile(tile_size, x, y, tile_surface)

                    if type == "crates":
                        sprite = Crate(tile_size, x, y)

                    if type == "coins":
                        if value == "0":
                            sprite = Coin(tile_size, x, y, "Python-Project/graphics/coins/gold")
                        if value == "1":
                            sprite = Coin(tile_size, x, y, "Python-Project/graphics/coins/silver")

                    if type == "fg_palms":
                        if value == "0":
                            sprite = Palm(tile_size, x, y, "Python-Project/graphics/terrain/palm_small", 38)
                        if value == "1":
                            sprite = Palm(tile_size, x, y, "Python-Project/graphics/terrain/palm_large", 64)

                    sprite_group.add(sprite)

        return sprite_group

    def run(self):
        self.terrain_sprites.update(self.world_shift)
        self.terrain_sprites.draw(self.display_surface)

        self.grass_sprites.update(self.world_shift)
        self.grass_sprites.draw(self.display_surface)

        self.crates_sprites.update(self.world_shift)
        self.crates_sprites.draw(self.display_surface)

        self.coins_sprites.update(self.world_shift)
        self.coins_sprites.draw(self.display_surface)

        self.fg_palms_sprites.update(self.world_shift)
        self.fg_palms_sprites.draw(self.display_surface)