# -*- coding: utf-8 -*-
"""
Created on Mon May 14 11:16:34 2018

@author: byy
"""

import pygame

class Center():
    def __init__(self, ai_settings, screen):
        """Initialize the ship and set its starting position."""
        self.screen = screen
        self.ai_settings = ai_settings
        # Load the ship image and get its rect.
        self.image = pygame.image.load('images/ball.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        # Start each new ship at the bottom center of the screen.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery
        

    def update(self):
        """Update the ship's position based on movement flags."""
        # Update the ship's center value, not the rect.
        # Update rect object from self.center.
        self.rect.centerx = self.center
                
    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)
