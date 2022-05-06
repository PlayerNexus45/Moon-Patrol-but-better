#Abandon all hope ye who enter here
import pygame
import sys
class Rover:
    def __init__(self, mp, pos):
        self.screen = mp.screen
        self.screen_rect = self.screen.get_rect()
        self.image = pygame.image.load("images/car5.png")
        self.rect = self.image.get_rect()
        self._startx, self._starty = pos
        self.rect.x = self._startx
        self.rect.y = self._starty
        self._dy = 5
        self._moving_right = False
        self._moving_left = False
        self._jumping = False
        self.speed = 1
    def show(self):
        self.screen.blit(self.image, self.rect)
    def update(self):
        if not self._jumping:
            self.equi()
            if self._moving_right and self.rect.x < 1024:
                self.rect.x += self.speed
            if self._moving_left and self.rect.x > 0:
                self.rect.x -= self.speed
        else:
            if self._dy >= -10:
                self.rect.y -= (self._dy * abs(self._dy)) * 0.5
            else: 
                self._dy = 10
                self._jumping = False
        if self.rect.y < self._starty:
            self.rect.y += 1

    def equi(self):
        if self._moving_left is not True and self._moving_right is not True and self.rect.x != self._startx:
            if self.rect.x > self._startx:
                self.rect.x -= self.speed
            else:
                self.rect.x += self.speed

    

class MoonPatrol:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Moon Patrol")
        resolution = (1280, 1024)
        self.screen = pygame.display.set_mode(resolution)
        self.bgcolor = (20, 20, 20)
        self.sbcolor = (69, 78, 255)
        self.rover = Rover(self, (200, 700))
    def _update_screen(self):
        self.screen.fill(self.bgcolor)
        self.rover.show()
        self.rover.update()

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
                    self.rover._jumping = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.rover._moving_right = False
                if event.key == pygame.K_LEFT:
                    self.rover._moving_left = False

    def run_game(self):
        while True:
            self._check_events()
            self._update_screen()


if __name__ == "__main__":
    moon_patrol = MoonPatrol()
    moon_patrol.run_game()