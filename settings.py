class Settings:
    """A class to store the static and dynamic settings of the game."""
    def __init__(self):
        """Initialize the static and dynamic settings attributes."""
        self.initialize_static_settings()
        self.initialize_dynamic_settings()

    def initialize_static_settings(self):
        """Initialize the static settings within the game."""
        # Screen Attributes
        self.SCREEN_WIDTH = 1024
        self.SCREEN_HEIGHT = 800
        self.SCREEN_BG_COLOR = (0, 0, 0) # Black

        # Sound Attributes
        self.SOUND_VOLUME = 0.7

        # Ship Attributes
        self.SHIP_SPEED = 12.5

        # Bullet Attributes.
        self.BULLET_HEIGHT = 12.5
        self.BULLET_WIDTH = 2
        self.BULLET_COLOR = (255, 110, 100) # Red.
        self.BULLET_LIMIT = 4
        self.BULLET_VELOCITY = 7.5

        # Alien and Fleet Static Attributes
        self.ALIEN_FLEET_DROPLEN = 24

        # MAX_LIVES
        self.MAX_LIVES = 3

    def initialize_dynamic_settings(self):
        """Initialize the dynamic settings within the game."""
        # Alien and Fleet Dynamic Attributes.
        self.ALIEN_DEFAULT_VELOCITY = 3.5
        self.ALIEN_VELOCITY = 3.5 # positive value is left, negative value is right.
        self.ALIEN_VELOCITY_FACTOR = 1.12
        self.ALIEN_VELOCITY_MAX = 12.5

        # Score Multiplier
        self.HIT_SCORE_DEFAULT = 10
        self.HIT_SCORE = 10
        self.SCORE_MULTIPLIER = 1.25
        self.HIT_SCORE_MAX = 100


