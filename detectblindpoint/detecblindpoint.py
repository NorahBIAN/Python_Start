import pygame


from settings import Settings
from ball import Ball
from center import Center
import game_functions as gf

def run_game():
    # Initialize pygame, settings, and screen object.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Detect BlindPoint")
    
    
    # Make a ship.
    ball = Ball(ai_settings, screen)
    center = Center(ai_settings,screen)

    # Start the main loop for the game.
    while True:
        gf.check_events(ball)
        ball.update()
        gf.update_screen(ai_settings, screen, ball, center)
    
    
    
run_game()
quit