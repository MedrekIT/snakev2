import pygame
import random
from snaketile import SnakeTile
from constants import *

class SnakeBody(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self, self.containers)

    def spawn(self, radius, position, velocity):
        pass

    def update(self, dt):
        pass