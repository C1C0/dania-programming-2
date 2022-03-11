import os
import pygame

from config.game import GAME, DIRECTIONS


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


class _PLAYER(_GameItem):

    def __init__(self, positions: tuple, dimesions: tuple, *path) -> None:
        super().__init__(dimesions, *path)

        self.__player = pygame.Rect(
            positions[0], positions[1], dimesions[0], dimesions[1])

    def checkMovement(self, vel: int = GAME.DEFAULT_MOVE_VEL, keys: tuple = [pygame.K_a, pygame.K_d, pygame.K_w, pygame.K_s]) -> None:
        if pygame.key.get_pressed()[keys[0]]:  # LEFT
            self.__move(DIRECTIONS.LEFT, vel)

        if pygame.key.get_pressed()[keys[1]]:  # RIGHT
            self.__move(DIRECTIONS.RIGHT, vel)

        if pygame.key.get_pressed()[keys[2]]:  # UP
            self.__move(DIRECTIONS.UP, vel)

        if pygame.key.get_pressed()[keys[3]]:  # DOWN
            self.__move(DIRECTIONS.DOWN, vel)

    def __move(self, direction: str, speed: int = 1) -> None:
        if direction == DIRECTIONS.LEFT:
            self.__player.x -= speed

        if direction == DIRECTIONS.RIGHT:
            self.__player.x += speed

        if direction == DIRECTIONS.UP:
            self.__player.y -= speed

        if direction == DIRECTIONS.DOWN:
            self.__player.y += speed

    def getPlayer(self) -> pygame.Rect:
        return self.__player


class COLORS:
    WHITE = (255, 255, 255)


class IMAGES:
    pass


class ITEMS:
    YELLOW_SPACESHIP = _PLAYER((200, 300), (GAME.ItemsDimenstions.Spaceship.WIDTH,
                                            GAME.ItemsDimenstions.Spaceship.HEIGHT), '..', 'assets', 'spaceship_yellow.png')
    RED_SPACESHIP = _PLAYER((500, 300), (GAME.ItemsDimenstions.Spaceship.WIDTH,
                                         GAME.ItemsDimenstions.Spaceship.HEIGHT), '..', 'assets', 'spaceship_red.png')
