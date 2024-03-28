import pygame as pg

class Button:
    """A class representing a button eg. play-button in the game."""
    def __init__(self, sb_game, font_size=28, bold=False):
        """Initialize the attributes of a button."""
        self.font = pg.font.SysFont("Monospace", font_size, bold)
        self.screen = sb_game.screen
        self.screen_rect = sb_game.screen_rect
        

class PlayButton(Button):
    """A class representing a playbutton."""
    def __init__(self, sb_game):
        """Initialize the attributes of a playbutton."""
        super().__init__(sb_game, font_size=28, bold=True)
        self.image = self.font.render("Play", True, (255, 255, 255))
        self.rect = self.image.get_rect()

    def draw(self):
        """Draw the playbutton onto the screen."""
        self.rect.center = self.screen_rect.center
        self.screen.fill((90, 90, 90), self.rect)
        self.screen.blit(self.image, self.rect)