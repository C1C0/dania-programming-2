import pygame


class GAME:
    WIDTH, HEIGHT = 900, 500
    WIN = pygame.display.set_mode((WIDTH, HEIGHT))

    FPS = 60

    CLOCK = pygame.time.Clock()

    class ItemsDimenstions:
        class Spaceship:
            HEIGHT = 55
            WIDTH = 45

    def init() -> None:
        # Set name
        pygame.display.set_caption("PewPew Game - Winner of Game Award 2099")
