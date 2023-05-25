from settings import vertical_tile_number, tile_size, SCREEN_WIDTH, graphics
import pygame
from tiles import AnimatedTile, StaticTile
from support import import_folder
from random import choice, randint

class Sky:
    def __init__(self, horizon, style = "level"):
        self.top = pygame.image.load(f"Python-Project/graphics/{graphics}/decoration/sky/sky_top.png").convert_alpha()
        self.middle = pygame.image.load(f"Python-Project/graphics/{graphics}/decoration/sky/sky_middle.png").convert_alpha()
        self.bottom = pygame.image.load(f"Python-Project/graphics/{graphics}/decoration/sky/sky_bottom.png").convert_alpha()
        self.horizon = horizon

        self.top = pygame.transform.scale(self.top, (SCREEN_WIDTH, tile_size))
        self.middle = pygame.transform.scale(self.middle, (SCREEN_WIDTH, tile_size))
        self.bottom = pygame.transform.scale(self.bottom, (SCREEN_WIDTH, tile_size))

        self.style = style
        if self.style == "overworld":
            palm_surfaces = import_folder(f"Python-Project/graphics/{graphics}/overworld/palms")
            self.palms = []

            for surface in [choice(palm_surfaces) for image in range(10)]:
                x = randint(0, SCREEN_WIDTH)
                y = (self.horizon * tile_size) + randint(50, 100)
                rect = surface.get_rect(midbottom = (x, y))
                self.palms.append((surface, rect))

            cloud_surfaces = import_folder(f"Python-Project/graphics/{graphics}/overworld/clouds")
            self.clouds = []

            for surface in [choice(cloud_surfaces) for image in range(10)]:
                x = randint(0, SCREEN_WIDTH)
                y = randint(0, (self.horizon * tile_size) - 100)
                rect = surface.get_rect(midbottom = (x, y))
                self.clouds.append((surface, rect))

    def draw(self, surface):
        for row in range(vertical_tile_number):
            y = row * tile_size
            if row < self.horizon:
                surface.blit(self.top, (0, y))
            elif row == self.horizon:
                surface.blit(self.middle, (0, y))
            else:
                surface.blit(self.bottom, (0, y))

        if self.style == "overworld":
            for palm in self.palms:
                surface.blit(palm[0], palm[1])
            for cloud in self.clouds:
                surface.blit(cloud[0], cloud[1])

class Water:
    def __init__(self, top, level_width):
        water_start = -SCREEN_WIDTH
        water_tile_width = 192
        tile_x_amount = int((level_width + SCREEN_WIDTH * 2) / water_tile_width)
        self.water_sprites = pygame.sprite.Group()

        for tile in range(tile_x_amount):
            x = tile * water_tile_width + water_start
            y = top
            sprite = AnimatedTile(192, x, y, f"Python-Project/graphics/{graphics}/decoration/water")
            self.water_sprites.add(sprite)

    def draw(self, surface, shift):
        self.water_sprites.update(shift)
        self.water_sprites.draw(surface)

class Clouds:
    def __init__(self, horizon, level_width, cloud_number):
        cloud_surface_list = import_folder(f"Python-Project/graphics/{graphics}/decoration/clouds")
        min_x = -SCREEN_WIDTH
        max_x = level_width + SCREEN_WIDTH
        min_y = 0
        max_y = horizon
        self.cloud_sprites = pygame.sprite.Group()

        for cloud in range(cloud_number):
            cloud = choice(cloud_surface_list)
            x = randint(min_x, max_x)
            y = randint(min_y, max_y)
            sprite = StaticTile(0, x, y, cloud)
            self.cloud_sprites.add(sprite)

    def draw(self, surface, shift):
        self.cloud_sprites.update(shift)
        self.cloud_sprites.draw(surface)