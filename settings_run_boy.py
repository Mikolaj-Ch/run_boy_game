class Settings:
    """Class meant for all settings in the game"""

    def __init__(self):
        """Initialization settings of game"""

        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.background_color = (192, 192, 192)

        # Hero speed
        self.hero_speed = 1.2
        self.live_limit = 1

        # Enemy settings
        self.enemy_speed = 0.1  # 20
        self.direction_for_enemy = -1

        # For stats
        self.point = 0.00001

        # Checking level for game
        self.level = 0
