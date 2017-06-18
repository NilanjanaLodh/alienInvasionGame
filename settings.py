class Settings():
    """ store all settings for alien invasion """

    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 700
        self.bg_color = (200, 200, 255) ###pale, sky blue
        self.ship_speed = 1
        self.bullet_speed = 0.5
        self.bullet_size = 20
        self.bullet_color = (200, 50, 50) ###pinkish

        self.alien_speed = 0.3
        self.alien_drop_speed = 10
        self.alien_direction = 1
        self.alien_width = 64
        self.alien_height = 64
        self.alien_border = 100
        self.alien_xspacing = 80
        self.alien_yspacing = 60
        spacex = self.screen_width - 2 * self.alien_border
        self.num_aliens_x = int(spacex / (self.alien_width + self.alien_xspacing)) + 1
        self.num_alien_rows = 2

        self.ship_lives = 4
