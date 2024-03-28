import pygame as pg
from pygame.sprite import Sprite

class Bullet(Sprite):
    """A class representing a Bullet in the game."""

    def __init__(self, sb_game):
        """Initialize the attributes of a bullet."""
        super().__init__()
        self.settings = sb_game.settings
        self.screen = sb_game.screen
        self.ship_rect = sb_game.ship.rect
        self.rect = pg.Rect(0, 0, self.settings.BULLET_WIDTH, self.settings.BULLET_HEIGHT)
        self.rect.midbottom = self.ship_rect.midtop
        self.y = self.rect.y

    def draw(self):
        """Draw the bullets onto the screen."""
        pg.draw.rect(self.screen, self.settings.BULLET_COLOR, self.rect)

    def update(self):
        """Update the position of the bullets onto the screen."""
        self.y -= self.settings.BULLET_VELOCITY
        self.rect.y = self.y
