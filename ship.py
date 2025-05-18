import pygame

class Ship():

    def __init__(self, cus_settings, screen,):
        """initialize the ship and set its starting position."""
        self.screen = screen
        self.cus_settings = cus_settings
        
        # Load the original image
        original_image = pygame.image.load('Images/ship.bmp')
        
        # Define the new size you want (width, height)
        new_width = 80  # Adjust these values as needed
        new_height = 60  # Adjust these values as needed
        
        # Scale the image to the new size
        self.image = pygame.transform.scale(original_image, (new_width, new_height))
        
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # start each new ship at the bottom center of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # store decimal value for ship's center
        self.center = float(self.rect.centerx)

        # moving flag
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """update the ship's position based on the movement flag"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.cus_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.cus_settings.ship_speed_factor

        # update rect obj fromself.center
        self.rect.centerx = self.center


    def blitme(self):
        """draws the ship at the current location"""
        self.screen.blit(self.image, self.rect)



