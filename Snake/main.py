import pygame
import sys
import pygame.freetype

from config import config 
from my_librery import func


if __name__ == "__main__":
    pygame.init()
    pygame.display.set_caption('Snake')

    clock = pygame.time.Clock()
    window = pygame.display.set_mode(config.RESOLUTION)
    snake = [[config.RESOLUTION[0] // 2, config.RESOLUTION[1] // 2]]
    apple = func.generate_apple(config.RESOLUTION, config.SNAKE_PART_SIZE)
    gold_apple = None
    direction = "UP"
    score = 0
    number_of_red_apples = 0 
    speed = config.SNAKE_PART_SIZE
    font_small = pygame.font.SysFont("comicsans", 15)
    font_big = pygame.font.SysFont("comicsans", 30)
    ganerated = "NO"
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        key = pygame.key.get_pressed()
        direction = func.update_direction(direction, key)
        snake_new_position = func.update_position(snake[0], direction, speed)
        snake.insert(0, snake_new_position)
        score_text = font_small.render(f"Score: {score}", True, (255, 255, 255))
        gold_apple_text = font_big.render("GOLD APPLE", True, (204, 153, 0))
        game_over_text = font_big.render(f"GAME OVER", True, (255, 0, 0)) 
        
        if apple == snake[0] or gold_apple == snake[0]:
            if apple == snake[0]:
                score += 1
                number_of_red_apples += 1
                print("+1")
                apple = func.generate_apple(config.RESOLUTION, config.SNAKE_PART_SIZE)
            else:
                score += 3
                print("+3")
                gold_apple = None
                generated = "NO"
                if len(snake) > config.POWER_OF_GOLDEN_APPPLE + 1:
                    for i in range(config.POWER_OF_GOLDEN_APPPLE):
                        snake.pop()
        else:
            snake.pop()

        if number_of_red_apples % config.GOLDEN_APPLE_SPOWN == 0 and ganerated == "NO":
            if number_of_red_apples > 1:
                print("GOLDEN APPLE")
                gold_apple = func.generate_apple(config.RESOLUTION, config.SNAKE_PART_SIZE)
                ganerated = "YES"

        if func.is_out(snake[0], config.RESOLUTION) or func.body_colizion(snake, snake_new_position):
            func.end_game(window, score)

        for part in snake:
            pygame.draw.rect(window, config.BODY_COLOR, pygame.Rect(part[0], part[1], config.SNAKE_PART_SIZE, config.SNAKE_PART_SIZE))
        pygame.draw.rect(window, config.APPLE_COLOR, pygame.Rect(apple[0], apple[1], config.SNAKE_PART_SIZE, config.SNAKE_PART_SIZE))

        if gold_apple is not None:
            pygame.draw.rect(window, config.GOLD_APPLE_COLOR, pygame.Rect(gold_apple[0], gold_apple[1], config.SNAKE_PART_SIZE, config.SNAKE_PART_SIZE))

        window.blit(score_text, (0, 0))
        pygame.display.update()
        window.fill(config.BACK_GROUND_COLOR)
        clock.tick(config.FPS)