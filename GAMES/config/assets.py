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
    def __init__(self, name, positions: tuple, dimesions: tuple, *path) -> None:
        super().__init__(positions, dimesions, *path)

        self.name = name

        self.bulletsCount = GAME.DEFAULT_BULLETS_COUNT
        self.bullets: list = []
        
        self.health = GAME.ItemsDimenstions.Spaceship.MAX_HEALTH

    def checkMovement(self, border: _BORDER, speed: int = GAME.DEFAULT_MOVE_VEL, keys: tuple = [pygame.K_a, pygame.K_d, pygame.K_w, pygame.K_s]) -> None:
        pressed = pygame.key.get_pressed()

        # chech if ROCKET is before or after the half
        # self._entity.x + self._entity.width - right border of spaceship
        if self._entity.x + self._entity.width <= border.getEntity().x:
            if pressed[keys[0]]:  # LEFT
                self.__move(DIRECTIONS.LEFT, speed)

            if pressed[keys[1]] and self._entity.x + self._entity.width + speed < border.getEntity().x:  # RIGHT
                self.__move(DIRECTIONS.RIGHT, speed)

        if self._entity.x > border.getEntity().x + border.getEntity().width:
            if pressed[keys[0]] and self._entity.x - speed > border.getEntity().x + border.getEntity().width:  # LEFT
                self.__move(DIRECTIONS.LEFT, speed)

            if pressed[keys[1]]:  # RIGHT
                self.__move(DIRECTIONS.RIGHT, speed)

        if pressed[keys[2]]:  # UP
            self.__move(DIRECTIONS.UP, speed)

        if pressed[keys[3]]:  # DOWN
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

    def shoot(self, key: int, facingRight: bool = True):
        if pygame.key.get_pressed()[key] and len(self.bullets) < self.bulletsCount:

            SOUNDS.BULLET_FIRE.play()

            if facingRight:
                x = self._entity.x + self._entity.width
            else:
                x = self._entity.x

            y = self._entity.y + self._entity.height // 2 - 7

            bullet = pygame.Rect(x, y,
                                 GAME.ItemsDimenstions.Bullet.WIDTH,
                                 GAME.ItemsDimenstions.Bullet.HEIGHT)

            self.bullets.append(bullet)

    def checkCollisionsWith(self, bullets: list[pygame.Rect], facingRight: bool = True):
        for bullet in bullets:
            if facingRight:
                bullet.x += GAME.DEFAULT_BULLET_VEL
            else:
                bullet.x -= GAME.DEFAULT_BULLET_VEL

            if self._entity.colliderect(bullet):
                SOUNDS.BULLET_HIT.play()
                self.health -= 1
                bullets.remove(bullet)
                
                if not self.stillAlive():
                    pygame.event.post(pygame.event.Event(GAME.Events.WINNER))
                    GAME.LOSER = self
                    
                return

            if facingRight:
                if bullet.x > GAME.WIDTH:
                    bullets.remove(bullet)
            else:
                if bullet.x < 0:
                    bullets.remove(bullet)
                    
    def stillAlive(self):
        return self.health > 0


class COLORS:
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    RED = (255, 30, 30)
    YELLOW = (250, 250, 30)


class IMAGES:
    pass

class SOUNDS:
    pygame.mixer.init()
    BULLET_HIT = pygame.mixer.Sound(os.path.join(os.path.dirname(
            __file__), '..', 'assets', 'Grenade+1.mp3'))
    BULLET_FIRE = pygame.mixer.Sound(os.path.join(os.path.dirname(
        __file__), '..', 'assets', 'Gun+Silencer.mp3'))
    
    BULLET_HIT.set_volume(.06)
    BULLET_FIRE.set_volume(.05)

class ITEMS:
    YELLOW_SPACESHIP = _PLAYER("Player - Left", (200, 300), (GAME.ItemsDimenstions.Spaceship.WIDTH,
                                            GAME.ItemsDimenstions.Spaceship.HEIGHT), '..', 'assets', 'spaceship_yellow.png')
    RED_SPACESHIP = _PLAYER("Player - Right", (500, 300), (GAME.ItemsDimenstions.Spaceship.WIDTH,
                                         GAME.ItemsDimenstions.Spaceship.HEIGHT), '..', 'assets', 'spaceship_red.png')
    MID_BORDER = _BORDER((GAME.WIDTH / 2 - 5, 0), (10, GAME.HEIGHT))
    SPACE = pygame.transform.scale(
        pygame.image.load(os.path.join(os.path.dirname(
            __file__), '..', 'assets', 'space.png')),
        (GAME.WIDTH, GAME.HEIGHT))
