import math

import pygame

from PIL import Image


import utils
from utils import scale_image


class checkpoint:

    def __init__(self, pos, angle, image, win):
        self.x = pos[0]
        self.y = pos[1]
        self.angle = angle
        self.centre_x = self.x + 45 * math.cos(math.radians(angle))
        self.centre_y = self.y + 45 * math.sin(math.radians(angle))
        self.image = scale_image(pygame.image.load(image), 0.8)
        self.rotated = pygame.transform.rotate(self.image, angle)
        self.mask = pygame.mask.from_surface(self.rotated)

    def distance_to(self, x, y):
        return math.dist((x, y), (self.centre_x, self.centre_y))
