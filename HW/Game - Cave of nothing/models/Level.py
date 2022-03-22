import pygame

from models.Tile import Tile

class Level:
    def __init__(self, levelData: list[str], surface: pygame.Surface) -> None:
        self.displaySurface: pygame.Surface = surface
        self.levelData: list[str] = levelData
        
    def run(self):
        pass
