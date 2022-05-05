#Abandon all hope ye who enter here
import pygame
import sys
#witaj jsonie de rullo tutaj wytumacze ci troche jak gra bedzie dzialac
#
class Rover:
    def __init__(self, mp):
        self.screen = mp.screen
        self.image = pygame.image.load("placeholder.png")
        self.rect = self.image.get_rect()
    def show(self):
        self.screen.blit(self.image, self.rect)

class MoonPatrol:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Moon Patrol")
        resolution = (800, 600)
        self.screen = pygame.display.set_mode(resolution)
        self.bgcolor = (51, 51, 255)
        self.rover = Rover(self)
    def _update_screen(self):
        self.screen.fill(self.bgcolor)
        self.rover.show()

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