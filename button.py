import pygame.font


class Button:
    def __init__(self, hero_game, msg, xx, yy):
        """Class for initialization button"""

        self.screen = hero_game.screen
        self.screen_rect = self.screen.get_rect()

        # Settings for button
        self.width = 200
        self.height = 50
        self.button_color = (0, 255, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        # Createing rectangle's button
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.y = self.screen_rect.y + yy
        self.rect.x = self.screen_rect.x + xx

        # Text for button
        self._prep_msg(msg)

    def _prep_msg(self, msg):
        """Preparing the text in the button"""
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        """Drawing button on screen"""
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
