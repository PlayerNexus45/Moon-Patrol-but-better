import pygame
from pygame.sprite import Sprite

class Toxic(Sprite):
    def __init__(self, mp, g_pos, x, y_off):
        super().__init__()
        self.screen = mp.screen
        self.image = pygame.image.load("images/toxicTest2.png")
        self.rect = self.image.get_rect()
        self.rect.bottom = g_pos + y_off
        self.rect.x = x
        self.speed = mp.gs.worldspeed
    def update(self):
        self.rect.x -= self.speed
        if self.rect.x <= -100:
            self.kill()
    def show(self):
        self.screen.blit(self.image, self.rect)

class Mine(Sprite):
    def __init__(self, mp, g_pos, x, y_off):
        super().__init__()
        self.screen = mp.screen
        self.image = pygame.image.load("images/mine.png")
        self.rect = self.image.get_rect()
        self.rect.bottom = g_pos + y_off
        self.rect.x = x
        self.speed = mp.gs.worldspeed
    def update(self):
        self.rect.x -= self.speed
        if self.rect.x <= -100:
            self.kill()
    def show(self):
        self.screen.blit(self.image, self.rect)

class PSA(Sprite):
    def __init__(self, mp, g_pos, x, y_off):
        super().__init__()
        self.screen = mp.screen
        self.image = pygame.image.load("images/psa.png")
        self.rect = self.image.get_rect()
        self.rect.bottom = g_pos + y_off
        self.rect.x = x
        self.speed = 6
    def update(self):
        self.rect.x -= self.speed
        if self.rect.x <= -300:
            self.kill()
    def show(self):
        self.screen.blit(self.image, self.rect)