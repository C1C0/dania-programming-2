import os
import pygame

from config.game import GAME


class _GameItem:
    def __init__(self, dimesions: tuple, *path) -> None:
        """_summary_

        Args:
            dimesions (tuple): _description_
            *path (strings): being accessed from this file
        """
        self.__image = pygame.image.load(
            os.path.join(os.path.dirname(__file__), *path))
        self.__object: pygame.Surface = pygame.transform.scale(
            self.__image, dimesions)

    def rotateItem(self, rotationDegree: int) -> pygame.Surface:
        self.__object = pygame.transform.rotate(self.__object, rotationDegree)
        return self.__object

    def getItem(self) -> pygame.Surface:
        return self.__object


class COLORS:
    WHITE = (255, 255, 255)


class IMAGES:
    pass


class ITEMS:
    YELLOW_SPACESHIP = _GameItem((GAME.ItemsDimenstions.Spaceship.WIDTH,
                                 GAME.ItemsDimenstions.Spaceship.HEIGHT), '..', 'assets', 'spaceship_yellow.png')
    RED_SPACESHIP = _GameItem((GAME.ItemsDimenstions.Spaceship.WIDTH,
                              GAME.ItemsDimenstions.Spaceship.HEIGHT), '..', 'assets', 'spaceship_red.png')
