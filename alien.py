import pygame as pg
from pygame.sprite import Sprite

class Alien(Sprite):
    """A class representing an Alien in the game."""
    def __init__(self, sb_game, x, y):
        super().__init__()
        self.image = pg.image.load('./assets/images/alien.png')
        self.rect = self.image.get_rect()
        self.settings = sb_game.settings
        self.rect.x, self.rect.y, self.x, self.y = x, y, x, y
        
    def update(self):
        """Update the position of aliens."""
        self.x += self.settings.ALIEN_VELOCITY
        self.rect.x = self.x