#Abandon all hope ye who enter here
import pygame
from pygame.sprite import Sprite
import sys
import random
from obstackle import Toxic
class Rover:
    def __init__(self, mp, pos):
        self.screen = mp.screen
        self.screen_rect = self.screen.get_rect()
        self.image = pygame.image.load("images/car5.png")
        self.rect = self.image.get_rect()
        
        self._startx, self._starty = pos
        self.rect.x, self.rect.y = pos
        self._dy = 0
        self._moving_right = False
        self._moving_left = False
        self._jumping = False
        
        self.speed = 3
        self.gravity = 2
    
    def show(self):
        self.screen.blit(self.image, self.rect)
    
    def update(self):
        self.equi()
        if not self._jumping and self._moving_right and self.rect.x < 1024:
            self.rect.x += self.speed
        if not self._jumping and self._moving_left and self.rect.x > 0:
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
            self._jumping = True
            self._dy=25

class MoonPatrol:
    def __init__(self):
        self.clock = pygame.time.Clock()
        
        pygame.init()
        pygame.display.set_caption("Moon Patrol")
        self.toxbrl = pygame.sprite.Group()
        resolution = (1280, 1024)
        self.ground_pos = 700
        self.screen = pygame.display.set_mode(resolution)
        self.bgcolor = (20, 20, 20)
        self.sbcolor = (69, 78, 255)
        self.rover = Rover(self, (200, self.ground_pos))
        self.time_since_last_tox = 0
    
    def genToxic(self, x):
        toxic = Toxic(self, self.ground_pos, x)
        self.toxbrl.add(toxic)

    def worldgen(self):
        self.time_since_last_tox += self.dt
        if self.time_since_last_tox > random.randrange(3, 10):
            self.genToxic(random.randrange(1060, 1100))
            self.time_since_last_tox = 0
    
    def _update_screen(self):
        self.screen.fill(self.bgcolor)
        self.rover.show()
        self.rover.update()
        for tox in self.toxbrl:
            tox.show()
        self.toxbrl.update()
        self.worldgen()
        pygame.display.flip()
    
    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.rover._moving_right = True
                if event.key == pygame.K_LEFT:
                    self.rover._moving_left = True
                if event.key == pygame.K_UP:
                    self.rover.jump()
                if event.key == pygame.K_t:
                    self.genToxic(200)
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.rover._moving_right = False
                if event.key == pygame.K_LEFT:
                    self.rover._moving_left = False

    def run_game(self):
        while True:
            self.dt = self.clock.tick()

            self._check_events()
            self._update_screen()
            self.clock.tick(60)


if __name__ == "__main__":
    moon_patrol = MoonPatrol()
    moon_patrol.run_game()