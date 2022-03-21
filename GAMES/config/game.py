import pygame

class DIRECTIONS:
    LEFT = 'left'
    RIGHT = 'right'
    UP = 'up'
    DOWN = 'down'
    

class GAME:
    WIDTH, HEIGHT = 900, 500
    WIN = pygame.display.set_mode((WIDTH, HEIGHT))

    FPS = 60
    
    DEFAULT_MOVE_VEL = 5
    DEFAULT_BULLET_VEL = 50
    DEFAULT_BULLETS_COUNT = 20
    
    FIRST_RUN = True
    
    LOSER: any = None
    
    CLOCK = pygame.time.Clock()
    
    class Font:
        FONT = None
    
    class Events:
        WINNER = pygame.USEREVENT + 1

    class ItemsDimenstions:
        class Spaceship:
            HEIGHT = 55
            WIDTH = 45
            
            MAX_HEALTH = 4
        
        class Bullet:
            HEIGHT = 5
            WIDTH = 10

    def init() -> None:
        # Set name
        pygame.display.set_caption("PewPew Game - Winner of Game Award 2099")
