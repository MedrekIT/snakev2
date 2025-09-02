import pygame
import random
from constants import *
from snaketile import SnakeTile
from apple import Apple

def main():
    pygame.init()
    game_clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    snake_tiles = pygame.sprite.Group()
    Apple.containers = (updatable, drawable)
    SnakeTile.containers = (updatable, drawable, snake_tiles)

    da_snake = SnakeTile(SCREEN_WIDTH // 2 - RECT_EDGE // 2, SCREEN_HEIGHT // 2 - RECT_EDGE // 2)

    apple_x = random.randrange(0, SCREEN_WIDTH, RECT_EDGE)
    apple_y = random.randrange(0, SCREEN_HEIGHT, RECT_EDGE)
    while apple_x == da_snake.x and apple_y == da_snake.y:
        apple_x = random.randrange(0, SCREEN_WIDTH, RECT_EDGE)
        apple_y = random.randrange(0, SCREEN_HEIGHT, RECT_EDGE)
    en_apple = Apple(apple_x, apple_y, RECT_EDGE)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        updatable.update()
        screen.fill("black")
        for obj in drawable:
            obj.draw(screen)
        pygame.display.flip()
        dt = game_clock.tick(24) / 1000

if __name__ == "__main__":
    main()
