import pygame, sys

from config.game import SCREEN_WIDTH, SCREEN_HEIGHT
from config.settings import LEVEL_MAP, TILE_SIZE

from models.Level import Level

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
level = Level(LEVEL_MAP, screen)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
    screen.fill('black')
    
    level.run()
    
    pygame.display.update()
    clock.tick(60)
