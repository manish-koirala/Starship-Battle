import pygame as pg
from sys import exit as sysexit
from time import sleep as timesleep
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien
from button import PlayButton
from stats import Stats
from scoreboard import ScoreBoard

class StarshipBattle:
    """A class that represents the main game."""
    def __init__(self):
        pg.init()
        pg.mixer.init()
        self.settings = Settings()
        self.screen = pg.display.set_mode((self.settings.SCREEN_WIDTH, self.settings.SCREEN_HEIGHT))
        self.screen_rect = self.screen.get_rect()
        pg.display.set_caption("Starship Battle")
        self.icon = pg.image.load("./assets/images/alien.png")
        pg.display.set_icon(self.icon)
        self.clock = pg.time.Clock()
        self.ship = Ship(self)
        self.run = False
        self.bullets = pg.sprite.Group()
        self.aliens = pg.sprite.Group()
        self.play_btn = PlayButton(self)
        self.stats = Stats(self)
        self.scoreboard = ScoreBoard(self)
        self._create_fleet()
        self.shoot_sound = pg.mixer.Sound("./assets/sounds/shoot.mp3")
        self.explode_sound = pg.mixer.Sound("./assets/sounds/explode.mp3")
        pg.mixer.music.set_volume(self.settings.SOUND_VOLUME)

    def run_game(self):
        """Run the game."""
        while True:
            # Check for events within the game.
            self._check_events()
            if self.run:
                # Update the ship position.
                self.ship.update()
                # Update the alien fleet.
                self._update_fleet()
                # Detect the collision between alien and bullets.
                self._detect_collisions()
                # Update the game stats.
                self._update_game_stats()
            # Update the display accordingly.
            self._update_display()
            # Set the tick rate
            self.clock.tick(68)

    def _check_events(self):
        """Check for in-game events like keypresses and mouse clicks."""
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sysexit()
            
            if event.type == pg.KEYDOWN:
                self._check_keydown_events(event)
            
            if event.type == pg.KEYUP:
                self._check_keyup_events(event)

            if event.type == pg.MOUSEBUTTONDOWN:
                self._check_mousedown_events(event)

    def _check_keydown_events(self, event):
        """Check for keydown events"""
        if event.key == pg.K_LEFT:
            self.ship.is_moving_left = True
        elif event.key == pg.K_RIGHT:
            self.ship.is_moving_right = True
        elif event.key == pg.K_q:
            pg.quit()
            sysexit()
        elif event.key == pg.K_SPACE:
            self._create_bullet()

    def _check_keyup_events(self, event):
        """Check for keyup events."""
        if event.key == pg.K_LEFT:
            self.ship.is_moving_left = False
        elif event.key == pg.K_RIGHT:
            self.ship.is_moving_right = False

    def _check_mousedown_events(self, event):
        """Check for events that involve mouse clicks."""
        # Check if the user clicked in play btn.
        if not self.run and pg.Rect.collidepoint(self.play_btn.rect, pg.mouse.get_pos()):
            self.run = True
    
    def _update_display(self):
        """Update the display screen."""
        # Fill the screen with white color.
        self.screen.fill(self.settings.SCREEN_BG_COLOR)
        # Draw the ship.
        self.ship.draw()
        
        # Draw, update and refresh the bullets.
        self._draw_bullets()
        self._update_bullets()
        self._refresh_bullets()
        # Draw the alien fleet.
        self._draw_fleet()

        # Draw the play_btn on top
        if not self.run:
            # Draw play button.
            self.play_btn.draw()
        
        # Draw the lives.
        self.stats.draw_lives()
        # Draw the scores.
        self.scoreboard.draw_score()
        self.scoreboard.draw_high_score()
        # Draw the level.
        self.stats.draw_level()
        # Update the display.
        pg.display.flip()


    # BULLETS
    def _create_bullet(self):
        """Create a new bullet."""
        if len(self.bullets) < self.settings.BULLET_LIMIT:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
            pg.mixer.Sound.play(self.shoot_sound)

    def _draw_bullets(self):
        """Draw all the bullets in the bullets group."""
        for bullet in self.bullets.sprites():
            bullet.draw()       

    def _update_bullets(self):
        """Update all the bullets in the bullets group."""
        for bullet in self.bullets.sprites():
            bullet.update()
    
    def _refresh_bullets(self):
        """Destroy the bullets that leave the screen."""
        for bullet in self.bullets.sprites():
            if bullet.rect.y < self.screen_rect.top:
                self.bullets.remove(bullet)
                break

    def _empty_bullets(self):
        """Kill all the bullets."""
        self.bullets.empty()
        

    # ALIENS
    def _create_alien(self, x, y):
        """Create an alien."""
        new_alien = Alien(self, x, y)
        self.aliens.add(new_alien)
    
    def _create_fleet(self):
        """Create an alien fleet."""
        test_alien = Alien(self, 0, 0)
        num_col = (self.screen_rect.width // (2 * test_alien.rect.width)) - 4
        num_row = self.screen_rect.height // (4 * test_alien.rect.height)
        for y in range(num_row):
            for x in range(num_col):
                alien = Alien(self, x*test_alien.rect.width*2, test_alien.rect.height + y*test_alien.rect.height*2)
                self.aliens.add(alien)

    def _delete_fleet(self):
        """Wipe out the alien fleet."""
        self.aliens.empty()

    def _draw_fleet(self):
        """Draw the entire alien fleet."""
        self.aliens.draw(self.screen)

    def _update_fleet(self):
        """Update the entire alien fleet."""
        # Move the aliens in their direction.
        self.aliens.update()
        for alien in self.aliens.sprites():
            if alien.rect.right > self.screen_rect.right or alien.rect.left < self.screen_rect.left:
                self.settings.ALIEN_VELOCITY *= -1 # Inverse the direction of movement.
                self._drop_fleet() # Drop the alien fleet.
                break
        
    def _drop_fleet(self):
        """Drop the alien fleet."""
        for alien in self.aliens.sprites():
            alien.y += self.settings.ALIEN_FLEET_DROPLEN
            alien.rect.y = alien.y

    def _detect_collisions(self):
        """Detect collisions in the game."""
        # Collision between alien and bullet.
        for alien in self.aliens.sprites():
            for bullet in self.bullets.sprites():
                if pg.Rect.colliderect(alien.rect, bullet.rect):
                    self.bullets.remove(bullet)
                    self.aliens.remove(alien)
                    self.scoreboard.current_score += self.settings.HIT_SCORE
                    pg.mixer.Sound.play(self.explode_sound)

            # Collision between ship and alien.
            if pg.Rect.colliderect(alien.rect, self.ship.rect) and self.stats.CURRENT_LIVES > 0:
                self.stats.CURRENT_LIVES -= 1
                self.stats.lives.remove(self.stats.lives.sprites()[-1])
                self._delete_fleet()
                self._empty_bullets()
                self._create_fleet()
                pg.mixer.Sound.play(self.explode_sound)
                timesleep(1.5)
    
    def _update_game_stats(self):
        """Update the game stats."""
        # Reset the game stats when the player has zero lives.
        if self.stats.CURRENT_LIVES == 0:
            self.run = False
            self.stats.CURRENT_LIVES = self.stats.MAX_LIVES
            self.stats.create_lives() # Recreate lives.
            # Reset the current score to 0.
            self.scoreboard.current_score = 0
            # Reset the alien speed.
            self.settings.ALIEN_VELOCITY = self.settings.ALIEN_DEFAULT_VELOCITY   
            # Write the high scores.
            self.scoreboard.write_high_score()
            # Reset the level.
            self.stats.level.level = 0
            # Reset the hit score.
            self.settings.HIT_SCORE = self.settings.HIT_SCORE_DEFAULT

        # Update the high score if the curren_score is more than the high score.
        if self.scoreboard.current_score > self.scoreboard.high_score:
            self.scoreboard.high_score = self.scoreboard.current_score

        # Update the levels.
        if len(self.aliens) == 0:
            self._delete_fleet()
            self._empty_bullets()
            self.stats.level.level += 1
            if self.settings.ALIEN_VELOCITY < self.settings.ALIEN_VELOCITY_MAX:
                self.settings.ALIEN_VELOCITY *= self.settings.ALIEN_VELOCITY_FACTOR
            if self.settings.HIT_SCORE < self.settings.HIT_SCORE_MAX:
                self.settings.HIT_SCORE = round(self.settings.HIT_SCORE * self.settings.SCORE_MULTIPLIER)
            self._create_fleet()
        
   
if __name__ == '__main__':
    # Run the game, if this module is run directly.
    sb = StarshipBattle()
    sb.run_game()