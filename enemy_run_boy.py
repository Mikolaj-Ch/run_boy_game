import pygame
import random

from pygame.sprite import Sprite


class Enemy(Sprite):
    """Class attendant single enemy"""

    def __init__(self, hero_game):
        """Initialization of the enemy and his position"""

        super().__init__()

        self.setting = hero_game.setting
        self.screen = hero_game.screen
        self.hero_game = hero_game
        self.screen_rect = hero_game.screen.get_rect()

        self.rect_hero_x = hero_game.hero.rect.x
        self.rect_hero_y = hero_game.hero.rect.y

        # Download image
        self.image = pygame.image.load("images_run_boy/resize_enemy.bmp")
        self.rect = self.image.get_rect()

        # Create new enemy
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Enemy's position
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        self.xx = float(self.rect_hero_x)
        self.yy = float(self.rect_hero_y)

    # def update(self):
    # """Moving enemy, random posytion"""

    # direction = random.randint(0, 150)

    # if direction == 4:
    # direction = direction * self.setting.direction_for_enemy

    # if direction == 1 and self.rect.right < self.screen_rect.right:
    # self.x += self.setting.enemy_speed
    # elif direction == 2 and self.rect.bottom < self.screen_rect.bottom:
    # self.y += self.setting.enemy_speed
    # elif direction == 3 and self.rect.left > 0:
    # self.x -= self.setting.enemy_speed
    # elif direction == 0 and self.rect.top > 0:
    # self.y -= self.setting.enemy_speed

    # self.rect.x = self.x
    # self.rect.y = self.y

    def update(self):
        """Moving the opponent behind the player"""
        self.rect_hero_x = self.hero_game.hero.rect.x
        self.rect_hero_y = self.hero_game.hero.rect.y
        self.xx = float(self.rect_hero_x)
        self.yy = float(self.rect_hero_y)

        if self.y != self.yy:
            if self.y < self.yy and self.rect.bottom < self.screen_rect.bottom:
                self.y += self.setting.enemy_speed
            elif self.y > self.yy and self.rect.top > 0:
                self.y -= self.setting.enemy_speed
        if self.x != self.xx:
            if self.x < self.xx and self.rect.right < self.screen_rect.right:
                self.x += self.setting.enemy_speed
            elif self.x > self.xx and self.rect.left > 0:
                self.x -= self.setting.enemy_speed

        self.rect.x = self.x
        self.rect.y = self.y
