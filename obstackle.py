import pygame
from pygame.sprite import Sprite

class Toxic(Sprite):
    def __init__(self, mp, g_pos, x):
        super().__init__()
        self.screen = mp.screen
        self.image = pygame.image.load("images/toxicWaste.png")
        self.rect = self.image.get_rect()
        self.rect.bottom = g_pos + 100
        self.rect.x = x
        self.speed = 1
    def update(self):
        self.rect.x -= self.speed
        print(self.rect.x, self.rect.y)
        if self.rect.x <= -60:
            self.kill()
    def show(self):
        self.screen.blit(self.image, self.rect)