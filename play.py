import pygame
import random
from config import WIDTH, HEIGHT, INIT, GAME, END, QUIT
from start_screen import start_screen
from game_screen import game_screen
from end_screen import end_screen

pygame.init()
pygame.mixer.init()

window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('The Apocalipse')

state = INIT
while state != QUIT:
    if state == INIT:
        state = start_screen(window)
    elif state == GAME:
       state = game_screen(window)
    elif state == END:
       state = end_screen(window)
    else:
        state = QUIT

pygame.quit()

