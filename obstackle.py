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
        self.speed = 4
    def update(self):
        self.rect.x -= self.speed
        if self.rect.x <= -60:
            self.kill()
    def show(self):
        self.screen.blit(self.image, self.rect)