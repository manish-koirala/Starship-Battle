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
        self.SCREEN_BG_COLOR = (20, 20, 20) # Black

        # Ship Attributes
        self.SHIP_SPEED = 10

        # Bullet Attributes.
        self.BULLET_HEIGHT = 2
        self.BULLET_WIDTH = 100
        self.BULLET_COLOR = (255, 110, 100) # Red.
        self.BULLET_LIMIT = 5
        self.BULLET_VELOCITY = 8

        # Alien and Fleet Static Attributes
        self.ALIEN_FLEET_DROPLEN = 14

    def initialize_dynamic_settings(self):
        """Initialize the dynamic settings within the game."""
        # Alien and Fleet Dynamic Attributes.
        self.ALIEN_VELOCITY = 3.5 # positive value is left, negative value is right.


