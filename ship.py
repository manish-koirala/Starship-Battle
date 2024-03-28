import pygame as pg

class Ship:
    """A class that represents that attributes and behavior of the main ship in the game."""
    def __init__(self, sb_instance):
        """Initialize the attributes of a Ship instance."""
        self.screen = sb_instance.screen
        self.settings = sb_instance.settings
        self.image = pg.image.load("./assets/images/spaceship.png")
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = self.rect.x
        self.is_moving_left = False
        self.is_moving_right = False

    def draw(self):
        """Draw the ship onto the screen."""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """Update the position of the ship."""
        if self.is_moving_left and self.rect.left > self.screen_rect.left + 20:
            self.x -= self.settings.SHIP_SPEED
        if self.is_moving_right and self.rect.right < self.screen_rect.right - 20:
            self.x += self.settings.SHIP_SPEED
        
        self.rect.x = self.x