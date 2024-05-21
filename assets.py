import pygame
import os
from config import *

def loading():
    assets = {}
    assets['coin'] = pygame.image.load(os.path.join(IMG_DIR, 'moeda.png'))
    assets['skull'] = pygame.image.load(os.path.join(IMG_DIR, 'caveira.png'))


    assets['background'] = pygame.image.load(os.path.join(IMG_DIR, 'fundo.png'))
    assets['barreira'] = pygame.image.load(os.path.join(IMG_DIR, 'barreira.png'))
    assets['chaobase'] = pygame.image.load(os.path.join(IMG_DIR, 'chaobase.png'))

    assets['info'] = pygame.image.load(os.path.join(IMG_DIR, 'info.png'))

    
    assets['player_pistola'] = pygame.image.load(os.path.join(IMG_DIR, 'player_pistola.png'))
    assets['player_pistola'] = pygame.transform.scale(assets['player_pistola'],(64,64))
    assets['player_ak'] = pygame.image.load(os.path.join(IMG_DIR, 'player_ak.png'))
    assets['player_ak'] = pygame.transform.scale(assets['player_ak'],(64,64))
    assets['player_shotgun'] = pygame.image.load(os.path.join(IMG_DIR, 'player_shotgun.png'))
    assets['player_shotgun'] = pygame.transform.scale(assets['player_shotgun'],(64,64))

    assets['pistolatiro'] = []
    for i in range(1,4):
        img = pygame.image.load(os.path.join(IMG_DIR, f'pistolatiro{i}.png'))
        img = pygame.transform.scale(img,(64,64))
        assets['pistolatiro'].append(img)

    assets['aktiro'] = []
    for i in range(1,4):
        img = pygame.image.load(os.path.join(IMG_DIR, f'aktiro{i}.png'))
        img = pygame.transform.scale(img,(64,64))
        assets['aktiro'].append(img)

    assets['shotguntiro'] = []
    for i in range(1,4):
        img = pygame.image.load(os.path.join(IMG_DIR, f'shotguntiro{i}.png'))
        img = pygame.transform.scale(img,(64,64))
        assets['shotguntiro'].append(img)

    assets['zombie_walk'] = []
    for i in range (17):
        z = pygame.image.load(os.path.join(IMG_DIR, f'skeleton-move_{i}.png'))
        z = pygame.transform.scale(z,(64,64))
        assets['zombie_walk'].append(z)

    assets['zombie_attack'] = []
    for i in range (9):
        z = pygame.image.load(os.path.join(IMG_DIR, f'skeleton-attack_{i}.png'))
        z = pygame.transform.scale(z,(64,64))
        assets['zombie_attack'].append(z)

    return assets


def create_icons(assets):
    icons = {}

    # Ícone de moeda
    coin_icon = assets['coin']
    coin_icon = pygame.transform.scale(coin_icon, (HUD_ICON_SIZE, HUD_ICON_SIZE))
    icons['coin'] = coin_icon

    skull_icon = assets['skull']
    skull_icon = pygame.transform.scale(skull_icon, (HUD_ICON_SIZE, HUD_ICON_SIZE))
    icons['skull'] = skull_icon

    # info
    icons['info'] = assets['info']

    # Ícone para kills
    icons['kills'] = pygame.Surface((HUD_ICON_SIZE, HUD_ICON_SIZE), pygame.SRCALPHA)
    pygame.draw.circle(icons['kills'], WHITE, (HUD_ICON_SIZE // 2, HUD_ICON_SIZE // 2), HUD_ICON_SIZE // 2)
    pygame.draw.circle(icons['kills'], T_BLACK, (HUD_ICON_SIZE // 2, HUD_ICON_SIZE // 2), HUD_ICON_SIZE // 2 - 2)

    return icons
