


class GameStats():
    def __init__(self, settings):
        self.settings = settings
        self.reset()

    def reset(self):
        self.lives_left = self.settings.ship_lives
