import pygame
from game_data import levels

class Node(pygame.sprite.Sprite):
    def __init__(self, position, status):
        super().__init__()
        self.image = pygame.Surface((100, 80))
        if status == "available":
            self.image.fill((255, 0, 0))
        else:
            self.image.fill((100, 100, 100))
        self.rect = self.image.get_rect(center = position)

class Overworld:
    def __init__(self, start_level, max_level, surface):
        self.display_surface = surface
        self.max_level = max_level
        self.current_level = start_level

        self.setup_nodes()

    def setup_nodes(self):
        self.nodes = pygame.sprite.Group()
        
        for node_index, node_data in enumerate(levels.values()):
            if node_index <= self.max_level:
                node_sprite = Node(node_data["node_position"], "available")
            else:
                node_sprite = Node(node_data["node_position"], "locked")
            self.nodes.add(node_sprite)

    def draw_paths(self):
        points = [node["node_position"] for node_index, node in enumerate(levels.values()) if node_index <= self.max_level]
        pygame.draw.lines(self.display_surface, (255, 0, 0), False, points, 6)

    def run(self):
        self.draw_paths()
        self.nodes.draw(self.display_surface)