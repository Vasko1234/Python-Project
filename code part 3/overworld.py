import pygame
from game_data import levels

class Node(pygame.sprite.Sprite):
    def __init__(self, position, status, icon_speed):
        super().__init__()
        self.image = pygame.Surface((100, 80))
        if status == "available":
            self.image.fill((255, 0, 0))
        else:
            self.image.fill((100, 100, 100))
        self.rect = self.image.get_rect(center = position)

        self.detection_zone = pygame.Rect(self.rect.centerx - (icon_speed / 2), self.rect.centery - (icon_speed / 2), icon_speed, icon_speed)

class Icon(pygame.sprite.Sprite):
    def __init__(self, position):
        super().__init__()
        self.position = position
        self.image = pygame.Surface((20, 20))
        self.image.fill((0, 0, 255))
        self.rect = self.image.get_rect(center = position)

    def update(self):
        self.rect.center = self.position

class Overworld:
    def __init__(self, start_level, max_level, surface):
        self.display_surface = surface
        self.max_level = max_level
        self.current_level = start_level

        self.moving = False
        self.move_direction = pygame.math.Vector2(0, 0)
        self.speed = 3

        self.setup_nodes()
        self.setup_icon()

    def setup_nodes(self):
        self.nodes = pygame.sprite.Group()
        
        for node_index, node_data in enumerate(levels.values()):
            if node_index <= self.max_level:
                node_sprite = Node(node_data["node_position"], "available", self.speed)
            else:
                node_sprite = Node(node_data["node_position"], "locked", self.speed)
            self.nodes.add(node_sprite)

    def draw_paths(self):
        points = [node["node_position"] for node_index, node in enumerate(levels.values()) if node_index <= self.max_level]
        pygame.draw.lines(self.display_surface, (255, 0, 0), False, points, 6)

    def setup_icon(self):
        self.icon = pygame.sprite.GroupSingle()
        icon_sprite = Icon(self.nodes.sprites()[self.current_level].rect.center)
        self.icon.add(icon_sprite)

    def input(self):
        keys = pygame.key.get_pressed()

        if not self.moving:
            if keys[pygame.K_d] and self.current_level < self.max_level:
                self.move_direction = self.get_movement_data("next")
                self.current_level += 1
                self.moving = True
            elif keys[pygame.K_a] and self.current_level:
                self.move_direction = self.get_movement_data("previous")
                self.current_level -= 1
                self.moving = True

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
            if target_node.detection_zone.collidepoint(self.icon.sprite.position):
                self.moving = False
                self.move_direction = pygame.math.Vector2(0, 0)

    def run(self):
        self.input()
        self.update_icon_position()
        self.icon.update()
        self.draw_paths()
        self.nodes.draw(self.display_surface)
        self.icon.draw(self.display_surface)