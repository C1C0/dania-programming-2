import pygame

"""
Terms:
- surface
- events
"""

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

# Set name
pygame.display.set_caption("PewPew Game - Winner of Game Award 2099")

def main() -> int:
    """
    Main Game's code
    """
    
    run = True
    while run:
        
        # get all events and listen to them
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                run = False
                
    pygame.quit()
    
if __name__ == '__main__':
    main()