import pygame
from snaketile import *
from constants import *

class SnakeBody(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self, self.containers)
    
    def extend(self, snake_tiles):
        for tile in snake_tiles:
            if tile.is_tail:
                x, y, direction = self.position(tile)
                tile.is_tail = False
        new_tile = SnakeTile(x, y, direction=direction)
    
    def position(self, tile):
        direction = tile.direction
        if direction == Direction.DOWN:
            return tile.x, tile.y - RECT_EDGE, direction
        elif direction == Direction.UP:
            return tile.x, tile.y + RECT_EDGE, direction
        elif direction == Direction.LEFT:
            return tile.x - RECT_EDGE, tile.y, direction
        elif direction == Direction.RIGHT:
            return tile.x + RECT_EDGE, tile.y, direction
        else:
            raise Exception("Error: unknown snake direction")