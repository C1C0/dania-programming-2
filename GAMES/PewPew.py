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
    GAME.WIN.blit(ITEMS.SPACE, (0, 0))

    pygame.draw.rect(GAME.WIN, COLORS.BLACK, ITEMS.MID_BORDER.getEntity())
    
    GAME.WIN.blit(GAME.Font.FONT.render(f"H: {ITEMS.YELLOW_SPACESHIP.health}", 1, COLORS.YELLOW), (5,5))
    GAME.WIN.blit(GAME.Font.FONT.render(f"H: {ITEMS.RED_SPACESHIP.health}", 1, COLORS.YELLOW), (GAME.WIDTH - 75,5))
    
    GAME.WIN.blit(ITEMS.YELLOW_SPACESHIP.getItem(), (ITEMS.YELLOW_SPACESHIP.getPlayer().x, ITEMS.YELLOW_SPACESHIP.getPlayer().y))
    GAME.WIN.blit(ITEMS.RED_SPACESHIP.getItem(), (ITEMS.RED_SPACESHIP.getPlayer().x, ITEMS.RED_SPACESHIP.getPlayer().y))
    
    drawBullets(ITEMS.YELLOW_SPACESHIP, COLORS.YELLOW)
    drawBullets(ITEMS.RED_SPACESHIP, COLORS.RED)
    
    if GAME.LOSER:
        text = GAME.Font.FONT.render(f"{GAME.LOSER.name} LOST", True, COLORS.BLACK, COLORS.WHITE)
        #get the rect of the text
        textRect = text.get_rect()
        #set the position of the text
        textRect.center = (GAME.WIDTH // 2, GAME.HEIGHT // 2)
        #add text to window
        GAME.WIN.blit(text, textRect)

    pygame.display.update()
    
def drawBullets(spaceship, color):
    for bullet in spaceship.bullets:
        pygame.draw.rect(GAME.WIN, color, bullet)


def initItems() -> None:
    pygame.font.init()
    
    GAME.Font.FONT = pygame.font.Font(None, 32)
    
    ITEMS.YELLOW_SPACESHIP.rotateItem(90)
    ITEMS.RED_SPACESHIP.rotateItem(-90)


def main() -> int:
    """
    Main Game's code
    """

    if GAME.FIRST_RUN:
        initItems()
        GAME.FIRST_RUN = False

    run = True
    while run:

        # Enables max specified framerate, but doesn't affect the TIME of the game
        GAME.CLOCK.tick(GAME.FPS)

        # get all events and listen to them
        for event in pygame.event.get():

            # If quit ... then quit :)
            if event.type == pygame.QUIT:
                run = False
            
            if event.type == pygame.KEYDOWN: # does something only on event of PRESSING down (any) key   
                ITEMS.YELLOW_SPACESHIP.shoot(pygame.K_SPACE)
                ITEMS.RED_SPACESHIP.shoot(pygame.K_RCTRL, False)
                
        if not GAME.LOSER:              
            ITEMS.YELLOW_SPACESHIP.checkMovement(ITEMS.MID_BORDER, 10)
            ITEMS.RED_SPACESHIP.checkMovement(ITEMS.MID_BORDER, 10, [pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN])
            
            ITEMS.YELLOW_SPACESHIP.checkCollisionsWith(ITEMS.RED_SPACESHIP.bullets, False)
            ITEMS.RED_SPACESHIP.checkCollisionsWith(ITEMS.YELLOW_SPACESHIP.bullets)
        
        drawWindow()

    pygame.quit()

if __name__ == '__main__':
    main()
