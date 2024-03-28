import pygame as pg
import json

class ScoreBoard:
    """A class that represents the game scoreboard displaying highscores and current scores."""
    def __init__(self, sb_game):
        """Initialize the attributes of the scoreboard."""
        self.current_score = 0
        with open('data.json', 'r') as fo:
            self.high_score = json.load(fo)['high_score']
        self.font = pg.font.SysFont("Arial", 36, True)
        self.screen = sb_game.screen
        self.screen_rect = sb_game.screen_rect

    def draw_score(self):
        """Draw the current score onto the screen."""
        score_text = self.font.render(str(self.current_score), True, (255, 255, 255))
        score_text_rect = score_text.get_rect()
        score_text_rect.topright = self.screen_rect.topright
        score_text_rect.x -= 10
        self.screen.blit(score_text, score_text_rect)

    def draw_high_score(self):
        """Draw the high score onto the screen."""
        high_score_text = self.font.render(str(self.high_score), True, (255, 255, 255))
        high_score_text_rect = high_score_text.get_rect()
        high_score_text_rect.topright = self.screen_rect.topright
        high_score_text_rect.x -= 10
        high_score_text_rect.y += (high_score_text_rect.height + 10)
        self.screen.blit(high_score_text, high_score_text_rect)

    def write_high_score(self):
        """Write the high score permanently to a file for future reference."""
        data = {'high_score': self.high_score}
        with open('./data.json', 'w') as fo:
            json.dump(data, fo)