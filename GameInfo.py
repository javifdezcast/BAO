import pygame
from pygame import time


class GameInfo:
    LEVELS = 10

    def __init__(self, level=1):
        self.level = level
        self.started = False
        self.level_start_time = 0

    def next_level(self):
        self.level += 1
        self.started = False

    def reset(self):
        self.level = 1
        self.started = False
        self.level_start_time = 0

    def game_finished(self):
        return self.level > self.LEVELS

    def start_level(self):
        self.started = True
        self.level_start_time = pygame.time.get_ticks()/1000

    def get_level_time(self):
        if not self.started:
            return 0
        return round( pygame.time.get_ticks()/1000 - self.level_start_time)
