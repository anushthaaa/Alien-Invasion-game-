# creating a setting class

class Settings():
    """A class to store all setting of this game"""

    def __init__(self):
        """initializing the same's setting"""
        # screen settings
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (30,0,60)

        # ship settings
        self.ship_speed_factor = 1.5


        