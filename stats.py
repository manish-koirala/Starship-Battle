import pygame as pg
from pygame.sprite import Sprite

class Stats:
    """A class to manage the game stats eg. lives in the game."""
    def __init__(self, sb_game):
        """Initialize the attributes of stats."""
        self.settings = sb_game.settings
        self.MAX_LIVES = self.settings.MAX_LIVES
        self.screen = sb_game.screen
        self.CURRENT_LIVES = self.MAX_LIVES
        self.lives = pg.sprite.Group()
        self.level = Level(sb_game)
        self.create_lives()

    def create_lives(self):
        """Create the max number of lives."""
        for i in range(self.MAX_LIVES):
            life = Life()
            life.rect.x = life.rect.width * i * 2
            self.lives.add(life)

    def draw_lives(self):
        """Draw the lives onto the screen."""
        self.lives.draw(self.screen)

    def draw_level(self):
        """Draw the level onto the screen."""
        self.level.draw()

class Life(Sprite):
    """A class representing a game life."""
    def __init__(self):
        super().__init__()
        self.image = pg.transform.scale_by(pg.image.load('./assets/images/spaceship.png'), 0.5)
        self.rect = self.image.get_rect()

class Level():
    """A class representing the current game level."""
    def __init__(self, sb_game):
        self.level = 0
        self.font = pg.font.SysFont("Arial", 32, True)
        self.screen = sb_game.screen
        self.screen_rect = sb_game.screen_rect

    def draw(self):
        self.image = self.font.render(str(self.level), True, (255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.midtop = self.screen_rect.midtop
        self.screen.blit(self.image, self.rect)

