import pygame
from constants import *

# Base class for game objects
class RectangleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, edge):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.x = x
        self.y = y
        self.velocity = pygame.Vector2(0, 0)
        self.edge = edge

    def draw(self, screen):
        pass

    def update(self):
        pass