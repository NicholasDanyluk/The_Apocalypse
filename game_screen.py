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

    # Variáveis de controle de upgrade
    current_weapon_index = 0  # Índice da arma atual
    weapons = ['shotgun', 'ak']  # Lista de armas disponíveis
    weapon_costs = [COST_SHOTGUN, COST_AK]  # Custo de cada arma

    # Criar ícones do HUD
    icons = create_icons(assets)

    pygame.mixer.music.play(loops=-1)
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
                if event.key == pygame.K_u:
                    # Upgrade de arma
                    if current_weapon_index == 2:
                            current_weapon_index = 1
                            a = 1
                    if moedas >= weapon_costs[current_weapon_index]:
                        if a == 0:
                            moedas -= weapon_costs[current_weapon_index]
                        player.change_weapon(weapons[current_weapon_index])
                        current_weapon_index += 1
                elif event.key == pygame.K_i:
                    # Uso de moedas para recuperar parte da vida da base
                    if moedas >= COST_BARRIER:  # Custo para recuperar vida da base
                        moedas -= COST_BARRIER
                        barreira.health += 100  # Recupera 100 de vida da base
                        if barreira.health > barreira.max_health:
                            barreira.health = barreira.max_health
            # elif event.type == pygame.KEYDOWN:
            #     if event.key == pygame.K_1:
            #         player.change_weapon('pistola')
            #     elif event.key == pygame.K_2:
            #         player.change_weapon('ak')
            #     elif event.key == pygame.K_3:
            #         player.change_weapon('shotgun')
        
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

        ### HUD ###
        # Desenhar a barra de vida
        barra_vida_width_atual = int(HUD_BAR_WIDTH * (barreira.health / barreira.max_health))
        
        # Desenhar fundo da barra de vida
        pygame.draw.rect(screen, RED, 
                         [HUD_PADDING, screen.get_height() - HUD_PADDING - HUD_BAR_HEIGHT, HUD_BAR_WIDTH, HUD_BAR_HEIGHT], 
                         border_radius=HUD_BAR_BORDER_RADIUS)
        
        # Desenhar barra de vida atual
        pygame.draw.rect(screen, GREEN, 
                         [HUD_PADDING, screen.get_height() - HUD_PADDING - HUD_BAR_HEIGHT, barra_vida_width_atual, HUD_BAR_HEIGHT], 
                         border_radius=HUD_BAR_BORDER_RADIUS)
        
        # Desenhar borda da barra de vida
        pygame.draw.rect(screen, WHITE, 
                         [HUD_PADDING, screen.get_height() - HUD_PADDING - HUD_BAR_HEIGHT, HUD_BAR_WIDTH, HUD_BAR_HEIGHT], 
                         2, border_radius=HUD_BAR_BORDER_RADIUS)

        # Fonte para o contador de zombies
        fonte = pygame.font.Font(None, HUD_FONT_SIZE)

        # Desenhar o ícone de mortes
        deaths_icon = icons['skull']
        deaths_icon = pygame.transform.scale(deaths_icon, (HUD_ICON_SIZE, HUD_ICON_SIZE))
        screen.blit(deaths_icon, (HUD_PADDING, HUD_PADDING))

        # Desenhar o contador de zombies com texto
        contador_texto = fonte.render(f"{contador_zombies}", True, WHITE)
        screen.blit(contador_texto, (HUD_PADDING + HUD_ICON_SIZE + HUD_ICON_PADDING, HUD_PADDING + HUD_ICON_SIZE // 2 - fonte.get_height() // 2))

        # Desenhar ícone de moeda
        coin_icon = icons['coin']
        screen.blit(coin_icon, (HUD_PADDING + HUD_ICON_SIZE + HUD_ICON_PADDING * 2 + HUD_FONT_SIZE, HUD_PADDING))

        # Desenhar contador de moedas
        moedas_texto = fonte.render(f"{moedas}", True, WHITE)
        screen.blit(moedas_texto, (HUD_PADDING + HUD_ICON_SIZE + HUD_ICON_PADDING * 3 + HUD_FONT_SIZE + HUD_ICON_SIZE, HUD_PADDING + HUD_ICON_SIZE // 2 - fonte.get_height() // 2))

        # Desenha as informações na tela
        info = icons['info']
        info = pygame.transform.scale(info, (WIDTH, HEIGHT))
        screen.blit(info, (0, 0))


        pygame.display.update()

    return state
