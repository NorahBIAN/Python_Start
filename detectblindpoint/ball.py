import pygame

class Ball():
    def __init__(self, ai_settings, screen):
        """Initialize the ship and set its starting position."""
        self.screen = screen
        self.ai_settings = ai_settings
        # Load the ship image and get its rect.
        self.image = pygame.image.load('images/ball2.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        # Start each new ship at the bottom center of the screen.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery
        
        # Store a decimal value for the ship's center.
        self.center = float(self.rect.centerx)

        
        # Movemlf.centeryy = float(self.rect.centerx)ent flags
        self.moving_right = False
        self.moving_left = False
    
    def update(self):
        """Update the ship's position based on movement flags."""
        # Update the ship's center value, not the rect.
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ball_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ball_speed_factor
 
        # Update rect object from self.center.
        self.rect.centerx = self.center

                
    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)
