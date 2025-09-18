from models.rectangleshape import *

class SnakeTile(RectangleShape):
    def __init__(self, x, y, is_head = False, direction = Direction.NONE):
        super().__init__(x, y, RECT_EDGE)
        self.direction = direction
        self.is_head = is_head
        self.is_tail = True
        self.prev = None
        self.prevPos = (None, None)
    
    def move(self):
        self.prevPos = self.x, self.y

        if self.is_head:
            if self.direction == Direction.RIGHT:
                self.x += RECT_EDGE
            elif self.direction == Direction.LEFT:
                self.x -= RECT_EDGE
            elif self.direction == Direction.DOWN:
                self.y += RECT_EDGE
            elif self.direction == Direction.UP:
                self.y -= RECT_EDGE
        else:
            self.x, self.y = self.prev.prevPos
    
    def turn(self, dir: Direction):
        self.direction = dir
    
    def draw(self, screen):
        pygame.draw.rect(screen, (180, 240, 200), [self.x + 1, self.y + 1, RECT_EDGE - 2, RECT_EDGE - 2])
        return super().draw(screen)
    
    def update(self):
        if self.is_head:
            keys = pygame.key.get_pressed()

            if keys[pygame.K_a] and self.direction != Direction.RIGHT:
                self.turn(Direction.LEFT)
            elif keys[pygame.K_d] and self.direction != Direction.LEFT:
                self.turn(Direction.RIGHT)
            elif keys[pygame.K_w] and self.direction != Direction.DOWN:
                self.turn(Direction.UP)
            elif keys[pygame.K_s] and self.direction != Direction.UP:
                self.turn(Direction.DOWN)
            
        self.move()
    
    def extend(self):
        x, y, direction = self.x, self.y, self.direction
        if direction == Direction.RIGHT:
            x -= RECT_EDGE
        elif direction == Direction.LEFT:
            x += RECT_EDGE
        elif direction == Direction.DOWN:
            y += RECT_EDGE
        elif direction == Direction.UP:
            y -= RECT_EDGE
        self.is_tail = False
        new_tile = SnakeTile(x, y)
        new_tile.prev = self