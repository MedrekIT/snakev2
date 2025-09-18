import pygame
from constants import *
from snaketile import SnakeTile, Direction
from apple import Apple
from enum import Enum

def render_text(screen, text, pos, font=GAME_FONT, color=(240, 240, 220)):
    text_render = font.render(text, True, color)
    text_rect = text_render.get_rect()
    text_rect.center = pos
    screen.blit(text_render, text_rect)

def mainMenu(screen):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                keys = pygame.key.get_pressed()

                if keys[pygame.K_1]:
                    return Difficulty.EASY
                elif keys[pygame.K_2]:
                    return Difficulty.NORMAL
                elif keys[pygame.K_3]:
                    return Difficulty.HARD
                elif keys[pygame.K_4]:
                    return Difficulty.INSANE
            if event.type == pygame.QUIT:
                exit()
        
        screen.fill((16, 23, 32))
        name_font = pygame.font.SysFont("timesnewroman", 100)
        render_text(screen, "Snake!", (SCREEN_WIDTH // 2, 60), name_font)
        render_text(screen, "Choose difficulty:", (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 3))
        for i, diff in enumerate(Difficulty, 1):
            render_text(screen, f"{diff.value} - {diff.name}", (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 3 + i * 50))
        pygame.display.flip()

def new_game(screen):
    game_clock = pygame.time.Clock()
    DIFF = mainMenu(screen)
    score = 0

    drawable = pygame.sprite.Group()
    snake_tiles = pygame.sprite.Group()
    Apple.containers = drawable
    SnakeTile.containers = (drawable, snake_tiles)

    snake_head = SnakeTile(SCREEN_WIDTH // 2 - RECT_EDGE, SCREEN_HEIGHT // 2 - RECT_EDGE, True)
    apple = Apple(0, 0, RECT_EDGE)
    apple.update(snake_tiles)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
        
        snake_tiles.update()
        if apple.is_eaten:
            for tile in snake_tiles:
                if tile.is_tail:
                    tile.extend()
        apple.update(snake_tiles)

        if snake_head.x < 0 or snake_head.x >= SCREEN_WIDTH or snake_head.y < 0 or snake_head.y >= SCREEN_HEIGHT:
            game_over(screen, score)
        for tile in snake_tiles:
            if not tile.is_head and tile.collision(snake_head):
                game_over(screen, score)
        if snake_head.collision(apple):
            score += int(((((2 ** len(snake_tiles)) * (2 ** DIFF.value)) * 0.1) // (0.1 * score)) + 0.1 * score)
            apple.is_eaten = True
        
        if snake_head.direction != Direction.NONE:
            score += ((len(snake_tiles) * DIFF.value * game_clock.get_time()) // 100)
        
        screen.fill((16, 23, 32))
        for obj in drawable:
            obj.draw(screen)
        if snake_head.direction == Direction.NONE:
            for i, dir in enumerate(Direction):
                if dir.value:
                    render_text(screen, f"{dir.value} - Move {dir.name}", (150, SCREEN_HEIGHT // 4 * 3 + i * 50))
        render_text(screen, f"Score: {score}", (SCREEN_WIDTH // 2, 20))
        pygame.display.flip()

        game_clock.tick(10 + ((len(snake_tiles) // 2) * DIFF.value)) / 1000

def game_over(screen, score):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                keys = pygame.key.get_pressed()
                if keys[pygame.K_SPACE]:
                    new_game(screen)
                if keys[pygame.K_ESCAPE]:
                    exit()
            if event.type == pygame.QUIT:
                exit()
        
        screen.fill((16, 23, 32))
        over_font = pygame.font.SysFont("timesnewroman", 70)
        render_text(screen, "Game over!", (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2), over_font)
        render_text(screen, f"Your score: {score}", (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 150))
        render_text(screen, "Press [SPACE] to play again!", (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 200))
        render_text(screen, "Press [ESC] or close the window to leave!", (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 250))
        pygame.display.flip()

def main():
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Snake")

    new_game(screen)
    

if __name__ == "__main__":
    main()
