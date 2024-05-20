import pygame
from os import path
from config import *
from sprites import start_backgrownd
from assets import *

def start_screen(screen):
    clock = pygame.time.Clock()

    sptr = pygame.sprite.Group()
    background = start_backgrownd()
    sptr.add(background)


    running = True
    while running:
        clock.tick(FPS)

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                state = QUIT
                running = False

            if event.type == pygame.KEYUP:
                state = GAME
                running = False

        sptr.update()


        screen.fill(BLACK)
        sptr.draw(screen)
        
        pygame.display.flip()

    return state