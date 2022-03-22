import pygame

from config.settings import PLAYER_SIZES

PLAYER_SIGN = 'P'


class Player(pygame.sprite.Sprite):
    def __init__(self, pos) -> None:
        super().__init__()

        self.image = pygame.Surface(PLAYER_SIZES)
        self.image.fill('yellow')
        self.rect = self.image.get_rect(topleft=pos)
