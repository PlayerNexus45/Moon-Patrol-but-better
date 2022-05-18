import pygame

class EndGame():

    def __init__(self, mp):
        self.screen = mp.screen
        self.screen_rect = mp.screen.get_rect()

        self.box_color = (167, 247, 7)

        self.rect = pygame.Rect(0, 0, 1280, 1024)
        self.rect.midtop =  self.screen_rect.midtop


    def show_endscreen (self):
        pygame.draw.rect(self.screen, self.box_color, self.rect)