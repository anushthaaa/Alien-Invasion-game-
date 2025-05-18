import sys # to exit the game when player quits
import pygame

def check_events():
    """responds to keypresses and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

def update_screen(cus_settings, scree, ship):
    """updates images on the screen and flip to the new screen"""
    scree.fill(cus_settings.bg_color)
    ship.blitme()

    #make the most recently drawn screen visible
    pygame.display.flip()