import random
from rectangleshape import *

class Apple(RectangleShape):
    def __init__(self, x, y, edge):
        super().__init__(x, y, edge)
        self.is_eaten = True
    
    def draw(self, screen):
        pygame.draw.rect(screen, (200, 70, 70), [self.x + 1, self.y + 1, RECT_EDGE - 2, RECT_EDGE - 2])
        return super().draw(screen)
    
    def update(self, snake_tiles):
        if self.is_eaten:
            self.x, self.y = self.check_squares(snake_tiles)
            self.is_eaten = False
        return super().update()
    
    def check_squares(self, snake_tiles):
        x = random.randrange(0, SCREEN_WIDTH, RECT_EDGE)
        y = random.randrange(0, SCREEN_HEIGHT, RECT_EDGE)
        
        for tile in snake_tiles:
            occupied_tiles = []
            occupied_tiles.append((tile.x, tile.y))

        while (x, y) in occupied_tiles:
            x = random.randrange(0, SCREEN_WIDTH, RECT_EDGE)
            y = random.randrange(0, SCREEN_HEIGHT, RECT_EDGE)
        
        return x, y