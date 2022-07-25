import pygame

from math import cos, sin, pi

from FireShip import *


class Enemy(SpaceShip):
    def __init__(self, pos, speed, img, bullet_img, ellipse, res):
        SpaceShip.__init__(self, pos, speed, img, bullet_img)

        self.res = res

        self.ellipse_origin = ellipse
        self.ellipse = self.ellipse_origin
        self.ellipse_speed = (2*pi/50) * 0.15

<<<<<<< Updated upstream
        self.time = ()
        self.clockwise = True
=======
        self.time = 0
        self.clockwise = False
>>>>>>> Stashed changes

    def increase_time(self):
        if self.clockwise:
            self.time += self.ellipse_speed
        else:
            self.time -= self.ellipse_speed
<<<<<<< Updated upstream
    
    def calculate_ellipse(self, a, b, t):
        return (self.res[0]/2 + a*cos(t), self.res[1]/2 + b*sin(t))
    
=======

    def calculate_ellipse(self, a, b, t):
        return (self.res[0]/2 + a*cos(t), self.res[1]/2 + b*sin(t))

>>>>>>> Stashed changes
    def pre_update(self, player):
        direction = pygame.math.Vector2(self.pos[0] - player.pos[0], self.pos[1] - player.pos[1])
        angle = direction.angle_to(pygame.math.Vector2(0, -1))

        self.rotation = angle

        self.increase_time()
<<<<<<< Updated upstream
        self.pos = self.calculate_ellipse(self.ellipse[0], self.ellipse[1], self.time) 


=======
        self.pos = self.calculate_ellipse(self.ellipse[0], self.ellipse[1], self.time)
>>>>>>> Stashed changes
