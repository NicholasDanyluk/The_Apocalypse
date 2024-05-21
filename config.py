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

# Coordenadas e dimensões da barra de vida
barra_vida_width = 200
barra_vida_height = 20
barra_vida_x = 20
barra_vida_y = HEIGHT - 40

# Custo de cada arma
COST_SHOTGUN = 50
COST_AK = 100
COST_BARRIER = 100

# Constantes para o HUD
HUD_PADDING = 20
HUD_FONT_SIZE = 36
HUD_BAR_WIDTH = 200
HUD_BAR_HEIGHT = 25
HUD_BAR_BORDER_RADIUS = 12
HUD_ICON_SIZE = 50
HUD_ICON_PADDING = 10
HUD_KILLS_PADDING = 10
HUD_TEXT_Y_OFFSET = 20

HUD_BACKGROUND_COLOR = (0, 0, 0, 128)  # Preto semi-transparente
HUD_BORDER_COLOR = (255, 255, 255)
HUD_HEALTH_COLOR = (0, 255, 0)
HUD_BACKGROUND_HEALTH_COLOR = (255, 0, 0)
HUD_WHITE = (255, 255, 255)
