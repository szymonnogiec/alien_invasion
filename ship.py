import pygame


class Ship:
    def __init__(self, ai_settings, screen):
        """Init the ship object"""
        self.ai_settings = ai_settings
        self.screen = screen
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # place new ship in the center
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.center = float(self.rect.centerx)

        # movement flags
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Update ship's position based on the movement flags"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor
        # update rect object
        self.rect.centerx = self.center

    def blit_me(self):
        """Draw the ship at its current position"""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """Center the ship on the screen"""
        self.center = self.screen_rect.centerx
