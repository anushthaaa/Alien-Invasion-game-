# for creating an empty pygame window

import pygame # for the functionality needed for the game
from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
    # inititalize game and create a screen obj
    pygame.init() #initializes background setting to work clearly
    cus_settings = Settings()
    screen = pygame.display.set_mode((cus_settings.screen_height, cus_settings.screen_width))
    pygame.display.set_caption("ALIEN INVASION")

    ship = Ship(screen)

    while True:
        gf.check_events
        gf.update_screen(cus_settings, screen, ship)

        # make the most recently drawn screen visible
        pygame.display.flip()
    
run_game()



