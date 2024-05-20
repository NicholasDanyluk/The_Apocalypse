import random
import pygame
import os
import math
from config import *
from assets import *


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
