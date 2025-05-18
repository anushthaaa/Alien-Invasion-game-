import sys # to exit the game when player quits
import pygame

def check_events(ship):
    """responds to keypresses and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ship)

        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship) 
            

def check_keydown_events(event, ship):
        if event.key == pygame.K_RIGHT:
            ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            ship.moving_left = True

def check_keyup_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

    

def update_screen(cus_settings, screen, ship):
    """updates images on the screen and flip to the new screen"""
    screen.fill(cus_settings.bg_color)
    ship.blitme()

    #make the most recently drawn screen visible
    pygame.display.flip()


