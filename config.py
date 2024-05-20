from os import path
import pygame

# Estabelece a pasta que contem as figuras e sons.
IMG_DIR = path.join(path.dirname(__file__), 'assets', 'img')
SND_DIR = path.join(path.dirname(__file__), 'assets', 'snd')
FNT_DIR = path.join(path.dirname(__file__), 'assets', 'font')

### DADOS ###
WIDTH = 1024
HEIGHT = 576
FPS = 60

### TAMANHOS ###
T_CAIXA = 64
PLAYER_WIDTH = 50
PLAYER_HEIGHT = 38

### CORES ###
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

### ESTADOS ###
INIT = 0
GAME = 1
END = 2
QUIT = 3
