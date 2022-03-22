import pygame

from config.settings import PLAYER_SIZES, PLAYER_DEFAULT_SPEED, GRAVITY, PLAYER_JUMP_SPEED

PLAYER_SIGN = 'P'

class Player(pygame.sprite.Sprite):
    def __init__(self, pos) -> None:
        super().__init__()

        self.image = pygame.Surface(PLAYER_SIZES)
        self.image.fill('yellow')
        self.rect = self.image.get_rect(topleft=pos)
        
        self.direction = pygame.math.Vector2(0,0)
        
        self.speed = PLAYER_DEFAULT_SPEED
        
        self.gravity = GRAVITY
        self.jump_speed = PLAYER_JUMP_SPEED
        
        
    def getInput(self):
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_RIGHT]:
            self.direction.x = 1
        elif keys[pygame.K_LEFT]:
            self.direction.x = -1
        else:
            self.direction.x = 0
            
        if keys[pygame.K_SPACE]:
            self.jump()
            
    def apply_gravity(self):
        self.direction.y += self.gravity
        
        self.rect.y += self.direction.y
        
    def jump(self):
        self.direction.y = self.jump_speed
            
    def update(self):
        self.getInput()
        self.rect.x += self.direction.x * self.speed
        
        self.apply_gravity()
