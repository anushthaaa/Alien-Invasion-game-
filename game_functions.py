import sys # to exit the game when player quits
import pygame

def check_events(ship):
    """responds to keypresses and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = True
            elif event.key == pygame.K_LEFT:
                ship.moving_right = True

        elif event.type == pygame.KEYUP:
            if event.type == pygame.K_RIGHT:
                ship.moving_right = False
            elif event.type == pygame.K_LEFT:
                ship.moving_left == False


def update_screen(cus_settings, screen, ship):
    """updates images on the screen and flip to the new screen"""
    screen.fill(cus_settings.bg_color)
    ship.blitme()

    #make the most recently drawn screen visible
    pygame.display.flip()


