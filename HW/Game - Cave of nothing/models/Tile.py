import pygame
import config.colors as colors

TILE_SIGN = 'X'

class Tile(pygame.sprite.Sprite):
    def __init__(self, pos: tuple, size) -> None:
        super().__init__()
        self.image = pygame.Surface((size, size))
        self.image.fill(colors.GREY)
        self.rect = self.image.get_rect(topleft = pos)
        
    def update(self, xShitf):
        self.rect.x += xShitf