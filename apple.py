import random
from rectangleshape import *

class Apple(RectangleShape):
    def __init__(self, x, y, edge):
        super().__init__(x, y, edge)
        self.eaten = False
    
    def draw(self, screen):
        pygame.draw.rect(screen, "red", [self.x, self.y, RECT_EDGE, RECT_EDGE])
        return super().draw(screen)
    
    def update(self):
        if self.eaten:
            self.spawn()
        return super().update()
    
    def spawn(self):
        self.x = random.randrange(0, SCREEN_WIDTH, RECT_EDGE)
        self.y = random.randrange(0, SCREEN_HEIGHT, RECT_EDGE)
        self.eaten = False