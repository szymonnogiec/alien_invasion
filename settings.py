class Settings:
    """A class for all the settings"""

    def __init__(self):
        """Intiialize all static settings"""
        self.width = 1200
        self.height = 800
        self.bg_color = (230, 230, 230)

        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3

        self.fleet_drop_speed = 10

        self.ship_limit = 3
        # how quickly the game speeds up
        self.speed_up_scale = 1.1
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game"""
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1
        # fleet direction of 1 represents right, -1 left
        self.fleet_direction = 1
        self.alien_points = 50

    def increase_speed(self):
        """Increase speed settings and point values"""
        self.ship_speed_factor *= self.speed_up_scale
        self.bullet_speed_factor *= self.speed_up_scale
        self.alien_speed_factor *= self.speed_up_scale
        self.alien_points = int(self.alien_points * self.score_scale)
