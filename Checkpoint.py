import math

import pygame

import utils
from PIL import Image


import utils
from utils import scale_image


class checkpoint:

    def __init__(self, pos, angle, car_angle, image, win):
        # Coordenadas del punto superior izquierdo del checkpoint
        self.x = pos[0]
        self.y = pos[1]
        # Angulo de la linea sobre la que se define el checkpoint
        self.angle = angle
        # Angulo que debe tener el coche al resetearse sobre este checkpoint
        self.car_angle = car_angle
        # Coordenadas del punto central del checkpoin para calcular la distancia
        # y resetear el coche a este punto
        self.centre_x = self.x + 45 * math.cos(math.radians(angle))
        self.centre_y = self.y + 45 * math.sin(math.radians(angle))
        # Imagen del checkpoint
        self.image = scale_image(pygame.image.load(image), 0.8)
        self.rotated = pygame.transform.rotate(self.image, angle)
        self.mask = pygame.mask.from_surface(self.rotated)
        self.mask.fill()

    def distance_to(self, x, y):
        return math.dist((x, y), (self.centre_x, self.centre_y))

    def draw_mask(self, win):
        surface = self.mask.to_surface()
        win.blit(surface, (self.x, self.y))

    # Detecta la colision con el checkpoint
    def collide(self, mask, x, y):
        offset = (float(self.x - x), float(self.y - y))
        poi = self.mask.overlap(mask, offset)
        return poi