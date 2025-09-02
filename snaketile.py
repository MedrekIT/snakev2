from rectangleshape import *
from enum import Enum

class Direction(Enum):
    UP = 'w'
    DOWN = 's'
    LEFT = 'a'
    RIGHT = 'd'
    NONE = ''

class SnakeTile(RectangleShape):
    def __init__(self, x, y):
        super().__init__(x, y, RECT_EDGE)
        self.direction = Direction.NONE
    
    def move(self):
        if self.direction == Direction.RIGHT:
            self.x += RECT_EDGE
        if self.direction == Direction.LEFT:
            self.x -= RECT_EDGE
        if self.direction == Direction.DOWN:
            self.y += RECT_EDGE
        if self.direction == Direction.UP:
            self.y -= RECT_EDGE
    
    def turn(self, dir: Direction):
        self.direction = dir
    
    def rectangle(self):
        a = self.x - RECT_EDGE // 2
        b = self.y - RECT_EDGE // 2

        return [a, b, RECT_EDGE, RECT_EDGE]
    
    def draw(self, screen):
        pygame.draw.rect(screen, "white", self.rectangle(), 2)
        return super().draw(screen)
    
    def update(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a] and self.direction != Direction.RIGHT:
            self.turn(Direction.LEFT)
        if keys[pygame.K_d] and self.direction != Direction.LEFT:
            self.turn(Direction.RIGHT)
        if keys[pygame.K_w] and self.direction != Direction.DOWN:
            self.turn(Direction.UP)
        if keys[pygame.K_s] and self.direction != Direction.UP:
            self.turn(Direction.DOWN)

        self.move()