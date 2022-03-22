import pygame

from models.Tile import Tile, TILE_SIGN
from models.Player import Player, PLAYER_SIGN
from config.settings import TILE_SIZE, PLAYER_SIZES


class Level:
    def __init__(self, levelData: list[str], surface: pygame.Surface) -> None:
        self.displaySurface: pygame.Surface = surface

        self.setup_level(levelData)

        self.worldShift = 0

    def setup_level(self, layout: list[str]):
        self.tiles = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()

        for rowIndex, row in enumerate(layout):
            for columnIndex, cell in enumerate(row):
                self.__placeSprite(cell, TILE_SIGN, self.tiles,
                                   Tile((columnIndex * TILE_SIZE,  rowIndex * TILE_SIZE),
                                        TILE_SIZE))

                self.__placeSprite(cell, PLAYER_SIGN, self.player,
                                   Player((columnIndex * PLAYER_SIZES[0],  rowIndex * PLAYER_SIZES[1])))

    def __placeSprite(self, cell, sign,
                      groupToAdd: pygame.sprite.Group | pygame.sprite.GroupSingle,
                      spriteToAdd: pygame.sprite.Sprite):
        if cell == sign:
            groupToAdd.add(spriteToAdd)

    def run(self):
        self.tiles.update(0)
        self.tiles.draw(self.displaySurface)
        
        self.player.update()
        self.player.draw(self.displaySurface)
