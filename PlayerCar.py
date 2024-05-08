import pygame

from AbstractCar import AbstractCar
from utils import scale_image

RED_CAR = scale_image(pygame.image.load("imgs/red-car.png"), 0.55)


class PlayerCar(AbstractCar):
    IMG = RED_CAR
    START_POS = (180, 200)

    def reduce_speed(self):
        self.vel = max(self.vel - self.acceleration / 2, 0)
        self.move()

    def bounce(self):
        self.vel = -self.vel
        self.move()
