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
    direction = "UP"
    score = 0 
    speed = config.SNAKE_PART_SIZE
    font = pygame.font.SysFont("comicsans", 15)


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        key = pygame.key.get_pressed()
        direction = func.update_direction(direction, key)
        snake_new_position = func.update_position(snake[0], direction, speed)
        snake.insert(0, snake_new_position)
        score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    
        if apple == snake[0]:
            score += 1
            print("+1")
            apple = func.generate_apple(config.RESOLUTION, config.SNAKE_PART_SIZE)
        else:
            snake.pop()

        if func.is_out(snake[0], config.RESOLUTION) or func.body_colizion(snake, snake_new_position):
            func.end_game(window, score)

        for fuck in snake:
            pygame.draw.rect(window, config.BODY_COLOR, pygame.Rect(fuck[0], fuck[1], config.SNAKE_PART_SIZE, config.SNAKE_PART_SIZE))
        pygame.draw.rect(window, config.APPLE_COLOR, pygame.Rect(apple[0], apple[1], config.SNAKE_PART_SIZE, config.SNAKE_PART_SIZE))
        window.blit(score_text, (0, 0))
        pygame.display.update()
        window.fill(config.BACK_GROUND_COLOR)
        clock.tick(config.FPS)