import pygame

from models.Tile import Tile, TILE_SIGN
from models.Player import Player, PLAYER_SIGN

from config.settings import TILE_SIZE, PLAYER_SIZES, HORIZONTAL_SCROLL_BOUNDARIES, PLAYER_DEFAULT_SPEED
from config.game import SCREEN_WIDTH


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

    def scroll_x(self):
        player = self.player.sprite
        player_x = player.rect.centerx
        direction_x = player.direction.x
        
        if player_x < HORIZONTAL_SCROLL_BOUNDARIES.left and direction_x < 0:
            self.worldShift = PLAYER_DEFAULT_SPEED
            player.speed = 0
            print("moving RIGHT")
        elif player_x > SCREEN_WIDTH - HORIZONTAL_SCROLL_BOUNDARIES.right and direction_x > 0:
            self.worldShift = -PLAYER_DEFAULT_SPEED
            player.speed = 0
        else:
            self.worldShift = 0
            player.speed = PLAYER_DEFAULT_SPEED

    def __placeSprite(self, cell, sign,
                      groupToAdd: pygame.sprite.Group | pygame.sprite.GroupSingle,
                      spriteToAdd: pygame.sprite.Sprite):
        if cell == sign:
            groupToAdd.add(spriteToAdd)
            
    def horizontalMovementCollision(self):
        player = self.player.sprite
        
        player.rect.x += player.direction.x * player.speed
        
        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.x < 0:
                    player.rect.left = sprite.rect.right
                elif player.direction.x > 0:
                    player.rect.right = sprite.rect.left
                    
    def verticalMoementCollision(self):
        player = self.player.sprite       
        player.apply_gravity()
        
        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.y < 0:
                    player.rect.top = sprite.rect.bottom
                    player.direction.y = 0
                elif player.direction.y > 0:
                    player.rect.bottom = sprite.rect.top       
                    player.direction.y = 0
                    player.inJump = False

    def run(self):
        self.tiles.update(self.worldShift)
        self.tiles.draw(self.displaySurface)
        
        self.player.update()
        self.horizontalMovementCollision()
        self.verticalMoementCollision()
        self.player.draw(self.displaySurface)

        self.scroll_x()
