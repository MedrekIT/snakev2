import pygame
import random
from constants import *
from snaketile import SnakeTile, Direction
from apple import Apple
from snakebody import SnakeBody
from enum import Enum

class Difficulty(Enum):
    EASY = 1
    NORMAL = 2
    HARD = 3
    INSANE = 4

def mainMenu(screen, game_font):

    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                keys = pygame.key.get_pressed()
                global DIFF

                if keys[pygame.K_1]:
                    DIFF = Difficulty.EASY
                    return
                if keys[pygame.K_2]:
                    DIFF = Difficulty.NORMAL
                    return
                if keys[pygame.K_3]:
                    DIFF = Difficulty.HARD
                    return
                if keys[pygame.K_4]:
                    DIFF = Difficulty.INSANE
                    return
            if event.type == pygame.QUIT:
                exit()
        
        diffReq = game_font.render("Choose difficulty:", True, (255, 255, 255))
        reqRect = diffReq.get_rect()
        reqRect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 3)

        diff1 = game_font.render("1 - EASY", True, (255, 255, 255))
        oneRect = diffReq.get_rect()
        oneRect.center = (SCREEN_WIDTH // 2, reqRect.centery + 50)

        diff2 = game_font.render("2 - NORMAL", True, (255, 255, 255))
        twoRect = diffReq.get_rect()
        twoRect.center = (SCREEN_WIDTH // 2, reqRect.centery + 100)

        diff3 = game_font.render("3 - HARD", True, (255, 255, 255))
        threeRect = diffReq.get_rect()
        threeRect.center = (SCREEN_WIDTH // 2, reqRect.centery + 150)

        diff4 = game_font.render("4 - INSANE", True, (255, 255, 255))
        fourRect = diffReq.get_rect()
        fourRect.center = (SCREEN_WIDTH // 2, reqRect.centery + 200)

        screen.blit(diffReq, reqRect)
        screen.blit(diff1, oneRect)
        screen.blit(diff2, twoRect)
        screen.blit(diff3, threeRect)
        screen.blit(diff4, fourRect)
        pygame.display.flip()


def main():
    pygame.init()
    game_clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Snake")
    game_font = pygame.font.SysFont("timesnewroman", 30)

    mainMenu(screen, game_font)

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    snake_tiles = pygame.sprite.Group()
    SnakeBody.containers = updatable
    Apple.containers = (updatable, drawable)
    SnakeTile.containers = (drawable, snake_tiles)

    snake_body = SnakeBody()
    snake_head = SnakeTile(SCREEN_WIDTH // 2 - RECT_EDGE, SCREEN_HEIGHT // 2 - RECT_EDGE, True)

    apple_x = random.randrange(0, SCREEN_WIDTH, RECT_EDGE)
    apple_y = random.randrange(0, SCREEN_HEIGHT, RECT_EDGE)
    while apple_x == snake_head.x and apple_y == snake_head.y:
        apple_x = random.randrange(0, SCREEN_WIDTH, RECT_EDGE)
        apple_y = random.randrange(0, SCREEN_HEIGHT, RECT_EDGE)
    an_apple = Apple(apple_x, apple_y, RECT_EDGE)

    score = 1

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

        updatable.update()
        snake_head.update(snake_tiles)
        if snake_head.x < 0 or snake_head.x >= SCREEN_WIDTH or snake_head.y < 0 or snake_head.y >= SCREEN_HEIGHT:
            print("Game over!")
            exit()
        for tile in snake_tiles:
            if not tile.is_head and tile.collision(snake_head):
                print("Game over!")
                exit()
        if snake_head.collision(an_apple):
            print((2 ** len(snake_tiles)))
            score += (2 ** (len(snake_tiles) * DIFF.value)) // (score // (10 * DIFF.value))
            print((2 ** (len(snake_tiles) * DIFF.value)) // (score // (10 * DIFF.value)))
            an_apple.spawn()
            snake_body.extend(snake_tiles)
        
        if snake_head.direction != Direction.NONE:
            score += (len(snake_tiles) * DIFF.value * game_clock.get_time()) // 10
        
        screen.fill("black")
        for obj in drawable:
            obj.draw(screen)
        scoreText = game_font.render(f"Score: {score}", True, (255, 255, 255))
        scoreRect = scoreText.get_rect()
        scoreRect.center = (SCREEN_WIDTH // 2, 20)
        screen.blit(scoreText, scoreRect)
        pygame.display.flip()

        game_clock.tick(10 + ((len(snake_tiles)/2) * DIFF.value)) / 1000

if __name__ == "__main__":
    main()
