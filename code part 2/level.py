import pygame
from support import import_csv_layout, import_cut_graphics
from settings import tile_size, SCREEN_HEIGHT
from tiles import Tile, StaticTile, Crate, AnimatedTile, Coin, Palm
from enemy import Enemy
from decoration import Sky, Water

class Level:
    def __init__(self, level_data, surface):
        self.display_surface = surface
        self.world_shift = -1

        player_layout = import_csv_layout(level_data["player"])
        self.player = pygame.sprite.GroupSingle()
        self.goal = pygame.sprite.GroupSingle()
        self.player_setup(player_layout)

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

        bg_palms_layout = import_csv_layout(level_data["bg_palms"])
        self.bg_palms_sprites = self.create_tile_group(bg_palms_layout, "bg_palms")

        enemies_layout = import_csv_layout(level_data["enemies"])
        self.enemies_sprites = self.create_tile_group(enemies_layout, "enemies")

        constraints_layout = import_csv_layout(level_data["constraints"])
        self.constraints_sprites = self.create_tile_group(constraints_layout, "constraints")

        self.sky = Sky(8)
        level_width = len(terrain_layout[0]) * tile_size
        self.water = Water(SCREEN_HEIGHT - 30, level_width)

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

                    if type == "bg_palms":
                        sprite = Palm(tile_size, x, y, "Python-Project/graphics/terrain/palm_bg", 64)

                    if type == "enemies":
                        sprite = Enemy(tile_size, x, y)

                    if type == "constraints":
                        sprite = Tile(tile_size, x, y)

                    sprite_group.add(sprite)

        return sprite_group
    
    def player_setup(self, layout):
        for row_index, row in enumerate(layout):
            for col_index, value in enumerate(row):
                x = col_index * tile_size
                y = row_index * tile_size
                if value == "0":
                    print("player goes here")
                if value == "1":
                    hat_surface = pygame.image.load("Python-Project/graphics/character/hat.png").convert_alpha()
                    sprite = StaticTile(tile_size, x, y, hat_surface)
                    self.goal.add(sprite)

    def enemy_collision_reverse(self):
        for enemy in self.enemies_sprites.sprites():
            if pygame.sprite.spritecollide(enemy, self.constraints_sprites, False):
                enemy.reverse()

    def run(self):

        self.sky.draw(self.display_surface)

        self.bg_palms_sprites.update(self.world_shift)
        self.bg_palms_sprites.draw(self.display_surface)

        self.terrain_sprites.update(self.world_shift)
        self.terrain_sprites.draw(self.display_surface)

        self.enemies_sprites.update(self.world_shift)
        self.constraints_sprites.update(self.world_shift)
        self.enemy_collision_reverse()
        self.enemies_sprites.draw(self.display_surface)

        self.crates_sprites.update(self.world_shift)
        self.crates_sprites.draw(self.display_surface)

        self.grass_sprites.update(self.world_shift)
        self.grass_sprites.draw(self.display_surface)

        self.coins_sprites.update(self.world_shift)
        self.coins_sprites.draw(self.display_surface)

        self.fg_palms_sprites.update(self.world_shift)
        self.fg_palms_sprites.draw(self.display_surface)

        self.goal.update(self.world_shift)
        self.goal.draw(self.display_surface)
        
        self.water.draw(self.display_surface, self.world_shift)