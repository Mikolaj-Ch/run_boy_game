import pygame


class Hero:
    """A class designed to handle the main character"""

    def __init__(self, hero_game):
        """Initialization hero, his start position and parameters for him"""

        self.screen = hero_game.screen
        self.setting = hero_game.setting
        self.screen_rect = hero_game.screen.get_rect()

        # Download a hero print and creating his rectangle

        self.image = pygame.image.load("images_run_boy/resize_my_hero.bmp")
        self.rect = self.image.get_rect()

        # All new hero create on center
        self.rect.midtop = self.screen_rect.center

        # Hero's  position
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        # Option that reacts to movement of hero
        self.moving_right = False
        self.moving_left = False
        self.moving_down = False
        self.moving_up = False

    def update(self):
        """Definicion for mmoving"""

        # Update value x and y for hero
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.setting.hero_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.setting.hero_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.setting.hero_speed
        if self.moving_up and self.rect.top > 0:
            self.y -= self.setting.hero_speed

        self.rect.x = self.x
        self.rect.y = self.y

    def blitme(self):
        """Shows a hero on his current location"""

        self.screen.blit(self.image, self.rect)
