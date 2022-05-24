import pygame
import pygame.font

class EndGame():

    def __init__(self, mp):
        self.screen = mp.screen
        self.screen_rect = mp.screen.get_rect()

        self.box_color = (167, 247, 7)

        self.rect = pygame.Rect(0, 0, 1280, 1024)
        self.rect.midtop =  self.screen_rect.midtop


    def show_endscreen (self):
        pygame.draw.rect(self.screen, self.box_color, self.rect)


class FinalScore:
    def __init__(self, game_stats, mp):
        self.screen = mp.screen
        self.game_stats = game_stats
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 100)


    def prep_score(self):
        score_str = str(self.game_stats.points)
        self.score_image = self.font.render(score_str, True, self.text_color, None)
        self.rect = self.score_image.get_rect()
        self.rect.midtop = (620, 500)

    def show_fianl_score(self):
        self.prep_score()
        self.screen.blit(self.score_image, self.rect)


class GameOver:
    def __init__(self,mp):
        self.screen = mp.screen
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)


    def prep_score(self):
        game_over_str = ("GAME OVER")
        self.score_image = self.font.render(game_over_str, True, self.text_color, None)
        self.rect = self.score_image.get_rect()
        self.rect.midtop = (620, 300)

    def show_game_over(self):
        self.prep_score()
        self.screen.blit(self.score_image, self.rect)


class HighScore:
    def __init__(self,mp, game_stats):
        self.game_stats = game_stats
        self.screen = mp.screen
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)


    def prep_score(self):
        self.game_stats.setHighScore()
        game_over_str = ("High score: "+str(self.game_stats.hs))
        self.score_image = self.font.render(game_over_str, True, self.text_color, None)
        self.rect = self.score_image.get_rect()
        self.rect.midtop = (620, 350)

    def show_game_over(self):
        self.prep_score()
        self.screen.blit(self.score_image, self.rect)