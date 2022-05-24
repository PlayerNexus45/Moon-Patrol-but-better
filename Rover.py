import pygame
from pygame.sprite import Sprite
from pygame import mixer
class Rover(Sprite):
    def __init__(self, mp, pos):
        super().__init__()
        self.mp = mp
        self.screen = mp.screen
        self.screen_rect = self.screen.get_rect()
        self.image = pygame.image.load("images/carplaceholder.png")
        self.expimage = pygame.image.load("images/explosion.png")
        self.jumpsound = mixer.Sound("sounds/jump.wav")
        self.explsound = mixer.Sound("sounds/explosion.wav")
        self.rect = self.image.get_rect()
        
        self._startx, self._starty = pos
        self.rect.x, self.rect.y = pos
        self._dy = 0
        self._moving_right = False
        self._moving_left = False
        self._jumping = False
        
        self.speed = 5
        self.gravity = 1
    
    def show(self):
        self.screen.blit(self.image, self.rect)
    
    def update(self):
        self.equi()
        if self._moving_right and self.rect.x < 1135:
            self.rect.x += self.speed
        if self._moving_left and self.rect.x > 0:
            self.rect.x -= self.speed
        if self._jumping and not self._dy <-25:
            self.rect.y -= self._dy
            self._dy -= self.gravity
        if self.rect.y == self._starty:
            self._jumping = False
    
    def equi(self):
        if not self._jumping and self._moving_left is not True and self._moving_right is not True and self.rect.x != self._startx:
            if self.rect.x > self._startx:
                self.rect.x -= self.speed
            else:
                self.rect.x += self.speed

    def jump(self):
        if not self._jumping:
            self.jumpsound.play()
            self._jumping = True
            self._dy=25
    def _check_death(self, col):
        return pygame.sprite.spritecollideany(self, col)
    def _take_damage(self):
        self.image = self.expimage
        self.rect.y -= 50
        self.rect.x -= 20
        self.screen.blit(self.image, self.rect)
        self.explsound.play()