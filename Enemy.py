import pygame

from FireShip import *


class Enemy(SpaceShip):
    def __init__(self, pos, speed, img, bullet_img, ellipse, res):
        SpaceShip.__init__(self, pos, speed, img, bullet_img)