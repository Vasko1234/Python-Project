import pygame
from game_data import levels
from support import import_folder
from decoration import Sky
from settings import graphics_color

class Node(pygame.sprite.Sprite):
    def __init__(self, position, status, icon_speed, path):
        super().__init__()
        self.frames = import_folder(path)
        self.frame_index = 0
        self.image = self.frames[self.frame_index]
        if status == "available":
            self.status = "available"
        else:
            self.status = "locked"
        self.rect = self.image.get_rect(center = position)

        self.detection_zone = pygame.Rect(self.rect.centerx - (icon_speed / 2), self.rect.centery - (icon_speed / 2), icon_speed, icon_speed)

    def animate(self):
        self.frame_index += 0.035
        if self.frame_index >= len(self.frames):
            self.frame_index = 0
        self.image = self.frames[int(self.frame_index)]

    def update(self):
        if self.status == "available":
            self.animate()
        else:
            tint_surface = self.image.copy()
            tint_surface.fill((0, 0, 0), None, pygame.BLEND_RGBA_MULT)
            self.image.blit(tint_surface, (0, 0))

class Icon(pygame.sprite.Sprite):
    def __init__(self, position):
        super().__init__()
        self.position = position
        self.image = pygame.image.load(f"Python-Project/graphics/{graphics_color}_graphics/overworld/hat.png").convert_alpha()
        self.rect = self.image.get_rect(center = position)

    def update(self):
        self.rect.center = self.position

class Overworld:
    def __init__(self, start_level, max_level, surface, create_level):
        self.display_surface = surface
        self.max_level = max_level
        self.current_level = start_level
        self.create_level = create_level

        self.moving = False
        self.move_direction = pygame.math.Vector2(0, 0)
        self.speed = 3

        self.setup_nodes()
        self.setup_icon()
        self.sky = Sky(8, "overworld")

        self.start_time = pygame.time.get_ticks()
        self.allow_input = False
        self.timer_length = 1000

    def setup_nodes(self):
        self.nodes = pygame.sprite.Group()
        
        for node_index, node_data in enumerate(levels.values()):
            if node_index <= self.max_level:
                node_sprite = Node(node_data["node_position"], "available", self.speed, node_data["node_graphics"])
            else:
                node_sprite = Node(node_data["node_position"], "locked", self.speed, node_data["node_graphics"])
            self.nodes.add(node_sprite)

    def draw_paths(self):
        if self.max_level:
            points = [node["node_position"] for node_index, node in enumerate(levels.values()) if node_index <= self.max_level]
            pygame.draw.lines(self.display_surface, "#a04f45", False, points, 6)

    def setup_icon(self):
        self.icon = pygame.sprite.GroupSingle()
        icon_sprite = Icon(self.nodes.sprites()[self.current_level].rect.center)
        self.icon.add(icon_sprite)

    def input(self):
        keys = pygame.key.get_pressed()

        if not self.moving and self.allow_input:
            if keys[pygame.K_d] and self.current_level < self.max_level:
                self.move_direction = self.get_movement_data("next")
                self.current_level += 1
                self.moving = True
            elif keys[pygame.K_a] and self.current_level:
                self.move_direction = self.get_movement_data("previous")
                self.current_level -= 1
                self.moving = True
            elif keys[pygame.K_SPACE]:
                self.create_level(self.current_level)

    def get_movement_data(self, target):
        start = pygame.math.Vector2(self.nodes.sprites()[self.current_level].rect.center)

        if target == "next":
            end = pygame.math.Vector2(self.nodes.sprites()[self.current_level + 1].rect.center)
        else:
            end = pygame.math.Vector2(self.nodes.sprites()[self.current_level - 1].rect.center)

        return (end - start).normalize()

    def update_icon_position(self):
        if self.moving and self.move_direction:
            self.icon.sprite.position += self.move_direction * self.speed
            target_node = self.nodes.sprites()[self.current_level]
            if self.move_direction.x > 0 and self.icon.sprite.position.x >= target_node.rect.centerx:
                self.icon.sprite.position.x = target_node.rect.centerx
                self.moving = False
                self.move_direction = pygame.math.Vector2(0, 0)
            elif self.move_direction.x < 0 and self.icon.sprite.position.x <= target_node.rect.centerx:
                self.icon.sprite.position.x = target_node.rect.centerx
                self.moving = False
                self.move_direction = pygame.math.Vector2(0, 0)

    def input_timer(self):
        if not self.allow_input:
            current_time = pygame.time.get_ticks()
            if current_time - self.start_time >= self.timer_length:
                self.allow_input = True

    def run(self):
        self.input_timer()
        self.input()
        self.update_icon_position()
        self.icon.update()
        self.nodes.update()

        self.sky.draw(self.display_surface)
        self.draw_paths()
        self.nodes.draw(self.display_surface)
        self.icon.draw(self.display_surface)