import pygame
from  pygame.locals import *
import time
import random


pygame.init() # this will start the pygame

#defining the colours for the game

red = (255,0,0)
blue = (51, 153, 255)
grey = (192, 192, 192)
green = (51, 102,0)

#Defining the game window size

win_width = 600
win_height = 400

window =pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption("Snake Game")
time.sleep(2)

snake = 10
snake_speed = 15



font_style = pygame.font.SysFont("calibri",26)
score_font = pygame.font.SysFont("comicsansms",30)

# to maintaines scores of a user
def user_score(score):
    number = score_font.render("Score :", score, True, red)
    window.blit(number,[0,0]) # blit used to display a change on screeen or calculation at a place 

def game_snake():
    pass
def message():
    msg = font_style.render(msg, True,red)
    window.blit(msg,[win_width/6, win_height/3]) # messsageand its location in the window

def game_loop():
    gaveOver = False
    gameClose = False

    x1 = win_width/2
    y1 = win_height/2

    x1_chnage = 0 # as the snake eat food its size(x and y) increases
    y1_change = 0

    snake_length_list = []
    snake_length = 1 # initial snake length

    foodx = round(random.randrange(0, win_width -snake)/10.0)*10.0 #random range will put food anywhere in the screen between 0 and width and leaving the snake
    foody = round(random.randrange(0, win_height -snake)/10.0)*10.0

    while not gameOver:
        while gameClose  == True:
            window.fill(grey)
            message("ou lost , Press P to play again and Q to quit the game")
            user_score(snake_length-1)
            pygame.display.update()

            for event in pygame.event.get


#user_score(12)
# fonts = pygame.font.get_fonts()
# print(fonts)
