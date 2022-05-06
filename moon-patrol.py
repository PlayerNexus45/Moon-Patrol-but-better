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
        self._dx, self._dy = 0, 0
    def show(self):
        self.screen.blit(self.image, self.rect)
    def update(self):
        self.rect.y += self._dy
        self.rect.x += self._dx
        if self.rect.y < 0:
            self.rect.y = 0
    def foward(self):
        if self.rect.x < 1024:
            self._dx +=3
    

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
    def run_game(self):
        while True:
            self._check_events()
            self._update_screen()


if __name__ == "__main__":
    moon_patrol = MoonPatrol()
    moon_patrol.run_game()