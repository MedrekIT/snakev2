import pygame
import os
from constants import *
from models.snaketile import SnakeTile, Direction
from models.apple import Apple
import scoring.scoring as scoring

def render_text(screen, text, pos, font=GAME_FONT, color=(240, 240, 220)):
    text_render = font.render(text, True, color)
    text_rect = text_render.get_rect()
    text_rect.center = pos
    screen.blit(text_render, text_rect)

def diff_screen(screen):
    name_font = pygame.font.SysFont("timesnewroman", 100)
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
        render_text(screen, "Snake!", (SCREEN_WIDTH // 2, 60), name_font, (180, 240, 200))
        render_text(screen, "Choose difficulty:", (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 3))
        for i, diff in enumerate(Difficulty, 1):
            render_text(screen, f"{diff.value} - {diff.name}", (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 3 + i * 50))
        pygame.display.flip()

def main_menu(screen):
    name_font = pygame.font.SysFont("timesnewroman", 100)
    while True:
        for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    keys = pygame.key.get_pressed()
                    if keys[pygame.K_SPACE]:
                        new_game(screen)
                    if keys[pygame.K_TAB]:
                        leaderboard(screen)
                    if keys[pygame.K_ESCAPE]:
                        exit()
                if event.type == pygame.QUIT:
                    exit()
        
        screen.fill((16, 23, 32))
        render_text(screen, "Snake!", (SCREEN_WIDTH // 2, 60), name_font, (180, 240, 200))
        render_text(screen, "[SPACE] - Start playing", (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 25))
        render_text(screen, "[TAB] - Leaderboard", (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 25))
        render_text(screen, "[ESC] - Leave", (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 75))
        pygame.display.flip()

def pause(screen):
    pause_font = pygame.font.SysFont("timesnewroman", 100)

    while True:
        for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    keys = pygame.key.get_pressed()
                    if keys[pygame.K_SPACE]:
                        return
                    if keys[pygame.K_ESCAPE]:
                        main_menu(screen)
                if event.type == pygame.QUIT:
                    exit()
        render_text(screen, "GAME PAUSED", (SCREEN_WIDTH // 2, 100), pause_font)
        render_text(screen, "Press [SPACE] to play!", (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        render_text(screen, "Press [ESC] to leave to main menu!", (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50))
        pygame.display.flip()

def new_game(screen):
    game_clock = pygame.time.Clock()
    DIFF = diff_screen(screen)
    score = 0

    drawable = pygame.sprite.Group()
    snake_tiles = pygame.sprite.Group()
    Apple.containers = drawable
    SnakeTile.containers = (drawable, snake_tiles)

    apple = Apple(0, 0, RECT_EDGE)
    snake_head = SnakeTile(SCREEN_WIDTH // 2 - RECT_EDGE, SCREEN_HEIGHT // 2 - RECT_EDGE, True)
    apple.update(snake_tiles)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                keys = pygame.key.get_pressed()
                if keys[pygame.K_SPACE]:
                    pause(screen)
                if keys[pygame.K_ESCAPE]:
                    pause(screen)
            if event.type == pygame.QUIT:
                exit()
        
        if apple.is_eaten:
            for tile in snake_tiles:
                if tile.is_tail:
                    tile.extend()
        apple.update(snake_tiles)
        snake_tiles.update()

        if snake_head.x < 0 or snake_head.x >= SCREEN_WIDTH or snake_head.y < 0 or snake_head.y >= SCREEN_HEIGHT:
            game_over(screen, score, DIFF)
        for tile in snake_tiles:
            if not tile.is_head and tile.collision(snake_head):
                game_over(screen, score, DIFF)
        if snake_head.collision(apple):
            score += int(((((2 ** len(snake_tiles)) * (2 ** DIFF.value)) * 0.1) // (0.1 * score)) + 0.1 * score)
            apple.is_eaten = True
        
        if snake_head.direction != Direction.NONE:
            score += ((len(snake_tiles) * DIFF.value * game_clock.get_time()) // 100)
        
        screen.fill((16, 23, 32))
        # apple.draw(screen)
        for obj in drawable:
            obj.draw(screen)
        if snake_head.direction == Direction.NONE:
            render_text(screen, f"[SPACE] - Pause", (150, SCREEN_HEIGHT // 4 * 3 - 50))
            for i, dir in enumerate(Direction):
                if dir.value:
                    render_text(screen, f"[{dir.value}] - Move {dir.name}", (150, SCREEN_HEIGHT // 4 * 3 + i * 50))
        render_text(screen, f"Score: {score}", (SCREEN_WIDTH // 2, 20))
        pygame.display.flip()

        game_clock.tick(10 + ((len(snake_tiles) // 2) * DIFF.value)) / 1000

def game_over(screen, score, diff):
    highest = False
    saved = False
    user_score = scoring.UserScore(score, diff.name)
    all_scores = scoring.AllScores()
    all_scores.get_scores_from_file()
    if all_scores.get_high_score() < score:
        high_font = pygame.font.SysFont("timesnewroman", 20)
        highest = True
    over_font = pygame.font.SysFont("timesnewroman", 70)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                keys = pygame.key.get_pressed()
                if keys[pygame.K_s] and not saved:
                    all_scores.insert_score(user_score)
                    saved = True
                if keys[pygame.K_SPACE]:
                    new_game(screen)
                if keys[pygame.K_ESCAPE]:
                    main_menu(screen)
            if event.type == pygame.QUIT:
                main_menu(screen)
        
        screen.fill((16, 23, 32))
        if highest:
            render_text(screen, "NEW HIGH SCORE!", (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 120), high_font, (240, 100, 150))
        render_text(screen, "Game over!", (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2), over_font)
        if not saved:
            render_text(screen, f"Your score: {score}, Press [S] if you want to save it!", (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 150))
        else:
            render_text(screen, f"Your score: {score}, Saved!", (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 150))
        render_text(screen, "Press [SPACE] to play again!", (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 200))
        render_text(screen, "Press [ESC] to leave to main menu!", (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 250))
        pygame.display.flip()

def leaderboard(screen):
    reset = False
    all_scores = scoring.AllScores()
    all_scores.get_scores_from_file()
    scores = all_scores.scores
    leaderboard_font = pygame.font.SysFont("timesnewroman", 70)

    while True:
        for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    keys = pygame.key.get_pressed()
                    if keys[pygame.K_BACKSPACE] and not reset:
                        all_scores.reset_scores()
                        scores = all_scores.scores
                        reset = True
                    if keys[pygame.K_SPACE]:
                        new_game(screen)
                    if keys[pygame.K_ESCAPE]:
                        main_menu(screen)
                if event.type == pygame.QUIT:
                    exit()
        
        
        screen.fill((16, 23, 32))
        render_text(screen, "Leaderboard:", (SCREEN_WIDTH // 2, 50), leaderboard_font)
        if len(scores) > 0:
            for i, score in enumerate(scores[:10], 1):
                render_text(screen, f"{i}.{score.score} - Difficulty: {score.diff}", (SCREEN_WIDTH // 2, SCREEN_HEIGHT // (len(scores[:10]) + 1) + i * 50))
            render_text(screen, "Press [SPACE] to start game!", (SCREEN_WIDTH // 2, SCREEN_HEIGHT // (len(scores[:10]) + 1) + (len(scores[:10]) + 1) * 50))
            render_text(screen, "Press [BACKSPACE] to reset scores!", (SCREEN_WIDTH // 2, SCREEN_HEIGHT // (len(scores[:10]) + 1) + (len(scores[:10]) + 1) * 50 + 40))
            render_text(screen, "Press [ESC] to leave to main menu!", (SCREEN_WIDTH // 2, SCREEN_HEIGHT // (len(scores[:10]) + 1) + (len(scores[:10]) + 1) * 50 + 80))
        else:
            render_text(screen, "There are no scores on leaderboard...", (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 25))
            render_text(screen, "Press [SPACE] to start game!", (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 25))
            render_text(screen, "Press [ESC] to leave to main menu!", (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 75))
        pygame.display.flip()

def main():
    if not os.path.isfile("./scoring/leaderboard.log"):
        try:
            with open("./scoring/leaderboard.log", "w") as f:
                pass
            f.close()
        except Exception as e:
            return f"{e}"
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Snake")

    main_menu(screen)
    

if __name__ == "__main__":
    main()
