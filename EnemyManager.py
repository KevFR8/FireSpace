import pygame
import random

from Enemy import *

class EnemyManager:
    def __init__(self, res, player):
        self.res = res
        self.player = player
    
        self.sprite_group = pygame.sprite.Group()

        self.bullet_img = pygame.image.load("res/sprites/fire.png")

        # ELS = Enderman & Luihum Ship's
        # ZS = Zai's Ship
        # KS = Kev's Ship

        # Maybe in the future add more enemy idk

        self.enemy_1 = pygame.image.load("res/sprites/ELS.png")
        self.enemy_2 = pygame.image.load("res/sprites/ZS.png")
        self.enemy_3 = pygame.image.load("res/sprites/KS.png")

        self.enemy_list = [ self.enemy_1,  self.enemy_2,  self.enemy_3 ]

    def update(self):
        self.sprite_group.update()

    def draw(self, surface):
        self.sprite_group.draw(surface)

    def spawn(self, n):
        for k in range(n):
            enemy_img = random.choice(self.enemy_list)
            enemy = enemy((400, 75*k ), self.player.speed, enemy_img, self.bullet_img)
            self.sprite_group.add(enemy)
        