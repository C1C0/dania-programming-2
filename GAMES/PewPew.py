import pygame

from config.colors import COLORS
from config.game import GAME

"""
Terms:
- surface
- events
"""

# Set name
pygame.display.set_caption("PewPew Game - Winner of Game Award 2099")

def drawWindow() -> None:
    # DRAWING !!!!
    GAME.WIN.fill(COLORS.WHITE)
    pygame.display.update()

def main() -> int:
    """
    Main Game's code
    """
    
    # Controls the speed of main loop
    clock = pygame.time.Clock()
    
    run = True
    while run:
        
        # Enables max specified framerate, but doesn't affect the TIME of the game
        clock.tick(GAME.FPS)
        
        # get all events and listen to them
        for event in pygame.event.get():
            
            # If quit ... then quit :)
            if event.type == pygame.QUIT:
                run = False
                
        drawWindow()
                
    pygame.quit()
    
if __name__ == '__main__':
    main()