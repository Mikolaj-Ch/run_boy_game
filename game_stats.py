class GameStats:
    """All data need for stats during game"""

    def __init__(self, hero_game):
        """Data initialization"""

        self.setting = hero_game.setting
        self.hero_game = hero_game

        # Start game in unactive mode
        self.game_active = False

        # Evry game needs to start with 0 seconds
        self.time = 0

        # Method for reset data
        self.reset_stats()

    def reset_stats(self):
        """Resets the data for a new game"""

        self.live_left = self.setting.live_limit
        self.hero_game.setting.enemy_speed = 0.1
        self.hero_game.setting.level = 0
        self.hero_game.enemys.empty()
