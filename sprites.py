import random
import pygame
import os
import math
from config import *
from assets import *

BARREIRA_ZERO_HEALTH = pygame.USEREVENT + 1

class start_backgrownd(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        ### load images
        self.start_back = []
        for i in range(1, 9):
            image_path = os.path.join(IMG_DIR, f'start{i}.png')
            back_image = pygame.image.load(image_path).convert()
            self.start_back.append(back_image)
        
        self.i = 0
        self.image = self.start_back[self.i]
        self.rect = self.image.get_rect()
        self.rect.topleft = (0, 0)
        self.loop = True
    
    def update(self):
        if self.i > 7:
            self.loop = False
        elif self.i < 0:
            self.loop = True
        if self.loop == True:
            self.i += 0.4
        elif self.loop == False:
            self.i -= 0.4
        self.image = self.start_back[int(self.i)]

class ChaoBase(pygame.sprite.Sprite):
    def __init__(self, assets):
        pygame.sprite.Sprite.__init__(self)
        self.image = assets['chaobase']
        self.image = pygame.transform.scale(self.image,(T_CAIXA,HEIGHT))
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = WIDTH - T_CAIXA
        self.rect.y = 0

class Barreira(pygame.sprite.Sprite):
    def __init__(self, assets):
        pygame.sprite.Sprite.__init__(self)
        self.image = assets['barreira']
        self.image = pygame.transform.scale(self.image,(T_CAIXA,HEIGHT))
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = WIDTH - 2*T_CAIXA
        self.rect.y = 0
        self.health = 1500
        self.max_health = 1500

    def update(self):
        if self.health <= 0:
            pygame.event.post(pygame.event.Event(BARREIRA_ZERO_HEALTH))
            # pygame.event.post(pygame.event.Event(pygame.QUIT))



class Balas(pygame.sprite.Sprite):
    def __init__(self, angle, assets):
        self.assets = assets
        pos = (982,275)
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((10, 10), pygame.SRCALPHA)
        pygame.draw.circle(self.image, (0, 0, 0), (5, 5), 5)
        self.rect = self.image.get_rect(center=pos)
        self.speed = 10
        self.angle = math.radians(angle)
        self.velocity = pygame.math.Vector2(self.speed * math.cos(self.angle), -self.speed * math.sin(self.angle))
        self.assets['tirosnd'].play()

    def update(self):
        self.rect.x += self.velocity.x
        self.rect.y += self.velocity.y

class Jogador(pygame.sprite.Sprite):
    def __init__(self, assets):
        pygame.sprite.Sprite.__init__(self)
        self.assets = assets
        self.current_weapon = 'pistola'
        self.original_image = assets['player_pistola']
        self.image = self.original_image
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH - 32
        self.rect.bottom = HEIGHT / 2 + 32

        # Carregar as imagens da animação de tiro
        self.shoot_images = assets['pistolatiro']
        self.shoot_index = 0
        self.shooting = False
        self.shoot_timer = 0
        self.shoot_delay = 200

        # Lista de balas
        self.balas = pygame.sprite.Group()

    def update(self):
        # Calcular a posição do mouse
        mouse_x, mouse_y = pygame.mouse.get_pos()

        # Calcular o ângulo entre o jogador e o mouse
        rel_x, rel_y = mouse_x - self.rect.centerx, mouse_y - self.rect.centery
        angle = (180 / math.pi) * -math.atan2(rel_y, rel_x)

        # Atualizar a imagem do jogador
        if self.shooting:
            self.handle_shooting(angle)
        else:
            self.image = pygame.transform.rotate(self.original_image, angle)
            self.rect = self.image.get_rect(center=self.rect.center)

        # Verificar cliques do mouse
        self.handle_mouse_input(angle)

        # Atualizar as balas
        self.balas.update()

    def handle_mouse_input(self, angle):
        mouse_buttons = pygame.mouse.get_pressed()
        if mouse_buttons[0]:  # Clique com o botão esquerdo do mouse
            self.start_shooting(angle)

    def start_shooting(self, angle):
        if not self.shooting:
            self.shooting = True
            self.shoot_index = 0
            self.shoot_timer = pygame.time.get_ticks()
            # Disparar uma bala
            self.shoot_bullet(angle)

    def handle_shooting(self, angle):
        now = pygame.time.get_ticks()
        if now - self.shoot_timer >= self.shoot_delay:
            self.shoot_timer = now
            self.shoot_index += 1
            if self.shoot_index >= len(self.shoot_images):
                self.shooting = False
                self.image = pygame.transform.rotate(self.original_image, angle)
            else:
                self.image = pygame.transform.rotate(self.shoot_images[self.shoot_index], angle)
            self.rect = self.image.get_rect(center=self.rect.center)

    def shoot_bullet(self, angle):
        bullet = Balas(angle, self.assets)
        self.balas.add(bullet)

    def change_weapon(self, new_weapon):
        if f'player_{new_weapon}' in self.assets:
            self.current_weapon = new_weapon
            self.original_image = self.assets[f'player_{new_weapon}']
            self.shoot_images = self.assets[f'{new_weapon}tiro']
            self.image = self.original_image
            self.mask = pygame.mask.from_surface(self.image)
            self.rect = self.image.get_rect(center=self.rect.center)

            if new_weapon == 'ak':
                self.shoot_delay = 50
            elif new_weapon == 'pistola':
                self.shoot_delay = 200
            elif new_weapon == 'shotgun':
                self.shoot_delay = 120

class Zombie(pygame.sprite.Sprite):
    def __init__(self, barreira, assets):
        pygame.sprite.Sprite.__init__(self)
        self.assets = assets
        self.i = 0
        self.image = self.assets["zombie_walk"][self.i]  # Use a primeira imagem como padrão
        self.rect = self.image.get_rect()
        self.rect.x = -64  # Spawn do lado esquerdo do mapa
        self.rect.y = random.randint(0, 576-64)  # Posição vertical aleatória
        self.speed = 4  # Velocidade de movimento do zombie
        self.barreira = barreira  # Barreira que o zombie irá atacar
        self.state = "walking"  # Estado inicial do zombie

    def update(self):
        if self.state == "walking":
            # Movimento em direção à barreira
            if self.rect.x < self.barreira.rect.x:
                self.rect.x += self.speed

            # Atualizar a animação de caminhada
            self.animate("zombie_walk", 17)

            # Verificar se o zombie atingiu a barreira
            if pygame.sprite.collide_rect(self, self.barreira):
                self.state = "attacking"  # Mudar para o estado de ataque

        elif self.state == "attacking":
            # Atualizar a animação de ataque
            self.animate("zombie_attack", 9)

            # Reduzir a vida da barreira enquanto o zombie ataca
            self.barreira.health -= 1

            # Verificar se a vida da barreira chegou a zero
            if self.barreira.health <= 0:
                self.barreira.health = 0  # Garantir que a vida da barreira não seja negativa
                self.state = "walking"  # Mudar de volta para o estado de caminhada

    def animate(self, anim_name, num_frames):
        # Alternar entre as imagens da animação
        self.i = (self.i + 0.2) % num_frames
        self.image = self.assets[anim_name][int(self.i)]

    def die(self):
        self.kill()
