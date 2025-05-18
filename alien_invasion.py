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

    ship = Ship(cus_settings, screen)

    while True:
        gf.check_events(ship)
        ship.update()
        gf.update_screen(cus_settings, screen, ship)


if __name__ == "__main__" :   
    run_game()



