import pygame

from config.assets import COLORS, IMAGES, ITEMS
from config.game import GAME, DIRECTIONS as D

"""
Terms:
- surface
- events
"""


def drawWindow() -> None:
    # DRAWING !!!!
    GAME.WIN.fill(COLORS.WHITE)

    pygame.draw.rect(GAME.WIN, COLORS.BLACK, ITEMS.MID_BORDER.getEntity())
    
    GAME.WIN.blit(ITEMS.YELLOW_SPACESHIP.getItem(), (ITEMS.YELLOW_SPACESHIP.getPlayer().x, ITEMS.YELLOW_SPACESHIP.getPlayer().y))
    GAME.WIN.blit(ITEMS.RED_SPACESHIP.getItem(), (ITEMS.RED_SPACESHIP.getPlayer().x, ITEMS.RED_SPACESHIP.getPlayer().y))

    pygame.display.update()


def initItems() -> None:
    ITEMS.YELLOW_SPACESHIP.rotateItem(90)
    ITEMS.RED_SPACESHIP.rotateItem(-90)


def main() -> int:
    """
    Main Game's code
    """

    initItems()

    run = True
    while run:

        # Enables max specified framerate, but doesn't affect the TIME of the game
        GAME.CLOCK.tick(GAME.FPS)

        # get all events and listen to them
        for event in pygame.event.get():

            # If quit ... then quit :)
            if event.type == pygame.QUIT:
                run = False
                
                
        ITEMS.YELLOW_SPACESHIP.checkMovement(10)
        ITEMS.RED_SPACESHIP.checkMovement(10, [pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN])
        
        
        drawWindow()

    pygame.quit()


if __name__ == '__main__':
    main()
