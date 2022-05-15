#Abandon all hope ye who enter here
import pygame
from pygame.sprite import Sprite

import sys
import random

from obstackle import Toxic
from Rover import Rover

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
        toxic = Toxic(self, self.ground_pos, x, 73)
        self.toxbrl.add(toxic)

    def worldgen(self):
        self.time_since_last_tox += self.dt
        if self.time_since_last_tox > random.randrange(3, 10):
            self.genToxic(random.randrange(1280, 1400))
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
                # if event.key == pygame.K_t:
                #     self.genToxic(1280)
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