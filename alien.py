import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """A class to represent a single alien in the fleet"""

    def __init__(self, ai_settings, screen):
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)

    def update(self):
        """Move the alien right of left"""
        self.x += (self.ai_settings.fleet_direction *
                   self.ai_settings.alien_speed_factor)
        self.rect.x = self.x

    def blit_me(self):
        """Draw the alient at its current location"""
        self.screen.blit(self.image, self.rect)

    def check_edges(self):
        """Returns True if alien is at the edge of the screen"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True
