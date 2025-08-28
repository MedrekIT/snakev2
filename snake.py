from rectangleshape import *

class Snake(RectangleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SNAKE_EDGE)
        self.direction = 0
    
    
    def rectangle(self):
        a = self.x - SNAKE_EDGE // 2
        b = self.y - SNAKE_EDGE // 2

        return [a, b, SNAKE_EDGE, SNAKE_EDGE]
    
    def draw(self, screen):
        pygame.draw.rect(screen, "white", self.rectangle(), 2)
        return super().draw(screen)