import pygame
import time
import random

pygame.init()

# Game variables
win_width = 600
win_height = 400
snake_block = 10
snake_speed = 10
font_style = pygame.font.SysFont(None, 50)
score_font = pygame.font.SysFont(None, 35)

# Colors
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)

# Game window
window = pygame.display.set_mode((win_width, win_height))

# Function to display score
def score(score):
    value = score_font.render("Your Score: " + str(score), True, green)
    window.blit(value, [0, 0])

# Function to draw snake
def draw_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(window, white, [x[0], x[1], snake_block, snake_block])

# Function for the game loop
def game_loop():
    game_over = False
    game_close = False

    # Starting coordinates for snake
    x1 = win_width / 2
    y1 = win_height / 2

    # Variables to change coordinates
    x1_change = 0
    y1_change = 0

    # Snake length list
    snake_list = []
    snake_length = 1

    # First food coordinates
    foodx = round(random.randrange(0, win_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, win_height - snake_block) / 10.0) * 10.0

    clock = pygame.time.Clock()

    while not game_over:

        while game_close == True:
            window.fill(red)
            message = font_style.render("You Lost! Press C-Play Again or Q-Quit", True, white)
            window.blit(message, [win_width / 29, win_height / 3])
            score(snake_length - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
                game_close = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0
                elif event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0

        if x1 >= win_width or x1 < 0 or y1 >= win_height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        window.fill(green)
        pygame.draw.rect(window, red, [foodx, foody, snake_block, snake_block])
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)
        if len(snake_list) > snake_length:
            del snake_list[0]

        for x in snake_list[:-1]:
            if x == snake_head:
                game_close = True

        draw_snake(snake_block, snake_list)
        score(snake_length - 1)

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, win_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, win_height - snake_block) / 10.0) * 10.0
            snake_length += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()

game_loop()
