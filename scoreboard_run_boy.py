import pygame.font


class ScoreBoard:
    """Class for shoving and menagment information about score"""

    def __init__(self, hero_game):
        """Class intended for scoring"""

        self.screen = hero_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = hero_game.setting
        self.stats = hero_game.stats
        self.hero_game = hero_game

        # Settings for font
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        # First screen with score
        self.prep_score()

    def prep_score(self):
        """Converting score to print"""
        if self.hero_game.stats.game_active == False:
            self.font = pygame.font.SysFont(None, 120)
        else:
            self.font = pygame.font.SysFont(None, 48)

        rounded_score = round(self.hero_game.stats.time, 1)
        score_str = "{:,}".format(rounded_score)
        self.score_image = self.font.render(
            score_str, True, self.text_color, self.settings.background_color
        )

        # Shoving score on right top
        self.score_rect = self.score_image.get_rect()
        self.score_rect_two = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def show_score(self):
        """Shoving score on screen"""

        self.screen.blit(self.score_image, self.score_rect)
