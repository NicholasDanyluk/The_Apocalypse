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

    ### zombies ###
    zombies = pygame.sprite.Group()
    contador_zombies = 0
    moedas = 0
    tempo_passado = 0
    tempo_novo_zombie = 0 
    frequencia_zombie = 1500

    # pygame.mixer.music.play(loops=-1)
    while state == GAME:
        clock.tick(FPS)
        tempo_passado += clock.get_time()
        tempo_novo_zombie += clock.get_time()

        # Verificar colisões entre balas e zombies
        hits = pygame.sprite.groupcollide(player.balas, zombies, True, True)
        for bullet, zombie in hits.items():
            for z in zombie:
                z.die()
                contador_zombies += 1
                moedas += 1

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
        
        if tempo_novo_zombie > frequencia_zombie:
            novo_zombie = Zombie(barreira, assets)
            zombies.add(novo_zombie)
            all_sprites.add(novo_zombie)
            tempo_novo_zombie = 0  # Reinicia o contador de tempo para o próximo zombie

            frequencia_zombie -= 20  # Reduzir o tempo entre zombies
            if frequencia_zombie < -1000:
                frequencia_zombie = 700

        all_sprites.update()
        player.balas.update()
        
        ### saidas ###
        screen.fill(BLACK)
        screen.blit(assets['background'], (0, 0))
        all_sprites.draw(screen)
        player.balas.draw(screen)

        pygame.display.update()

    return state
