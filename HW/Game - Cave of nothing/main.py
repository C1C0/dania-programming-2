import pygame, sys

from config.game import SCREEN_WIDTH, SCREEN_HEIGHT
from config.settings import LEVEL_MAP, TILE_SIZE

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
    screen.fill('black')
    
    pygame.display.update()
    clock.tick(60)
