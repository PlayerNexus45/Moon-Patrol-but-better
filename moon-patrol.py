#Abandon all hope ye who enter here
import pygame
from pygame.sprite import Sprite

import sys
import random

from obstackle import Toxic
from Rover import Rover
from ground import Ground

class MoonPatrol:
    def __init__(self):
        self.clock = pygame.time.Clock()
        
        pygame.init()
        pygame.display.set_caption("Moon Patrol")
        self.gameRunning = True
        self.allcolliders = pygame.sprite.Group()
        resolution = (1280, 1024)
        self.ground_pos = 650
        self.screen = pygame.display.set_mode(resolution)
        self.bgcolor = (20, 20, 20)
        self.sbcolor = (69, 78, 255)
        self.rover = Rover(self, (200, self.ground_pos))
        self.time_since_last_tox = 0
        self.grounds = pygame.sprite.Group()
        self.test_image = pygame.image.load("images/ground.png")
    
    def genToxic(self, x):
        toxic = Toxic(self, self.ground_pos, x, 73)
        self.allcolliders.add(toxic)

    def endGame(self):
        print("Game Over")
        self.gameRunning = False


    def worldgen(self):
        self.time_since_last_tox += self.dt
        if self.time_since_last_tox > random.randrange(3, 10):
            self.genToxic(random.randrange(1280, 1400))
            self.time_since_last_tox = 0
        if len(self.grounds) <=1:
            gd = Ground(self)
            self.grounds.add(gd)

    
    def _update_screen(self):
        self.screen.fill(self.bgcolor)
        for gd in self.grounds:
            gd.show()
        self.grounds.update()
        self.rover.show()
        self.rover.update()
        for col in self.allcolliders:
            col.show()
        self.allcolliders.update()
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
        while self.gameRunning:
            self.dt = self.clock.tick()
            if self.rover._check_death(self.allcolliders):
                self.endGame()
            self._check_events()
            self._update_screen()
            self.clock.tick(60)

if __name__ == "__main__":
    moon_patrol = MoonPatrol()
    moon_patrol.run_game()