import pygame
from os import path
from config import *
from sprites import start_backgrownd
from assets import *

def end_screen(screen):
    clock = pygame.time.Clock()

    background = pygame.image.load(path.join(IMG_DIR, 'end.png')).convert()
    background_rect = background.get_rect()

    running = True
    while running:
        clock.tick(FPS)

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                state = QUIT
                running = False

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_s:
                    state = GAME
                    running = False

                elif event.key == pygame.K_n:
                    state = QUIT
                    running = False

        screen.fill(BLACK)
        screen.blit(background, background_rect)
        
        pygame.display.flip()

    return state