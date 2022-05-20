#Abandon all hope ye who enter here
import pygame
from pygame.sprite import Sprite

import sys
import random

from obstackle import Toxic
from Rover import Rover
from ground import Ground
from gamestats import gameStats
from scoreboard import Scoreboard
from endgame import EndGame, FinalScore, GameOver , HighScore

class MoonPatrol:
    def __init__(self):
        self.clock = pygame.time.Clock()
        
        pygame.init()
        pygame.display.set_caption("Moon Patrol")
        self.gameRunning = True
        self.allcolliders = pygame.sprite.Group()
        resolution = (1280, 1024)
        self.screen = pygame.display.set_mode(resolution)
        self.delay = 20
        self.gs = gameStats()
        self.sc = Scoreboard(self.gs, self)
        self.end = EndGame(self)
        self.final = FinalScore(self.gs,self)
        self.over = GameOver(self)
        self.high = HighScore(self, self.gs)
        
        self.bgcolor = (20, 20, 20)
        self.sbcolor = (69, 78, 255)
        self.rover = Rover(self, (200, self.gs.ground_pos))
        self.time_since_last_tox = 0
        self.grounds = pygame.sprite.Group()
        self.test_image = pygame.image.load("images/ground.png")
    
    def genToxic(self, x):
        toxic = Toxic(self, self.gs.ground_pos, x, 60)
        self.allcolliders.add(toxic)





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
        if self.delay == 0:
            self.gs.addPoints()
            self.sc.prep_score()
            self.delay = 20
        else:
            self.delay -= 1
        self.sc.show_score()
        if self.rover._check_death(self.allcolliders):
            self.end.show_endscreen()
            self.final.show_fianl_score()
            self.over.show_game_over()
            self.high.show_game_over()
            pygame.time.delay(1000)
            pygame.display.flip()
            pygame.time.delay(5000)
            sys.exit()
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
            self._check_events()
            self._update_screen()

            self.clock.tick(60)

if __name__ == "__main__":
    moon_patrol = MoonPatrol()
    moon_patrol.run_game()