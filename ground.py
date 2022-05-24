import pygame
from gamestats import gameStats
from pygame.sprite import Sprite

class Ground(Sprite):
    def __init__ (self, mp, offset):
        super().__init__()
        self.grounds = mp.grounds
        self.gs = gameStats()
        self.screen = mp.screen
        self.ground_image = pygame.image.load("images/groundtest2.png")
        self.rect = self.ground_image.get_rect()
        self.rect.left = (self.rect.width-10 )* len(self.grounds)
        self.rect.y = mp.gs.ground_pos + offset

    def update(self):
        self.rect.x -= self.gs.worldspeed
        if self.rect.x <= -self.rect.width:
            self.kill()

    def show(self):
        self.screen.blit(self.ground_image, self.rect)
