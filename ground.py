import pygame
from pygame.sprite import Sprite

class Ground(Sprite):
    def __init__ (self, mp):
        super().__init__()
        self.grounds = mp.grounds
        self.screen = mp.screen
        self.ground_image = pygame.image.load("images/ground.png")
        self.rect = self.ground_image.get_rect()
        self.rect.left = (self.rect.width-5 )* len(self.grounds)
        self.rect.y = 700

    def update(self):
        self.rect.x -= 4
        if self.rect.x <= -self.rect.width:
            self.kill()

    def show(self):
        self.screen.blit(self.ground_image, self.rect)
