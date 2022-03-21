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


class _GameEntity(_GameItem):
    def __init__(self, positions: tuple, dimesions: tuple, *path) -> None:
        if path:
            super().__init__(dimesions, *path)

        self._entity = pygame.Rect(
            positions[0], positions[1], dimesions[0], dimesions[1])

    def getEntity(self) -> pygame.Rect:
        return self._entity


class _BORDER(_GameEntity):
    def __init__(self, positions: tuple, dimesions) -> None:
        super().__init__(positions, dimesions)


class _PLAYER(_GameEntity):
    def __init__(self, positions: tuple, dimesions: tuple, *path) -> None:
        super().__init__(positions, dimesions, *path)

    def checkMovement(self, border: _BORDER, speed: int = GAME.DEFAULT_MOVE_VEL, keys: tuple = [pygame.K_a, pygame.K_d, pygame.K_w, pygame.K_s]) -> None:
        # chech if ROCKET is before or after the half
        # self._entity.x + self._entity.width - right border of spaceship
        if self._entity.x + self._entity.width <= border.getEntity().x:
            if pygame.key.get_pressed()[keys[0]]:  # LEFT
                self.__move(DIRECTIONS.LEFT, speed)

            if pygame.key.get_pressed()[keys[1]] and self._entity.x + self._entity.width + speed < border.getEntity().x:  # RIGHT
                self.__move(DIRECTIONS.RIGHT, speed)

        if self._entity.x > border.getEntity().x + border.getEntity().width:
            if pygame.key.get_pressed()[keys[0]] and self._entity.x - speed > border.getEntity().x + border.getEntity().width:  # LEFT
                self.__move(DIRECTIONS.LEFT, speed)

            if pygame.key.get_pressed()[keys[1]]:  # RIGHT
                self.__move(DIRECTIONS.RIGHT, speed)

        if pygame.key.get_pressed()[keys[2]]:  # UP
            self.__move(DIRECTIONS.UP, speed)

        if pygame.key.get_pressed()[keys[3]]:  # DOWN
            self.__move(DIRECTIONS.DOWN, speed)

    def __move(self, direction: str, speed: int = 1) -> None:
        if direction == DIRECTIONS.LEFT and self._entity.x - speed > 0:
            self._entity.x -= speed

        if direction == DIRECTIONS.RIGHT and self._entity.x + self._entity.width + speed < GAME.WIDTH:
            self._entity.x += speed

        if direction == DIRECTIONS.UP and self._entity.y - speed > 0:
            self._entity.y -= speed

        if direction == DIRECTIONS.DOWN and self._entity.y + self._entity.height + speed < GAME.HEIGHT:
            self._entity.y += speed

    def getPlayer(self) -> pygame.Rect:
        return self._entity


class COLORS:
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)


class IMAGES:
    pass


class ITEMS:
    YELLOW_SPACESHIP = _PLAYER((200, 300), (GAME.ItemsDimenstions.Spaceship.WIDTH,
                                            GAME.ItemsDimenstions.Spaceship.HEIGHT), '..', 'assets', 'spaceship_yellow.png')
    RED_SPACESHIP = _PLAYER((500, 300), (GAME.ItemsDimenstions.Spaceship.WIDTH,
                                         GAME.ItemsDimenstions.Spaceship.HEIGHT), '..', 'assets', 'spaceship_red.png')
    MID_BORDER = _BORDER((GAME.WIDTH / 2 - 5, 0), (10, GAME.HEIGHT))
