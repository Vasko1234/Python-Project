import pygame
from support import import_folder

class Player(pygame.sprite.Sprite):
    def __init__(self, position):
        super().__init__()
        self.image = pygame.Surface((32, 64))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect(topleft = position)
        
        self.direction = pygame.math.Vector2(0, 0)
        self.speed = 2
        self.gravity = 0.08
        self.jump_speed = -4

    def import_character_assets(self):
        character_path = "../graphics/character/"
        self.animations = {"idle": [], "run": [], "jump": [], "fall": []}

        for animation in self.animations.keys():
            full_path = character_path + animation
            self.animations[animation] = import_folder(full_path)

    def get_input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.direction.x = 1
        elif keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.direction.x = -1
        else:
            self.direction.x = 0

        if keys[pygame.K_SPACE] or keys[pygame.K_w]:
            self.jump()

    def apply_gravity(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y

    def jump(self):
        self.direction.y = self.jump_speed

    def update(self):
        self.get_input()