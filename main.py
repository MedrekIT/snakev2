import pygame
import random
from constants import *
from snaketile import SnakeTile
from apple import Apple
from snakebody import SnakeBody

def main():
    pygame.init()
    game_clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    snake_tiles = pygame.sprite.Group()
    SnakeBody.containers = updatable
    Apple.containers = (updatable, drawable)
    SnakeTile.containers = (updatable, drawable, snake_tiles)

    
    snake_body = SnakeBody()
    snake_head = SnakeTile(SCREEN_WIDTH // 2 - RECT_EDGE, SCREEN_HEIGHT // 2 - RECT_EDGE, True)

    apple_x = random.randrange(0, SCREEN_WIDTH, RECT_EDGE)
    apple_y = random.randrange(0, SCREEN_HEIGHT, RECT_EDGE)
    while apple_x == snake_head.x and apple_y == snake_head.y:
        apple_x = random.randrange(0, SCREEN_WIDTH, RECT_EDGE)
        apple_y = random.randrange(0, SCREEN_HEIGHT, RECT_EDGE)
    an_apple = Apple(apple_x, apple_y, RECT_EDGE)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        updatable.update()
        for tile in snake_tiles:
            if tile.is_head and tile.collision(an_apple):
                print("Apple eaten!")
                snake_body.extend(snake_tiles)
            if not tile.is_head and tile.collision(snake_head):
                print("Game over!")
                exit()
        screen.fill("black")
        for obj in drawable:
            obj.draw(screen)
        pygame.display.flip()
        dt = game_clock.tick(24) / 1000

if __name__ == "__main__":
    main()
