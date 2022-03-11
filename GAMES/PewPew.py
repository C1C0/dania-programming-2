import pygame

from config.assets import COLORS, IMAGES
from config.game import GAME

"""
Terms:
- surface
- events
"""

def drawWindow() -> None:
    # DRAWING !!!!
    GAME.WIN.fill(COLORS.WHITE)
    
    # Drawing from top left corner
    GAME.WIN.blit(IMAGES.YELLOW_SPACESHIP_IMAGE, (300, 100))
    
    pygame.display.update()

def main() -> int:
    """
    Main Game's code
    """
    
    run = True
    while run:
        
        # Enables max specified framerate, but doesn't affect the TIME of the game
        GAME.CLOCK.tick(GAME.FPS)
        
        # get all events and listen to them
        for event in pygame.event.get():
            
            # If quit ... then quit :)
            if event.type == pygame.QUIT:
                run = False
                
        drawWindow()
                
    pygame.quit()
    
if __name__ == '__main__':
    main()