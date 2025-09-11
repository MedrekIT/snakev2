from rectangleshape import *
from enum import Enum

class Direction(Enum):
    UP = 'w'
    DOWN = 's'
    LEFT = 'a'
    RIGHT = 'd'
    NONE = ''

class SnakeTile(RectangleShape):
    def __init__(self, x, y, is_head = False, direction = Direction.NONE):
        super().__init__(x, y, RECT_EDGE)
        self.direction = direction
        self.is_head = is_head
        self.is_tail = True
    
    def move(self, snake_tiles):
        prev_x = self.x
        prev_y = self.y
        if self.direction == Direction.RIGHT:
            self.x += RECT_EDGE
        if self.direction == Direction.LEFT:
            self.x -= RECT_EDGE
        if self.direction == Direction.DOWN:
            self.y += RECT_EDGE
        if self.direction == Direction.UP:
            self.y -= RECT_EDGE
        
        for tile in snake_tiles:
            if not tile.is_head:
                tile.x, prev_x = prev_x, tile.x
                tile.y, prev_y = prev_y, tile.y
    
    def turn(self, dir: Direction):
        self.direction = dir
    
    def draw(self, screen):
        pygame.draw.rect(screen, "white", [self.x, self.y, RECT_EDGE, RECT_EDGE], 2)
        return super().draw(screen)
    
    def update(self, snake_tiles):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a] and self.direction != Direction.RIGHT:
                self.turn(Direction.LEFT)
        elif keys[pygame.K_d] and self.direction != Direction.LEFT:
                self.turn(Direction.RIGHT)
        elif keys[pygame.K_w] and self.direction != Direction.DOWN:
                self.turn(Direction.UP)
        elif keys[pygame.K_s] and self.direction != Direction.UP:
                self.turn(Direction.DOWN)
        
        self.move(snake_tiles)