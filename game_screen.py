import pygame
from config import *
from assets import *
from sprites import *

def game_screen(screen):
    state = GAME
    a = 0
    clock = pygame.time.Clock()
    assets = loading()

    all_sprites = pygame.sprite.Group()

    ### base ###
    chaobase = ChaoBase(assets)
    barreira = Barreira(assets)
    all_sprites.add(chaobase)
    all_sprites.add(barreira)

    ### player ###
    player = Jogador(assets)
    all_sprites.add(player)

    # pygame.mixer.music.play(loops=-1)
    while state == GAME:
        clock.tick(FPS)

        for event in pygame.event.get():
            # ----- Verifica consequências
            if event.type == pygame.QUIT:
                state = QUIT
            elif event.type == BARREIRA_ZERO_HEALTH:
                state = END
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    player.change_weapon('pistola')
                elif event.key == pygame.K_2:
                    player.change_weapon('ak')
                elif event.key == pygame.K_3:
                    player.change_weapon('shotgun')
        
        all_sprites.update()
        player.balas.update()
        
        ### saidas ###
        screen.fill(BLACK)
        screen.blit(assets['background'], (0, 0))
        all_sprites.draw(screen)
        player.balas.draw(screen)

        pygame.display.update()

    return state
