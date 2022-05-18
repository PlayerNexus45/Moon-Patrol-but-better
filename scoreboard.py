import pygame.font
import pygame
class Scoreboard:
    def __init__(self, game_stats, mp):
        self.aig = mp
        self.screen = mp.screen
        self.game_stats = game_stats
        self.text_color = (167, 247, 7)
        self.font = pygame.font.SysFont(None, 48)

        self.prep_score()
    def prep_score(self):
        score_str = str(self.game_stats.points)
        self.score_image = self.font.render(score_str, True, self.text_color, None)
        self.rect = self.score_image.get_rect()
        self.rect.top = 20
        self.rect.right = self.screen.get_rect().right - 20

    def show_score(self):
        self.screen.blit(self.score_image, self.rect)