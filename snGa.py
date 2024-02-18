import pygame
import time
import random
import numpy as np

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
    window.blit(number,[0,0]) # blit used to display a calculation at a place 

def game_snake():
    pass

def game_loop():
    gaveOver = False
    gameOver = False

#user_score(12)
# fonts = pygame.font.get_fonts()
# print(fonts)
