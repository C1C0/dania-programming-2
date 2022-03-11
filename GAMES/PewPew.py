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

        ITEMS.YELLOW_SPACESHIP.move(D.RIGHT)
        drawWindow()

    pygame.quit()


if __name__ == '__main__':
    main()
