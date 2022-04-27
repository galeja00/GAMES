import pygame
import pygame.freetype
import random
import sys

from config import config


def update_position(position, direction, speed):
    if direction == "UP":
        position = [position[0], position[1] - speed]
    if direction == "DOWN":
        position = [position[0], position[1] + speed]
    if direction == "LEFT":
        position = [position[0] - speed, position[1]]
    if direction == "RIGHT":
        position = [position[0] + speed, position[1]]
    return position

def update_direction(direction, key):
    if key[pygame.K_LEFT] or key[pygame.K_a]:
        return "LEFT" if direction != "RIGHT" else direction
    if key[pygame.K_RIGHT] or key[pygame.K_d]:
        return "RIGHT" if direction != "LEFT" else direction
    if key[pygame.K_UP] or key[pygame.K_w]:
        return "UP" if direction != "DOWN" else direction
    if key[pygame.K_DOWN] or key[pygame.K_s]:
        return "DOWN" if direction != "UP" else direction
    return direction

def is_out(position, field):
    if position[0] > field[0] or position[1] > field[1] or position[0] < 0 or position[1] < 0:
        return True
    return False

def end_game(window, score):
    print("YOU ARE NOOB", end="\n")
    print("SCORE:", score, end="\n")
    for i in range(10):
        print("-", end=" ")
    print("\n")
    print("GAME OVER")
    window.fill(config.BACK_GROUND_COLOR)
    pygame.quit()
    sys.exit()

def generate_apple(game_res, size):
    lst_x = []
    lst_y = []
    n = size
    while n < game_res[0] - 11:
        lst_x.append(n)
        n += size
    n = size
    while n < game_res[1] - 11:
        lst_y.append(n)
        n += size
    x = random.choice(lst_x)
    y = random.choice(lst_y)
    return [x, y]


def body_colizion(snake, snake_head):
    for i in range(1, len(snake)):
        if snake_head == snake[i]:
            return True
   
    

    



    