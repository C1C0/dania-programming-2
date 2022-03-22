import pygame

from models.Tile import Tile, TILE_SIGN
from config.settings import TILE_SIZE


class Level:
    def __init__(self, levelData: list[str], surface: pygame.Surface) -> None:
        self.displaySurface: pygame.Surface = surface

        self.setup_level(levelData)
        
        self.worldShift = 0

    def setup_level(self, layout: list[str]):
        self.tiles = pygame.sprite.Group()

        for rowIndex, row in enumerate(layout):
            for columnIndex, cell in enumerate(row):
                if cell == TILE_SIGN:
                    self.tiles.add(Tile((columnIndex * TILE_SIZE,  rowIndex * TILE_SIZE),
                                        TILE_SIZE))

    def run(self):
        self.tiles.update()
        self.tiles.draw(self.displaySurface)
